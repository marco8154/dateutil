# Run log: P-1 isoparse round trip, seed 1 (first run)

Claim: P-1 (`docs/claims.md`), test
`tests/property/test_isoparse_prop.py::test_timespec_auto` (upstream, unchanged).

## Command

Run from the project root:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_isoparse_prop.py::test_timespec_auto" --hypothesis-seed=1 -v
```

## Environment

- Commit: `07192198072683ffc239b3aebf46a6161459e20f` (the task's base commit;
  the sandbox had no `git` and no `.git` folder, so `git rev-parse HEAD` could
  not be run)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_isoparse_prop.py`:
  `04f92e9b74c57dc0ce600e7944a51389da010a61686078a3711f0c9b922e787f  tests/property/test_isoparse_prop.py`
- Hypothesis profile as reported by pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Wall time (`time`): `real 12m6.287s` (`user 12m2.986s`, `sys 0m2.790s`)
- pytest summary line:

```
======================== 1 passed in 714.33s (0:11:54) =========================
```

`max_examples=200000` is an upper bound. The command does not print Hypothesis
statistics, so this log does not record how many examples were actually
generated or how many were discarded by `assume(...)`.

## Findings

none
