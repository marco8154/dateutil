import io
import re

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil import tz

SEED = "\n".join([
    "BEGIN:VTIMEZONE",
    "TZID:Test/Zone",
    "BEGIN:STANDARD",
    "DTSTART:19701025T030000",
    "TZOFFSETFROM:+0200",
    "TZOFFSETTO:+0100",
    "TZNAME:CET",
    "RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU",
    "END:STANDARD",
    "BEGIN:DAYLIGHT",
    "DTSTART:19700329T020000",
    "TZOFFSETFROM:+0100",
    "TZOFFSETTO:+0200",
    "TZNAME:CEST",
    "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU",
    "END:DAYLIGHT",
    "END:VTIMEZONE",
])

MUTATION_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ:;=-+0123456789"


@st.composite
def mutated_lines(draw):
    """SEED with one line deleted, duplicated or replaced."""
    lines = SEED.splitlines()
    operation = draw(st.sampled_from(("delete", "duplicate", "replace")))
    i = draw(st.integers(0, len(lines) - 1))
    if operation == "delete":
        del lines[i]
    elif operation == "duplicate":
        lines.insert(i, lines[i])
    else:
        lines[i] = draw(st.text(alphabet=MUTATION_ALPHABET, max_size=30))
    return "\n".join(lines)


@st.composite
def mutated_chars(draw):
    """SEED with 1-4 characters deleted or inserted at drawn positions."""
    s = SEED
    for _ in range(draw(st.integers(1, 4))):
        if draw(st.booleans()):
            i = draw(st.integers(0, len(s)))
            s = s[:i] + draw(st.sampled_from(MUTATION_ALPHABET)) + s[i:]
        elif s:
            i = draw(st.integers(0, len(s) - 1))
            s = s[:i] + s[i + 1:]
    return s


def fuzz_strings():
    return st.one_of(
        st.text(),
        mutated_lines(),
        mutated_chars(),
    )


# Inputs of the finding pinned as an xfail test below; OverflowError is
# tolerated for them only, so that any other finding still fails the run.
# See docs/reports/t3-tzical-overflowerror.md.
_DTSTART_VALUE = re.compile(r"\d{8}T\d{6}")


def _has_invalid_dtstart(s):
    for line in s.splitlines():
        name, sep, value = line.partition(":")
        if sep and name.split(";", 1)[0].strip().upper() == "DTSTART":
            if not _DTSTART_VALUE.fullmatch(value):
                return True
    return False


DTSTART_OVERFLOW_INPUT = SEED.replace(
    "DTSTART:19701025T030000", "DTSTART:1970102503000")


def test_seed_is_valid():
    assert tz.tzical(io.StringIO(SEED)).get() is not None


@given(s=fuzz_strings())
@example(DTSTART_OVERFLOW_INPUT)
def test_tzical_raises_only_valueerror(s):
    try:
        tz.tzical(io.StringIO(s))
    except ValueError:
        pass
    except OverflowError:
        if _has_invalid_dtstart(s):
            return
        raise


@pytest.mark.xfail(
    strict=True,
    raises=OverflowError,
    reason="dateutil/dateutil#1683, docs/reports/t3-tzical-overflowerror.md",
)
def test_tzical_dtstart_overflow():
    try:
        tz.tzical(io.StringIO(DTSTART_OVERFLOW_INPUT))
    except ValueError:
        pass
