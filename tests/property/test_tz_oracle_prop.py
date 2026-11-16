"""Oracle tests: ``dateutil.tz.gettz`` against ``zoneinfo`` (claims Z-1, Z-2).

Both read the same time zone data: ``dateutil.tz.TZPATH`` is
``zoneinfo.TZPATH``, ``tz_source_context`` points both at one source, and
``zoneinfo`` is always loaded with ``ZoneInfo.no_cache`` so that no cached
instance from another source is used.
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil import tz
from strategies_tz import (
    iana_keys,
    instants_near_transitions,
    wall_times_near_transitions,
)
from tests._common import TZ_SOURCES, tz_source_context, tz_source_skip_reason

UTC = timezone.utc

KNOWN_UPSTREAM = {
    "Africa/Casablanca": "dateutil/dateutil#1667",
    "Africa/El_Aaiun": "dateutil/dateutil#1667",
}

DST_REPORT = "docs/reports/Z-1-dst-inference.md"
# One wall time (fold 0) per key at which dst() differs; utcoffset() and
# tzname() agree there. Winamac and Vilnius differ only with the tzdata
# package, the others with both sources.
DST_EXAMPLES = (
    ("America/Bahia_Banderas", datetime(2010, 4, 4, 4)),
    ("America/Indiana/Tell_City", datetime(1970, 4, 26, 3)),
    ("America/Indiana/Winamac", datetime(2007, 3, 11, 4)),
    ("America/Inuvik", datetime(1979, 4, 29, 4)),
    ("America/Scoresbysund", datetime(1981, 3, 29, 2)),
    ("Asia/Ust-Nera", datetime(1981, 4, 1, 3)),
    ("Europe/Vilnius", datetime(1998, 3, 29, 3)),
    ("Pacific/Rarotonga", datetime(1978, 11, 12, 1)),
)
DST_FINDINGS = {key: DST_REPORT for key, _ in DST_EXAMPLES}


def _skip_unavailable(source):
    reason = tz_source_skip_reason(source)
    if reason is not None:
        pytest.skip(reason)


@pytest.mark.gettz
@pytest.mark.parametrize("source", TZ_SOURCES)
@given(data=st.data())
def test_gettz_matches_zoneinfo(source, data):
    """Z-1: utcoffset, dst and tzname of gettz(key) equal zoneinfo's."""
    _skip_unavailable(source)
    with tz_source_context(source):
        key = data.draw(iana_keys(), label="key")
        wall = data.draw(wall_times_near_transitions(key), label="wall")
        act = wall.replace(tzinfo=tz.gettz(key))
        exp = wall.replace(tzinfo=ZoneInfo.no_cache(key))

        assert act.utcoffset() == exp.utcoffset()
        if key not in KNOWN_UPSTREAM and key not in DST_FINDINGS:
            assert act.dst() == exp.dst()
        assert act.tzname() == exp.tzname()


@pytest.mark.gettz
@pytest.mark.xfail(strict=True, reason=DST_REPORT)
@pytest.mark.parametrize("source", TZ_SOURCES)
@given(case=st.sampled_from(DST_EXAMPLES))
@example(case=DST_EXAMPLES[0])
@example(case=DST_EXAMPLES[1])
@example(case=DST_EXAMPLES[2])
@example(case=DST_EXAMPLES[3])
@example(case=DST_EXAMPLES[4])
@example(case=DST_EXAMPLES[5])
@example(case=DST_EXAMPLES[6])
@example(case=DST_EXAMPLES[7])
def test_gettz_dst_matches_zoneinfo_examples(source, case):
    """Z-1, dst() at the pinned findings that the generic test leaves out."""
    _skip_unavailable(source)
    key, wall = case
    with tz_source_context(source):
        act = wall.replace(tzinfo=tz.gettz(key))
        exp = wall.replace(tzinfo=ZoneInfo.no_cache(key))

        assert act.dst() == exp.dst()


@pytest.mark.gettz
@pytest.mark.parametrize("source", TZ_SOURCES)
@given(data=st.data())
def test_gettz_round_trip_matches_zoneinfo(source, data):
    """Z-2: UTC -> gettz(key) -> UTC is the identity; the wall time and fold
    equal zoneinfo's."""
    _skip_unavailable(source)
    with tz_source_context(source):
        key = data.draw(iana_keys(), label="key")
        dt = data.draw(instants_near_transitions(key), label="dt")
        local = dt.astimezone(tz.gettz(key))
        exp = dt.astimezone(ZoneInfo.no_cache(key))

        assert local.astimezone(UTC) == dt
        assert local.replace(tzinfo=None) == exp.replace(tzinfo=None)
        assert local.fold == exp.fold


@pytest.mark.gettz
@pytest.mark.xfail(
    strict=False, reason="dateutil/dateutil#1667; depends on tz data version"
)
@pytest.mark.parametrize("source", TZ_SOURCES)
@pytest.mark.parametrize("key", sorted(KNOWN_UPSTREAM))
@pytest.mark.parametrize(
    "dt",
    [datetime(2100, 1, 1, tzinfo=UTC), datetime(2400, 1, 1, tzinfo=UTC)],
)
def test_known_upstream_dst(source, key, dt):
    _skip_unavailable(source)
    with tz_source_context(source):
        act = dt.astimezone(tz.gettz(key))
        exp = dt.astimezone(ZoneInfo.no_cache(key))

        assert act.dst() == exp.dst()
