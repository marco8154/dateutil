# Run log: D-5 relativedelta diff long run, seed 2 (second run)

Claims: D-5 (`docs/claims.md`), tests in `tests/property/test_relativedelta_diff_prop.py` (unchanged):
- `tests/property/test_relativedelta_diff_prop.py::test_diff_then_add`
- `tests/property/test_relativedelta_diff_prop.py::test_diff_then_add_subsecond_negative`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_relativedelta_diff_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `0f2b9e65c7d2adeed531fc22fa76ed3f3f4a10b1` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026f` (`tzdata.IANA_VERSION`)
- `sha256sum tests/property/test_relativedelta_diff_prop.py`:
  `f81ae96425ed3508f88bb99454f37054f40735ce0d9b465ae19558a1403d25fb  tests/property/test_relativedelta_diff_prop.py`
- Precondition checks: `grep -c max_examples` on the test file gave `0`; the file contains `test_diff_then_add_subsecond_negative`.
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 5m26.110s` (shell `time`; `user 5m23.785s`, `sys 0m0.801s`); pytest reported `323.20s (0:05:23)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 323.20s (0:05:23) =========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_diff_then_add`: `200000 passing, 0 failing, and 0 invalid test cases` (generate phase 173.60 s); stopped because `settings.max_examples=200000`.
- `test_diff_then_add_subsecond_negative`: `200000 passing, 0 failing, and 0 invalid test cases` (generate phase 149.03 s); stopped because `settings.max_examples=200000`. Event: `0.17%, Retried draw from integers(1, 9999999).filter(lambda m: m % 1000000 != 0) to satisfy filter`.

Both tests ran their full 200 000 examples.

## Findings

Findings: none
