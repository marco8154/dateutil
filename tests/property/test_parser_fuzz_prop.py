"""Fuzz target for claim P-7: ``parse(s)`` only raises the documented errors."""
from datetime import datetime

from hypothesis import example, given
from hypothesis import strategies as st

import pytest

from dateutil.parser import ParserError, parse, parserinfo

_info = parserinfo()

_words = sorted(
    {name for names in _info.MONTHS + _info.WEEKDAYS for name in names}
    | {"AM", "PM", "UTC", "Z", "of", "at", "on"}
)

token = st.one_of(
    st.integers(-10**12, 10**12).map(str),
    st.sampled_from(_words),
    st.sampled_from(["+05:30", "-0800", "+00", "-23:59", "+1400"]),
    st.sampled_from([":", "/", "-", ".", ","]),
    st.text(alphabet="0123456789:./-+ ", max_size=12),
)

fuzz_strings = st.one_of(
    st.text(),
    st.lists(token, min_size=1, max_size=8).map(" ".join),
)


# UnknownTimezoneWarning is the documented reaction to unknown zone names,
# not an exception, so it must not turn into one here.
@pytest.mark.filterwarnings("ignore::dateutil.parser.UnknownTimezoneWarning")
@given(fuzz_strings)
@example("")
@example("99999999999999999999")
@example("Dec 31 9999 24:00")
@example("9999-12-31 23:59 -2359")
def test_parse_raises_only_documented_errors(s):
    try:
        result = parse(s)
    except (ParserError, OverflowError):
        return
    assert isinstance(result, datetime)
