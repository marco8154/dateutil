# `rrule` WEEKLY with `bysetpos` counts the first week from `dtstart` instead of from the week start

**Status:** draft, not submitted.

With `freq=WEEKLY` and `bysetpos`, when `dtstart` does not fall on the first
day of its week (`wkst`), `rrule` builds the first week's set only from the
days on or after `dtstart`. Candidates earlier in that week are not counted,
so positive positions in the first week select the wrong instance.

**Reproducer**

```python
from datetime import datetime
from dateutil.rrule import WEEKLY, MO, SA, rrule

dtstart = datetime(2000, 1, 1, 9)  # a Saturday; its week starts on Mon 1999-12-27
until = datetime(2000, 1, 20, 9)
print(list(rrule(WEEKLY, dtstart=dtstart, until=until,
                 byweekday=[MO, SA], bysetpos=[1])))
# [2000-01-01 09:00, 2000-01-03 09:00, 2000-01-10 09:00, 2000-01-17 09:00]
print(list(rrule(WEEKLY, dtstart=dtstart, until=until,
                 byweekday=[MO, SA], bysetpos=[2])))
# [2000-01-08 09:00, 2000-01-15 09:00]
```

**Expected (RFC 5545 3.3.10):** "BYSETPOS operates on a set of recurrence
instances in one interval of the recurrence rule. For example, in a WEEKLY
rule, the interval would be one week A set of recurrence instances starts at
the beginning of the interval defined by the FREQ rule part" (l. 2366-2370).
The first set is Mon 1999-12-27 and Sat 2000-01-01. `BYSETPOS=1` selects
1999-12-27, which precedes `DTSTART` and is dropped, so the result is
2000-01-03, 01-10, 01-17. `BYSETPOS=2` selects 2000-01-01, so the result is
2000-01-01, 01-08, 01-15. The independent reference
`tests/property/rrule_reference.py` returns exactly these.

**Actual:** `BYSETPOS=1` adds 2000-01-01, `BYSETPOS=2` misses it.
`_iterinfo.wdayset` (`rrule.py:1278-1290`) starts the day set at `dtstart`'s
day and runs up to the next `wkst`, so in the first week the positions are
counted over the days from `dtstart` onward. MONTHLY and YEARLY use the full
month/year (`mdayset`/`ydayset`) and are not affected. Negative positions give
the same result either way, because the days left out all precede `dtstart`
and would be dropped anyway.

**Versions:** dateutil 4.0.0 (development, base commit
`a534c5ee26c8a3a5e58f7085e1ce37cb0596bfab`), Python 3.13.

Test: `tests/property/test_rrule_reference_setpos_prop.py::test_rrule_weekly_setpos_midweek_dtstart`
(strict xfail). The BYSETPOS oracle test moves a WEEKLY `dtstart` to the start
of its week, so it does not reach this case.

## Duplicate search

pending (lead)
