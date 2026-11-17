# Run log: P-2 and P-5 long run, seed 2 (second run)

Claims: P-2 and P-5 (`docs/claims.md`), tests
`tests/property/test_isoparse_oracle_prop.py::test_isoparse_matches_fromisoformat`
and `tests/property/test_isoparse_oracle_prop.py::test_isoparse_week_date`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_oracle_prop.py --hypothesis-seed=2 -v
```

## Environment

- Commit: `dc438dab8a696b9081e16f0f89494e6b61de60d4` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_oracle_prop.py`:
  `9e0c6182f7e7a97d90ee8dccc200ea2d7363111a4194ae00c9251fd1c9f5f96a  tests/property/test_isoparse_oracle_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 16m31.434s` (shell `time`; `user 16m30.085s`, `sys 0m1.206s`);
  pytest reported 985.47s (0:16:25).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 985.47s (0:16:25) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound.

## Findings

Findings: none
