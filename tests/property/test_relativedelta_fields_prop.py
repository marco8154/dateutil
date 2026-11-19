"""Property tests for claims D-3 and D-4 on ``relativedelta``.

D-3 (docstring lines 37-41): absolute fields replace the corresponding
component of the datetime, with ``day`` clamped to the last day of the month.

D-4 (:meth:`relativedelta.normalized`): normalizing does not change the
result of adding the delta to a datetime.
"""
import calendar
from datetime import datetime

from hypothesis import example, given

from dateutil.relativedelta import relativedelta

from strategies_relativedelta import absolute_kwargs, base_datetimes, relative_kwargs

_FIELDS = ("year", "month", "day", "hour", "minute", "second", "microsecond")


@given(dt=base_datetimes(), kw=absolute_kwargs())
# Day beyond the end of the (new) month is clamped to the last day:
# 2021-02 has 28 days.
@example(dt=datetime(2021, 1, 15), kw={"month": 2, "day": 31})
# 2024-02 has 29 days.
@example(dt=datetime(2021, 1, 15), kw={"year": 2024, "month": 2, "day": 30})
def test_absolute_fields_set_value(dt, kw):
    res = dt + relativedelta(**kw)
    for field in _FIELDS:
        if field == "day":
            continue
        if field in kw:
            assert getattr(res, field) == kw[field]
        else:
            assert getattr(res, field) == getattr(dt, field)
    last_day = calendar.monthrange(res.year, res.month)[1]
    assert res.day == min(kw.get("day", dt.day), last_day)


@given(dt=base_datetimes(), kw=relative_kwargs(fractional=True))
@example(dt=datetime(2021, 1, 15), kw={"days": 1.5})
@example(dt=datetime(2021, 1, 15), kw={"hours": 25.25})
@example(dt=datetime(2021, 1, 15), kw={"days": -0.75, "hours": 0.5})
def test_normalized_same_result(dt, kw):
    rd = relativedelta(**kw)
    assert dt + rd.normalized() == dt + rd
