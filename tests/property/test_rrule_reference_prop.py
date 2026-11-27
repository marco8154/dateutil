"""Oracle test for claim R-7 of ``dateutil.rrule``.

For every small rule from ``rrule_kwargs()`` (FREQ YEARLY to DAILY, window of
at most two years), ``rrule`` yields exactly the occurrences of the
independent brute-force reference ``expand`` (RFC 5545 3.3.10).
"""
from datetime import datetime, timedelta

import pytest
from hypothesis import example, given

from dateutil.rrule import DAILY, MONTHLY, WEEKLY, YEARLY, rrule

from rrule_reference import expand
from strategies_rrule import rrule_kwargs

NAMES = {YEARLY: "YEARLY", MONTHLY: "MONTHLY", WEEKLY: "WEEKLY", DAILY: "DAILY"}


def _cap_until(kw):
    kw["until"] = min(kw["until"], kw["dtstart"] + timedelta(days=731))
    return kw


# RFC 5545 forbids BYMONTHDAY with FREQ=WEEKLY (l. 2321-2322); outside claim R-7, see docs/claims.md.
# WEEKLY with BYMONTHDAY and BYWEEKDAY stays in the comparison on purpose: a match there means
# same behavior, not RFC conformance (docs/claims.md, R-7).
def _weekly_bymonthday_only(kw):
    return (kw["freq"] == WEEKLY and kw["bymonthday"] is not None
            and kw["byweekday"] is None)


def small_rrule_kwargs():
    return (
        rrule_kwargs()
        .filter(lambda kw: kw["freq"] in NAMES)
        .filter(lambda kw: not _weekly_bymonthday_only(kw))
        .map(_cap_until)
    )


def _rule(freq, dtstart, until, interval=1, wkst=None, **filters):
    kw = {
        "freq": freq,
        "dtstart": dtstart,
        "interval": interval,
        "until": until,
        "wkst": wkst,
        "bymonth": None,
        "bymonthday": None,
        "byweekday": None,
        "byhour": None,
        "byminute": None,
        "bysecond": None,
    }
    kw.update(filters)
    return kw


def _expected(kw):
    return expand(
        NAMES[kw["freq"]],
        kw["dtstart"],
        interval=kw["interval"],
        until=kw["until"],
        wkst=0 if kw["wkst"] is None else kw["wkst"],
        bymonth=kw["bymonth"],
        bymonthday=kw["bymonthday"],
        byweekday=kw["byweekday"],
        byhour=kw["byhour"],
        byminute=kw["byminute"],
        bysecond=kw["bysecond"],
    )


PIN_YEARLY_BYMONTH_BYMONTHDAY = _rule(
    YEARLY, datetime(2020, 3, 15, 10), datetime(2022, 3, 15, 10),
    bymonth=[3, 6], bymonthday=[15],
)

PIN_MONTHLY_LAST_DAY_INTERVAL_3 = _rule(
    MONTHLY, datetime(2021, 1, 31, 8, 30), datetime(2023, 2, 1, 8, 30),
    interval=3, bymonthday=[-1],
)

# RFC 5545 3.8.5.3 example (l. 7321-7332; WKST l. 2349-2362):
# with INTERVAL=2 and BYDAY=TU,SU, WKST=SU gives other dates than WKST=MO.
PIN_WEEKLY_WKST_SU = _rule(
    WEEKLY, datetime(1997, 8, 5, 9), datetime(1997, 8, 31, 9),
    interval=2, wkst=6, byweekday=[1, 6],
)

PIN_DAILY_BYWEEKDAY_BYMONTH = _rule(
    DAILY, datetime(2023, 2, 27, 7), datetime(2023, 3, 31, 7),
    interval=2, bymonth=[2, 3], byweekday=[0, 2],
)

PINS = [
    PIN_YEARLY_BYMONTH_BYMONTHDAY,
    PIN_MONTHLY_LAST_DAY_INTERVAL_3,
    PIN_WEEKLY_WKST_SU,
    PIN_DAILY_BYWEEKDAY_BYMONTH,
]


@pytest.mark.rrule
@example(kw=PIN_YEARLY_BYMONTH_BYMONTHDAY)
@example(kw=PIN_MONTHLY_LAST_DAY_INTERVAL_3)
@example(kw=PIN_WEEKLY_WKST_SU)
@example(kw=PIN_DAILY_BYWEEKDAY_BYMONTH)
@given(kw=small_rrule_kwargs())
def test_rrule_matches_reference(kw):
    assert list(rrule(**kw)) == _expected(kw)


@pytest.mark.rrule
@pytest.mark.parametrize("kw", PINS)
def test_pins_have_two_occurrences(kw):
    assert len(_expected(kw)) >= 2


@pytest.mark.rrule
def test_wkst_pin_depends_on_wkst():
    other = dict(PIN_WEEKLY_WKST_SU, wkst=0)
    assert _expected(PIN_WEEKLY_WKST_SU) != _expected(other)
