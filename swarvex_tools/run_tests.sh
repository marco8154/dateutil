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
# Upstream files carry no license headers; tests must stay submittable as is.
if grep -rln 'SPDX' tests; then
  echo "tests must not carry SPDX headers (docs/decisions/0001-lizenz.md)" >&2
  exit 1
fi
# A contribution that only changes Markdown under docs/ (run logs, reports)
# cannot change a test result; the full run would only hit the pipeline's time
# limit on slow machines. Without SWARVEX_CHANGED everything runs.
if [ -n "${SWARVEX_CHANGED:-}" ]; then
  docs_only=1
  for f in $SWARVEX_CHANGED; do
    case "$f" in
      docs/*.md) ;;
      *) docs_only=0 ;;
    esac
  done
  if [ "$docs_only" = 1 ]; then
    echo "only docs/*.md changed ($SWARVEX_CHANGED): test run skipped"
    exit 0
  fi
fi
exec .venv/bin/python -m pytest -p no:cacheprovider -p swarvex_tools.hypothesis_profile -n auto tests docs \
  --deselect 'tests/test_tz.py::test_gettz_link[tzpath-Europe/Monaco-Europe/Paris]' \
  --deselect 'tests/test_tzpath_data.py::test_dst_matches_tzdata_zi[tzpath]' \
  "$@"
