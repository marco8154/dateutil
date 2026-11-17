# Run log: Z-1 and Z-2 long run, seed 1 (first run)

Claims: Z-1 and Z-2 (`docs/claims.md`), tests
`tests/property/test_tz_oracle_prop.py` (`dateutil.tz.gettz` against
`zoneinfo`, unchanged). This run checks `utcoffset()`, `tzname()` (Z-1) and
the UTC round trip (Z-2) on 20 000 examples per test instead of the 200 of
the pipeline profile.

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_tz_oracle_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `8f9a29ef4f94baac745b2de72c85cc54a3dfc0fb` (task base commit;
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

- Runtime: `real 3m52.278s` (shell `time`; `user 3m8.051s`, `sys 0m44.175s`);
  pytest reported 230.81s (0:03:50).
- Exit code: 0
- pytest summary line, verbatim:

```
============= 4 passed, 2 xfailed, 8 xpassed in 230.81s (0:03:50) ==============
```

14 tests were collected and none were skipped: both `[tzpath]` and
`[tzdata]` sources were available and ran. The 2 `xfailed` are the pinned
`dst()` findings of
`test_gettz_dst_matches_zoneinfo_examples` (`docs/reports/Z-1-dst-inference.md`);
the 8 `xpassed` are the non-strict `test_known_upstream_dst`
(dateutil/dateutil#1667, consistent with tzdata 2026.6). Neither is a
finding; a finding would be a `FAILED`.

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=20000` is the configured upper
bound.

## Findings

Findings: none
