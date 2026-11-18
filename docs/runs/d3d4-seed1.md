# Run log: D-3/D-4 relativedelta field targets, seed 1 (first run)

Claim: D-3 and D-4 (`docs/claims.md`), test file
`tests/property/test_relativedelta_fields_prop.py` (unchanged).

## Command

Run from the project root:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_relativedelta_fields_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `960b86be3a099241eec4eb1e25fcfeb8c1536f99` (the task's base commit; the sandbox had no `git` and no `.git` folder, so `git rev-parse HEAD` could not be run)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_relativedelta_fields_prop.py`:
  `538340426cda07856446d715d5ea18a4416d6c3af55cc47690862b4581a10f7d  tests/property/test_relativedelta_fields_prop.py`
- Hypothesis profile as reported by pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Wall time (`time`): `real 28m14.493s` (`user 28m12.621s`, `sys 0m1.642s`)
- Per-test outcome:
  - `test_absolute_fields_set_value` PASSED — 200000 passing, 0 failing, 57133 invalid (stopped because `settings.max_examples=200000`)
  - `test_normalized_same_result` PASSED — 200000 passing, 0 failing, 43878 invalid (stopped because `settings.max_examples=200000`)
- pytest summary line:

```
======================== 2 passed in 1687.46s (0:28:07) =========================
```

Hypothesis statistics were printed with `--hypothesis-show-statistics` (see per-test outcome above).

## Findings

none
