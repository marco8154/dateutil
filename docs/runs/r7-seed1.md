# Run log: R-7 rrule vs. brute-force reference long run, seed 1 (first run)

Claim: R-7 (`docs/claims.md`), test in
`tests/property/test_rrule_reference_prop.py` (unchanged), reference in
`tests/property/rrule_reference.py` (unchanged):
- `tests/property/test_rrule_reference_prop.py::test_rrule_matches_reference`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_rrule_reference_prop.py::test_rrule_matches_reference" --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `1c872bd5c5a0f0d5e3db2a3e4f17ff5c53f3eaf2` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `git` and no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_reference_prop.py tests/property/rrule_reference.py`:
  `04edb444b52553264f0e0e7a77435e0568cc2612ee319a48d9bd6c26da7ed59c  tests/property/test_rrule_reference_prop.py`
  `0a9e3f75150142d3dd32add30dedebbb650e0c3f684f996b68d6836a0bebb591  tests/property/rrule_reference.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 1m8.985s` (shell `time`; `user 1m8.896s`, `sys 0m0.082s`); pytest reported `66.56s (0:01:06)`.
- Exit code: 0
- pytest summary line, verbatim:

```
========================= 1 passed in 66.56s (0:01:06) =========================
```

Hypothesis statistics for the test (with `--hypothesis-show-statistics`):

- `test_rrule_matches_reference`: `20000 passing, 0 failing, and 2492 invalid test cases` (generate phase 66.49 s); stopped because `settings.max_examples=20000`.

The test case ran its full 20 000 examples; the invalid cases are draws the strategy's filters aborted, not test failures.

Two notes on the run itself:

- The wall time is far below the 10-30 minutes estimated in the task: the rules are capped at
  `until <= dtstart + 731 days` and the typical per-example runtime reported by Hypothesis is
  `~ 1-4 ms`, so 20 000 examples is about a minute here.
- The same command was executed once more before the logged invocation (its exit status was not
  captured). Both runs agree on every statistic (20 000 passing, 0 failing, 2 492 invalid, same
  event shares); only timings and the `repr()` addresses in the event labels differ, as expected
  for a seeded run with `database=None`.

## Findings

Findings: none
