# Run log: R-6 rruleset long run, seed 2 (second run)

Claim: R-6 (`docs/claims.md`), test in `tests/property/test_rruleset_prop.py` (unchanged):
- `tests/property/test_rruleset_prop.py::test_rruleset_matches_set_algebra`

Precondition: `grep -c max_examples tests/property/test_rruleset_prop.py` printed `0`.

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rruleset_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `eed4d3707ac16d5a92d23c5518495da347332643` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rruleset_prop.py`:
  `e8557d6303df43cd63defcd7a5aea69703908eae5813aaa69e9140159629cf11  tests/property/test_rruleset_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 8m42.897s` (shell `time`; `user 8m40.071s`, `sys 0m1.128s`); pytest reported `520.76s (0:08:40)`.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 520.76s (0:08:40) =========================
```

Hypothesis statistics per test (all with `--hypothesis-show-statistics`):

- `test_rruleset_matches_set_algebra`: `20000 passing, 0 failing, and 3568 invalid test cases` (generate phase 520.65 s; typical runtimes ~2-25 ms, of which ~2-10 ms in data generation); stopped because `settings.max_examples=20000`.

The test ran its full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures.

## Findings

Findings: none
