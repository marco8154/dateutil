#!/bin/sh
# Test step of the swarvex pipeline (called from swarvex.yaml). Kept in a file
# so the pipeline does not have to carry quoted arguments through its own shell.
set -e
export SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0
export TZ=America/New_York
.venv/bin/python -c "import hypothesis, tzdata; from importlib.metadata import version as v; assert (hypothesis.__version__, v('tzdata')) == ('6.170.5', '2026.6')"
# A max_examples in a test would override SWARVEX_MAX_EXAMPLES in long runs.
if grep -rn --include='*.py' 'max_examples' tests/property; then
  echo "tests/property must not set max_examples; the profile sets it" >&2
  exit 1
fi
exec .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile -n auto tests docs \
  --deselect 'tests/test_tz.py::test_gettz_link[tzpath-Europe/Monaco-Europe/Paris]' \
  --deselect 'tests/test_tzpath_data.py::test_dst_matches_tzdata_zi[tzpath]' \
  "$@"
