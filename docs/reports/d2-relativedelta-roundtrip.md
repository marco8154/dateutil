# `relativedelta` is not round-trip stable across a month boundary

`(dt + rd) - rd == dt` does not hold for `relativedelta` once the added time
units cross a month boundary. Claim D-2 is an expectation (not a contract), so
this is a finding reported against the documentation, not a contract breach.

**Reproducer**

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

# dt + rd = 2021-03-03, then subtracting rd again lands on 2021-01-31
dt = datetime(2021, 1, 28)
rd = relativedelta(months=1, days=3)
assert (dt + rd) - rd == dt   # fails: 2021-01-31 != 2021-01-28
```

The same failure occurs with a microsecond component:

```python
dt = datetime(2021, 1, 28)
rd = relativedelta(months=1, days=3, microseconds=1)
(dt + rd) - rd == dt   # False: 2021-01-31 != 2021-01-28
```

**Expected:** `(dt + rd) - rd == dt`.

**Actual:** `(dt + rd) - rd == 2021-01-31 != 2021-01-28`.

**Versions:** dateutil 4.0.0 (development, commit
`8c5a2667cef8c9ddb8181ab0633f56013db39676`), Python 3.13.18.

<details>
<summary>Cause</summary>

`relativedelta.__add__` with a `datetime`
(`src/dateutil/relativedelta.py`, the ``datetime`` branch around lines 368-404)
first sets year and month via `replace`, then adds days and the smaller units
as a `timedelta`. Subtraction does the same with negated values, months first
again. The two steps do not commute once the time units cross a month
boundary: adding `months=1, days=3` moves into March and only then adds the
days, while subtracting applies the negative month first and the negative days
afterwards, landing on a different day of the original month.
</details>

**Assessment.** The `relativedelta` docstring does not promise round-trip
stability; the behaviour follows the documented order of operations (calendar
fields first, then the ``timedelta`` part). The report therefore asks for a
hint in the documentation, not for a code change.

## Duplicate search

TODO (lead): search dateutil/dateutil issues and pull requests (all states,
title and body) for `relativedelta round trip`, `(dt + rd) - rd`,
`relativedelta months days non-commutative`, and related phrasing; record
whether an existing issue or PR covers this finding.

## Reproduced on upstream master

TODO (lead): reproduce on upstream `master` at the current head with the two
reproducers above and record the commit and Python version.
