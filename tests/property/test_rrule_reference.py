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


def test_unmatched_dtstart_is_not_emitted():
    # Jan 2025: Wed 1, Mon 6, Mon 13. DTSTART (a Wednesday) does not match
    # BYDAY=MO, so it is skipped (module docstring of rrule_reference).
    assert expand(
        "WEEKLY", datetime(2025, 1, 1, 8), byweekday=[0], count=2
    ) == [
        datetime(2025, 1, 6, 8),
        datetime(2025, 1, 13, 8),
    ]


def test_yearly_bymonthday_without_bymonth_expands_all_months():
    # BYMONTHDAY=15 at YEARLY expands over every month (RFC l. 2440).
    assert expand(
        "YEARLY", datetime(2025, 1, 1, 8), bymonthday=[15], count=3
    ) == [
        datetime(2025, 1, 15, 8),
        datetime(2025, 2, 15, 8),
        datetime(2025, 3, 15, 8),
    ]


def test_yearly_byweekday_without_bymonth_is_every_such_weekday():
    # Jan 1 2025 is a Wednesday (calendar), so Wednesdays are Jan 1, 8, 15.
    assert expand(
        "YEARLY", datetime(2025, 1, 1, 8), byweekday=[2], count=3
    ) == [
        datetime(2025, 1, 1, 8),
        datetime(2025, 1, 8, 8),
        datetime(2025, 1, 15, 8),
    ]


def test_yearly_last_sunday_of_march_uses_month_scope():
    # Sundays: Mar 2025 ... 30; Mar 2026 1, 8, 15, 22, 29; Mar 2027 7, ... 28.
    assert expand(
        "YEARLY", datetime(2025, 1, 1, 8), bymonth=[3], byweekday=[(6, -1)],
        count=3,
    ) == [
        datetime(2025, 3, 30, 8),
        datetime(2026, 3, 29, 8),
        datetime(2027, 3, 28, 8),
    ]


def test_yearly_twentieth_monday_skips_year_before_dtstart():
    # 20th Monday: May 19 2025 (before DTSTART 2025-06-01, so dropped),
    # May 18 2026; 2027 starts on a Friday, first Monday Jan 4, 20th is May 17.
    assert expand(
        "YEARLY", datetime(2025, 6, 1, 8), byweekday=[(0, 20)], count=2
    ) == [
        datetime(2026, 5, 18, 8),
        datetime(2027, 5, 17, 8),
    ]


def test_yearly_last_monday_of_year_uses_year_scope():
    # Dec 2025 ends on Wed 31, so the last Monday is the 29th; Dec 2026 ends
    # on Thu 31, so it is the 28th.
    assert expand(
        "YEARLY", datetime(2025, 1, 1, 8), byweekday=[(0, -1)], count=2
    ) == [
        datetime(2025, 12, 29, 8),
        datetime(2026, 12, 28, 8),
    ]


def test_monthly_interval_three():
    assert expand("MONTHLY", datetime(2025, 1, 15, 8), interval=3, count=3) == [
        datetime(2025, 1, 15, 8),
        datetime(2025, 4, 15, 8),
        datetime(2025, 7, 15, 8),
    ]


def test_yearly_interval_two():
    assert expand("YEARLY", datetime(2025, 3, 15, 8), interval=2, count=3) == [
        datetime(2025, 3, 15, 8),
        datetime(2027, 3, 15, 8),
        datetime(2029, 3, 15, 8),
    ]


def test_weekly_interval_two_without_byweekday_uses_dtstart_weekday():
    # Jan 1 2025 is a Wednesday; every second week is Jan 1, 15, 29.
    assert expand("WEEKLY", datetime(2025, 1, 1, 8), interval=2, count=3) == [
        datetime(2025, 1, 1, 8),
        datetime(2025, 1, 15, 8),
        datetime(2025, 1, 29, 8),
    ]


def test_bymonth_limits_monthly():
    assert expand(
        "MONTHLY", datetime(2025, 1, 10, 8), bymonth=[1, 4], count=3
    ) == [
        datetime(2025, 1, 10, 8),
        datetime(2025, 4, 10, 8),
        datetime(2026, 1, 10, 8),
    ]


def test_bymonth_limits_weekly():
    # Wednesdays in Feb 2025 (calendar): 5, 12, 19; Jan 29 is outside BYMONTH.
    assert expand(
        "WEEKLY", datetime(2025, 1, 29, 8), bymonth=[2], count=3
    ) == [
        datetime(2025, 2, 5, 8),
        datetime(2025, 2, 12, 8),
        datetime(2025, 2, 19, 8),
    ]


def test_bymonth_limits_daily():
    assert expand(
        "DAILY", datetime(2025, 1, 30, 8), bymonth=[2], count=3
    ) == [
        datetime(2025, 2, 1, 8),
        datetime(2025, 2, 2, 8),
        datetime(2025, 2, 3, 8),
    ]


def test_daily_bymonthday_limits():
    assert expand(
        "DAILY", datetime(2025, 1, 1, 8), bymonthday=[1, 15], count=4
    ) == [
        datetime(2025, 1, 1, 8),
        datetime(2025, 1, 15, 8),
        datetime(2025, 2, 1, 8),
        datetime(2025, 2, 15, 8),
    ]


def test_daily_byweekday_limits():
    # Jan 2025: Fri 3, Mon 6, Fri 10, Mon 13.
    assert expand(
        "DAILY", datetime(2025, 1, 1, 8), byweekday=[0, 4], count=4
    ) == [
        datetime(2025, 1, 3, 8),
        datetime(2025, 1, 6, 8),
        datetime(2025, 1, 10, 8),
        datetime(2025, 1, 13, 8),
    ]


def test_byminute_and_bysecond_expand():
    # 2 minutes x 2 seconds = 4 times per day (RFC l. 2445-2446).
    assert expand(
        "DAILY", datetime(2025, 1, 1, 8, 15), byminute=[45, 15],
        bysecond=[30, 0], count=5,
    ) == [
        datetime(2025, 1, 1, 8, 15, 0),
        datetime(2025, 1, 1, 8, 15, 30),
        datetime(2025, 1, 1, 8, 45, 0),
        datetime(2025, 1, 1, 8, 45, 30),
        datetime(2025, 1, 2, 8, 15, 0),
    ]


def test_until_before_last_time_of_final_day():
    # Jan 3 12:00 keeps 08:00 but drops 20:00 on the final day.
    assert expand(
        "DAILY", datetime(2025, 1, 1, 8), byhour=[8, 20],
        until=datetime(2025, 1, 3, 12),
    ) == [
        datetime(2025, 1, 1, 8),
        datetime(2025, 1, 1, 20),
        datetime(2025, 1, 2, 8),
        datetime(2025, 1, 2, 20),
        datetime(2025, 1, 3, 8),
    ]


@pytest.mark.parametrize("freq", ["DAILY", "WEEKLY"])
def test_ordinal_byweekday_raises_for_daily_and_weekly(freq):
    with pytest.raises(ValueError, match="ordinal"):
        expand(freq, datetime(2025, 1, 1), byweekday=[(0, 1)], count=1)


@pytest.mark.parametrize("n", [0, 54, -54])
def test_ordinal_out_of_range_raises(n):
    with pytest.raises(ValueError, match="ordinal"):
        expand("MONTHLY", datetime(2025, 1, 1), byweekday=[(0, n)], count=1)


@pytest.mark.parametrize("term", [7, -1, (7, 1), (-1, 1)])
def test_weekday_out_of_range_raises(term):
    with pytest.raises(ValueError, match="weekday"):
        expand("MONTHLY", datetime(2025, 1, 1), byweekday=[term], count=1)
