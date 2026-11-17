# Run log: Z-1 and Z-2 long run, seed 2 (second run)

Claims: Z-1 and Z-2 (`docs/claims.md`), tests
`tests/property/test_tz_oracle_wide_prop.py` (unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_tz_oracle_wide_prop.py -k "not examples" --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `a1cf86ba39dfc7d0970e58d546291fc351c6458c` (task base commit;
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

- Runtime: `real 19m22.277s` (shell `time`; `user 14m42.442s`, `sys 4m39.678s`);
  pytest reported 1159.44s (0:19:19).
- Exit code: 0
- 78 items collected, 74 deselected, 4 selected: the pinned
  `test_gettz_dst_wide_examples` cases are deselected by `-k "not examples"`;
  the system time zone data on `TZPATH` was present, so the `[tzpath]`
  parametrizations all ran (0 skipped).
- pytest summary line, verbatim:

```
============== 4 passed, 74 deselected in 1159.44s (0:19:19) =================
```

- Hypothesis statistics (one line per test, verbatim from the run):

```
tests/property/test_tz_oracle_wide_prop.py::test_gettz_matches_zoneinfo_wide[tzpath]:
  - 20000 passing, 0 failing, and 0 invalid test cases
  - Stopped because settings.max_examples=20000

tests/property/test_tz_oracle_wide_prop.py::test_gettz_matches_zoneinfo_wide[tzdata]:
  - 20000 passing, 0 failing, and 0 invalid test cases
  - Stopped because settings.max_examples=20000

tests/property/test_tz_oracle_wide_prop.py::test_astimezone_roundtrip_wide[tzpath]:
  - 20000 passing, 0 failing, and 0 invalid test cases
  - Stopped because settings.max_examples=20000

tests/property/test_tz_oracle_wide_prop.py::test_astimezone_roundtrip_wide[tzdata]:
  - 20000 passing, 0 failing, and 0 invalid test cases
  - Stopped because settings.max_examples=20000
```

All four tests show `20000 passing`; no `FAILED` test, so no falsifying example
was produced.

## Findings

Findings: none
