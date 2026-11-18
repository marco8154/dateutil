# Run log: D-1/D-2.1 relativedelta long run, seed 2 (second run)

Claims: D-1, D-2 and D-2.1 (`docs/claims.md`), tests
`tests/property/test_relativedelta_prop.py::test_matches_timedelta`,
`tests/property/test_relativedelta_prop.py::test_add_then_subtract` and
`tests/property/test_relativedelta_prop.py::test_add_then_subtract_calendar`
(unchanged).

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_relativedelta_prop.py --hypothesis-seed=2 -v --hypothesis-show-statistics
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

- Runtime: `real 6m33.002s` (shell `time`; `user 6m32.762s`, `sys 0m0.199s`);
  pytest reported 387.94s (0:06:27).
- Exit code: 0
- pytest summary line, verbatim:

```
=================== 2 passed, 1 xfailed in 387.94s (0:06:27) ===================
```

- Hypothesis statistics for
  `tests/property/test_relativedelta_prop.py::test_matches_timedelta`:

```
  - during generate phase (256.88 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 200000 passing, 0 failing, and 71016 invalid test cases

  - Stopped because settings.max_examples=200000
```

- Hypothesis statistics for
  `tests/property/test_relativedelta_prop.py::test_add_then_subtract_calendar`:

```
  - during generate phase (130.05 seconds):
    - Typical runtimes: < 1ms, of which < 1ms in data generation
    - 200000 passing, 0 failing, and 192 invalid test cases

  - Stopped because settings.max_examples=200000
```

- `tests/property/test_relativedelta_prop.py::test_add_then_subtract`
  (`xfail(strict=True)`, D-2 refuted) shows no Hypothesis statistics: it
  ended on its pinned `@example` as expected, which is not a finding.

Both non-xfail tests ran their full 200 000 examples; the invalid cases are
draws the strategies' filters aborted, not test failures. The pinned
`@example` cases of both tests passed as part of the run.

## Findings

Findings: none
