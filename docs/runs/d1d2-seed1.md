# Run log: D-1/D-2.1 relativedelta long run, seed 1 (first run)

Claims: D-1 and D-2.1 (`docs/claims.md`); the file also carries the pinned
D-2 falsification (`test_add_then_subtract`, `xfail(strict=True)`). Test file
`tests/property/test_relativedelta_prop.py` (unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_relativedelta_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `e86170c7cdc99fb487c04d6c738677fe9d68d9a7` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_relativedelta_prop.py`:
  `928c49e59fc8cd6dc2252cfe67fde42b39d077f7712e88bb9cbb6d525a9d4f42  tests/property/test_relativedelta_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 6m28.637s` (shell `time`; `user 6m28.389s`, `sys 0m0.208s`);
  pytest reported 383.55s (0:06:23).
- Exit code: 0
- pytest summary line, verbatim:

```
=================== 2 passed, 1 xfailed in 383.55s (0:06:23) ===================
```

- Hypothesis statistics for
  `tests/property/test_relativedelta_prop.py::test_matches_timedelta`:

```
  - during generate phase (253.28 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 200000 passing, 0 failing, and 68860 invalid test cases
    - Events:
      * 9.42%, Retried draw from builds(build, weeks=one_of(none(), integers(min_value=-520, max_value=520)), days=one_of(none(), integers(min_value=-3650, max_value=3650)), hours=one_of(none(), integers(min_value=-87600, max_value=87600)), minutes=one_of(none(), integers(min_value=-1000000, max_value=1000000)), seconds=one_of(none(), integers(min_value=-10000000, max_value=10000000)), microseconds=one_of(none(), integers(min_value=-1_000_000_000, max_value=1_000_000_000))).filter(lambda kw: bool(kw)) to satisfy filter
      * 0.00%, gave up because: Aborted test because unable to satisfy builds(build, weeks=one_of(none(), integers(min_value=-520, max_value=520)), days=one_of(none(), integers(min_value=-3650, max_value=3650)), hours=one_of(none(), integers(min_value=-87600, max_value=87600)), minutes=one_of(none(), integers(min_value=-1000000, max_value=1000000)), seconds=one_of(none(), integers(min_value=-10000000, max_value=10000000)), microseconds=one_of(none(), integers(min_value=-1_000_000_000, max_value=1_000_000_000))).filter(lambda kw: bool(kw))

  - Stopped because settings.max_examples=200000
```

- Hypothesis statistics for
  `tests/property/test_relativedelta_prop.py::test_add_then_subtract`: none —
  Hypothesis printed no statistics block for this test; it ends on its pinned
  `@example` right away (`XFAIL`), which is expected for the
  `xfail(strict=True)` D-2 falsification.
- Hypothesis statistics for
  `tests/property/test_relativedelta_prop.py::test_add_then_subtract_calendar`:

```
  - during generate phase (129.28 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 200000 passing, 0 failing, and 181 invalid test cases
    - Events:
      * 4.38%, Retried draw from <hypothesis.strategies._internal.datetime.DatetimeStrategy object at 0x78b2d0073d90>.filter(lambda dt: dt.day <= max_day) to satisfy filter
      * 0.09%, gave up because: Aborted test because unable to satisfy <hypothesis.strategies._internal.datetime.DatetimeStrategy object at 0x78b2d0073d90>.filter(lambda dt: dt.day <= max_day)

  - Stopped because settings.max_examples=200000
```

Both long-running tests ran their full 200 000 examples; the invalid cases
are draws the strategies' filters aborted, not test failures. The pinned
`@example` cases passed as part of the run.

## Findings

Findings: none
