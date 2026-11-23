# Run log: P-8 long run, seed 1 (first run)

Claim: P-8 (`docs/claims.md`), test
`tests/property/test_parser_roundtrip_prop.py::test_parse_isoformat_roundtrip`
(unchanged), parametrized over `sep` (`T` and space).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_parser_roundtrip_prop.py --hypothesis-seed=1 -v
```

## Environment

- Commit: `3a6b501913bebee88cffac12bde5f1c3ce284177` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_parser_roundtrip_prop.py`:
  `d48358063adb10678447c8f885237a88c9f8f79a2b4569c02985b1ad01a636d6  tests/property/test_parser_roundtrip_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 11m45.313s` (shell `time`; `user 11m43.997s`, `sys 0m1.224s`);
  pytest reported 697.65s (0:11:37).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 2 passed in 697.65s (0:11:37) =========================
```

The run did not print Hypothesis statistics, so the number of examples
actually executed is not shown; `max_examples=200000` is the configured upper
bound.

## Findings

Findings: none
