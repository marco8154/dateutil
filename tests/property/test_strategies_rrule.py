"""Tests for the shared ``rrule`` strategies in ``strategies_rrule.py``."""

import calendar
from datetime import datetime

import pytest
from hypothesis import find, given, strategies as st

import strategies_rrule
from dateutil.rrule import (
    DAILY,
    HOURLY,
    MINUTELY,
    MONTHLY,
    SECONDLY,
    WEEKLY,
    YEARLY,
    rrule,
)
from strategies_rrule import FILTER_KEYS, UNTIL_WINDOW, rrule_kwargs

FREQS = (YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY)
EXPECTED_KEYS = {"freq", "dtstart", "interval", "until", "wkst", *FILTER_KEYS}

_MIN_DATE = datetime(1990, 1, 1)
_MAX_DATE = datetime(2030, 12, 31, 23, 59, 59)


def _anchor_values(key, start):
    """The value(s) of ``start`` that a set filter for *key* must contain."""
    if key == "bymonth":
        return {start.month}
    if key == "bymonthday":
        days = calendar.monthrange(start.year, start.month)[1]
        return {start.day, start.day - days - 1}
    if key == "byweekday":
        return {start.weekday()}
    if key == "byhour":
        return {start.hour}
    if key == "byminute":
        return {start.minute}
    return {start.second}


def _domain(key):
    if key == "bymonth":
        return range(1, 13)
    if key == "bymonthday":
        return list(range(-31, 0)) + list(range(1, 32))
    if key == "byweekday":
        return range(7)
    if key == "byhour":
        return range(24)
    if key == "byminute":
        return range(60)
    return range(60)


@pytest.mark.rrule
@given(kw=rrule_kwargs())
def test_keys_exact(kw):
    assert set(kw) == EXPECTED_KEYS


@pytest.mark.rrule
@given(kw=rrule_kwargs())
def test_dtstart_and_interval_bounds(kw):
    assert _MIN_DATE <= kw["dtstart"] <= _MAX_DATE
    assert kw["dtstart"].microsecond == 0
    assert 1 <= kw["interval"] <= 4
    assert kw["wkst"] is None or 0 <= kw["wkst"] <= 6
    assert kw["freq"] in FREQS


@pytest.mark.rrule
@given(kw=rrule_kwargs())
def test_until_matches_window(kw):
    assert kw["until"] - kw["dtstart"] == UNTIL_WINDOW[kw["freq"]]


@pytest.mark.rrule
@given(kw=rrule_kwargs())
def test_filters_are_sorted_unique_in_range_and_anchored(kw):
    start = kw["dtstart"]
    for key in FILTER_KEYS:
        values = kw[key]
        if values is None:
            continue
        assert values == sorted(values), (key, values)
        assert len(values) == len(set(values)), (key, values)
        assert 1 <= len(values) <= 4, (key, values)
        assert all(value in _domain(key) for value in values), (key, values)
        assert _anchor_values(key, start).intersection(values), (key, values, start)


@pytest.mark.rrule
@given(kw=rrule_kwargs())
def test_rule_yields_at_most_1000_occurrences(kw):
    assert len(list(rrule(**kw))) <= 1000


@pytest.mark.rrule
def test_every_frequency_can_be_generated():
    for freq in FREQS:
        found = find(rrule_kwargs(), lambda kw: kw["freq"] == freq)
        assert found["freq"] == freq


@pytest.mark.rrule
def test_every_filter_can_be_set():
    for key in FILTER_KEYS:
        found = find(rrule_kwargs(), lambda kw: kw[key] is not None)
        assert found[key] is not None


@pytest.mark.rrule
def test_yearly_bymonthday_can_be_generated():
    found = find(
        rrule_kwargs(),
        lambda kw: kw["freq"] == YEARLY and kw["bymonthday"] is not None,
    )
    assert found["freq"] == YEARLY
    assert found["bymonthday"] is not None
    assert found["bymonth"] is not None


@pytest.mark.rrule
def test_yearly_byweekday_can_be_generated():
    found = find(
        rrule_kwargs(),
        lambda kw: kw["freq"] == YEARLY and kw["byweekday"] is not None,
    )
    assert found["freq"] == YEARLY
    assert found["byweekday"] is not None
    assert found["bymonth"] is not None
    assert len(found["bymonth"]) == 1


@pytest.mark.rrule
def test_monthly_byweekday_can_be_generated():
    found = find(
        rrule_kwargs(),
        lambda kw: kw["freq"] == MONTHLY and kw["byweekday"] is not None,
    )
    assert found["freq"] == MONTHLY
    assert found["byweekday"] is not None
    assert found["bymonth"] is not None
    assert len(found["bymonth"]) <= 2


# 2000-01-01: Saturday, start of a 31-day month, midnight time anchors.
_WORST_DTSTART = datetime(2000, 1, 1)


def _worst_case_kwargs(freq, **filters):
    """``interval=1`` rule with the largest anchored filter lists that
    ``rrule_kwargs()`` can generate for *freq*."""
    kwargs = {
        "freq": freq,
        "dtstart": _WORST_DTSTART,
        "interval": 1,
        "until": _WORST_DTSTART + UNTIL_WINDOW[freq],
        "wkst": None,
        "bymonth": None,
        "bymonthday": None,
        "byweekday": None,
        "byhour": [0],
        "byminute": [0],
        "bysecond": [0],
    }
    kwargs.update(filters)
    return kwargs


@pytest.mark.rrule
@pytest.mark.parametrize(
    "freq,filters",
    [
        # The three gated combinations (R-2..R-5 need them generatable):
        (YEARLY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1]}),
        (YEARLY, {"bymonth": [1], "byweekday": [5]}),
        (MONTHLY, {"bymonth": [1, 2], "byweekday": [5]}),
        # Largest unbounded lists per frequency.
        (YEARLY, {"bymonth": [1, 2, 3, 4]}),
        (MONTHLY, {"bymonthday": [1]}),
        (MONTHLY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1]}),
        (WEEKLY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1, 2, 3, 4],
                  "byweekday": [5]}),
        (DAILY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1, 2, 3, 4],
                 "byweekday": [2, 3, 4, 5]}),
        (HOURLY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1, 2, 3, 4],
                  "byweekday": [2, 3, 4, 5], "byhour": [0, 1, 2, 3]}),
        (MINUTELY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1, 2, 3, 4],
                    "byweekday": [2, 3, 4, 5], "byhour": [0, 1, 2, 3],
                    "byminute": [0, 1, 2, 3]}),
        (SECONDLY, {"bymonth": [1, 2, 3, 4], "bymonthday": [1, 2, 3, 4],
                    "byweekday": [2, 3, 4, 5], "byhour": [0, 1, 2, 3],
                    "byminute": [0, 1, 2, 3], "bysecond": [0, 1, 2, 3]}),
    ],
)
def test_worst_case_lists_yield_at_most_1000_occurrences(freq, filters):
    assert len(list(rrule(**_worst_case_kwargs(freq, **filters)))) <= 1000
