"""Property test for claim R-4 with an aware ``dtstart`` (``docs/claims.md``).

``rrulestr(str(r))`` reproduces ``r`` for a naive ``dtstart`` (see
``test_rrule_roundtrip_prop.py``). It does not for an aware ``dtstart``:
``rrule.__str__`` writes ``DTSTART:`` without a ``TZID`` parameter and
without ``Z``, so ``rrulestr`` returns naive occurrences. ``rrule`` defines no
``__eq__``, so occurrence lists are compared, not rules.
"""
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
from hypothesis import example, given
from hypothesis import strategies as st

from dateutil import tz
from dateutil.rrule import DAILY, rrule, rrulestr

from strategies_rrule import rrule_kwargs

ZONE_KEYS = ("Europe/Berlin", "America/New_York", "Asia/Kolkata")

ZONES = [tz.UTC]
for _key in ZONE_KEYS:
    ZONES.extend([ZoneInfo(_key), tz.gettz(_key)])


@st.composite
def aware_rrule_kwargs(draw):
    """``rrule_kwargs()`` with ``dtstart`` and ``until`` in one time zone.

    Both get the same zone via ``replace(tzinfo=...)``; the wall time and the
    rest of the keyword arguments are unchanged.
    """
    zone = draw(st.sampled_from(ZONES))
    kw = draw(rrule_kwargs())
    return {
        **kw,
        "dtstart": kw["dtstart"].replace(tzinfo=zone),
        "until": kw["until"].replace(tzinfo=zone),
    }


PIN_AWARE_ZONEINFO = {
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

PIN_AWARE_GETTZ = {
    "freq": DAILY,
    "dtstart": datetime(2021, 3, 27, 2, 30, tzinfo=tz.gettz("Europe/Berlin")),
    "interval": 1,
    "until": datetime(2021, 4, 5, tzinfo=tz.gettz("Europe/Berlin")),
    "wkst": None,
    "bymonth": None,
    "bymonthday": None,
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}

PIN_AWARE_UTC = {
    "freq": DAILY,
    "dtstart": datetime(2021, 3, 27, 2, 30, tzinfo=tz.UTC),
    "interval": 1,
    "until": datetime(2021, 4, 5, tzinfo=tz.UTC),
    "wkst": None,
    "bymonth": None,
    "bymonthday": None,
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
}


@pytest.mark.rrule
@pytest.mark.rrulestr
@pytest.mark.xfail(strict=True, reason="docs/reports/r4-rrule-str-drops-tzinfo.md")
@example(kw=PIN_AWARE_ZONEINFO)
@example(kw=PIN_AWARE_GETTZ)
@example(kw=PIN_AWARE_UTC)
@given(kw=aware_rrule_kwargs())
def test_str_roundtrip_aware(kw):
    r = rrule(**kw)
    assert list(rrulestr(str(r))) == list(r)


@pytest.mark.rrule
@pytest.mark.rrulestr
@given(kw=aware_rrule_kwargs())
def test_str_has_no_tz_marker(kw):
    """As of dateutil 4.0.0, ``str(r)`` drops the ``dtstart`` time zone.

    The first line is a bare ``DTSTART:`` date-time: no ``TZID`` parameter and
    no ``Z`` suffix, even for an aware ``dtstart``. A fix that emits the RFC
    5545 UTC form (``...Z``) or a ``TZID`` parameter will make this test fail.
    """
    first_line = str(rrule(**kw)).splitlines()[0]
    assert first_line.startswith("DTSTART:")
    assert not first_line.endswith("Z")
