"""Known upstream cases for ``isoparse`` week dates.

- Claim P-9: ``isoparse`` should reject week 53 in an ISO year with only 52
  weeks, like ``date.fromisocalendar`` does.
- The ``isoparse`` docstring says the day of ``YYYY-Www`` "defaults to 0",
  but it defaults to 1 (Monday).
"""
from datetime import date

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.parser import isoparse, isoparser
from strategies_iso import WEEK_DATE_FORMS


def _has_52_weeks(year):
    return date(year, 12, 28).isocalendar()[1] == 52


@st.composite
def week_53_strings(draw):
    # Year 9999 is excluded: isoparse("9999-W53-1") raises OverflowError,
    # which belongs to claim P-6 (milestone 2), not to this test.
    year = draw(st.integers(1, 9998).filter(_has_52_weeks))
    form = draw(st.sampled_from(WEEK_DATE_FORMS))
    day = draw(st.integers(1, 7))
    return (
        form.replace("YYYY", "%04d" % year)
        .replace("ww", "53")
        .replace("D", str(day))
    )


@pytest.mark.isoparser
@pytest.mark.xfail(
    strict=True,
    reason="known upstream: dateutil/dateutil#1457, #1506, #1551, #1582, #1659",
)
@given(s=week_53_strings())
@example(s="2017-W53-1")
@example(s="2017W537")
@example(s="2017-W53")
# Year 1 has 52 ISO weeks: date(1, 12, 28).isocalendar() is (1, 52, 5).
@example(s="0001W531")
def test_week_53_in_52_week_year_raises(s):
    with pytest.raises(ValueError):
        isoparse(s)


@pytest.mark.isoparser
@pytest.mark.xfail(
    strict=True, reason="known upstream: dateutil/dateutil#1629, PR #1630"
)
def test_docstring_week_default_is_monday():
    assert "day defaults to 0" not in isoparser.isoparse.__doc__
