"""Fuzz target for claim P-6: ``isoparse`` only ever raises ``ValueError``."""
import re
from datetime import datetime

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.parser import isoparse

from strategies_iso import iso_dates, iso_datetimes

ISO_ALPHABET = "0123456789-:T.,+Z W"

OVERFLOW_REPORT = "dateutil/dateutil#1684, docs/reports/p6-isoparse-overflowerror.md"

# The two forms of the known finding: a week date after 9999-12-31, and hour
# 24 on 9999-12-31 in any of its calendar, ordinal or week date spellings.
KNOWN_OVERFLOW = re.compile(
    r"9999(-?W53(-?[1-7])?|-?W52-?[67]"
    r"|(-12-31|1231|-?365|-?W52-?5)[T ]24)"
)


@st.composite
def mutated_iso_strings(draw):
    """A valid ISO string with one character deleted, replaced or inserted."""
    s = draw(st.one_of(iso_datetimes(), iso_dates()))[0]
    op = draw(st.sampled_from(("delete", "replace", "insert")))
    if op == "insert":
        pos = draw(st.integers(0, len(s)))
        return s[:pos] + draw(st.sampled_from(ISO_ALPHABET)) + s[pos:]
    pos = draw(st.integers(0, len(s) - 1))
    if op == "delete":
        return s[:pos] + s[pos + 1:]
    return s[:pos] + draw(st.sampled_from(ISO_ALPHABET)) + s[pos + 1:]


fuzz_strings = st.one_of(
    st.text(),
    st.text(alphabet=ISO_ALPHABET),
    mutated_iso_strings(),
)


@pytest.mark.isoparser
@given(s=fuzz_strings)
@example(s="9999-W53-1")
@example(s="9999-12-31T24:00")
def test_isoparse_raises_only_valueerror(s):
    try:
        result = isoparse(s)
    except ValueError:
        return
    except OverflowError:
        # Known finding, see OVERFLOW_REPORT; any other overflow is new.
        if KNOWN_OVERFLOW.match(s):
            return
        raise
    assert isinstance(result, datetime)


@pytest.mark.isoparser
@pytest.mark.xfail(strict=True, raises=OverflowError, reason=OVERFLOW_REPORT)
@pytest.mark.parametrize("s", [
    "9999-W53-1",
    "9999-W52-6",
    "9999-12-31T24:00",
    "9999-12-31 24:00",
    "9999-365T24:00",
])
def test_isoparse_overflow_year_9999(s):
    with pytest.raises(ValueError):
        isoparse(s)


@pytest.mark.parametrize("s, known", [
    ("9999-W53-1", True),
    ("9999W537", True),
    ("9999-W53", True),
    ("9999-W52-6", True),
    ("9999-W52-7", True),
    ("9999-12-31T24", True),
    ("99991231T2400", True),
    ("9999-12-31 24:00", True),
    ("9999-12-31T24:00:00.000+05:00", True),
    ("9999-365T24:00", True),
    ("9999365T24", True),
    ("9999-W52-5T24", True),
    ("9999-W52-5", False),
    ("9999-12-31T23:59", False),
    ("9999-12-30T24:00", False),
    ("9998-W53-1", False),
])
def test_known_overflow_pattern(s, known):
    assert bool(KNOWN_OVERFLOW.match(s)) is known
