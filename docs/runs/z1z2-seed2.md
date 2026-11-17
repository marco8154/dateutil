# Run log: Z-1 and Z-2 long run, seed 2 (second run)

Claims: Z-1 and Z-2 (`docs/claims.md`), tests
`tests/property/test_tz_oracle_prop.py` (unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_tz_oracle_prop.py --hypothesis-seed=2 -v
```

## Environment

- Commit: `27952c810f581b8f113fbfd1c027cf9dc13efc77` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_tz_oracle_prop.py`:
  `2d7cc02349e44f3f4b9c5bfa7ec0162166bc781774a350689998415c0e394fb3  tests/property/test_tz_oracle_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 3m58.758s` (shell `time`; `user 3m13.069s`, `sys 0m45.656s`);
  pytest reported 236.28s (0:03:56). This is well below the 20–60 minute
  estimate from the 2000-examples-in-125-s calibration of the first run.
- Exit code: 0
- 14 tests collected, 0 skipped: the system time zone data on `TZPATH` was
  present, so the `[tzpath]` parametrizations all ran.
- pytest summary line, verbatim:

```
============= 4 passed, 2 xfailed, 8 xpassed in 236.28s (0:03:56) ==============
```

The `2 xfailed` are the pinned `dst()` findings
(`test_gettz_dst_matches_zoneinfo_examples`, strict per the report
`docs/reports/Z-1-dst-inference.md`); the `8 xpassed` are the non-strict
`test_known_upstream_dst` cases (`dateutil/dateutil#1667`, depends on the tz
data version). Neither is a finding; a finding would be a `FAILED` test.

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=20000` is the configured upper
bound.

## Findings

Findings: none
