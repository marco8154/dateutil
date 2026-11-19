# Run log: R-6 rruleset long run, seed 1 (first run)

Claims: R-6 (`docs/claims.md`), tests in `tests/property/test_rruleset_prop.py` (unchanged):
- `tests/property/test_rruleset_prop.py::test_rruleset_matches_set_algebra`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rruleset_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `0f2b9e65c7d2adeed531fc22fa76ed3f3f4a10b1` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rruleset_prop.py`:
  `e8557d6303df43cd63defcd7a5aea69703908eae5813aaa69e9140159629cf11  tests/property/test_rruleset_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 4m03.839s` (shell `time`; `user 4m3.665s`, `sys 0m0.152s`); pytest reported `240.94s (0:04:00)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 240.94s (0:04:00) =========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_rruleset_matches_set_algebra`: `20000 passing, 0 failing, and 3542 invalid test cases` (generate phase 240.88 s); stopped because `settings.max_examples=20000`.

The test case ran its full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures.

## Findings

Findings: none
