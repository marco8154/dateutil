"""Shared Hypothesis strategies for finite ``dateutil.rrule.rrule`` rules.

Yields keyword argument dictionaries that can be passed straight to
``rrule(**kw)``. Every rule is finite (bounded by ``until``) and small
(well below 1000 occurrences), and every set ``byxxx`` filter is anchored
on ``dtstart`` so the rule can never turn out empty.

Expected values are never derived from dateutil itself; only the frequency
constants are imported from it.
"""

import calendar
from datetime import datetime, timedelta

from hypothesis import strategies as st

from dateutil.rrule import (
    DAILY,
    HOURLY,
    MINUTELY,
    MONTHLY,
    SECONDLY,
    WEEKLY,
    YEARLY,
)

FREQS = (YEARLY, MONTHLY, WEEKLY, DAILY, HOURLY, MINUTELY, SECONDLY)

# ``until = dtstart + UNTIL_WINDOW[freq]`` keeps every rule small: at most a
# few hundred occurrences, even before any ``byxxx`` filtering.
UNTIL_WINDOW: dict[int, timedelta] = {
    YEARLY: timedelta(days=73049),    # about 200 years
    MONTHLY: timedelta(days=18262),   # about 50 years
    WEEKLY: timedelta(weeks=600),
    DAILY: timedelta(days=600),
    HOURLY: timedelta(hours=600),
    MINUTELY: timedelta(minutes=600),
    SECONDLY: timedelta(seconds=600),
}

FILTER_KEYS: tuple[str, ...] = (
    "bymonth",
    "bymonthday",
    "byweekday",
    "byhour",
    "byminute",
    "bysecond",
)

_DOMAINS = {
    "bymonth": st.integers(min_value=1, max_value=12),
    "bymonthday": st.one_of(
        st.integers(min_value=-31, max_value=-1), st.integers(min_value=1, max_value=31)
    ),
    "byweekday": st.integers(min_value=0, max_value=6),
    "byhour": st.integers(min_value=0, max_value=23),
    "byminute": st.integers(min_value=0, max_value=59),
    "bysecond": st.integers(min_value=0, max_value=59),
}

# Obergrenze der Listenlaenge pro Filter-Schluessel und Frequenz.
# Filter, die feiner gegliedert sind als die Regel-Frequenz, multiplizieren
# die Termine (z. B. BYWEEKDAY bei YEARLY liefert jeden passenden
# Wochentag jedes Jahres). Die Obergrenzen halten auch bei voll ausgelasteten
# Listen jede Regel unter 1000 Terminen. Jeder Filter bleibt bei mindestens
# einer Frequenz erzeugbar.
_FILTER_MAX_SIZE: dict[int, dict[str, int]] = {
    YEARLY: {"bymonth": 4, "bymonthday": 0, "byweekday": 0, "byhour": 1, "byminute": 1, "bysecond": 1},
    MONTHLY: {"bymonth": 4, "bymonthday": 1, "byweekday": 0, "byhour": 1, "byminute": 1, "bysecond": 1},
    WEEKLY: {"bymonth": 4, "bymonthday": 4, "byweekday": 1, "byhour": 1, "byminute": 1, "bysecond": 1},
    DAILY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 1, "byminute": 1, "bysecond": 1},
    HOURLY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 4, "byminute": 1, "bysecond": 1},
    MINUTELY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 4, "byminute": 4, "bysecond": 1},
    SECONDLY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 4, "byminute": 4, "bysecond": 4},
}


def _dtstart() -> st.SearchStrategy[datetime]:
    """Naive datetimes in [1990-01-01, 2030-12-31 23:59:59] without
    microseconds (rrule drops them from ``dtstart``)."""
    return st.datetimes(
        min_value=datetime(1990, 1, 1),
        max_value=datetime(2030, 12, 31, 23, 59, 59),
    ).map(lambda dt: dt.replace(microsecond=0))


@st.composite
def _filter_list(draw, anchor, domain, max_size) -> list[int] | None:
    """``None`` or a sorted, duplicate-free list of 1-*max_size* values from
    *domain* that always contains *anchor*. *max_size* of 0 always gives
    ``None``."""
    if max_size == 0 or not draw(st.booleans()):
        return None
    n_extra = draw(st.integers(min_value=0, max_value=max_size - 1))
    others = draw(
        st.lists(
            domain.filter(lambda value: value != anchor),
            min_size=n_extra,
            max_size=n_extra,
            unique=True,
        )
    )
    return sorted((anchor, *others))


@st.composite
def rrule_kwargs(draw) -> dict:
    """Keyword arguments for a finite, small ``rrule`` rule.

    The result carries exactly the keys ``freq``, ``dtstart``, ``interval``,
    ``until``, ``wkst`` plus every key of :data:`FILTER_KEYS`.
    """
    freq = draw(st.sampled_from(FREQS))
    dtstart = draw(_dtstart())
    until = dtstart + UNTIL_WINDOW[freq]
    wkst = draw(st.none() | st.integers(min_value=0, max_value=6))
    interval = draw(st.integers(min_value=1, max_value=4))

    kwargs = {
        "freq": freq,
        "dtstart": dtstart,
        "interval": interval,
        "until": until,
        "wkst": wkst,
    }

    limits = _FILTER_MAX_SIZE[freq]
    days_in_month = calendar.monthrange(dtstart.year, dtstart.month)[1]
    anchors = {
        "bymonth": dtstart.month,
        "bymonthday": draw(
            st.sampled_from([dtstart.day, dtstart.day - days_in_month - 1])
        ),
        "byweekday": dtstart.weekday(),
        "byhour": dtstart.hour,
        "byminute": dtstart.minute,
        "bysecond": dtstart.second,
    }
    for key in FILTER_KEYS:
        kwargs[key] = draw(_filter_list(anchors[key], _DOMAINS[key], limits[key]))
    return kwargs
