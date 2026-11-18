# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Property test for claim R-6 of ``dateutil.rrule``.

An ``rruleset`` built from rules, ``rdate`` and ``exdate`` yields exactly the
sorted union of the rule and ``rdate`` occurrences, without duplicates and
without the ``exdate`` occurrences (RFC 5545 3.8.5.1/3.8.5.2).
"""
from datetime import datetime, timedelta

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.rrule import DAILY, HOURLY, WEEKLY, rrule, rruleset

from strategies_rrule import rrule_kwargs


def _rule(freq, dtstart, until, interval=1):
    return {
        "freq": freq,
        "dtstart": dtstart,
        "interval": interval,
        "until": until,
        "wkst": None,
        "bymonth": None,
        "bymonthday": None,
        "byweekday": None,
        "byhour": None,
        "byminute": None,
        "bysecond": None,
    }


@st.composite
def rruleset_cases(draw):
    """``(rule_kwargs, rdates, exdates)`` for a finite ``rruleset``.

    ``rdates`` may contain duplicates; ``exdates`` are drawn mostly from the
    occurrences actually in the set so that they remove something.
    """
    rule_kwargs = draw(st.lists(rrule_kwargs(), min_size=1, max_size=2))
    base = rule_kwargs[0]["dtstart"]
    offset = st.integers(min_value=-10**6, max_value=10**6).map(
        lambda seconds: base + timedelta(seconds=seconds)
    )
    rdates = draw(st.lists(offset, max_size=5))
    pool = sorted(
        {occurrence for kw in rule_kwargs for occurrence in rrule(**kw)}
        | set(rdates)
    )
    exdates = []
    if pool:
        exdates += draw(st.lists(st.sampled_from(pool), max_size=5))
    exdates += draw(st.lists(offset, max_size=2))
    return rule_kwargs, rdates, exdates


PIN_TWO_OVERLAPPING_RULES = (
    [
        _rule(DAILY, datetime(2020, 1, 1), datetime(2020, 1, 10)),
        _rule(DAILY, datetime(2020, 1, 1), datetime(2020, 1, 10), interval=2),
    ],
    [datetime(2020, 1, 3)],
    [datetime(2020, 1, 5)],
)

PIN_WEEKLY_RDATE_DUPLICATE = (
    [_rule(WEEKLY, datetime(2021, 6, 7, 9, 0), datetime(2021, 7, 5, 9, 0))],
    [datetime(2021, 6, 8, 9, 0), datetime(2021, 6, 8, 9, 0)],
    [datetime(2021, 6, 14, 9, 0), datetime(2021, 6, 8, 9, 0)],
)

PIN_HOURLY_RDATE_BEFORE_DTSTART = (
    [_rule(HOURLY, datetime(2022, 3, 1), datetime(2022, 3, 1, 5))],
    [datetime(2022, 2, 28, 23)],
    [datetime(2022, 3, 1, 2), datetime(2030, 1, 1)],
)


@pytest.mark.rruleset
@example(case=PIN_TWO_OVERLAPPING_RULES)
@example(case=PIN_WEEKLY_RDATE_DUPLICATE)
@example(case=PIN_HOURLY_RDATE_BEFORE_DTSTART)
@given(case=rruleset_cases())
def test_rruleset_matches_set_algebra(case):
    rule_kwargs, rdates, exdates = case

    rs = rruleset()
    for kw in rule_kwargs:
        rs.rrule(rrule(**kw))
    for date in rdates:
        rs.rdate(date)
    for date in exdates:
        rs.exdate(date)

    rule_terms = set()
    for kw in rule_kwargs:
        rule_terms.update(rrule(**kw))
    expected = sorted((rule_terms | set(rdates)) - set(exdates))

    assert list(rs) == expected
