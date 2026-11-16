# Run log: P-1 long run, seed 2 (second run)

Claim: P-1 (`docs/claims.md`), test
`tests/property/test_isoparse_prop.py::test_timespec_auto` (unchanged).

## Command

Run in the project folder, verbatim:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_isoparse_prop.py::test_timespec_auto" --hypothesis-seed=2 -v
```

## Environment

- Commit: `26e05c6dd38749cb4da1f1aa1b71ed5ef6dd4008` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_prop.py`:
  `04f92e9b74c57dc0ce600e7944a51389da010a61686078a3711f0c9b922e787f  tests/property/test_isoparse_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: 678.34 s (0:11:18), as reported by pytest. The shell timer
  failed (`bc` is not installed), so this is the only measurement.
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 678.34s (0:11:18) =========================
```

Note: a first attempt with the same command was stopped by the agent sandbox
after 10 minutes (a background time limit, not a test failure) and produced
no result. The run above is a complete rerun.

## Findings

Findings: none
