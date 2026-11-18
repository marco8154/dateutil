# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Property tests for claims R-2 and R-5 of ``dateutil.rrule`` with a
time-zone-aware ``dtstart``.

Same as ``test_rrule_claims_prop.py``, but ``dtstart`` and ``until`` carry
the same zone (``zoneinfo.ZoneInfo``, ``tz.gettz`` or ``tz.UTC``), so the
tested space includes rules crossing DST gaps and half-hour transitions.

R-2: occurrences are strictly ascending and bounded by ``dtstart``/``until``.
R-5: every occurrence satisfies all explicitly set ``byxxx`` filters.
"""
import calendar
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil import tz
from dateutil.rrule import DAILY, HOURLY, rrule

from strategies_rrule import FILTER_KEYS, rrule_kwargs

KEYS = (
    "Europe/Berlin",
    "America/New_York",
    "Australia/Lord_Howe",
    "Asia/Kolkata",
    "America/St_Johns",
)
ZONES = (
    st.sampled_from(KEYS).flatmap(
        lambda k: st.sampled_from([ZoneInfo(k), tz.gettz(k)])
    )
    | st.just(tz.UTC)
)


@st.composite
def aware_rrule_kwargs(draw):
    kw = draw(rrule_kwargs())
    zone = draw(ZONES)
    kw["dtstart"] = kw["dtstart"].replace(tzinfo=zone)
    kw["until"] = kw["until"].replace(tzinfo=zone)
    return kw


PIN_DAILY_BERLIN_GAP_ZONEINFO = {
    "freq": DAILY,
    "dtstart": datetime(2021, 3, 27, 2, 30, tzinfo=ZoneInfo("Europe/Berlin")),
    "interval": 1,
    "until": datetime(2021, 4, 5, tzinfo=ZoneInfo("Europe/Berlin")),
    "wkst": None,
    "bymonth": None,
    "bymonthday": None,
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PIN_DAILY_BERLIN_GAP_GETTZ = {
    "freq": DAILY,
    "dtstart": datetime(2021, 3, 27, 2, 30, tzinfo=tz.gettz("Europe/Berlin")),
    "interval": 1,
    "until": datetime(2021, 4, 5, tzinfo=tz.gettz("Europe/Berlin")),
    "wkst": None,
    "bymonth": None,
    "bymonthday": None,
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PIN_HOURLY_LORD_HOWE_HALF_HOUR = {
    "freq": HOURLY,
    "dtstart": datetime(
        2021, 10, 3, 0, 0, tzinfo=ZoneInfo("Australia/Lord_Howe")
    ),
    "interval": 1,
    "until": datetime(
        2021, 10, 3, 6, 0, tzinfo=ZoneInfo("Australia/Lord_Howe")
    ),
    "wkst": None,
    "bymonth": None,
    "bymonthday": None,
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PINS = (
    PIN_DAILY_BERLIN_GAP_ZONEINFO,
    PIN_DAILY_BERLIN_GAP_GETTZ,
    PIN_HOURLY_LORD_HOWE_HALF_HOUR,
)


@pytest.mark.rrule
@example(kw=PIN_DAILY_BERLIN_GAP_ZONEINFO)
@example(kw=PIN_DAILY_BERLIN_GAP_GETTZ)
@example(kw=PIN_HOURLY_LORD_HOWE_HALF_HOUR)
@given(kw=aware_rrule_kwargs())
def test_aware_ascending_and_bounded(kw):
    occ = list(rrule(**kw))
    assert occ
    assert all(occ[i] < occ[i + 1] for i in range(len(occ) - 1))
    assert all(kw["dtstart"] <= o <= kw["until"] for o in occ)
    assert all(o.tzinfo is kw["dtstart"].tzinfo for o in occ)


@pytest.mark.rrule
@example(kw=PIN_DAILY_BERLIN_GAP_ZONEINFO)
@example(kw=PIN_DAILY_BERLIN_GAP_GETTZ)
@example(kw=PIN_HOURLY_LORD_HOWE_HALF_HOUR)
@given(kw=aware_rrule_kwargs())
def test_aware_occurrences_match_filters(kw):
    for occurrence in list(rrule(**kw)):
        for key in FILTER_KEYS:
            if kw[key] is None:
                continue
            if key == "bymonth":
                assert occurrence.month in kw[key]
            elif key == "bymonthday":
                days_in_month = calendar.monthrange(
                    occurrence.year, occurrence.month
                )[1]
                assert (
                    occurrence.day in kw[key]
                    or occurrence.day - days_in_month - 1 in kw[key]
                )
            elif key == "byweekday":
                assert occurrence.weekday() in kw[key]
            elif key == "byhour":
                assert occurrence.hour in kw[key]
            elif key == "byminute":
                assert occurrence.minute in kw[key]
            elif key == "bysecond":
                assert occurrence.second in kw[key]
