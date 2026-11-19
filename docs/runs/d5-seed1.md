# Run log: D-5 relativedelta difference round trip, long run, seed 1 (first run)

Claim: D-5 (`docs/claims.md`), tests in `tests/property/test_relativedelta_diff_prop.py` (unchanged):
- `tests/property/test_relativedelta_diff_prop.py::test_diff_then_add`
- `tests/property/test_relativedelta_diff_prop.py::test_diff_then_add_subsecond_negative`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_relativedelta_diff_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `0f2b9e65c7d2adeed531fc22fa76ed3f3f4a10b1` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6` (IANA `2026f`)
- `sha256sum tests/property/test_relativedelta_diff_prop.py`:
  `f81ae96425ed3508f88bb99454f37054f40735ce0d9b465ae19558a1403d25fb  tests/property/test_relativedelta_diff_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 5m25.223s` (shell `time`; `user 5m23.439s`, `sys 0m0.259s`); pytest reported `322.35s (0:05:22)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 322.35s (0:05:22) =========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_diff_then_add`: `200000 passing, 0 failing, and 0 invalid test cases` (generate phase 173.07 s); stopped because `settings.max_examples=200000`.
- `test_diff_then_add_subsecond_negative`: `200000 passing, 0 failing, and 0 invalid test cases` (generate phase 148.73 s); stopped because `settings.max_examples=200000`.

Both tests ran their full 200 000 examples.

## Findings

Findings: none
