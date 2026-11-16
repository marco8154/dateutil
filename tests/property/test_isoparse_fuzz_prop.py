# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Fuzz target for claim P-6: ``isoparse`` only ever raises ``ValueError``."""
from datetime import datetime

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil.parser import isoparse

from strategies_iso import iso_dates, iso_datetimes

ISO_ALPHABET = "0123456789-:T.,+Z W"

OVERFLOW_REPORT = "docs/reports/p6-isoparse-overflowerror.md"


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
        if s.startswith("9999"):
            return
        raise
    assert isinstance(result, datetime)


@pytest.mark.isoparser
@pytest.mark.xfail(strict=True, raises=OverflowError, reason=OVERFLOW_REPORT)
@pytest.mark.parametrize("s", ["9999-W53-1", "9999-12-31T24:00"])
def test_isoparse_overflow_year_9999(s):
    with pytest.raises(ValueError):
        isoparse(s)
