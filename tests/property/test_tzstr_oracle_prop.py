"""Oracle: the POSIX TZ string in the TZif footer against zoneinfo (claim T-2).

Both sides read the same bytes from the pinned ``tzdata`` package: the
expected zone is built with ``zoneinfo.ZoneInfo.from_file`` from those bytes,
so no import of dateutil is on the oracle path and the ``tz_source`` fixture
is not needed here.
"""

import functools
import importlib.resources
import io
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, available_timezones

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil import tz

_UTC = timezone.utc


@functools.lru_cache(maxsize=None)
def _zone_bytes(key):
    try:
        return (
            importlib.resources.files("tzdata.zoneinfo")
            .joinpath(*key.split("/"))
            .read_bytes()
        )
    except FileNotFoundError:
        return None


def footer(key):
    """The POSIX TZ string in the footer of the TZif file for *key*, or None."""
    data = _zone_bytes(key)
    if data is None or not data.startswith(b"TZif"):
        return None
    line = data.rstrip(b"\n").rsplit(b"\n", 1)[-1].decode("ascii")
    return line or None


def _oracle_zone(key):
    return ZoneInfo.from_file(io.BytesIO(_zone_bytes(key)), key=key)


# Footers with a transition time or a negative DST that tzstr misapplies;
# see docs/reports/t2-tzstr-transition-times.md.
KNOWN_DIFFERENCES = [
    ("Asia/Beirut", datetime(2040, 10, 27, 21, 0, tzinfo=_UTC)),
    ("Asia/Gaza", datetime(2040, 3, 24, 0, 0, tzinfo=_UTC)),
    ("Asia/Hebron", datetime(2040, 3, 24, 0, 0, tzinfo=_UTC)),
    ("Asia/Jerusalem", datetime(2040, 3, 23, 0, 0, tzinfo=_UTC)),
    ("Asia/Tel_Aviv", datetime(2040, 3, 23, 0, 0, tzinfo=_UTC)),
    ("Israel", datetime(2040, 3, 23, 0, 0, tzinfo=_UTC)),
    ("Europe/Dublin", datetime(2040, 10, 28, 1, 0, tzinfo=_UTC)),
    ("Eire", datetime(2040, 10, 28, 1, 0, tzinfo=_UTC)),
]
KNOWN = [key for key, _ in KNOWN_DIFFERENCES]

# Footers with <...> abbreviations, which the GNU TZ format allows but tzstr
# rejects; see docs/reports/t2-tzstr-angle-brackets.md.
ALL_KEYS = sorted(available_timezones())
ANGLE = [key for key in ALL_KEYS if footer(key) and "<" in footer(key)]
KEYS = sorted(
    key
    for key in ALL_KEYS
    if footer(key) and key not in ANGLE and key not in KNOWN
)

ANGLE_KEYS = [
    "America/Argentina/Buenos_Aires",
    "America/Santiago",
    "Australia/Lord_Howe",
    "Asia/Dubai",
]


@pytest.mark.tzstr
@given(
    key=st.sampled_from(KEYS),
    u=st.datetimes(
        min_value=datetime(2040, 1, 1),
        max_value=datetime(2099, 12, 31),
        timezones=st.just(_UTC),
    ),
)
# One minute either side of the spring-forward transition of a northern zone.
@example(key="America/New_York", u=datetime(2040, 3, 11, 6, 59, tzinfo=_UTC))
@example(key="America/New_York", u=datetime(2040, 3, 11, 7, 1, tzinfo=_UTC))
# Same for a southern-hemisphere zone (DST starts in October there).
@example(key="Australia/Sydney", u=datetime(2040, 10, 6, 15, 59, tzinfo=_UTC))
@example(key="Australia/Sydney", u=datetime(2040, 10, 6, 16, 1, tzinfo=_UTC))
def test_tzstr_matches_zoneinfo_after_last_transition(key, u):
    # All TZif files in tzdata 2026.6 end their transitions before 2040, so
    # every instant in the range is governed by the footer rule alone.
    tzn = tz.tzstr(footer(key), posix_offset=True)
    assert u.astimezone(tzn).utcoffset() == u.astimezone(_oracle_zone(key)).utcoffset()


@pytest.mark.tzstr
@pytest.mark.xfail(
    strict=True,
    raises=ValueError,
    reason="docs/reports/t2-tzstr-angle-brackets.md",
)
@pytest.mark.parametrize("key", ANGLE_KEYS)
def test_tzstr_angle_bracket_abbreviations(key):
    assert footer(key) is not None and "<" in footer(key)
    tzn = tz.tzstr(footer(key), posix_offset=True)
    zi = _oracle_zone(key)
    for u in (
        datetime(2040, 1, 15, 12, 0, tzinfo=_UTC),
        datetime(2040, 7, 15, 12, 0, tzinfo=_UTC),
    ):
        assert u.astimezone(tzn).utcoffset() == u.astimezone(zi).utcoffset()


@pytest.mark.tzstr
@pytest.mark.xfail(
    strict=True,
    reason="docs/reports/t2-tzstr-transition-times.md",
)
@pytest.mark.parametrize("key,u", KNOWN_DIFFERENCES)
def test_tzstr_known_offset_differences(key, u):
    tzn = tz.tzstr(footer(key), posix_offset=True)
    assert u.astimezone(tzn).utcoffset() == u.astimezone(_oracle_zone(key)).utcoffset()
