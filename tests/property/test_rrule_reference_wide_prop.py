"""Wider oracle test for claim R-7 of ``dateutil.rrule``.

Covers what ``test_rrule_reference_prop.py`` does not reach: several
BYHOUR/BYMINUTE/BYSECOND values, ordinal BYDAY terms, several weekdays,
``count``, YEARLY without BYMONTH and ``dtstart`` from 1890 to 2210.
"""
import calendar
from datetime import date, datetime

import hypothesis
import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.rrule import DAILY, MONTHLY, WEEKLY, YEARLY, rrule, weekday

from rrule_reference import expand

NAMES = {YEARLY: "YEARLY", MONTHLY: "MONTHLY", WEEKLY: "WEEKLY", DAILY: "DAILY"}
FILTER_KEYS = ("bymonth", "bymonthday", "byweekday", "byhour", "byminute", "bysecond")


@st.composite
def _with_extras(draw, anchor, domain, max_extra):
    """``None`` or a sorted list holding *anchor* plus 0-*max_extra* other values."""
    if not draw(st.booleans()):
        return None
    extra = draw(st.lists(domain.filter(lambda v: v != anchor), max_size=max_extra,
                          unique=True))
    return sorted((anchor, *extra), key=lambda v: (v if isinstance(v, tuple) else (v, 0)))


def _ordinal_terms(max_n):
    return st.tuples(
        st.integers(0, 6),
        st.integers(1, max_n).flatmap(lambda n: st.sampled_from([n, -n])),
    )


def _ordinal_anchor(dtstart, yearly_scope, from_end):
    """The ``(weekday, n)`` term that selects ``dtstart`` within its month or year."""
    if yearly_scope:
        start = date(dtstart.year, 1, 1)
        length = 366 if calendar.isleap(dtstart.year) else 365
    else:
        start = date(dtstart.year, dtstart.month, 1)
        length = calendar.monthrange(dtstart.year, dtstart.month)[1]
    index = (dtstart.date() - start).days
    if from_end:
        return dtstart.weekday(), -((length - 1 - index) // 7 + 1)
    return dtstart.weekday(), index // 7 + 1


@st.composite
def wide_rrule_kwargs(draw):
    freq = draw(st.sampled_from(list(NAMES)))
    dtstart = draw(st.datetimes(min_value=datetime(1890, 1, 1),
                                max_value=datetime(2210, 12, 31, 23, 59, 59))
                   .map(lambda dt: dt.replace(microsecond=0)))
    kw = {
        "freq": freq,
        "dtstart": dtstart,
        "interval": draw(st.integers(1, 4)),
        "count": draw(st.integers(1, 50)),
        "wkst": draw(st.none() | st.integers(0, 6)),
    }
    kw["bymonth"] = draw(_with_extras(dtstart.month, st.integers(1, 12), 2))
    if freq == WEEKLY:
        kw["bymonthday"] = None
    else:
        monthday = draw(st.sampled_from([dtstart.day, dtstart.day - 32]))
        kw["bymonthday"] = draw(_with_extras(
            monthday, st.integers(1, 31) | st.integers(-31, -1), 1))
    if freq in (WEEKLY, DAILY) or draw(st.booleans()):
        kw["byweekday"] = draw(_with_extras(dtstart.weekday(), st.integers(0, 6), 2))
    else:
        yearly_scope = freq == YEARLY and not kw["bymonth"]
        max_n = 53 if yearly_scope else 5
        anchor = _ordinal_anchor(dtstart, yearly_scope, draw(st.booleans()))
        kw["byweekday"] = draw(_with_extras(anchor, _ordinal_terms(max_n), 2))
    kw["byhour"] = draw(_with_extras(dtstart.hour, st.integers(0, 23), 2))
    kw["byminute"] = draw(_with_extras(dtstart.minute, st.integers(0, 59), 2))
    kw["bysecond"] = draw(_with_extras(dtstart.second, st.integers(0, 59), 2))
    return kw


def _rrule_kw(kw):
    kw = dict(kw)
    if kw["byweekday"] is not None:
        kw["byweekday"] = [weekday(*t) if isinstance(t, tuple) else t
                           for t in kw["byweekday"]]
    return kw


def _expected(kw):
    return expand(
        NAMES[kw["freq"]],
        kw["dtstart"],
        interval=kw["interval"],
        count=kw["count"],
        wkst=0 if kw["wkst"] is None else kw["wkst"],
        **{key: kw[key] for key in FILTER_KEYS},
    )


def _rule(freq, dtstart, count, interval=1, wkst=None, **filters):
    kw = dict.fromkeys(FILTER_KEYS)
    kw.update(freq=freq, dtstart=dtstart, count=count, interval=interval,
              wkst=wkst, **filters)
    return kw


PIN_DAILY_BYHOUR = _rule(DAILY, datetime(2023, 5, 1, 9), 4, byhour=[9, 17])

# 2024-01-01 is the first Monday; the last Friday adds days to it.
PIN_MONTHLY_LAST_FRIDAY = _rule(
    MONTHLY, datetime(2024, 1, 1, 8), 6, byweekday=[(0, 1), (4, -1)])

# BYDAY=MO,-1FR: plain and ordinal terms in one list.
PIN_MONTHLY_MIXED_BYDAY = _rule(
    MONTHLY, datetime(2024, 1, 1, 8), 6, byweekday=[0, (4, -1)])

PIN_YEARLY_BYMONTHDAY_NO_BYMONTH = _rule(
    YEARLY, datetime(2020, 3, 15, 10), 5, bymonthday=[15])

# 2100 is not a leap year, so interval 4 skips it.
PIN_YEARLY_FEB_29 = _rule(YEARLY, datetime(2096, 2, 29, 9), 3, interval=4)

# Each pin with the feature it is named for removed.
PINS = {
    "daily_byhour": (PIN_DAILY_BYHOUR, {"byhour": None}),
    "monthly_last_friday": (PIN_MONTHLY_LAST_FRIDAY, {"byweekday": [(0, 1)]}),
    "yearly_bymonthday": (PIN_YEARLY_BYMONTHDAY_NO_BYMONTH, {"bymonth": [3]}),
}


@pytest.mark.rrule
@example(kw=PIN_DAILY_BYHOUR)
@example(kw=PIN_MONTHLY_LAST_FRIDAY)
@example(kw=PIN_YEARLY_BYMONTHDAY_NO_BYMONTH)
@example(kw=PIN_YEARLY_FEB_29)
@given(kw=wide_rrule_kwargs())
def test_rrule_matches_reference_wide(kw):
    try:
        expected = _expected(kw)
    except ValueError:
        hypothesis.assume(False)
    assert list(rrule(**_rrule_kw(kw))) == expected


@pytest.mark.rrule
@pytest.mark.parametrize("name", PINS)
def test_pins_have_two_occurrences(name):
    assert len(_expected(PINS[name][0])) >= 2


@pytest.mark.rrule
@pytest.mark.parametrize("name", PINS)
def test_pin_depends_on_feature(name):
    kw, without = PINS[name]
    assert _expected(kw) != _expected(dict(kw, **without))


@pytest.mark.rrule
def test_pin_feb_29_dates():
    assert _expected(PIN_YEARLY_FEB_29) == [
        datetime(2096, 2, 29, 9), datetime(2104, 2, 29, 9), datetime(2108, 2, 29, 9)]


@pytest.mark.rrule
@pytest.mark.xfail(strict=True, reason="docs/reports/r7-wide-mixed-byday.md")
def test_rrule_mixed_plain_and_ordinal_byday():
    kw = PIN_MONTHLY_MIXED_BYDAY
    assert len(_expected(kw)) >= 2
    assert list(rrule(**_rrule_kw(kw))) == _expected(kw)
