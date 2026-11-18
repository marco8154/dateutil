# Run log: R-2/R-5 rrule claims with a time-zone-aware dtstart, seed 1 (first run)

Claims: R-2 and R-5 (`docs/claims.md`), tests in
`tests/property/test_rrule_tz_claims_prop.py` (unchanged):
- `tests/property/test_rrule_tz_claims_prop.py::test_aware_ascending_and_bounded`
- `tests/property/test_rrule_tz_claims_prop.py::test_aware_occurrences_match_filters`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_tz_claims_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `e86170c7cdc99fb487c04d6c738677fe9d68d9a7` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_tz_claims_prop.py`:
  `271f966387abdbce9b55237aa04b0d0d621b067eb9a6f0565ae4b571cb03190f  tests/property/test_rrule_tz_claims_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 4m50.327s` (shell `time`; `user 4m50.199s`, `sys 0m0.105s`); pytest reported `288.14s (0:04:48)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 288.14s (0:04:48) =========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_aware_ascending_and_bounded`: `20000 passing, 0 failing, and 4518 invalid test cases` (generate phase 145.42 s); stopped because `settings.max_examples=20000`.
- `test_aware_occurrences_match_filters`: `20000 passing, 0 failing, and 4518 invalid test cases` (generate phase 142.61 s); stopped because `settings.max_examples=20000`.

Both test cases ran their full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures. The three pinned `@example` cases passed as part of the run.

## Findings

Findings: none
