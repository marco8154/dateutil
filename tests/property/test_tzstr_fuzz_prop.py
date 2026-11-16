import re
import warnings

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil import tz

SEEDS = [
    "EST5EDT",
    "EST5EDT,M3.2.0,M11.1.0",
    "<-03>3",
    "EET-2EEST,M3.4.4/50,M10.4.4/50",
    "IST-1GMT0,M10.5.0,M3.5.0/1",
    "UTC0",
    "GMT+3",
    "EST5EDT,4,0,6,7200,10,0,26,7200,3600",
]

MUTATION_ALPHABET = "ESTDTGMUC<>0123456789+-:,/.MJ"


@st.composite
def mutated_seed(draw):
    """A valid TZ string with 1-3 characters deleted, replaced or inserted."""
    s = draw(st.sampled_from(SEEDS))
    for _ in range(draw(st.integers(1, 3))):
        operation = draw(st.sampled_from(("delete", "replace", "insert")))
        if operation == "insert":
            i = draw(st.integers(0, len(s)))
            s = s[:i] + draw(st.sampled_from(MUTATION_ALPHABET)) + s[i:]
        elif s:
            i = draw(st.integers(0, len(s) - 1))
            if operation == "delete":
                s = s[:i] + s[i + 1:]
            else:
                s = s[:i] + draw(st.sampled_from(MUTATION_ALPHABET)) + s[i + 1:]
    return s


def fuzz_strings():
    return st.one_of(
        st.text(),
        st.text(alphabet=MUTATION_ALPHABET, max_size=40),
        mutated_seed(),
    )


# Inputs of the findings pinned as xfail tests below; TypeError is tolerated
# for them only, so that any other finding still fails the run.
# See docs/reports/t1-tzstr-typeerror.md.
def _gmt_utc_without_offset(s):
    return re.fullmatch(r"(?:GMT|UTC)[,:]*", s) is not None


def _deprecated_format_without_offset(s):
    # The non-standard comma format is reached with 8-9 commas; the standard
    # offset is missing when the part before the first comma has no digits.
    return 8 <= s.count(",") <= 9 and not any(c.isdigit() for c in s.split(",")[0])


@pytest.mark.tzstr
@given(s=fuzz_strings())
@example("UTC")
@example("GMT")
@example("EST,4,0,6,7200,10,0,26,7200,3600")
def test_tzstr_raises_only_valueerror(s):
    with warnings.catch_warnings():
        # The deprecated comma format warns instead of failing, by contract.
        warnings.simplefilter("ignore", tz.DeprecatedTzFormatWarning)
        try:
            tz.tzstr(s)
        except ValueError:
            pass
        except TypeError:
            if _gmt_utc_without_offset(s) or _deprecated_format_without_offset(s):
                return
            raise


@pytest.mark.tzstr
@pytest.mark.xfail(
    strict=True,
    raises=TypeError,
    reason="docs/reports/t1-tzstr-typeerror.md",
)
@pytest.mark.parametrize("s", ["UTC", "GMT"])
def test_tzstr_gmt_utc_without_offset(s):
    try:
        tz.tzstr(s)
    except ValueError:
        pass


@pytest.mark.tzstr
@pytest.mark.xfail(
    strict=True,
    raises=TypeError,
    reason="docs/reports/t1-tzstr-typeerror.md",
)
def test_tzstr_deprecated_format_without_offset():
    try:
        tz.tzstr(",0,0,0,0,0,0,0,0,0")
    except ValueError:
        pass
