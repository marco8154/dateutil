"""Check the brute-force reference against the RFC 5545 RRULE examples.

The rule text is translated by a small parser local to this file; nothing from
the library under test is used.
"""

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from rrule_reference import expand

DATA = Path(__file__).parent / "data"
WEEKDAYS = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}
IN_SCOPE_FREQS = ("YEARLY", "MONTHLY", "WEEKLY", "DAILY")
OUT_OF_SCOPE_PARTS = ("BYWEEKNO", "BYYEARDAY")


def _load():
    examples = []
    for name in ("rfc5545_rrule_examples_1.json", "rfc5545_rrule_examples_2.json"):
        examples.extend(json.loads((DATA / name).read_text())["examples"])
    return examples


def _parse_until(value, tzid):
    if value.endswith("Z"):
        utc = datetime.strptime(value, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        return utc.astimezone(ZoneInfo(tzid)).replace(tzinfo=None)
    if "T" in value:
        return datetime.strptime(value, "%Y%m%dT%H%M%S")
    day = datetime.strptime(value, "%Y%m%d")
    return day.replace(hour=23, minute=59, second=59)


def _parse_byday(value):
    terms = []
    for term in value.split(","):
        match = re.fullmatch(r"([+-]?\d+)?(MO|TU|WE|TH|FR|SA|SU)", term)
        weekday = WEEKDAYS[match.group(2)]
        terms.append((weekday, int(match.group(1))) if match.group(1) else weekday)
    return terms


def _ints(value):
    return [int(v) for v in value.split(",")]


def parse_rule(text, tzid="UTC"):
    """Translate an RRULE value into keyword arguments for ``expand``."""
    parts = dict(item.split("=", 1) for item in text.split(";"))
    kwargs = {"freq": parts["FREQ"]}
    if "INTERVAL" in parts:
        kwargs["interval"] = int(parts["INTERVAL"])
    if "COUNT" in parts:
        kwargs["count"] = int(parts["COUNT"])
    if "UNTIL" in parts:
        kwargs["until"] = _parse_until(parts["UNTIL"], tzid)
    if "WKST" in parts:
        kwargs["wkst"] = WEEKDAYS[parts["WKST"]]
    if "BYMONTH" in parts:
        kwargs["bymonth"] = _ints(parts["BYMONTH"])
    if "BYMONTHDAY" in parts:
        kwargs["bymonthday"] = _ints(parts["BYMONTHDAY"])
    if "BYDAY" in parts:
        kwargs["byweekday"] = _parse_byday(parts["BYDAY"])
    if "BYHOUR" in parts:
        kwargs["byhour"] = _ints(parts["BYHOUR"])
    if "BYMINUTE" in parts:
        kwargs["byminute"] = _ints(parts["BYMINUTE"])
    if "BYSECOND" in parts:
        kwargs["bysecond"] = _ints(parts["BYSECOND"])
    if "BYSETPOS" in parts:
        kwargs["bysetpos"] = _ints(parts["BYSETPOS"])
    return kwargs


def _in_scope(entry):
    parts = {item.split("=", 1)[0]: item.split("=", 1)[1]
             for item in entry["rrule"].split(";")}
    return (parts["FREQ"] in IN_SCOPE_FREQS
            and not any(p in parts for p in OUT_OF_SCOPE_PARTS))


CASES = [pytest.param(e, id=e["id"]) for e in _load()]


@pytest.mark.parametrize("entry", CASES)
def test_reference_matches_rfc_example(entry):
    if not _in_scope(entry) or not entry["expected"]:
        pytest.skip("outside the reference scope")

    expected = [datetime.fromisoformat(v) for v in entry["expected"]]
    kwargs = parse_rule(entry["rrule"], entry["tzid"])
    if "count" not in kwargs and "until" not in kwargs:
        kwargs["until"] = expected[-1]
    result = expand(dtstart=datetime.fromisoformat(entry["dtstart"]), **kwargs)

    if entry["complete"]:
        assert result == expected
    else:
        assert result[:len(expected)] == expected
