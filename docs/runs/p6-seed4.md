# Run log: P-6 long run, seed 4 (second run, restricted exception)

Claim: P-6 (`docs/claims.md`), test
`tests/property/test_isoparse_fuzz_prop.py::test_isoparse_raises_only_valueerror`
(unchanged; the `OverflowError` allowance is restricted to `KNOWN_OVERFLOW`).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_isoparse_fuzz_prop.py --hypothesis-seed=4 -v
```

## Environment

- Commit: `dc438dab8a696b9081e16f0f89494e6b61de60d4` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_fuzz_prop.py`:
  `ba1780874e2eb448d0adb1f08e621c2c966c78820842dc007dffdab11f31ceea  tests/property/test_isoparse_fuzz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 2m50.132s` (shell `time`; `user 2m49.889s`, `sys 0m0.196s`);
  pytest reported 165.38 s (0:02:45).
- Exit code: 0
- pytest summary line, verbatim:

```
================== 17 passed, 5 xfailed in 165.38s (0:02:45) ===================
```

The 5 `xfailed` cases are `test_isoparse_overflow_year_9999`, the pinned known
finding (`docs/reports/p6-isoparse-overflowerror.md`), and are expected.

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound.

## Findings

Findings: none
