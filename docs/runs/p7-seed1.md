# Run log: P-7 parse fuzz target, seed 1 (first run)

Claim: P-7 (`docs/claims.md`), test
`tests/property/test_parser_fuzz_prop.py::test_parse_raises_only_documented_errors`
(task #393, unchanged).

## Command

Run from the project root:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_parser_fuzz_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `017d4bbf50e2a9fabb21827634531de3d6984fd9` (the task's base commit;
  the sandbox had no `git` and no `.git` folder, so `git rev-parse HEAD` could
  not be run)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_parser_fuzz_prop.py`:
  `994160f41384abae9e63449c75b8451e274c3892c0822b65c87e09d457b5b158  tests/property/test_parser_fuzz_prop.py`
- Hypothesis profile as reported by pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Wall time (`time`): `real 6m28.705s` (`user 6m27.739s`, `sys 0m0.860s`)
- pytest summary line:

```
======================== 1 passed in 382.67s (0:06:22) =========================
```

`max_examples=200000` is an upper bound. The command does not print Hypothesis
statistics, so this log does not record how many examples were actually
generated.

## Findings

none
