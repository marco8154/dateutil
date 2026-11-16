# `isoparse` raises `OverflowError` instead of `ValueError` at the end of year 9999

`isoparse` raises `OverflowError: date value out of range` for two strings
that denote a date after `date.max` (9999-12-31). The `isoparse` docstring
only names `ValueError` for invalid input, and every other out-of-range
input raises `ValueError`.

**Reproducer**

```python
from dateutil.parser import isoparse

isoparse("9999-W53-1")        # OverflowError: date value out of range
isoparse("9999-12-31T24:00")  # OverflowError: date value out of range
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
  leaves the `date` range.
- `9999-12-31T24:00`: `isoparse` turns hour 24 into
  `datetime(9999, 12, 31, 0) + timedelta(days=1)`, which overflows.

Other strings with a week 53 in a 52-week year (e.g. `2021-W53-1`) do not
overflow but return a date in the next year; that is tracked separately.
</details>

A Hypothesis fuzz test (`text()`, ISO-alphabet text and one-character
mutations of valid ISO strings) found no other exception class than
`ValueError` and these two `OverflowError` cases. No warnings were emitted.

## Duplicate search

TODO (lead)

## Reproduced on upstream master

TODO (lead)
