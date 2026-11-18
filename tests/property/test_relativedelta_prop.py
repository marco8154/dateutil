"""Property tests for ``relativedelta`` arithmetic against the standard library.

- Claim D-1: with only relative time units, ``dt + relativedelta(**kw) == dt
  + timedelta(**kw)`` (oracle: ``timedelta``).
- Claim D-2: ``(dt + rd) - rd == dt`` when no month-end clamping occurs
  (``base_datetimes(max_day=28)`` excludes clamping). Falsified over the whole
  input space; see docs/reports/d2-relativedelta-roundtrip.md.
"""
from datetime import datetime, timedelta

import pytest
from hypothesis import example, given

from dateutil.relativedelta import relativedelta

from strategies_relativedelta import base_datetimes, relative_kwargs, relative_time_kwargs


@given(dt=base_datetimes(), kw=relative_time_kwargs())
@example(dt=datetime(2000, 1, 1), kw={"days": -1, "microseconds": 1})
def test_matches_timedelta(dt, kw):
    assert dt + relativedelta(**kw) == dt + timedelta(**kw)


@pytest.mark.xfail(
    strict=True,
    reason="docs/reports/d2-relativedelta-roundtrip.md",
)
@given(dt=base_datetimes(max_day=28), kw=relative_kwargs())
@example(dt=datetime(2021, 1, 28), kw={"months": 1, "days": 3})
@example(dt=datetime(2021, 1, 28), kw={"months": 1, "days": 3, "microseconds": 1})
def test_add_then_subtract(dt, kw):
    rd = relativedelta(**kw)
    assert (dt + rd) - rd == dt
