# `rrule` with plain and ordinal `byweekday` terms in one list yields too few occurrences

**Status:** draft; duplicate search and reproduction on upstream `master` still to be done by the lead (sandbox has no network).

With `freq=MONTHLY` (and `YEARLY`), a `byweekday` list that mixes a plain
weekday and an ordinal one (`[MO, FR(-1)]`) selects only days matching both,
instead of days matching either. Here the result is empty.

**Reproducer**

```python
from datetime import datetime
from dateutil.rrule import MONTHLY, MO, FR, rrule

dtstart = datetime(2024, 1, 1, 8)
print(list(rrule(MONTHLY, dtstart=dtstart, count=6, byweekday=[MO, FR(-1)])))
# []
print(list(rrule(MONTHLY, dtstart=dtstart, count=3, byweekday=[MO])))
# [2024-01-01 08:00, 2024-01-08 08:00, 2024-01-15 08:00]
print(list(rrule(MONTHLY, dtstart=dtstart, count=3, byweekday=[FR(-1)])))
# [2024-01-26 08:00, 2024-02-23 08:00, 2024-03-29 08:00]
```

**Expected (RFC 5545 3.3.10):** `BYDAY=MO,-1FR` is a valid `bywdaylist`
(`weekdaynum *("," weekdaynum)`, l. 2170-2172); the rule selects every Monday
and the last Friday of each month: 2024-01-01, 01-08, 01-15, 01-22, 01-26,
01-29, ... The independent reference `tests/property/rrule_reference.py`
returns exactly this.

**Actual:** `rrule.__init__` stores plain weekdays in `_byweekday` and
ordinal ones in `_bynweekday` (`rrule.py:609-622`). The day filter in
`rrule._iter` (`rrule.py:850-851`) skips a day unless it passes both `wdaymask[i] in byweekday` and `nwdaymask[i]`, so the two kinds of
term intersect instead of uniting.

**Versions:** dateutil 4.0.0 (development, base commit
`5d5796450036761fabe6d2e142efa916df94ae8c`), Python 3.13.

Test: `tests/property/test_rrule_reference_wide_prop.py::test_rrule_mixed_plain_and_ordinal_byday`
(strict xfail). The wide oracle test generates plain-only or ordinal-only
`byweekday` lists, so it does not reach this case.

## Duplicate search

Not done (no network); the lead searches upstream before the report is sent.

## Reproduction on upstream master

Not done; the lead reproduces it.
