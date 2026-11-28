"""Oracle test for claim R-8: ``dateutil.rrule`` with BYSETPOS.

Rules end with ``until`` (``dtstart`` plus up to 731 days). Rules whose
expected result is empty are not compared by the property test: ``rrule``
does not stop at ``until`` when no period selects anything and searches up
to the year 9999. Three fixed cases in ``test_rrule_empty_setpos_cases``
cover them instead.
"""
import calendar
from datetime import date, datetime, timedelta

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
def _position(draw):
    if draw(st.integers(0, 9)) == 0:
        return draw(st.sampled_from([53, -53, 366, -366]))
    return draw(st.integers(1, 3) | st.integers(-3, -1))


@st.composite
def setpos_rrule_kwargs(draw):
    freq = draw(st.sampled_from(list(NAMES)))
    dtstart = draw(st.datetimes(min_value=datetime(1890, 1, 1),
                                max_value=datetime(2210, 12, 31, 23, 59, 59))
                   .map(lambda dt: dt.replace(microsecond=0)))
    wkst = draw(st.none() | st.integers(0, 6))
    if freq == WEEKLY:
        # rrule builds the first week's set from dtstart, not from the week
        # start (docs/reports/r8-weekly-first-week-setpos.md).
        dtstart += timedelta(days=((wkst or 0) - dtstart.weekday()) % 7)
        if dtstart.year > 2210:
            dtstart -= timedelta(days=7)
    kw = {
        "freq": freq,
        "dtstart": dtstart,
        "interval": draw(st.integers(1, 4)),
        "count": None,
        "until": dtstart + timedelta(days=draw(st.integers(0, 731))),
        "wkst": wkst,
    }
    kw["bymonth"] = draw(_with_extras(dtstart.month, st.integers(1, 12), 2))
    if freq == WEEKLY:
        # BYMONTHDAY is N/A at WEEKLY (RFC 5545 table, l. 2450).
        kw["bymonthday"] = None
    else:
        monthday = draw(st.sampled_from([dtstart.day, dtstart.day - 32]))
        kw["bymonthday"] = draw(_with_extras(
            monthday, st.integers(1, 31) | st.integers(-31, -1), 2))
    # Plain or ordinal weekdays only; mixed lists are the R-7 finding
    # (docs/reports/r7-wide-mixed-byday.md).
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
    kw["bysetpos"] = draw(st.lists(_position(), min_size=1, max_size=3, unique=True))
    if all(kw[key] is None for key in FILTER_KEYS):
        # BYSETPOS needs another BYxxx rule part (RFC 5545 l. 2372-2373).
        kw["byhour"] = [dtstart.hour]
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
        until=kw["until"],
        wkst=0 if kw["wkst"] is None else kw["wkst"],
        bysetpos=kw["bysetpos"],
        **{key: kw[key] for key in FILTER_KEYS},
    )


def _rule(freq, dtstart, until, bysetpos, interval=1, wkst=None, **filters):
    kw = dict.fromkeys(FILTER_KEYS)
    kw.update(freq=freq, dtstart=dtstart, until=until, count=None,
              interval=interval, wkst=wkst, bysetpos=bysetpos, **filters)
    return kw


PIN_MONTHLY_LAST_WORKDAY = _rule(
    MONTHLY, datetime(2024, 1, 1, 9), datetime(2024, 6, 30, 9), [-1],
    byweekday=[0, 1, 2, 3, 4])

# RFC 5545 l. 7259: the third instance of TU, WE or TH in each month.
PIN_MONTHLY_THIRD_TU_WE_TH = _rule(
    MONTHLY, datetime(1997, 9, 4, 9), datetime(1997, 12, 31, 9), [3],
    byweekday=[1, 2, 3])

# The first of MO/SU in the week is SU when the week starts on Sunday.
PIN_WEEKLY_WKST_SUNDAY = _rule(
    WEEKLY, datetime(2024, 1, 7, 9), datetime(2024, 2, 29, 9), [1],
    wkst=6, byweekday=[0, 6])

PIN_DAILY_LAST_HOUR = _rule(
    DAILY, datetime(2023, 5, 1, 9), datetime(2023, 5, 5, 9), [-1],
    byhour=[9, 12, 17])

PIN_YEARLY_SECOND_OF_JAN_JUL = _rule(
    YEARLY, datetime(2020, 1, 1, 9), datetime(2023, 12, 31, 9), [2],
    bymonth=[1, 7], bymonthday=[1])

PINS = {
    "monthly_last_workday": PIN_MONTHLY_LAST_WORKDAY,
    "monthly_third_tu_we_th": PIN_MONTHLY_THIRD_TU_WE_TH,
    "weekly_wkst_sunday": PIN_WEEKLY_WKST_SUNDAY,
    "daily_last_hour": PIN_DAILY_LAST_HOUR,
    "yearly_second_of_jan_jul": PIN_YEARLY_SECOND_OF_JAN_JUL,
}


@pytest.mark.rrule
@example(kw=PIN_MONTHLY_LAST_WORKDAY)
@example(kw=PIN_MONTHLY_THIRD_TU_WE_TH)
@example(kw=PIN_WEEKLY_WKST_SUNDAY)
@example(kw=PIN_DAILY_LAST_HOUR)
@example(kw=PIN_YEARLY_SECOND_OF_JAN_JUL)
@given(kw=setpos_rrule_kwargs())
def test_rrule_matches_reference_setpos(kw):
    try:
        expected = _expected(kw)
    except ValueError:
        hypothesis.assume(False)
    if not expected:
        hypothesis.event("empty")
        hypothesis.assume(False)
    hypothesis.event("non-empty")
    assert list(rrule(**_rrule_kw(kw))) == expected


@pytest.mark.rrule
@pytest.mark.parametrize("name", PINS)
def test_setpos_pins_have_two_occurrences(name):
    assert len(_expected(PINS[name])) >= 2


@pytest.mark.rrule
@pytest.mark.parametrize("name", PINS)
def test_setpos_pin_depends_on_bysetpos(name):
    kw = PINS[name]
    assert _expected(kw) != _expected(dict(kw, bysetpos=None))


@pytest.mark.rrule
def test_setpos_pin_depends_on_wkst():
    kw = PIN_WEEKLY_WKST_SUNDAY
    assert _expected(kw) != _expected(dict(kw, wkst=None))


@pytest.mark.rrule
@pytest.mark.parametrize("kw", [
    pytest.param(_rule(MONTHLY, datetime(2025, 1, 1, 9), datetime(2025, 6, 30, 9),
                       [3], bymonthday=[1, 15]), id="monthly"),
    pytest.param(_rule(WEEKLY, datetime(2003, 6, 1, 9), datetime(2003, 7, 31, 9),
                       [-2], byweekday=[3]), id="weekly"),
    pytest.param(_rule(YEARLY, datetime(2025, 1, 1, 9), datetime(2027, 1, 1, 9),
                       [2], bymonth=[1], bymonthday=[1]), id="yearly"),
])
def test_rrule_empty_setpos_cases(kw):
    assert _expected(kw) == []
    assert list(rrule(**_rrule_kw(kw))) == []


# 2000-01-01 is a Saturday; its week (from MO) starts on 1999-12-27.
PIN_WEEKLY_MIDWEEK_DTSTART = _rule(
    WEEKLY, datetime(2000, 1, 1, 9), datetime(2000, 1, 20, 9), [1],
    byweekday=[0, 5])


@pytest.mark.rrule
@pytest.mark.xfail(strict=True, reason="docs/reports/r8-weekly-first-week-setpos.md")
def test_rrule_weekly_setpos_midweek_dtstart():
    kw = PIN_WEEKLY_MIDWEEK_DTSTART
    assert _expected(kw) == [datetime(2000, 1, 3, 9), datetime(2000, 1, 10, 9),
                             datetime(2000, 1, 17, 9)]
    assert list(rrule(**_rrule_kw(kw))) == _expected(kw)
