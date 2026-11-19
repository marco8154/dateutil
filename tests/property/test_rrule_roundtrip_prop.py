"""Property test for claim R-4: ``rrulestr(str(r))`` yields the same
occurrences as ``r`` (``docs/claims.md``).

``rrule`` defines no ``__eq__``, so occurrence lists are compared, not rules.
"""
from datetime import datetime

import pytest
from hypothesis import given, example, strategies as st

from dateutil.rrule import DAILY, MONTHLY, WEEKLY, rrule, rrulestr

from strategies_rrule import rrule_kwargs


@pytest.mark.rrule
@pytest.mark.rrulestr
@example(
    kw={
        "freq": WEEKLY,
        "dtstart": datetime(2020, 3, 3, 9, 30, 0),
        "interval": 2,
        "until": datetime(2020, 6, 1),
        "wkst": 6,
        "bymonth": None,
        "bymonthday": None,
        "byweekday": [1, 6],
        "byhour": None,
        "byminute": None,
        "bysecond": None,
    }
)
@example(
    kw={
        "freq": MONTHLY,
        "dtstart": datetime(2020, 3, 15, 12, 0, 0),
        "interval": 1,
        "until": datetime(2021, 3, 15),
        "wkst": None,
        "bymonth": None,
        "bymonthday": -1,
        "byweekday": None,
        "byhour": None,
        "byminute": None,
        "bysecond": None,
    }
)
@example(
    kw={
        "freq": DAILY,
        "dtstart": datetime(2020, 3, 10, 8, 30, 45),
        "interval": 1,
        "until": datetime(2020, 4, 10),
        "wkst": None,
        "bymonth": [3],
        "bymonthday": [10],
        "byweekday": [1, 4],
        "byhour": [8],
        "byminute": [30],
        "bysecond": [45],
    }
)
@given(kw=rrule_kwargs())
def test_str_roundtrip(kw):
    r = rrule(**kw)
    s = str(r)
    r2 = rrulestr(s)
    assert list(r2) == list(r)


@pytest.mark.rrule
@pytest.mark.rrulestr
@given(data=st.data())
def test_str_roundtrip_count(data):
    kw = data.draw(rrule_kwargs())
    occurrences = list(rrule(**kw))
    assert occurrences
    n = data.draw(st.integers(min_value=1, max_value=len(occurrences)))
    kw_count = {key: value for key, value in kw.items() if key != "until"}
    kw_count["count"] = n
    r = rrule(**kw_count)
    s = str(r)
    r2 = rrulestr(s)
    assert list(r2) == list(r)
