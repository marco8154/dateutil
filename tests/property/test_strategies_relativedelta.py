"""Self-tests for the shared ``relativedelta`` strategies."""

from __future__ import annotations

from datetime import datetime, timedelta

import pytest
from hypothesis import find, given

from dateutil.relativedelta import relativedelta

from strategies_relativedelta import (
    absolute_kwargs,
    base_datetimes,
    relative_kwargs,
    relative_time_kwargs,
)

_RELATIVE_TIME = ("weeks", "days", "hours", "minutes", "seconds", "microseconds")
_RELATIVE_ALL = _RELATIVE_TIME + ("years", "months")
_ABSOLUTE = ("year", "month", "day", "hour", "minute", "second", "microsecond")

_TIME_RANGES = {
    "weeks": (-520, 520),
    "days": (-3650, 3650),
    "hours": (-87600, 87600),
    "minutes": (-10**6, 10**6),
    "seconds": (-10**7, 10**7),
    "microseconds": (-10**9, 10**9),
}
_CALENDAR_RANGES = {"years": (-50, 50), "months": (-600, 600)}
_ABSOLUTE_RANGES = {
    "year": (1900, 2100),
    "month": (1, 12),
    "day": (1, 31),
    "hour": (0, 23),
    "minute": (0, 59),
    "second": (0, 59),
    "microsecond": (0, 999999),
}


def _check_int_ranges(kw, ranges):
    for key, value in kw.items():
        assert type(value) is int, (key, value, type(value))
        lo, hi = ranges[key]
        assert lo <= value <= hi, (key, value, lo, hi)


@given(kw=relative_time_kwargs())
def test_relative_time_kwargs_shape(kw):
    assert kw
    assert set(kw) <= set(_RELATIVE_TIME)
    _check_int_ranges(kw, _TIME_RANGES)


@given(kw=relative_time_kwargs())
def test_relative_time_kwargs_builds_timedelta(kw):
    timedelta(**kw)


@given(kw=relative_kwargs())
def test_relative_kwargs_shape(kw):
    assert kw
    assert set(kw) <= set(_RELATIVE_ALL)
    _check_int_ranges(kw, {**_TIME_RANGES, **_CALENDAR_RANGES})
    assert "weekday" not in kw


@given(kw=relative_kwargs(fractional=True))
def test_relative_kwargs_fractional(kw):
    assert kw
    assert set(kw) <= set(_RELATIVE_ALL)
    assert "weekday" not in kw
    for key, value in kw.items():
        if key in ("years", "months"):
            assert type(value) is int, (key, value)
            lo, hi = _CALENDAR_RANGES[key]
            assert lo <= value <= hi
        elif key in ("days", "hours", "minutes"):
            assert type(value) is float, (key, value, type(value))
            assert (value * 4).is_integer(), (key, value)
            lo, hi = _TIME_RANGES[key]
            assert lo <= value <= hi
        else:
            assert type(value) is int, (key, value)
            lo, hi = _TIME_RANGES[key]
            assert lo <= value <= hi


@given(kw=absolute_kwargs())
def test_absolute_kwargs_shape(kw):
    assert kw
    assert set(kw) <= set(_ABSOLUTE)
    assert "weekday" not in kw
    _check_int_ranges(kw, _ABSOLUTE_RANGES)


@given(dt=base_datetimes(28))
def test_base_datetimes_28_never_past_month_end(dt):
    assert 1900 <= dt.year <= 2100
    assert dt.day <= 28


@given(dt=base_datetimes())
def test_base_datetimes_bounds(dt):
    assert 1900 <= dt.year <= 2100


@given(dt=base_datetimes(), kw=relative_kwargs())
def test_add_relativedelta_never_overflows(dt, kw):
    try:
        result = dt + relativedelta(**kw)
    except (OverflowError, ValueError) as exc:  # pragma: no cover
        raise AssertionError(
            f"dt + relativedelta({kw!r}) raised {type(exc).__name__} for {dt!r}"
        )
    assert isinstance(result, datetime)


@pytest.mark.parametrize(
    "strategy",
    [relative_time_kwargs, relative_kwargs, absolute_kwargs],
)
def test_every_strategy_can_draw(strategy):
    find(strategy(), lambda _: True)
