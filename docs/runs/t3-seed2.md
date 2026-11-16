# T-3 long run — seed 2, 200 000 examples (second run)

Claim: T-3 (`docs/claims.md`) — `tzical(StringIO(s))` returns an object or
raises `ValueError` for any string, never another exception; the known
`OverflowError` path (invalid `DTSTART`, e.g. `DTSTART:1970102503000`) is
tolerated in the test. This second, independent run (different seed from the
seed-1 run in `t3-seed1.md`) checks the claim on 200 000 examples beyond that
path.

## Command

Run verbatim from the project folder (timed with `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_tzical_fuzz_prop.py::test_tzical_raises_only_valueerror" --hypothesis-seed=2 -v
```

## Environment

- Commit: `2836feab180df756f67e6102ff0e5b71d0fa7bfd` (base commit of the task;
  the sandbox has no `.git` folder and no `git` binary, so `git rev-parse HEAD`
  could not be run — this is the commit the checked-out files came from)
- Python, hypothesis, tzdata
  (`.venv/bin/python -c "import sys, hypothesis; from importlib.metadata import version; print(sys.version, hypothesis.__version__, version('tzdata'))"`):

  ```
  3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0] 6.170.5 2026.6
  ```
- `sha256sum tests/property/test_tzical_fuzz_prop.py`:

  ```
  9cb8bf5aa5284841c9faf271bbf0324263f3eb2bc668860d6b70c17f94d12845  tests/property/test_tzical_fuzz_prop.py
  ```

  (identical to the seed-1 run)
- Profile: `swarvex`, not derandomized (`SWARVEX_MAX_EXAMPLES` set), seeded
  with `--hypothesis-seed=2`, `max_examples=200000`, `database=None`,
  `deadline=None`.

## Result

- Wall time (`time`): `real 4m47.616s` (user `4m46.950s`)
- pytest summary line (verbatim):

  ```
  ======================== 1 passed in 282.59s (0:04:42) =========================
  ```

## Findings

none
