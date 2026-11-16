from datetime import date, datetime, time, timedelta

import pytest
from hypothesis import assume, example, given, settings
from hypothesis import strategies as st

from dateutil import tz
from dateutil.parser import isoparse
from strategies_iso import iso_dates, iso_offsets

# Strategies
ZONES = [
    tz.gettz(zname)
    for zname in (
        "America/New_York",
        "America/Los_Angeles",
        "Australia/Sydney",
        "Europe/London",
    )
]
# A missing zone must not silently turn into a naive datetime.
assert None not in ZONES
TIME_ZONE_STRATEGY = st.sampled_from([None, tz.UTC] + ZONES)
ASCII_STRATEGY = st.characters(max_codepoint=127)


@pytest.mark.isoparser
@settings(deadline=3000)
@given(dt=st.datetimes(timezones=TIME_ZONE_STRATEGY), sep=ASCII_STRATEGY)
# Ambiguous in US/Eastern: the first 01:00 (EDT) and the second (EST)
@example(dt=datetime(2020, 11, 1, 1, tzinfo=tz.gettz("US/Eastern")), sep="T")
@example(
    dt=tz.enfold(datetime(2020, 11, 1, 1, tzinfo=tz.gettz("US/Eastern")), 1),
    sep="T",
)
def test_timespec_auto(dt, sep):
    if dt.tzinfo is not None:
        # Assume offset has no sub-second components
        assume(dt.utcoffset().total_seconds() % 60 == 0)

    dtstr = dt.isoformat(sep=sep)
    dt_rt = isoparse(dtstr)

    # The round trip preserves the wall time and the offset.
    assert dt_rt.replace(tzinfo=None) == dt.replace(tzinfo=None)
    assert dt_rt.utcoffset() == dt.utcoffset()

    # According to PEP 495, if the value of fold would change the return value
    # of utcoffset(), comparisons with the datetime always return false, so we
    # must handle the case of ambiguous and imaginary datetimes here for the
    # property to remain valid.
    if (
        dt.tzinfo is None
        or tz.enfold(dt, fold=0).utcoffset()
        == tz.enfold(dt, fold=1).utcoffset()
    ):
        assert dt_rt == dt
    else:
        assert dt_rt != dt


MIDNIGHT_24_FORMS = ["24", "24:00", "2400", "24:00:00", "240000"] + [
    base + dec_sep + "0" * n
    for base in ("24:00:00", "240000")
    for dec_sep in ".,"
    for n in range(1, 7)
]
FULL_DATE_FORMS = ("YYYY-MM-DD", "YYYYMMDD", "YYYY-Www-D", "YYYYWwwD")


@pytest.mark.isoparser
@given(
    date_=iso_dates(forms=FULL_DATE_FORMS),
    time_str=st.sampled_from(MIDNIGHT_24_FORMS),
    offset_=iso_offsets(),
)
@example(
    date_=("2020-12-31", date(2020, 12, 31), "YYYY-MM-DD"),
    time_str="24:00",
    offset_=("", None, ""),
)
@example(
    date_=("2020-02-28", date(2020, 2, 28), "YYYY-MM-DD"),
    time_str="24:00:00",
    offset_=("Z", timedelta(0), "Z"),
)
@example(
    date_=("20200229", date(2020, 2, 29), "YYYYMMDD"),
    time_str="240000,000000",
    offset_=("+0530", timedelta(hours=5, minutes=30), "+HHMM"),
)
# Sunday of ISO week 53 of 2020 is 3 January 2021.
@example(
    date_=("2020W537", date(2021, 1, 3), "YYYYWwwD"),
    time_str="24",
    offset_=("-08:00", timedelta(hours=-8), "+HH:MM"),
)
def test_midnight_24_is_next_day(date_, time_str, offset_):
    date_str, d, _ = date_
    offset_str, offset, _ = offset_
    # 24:00 on date.max denotes a day that datetime cannot represent; what
    # isoparse should do there is out of scope for this claim.
    assume(d != date(9999, 12, 31))

    result = isoparse(date_str + "T" + time_str + offset_str)

    assert result.replace(tzinfo=None) == datetime.combine(
        d + timedelta(days=1), time(0)
    )
    assert result.utcoffset() == offset
