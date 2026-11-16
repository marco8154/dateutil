# Run log: P-6 isoparse fuzz target, seed 1 (first run)

Claim: P-6 (`docs/claims.md`), test file
`tests/property/test_isoparse_fuzz_prop.py` (#392, unchanged).

## Command

Run from the project root:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_fuzz_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `017d4bbf50e2a9fabb21827634531de3d6984fd9` (the task's base commit;
  the sandbox had no `git` and no `.git` folder, so `git rev-parse HEAD` could
  not be run)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_fuzz_prop.py`:
  `b10c34f7f0e80a0b378eaed14f80dd6a9e15eede5e44ed4b88586d9ab4998e16  tests/property/test_isoparse_fuzz_prop.py`
- Hypothesis profile as reported by pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Wall time (`time`): `real 6m18.552s` (`user 6m17.737s`, `sys 0m0.712s`)
- Per-test outcome:
  - `test_isoparse_raises_only_valueerror` PASSED
  - `test_isoparse_overflow_year_9999[9999-W53-1]` XFAIL (known finding)
  - `test_isoparse_overflow_year_9999[9999-12-31T24:00]` XFAIL (known finding)
- pytest summary line:

```
=================== 1 passed, 2 xfailed in 373.13s (0:06:13) ===================
```

`max_examples=200000` is an upper bound. The command does not print Hypothesis
statistics, so this log does not record how many examples were actually
generated. The fuzz test accepts any `OverflowError` for inputs starting with
`9999` (known finding, `docs/reports/p6-isoparse-overflowerror.md`), so this
run cannot detect further overflow inputs with that prefix.

## Findings

none
