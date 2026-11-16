from datetime import datetime, timedelta, timezone

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.parser import parse

# Whole-minute offsets only; isoformat writes seconds for other offsets.
TIME_ZONE_STRATEGY = st.one_of(
    st.none(),
    st.just(timezone.utc),
    st.integers(min_value=-1439, max_value=1439).map(
        lambda m: timezone(timedelta(minutes=m))
    ),
)
DATETIME_STRATEGY = st.datetimes(
    min_value=datetime(1, 1, 1),
    max_value=datetime(9999, 12, 31, 23, 59, 59, 999999),
    timezones=TIME_ZONE_STRATEGY,
)


@pytest.mark.parametrize("sep", ["T", " "])
@given(dt=DATETIME_STRATEGY)
# Years below 100 are written with leading zeros ("0050-...").
@example(dt=datetime(50, 3, 4, 5, 6, 7, 8))
@example(dt=datetime(1, 1, 1, tzinfo=timezone(timedelta(minutes=-1439))))
@example(dt=datetime(12, 1, 13, tzinfo=timezone.utc))
@example(
    dt=datetime(
        9999, 12, 31, 23, 59, 59, 999999,
        tzinfo=timezone(timedelta(minutes=1439)),
    )
)
def test_parse_isoformat_roundtrip(dt, sep):
    dtstr = dt.isoformat(sep=sep)
    dt_rt = parse(dtstr)

    assert dt_rt.replace(tzinfo=None) == dt.replace(tzinfo=None)
    if dt.tzinfo is None:
        assert dt_rt.tzinfo is None
    else:
        assert dt_rt.utcoffset() == dt.utcoffset()
