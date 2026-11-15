"""Self-tests for the shared ISO-8601 strategies; they must not use dateutil."""
from __future__ import annotations

import re
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

import pytest
from hypothesis import find, given
from hypothesis import strategies as st

import strategies_iso
from strategies_iso import (
    ISO_DATE_FORMS,
    ISO_OFFSET_FORMS,
    ISO_TIME_FORMS,
    iso_dates,
    iso_datetimes,
    iso_offsets,
    iso_times,
)

DATE_PATTERNS = {
    "YYYY": r"\d{4}",
    "YYYY-MM": r"\d{4}-\d{2}",
    "YYYY-MM-DD": r"\d{4}-\d{2}-\d{2}",
    "YYYYMMDD": r"\d{8}",
    "YYYY-Www": r"\d{4}-W\d{2}",
    "YYYYWww": r"\d{4}W\d{2}",
    "YYYY-Www-D": r"\d{4}-W\d{2}-\d",
    "YYYYWwwD": r"\d{4}W\d{2}\d",
}

TIME_PATTERNS = {
    "hh": r"\d{2}",
    "hh:mm": r"\d{2}:\d{2}",
    "hhmm": r"\d{4}",
    "hh:mm:ss": r"\d{2}:\d{2}:\d{2}",
    "hhmmss": r"\d{6}",
    "hh:mm:ss.f": r"\d{2}:\d{2}:\d{2}[.,]\d{1,6}",
    "hhmmss.f": r"\d{6}[.,]\d{1,6}",
}

OFFSET_PATTERNS = {
    "": r"",
    "Z": r"Z",
    "+HH:MM": r"[+-]\d{2}:\d{2}",
    "+HHMM": r"[+-]\d{4}",
    "+HH": r"[+-]\d{2}",
}

_DATE_BODY = r"(?:\d{4}-\d{2}-\d{2}|\d{8}|\d{4}-W\d{2}-\d|\d{4}W\d{2}\d)"
_TIME_BODY = r"\d{2}(?::?\d{2}(?::?\d{2}(?:[.,]\d{1,6})?)?)?"
_OFFSET_BODY = r"(?:Z|[+-]\d{2}(?::?\d{2})?)?"


def _date_from_text(text: str) -> date:
    """Rebuild the date a string denotes, from its digits alone."""
    compact = text.replace("-", "")
    year = int(compact[:4])
    if "W" in compact:
        week = int(compact[5:7])
        day = int(compact[7]) if len(compact) == 8 else 1
        return date.fromisocalendar(year, week, day)
    month = int(compact[4:6]) if len(compact) >= 6 else 1
    day = int(compact[6:8]) if len(compact) == 8 else 1
    return date(year, month, day)


def _time_from_text(text: str) -> time:
    """Rebuild the naive time a string denotes, fraction scaled to microseconds."""
    if "." in text or "," in text:
        text, digits = re.split(r"[.,]", text, maxsplit=1)
        microsecond = int(digits) * 10 ** (6 - len(digits))
    else:
        microsecond = 0
    digits = text.replace(":", "")
    hour = int(digits[0:2])
    minute = int(digits[2:4]) if len(digits) >= 4 else 0
    second = int(digits[4:6]) if len(digits) >= 6 else 0
    return time(hour, minute, second, microsecond)


def _split_time_and_offset(tail: str) -> tuple[str, str]:
    """Split a time-with-optional-offset string at the start of the offset."""
    if tail.endswith("Z"):
        return tail[:-1], "Z"
    match = re.search(r"[+-]\d{2}(?::?\d{2})?$", tail)
    if match is None:
        return tail, ""
    return tail[: match.start()], match.group()


def _offset_from_text(text: str) -> timedelta | None:
    """Offset denoted by an offset string, or None for the empty string."""
    if text.endswith("Z"):
        return timedelta(0)
    match = re.fullmatch(r"([+-])(\d{2}):?(\d{2})?", text)
    if match is None:
        return None
    offset = timedelta(hours=int(match.group(2)), minutes=int(match.group(3) or 0))
    return -offset if match.group(1) == "-" else offset


@pytest.mark.isoparser
@pytest.mark.parametrize("form", ISO_DATE_FORMS)
@given(data=st.data())
def test_iso_dates_form(form, data):
    text, expected, drawn_form = data.draw(iso_dates(forms=(form,)))
    assert drawn_form == form
    assert re.fullmatch(DATE_PATTERNS[form], text)
    assert type(expected) is date
    assert expected == _date_from_text(text)


@pytest.mark.isoparser
@pytest.mark.parametrize("form", ISO_TIME_FORMS)
@given(data=st.data())
def test_iso_times_form(form, data):
    text, expected, drawn_form = data.draw(iso_times(forms=(form,)))
    assert drawn_form == form
    assert re.fullmatch(TIME_PATTERNS[form], text)
    assert expected == _time_from_text(text)
    assert expected.tzinfo is None
    assert expected.hour < 24


@pytest.mark.isoparser
@pytest.mark.parametrize("form", ISO_OFFSET_FORMS)
@given(data=st.data())
def test_iso_offsets_form(form, data):
    text, expected, drawn_form = data.draw(iso_offsets(forms=(form,)))
    assert drawn_form == form
    assert re.fullmatch(OFFSET_PATTERNS[form], text)
    assert expected == _offset_from_text(text)
    if expected is not None:
        assert abs(expected) < timedelta(hours=24)
        assert expected.total_seconds() % 60 == 0


@pytest.mark.isoparser
@pytest.mark.parametrize("form", ISO_DATE_FORMS)
def test_every_date_form_is_generated(form):
    assert find(iso_dates(), lambda item: item[2] == form)[2] == form


@pytest.mark.isoparser
@pytest.mark.parametrize("form", ISO_TIME_FORMS)
def test_every_time_form_is_generated(form):
    assert find(iso_times(), lambda item: item[2] == form)[2] == form


@pytest.mark.isoparser
@pytest.mark.parametrize("form", ISO_OFFSET_FORMS)
def test_every_offset_form_is_generated(form):
    assert find(iso_offsets(), lambda item: item[2] == form)[2] == form


@pytest.mark.isoparser
@given(item=iso_datetimes())
def test_iso_datetimes_shape(item):
    text, expected = item
    assert re.fullmatch(_DATE_BODY + "T" + _TIME_BODY + _OFFSET_BODY, text)
    assert type(expected) is datetime


@pytest.mark.isoparser
@given(item=iso_datetimes())
def test_iso_datetimes_expected_value(item):
    text, expected = item
    date_text, _, tail = text.partition("T")
    time_text, offset_text = _split_time_and_offset(tail)

    assert expected.date() == _date_from_text(date_text)
    assert expected.timetz().replace(tzinfo=None) == _time_from_text(time_text)

    if offset_text == "":
        assert expected.tzinfo is None
    else:
        # Aware values must use datetime.timezone, never a dateutil tzinfo.
        assert type(expected.tzinfo) is timezone
        assert expected.utcoffset() == _offset_from_text(offset_text)


@pytest.mark.isoparser
@pytest.mark.parametrize("sep", ["T", " ", "-"])
@given(data=st.data())
def test_iso_datetimes_separator(sep, data):
    text, _ = data.draw(iso_datetimes(sep=sep))
    assert re.fullmatch(
        _DATE_BODY + re.escape(sep) + _TIME_BODY + _OFFSET_BODY, text
    )


@pytest.mark.isoparser
def test_strategies_iso_does_not_use_the_library_under_test():
    source = Path(strategies_iso.__file__).read_text(encoding="utf-8")
    assert "dateutil" not in source
