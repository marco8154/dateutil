# T-1 long run — seed 1, 200 000 examples (first run)

Claim: T-1 (`docs/claims.md`) — `tzstr(s)` returns a `tzinfo` or raises
`ValueError` for any string, never another exception; the two known
`TypeError` paths (`UTC`/`GMT` and the comma alt-format without a standard
offset) are tolerated in the test. This run checks the claim on 200 000
examples beyond those two paths.

## Command

Run verbatim from the project folder (timed with `time`):

```
SWARVEX_MAX_EXAMPLES=200000 TZ=America/New_York SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0 .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile "tests/property/test_tzstr_fuzz_prop.py::test_tzstr_raises_only_valueerror" --hypothesis-seed=1 -v
```

## Environment

- Commit: `792675b03e70edc4e18c314dffa98464e92bdb3d` (the task environment
  ships the files without a `.git` folder and without `git`, so
  `git rev-parse HEAD` could not be run; this is the commit the task states
  the files are at)
- Python / hypothesis / tzdata
  (`import sys, hypothesis; from importlib.metadata import version; print(sys.version, hypothesis.__version__, version('tzdata'))`):
  `3.13.18 (main, Nov  5 2026, 07:59:38) [GCC 14.2.0] 6.170.5 2026.6`
- `sha256sum tests/property/test_tzstr_fuzz_prop.py`:
  `2fed937fe496646e19397c46153473062faaa9323f8e9056bdfaa3de043a779d`
- Profile: `swarvex`, not derandomized (`SWARVEX_MAX_EXAMPLES` set), seeded
  with `--hypothesis-seed=1`, `max_examples=200000`, `database=None`,
  `deadline=None`.

## Result

Runtime: `real 2m8.177s` (wall clock, `time`); pytest reported the test
itself as `123.81s`.

pytest summary line (verbatim):

```
======================== 1 passed in 123.81s (0:02:03) =========================
```

## Findings

none
