"""Property tests for the query methods of ``rrulebase`` with aware ``dtstart``
(claim R-3, zoned).

``count()``, ``before``, ``after`` and ``between`` are compared against the
enumerated occurrence list of the same rule, with ``inc`` on both sides and
with the result cache both disabled and enabled. ``dtstart``, ``until`` and the
query points all carry the same ``tzinfo`` (``ZoneInfo``, ``tz.gettz`` or
``tz.UTC``), so the rule is exercised in real zones (DST gaps, 30-minute
transitions).
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytest
from hypothesis import example, given, strategies as st

from dateutil import tz
from dateutil.rrule import DAILY, rrule
from strategies_rrule import rrule_kwargs

KEYS = (
    "Europe/Berlin",
    "America/New_York",
    "Australia/Lord_Howe",
    "Asia/Kolkata",
    "America/St_Johns",
)
ZONES = st.sampled_from(KEYS).flatmap(
    lambda k: st.sampled_from([ZoneInfo(k), tz.gettz(k)])
) | st.just(tz.UTC)


@st.composite
def aware_rrule_kwargs(draw):
    """Like :func:`strategies_rrule.rrule_kwargs`, but ``dtstart`` and
    ``until`` carry the same zoned ``tzinfo``."""
    kw = draw(rrule_kwargs())
    zone = draw(ZONES)
    kw["dtstart"] = kw["dtstart"].replace(tzinfo=zone)
    kw["until"] = kw["until"].replace(tzinfo=zone)
    return kw


def _probe(data, kw, terms):
    """A point to query at: one of the occurrences, or any second in the
    window around the rule (between, before or after the occurrences), in the
    rule's own zone."""
    zone = kw["dtstart"].tzinfo
    if terms and data.draw(st.booleans()):
        return data.draw(st.sampled_from(terms))
    return data.draw(
        st.datetimes(
            min_value=kw["dtstart"].replace(tzinfo=None) - timedelta(days=1),
            max_value=kw["until"].replace(tzinfo=None) + timedelta(days=1),
        ).map(lambda dt: dt.replace(microsecond=0, tzinfo=zone))
    )


def _ref_before(terms, dt, inc):
    matches = [t for t in terms if (t <= dt if inc else t < dt)]
    return matches[-1] if matches else None


def _ref_after(terms, dt, inc):
    matches = [t for t in terms if (t >= dt if inc else t > dt)]
    return matches[0] if matches else None


def _ref_between(terms, after, before, inc):
    if inc:
        return [t for t in terms if after <= t <= before]
    return [t for t in terms if after < t < before]


@pytest.mark.rrule
@pytest.mark.parametrize("cache", [False, True])
@example(
    kw={
        "freq": DAILY,
        "dtstart": datetime(2021, 3, 27, 2, 30, tzinfo=ZoneInfo("Europe/Berlin")),
        "interval": 1,
        "until": datetime(2021, 4, 5, tzinfo=ZoneInfo("Europe/Berlin")),
        "wkst": None,
        "bymonth": None,
        "bymonthday": None,
        "byweekday": None,
        "byhour": None,
        "byminute": None,
        "bysecond": None,
    }
)
@given(kw=aware_rrule_kwargs())
def test_aware_count_matches_list(kw, cache):
    terms = list(rrule(**kw))
    assert rrule(cache=cache, **kw).count() == len(terms)


@pytest.mark.rrule
@pytest.mark.parametrize("cache", [False, True])
@given(data=st.data())
def test_aware_before_after(data, cache):
    kw = data.draw(aware_rrule_kwargs())
    terms = list(rrule(**kw))
    dt = _probe(data, kw, terms)
    for inc in (False, True):
        r = rrule(cache=cache, **kw)
        assert r.before(dt, inc) == _ref_before(terms, dt, inc)
        assert r.after(dt, inc) == _ref_after(terms, dt, inc)
        assert r.count() == len(terms)


@pytest.mark.rrule
@pytest.mark.parametrize("cache", [False, True])
@given(data=st.data())
def test_aware_between(data, cache):
    kw = data.draw(aware_rrule_kwargs())
    terms = list(rrule(**kw))
    a, b = sorted((_probe(data, kw, terms), _probe(data, kw, terms)))
    for inc in (False, True):
        r = rrule(cache=cache, **kw)
        assert r.between(a, b, inc=inc) == _ref_between(terms, a, b, inc)
        assert r.count() == len(terms)
