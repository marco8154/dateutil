# Run log: R-2/R-5 rrule claims long run, seed 1 (first run)

Claims: R-2 and R-5 (`docs/claims.md`), tests
`tests/property/test_rrule_claims_prop.py::test_occurrences_ascending_and_bounded`,
`tests/property/test_rrule_claims_prop.py::test_count_gives_prefix` and
`tests/property/test_rrule_claims_prop.py::test_occurrences_match_filters`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_claims_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `8c5a2667cef8c9ddb8181ab0633f56013db39676` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_claims_prop.py`:
  `f28c72d9d48ebfe386236390b1470bfd505336f77ba68b196ae2e4665ed1bc1a  tests/property/test_rrule_claims_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 5m18.692s` (shell `time`; `user 5m18.539s`, `sys 0m0.113s`);
  pytest reported 316.63s (0:05:16).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 3 passed in 316.63s (0:05:16) =========================
```

- Hypothesis statistics for
  `tests/property/test_rrule_claims_prop.py::test_occurrences_ascending_and_bounded`:

```
  - during generate phase (90.05 seconds):
    - Typical runtimes: ~ 1-4 ms, of which ~ 0-1 ms in data generation
    - 20000 passing, 0 failing, and 3373 invalid test cases

  - Stopped because settings.max_examples=20000
```

- Hypothesis statistics for
  `tests/property/test_rrule_claims_prop.py::test_count_gives_prefix`:

```
  - during generate phase (134.80 seconds):
    - Typical runtimes: ~ 1-5 ms, of which ~ 0-1 ms in data generation
    - 20000 passing, 0 failing, and 3001 invalid test cases

  - Stopped because settings.max_examples=20000
```

- Hypothesis statistics for
  `tests/property/test_rrule_claims_prop.py::test_occurrences_match_filters`:

```
  - during generate phase (91.63 seconds):
    - Typical runtimes: ~ 1-4 ms, of which ~ 0-1 ms in data generation
    - 20000 passing, 0 failing, and 3373 invalid test cases

  - Stopped because settings.max_examples=20000
```

All three tests ran their full 20 000 examples; the invalid cases are
draws the strategy's filters aborted, not test failures. The four
pinned `@example` cases passed as part of the run.

## Findings

Findings: none
