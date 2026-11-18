# Run log: R-4 rrulestr round trip, seed 1 (first run)

Claim: R-4 (`docs/claims.md`), test `tests/property/test_rrule_roundtrip_prop.py` (unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_roundtrip_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
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

- Wall time (`time`): `real 16m56.519s` (`user 16m55.926s`, `sys 0m0.493s`); pytest reported 1012.77s (0:16:52).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 1012.77s (0:16:52) ========================
```

Hypothesis statistics were printed (`--hypothesis-show-statistics`):

- `test_str_roundtrip`: 20000 passing, 0 failing, 3710 invalid test cases; stopped because `settings.max_examples=20000`.
- `test_str_roundtrip_count`: 20000 passing, 0 failing, 3274 invalid test cases; stopped because `settings.max_examples=20000`.

## Findings

Findings: none
