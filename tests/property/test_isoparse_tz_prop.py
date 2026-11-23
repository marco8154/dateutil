from datetime import date, time, timedelta

import pytest
from hypothesis import example, given

from dateutil import tz
from dateutil.parser import isoparse
from strategies_iso import FULL_DATE_FORMS, iso_dates, iso_offsets, iso_times

OFFSET_FORMS = ("Z", "+HH:MM", "+HHMM", "+HH")

DATE_2020 = ("2020-01-01", date(2020, 1, 1), "YYYY-MM-DD")
MIDNIGHT = ("00:00", time(0), "hh:mm")


@pytest.mark.isoparser
@given(
    date_=iso_dates(forms=FULL_DATE_FORMS),
    time_=iso_times(),
    offset_=iso_offsets(forms=OFFSET_FORMS),
)
@example(date_=DATE_2020, time_=MIDNIGHT, offset_=("Z", timedelta(0), "Z"))
@example(
    date_=DATE_2020, time_=MIDNIGHT, offset_=("-00:00", timedelta(0), "+HH:MM")
)
@example(
    date_=DATE_2020,
    time_=MIDNIGHT,
    offset_=("+0530", timedelta(hours=5, minutes=30), "+HHMM"),
)
@example(
    date_=DATE_2020, time_=MIDNIGHT, offset_=("-23", timedelta(hours=-23), "+HH")
)
def test_isoparse_offset_tzinfo_type(date_, time_, offset_):
    date_str, _, _ = date_
    time_str, _, _ = time_
    offset_str, offset, _ = offset_

    result = isoparse(date_str + "T" + time_str + offset_str)

    if offset == timedelta(0):
        # A tzoffset(None, 0) compares equal to tz.UTC; the docstring
        # promises the tzutc singleton itself.
        assert result.tzinfo is tz.UTC
    else:
        assert isinstance(result.tzinfo, tz.tzoffset)
        assert result.utcoffset() == offset
