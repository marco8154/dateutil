"""Shared Hypothesis strategies for IANA keys and time zone transitions.

Only zoneinfo and datetime are used, never dateutil: these strategies feed
oracle tests whose expected values must not depend on the module under test.
They use whichever time zone data zoneinfo currently sees.
"""

import functools
import zoneinfo
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, available_timezones

from hypothesis import strategies as st

_UTC = timezone.utc
# Not real zones: the system-local link, a leftover of old tzdata builds and
# the POSIX fallback zone.
_NON_ZONES = frozenset({"localtime", "posixrules", "Factory"})

_MICROSECOND = timedelta(microseconds=1)
_WINDOW = timedelta(days=2)


def iana_keys() -> st.SearchStrategy[str]:
    """A key of a real IANA time zone, from the data available at call time."""
    keys = sorted(set(available_timezones()) - _NON_ZONES)
    return st.sampled_from(keys)


def utc_datetimes(min_year: int = 1900, max_year: int = 2100) -> st.SearchStrategy[datetime]:
    """UTC-aware datetimes with a year in [min_year, max_year]."""
    return st.datetimes(
        min_value=datetime(min_year, 1, 1),
        max_value=datetime(max_year, 12, 31, 23, 59, 59, 999999),
        timezones=st.just(_UTC),
    )


def transitions(key: str, first_year: int = 1970, last_year: int = 2040) -> tuple[datetime, ...]:
    """Ascending UTC instants at which utcoffset, dst or tzname of *key* change.

    Each returned instant is the first instant of the new values. The scan
    steps one day at a time across [first_year, last_year] and bisects each
    change down to the microsecond.
    """
    # Tests switch the data source by resetting TZPATH, so it is part of the
    # cache key; it must be read here, at call time.
    return _transitions_for_tzpath(key, first_year, last_year, tuple(zoneinfo.TZPATH))


@functools.lru_cache(maxsize=None)
def _transitions_for_tzpath(key, first_year, last_year, tzpath):
    # ZoneInfo's own cache is keyed by key alone and would hand back a zone
    # loaded from another source.
    tzi = ZoneInfo.no_cache(key)

    def attrs(instant):
        local = instant.astimezone(tzi)
        return (local.utcoffset(), local.dst(), local.tzname())

    def bisect(lo, hi):
        # attrs(lo) != attrs(hi); return the first instant that has attrs(hi).
        while hi - lo > _MICROSECOND:
            mid = lo + (hi - lo) // 2
            if attrs(mid) == attrs(lo):
                lo = mid
            else:
                hi = mid
        return hi

    found = []
    prev = datetime(first_year, 1, 1, tzinfo=_UTC)
    stop = datetime(last_year + 1, 1, 1, tzinfo=_UTC)
    prev_attrs = attrs(prev)
    day = prev + timedelta(days=1)
    while day <= stop:
        day_attrs = attrs(day)
        if day_attrs != prev_attrs:
            found.append(bisect(prev, day))
            prev_attrs = day_attrs
        prev = day
        day += timedelta(days=1)
    return tuple(found)


def _offset_deltas():
    # The exact transition, one microsecond either side and one hour either
    # side (the width of a typical DST shift) are weighted over the window so
    # that examples land on the interesting instants.
    return st.one_of(
        st.just(timedelta(0)),
        st.just(_MICROSECOND),
        st.just(-_MICROSECOND),
        st.just(timedelta(hours=-1)),
        st.just(timedelta(hours=1)),
        st.timedeltas(min_value=-_WINDOW, max_value=_WINDOW),
    )


def instants_near_transitions(
    key: str, first_year: int = 1970, last_year: int = 2040
) -> st.SearchStrategy[datetime]:
    """A UTC instant within two days of a transition of *key*.

    Keys with no transitions in the default range fall back to plain
    utc_datetimes().
    """
    instants = transitions(key, first_year, last_year)
    if not instants:
        return utc_datetimes()
    return st.sampled_from(instants).flatmap(
        lambda instant: _offset_deltas().map(lambda delta: instant + delta)
    )


def wall_times_near_transitions(
    key: str, first_year: int = 1970, last_year: int = 2040
) -> st.SearchStrategy[datetime]:
    """A naive wall time within two days of a transition of *key*, fold 0 or 1.

    The delta is applied to the wall time, so values inside a gap (imaginary)
    or a fold (ambiguous) are reachable. Keys with no transitions in the
    default range fall back to plain utc_datetimes().
    """
    instants = transitions(key, first_year, last_year)
    if not instants:
        return utc_datetimes().map(lambda dt: dt.replace(tzinfo=None))

    # Loaded now, from the source that also gave the instants; ZoneInfo's
    # cache is keyed by key alone.
    tzi = ZoneInfo.no_cache(key)

    def near_wall(instant):
        local = instant.astimezone(tzi)
        return _offset_deltas().map(
            lambda delta: (local + delta).replace(tzinfo=None)
        )

    def with_fold(wall):
        return st.sampled_from([0, 1]).map(lambda fold: wall.replace(fold=fold))

    return st.sampled_from(instants).flatmap(near_wall).flatmap(with_fold)
