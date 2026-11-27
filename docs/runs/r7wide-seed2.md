# Run log: R-7 `rrule` reference-oracle long run, seed 2 (wide run)

Claim: R-7 (`docs/claims.md`), test in
`tests/property/test_rrule_reference_wide_prop.py` (unchanged):
- `tests/property/test_rrule_reference_wide_prop.py::test_rrule_matches_reference_wide`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=5000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_rrule_reference_wide_prop.py::test_rrule_matches_reference_wide" --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `439d2560939138263f004b762c45c21d3fdf5b08` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_reference_wide_prop.py`:
  `a7e85bd94d4183929586ca63c3db44f3ec04e25d5f9194e58274bc523df3d825  tests/property/test_rrule_reference_wide_prop.py`
- `sha256sum tests/property/rrule_reference.py`:
  `5e2abbb740b856e94f799ec5f51ef1a5358390bbda1894c2e2935c8c11b97d4e  tests/property/rrule_reference.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=5000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 1m21.202s` (shell `time`; `user 1m20.913s`, `sys 0m0.248s`); pytest reported `78.64s (0:01:18)`.
- Exit code: 0
- pytest summary line, verbatim:

```
========================= 1 passed in 78.64s (0:01:18) =========================
```

Hypothesis statistics for the test (with `--hypothesis-show-statistics`):

- `test_rrule_matches_reference_wide`: `5000 passing, 0 failing, and 503 invalid test cases` (generate phase 78.43 seconds); stopped because `settings.max_examples=5000`.

The test case ran its full 5 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures.

## Findings

Findings: none
