"""Claim Z-3: datetime_exists, datetime_ambiguous and resolve_imaginary agree
with the definitions computed from zoneinfo on the same time zone data."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pytest
from hypothesis import HealthCheck, example, given, settings
from hypothesis import strategies as st

from dateutil import tz
from strategies_tz import iana_keys, wall_times_near_transitions

# (key, naive wall time) pairs, drawn as one value so @example can pin both.
# The keys are listed at draw time, inside the tz_source context, so that only
# keys of the active data source are drawn.
CASES = (
    st.just(None)
    .flatmap(lambda _: iana_keys())
    .flatmap(lambda key: st.tuples(st.just(key), wall_times_near_transitions(key)))
)

PINS = [
    ("Europe/Berlin", datetime(2021, 3, 28, 2, 30)),  # gap
    ("Europe/Berlin", datetime(2021, 10, 31, 2, 30)),  # ambiguous
    ("Australia/Lord_Howe", datetime(2021, 10, 3, 2, 15)),  # 30-minute gap
    ("America/New_York", datetime(2021, 11, 7, 1, 30)),  # ambiguous
]


def pinned(test):
    for case in reversed(PINS):
        test = example(case=case)(test)
    return test


def property_test(test):
    # tz_source is function-scoped on purpose: it switches the data source
    # once per test function, which is all these tests need.
    return pytest.mark.gettz(
        given(case=CASES)(
            settings(
                suppress_health_check=[HealthCheck.function_scoped_fixture]
            )(pinned(test))
        )
    )


def _round_trip(wall, zi):
    aware = wall.replace(tzinfo=zi, fold=0)
    local = aware.astimezone(timezone.utc).astimezone(zi)
    return local.replace(tzinfo=None, fold=0)


def _exists(wall, zi):
    return _round_trip(wall, zi) == wall.replace(fold=0)


def _ambiguous(wall, zi):
    offset_0 = wall.replace(tzinfo=zi, fold=0).utcoffset()
    offset_1 = wall.replace(tzinfo=zi, fold=1).utcoffset()
    return _exists(wall, zi) and offset_0 != offset_1


def _zones(key):
    zone = tz.gettz(key)
    assert zone is not None, key
    return zone, ZoneInfo.no_cache(key)


@property_test
def test_datetime_exists_matches_zoneinfo(tz_source, case):
    key, wall = case
    zone, zi = _zones(key)
    assert tz.datetime_exists(wall, tz=zone) == _exists(wall, zi)


@property_test
def test_datetime_ambiguous_matches_zoneinfo(tz_source, case):
    key, wall = case
    zone, zi = _zones(key)
    assert tz.datetime_ambiguous(wall, tz=zone) == _ambiguous(wall, zi)


@property_test
def test_resolve_imaginary_matches_zoneinfo(tz_source, case):
    key, wall = case
    zone, zi = _zones(key)
    resolved = tz.resolve_imaginary(wall.replace(tzinfo=zone))
    assert resolved.replace(tzinfo=None, fold=0) == _round_trip(wall, zi)
