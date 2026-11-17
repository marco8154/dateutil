# Run log: Z-3 tz helpers oracle long run, seed 1 (first run)

Claim: Z-3 (`docs/claims.md`), tests
`tests/property/test_tz_helpers_prop.py::test_datetime_exists_matches_zoneinfo`,
`tests/property/test_tz_helpers_prop.py::test_datetime_ambiguous_matches_zoneinfo`
and `tests/property/test_tz_helpers_prop.py::test_resolve_imaginary_matches_zoneinfo`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_tz_helpers_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `fddbb93c60f0dac3d49e7d5cfa3edaed72fd1294` (task base commit;
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

- Runtime: `real 6m2.880s` (shell `time`; `user 4m54.160s`, `sys 1m7.813s`);
  pytest reported 361.45s (0:06:01).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 6 passed in 361.45s (0:06:01) =========================
```

System time zone data on TZPATH was present, so the `[tzpath]` instances ran
and none were skipped: three tests, two data sources each, six passed.

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=20000` is the configured upper
bound.

## Findings

Findings: none
