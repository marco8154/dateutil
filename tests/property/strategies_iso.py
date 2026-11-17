"""Hypothesis strategies for strings in the ISO-8601 grammar of ``isoparse``.

Each strategy yields the string together with the value it is expected to
denote.  Expected values are built with the standard library only, so that
they can be used as an oracle for ``isoparse`` without comparing the library
against itself.
"""
from __future__ import annotations

import calendar
from datetime import date, datetime, time, timedelta, timezone

from hypothesis import strategies as st

__all__ = [
    "ISO_DATE_FORMS",
    "ISO_TIME_FORMS",
    "ISO_OFFSET_FORMS",
    "iso_dates",
    "iso_times",
    "iso_offsets",
    "iso_datetimes",
]

ISO_DATE_FORMS: tuple[str, ...] = (
    "YYYY",
    "YYYY-MM",
    "YYYY-MM-DD",
    "YYYYMMDD",
    "YYYY-Www",
    "YYYYWww",
    "YYYY-Www-D",
    "YYYYWwwD",
)

ISO_TIME_FORMS: tuple[str, ...] = (
    "hh",
    "hh:mm",
    "hhmm",
    "hh:mm:ss",
    "hhmmss",
    "hh:mm:ss.f",
    "hhmmss.f",
)

# "" means "no offset"; the sign of the ± forms is drawn per value.
ISO_OFFSET_FORMS: tuple[str, ...] = ("", "Z", "+HH:MM", "+HHMM", "+HH")

_WEEK_DAY_FORMS = frozenset(("YYYY-Www-D", "YYYYWwwD"))
_SECOND_FORMS = frozenset(("hh:mm:ss", "hhmmss", "hh:mm:ss.f", "hhmmss.f"))
_FRACTION_FORMS = frozenset(("hh:mm:ss.f", "hhmmss.f"))

FULL_DATE_FORMS = ("YYYY-MM-DD", "YYYYMMDD", "YYYY-Www-D", "YYYYWwwD")
WEEK_DATE_FORMS = ("YYYY-Www", "YYYYWww", "YYYY-Www-D", "YYYYWwwD")


def _weeks_in_year(year: int) -> int:
    """Number of ISO weeks in ``year``; 28 December is always in the last one."""
    return date(year, 12, 28).isocalendar()[1]


def _max_iso_day(year: int, week: int) -> int:
    """Last ISO weekday that exists in ``year``-W``week``.

    ``date.max`` cuts the final week of ISO year 9999 short.
    """
    week_start = date.fromisocalendar(year, week, 1).toordinal()
    return min(7, date.max.toordinal() - week_start + 1)


@st.composite
def iso_dates(
    draw, forms: tuple[str, ...] = ISO_DATE_FORMS
) -> tuple[str, date, str]:
    """A date string, the date it denotes and the form it was built in."""
    form = draw(st.sampled_from(tuple(forms)))
    year = draw(st.integers(1, 9999))

    if form in WEEK_DATE_FORMS:
        week = draw(st.integers(1, _weeks_in_year(year)))
        if form in _WEEK_DAY_FORMS:
            day = draw(st.integers(1, _max_iso_day(year, week)))
            sep = "-" if "-" in form else ""
            return f"{year:04d}{sep}W{week:02d}{sep}{day}", date.fromisocalendar(
                year, week, day
            ), form
        sep = "-" if "-" in form else ""
        # Without a day the ISO week defaults to its first day, Monday.
        return (
            f"{year:04d}{sep}W{week:02d}",
            date.fromisocalendar(year, week, 1),
            form,
        )

    if form == "YYYY":
        return f"{year:04d}", date(year, 1, 1), form

    month = draw(st.integers(1, 12))
    if form == "YYYY-MM":
        return f"{year:04d}-{month:02d}", date(year, month, 1), form

    day = draw(st.integers(1, calendar.monthrange(year, month)[1]))
    if form == "YYYY-MM-DD":
        return f"{year:04d}-{month:02d}-{day:02d}", date(year, month, day), form

    return f"{year:04d}{month:02d}{day:02d}", date(year, month, day), form


@st.composite
def iso_times(
    draw, forms: tuple[str, ...] = ISO_TIME_FORMS
) -> tuple[str, time, str]:
    """A time string, the naive time it denotes and the form it was built in."""
    form = draw(st.sampled_from(tuple(forms)))
    # 24 is only valid as 24:00 and is covered by its own claim.
    hour = draw(st.integers(0, 23))
    minute = draw(st.integers(0, 59)) if form != "hh" else 0
    second = draw(st.integers(0, 59)) if form in _SECOND_FORMS else 0

    sep = ":" if ":" in form else ""
    text = f"{hour:02d}"
    if form != "hh":
        text += f"{sep}{minute:02d}"
    if form in _SECOND_FORMS:
        text += f"{sep}{second:02d}"

    microsecond = 0
    if form in _FRACTION_FORMS:
        digits = draw(
            st.integers(1, 6).flatmap(
                lambda n: st.integers(0, 10**n - 1).map(lambda v: f"{v:0{n}d}")
            )
        )
        text += draw(st.sampled_from(".,")) + digits
        # The digits are a decimal fraction of a second: "5" means 500000 µs.
        microsecond = int(digits) * 10 ** (6 - len(digits))

    return text, time(hour, minute, second, microsecond), form


@st.composite
def iso_offsets(
    draw, forms: tuple[str, ...] = ISO_OFFSET_FORMS
) -> tuple[str, timedelta | None, str]:
    """An offset string, its offset as a timedelta (``None`` if absent), form."""
    form = draw(st.sampled_from(tuple(forms)))
    if form == "":
        return "", None, form
    if form == "Z":
        return "Z", timedelta(0), form

    sign = draw(st.sampled_from("+-"))
    # Hours up to 23 with at most 59 minutes keep |offset| strictly under 24 h.
    hours = draw(st.integers(0, 23))
    minutes = draw(st.integers(0, 59)) if form != "+HH" else 0
    if form == "+HH:MM":
        text = f"{sign}{hours:02d}:{minutes:02d}"
    elif form == "+HHMM":
        text = f"{sign}{hours:02d}{minutes:02d}"
    else:
        text = f"{sign}{hours:02d}"
    offset = timedelta(hours=hours, minutes=minutes)
    return text, -offset if sign == "-" else offset, form


@st.composite
def iso_datetimes(draw, sep: str = "T") -> tuple[str, datetime]:
    """A full datetime string and the datetime it denotes.

    Only complete date forms are used; the compact and the extended style are
    mixed freely because the documented grammar does not forbid it.
    """
    date_str, expected_date, _ = draw(iso_dates(forms=FULL_DATE_FORMS))
    time_str, expected_time, _ = draw(iso_times())
    offset_str, offset, _ = draw(iso_offsets())

    if offset is None:
        expected = datetime.combine(expected_date, expected_time)
    else:
        # A stdlib timezone keeps the expected value independent of the parser.
        expected = datetime.combine(
            expected_date, expected_time, tzinfo=timezone(offset)
        )

    return date_str + sep + time_str + offset_str, expected
