# Run log: R-2/R-5 long run, seed 2 (second run)

Claims: R-2 and R-5 (`docs/claims.md`), tests in `tests/property/test_rrule_claims_prop.py` (unchanged):
- `tests/property/test_rrule_claims_prop.py::test_occurrences_ascending_and_bounded`
- `tests/property/test_rrule_claims_prop.py::test_count_gives_prefix`
- `tests/property/test_rrule_claims_prop.py::test_occurrences_match_filters`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_claims_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `8c5a2667cef8c9ddb8181ab0633f56013db39676` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_claims_prop.py`:
  `f28c72d9d48ebfe386236390b1470bfd505336f77ba68b196ae2e4665ed1bc1a  tests/property/test_rrule_claims_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 26m31.180s` (shell `time`; `user 26m30.517s`, `sys 0m0.527s`); pytest reported `1587.41s (0:26:27)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 3 passed in 1587.41s (0:26:27) ========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_occurrences_ascending_and_bounded`: `20000 passing, 0 failing, and 3332 invalid test cases` (generate phase 570.81 s); stopped because `settings.max_examples=20000`.
- `test_count_gives_prefix`: `20000 passing, 0 failing, and 3095 invalid test cases` (generate phase 452.88 s); stopped because `settings.max_examples=20000`.
- `test_occurrences_match_filters`: `20000 passing, 0 failing, and 3332 invalid test cases` (generate phase 563.31 s); stopped because `settings.max_examples=20000`.

## Findings

Findings: none
