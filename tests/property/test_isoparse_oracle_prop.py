# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Oracle tests for ``isoparse`` against the standard library.

- Claim P-2: on strings that ``datetime.fromisoformat`` (Python 3.11+) also
  accepts, both return the same value and the same ``utcoffset()``.
- Claim P-5: ``YYYY-Www[-D]`` denotes ``date.fromisocalendar(YYYY, ww, D)``.
"""
from datetime import date, datetime

import pytest
from hypothesis import assume, example, given
from hypothesis import strategies as st

from dateutil.parser import isoparse

from strategies_iso import ISO_DATE_FORMS, iso_dates, iso_datetimes

# ``YYYY`` and ``YYYY-MM`` are not complete dates; fromisoformat rejects them.
COMPLETE_DATE_FORMS = tuple(
    f for f in ISO_DATE_FORMS if f not in ("YYYY", "YYYY-MM")
)
WEEK_FORMS = tuple(f for f in ISO_DATE_FORMS if "W" in f)

iso_strings = st.one_of(
    st.sampled_from("T ").flatmap(iso_datetimes).map(lambda t: t[0]),
    iso_dates(forms=COMPLETE_DATE_FORMS).map(lambda t: t[0]),
)


@pytest.mark.isoparser
@given(s=iso_strings)
@example(s="0001-01-01T00:00+23:59")
@example(s="9999-12-31T23:59:59.999999-23:59")
@example(s="9999W525T23:59:59,9-00:00")
@example(s="20200101T12:30:15.000001Z")
@example(s="2020-01-01 1230+05")
@example(s="9999-W52-5")
@example(s="2020W01")
def test_isoparse_matches_fromisoformat(s):
    try:
        expected = datetime.fromisoformat(s)
    except ValueError:
        # Outside the intersection dateutil is not bound by fromisoformat.
        assume(False)
    actual = isoparse(s)
    assert actual == expected
    assert actual.utcoffset() == expected.utcoffset()


@pytest.mark.isoparser
@given(t=iso_dates(forms=WEEK_FORMS))
# date(9999, 12, 28).isocalendar() is (9999, 52, 2): W52 is the last week.
@example(t=("9999-W52-5", date.fromisocalendar(9999, 52, 5), "YYYY-Www-D"))
@example(t=("9999W52", date.fromisocalendar(9999, 52, 1), "YYYYWww"))
# ISO year 2020 starts on 2019-12-30, so the week date lies in another year.
@example(t=("2020-W01", date.fromisocalendar(2020, 1, 1), "YYYY-Www"))
@example(t=("0001W011", date.fromisocalendar(1, 1, 1), "YYYYWwwD"))
@example(t=("2020W537", date.fromisocalendar(2020, 53, 7), "YYYYWwwD"))
def test_isoparse_week_date(t):
    s, expected, _ = t
    assert isoparse(s).date() == expected
