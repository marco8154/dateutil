# Run log: R-2 rrule count with a time-zone-aware dtstart, seed 1 (first run)

Claim: R-2 (`docs/claims.md`), test in
`tests/property/test_rrule_tz_claims_prop.py` (unchanged):
- `tests/property/test_rrule_tz_claims_prop.py::test_aware_count_gives_prefix`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_rrule_tz_claims_prop.py::test_aware_count_gives_prefix" --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `f692c99901cc758ddf7190b2a9d99011756ec906` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_tz_claims_prop.py`:
  `b8f5ecb10cee45d5e6ac7fd6ef64413cea0920d24c9ac2e6f70b04a634183fe6  tests/property/test_rrule_tz_claims_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 2m14.971s` (shell `time`; `user 2m14.823s`, `sys 0m0.114s`); pytest reported `131.34s (0:02:11)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 131.34s (0:02:11) =========================
```

Hypothesis statistics for the test (with `--hypothesis-show-statistics`):

- `test_aware_count_gives_prefix`: `20000 passing, 0 failing, and 4336 invalid test cases` (generate phase 131.21 s); stopped because `settings.max_examples=20000`.

The test case ran its full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures. This test has no pinned `@example` cases (the pins for the count half of R-2 live in `test_aware_count_gives_prefix_pinned`, which is not part of this run).

## Findings

Findings: none
