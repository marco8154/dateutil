# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""pytest plugin that makes Hypothesis deterministic in the swarvex pipeline.

Loaded with ``-p swarvex_tools.hypothesis_profile`` from ``swarvex.yaml`` so
that upstream's ``tests/conftest.py`` stays unchanged.

Long runs (``simulation`` tasks) set ``SWARVEX_MAX_EXAMPLES``; they are then
seeded with ``--hypothesis-seed`` instead of derandomized, so that two runs
with different seeds explore different inputs.
"""
import os

from hypothesis import HealthCheck, settings

_long_run = os.environ.get("SWARVEX_MAX_EXAMPLES")

settings.register_profile(
    "swarvex",
    derandomize=_long_run is None,
    database=None,
    deadline=None,
    max_examples=int(_long_run) if _long_run else 200,
    print_blob=True,
    suppress_health_check=[HealthCheck.too_slow],
)
settings.load_profile("swarvex")
