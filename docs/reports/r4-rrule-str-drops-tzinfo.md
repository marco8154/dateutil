# `str(rrule)` drops the `dtstart` time zone, so `rrulestr(str(r))` returns naive occurrences

**Status:** known upstream; no new issue and no report candidate (visionary, 2026-11-24). A comment on #637 only on the visionary's explicit instruction.

`rrule.__str__` writes `DTSTART:` (and `UNTIL=`) as a bare local date-time: no
`TZID` parameter and no `Z` suffix, even when `dtstart` is time-zone aware.
Passing the result back to `rrulestr` therefore yields naive occurrences, so
`rrulestr(str(r))` does not reproduce the aware rule `r`. This holds for
`zoneinfo`, `dateutil.tz.gettz` and even `dateutil.tz.UTC`.

**Reproducer**

```python
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil.rrule import DAILY, rrule, rrulestr

r = rrule(DAILY,
          dtstart=datetime(2021, 3, 27, 2, 30, tzinfo=ZoneInfo("Europe/Berlin")),
          count=3)

print(str(r))
# DTSTART:20210327T023000
# RRULE:FREQ=DAILY;COUNT=3

print(list(rrulestr(str(r))))
# [datetime(2021, 3, 27, 2, 30), datetime(2021, 3, 28, 2, 30), datetime(2021, 3, 29, 2, 30)]

list(rrulestr(str(r))) == list(r)          # False
[o.tzinfo for o in rrulestr(str(r))][0]    # None
```

`r` yields occurrences with `tzinfo=ZoneInfo("Europe/Berlin")`; the round trip
drops them. The same happens for `dtstart=datetime(..., tzinfo=tz.UTC)`: the
`Z` suffix is missing too, so the value is read back as floating/local, not
UTC.

**Expected (RFC 5545):** `DTSTART` (section 3.8.2.4) may carry a DATE-TIME in
one of the three forms of section 3.3.5 — Form 1 local/floating, Form 2 UTC
(suffixed with `Z`), Form 3 with a `TZID` parameter naming the zone. For an
aware `dtstart`, `__str__` should use Form 2 (`DTSTART:...Z`) or Form 3
(`DTSTART;TZID=Europe/Berlin:...`) so the offset survives. `UNTIL` (section
3.8.5.1) is the same story: RFC 5545 requires the UTC form there.

**Actual:** `rrule.__str__` always emits Form 1 (`rrule.py:725`,
`self._dtstart.strftime('DTSTART:%Y%m%dT%H%M%S')`, and likewise `UNTIL=` at
`rrule.py:739`), ignoring `self._dtstart.tzinfo`. `rrulestr` reads that back as
a naive rule.

`rrulestr` already understands the RFC forms it should emit; only the writer
loses the zone:

```python
list(rrulestr("DTSTART;TZID=Europe/Berlin:20210327T023000\n"
              "RRULE:FREQ=DAILY;COUNT=2"))
# [datetime(2021, 3, 27, 2, 30, tzinfo=tzfile('.../Europe/Berlin')),
#  datetime(2021, 3, 28, 2, 30, tzinfo=tzfile('.../Europe/Berlin'))]
```

**Versions:** dateutil 4.0.0 (development, commit
`4ac3763c89ae245845818f7cd2782d06925882d4`), Python 3.13.18.

## Duplicate search

Searched dateutil/dateutil issues and pull requests (all states) on 2026-11-24 (by the visionary) for `rrule str tzinfo`, `rrule __str__ TZID`, `rrulestr DTSTART timezone`, `rrule str timezone`, `rrulestr str round trip`, `DTSTART TZID str`, `rrule str UTC Z`, `UNTIL UTC str rrule`, `rrule serialize timezone`, `rrule string DTSTART naive`. Duplicate:

- #348 (open, 2017): `rrulestr(str(r))` loses the zone of `_dtstart`; same case with `tzutc()`.
- #637 (open, 2018): `str()` of a rule with `DTSTART;TZID=America/New_York` writes `DTSTART` without `TZID` and `UNTIL` without `Z`.
- #603 (closed) with PR #604 (closed, not merged): `DTSTART:...Z` loses the `Z`.
- #806 (open) with PR #1631 (open, 2026-10-22, "Closes #806"): writes only `UNTIL` in UTC with `Z` for an aware rule; `DTSTART`/`TZID` is explicitly left to #637. With #1631, `rrulestr(str(r))` for an aware rule with `UNTIL` raises `ValueError` instead of silently dropping the zone.

## Reproduction on upstream master

Reproduced on upstream `master` at `261e291` (checked 2026-11-17 and again
2026-11-19) with `dtstart` in `zoneinfo.ZoneInfo("Europe/Berlin")`,
`dateutil.tz.gettz("Europe/Berlin")` and `dateutil.tz.UTC`: in all three cases
`str(r)` starts with `DTSTART:20210327T023000` (no `TZID`, no `Z`) and the
occurrences of `rrulestr(str(r))` have `tzinfo=None`.
