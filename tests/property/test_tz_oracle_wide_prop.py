"""Oracle tests over 1850-2100: ``dateutil.tz.gettz`` against ``zoneinfo`` (claims Z-1, Z-2).

Both read the same time zone data: ``dateutil.tz.TZPATH`` is
``zoneinfo.TZPATH``, ``tz_source_context`` points both at one source, and
``zoneinfo`` is always loaded with ``ZoneInfo.no_cache`` so that no cached
instance from another source is used.

Transitions are scanned over 1850-2100, so LMT time (before 1900) and the
post-2038 range are covered.
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from dateutil import tz
from strategies_tz import (
    iana_keys,
    instants_near_transitions,
    wall_times_near_transitions,
)
from tests._common import TZ_SOURCES, tz_source_context, tz_source_skip_reason
from test_tz_oracle_prop import DST_FINDINGS, KNOWN_UPSTREAM

UTC = timezone.utc

WIDE_DST_REPORT = "docs/reports/z1w-dst-inference.md"

# ``(key, wall, fold, source)`` cases at which ``dst()`` differs between
# ``dateutil.tz.gettz(key)`` and ``zoneinfo.ZoneInfo(key)`` over 1850-2100.
# ``utcoffset()`` and ``tzname()`` agree at these wall times; only ``dst()``
# is inferred differently. One representative case per (key, source), found by
# scanning every transition wall time (both folds) of every key against both
# data sources. W-SU is included only under ``tzdata``: under ``tzpath`` the
# key does not exist (``gettz("W-SU")`` is None), so it cannot be compared.
WIDE_DST_CASES = [
    ('America/Bahia_Banderas', datetime(2010, 4, 4, 4, 0), 0, 'tzpath'),
    ('America/Coyhaique', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzpath'),
    ('America/Indiana/Tell_City', datetime(1969, 4, 27, 4, 0), 0, 'tzpath'),
    ('America/Inuvik', datetime(1979, 4, 29, 4, 0), 0, 'tzpath'),
    ('America/Montevideo', datetime(1923, 10, 1, 1, 0), 0, 'tzpath'),
    ('America/Punta_Arenas', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzpath'),
    ('America/Santiago', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzpath'),
    ('America/Scoresbysund', datetime(1981, 3, 29, 2, 0), 0, 'tzpath'),
    ('Asia/Hong_Kong', datetime(1941, 10, 1, 3, 30), 1, 'tzpath'),
    ('Asia/Ust-Nera', datetime(1981, 4, 1, 3, 0), 0, 'tzpath'),
    ('Atlantic/Azores', datetime(1942, 4, 26, 0, 0), 0, 'tzpath'),
    ('Atlantic/Madeira', datetime(1942, 4, 26, 0, 0), 0, 'tzpath'),
    ('Europe/Amsterdam', datetime(1940, 5, 16, 1, 40), 0, 'tzpath'),
    ('Europe/Belfast', datetime(1941, 5, 4, 3, 0), 0, 'tzpath'),
    ('Europe/Berlin', datetime(1945, 5, 24, 3, 0), 0, 'tzpath'),
    ('Europe/Gibraltar', datetime(1941, 5, 4, 3, 0), 0, 'tzpath'),
    ('Europe/Guernsey', datetime(1947, 4, 13, 3, 0), 0, 'tzpath'),
    ('Europe/Isle_of_Man', datetime(1941, 5, 4, 3, 0), 0, 'tzpath'),
    ('Europe/Jersey', datetime(1947, 4, 13, 3, 0), 0, 'tzpath'),
    ('Europe/Kyiv', datetime(1941, 9, 19, 23, 0), 1, 'tzpath'),
    ('Europe/Lisbon', datetime(1942, 4, 26, 0, 0), 0, 'tzpath'),
    ('Europe/London', datetime(1941, 5, 4, 3, 0), 0, 'tzpath'),
    ('Europe/Madrid', datetime(1938, 5, 1, 0, 0), 0, 'tzpath'),
    ('Europe/Minsk', datetime(1941, 6, 27, 23, 0), 1, 'tzpath'),
    ('Europe/Moscow', datetime(1921, 3, 21, 0, 0), 0, 'tzpath'),
    ('Europe/Riga', datetime(1941, 6, 30, 23, 0), 1, 'tzpath'),
    ('Europe/Simferopol', datetime(1941, 10, 31, 23, 0), 1, 'tzpath'),
    ('Europe/Tallinn', datetime(1941, 9, 14, 23, 0), 1, 'tzpath'),
    ('Europe/Vilnius', datetime(1941, 6, 23, 23, 0), 1, 'tzpath'),
    ('Pacific/Rarotonga', datetime(1978, 11, 12, 1, 0), 0, 'tzpath'),
    ('America/Bahia_Banderas', datetime(2010, 4, 4, 4, 0), 0, 'tzdata'),
    ('America/Coyhaique', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzdata'),
    ('America/Indiana/Tell_City', datetime(1969, 4, 27, 4, 0), 0, 'tzdata'),
    ('America/Indiana/Winamac', datetime(2007, 3, 11, 4, 0), 0, 'tzdata'),
    ('America/Inuvik', datetime(1979, 4, 29, 4, 0), 0, 'tzdata'),
    ('America/Montevideo', datetime(1923, 10, 1, 1, 0), 0, 'tzdata'),
    ('America/Punta_Arenas', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzdata'),
    ('America/Santiago', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzdata'),
    ('America/Scoresbysund', datetime(1981, 3, 29, 2, 0), 0, 'tzdata'),
    ('Arctic/Longyearbyen', datetime(1945, 5, 24, 3, 0), 0, 'tzdata'),
    ('Asia/Hong_Kong', datetime(1941, 10, 1, 3, 30), 1, 'tzdata'),
    ('Asia/Ust-Nera', datetime(1981, 4, 1, 3, 0), 0, 'tzdata'),
    ('Atlantic/Azores', datetime(1942, 4, 26, 0, 0), 0, 'tzdata'),
    ('Atlantic/Jan_Mayen', datetime(1945, 5, 24, 3, 0), 0, 'tzdata'),
    ('Atlantic/Madeira', datetime(1942, 4, 26, 0, 0), 0, 'tzdata'),
    ('Chile/Continental', datetime(1927, 9, 1, 0, 42, 45), 0, 'tzdata'),
    ('Europe/Belfast', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Europe/Berlin', datetime(1945, 5, 24, 3, 0), 0, 'tzdata'),
    ('Europe/Copenhagen', datetime(1945, 5, 24, 3, 0), 0, 'tzdata'),
    ('Europe/Gibraltar', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Europe/Guernsey', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Europe/Isle_of_Man', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Europe/Jersey', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Europe/Kiev', datetime(1941, 9, 19, 23, 0), 1, 'tzdata'),
    ('Europe/Kyiv', datetime(1941, 9, 19, 23, 0), 1, 'tzdata'),
    ('Europe/Lisbon', datetime(1942, 4, 26, 0, 0), 0, 'tzdata'),
    ('Europe/London', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Europe/Madrid', datetime(1938, 5, 1, 0, 0), 0, 'tzdata'),
    ('Europe/Minsk', datetime(1941, 6, 27, 23, 0), 1, 'tzdata'),
    ('Europe/Moscow', datetime(1921, 3, 21, 0, 0), 0, 'tzdata'),
    ('Europe/Oslo', datetime(1945, 5, 24, 3, 0), 0, 'tzdata'),
    ('Europe/Riga', datetime(1941, 6, 30, 23, 0), 1, 'tzdata'),
    ('Europe/Simferopol', datetime(1941, 10, 31, 23, 0), 1, 'tzdata'),
    ('Europe/Stockholm', datetime(1945, 5, 24, 3, 0), 0, 'tzdata'),
    ('Europe/Uzhgorod', datetime(1941, 9, 19, 23, 0), 1, 'tzdata'),
    ('Europe/Vilnius', datetime(1941, 6, 23, 23, 0), 1, 'tzdata'),
    ('Europe/Zaporozhye', datetime(1941, 9, 19, 23, 0), 1, 'tzdata'),
    ('GB', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('GB-Eire', datetime(1941, 5, 4, 3, 0), 0, 'tzdata'),
    ('Hongkong', datetime(1941, 10, 1, 3, 30), 1, 'tzdata'),
    ('Pacific/Rarotonga', datetime(1978, 11, 12, 1, 0), 0, 'tzdata'),
    ('Portugal', datetime(1942, 4, 26, 0, 0), 0, 'tzdata'),
    ('W-SU', datetime(1921, 3, 21, 0, 0), 0, 'tzdata'),
    ('WET', datetime(1942, 4, 26, 0, 0), 0, 'tzdata'),
]

WIDE_DST_KEYS = {case[0] for case in WIDE_DST_CASES}


def _skip_unavailable(source):
    reason = tz_source_skip_reason(source)
    if reason is not None:
        pytest.skip(reason)


@pytest.mark.gettz
@pytest.mark.parametrize("source", TZ_SOURCES)
@settings(max_examples=120)
@given(data=st.data())
def test_gettz_matches_zoneinfo_wide(source, data):
    """Z-1 over 1850-2100: utcoffset, dst and tzname of gettz(key) equal
    zoneinfo's, for fold=0 and fold=1.

    ``dst()`` is not compared for keys in KNOWN_UPSTREAM, DST_FINDINGS or
    WIDE_DST_KEYS; those are covered by pinned strict-xfail cases instead.
    """
    _skip_unavailable(source)
    with tz_source_context(source):
        key = data.draw(iana_keys(), label="key")
        wall = data.draw(
            wall_times_near_transitions(key, 1850, 2100), label="wall"
        )
        act = wall.replace(tzinfo=tz.gettz(key))
        exp = wall.replace(tzinfo=ZoneInfo.no_cache(key))

        assert act.utcoffset() == exp.utcoffset()
        if (
            key not in KNOWN_UPSTREAM
            and key not in DST_FINDINGS
            and key not in WIDE_DST_KEYS
        ):
            assert act.dst() == exp.dst()
        assert act.tzname() == exp.tzname()


@pytest.mark.gettz
@pytest.mark.parametrize("source", TZ_SOURCES)
@settings(max_examples=120)
@given(data=st.data())
def test_astimezone_roundtrip_wide(source, data):
    """Z-2 over 1850-2100: ``dt.astimezone(z).astimezone(UTC) == dt``."""
    _skip_unavailable(source)
    with tz_source_context(source):
        key = data.draw(iana_keys(), label="key")
        dt = data.draw(
            instants_near_transitions(key, 1850, 2100), label="dt"
        )
        local = dt.astimezone(tz.gettz(key))

        assert local.astimezone(UTC) == dt


@pytest.mark.gettz
@pytest.mark.parametrize(
    "key,wall,fold,source",
    [
        pytest.param(
            *case,
            marks=pytest.mark.xfail(strict=True, reason=WIDE_DST_REPORT),
            id=f"{case[0]}-{case[3]}",
        )
        for case in WIDE_DST_CASES
    ],
)
def test_gettz_dst_wide_examples(key, wall, fold, source):
    """Z-1 over 1850-2100: ``dst()`` at the pinned wide findings.

    Each case is its own strict xfail so a partial upstream fix stays
    visible instead of being hidden behind an all-or-nothing test.
    """
    _skip_unavailable(source)
    with tz_source_context(source):
        act = wall.replace(fold=fold, tzinfo=tz.gettz(key))
        exp = wall.replace(fold=fold, tzinfo=ZoneInfo.no_cache(key))

        assert act.dst() == exp.dst()
