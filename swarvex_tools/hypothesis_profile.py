# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""pytest plugin that makes Hypothesis deterministic in the swarvex pipeline.

Loaded with ``-p swarvex_tools.hypothesis_profile`` from ``swarvex.yaml`` so
that upstream's ``tests/conftest.py`` stays unchanged.
"""
from hypothesis import HealthCheck, settings

settings.register_profile(
    "swarvex",
    derandomize=True,
    database=None,
    deadline=None,
    max_examples=200,
    print_blob=True,
    suppress_health_check=[HealthCheck.too_slow],
)
settings.load_profile("swarvex")
