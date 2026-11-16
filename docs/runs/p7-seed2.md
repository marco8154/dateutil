# Run log: P-7 long run, seed 2 (second run)

Claim: P-7 (`docs/claims.md`), test
`tests/property/test_parser_fuzz_prop.py::test_parse_raises_only_documented_errors`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_parser_fuzz_prop.py --hypothesis-seed=2 -v
```

## Environment

- Commit: `2836feab180df756f67e6102ff0e5b71d0fa7bfd` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_parser_fuzz_prop.py`:
  `994160f41384abae9e63449c75b8451e274c3892c0822b65c87e09d457b5b158  tests/property/test_parser_fuzz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 6m27.102s` (shell `time`; `user 6m26.050s`, `sys 0m0.948s`);
  pytest reported 381.09 s (0:06:21).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 381.09s (0:06:21) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound.

## Findings

Findings: none
