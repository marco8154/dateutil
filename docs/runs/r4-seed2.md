# Run log: R-4 rrulestr roundtrip long run, seed 2 (second run)

Claim: R-4 (`docs/claims.md`), tests
`tests/property/test_rrule_roundtrip_prop.py::test_str_roundtrip` and
`tests/property/test_rrule_roundtrip_prop.py::test_str_roundtrip_count`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_roundtrip_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `960b86be3a099241eec4eb1e25fcfeb8c1536f99` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_roundtrip_prop.py`:
  `da2a2edff7940a8f20c7e7190f278f46456c976858412fb3ad1191ae91ce6c5c  tests/property/test_rrule_roundtrip_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 16m18.226s` (shell `time`; `user 16m17.589s`, `sys 0m0.534s`);
  pytest reported 974.44s (0:16:14).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 974.44s (0:16:14) =========================
```

- Hypothesis statistics for
  `tests/property/test_rrule_roundtrip_prop.py::test_str_roundtrip`:
  `20000 passing, 0 failing, and 3571 invalid test cases` (generate phase 549.15 s); stopped because `settings.max_examples=20000`.
- Hypothesis statistics for
  `tests/property/test_rrule_roundtrip_prop.py::test_str_roundtrip_count`:
  `20000 passing, 0 failing, and 3280 invalid test cases` (generate phase 424.97 s); stopped because `settings.max_examples=20000`.

Both tests ran their full 20 000 examples; the invalid cases are draws the
strategy's filters aborted, not test failures. The pinned `@example` cases
passed as part of the run.

## Findings

Findings: none
