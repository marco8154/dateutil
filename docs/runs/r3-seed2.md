# Run log: R-3 rrule queries long run, seed 2 (second run)

Claims: R-3 (`docs/claims.md`), tests in `tests/property/test_rrule_query_prop.py` (unchanged):
- `tests/property/test_rrule_query_prop.py::test_count_matches_list[False]`
- `tests/property/test_rrule_query_prop.py::test_count_matches_list[True]`
- `tests/property/test_rrule_query_prop.py::test_before_after[False]`
- `tests/property/test_rrule_query_prop.py::test_before_after[True]`
- `tests/property/test_rrule_query_prop.py::test_between[False]`
- `tests/property/test_rrule_query_prop.py::test_between[True]`
- `tests/property/test_rrule_query_prop.py::test_queries_on_complete_cache`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_query_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `e44c22fc4303724e28d48e55e78467aaa13ce6b1` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_query_prop.py`:
  `6271dd91f91779d8ed84ba54ff223eb13a5b50a2db6f6c5adeba1bcae6d3a524  tests/property/test_rrule_query_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 28m7.025s` (shell `time`; `user 28m6.655s`, `sys 0m0.177s`); pytest reported `1683.57s (0:28:03)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 7 passed in 1683.57s (0:28:03) ========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_count_matches_list[False]`: `20000 passing, 0 failing, and 3558 invalid test cases` (generate phase 188.67 s); stopped because `settings.max_examples=20000`.
- `test_count_matches_list[True]`: `20000 passing, 0 failing, and 3558 invalid test cases` (generate phase 190.00 s); stopped because `settings.max_examples=20000`.
- `test_before_after[False]`: `20000 passing, 0 failing, and 7875 invalid test cases` (generate phase 327.63 s); stopped because `settings.max_examples=20000`.
- `test_before_after[True]`: `20000 passing, 0 failing, and 7875 invalid test cases` (generate phase 309.98 s); stopped because `settings.max_examples=20000`.
- `test_between[False]`: `20000 passing, 0 failing, and 8279 invalid test cases` (generate phase 251.23 s); stopped because `settings.max_examples=20000`.
- `test_between[True]`: `20000 passing, 0 failing, and 8279 invalid test cases` (generate phase 244.04 s); stopped because `settings.max_examples=20000`.
- `test_queries_on_complete_cache`: `20000 passing, 0 failing, and 8202 invalid test cases` (generate phase 171.71 s); stopped because `settings.max_examples=20000`.

All seven test cases ran their full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures.

## Findings

Findings: none
