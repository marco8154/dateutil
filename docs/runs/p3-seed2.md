# Run log: P-3 long run, seed 2 (second run)

Claim: P-3 (`docs/claims.md`), test
`tests/property/test_isoparse_tz_prop.py::test_isoparse_offset_tzinfo_type`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_tz_prop.py --hypothesis-seed=2 -v
```

## Environment

- Commit: `e2a5c4191c530d97ae1dd77d85c14e5869d1a74b` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_tz_prop.py`:
  `6e9c00bb526cf9337d2d9766bf93e295d63a801bb1476a577c83d28af55998e1  tests/property/test_isoparse_tz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 5m36.109s` (shell `time`; `user 5m35.348s`, `sys 0m0.628s`);
  pytest reported 330.40s (0:05:30).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 330.40s (0:05:30) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound. The test function is `test_isoparse_offset_tzinfo_type` (the task text
calls it `test_offset_tzinfo`); it is the only test in the file.

## Findings

Findings: none
