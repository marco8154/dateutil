"""Golden tests for claim R-1 of ``dateutil.rrule``.

R-1: for every RRULE example of RFC 5545, section 3.8.5.3, ``rrulestr``
yields exactly the occurrences listed in the RFC.
"""
import itertools
import json
from datetime import datetime
from pathlib import Path

import pytest

from dateutil import tz
from dateutil.rrule import rrulestr

DATA_FILES = sorted(
    Path(__file__).parent.joinpath("data").glob("rfc5545_rrule_examples_*.json")
)


def _load_examples():
    examples = []
    for path in DATA_FILES:
        with path.open(encoding="utf-8") as f:
            examples.extend(json.load(f)["examples"])
    return examples


EXAMPLES = _load_examples()


@pytest.mark.rrule
@pytest.mark.rrulestr
@pytest.mark.parametrize(
    "example", EXAMPLES, ids=[example["id"] for example in EXAMPLES]
)
def test_rrulestr_matches_rfc5545_example(example):
    expected = example["expected"]
    if not expected:
        pytest.skip("RFC lists no occurrences")

    zone = tz.gettz(example["tzid"])
    dtstart = datetime.fromisoformat(example["dtstart"]).replace(tzinfo=zone)
    rule = rrulestr(example["rrule"], dtstart=dtstart)

    if example["complete"]:
        got = list(rule)
    else:
        got = list(itertools.islice(rule, len(expected)))

    # Wall times, not UTC: the examples span DST transitions.
    assert [t.replace(tzinfo=None) for t in got] == [
        datetime.fromisoformat(e) for e in expected
    ]
    assert all(t.tzinfo is zone for t in got)


def test_data_files_present():
    assert len(DATA_FILES) == 2
    assert len(EXAMPLES) == 42
