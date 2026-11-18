"""Shared Hypothesis strategies for finite ``dateutil.rrule.rrule`` rules.

Yields keyword argument dictionaries that can be passed straight to
``rrule(**kw)``. Every rule is finite (bounded by ``until``) and small
(at most 1000 occurrences), and every set ``byxxx`` filter is anchored
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

# Upper bound on the length of each filter list per filter key and
# frequency. Filters finer than the rule frequency multiply the number of
# occurrences (e.g. BYWEEKDAY on a YEARLY rule yields every matching
# weekday of every year). The caps keep every rule within 1000 occurrences,
# even for fully populated lists, and every filter stays generatable for at
# least one frequency. Three combinations expand too much to be bounded by
# list length alone; they are only set when BYMONTH restricts the expanded
# months (see _BYMONTH_MAX), assuming the finer time filters stay at their
# single anchor value:
#
#   YEARLY   bymonthday:  1 value x 4 months x ~200 years      <= 800
#   YEARLY   byweekday:   1 value x 1 month  x ~200 years x 5  <= 1000
#   MONTHLY  byweekday:   1 value x 2 months x ~50 years  x 5  <= 500
_FILTER_MAX_SIZE: dict[int, dict[str, int]] = {
    YEARLY: {"bymonth": 4, "bymonthday": 1, "byweekday": 1, "byhour": 1, "byminute": 1, "bysecond": 1},
    MONTHLY: {"bymonth": 4, "bymonthday": 1, "byweekday": 1, "byhour": 1, "byminute": 1, "bysecond": 1},
    WEEKLY: {"bymonth": 4, "bymonthday": 4, "byweekday": 1, "byhour": 1, "byminute": 1, "bysecond": 1},
    DAILY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 1, "byminute": 1, "bysecond": 1},
    HOURLY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 4, "byminute": 1, "bysecond": 1},
    MINUTELY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 4, "byminute": 4, "bysecond": 1},
    SECONDLY: {"bymonth": 4, "bymonthday": 4, "byweekday": 4, "byhour": 4, "byminute": 4, "bysecond": 4},
}

# (freq, filter key) -> largest BYMONTH list for which the filter may be
# set; with a missing or larger BYMONTH the expansion would exceed 1000
# occurrences (RFC 5545 3.3.10 month expansion).
_BYMONTH_MAX: dict[tuple[int, str], int] = {
    (YEARLY, "bymonthday"): 4,
    (YEARLY, "byweekday"): 1,
    (MONTHLY, "byweekday"): 2,
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
        # bymonth is drawn first, so gated filters can check it here; with a
        # missing or too large bymonth the cap drops to 0 (-> None).
        limit = limits[key]
        bymonth_cap = _BYMONTH_MAX.get((freq, key))
        if bymonth_cap is not None and (
            kwargs["bymonth"] is None or len(kwargs["bymonth"]) > bymonth_cap
        ):
            limit = 0
        kwargs[key] = draw(_filter_list(anchors[key], _DOMAINS[key], limit))
    return kwargs
