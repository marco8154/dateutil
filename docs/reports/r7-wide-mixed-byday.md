# `rrule` with plain and ordinal `byweekday` terms in one list yields too few occurrences

**Status:** not submitted: duplicate of dateutil/dateutil#1588 (duplicate search 2026-11-28 by the visionary).

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

Searched 2026-11-28 in dateutil/dateutil, issues and pull requests in all
states (terms included "byweekday nth", "BYDAY ordinal", "byweekday mixed",
"FR(-1)", "nwdaymask", "bynweekday byweekday").

- #1588 (open, 2026-09-30): a `BYDAY` of plain and ordinal weekdays is
  treated as an intersection instead of a union (`MO,1FR` gives `[]`,
  `FR,1FR` only the first Friday; MONTHLY and YEARLY). Same cause.
- PR #1589 (open, "Fixes #1588"): drops a day only if it matches neither
  list, citing RFC 5545 3.3.10.
- PR #1610 (closed 2026-10-14, not merged): a second fix for #1588.

Result: duplicate, no new issue. The xfail stays strict so a merge of #1589
shows up as XPASS.

## Reproduction on upstream master

Not needed: according to #1588, `rrule.py` is unchanged since 2021, and it
did not change between `a78cbd8` and `261e291`.
