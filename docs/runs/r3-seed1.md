# Run log: R-3 rrule query long run, seed 1 (first run)

Claim: R-3 (`docs/claims.md`), tests `tests/property/test_rrule_query_prop.py` (unchanged):
`test_count_matches_list`, `test_before_after`, `test_between`,
`test_queries_on_complete_cache`.

## Command

Run in the project folder, verbatim (wrapped in the shell's `time`):

```
SWARVEX_MAX_EXAMPLES=20000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile tests/property/test_rrule_query_prop.py --hypothesis-seed=1 -v --hypothesis-show-statistics
```

## Environment

- Commit: `e44c22fc4303724e28d48e55e78467aaa13ce6b1` (task base commit;
  `git rev-parse HEAD` was not available: the sandbox has no `git` and no
  `.git` folder)
- Python: `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0]`
- hypothesis: `6.170.5`
- tzdata: `2026.6`
- `sha256sum tests/property/test_rrule_query_prop.py`:
  `6271dd91f91779d8ed84ba54ff223eb13a5b50a2db6f6c5adeba1bcae6d3a524  tests/property/test_rrule_query_prop.py`
- Hypothesis profile line from pytest:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=20000, suppress_health_check=(HealthCheck.too_slow,)`

## Result

- Runtime: `real 77m55.091s` (shell `time`; `user 77m53.622s`, `sys 0m0.899s`);
  pytest reported 4670.46s (1:17:50).
- Exit code: 0
- pytest summary line, verbatim:

```
======================== 7 passed in 4670.46s (1:17:50) =========================
```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_count_matches_list[False]`:

  ```
    - during generate phase (679.79 seconds):
      - Typical runtimes: ~ 3-21 ms, of which ~ 2-5 ms in data generation
      - 20000 passing, 0 failing, and 3634 invalid test cases
      - Events:
        * 5.38%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.77%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 2.07%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.54%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.88%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.25%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.23%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.11%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.09%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.00%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)

    - Stopped because settings.max_examples=20000
  ```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_count_matches_list[True]`:

  ```
    - during generate phase (690.64 seconds):
      - Typical runtimes: ~ 3-22 ms, of which ~ 2-5 ms in data generation
      - 20000 passing, 0 failing, and 3634 invalid test cases
      - Events:
        * 5.38%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.77%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 2.07%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.54%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.88%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.25%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.23%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.11%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.09%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.00%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)

    - Stopped because settings.max_examples=20000
  ```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_before_after[False]`:

  ```
    - during generate phase (669.19 seconds):
      - Typical runtimes: ~ 4-34 ms, of which ~ 2-6 ms in data generation
      - 20000 passing, 0 failing, and 7874 invalid test cases
      - Events:
        * 5.48%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.68%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.88%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.57%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.86%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.60%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.20%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.19%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.18%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.09%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy integers(1, 31).filter(lambda value: value != anchor)

    - Stopped because settings.max_examples=20000
  ```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_before_after[True]`:

  ```
    - during generate phase (627.76 seconds):
      - Typical runtimes: ~ 4-30 ms, of which ~ 2-6 ms in data generation
      - 20000 passing, 0 failing, and 7874 invalid test cases
      - Events:
        * 5.48%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.68%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.88%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.57%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.86%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.60%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.20%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.19%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.18%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.09%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy integers(1, 31).filter(lambda value: value != anchor)

    - Stopped because settings.max_examples=20000
  ```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_between[False]`:

  ```
    - during generate phase (601.51 seconds):
      - Typical runtimes: ~ 5-35 ms, of which ~ 3-7 ms in data generation
      - 20000 passing, 0 failing, and 8471 invalid test cases
      - Events:
        * 5.62%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.30%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.94%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.68%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.05%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.74%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.34%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.16%, gave up because: Aborted test because unable to satisfy one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list)
        * 0.14%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.12%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.04%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy integers(1, 31).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.01%, gave up because: Aborted test because unable to satisfy integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.00%, gave up because: Aborted test because unable to satisfy integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)

    - Stopped because settings.max_examples=20000
  ```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_between[True]`:

  ```
    - during generate phase (574.44 seconds):
      - Typical runtimes: ~ 5-31 ms, of which ~ 3-7 ms in data generation
      - 20000 passing, 0 failing, and 8471 invalid test cases
      - Events:
        * 5.62%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.30%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.94%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.68%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.05%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.74%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.34%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.16%, gave up because: Aborted test because unable to satisfy one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list)
        * 0.14%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.12%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.04%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy integers(1, 31).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.01%, gave up because: Aborted test because unable to satisfy integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.00%, gave up because: Aborted test because unable to satisfy integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)

    - Stopped because settings.max_examples=20000
  ```

- Hypothesis statistics for
  `tests/property/test_rrule_query_prop.py::test_queries_on_complete_cache`:

  ```
    - during generate phase (826.47 seconds):
      - Typical runtimes: ~ 6-24 ms, of which ~ 3-7 ms in data generation
      - 20000 passing, 0 failing, and 8059 invalid test cases
      - Events:
        * 5.24%, Retried draw from integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 4.18%, Retried draw from integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 1.79%, Retried draw from one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list) to satisfy filter
        * 1.48%, Retried draw from integers(0, 23).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.85%, Retried draw from integers(0, 59).filter(lambda value: value != anchor).filter(not_yet_in_unique_list) to satisfy filter
        * 0.77%, gave up because: Aborted test because unable to satisfy integers(1, 12).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.47%, gave up because: Aborted test because unable to satisfy integers(0, 6).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.40%, gave up because: Aborted test because unable to satisfy one_of(integers(min_value=-31, max_value=-1).filter(lambda value: value != anchor), integers(min_value=1, max_value=31).filter(lambda value: value != anchor)).filter(not_yet_in_unique_list)
        * 0.19%, Retried draw from integers(-31, -1).filter(lambda value: value != anchor) to satisfy filter
        * 0.14%, Retried draw from integers(1, 31).filter(lambda value: value != anchor) to satisfy filter
        * 0.08%, gave up because: Aborted test because unable to satisfy integers(-31, -1).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)
        * 0.02%, gave up because: Aborted test because unable to satisfy integers(1, 31).filter(lambda value: value != anchor).filter(not_yet_in_unique_list)

    - Stopped because settings.max_examples=20000
  ```

All seven tests ran their full 20 000 examples; the invalid cases are draws
the strategy's filters aborted, not test failures.

## Findings

Findings: none
