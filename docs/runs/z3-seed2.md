# Run log: Claim Z-3 long run, seed 2 (second run)

Claim: Z-3 (`docs/claims.md`), tests
`tests/property/test_tz_helpers_prop.py` (unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_tz_helpers_prop.py --hypothesis-seed=2 -v
```

## Environment

- Commit: `f5dc761477ae75c6d46adcd00090d1d386d4a6ef` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_tz_helpers_prop.py`:
  `1239b015ef287d04cb8ed72ef97c789ad8a7ce3abf68a92db98b23e976fa87e6  tests/property/test_tz_helpers_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 25m13.215s` (shell `time`; `user 17m53.141s`, `sys 7m19.536s`);
  pytest reported 1510.27s (0:25:10).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 6 passed in 1510.27s (0:25:10) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=20000` is the configured upper
bound.

## Findings

Findings: none
