# Run log: Z-1 and Z-2 long run, seed 1 (wide, 1850-2100)

Claims: Z-1 and Z-2 (`docs/claims.md`), tests
`tests/property/test_tz_oracle_wide_prop.py` (`dateutil.tz.gettz` against
`zoneinfo`, unchanged). This run checks `utcoffset()`, `tzname()` (Z-1) and
the UTC round trip (Z-2) on 20 000 examples per test over 1850-2100 instead
of the 200 of the pipeline profile.

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_tz_oracle_wide_prop.py -k "not examples" --hypothesis-seed=1 -v
```

## Environment

- Commit: `fe346b4310720e3395d387415f4f248e38c83769` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_tz_oracle_wide_prop.py`:
  `2af57c2f091d7230066f50ef31db63e1384b521a5f718ac9c52f13c79b9494ab  tests/property/test_tz_oracle_wide_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 19m35.189s` (shell `time`; `user 14m42.620s`, `sys 4m52.460s`);
  pytest reported 1172.56s (0:19:32).
- Exit code: 0
- pytest summary line, verbatim:

```
================ 4 passed, 74 deselected in 1172.56s (0:19:32) ================
```

Collected 78 items: 4 selected (`test_gettz_matches_zoneinfo_wide` and
`test_astimezone_roundtrip_wide`, each under `[tzpath]` and `[tzdata]`), 74
deselected (`-k "not examples"` removes the pinned
`test_gettz_dst_wide_examples`). Neither source was skipped: both `[tzpath]`
and `[tzdata]` ran. There was no `FAILED`, so there is no finding to record.

## Findings

Findings: none
