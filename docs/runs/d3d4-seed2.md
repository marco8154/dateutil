# Run log: D-3/D-4 long run, seed 2 (second run)

Claims: D-3 and D-4 (`docs/claims.md`), tests in
`tests/property/test_relativedelta_fields_prop.py` (unchanged):

- `tests/property/test_relativedelta_fields_prop.py::test_absolute_fields_set_value`
- `tests/property/test_relativedelta_fields_prop.py::test_normalized_same_result`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_relativedelta_fields_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `960b86be3a099241eec4eb1e25fcfeb8c1536f99` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_relativedelta_fields_prop.py`:
  `538340426cda07856446d715d5ea18a4416d6c3af55cc47690862b4581a10f7d  tests/property/test_relativedelta_fields_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 8m47.722s` (shell `time`; `user 8m47.421s`, `sys 0m0.243s`);
  pytest reported 521.60s (0:08:41).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 521.60s (0:08:41) =========================
```

- Hypothesis statistics per test (`--hypothesis-show-statistics`):
  - `test_absolute_fields_set_value`: `200000 passing, 0 failing, and 58161
    invalid test cases` (generate phase 252.68 seconds); stopped because
    `settings.max_examples=200000`
  - `test_normalized_same_result`: `200000 passing, 0 failing, and 42757
    invalid test cases` (generate phase 267.87 seconds); stopped because
    `settings.max_examples=200000`

## Findings

Findings: none
