# Run log: P-7 long run, seed 4 (second run)

Claim: P-7 (`docs/claims.md`), test
`tests/property/test_parser_fuzz_prop.py::test_parse_raises_only_documented_errors`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_parser_fuzz_prop.py --hypothesis-seed=4 -v --hypothesis-show-statistics
```

## Environment

- Commit: `2b098ca7b3964baadbaa6a5307e5981aa6e60af0` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_parser_fuzz_prop.py`:
  `9538b6d1939ed0199244498ade653a306ff246c86e4393a4de01b6ccacb026ff  tests/property/test_parser_fuzz_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 9m10.955s` (shell `time`; `user 9m9.838s`, `sys 0m1.046s`);
  pytest reported 545.12s (0:09:05).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 545.12s (0:09:05) =========================
```

- Hypothesis statistics lines:

```
  - during generate phase (542.47 seconds):
    - Typical runtimes: ~ 0-3 ms, of which ~ 0-1 ms in data generation
    - 200000 passing, 0 failing, and 8091 invalid test cases

  - Stopped because settings.max_examples=200000
```

## Findings

Findings: none
