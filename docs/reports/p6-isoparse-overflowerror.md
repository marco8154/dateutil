# `isoparse` raises `OverflowError` instead of `ValueError` at the end of year 9999

`isoparse` raises `OverflowError: date value out of range` for strings
that denote a date after `date.max` (9999-12-31). The `isoparse` docstring
only names `ValueError` for invalid input, and every other out-of-range
input raises `ValueError`.

**Reproducer**

```python
from dateutil.parser import isoparse

# Week date after 9999-12-31 (9999-12-31 is 9999-W52-5)
isoparse("9999-W53-1")        # OverflowError: date value out of range
isoparse("9999-W52-6")        # OverflowError: date value out of range

# Hour 24 on 9999-12-31, in any date spelling
isoparse("9999-12-31T24:00")  # OverflowError: date value out of range
isoparse("9999-365T24:00")    # OverflowError: date value out of range
```

**Expected:** `ValueError` (the string does not denote a representable
`datetime`), as for e.g. `isoparse("9999-13-01")`.

**Actual:** `OverflowError: date value out of range`. `OverflowError` is not a
subclass of `ValueError`, so `except ValueError` around `isoparse` does not
catch it.

**Versions:** dateutil 4.0.0 (development, commit
`b50f89d182ada74700f3373d0d519655ff209078`), Python 3.13.18.

<details>
<summary>Cause</summary>

- `9999-W53-1`: ISO year 9999 has 52 weeks; `_calculate_weekdate` accepts
  week 53 and adds `timedelta(days=52 * 7)` to the Monday of week 1, which
  leaves the `date` range. `9999-W52-6` and `9999-W52-7` overflow the same
  way.
- `9999-12-31T24:00`: `isoparse` turns hour 24 into
  `datetime(9999, 12, 31, 0) + timedelta(days=1)`, which overflows.

Other strings with a week 53 in a 52-week year (e.g. `2021-W53-1`) do not
overflow but return a date in the next year; that is tracked separately.
</details>

A Hypothesis fuzz test (`text()`, ISO-alphabet text and one-character
mutations of valid ISO strings) found no other exception class than
`ValueError` and `OverflowError` for these two forms. No warnings were emitted.

## Duplicate search

Searched dateutil/dateutil issues and pull requests (all states, title and body) on 2026-11-17 for `isoparse OverflowError`, `isoparse 9999`, `isoparse W53 9999`, `24:00 9999-12-31`: no match. Related but different: #1617 (closed PR, non-digit characters in `isoparse`/`tzical` fields).

## Reproduced on upstream master

Reproduced on 2026-11-17 against upstream `master` at commit `a78cbd81d5d03b5f126eb36edb92bca78972c804` (2026-11-01, the current head), Python 3.13.18: all four calls in the reproducer raise `OverflowError: date value out of range`.
