# T-1 long run: `tzstr` fuzz target, 200 000 examples, seed 2 (second run)

Claim: T-1 (`docs/claims.md`) — `tz.tzstr(s)` returns a `tzinfo` or raises
`ValueError` for any string. The two known `TypeError` paths (`tzstr("UTC")` /
`tzstr("GMT")` and the comma format without a standard offset) are tolerated by
the test; everything else must pass.

## Command

Run from the project folder; wall time measured with `time`:

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_tzstr_fuzz_prop.py::test_tzstr_raises_only_valueerror" --hypothesis-seed=2 -v
```

## Environment

- Commit: `792675b03e70edc4e18c314dffa98464e92bdb3d` (base commit of the task;
  the sandbox has no `.git` folder and no `git` binary, so `git rev-parse HEAD`
  could not be run — this is the commit the checked-out files came from)
- Python, hypothesis, tzdata
  (`.venv/bin/python -c "import sys, hypothesis; from importlib.metadata import version; print(sys.version, hypothesis.__version__, version('tzdata'))"`):

  ```
  3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0] 6.170.5 2026.6
  ```
- `sha256sum tests/property/test_tzstr_fuzz_prop.py`:

  ```
  2fed937fe496646e19397c46153473062faaa9323f8e9056bdfaa3de043a779d  tests/property/test_tzstr_fuzz_prop.py
  ```

## Result

- Wall time (`time`): `real 2m6.796s` (user `2m6.605s`)
- Profile line of the run:
  `hypothesis profile 'swarvex' -> database=None, deadline=None, print_blob=True, max_examples=200000, suppress_health_check=(HealthCheck.too_slow,)`
- pytest summary line, verbatim:

  ```
  ======================== 1 passed in 122.76s (0:02:02) =========================
  ```

## Findings

none
