# Run log: R-8 rrule BYSETPOS vs. brute-force reference long run, seed 1

Claim: R-8 (`docs/claims.md`), test in
`tests/property/test_rrule_reference_setpos_prop.py` (unchanged), reference in
`tests/property/rrule_reference.py` (unchanged):
- `tests/property/test_rrule_reference_setpos_prop.py::test_rrule_matches_reference_setpos`

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=5000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_rrule_reference_setpos_prop.py::test_rrule_matches_reference_setpos" --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `f12f4025a3e6b99f31ea3b5fdaece8e159272af0` (task base commit; `git rev-parse HEAD` was not available: the sandbox has no `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_reference_setpos_prop.py tests/property/rrule_reference.py`:
  `178bfc81f64f5b8043703b4cbb6bb2a31eddeb90970beb2277206da004d2af23  tests/property/test_rrule_reference_setpos_prop.py`
  `6865bf398a5b8ee3873732313e5d52a195df9e97a96c6ba41722d2aabcfd46da  tests/property/rrule_reference.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=5000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 1m20.408s` (shell `time`; `user 1m19.796s`, `sys 0m0.461s`); pytest reported `76.92s (0:01:16)`.
- Exit code: 0
- pytest summary line, verbatim:

```
========================= 1 passed in 76.92s (0:01:16) =========================
```

Hypothesis statistics for the test (with `--hypothesis-show-statistics`), verbatim excerpt:

```
  - during generate phase (76.65 seconds):
    - Typical runtimes: ~ 3-10 ms, of which ~ 2-7 ms in data generation
    - 5000 passing, 0 failing, and 4671 invalid test cases
    - Events:
      * 51.70%, non-empty
      * 42.30%, empty
      * 42.30%, gave up because: failed to satisfy assume() in test_rrule_matches_reference_setpos (line 184)
```

Further `gave up` events, verbatim:

```
      * 0.09%, gave up because: Aborted test because unable to satisfy integers(1, 31).filter(lambda v: v != anchor)
      * 0.01%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda v: v != anchor)
```

The remaining events are `Retried draw ... to satisfy filter` lines from the
strategy's filters and are omitted here.

- Stopped because `settings.max_examples=5000`.

The test case ran its full 5 000 examples. The invalid cases are rules with an
empty expected result, rejected by `assume()` on purpose (the `empty` event,
same 42.30 %), plus a few draws the strategy's filters aborted; none are test
failures. The event percentages are relative to all 9 671 test cases (passing
plus invalid), so `empty` and `non-empty` do not add up to 100 %.

One note on the run itself:

- The wall time is below the 5-40 minutes estimated in the task: the typical
  per-example runtime reported by Hypothesis is `~ 3-10 ms`, so 5 000 examples
  take under two minutes here.

## Findings

Findings: none
