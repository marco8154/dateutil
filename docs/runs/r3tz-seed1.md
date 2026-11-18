# Run log: R-3 rrule queries (zoned) long run, seed 1 (first run)

Claims: R-3 (`docs/claims.md`), tests in `tests/property/test_rrule_query_tz_prop.py` (unchanged):
- `tests/property/test_rrule_query_tz_prop.py::test_aware_count_matches_list[False]`
- `tests/property/test_rrule_query_tz_prop.py::test_aware_count_matches_list[True]`
- `tests/property/test_rrule_query_tz_prop.py::test_aware_before_after[False]`
- `tests/property/test_rrule_query_tz_prop.py::test_aware_before_after[True]`
- `tests/property/test_rrule_query_tz_prop.py::test_aware_between[False]`
- `tests/property/test_rrule_query_tz_prop.py::test_aware_between[True]`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_query_tz_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `c08e7405a489e973b1d8784a87d01d4c354d4616` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_query_tz_prop.py`:
  `2e1d59e0563dce605ec9ceea250dbec6b8ab38df963a300e14643e42b07a2a8d  tests/property/test_rrule_query_tz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 22m23.799s` (shell `time`; `user 22m23.492s`, `sys 0m0.160s`); pytest reported `1340.54s (0:22:20)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 6 passed in 1340.54s (0:22:20) ========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_aware_count_matches_list[False]`: `20000 passing, 0 failing, and 4518 invalid test cases` (generate phase 234.93 s); stopped because `settings.max_examples=20000`.
- `test_aware_count_matches_list[True]`: `20000 passing, 0 failing, and 4518 invalid test cases` (generate phase 238.71 s); stopped because `settings.max_examples=20000`.
- `test_aware_before_after[False]`: `20000 passing, 0 failing, and 8002 invalid test cases` (generate phase 218.78 s); stopped because `settings.max_examples=20000`.
- `test_aware_before_after[True]`: `20000 passing, 0 failing, and 8002 invalid test cases` (generate phase 202.95 s); stopped because `settings.max_examples=20000`.
- `test_aware_between[False]`: `20000 passing, 0 failing, and 8758 invalid test cases` (generate phase 227.69 s); stopped because `settings.max_examples=20000`.
- `test_aware_between[True]`: `20000 passing, 0 failing, and 8758 invalid test cases` (generate phase 217.20 s); stopped because `settings.max_examples=20000`.

All six test cases ran their full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures.

## Findings

Findings: none
