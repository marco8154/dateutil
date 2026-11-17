# Run log: P-4 long run, seed 1 (first run)

Claim: P-4 (`docs/claims.md`), test `tests/property/test_isoparse_prop.py::test_midnight_24_is_next_day` (unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_prop.py::test_midnight_24_is_next_day --hypothesis-seed=1 -v
```

## Environment

- Commit: `26a9ebe5127fc873f969e7122e65fe501edebe80` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_prop.py`:
  `94d44e61d42d6b4c3f488363410d81c72b04ca4202580d83d73fd96c36adfcb1  tests/property/test_isoparse_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 7m10.948s` (shell `time`; `user 7m10.039s`, `sys 0m0.851s`);
  pytest reported 425.58s (0:07:05).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 425.58s (0:07:05) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound.

## Findings

Findings: none
