# Run log: P-6 long run, seed 2 (second run)

Claim: P-6 (`docs/claims.md`), test file
`tests/property/test_isoparse_fuzz_prop.py` (unchanged).

## Command

Run in the project folder, verbatim:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_fuzz_prop.py --hypothesis-seed=2 -v
```

## Environment

- Commit: `017d4bbf50e2a9fabb21827634531de3d6984fd9` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_fuzz_prop.py`:
  `b10c34f7f0e80a0b378eaed14f80dd6a9e15eede5e44ed4b88586d9ab4998e16  tests/property/test_isoparse_fuzz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: 368.83 s wall clock (shell timer around the command);
  pytest reports 363.34s (0:06:03).
- Exit code: 0
- pytest summary line, verbatim:

```
=================== 1 passed, 2 xfailed in 363.34s (0:06:03) ===================
```

The two `xfailed` cases are the expected
`test_isoparse_overflow_year_9999[9999-W53-1]` and
`test_isoparse_overflow_year_9999[9999-12-31T24:00]`.
`test_isoparse_raises_only_valueerror` passed.

## Findings

Findings: none
