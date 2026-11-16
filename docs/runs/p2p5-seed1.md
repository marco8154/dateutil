# Run log: P-2/P-5 isoparse oracles, seed 1 (first run)

Claims: P-2 and P-5 (`docs/claims.md`), tests
`tests/property/test_isoparse_oracle_prop.py::test_isoparse_matches_fromisoformat`
(P-2, oracle `datetime.fromisoformat`) and
`tests/property/test_isoparse_oracle_prop.py::test_isoparse_week_date`
(P-5, oracle `date.fromisocalendar`), unchanged.

## Command

Run from the project root:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_oracle_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `b66e240601df6e73352f05235965bcc58c185168` (the task's base commit;
  the sandbox had no `git` and no `.git` folder, so `git rev-parse HEAD` could
  not be run)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_oracle_prop.py`:
  `9e0c6182f7e7a97d90ee8dccc200ea2d7363111a4194ae00c9251fd1c9f5f96a  tests/property/test_isoparse_oracle_prop.py`
- Hypothesis profile as reported by pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Wall time (`time`): `real 14m30.852s` (`user 14m29.400s`, `sys 0m1.187s`)
- Per test (`-v`):
  - `test_isoparse_matches_fromisoformat PASSED`
  - `test_isoparse_week_date PASSED`
- pytest summary line:

```
======================== 2 passed in 865.01s (0:14:25) =========================
```

`max_examples=200000` is an upper bound per test. The command does not print
Hypothesis statistics, so this log does not record how many examples were
actually generated, nor how many inputs of
`test_isoparse_matches_fromisoformat` were discarded by `assume(False)` because
`fromisoformat` rejected them.

## Findings

none
