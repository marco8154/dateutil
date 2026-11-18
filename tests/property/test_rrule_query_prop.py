# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause
"""Property tests for the query methods of ``rrulebase`` (claim R-3).

``count()``, ``before``, ``after`` and ``between`` are compared against the
enumerated occurrence list of the same rule, with ``inc`` on both sides and
with the result cache both disabled and enabled.
"""

from datetime import timedelta

import pytest
from hypothesis import given, strategies as st

from dateutil.rrule import rrule
from strategies_rrule import rrule_kwargs


def _probe(data, kw, terms):
    """A point to query at: one of the occurrences, or any second in the
    window around the rule (between, before or after the occurrences)."""
    if terms and data.draw(st.booleans()):
        return data.draw(st.sampled_from(terms))
    return data.draw(
        st.datetimes(
            min_value=kw["dtstart"] - timedelta(days=1),
            max_value=kw["until"] + timedelta(days=1),
        ).map(lambda dt: dt.replace(microsecond=0))
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
@given(kw=rrule_kwargs())
def test_count_matches_list(kw, cache):
    terms = list(rrule(**kw))
    assert rrule(cache=cache, **kw).count() == len(terms)


@pytest.mark.rrule
@pytest.mark.parametrize("cache", [False, True])
@given(data=st.data())
def test_before_after(data, cache):
    kw = data.draw(rrule_kwargs())
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
def test_between(data, cache):
    kw = data.draw(rrule_kwargs())
    terms = list(rrule(**kw))
    a, b = sorted((_probe(data, kw, terms), _probe(data, kw, terms)))
    for inc in (False, True):
        r = rrule(cache=cache, **kw)
        assert r.between(a, b, inc=inc) == _ref_between(terms, a, b, inc)
        assert r.count() == len(terms)


@pytest.mark.rrule
@given(data=st.data())
def test_queries_on_complete_cache(data):
    kw = data.draw(rrule_kwargs())
    terms = list(rrule(**kw))
    dt = _probe(data, kw, terms)
    a, b = sorted((_probe(data, kw, terms), _probe(data, kw, terms)))
    r = rrule(cache=True, **kw)
    r.count()
    assert r._cache_complete
    for inc in (False, True):
        assert r.before(dt, inc) == _ref_before(terms, dt, inc)
        assert r.after(dt, inc) == _ref_after(terms, dt, inc)
        assert r.between(a, b, inc=inc) == _ref_between(terms, a, b, inc)
