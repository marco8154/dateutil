from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, available_timezones

import pytest
from hypothesis import find, given

from strategies_tz import (
    iana_keys,
    instants_near_transitions,
    transitions,
    utc_datetimes,
    wall_times_near_transitions,
)

UTC = timezone.utc

_TRANSITION_KEYS = (
    "Europe/Berlin",
    "America/New_York",
    "Australia/Lord_Howe",
    "Asia/Kolkata",
    "America/Sao_Paulo",
)
_NON_ZONES = {"localtime", "posixrules", "Factory"}
_AVAILABLE = set(available_timezones())


def _attrs(dt, tzi):
    local = dt.astimezone(tzi)
    return (local.utcoffset(), local.dst(), local.tzname())


def _is_ambiguous(wall):
    # An ambiguous wall time resolves to the earlier instant with fold=0.
    # The instants are compared in UTC: two datetimes sharing one tzinfo
    # object would otherwise compare by wall time fields alone.
    tzi = ZoneInfo("Europe/Berlin")
    first = wall.replace(fold=0, tzinfo=tzi).astimezone(UTC)
    second = wall.replace(fold=1, tzinfo=tzi).astimezone(UTC)
    return first < second


def _is_imaginary(wall):
    # An imaginary wall time keeps the pre-gap offset with fold=0, which puts
    # it after where fold=1 resolves it.
    tzi = ZoneInfo("Europe/Berlin")
    first = wall.replace(fold=0, tzinfo=tzi).astimezone(UTC)
    second = wall.replace(fold=1, tzinfo=tzi).astimezone(UTC)
    return first > second


@pytest.mark.gettz
def test_transitions_berlin_2021():
    assert transitions("Europe/Berlin", 2021, 2021) == (
        datetime(2021, 3, 28, 1, 0, tzinfo=UTC),
        datetime(2021, 10, 31, 1, 0, tzinfo=UTC),
    )


@pytest.mark.gettz
def test_transitions_utc_has_none():
    assert transitions("Etc/UTC") == ()


@pytest.mark.gettz
@pytest.mark.parametrize("key", _TRANSITION_KEYS)
def test_transitions_are_transitions(key):
    tzi = ZoneInfo(key)
    for instant in transitions(key):
        before = _attrs(instant - timedelta(microseconds=1), tzi)
        assert before != _attrs(instant, tzi), (key, instant)


@pytest.mark.gettz
def test_instants_reach_exact_transitions():
    ts = set(transitions("Europe/Berlin"))
    found = find(instants_near_transitions("Europe/Berlin"), lambda dt: dt in ts)
    assert found in ts


@pytest.mark.gettz
def test_instants_reach_one_microsecond_around_transitions():
    ts = transitions("Europe/Berlin")
    after = {t + timedelta(microseconds=1) for t in ts}
    before = {t - timedelta(microseconds=1) for t in ts}
    strategy = instants_near_transitions("Europe/Berlin")
    assert find(strategy, lambda dt: dt in after) in after
    assert find(strategy, lambda dt: dt in before) in before


@pytest.mark.gettz
@given(dt=instants_near_transitions("Europe/Berlin"))
def test_instants_near_transitions_are_within_window(dt):
    assert dt.tzinfo is UTC
    near = [t for t in transitions("Europe/Berlin") if abs(dt - t) <= timedelta(days=2)]
    assert near


@pytest.mark.gettz
@given(dt=instants_near_transitions("Asia/Kolkata"))
def test_instants_without_transitions_fall_back(dt):
    assert dt.tzinfo is UTC
    assert 1900 <= dt.year <= 2100


@pytest.mark.gettz
@given(dt=wall_times_near_transitions("Europe/Berlin"))
def test_wall_times_are_naive_with_fold(dt):
    assert dt.tzinfo is None
    assert dt.fold in (0, 1)
    berlin = ZoneInfo("Europe/Berlin")
    near = [
        t.astimezone(berlin).replace(tzinfo=None)
        for t in transitions("Europe/Berlin")
    ]
    assert any(abs(dt - w) <= timedelta(days=2) for w in near)


@pytest.mark.gettz
@given(dt=wall_times_near_transitions("Asia/Kolkata"))
def test_wall_times_without_transitions_fall_back(dt):
    assert dt.tzinfo is None
    assert dt.fold in (0, 1)
    assert 1900 <= dt.year <= 2100


@pytest.mark.gettz
def test_wall_times_reach_an_ambiguous_time():
    wall = find(wall_times_near_transitions("Europe/Berlin"), _is_ambiguous)
    assert wall.tzinfo is None


@pytest.mark.gettz
def test_wall_times_reach_an_imaginary_time():
    wall = find(wall_times_near_transitions("Europe/Berlin"), _is_imaginary)
    assert wall.tzinfo is None


@pytest.mark.gettz
@given(key=iana_keys())
def test_iana_keys_are_real_zones(key):
    assert key in _AVAILABLE
    assert key not in _NON_ZONES


@pytest.mark.gettz
@given(dt=utc_datetimes())
def test_utc_datetimes_are_utc_aware(dt):
    assert dt.tzinfo is UTC
    assert 1900 <= dt.year <= 2100


@pytest.mark.gettz
@given(dt=utc_datetimes(min_year=2000, max_year=2001))
def test_utc_datetimes_honours_bounds(dt):
    assert 2000 <= dt.year <= 2001
