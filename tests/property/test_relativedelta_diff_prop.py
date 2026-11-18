# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Property test for claim D-5: for naive ``dt1``/``dt2`` anywhere in
0001-9999, ``dt2 + relativedelta(dt1, dt2) == dt1``, including sub-second
fractions and negative differences.

Upstream PR #1676 changes only how the difference is split over ``seconds`` and
``microseconds``, not the result of adding it back, which is what is asserted.
"""
from datetime import datetime, timedelta

from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.relativedelta import relativedelta

ALL_DATETIMES = st.datetimes(
    min_value=datetime(1, 1, 1),
    max_value=datetime(9999, 12, 31, 23, 59, 59, 999999),
)


@given(dt1=ALL_DATETIMES, dt2=ALL_DATETIMES)
# Negative difference with a sub-second fraction.
@example(dt1=datetime(2000, 1, 1, 0, 0, 0, 500000), dt2=datetime(2000, 1, 1, 0, 0, 2))
# Month-end arithmetic.
@example(dt1=datetime(2021, 3, 31), dt2=datetime(2021, 2, 28))
# Leap day, negative difference.
@example(dt1=datetime(2019, 2, 28), dt2=datetime(2020, 2, 29))
# Range bounds, dt1 before dt2.
@example(dt1=datetime(1, 1, 1), dt2=datetime(9999, 12, 31, 23, 59, 59, 999999))
# Range bounds, dt1 after dt2.
@example(dt1=datetime(9999, 12, 31, 23, 59, 59, 999999), dt2=datetime(1, 1, 1))
def test_diff_then_add(dt1, dt2):
    assert dt2 + relativedelta(dt1, dt2) == dt1


@given(
    dt2=st.datetimes(
        min_value=datetime(1, 1, 1, 0, 0, 10), max_value=datetime(9999, 12, 31)
    ),
    micros=st.integers(min_value=1, max_value=9_999_999).filter(
        lambda m: m % 1_000_000 != 0
    ),
)
def test_diff_then_add_subsecond_negative(dt2, micros):
    dt1 = dt2 - timedelta(microseconds=micros)
    assert dt2 + relativedelta(dt1, dt2) == dt1
