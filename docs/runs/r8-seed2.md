# Run log: R-8 `rrule` reference-oracle long run, seed 2

Claim: R-8 (`docs/claims.md`), test in
`tests/property/test_rrule_reference_setpos_prop.py` (unchanged):
- `tests/property/test_rrule_reference_setpos_prop.py::test_rrule_matches_reference_setpos`

## Command

Run in the project folder, verbatim (wrapped in the shell's built-in `time`;
GNU `/usr/bin/time` is not available in this sandbox):

```
SWARVEX_MAX_EXAMPLES=5000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_rrule_reference_setpos_prop.py::test_rrule_matches_reference_setpos" --hypothesis-seed=2 -v --hypothesis-show-statistics
```

## Environment

- Commit: `f12f4025a3e6b99f31ea3b5fdaece8e159272af0` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_reference_setpos_prop.py`:
  `178bfc81f64f5b8043703b4cbb6bb2a31eddeb90970beb2277206da004d2af23  tests/property/test_rrule_reference_setpos_prop.py`
- `sha256sum tests/property/rrule_reference.py`:
  `6865bf398a5b8ee3873732313e5d52a195df9e97a96c6ba41722d2aabcfd46da  tests/property/rrule_reference.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=5000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 0m32.612s` (shell `time`; `user 0m32.473s`, `sys 0m0.125s`); pytest reported `29.28s`.
- Exit code: 0
- pytest summary line, verbatim:

```
============================== 1 passed in 29.28s ==============================
```

Hypothesis statistics for the test (with `--hypothesis-show-statistics`):

- `test_rrule_matches_reference_setpos`: `5000 passing, 0 failing, and 4760 invalid test cases` (generate phase 29.05 seconds); stopped because `settings.max_examples=5000`.
- Events: `51.23%, non-empty` and `42.10%, empty`.

The test case ran its full 5 000 examples; the invalid cases are the rules
whose expected result is empty (deliberately discarded by `assume(False)`, see
the module docstring) plus draws the strategy's filters aborted, not test
failures.

## Findings

Findings: none
