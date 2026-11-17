# Run log: P-7 long run, seed 3 (first run with return-value check)

Claim: P-7 (`docs/claims.md`), test
`tests/property/test_parser_fuzz_prop.py::test_parse_raises_only_documented_errors`
(unchanged; since #452 it also asserts `isinstance(result, datetime)`).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_parser_fuzz_prop.py --hypothesis-seed=3 -v --hypothesis-show-statistics
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

- Runtime: `real 3m1.955s` (shell `time`; `user 3m1.699s`, `sys 0m0.210s`);
  pytest reported 176.54 s (0:02:56).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 1 passed in 176.54s (0:02:56) =========================
```

- Hypothesis statistics for
  `tests/property/test_parser_fuzz_prop.py::test_parse_raises_only_documented_errors`:

```
  - during generate phase (175.41 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 200000 passing, 0 failing, and 8094 invalid test cases

  - Stopped because settings.max_examples=200000
```

## Findings

Findings: none
