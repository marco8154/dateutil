# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Property tests for claims R-2 and R-5 of ``dateutil.rrule``.

R-2: occurrences are strictly ascending, bounded by ``dtstart``/``until``,
and ``count=n`` yields exactly the first ``n`` occurrences.
R-5: every occurrence satisfies all explicitly set ``byxxx`` filters.
"""
import calendar
from datetime import datetime

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.rrule import (
    MONTHLY,
    SECONDLY,
    YEARLY,
    rrule,
)

from strategies_rrule import FILTER_KEYS, rrule_kwargs

PIN_MONTHLY_BYMONTHDAY_31 = {
    "freq": MONTHLY,
    "dtstart": datetime(2020, 1, 31),
    "interval": 1,
    "until": datetime(2020, 12, 31, 23, 59, 59),
    "wkst": None,
    "bymonth": None,
    "bymonthday": [31],
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PIN_MONTHLY_BYMONTHDAY_LAST = {
    "freq": MONTHLY,
    "dtstart": datetime(2020, 1, 31),
    "interval": 1,
    "until": datetime(2020, 12, 31, 23, 59, 59),
    "wkst": None,
    "bymonth": None,
    "bymonthday": [-1],
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PIN_SECONDLY_TIME_FILTERS = {
    "freq": SECONDLY,
    "dtstart": datetime(2020, 1, 1, 5, 6, 7),
    "interval": 4,
    "until": datetime(2020, 1, 1, 6, 0, 0),
    "wkst": None,
    "bymonth": None,
    "bymonthday": None,
    "byweekday": None,
    "byhour": [5],
    "byminute": [6],
    "bysecond": [7],
}

PIN_YEARLY_FEB29 = {
    "freq": YEARLY,
    "dtstart": datetime(2020, 2, 29),
    "interval": 1,
    "until": datetime(2030, 12, 31, 23, 59, 59),
    "wkst": None,
    "bymonth": [2],
    "bymonthday": [29],
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PINS = (
    PIN_MONTHLY_BYMONTHDAY_31,
    PIN_MONTHLY_BYMONTHDAY_LAST,
    PIN_SECONDLY_TIME_FILTERS,
    PIN_YEARLY_FEB29,
)


def _without_until(kw):
    return {key: value for key, value in kw.items() if key != "until"}


@pytest.mark.rrule
@example(kw=PIN_MONTHLY_BYMONTHDAY_31)
@example(kw=PIN_MONTHLY_BYMONTHDAY_LAST)
@example(kw=PIN_SECONDLY_TIME_FILTERS)
@example(kw=PIN_YEARLY_FEB29)
@given(kw=rrule_kwargs())
def test_occurrences_ascending_and_bounded(kw):
    terms = list(rrule(**kw))
    assert terms
    assert all(terms[i] < terms[i + 1] for i in range(len(terms) - 1))
    assert all(kw["dtstart"] <= occurrence <= kw["until"] for occurrence in terms)


@pytest.mark.rrule
@given(data=st.data())
def test_count_gives_prefix(data):
    kw = data.draw(rrule_kwargs())
    terms = list(rrule(**kw))
    assert terms
    n = data.draw(st.integers(min_value=1, max_value=len(terms)))
    assert list(rrule(count=n, **_without_until(kw))) == terms[:n]


@pytest.mark.rrule
@example(kw=PIN_MONTHLY_BYMONTHDAY_31)
@example(kw=PIN_MONTHLY_BYMONTHDAY_LAST)
@example(kw=PIN_SECONDLY_TIME_FILTERS)
@example(kw=PIN_YEARLY_FEB29)
@given(kw=rrule_kwargs())
def test_occurrences_match_filters(kw):
    for occurrence in list(rrule(**kw)):
        if kw["bymonth"] is not None:
            assert occurrence.month in kw["bymonth"]
        if kw["bymonthday"] is not None:
            days_in_month = calendar.monthrange(occurrence.year, occurrence.month)[1]
            assert (
                occurrence.day in kw["bymonthday"]
                or occurrence.day - days_in_month - 1 in kw["bymonthday"]
            )
        if kw["byweekday"] is not None:
            assert occurrence.weekday() in kw["byweekday"]
        if kw["byhour"] is not None:
            assert occurrence.hour in kw["byhour"]
        if kw["byminute"] is not None:
            assert occurrence.minute in kw["byminute"]
        if kw["bysecond"] is not None:
            assert occurrence.second in kw["bysecond"]
