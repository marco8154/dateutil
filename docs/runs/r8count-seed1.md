# Run log: R-8 `rrule` reference-oracle COUNT long run, seed 1

Claim: R-8 (`docs/claims.md`), test in
`tests/property/test_rrule_reference_setpos_prop.py` (unchanged):
- `tests/property/test_rrule_reference_setpos_prop.py::test_rrule_matches_reference_setpos_count`

## Command

Run in the project folder, verbatim (wrapped in the shell's built-in `time`;
GNU `/usr/bin/time` is not available in this sandbox):

```
SWARVEX_MAX_EXAMPLES=5000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_rrule_reference_setpos_prop.py::test_rrule_matches_reference_setpos_count" --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `e710e13f4fe1fe16a4a0dc5e59bdd4d615bc551d` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_reference_setpos_prop.py`:
  `6431ffde08e0447de61c66b1bb6ab30be92279b3246dc0db53ceef7522400008  tests/property/test_rrule_reference_setpos_prop.py`
- `sha256sum tests/property/rrule_reference.py`:
  `6865bf398a5b8ee3873732313e5d52a195df9e97a96c6ba41722d2aabcfd46da  tests/property/rrule_reference.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=5000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 1m12.051s` (shell `time`; `user 1m11.926s`, `sys 0m0.115s`); pytest reported `69.51s`.
- Exit code: 0
- pytest summary line, verbatim:

```
========================= 1 passed in 69.51s (0:01:09) =========================
```

Hypothesis statistics for the test (with `--hypothesis-show-statistics`):

- `test_rrule_matches_reference_setpos_count`: `5000 passing, 0 failing, and 18015 invalid test cases` (generate phase 69.40 seconds); stopped because `settings.max_examples=5000`.
- Events: `21.72%, compared` and `67.54%, too few` (with the matching
  `67.54%, gave up because: failed to satisfy assume() in
  test_rrule_matches_reference_setpos_count (line 213)`).

The test case ran its full 5 000 examples; the invalid cases are the draws
discarded by the `assume(False)` for rules with fewer than `count`
occurrences until `until` (the `too few` event, see the module docstring)
plus draws the strategy's filters aborted, not test failures.

## Findings

Findings: none
