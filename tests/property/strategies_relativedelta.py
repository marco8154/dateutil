"""Shared Hypothesis strategies for ``relativedelta`` keyword arguments.

Only ``datetime`` and ``hypothesis`` are used, never dateutil itself: these
strategies feed tests whose subject is dateutil.relativedelta.
"""

from datetime import datetime

from hypothesis import strategies as st

_RELATIVE_TIME = {
    "weeks": (-520, 520),
    "days": (-3650, 3650),
    "hours": (-87600, 87600),
    "minutes": (-10**6, 10**6),
    "seconds": (-10**7, 10**7),
    "microseconds": (-10**9, 10**9),
}

_RELATIVE_CALENDAR = {
    "years": (-50, 50),
    "months": (-600, 600),
}

_ABSOLUTE = {
    "year": (1900, 2100),
    "month": (1, 12),
    "day": (1, 31),
    "hour": (0, 23),
    "minute": (0, 59),
    "second": (0, 59),
    "microsecond": (0, 999999),
}


def _optional(strategy):
    """Draw the strategy's value, or leave the field out entirely."""
    return st.none() | strategy


def _non_empty(**fields):
    """Draw a non-empty dict from optional fields."""

    def build(**kwargs):
        return {key: value for key, value in kwargs.items() if value is not None}

    return st.builds(build, **fields).filter(lambda kw: bool(kw))


def base_datetimes(max_day: int = 31) -> st.SearchStrategy[datetime]:
    """Naive datetimes in 1900-01-01..2100-12-31 with ``day <= max_day``."""
    return st.datetimes(
        min_value=datetime(1900, 1, 1),
        max_value=datetime(2100, 12, 31, 23, 59, 59, 999999),
    ).filter(lambda dt: dt.day <= max_day)


def relative_time_kwargs() -> st.SearchStrategy[dict]:
    """Non-empty subset of the purely relative time-unit keywords.

    Every drawn dict is valid both as ``relativedelta(**kw)`` and as
    ``timedelta(**kw)``; all values are ``int``.
    """
    fields = {
        key: _optional(st.integers(min_value=lo, max_value=hi))
        for key, (lo, hi) in _RELATIVE_TIME.items()
    }
    return _non_empty(**fields)


def relative_kwargs(fractional: bool = False) -> st.SearchStrategy[dict]:
    """Non-empty subset of the relative keywords.

    Adds ``years`` and ``months`` to :func:`relative_time_kwargs`. With
    ``fractional=True``, ``days``, ``hours`` and ``minutes`` are floats that
    are exact multiples of 0.25 instead of integers. ``years`` and ``months``
    always stay integers.
    """
    fields = {
        key: _optional(st.integers(min_value=lo, max_value=hi))
        for key, (lo, hi) in _RELATIVE_TIME.items()
    }
    fields.update(
        {
            "years": _optional(st.integers(min_value=-50, max_value=50)),
            "months": _optional(st.integers(min_value=-600, max_value=600)),
        }
    )
    if fractional:

        def quarters(lo: int, hi: int) -> st.SearchStrategy[float]:
            return st.integers(min_value=lo * 4, max_value=hi * 4).map(
                lambda n: n * 0.25
            )

        fields["days"] = _optional(quarters(-3650, 3650))
        fields["hours"] = _optional(quarters(-87600, 87600))
        fields["minutes"] = _optional(quarters(-10**6, 10**6))
    return _non_empty(**fields)


def absolute_kwargs() -> st.SearchStrategy[dict]:
    """Non-empty subset of the absolute (singular) keywords, all ``int``."""
    fields = {
        key: _optional(st.integers(min_value=lo, max_value=hi))
        for key, (lo, hi) in _ABSOLUTE.items()
    }
    return _non_empty(**fields)
