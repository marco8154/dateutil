# Run log: P-3 long run, seed 1 (first run)

Claims: P-3 (`docs/claims.md`), test
`tests/property/test_isoparse_tz_prop.py::test_isoparse_offset_tzinfo_type`
(unchanged).

## Command

Run in the project folder, verbatim:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_tz_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `2ae5e2618bb4af3e190d9025cf573adf10250e64` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_tz_prop.py`:
  `6e9c00bb526cf9337d2d9766bf93e295d63a801bb1476a577c83d28af55998e1  tests/property/test_isoparse_tz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: pytest reported 484.24s (0:08:04); the command ran without a `time` wrapper.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 484.24s (0:08:04) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound.

## Findings

Findings: none
