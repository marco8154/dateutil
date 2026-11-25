"""Self-tests for the RFC 5545 brute-force reference (no Hypothesis).

Every expected occurrence list is derived by hand from RFC 5545 section 3.3.10
or a calendar; the reference module is checked against the RFC, not against
the library under test.
"""

from datetime import datetime

import pytest

from rrule_reference import expand


def test_daily_simple_count():
    assert expand("DAILY", datetime(2025, 1, 1, 8), count=3) == [
        datetime(2025, 1, 1, 8),
        datetime(2025, 1, 2, 8),
        datetime(2025, 1, 3, 8),
    ]


def test_daily_interval_two():
    assert expand("DAILY", datetime(2025, 1, 1, 8), interval=2, count=4) == [
        datetime(2025, 1, 1, 8),
        datetime(2025, 1, 3, 8),
        datetime(2025, 1, 5, 8),
        datetime(2025, 1, 7, 8),
    ]


def test_daily_byhour_expands_times():
    # BYHOUR=9,17 yields both times on each selected day (RFC l. 2444).
    assert expand("DAILY", datetime(2025, 1, 1, 9), byhour=[9, 17], count=3) == [
        datetime(2025, 1, 1, 9),
        datetime(2025, 1, 1, 17),
        datetime(2025, 1, 2, 9),
    ]


def test_weekly_wkst_monday_example():
    # RFC 5545 3.8.5.3, l. 7324-7327: August 5, 10, 19, 24 (1997).
    assert expand(
        "WEEKLY", datetime(1997, 8, 5, 9), interval=2, count=4,
        byweekday=[1, 6], wkst=0,
    ) == [
        datetime(1997, 8, 5, 9),
        datetime(1997, 8, 10, 9),
        datetime(1997, 8, 19, 9),
        datetime(1997, 8, 24, 9),
    ]


def test_weekly_wkst_sunday_example():
    # RFC 5545 3.8.5.3, l. 7331-7334: same rule, WKST=SU gives 5, 17, 19, 31.
    assert expand(
        "WEEKLY", datetime(1997, 8, 5, 9), interval=2, count=4,
        byweekday=[1, 6], wkst=6,
    ) == [
        datetime(1997, 8, 5, 9),
        datetime(1997, 8, 17, 9),
        datetime(1997, 8, 19, 9),
        datetime(1997, 8, 31, 9),
    ]


def test_monthly_last_day_of_month():
    assert expand("MONTHLY", datetime(2025, 1, 1, 8), bymonthday=[-1], count=4) == [
        datetime(2025, 1, 31, 8),
        datetime(2025, 2, 28, 8),
        datetime(2025, 3, 31, 8),
        datetime(2025, 4, 30, 8),
    ]


def test_monthly_31st_skips_short_months():
    # The 31st does not exist in 30-day months, so those months drop out.
    # RFC 5545 3.3.10, l. 2382 (invalid dates ignored).
    assert expand(
        "MONTHLY", datetime(2025, 1, 1, 8), bymonthday=[31],
        until=datetime(2025, 6, 30, 23, 59),
    ) == [
        datetime(2025, 1, 31, 8),
        datetime(2025, 3, 31, 8),
        datetime(2025, 5, 31, 8),
    ]


def test_monthly_first_friday():
    # BYDAY=1FR: Jan 1 2025 is a Wednesday so the first Friday is the 3rd.
    assert expand("MONTHLY", datetime(2025, 1, 1, 8), byweekday=[(4, 1)], count=3) == [
        datetime(2025, 1, 3, 8),
        datetime(2025, 2, 7, 8),
        datetime(2025, 3, 7, 8),
    ]


def test_monthly_last_sunday():
    # BYDAY=-1SU: last Sunday of January, February, March 2025.
    assert expand("MONTHLY", datetime(2025, 1, 1, 8), byweekday=[(6, -1)], count=3) == [
        datetime(2025, 1, 26, 8),
        datetime(2025, 2, 23, 8),
        datetime(2025, 3, 30, 8),
    ]


def test_monthly_fifth_friday_absent_in_short_months():
    # A 5th Friday only in October 2025 and January 2026 within the window.
    assert expand(
        "MONTHLY", datetime(2025, 9, 1, 10), byweekday=[(4, 5)], count=2
    ) == [
        datetime(2025, 10, 31, 10),
        datetime(2026, 1, 30, 10),
    ]


def test_monthly_friday_13th_is_second_friday():
    # BYDAY=2FR with BYMONTHDAY=13: every Friday the 13th is the 2nd Friday,
    # so the only match in 2025 is June 13 (RFC l. 2453, erratum 3747).
    assert expand(
        "MONTHLY", datetime(2025, 1, 1, 9), byweekday=[(4, 2)], bymonthday=[13],
        until=datetime(2025, 12, 31, 23, 59),
    ) == [datetime(2025, 6, 13, 9)]


def test_monthly_first_friday_with_monthday_13_never_matches():
    # The 13th can never be the first Friday, so BYDAY=1FR yields nothing.
    assert expand(
        "MONTHLY", datetime(2025, 1, 1, 9), byweekday=[(4, 1)], bymonthday=[13],
        until=datetime(2025, 12, 31, 23, 59),
    ) == []


def test_yearly_simple_count():
    assert expand("YEARLY", datetime(2025, 3, 15, 8), count=3) == [
        datetime(2025, 3, 15, 8),
        datetime(2026, 3, 15, 8),
        datetime(2027, 3, 15, 8),
    ]


def test_yearly_last_day_of_december():
    assert expand(
        "YEARLY", datetime(2025, 1, 1, 8), bymonth=[12], bymonthday=[-1], count=2
    ) == [
        datetime(2025, 12, 31, 8),
        datetime(2026, 12, 31, 8),
    ]


def test_yearly_february_29_only_in_leap_years():
    # No February 29 in 2025-2027, so those years produce no occurrence.
    # RFC 5545 3.3.10, l. 2382 (invalid dates ignored).
    assert expand("YEARLY", datetime(2024, 2, 29, 8), count=2) == [
        datetime(2024, 2, 29, 8),
        datetime(2028, 2, 29, 8),
    ]


def test_yearly_twentieth_monday_of_year():
    # YEARLY BYDAY=20MO without BYMONTH: ordinal within the year (RFC l. 2305).
    assert expand(
        "YEARLY", datetime(2025, 1, 1, 8), byweekday=[(0, 20)], count=2
    ) == [
        datetime(2025, 5, 19, 8),
        datetime(2026, 5, 18, 8),
    ]


def test_yearly_53rd_monday_only_in_long_years():
    # Only 2024 and 2029 have 53 Mondays among 2024-2031 (RFC l. 2305).
    assert expand(
        "YEARLY", datetime(2024, 1, 1, 8), byweekday=[(0, 53)], count=2
    ) == [
        datetime(2024, 12, 30, 8),
        datetime(2029, 12, 31, 8),
    ]


def test_unknown_freq_raises():
    with pytest.raises(ValueError):
        expand("HOURLY", datetime(2025, 1, 1), count=1)


def test_no_bound_raises():
    with pytest.raises(ValueError):
        expand("DAILY", datetime(2025, 1, 1))


def test_both_bounds_raise():
    with pytest.raises(ValueError):
        expand("DAILY", datetime(2025, 1, 1), count=2, until=datetime(2025, 2, 1))
