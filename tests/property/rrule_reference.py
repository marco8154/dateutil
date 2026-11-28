"""Independent brute-force reference for simple RFC 5545 recurrence rules.

Counts calendar days from ``DTSTART`` and filters them with the rules of
RFC 5545 section 3.3.10 (with Verified errata 1913, 3747, 3779, 4271, 4414).
Independent of the library under test: this is the oracle for claim R-7 and
must not be able to repeat its mistakes, so only the standard library
(``datetime``, ``calendar``) is used.

Weekdays are ``int`` with Monday = 0 (``datetime.weekday()``); ``wkst`` uses
the same convention (the RFC default ``MO`` is 0). An occurrence set is
always bounded by ``count`` or ``until`` so the enumeration terminates.

``expand`` emits ``dtstart`` only if ``dtstart`` itself matches the rule (as
the library under test does). This deviates from the literal reading of RFC 5545
3.3.10, l. 2272-2274 ("DTSTART always counts as the first occurrence") and is
intended.
"""

import calendar
from datetime import date, datetime, timedelta

_FREQS = ("YEARLY", "MONTHLY", "WEEKLY", "DAILY")

# Rough upper bound on the days scanned before a rule is declared endless
# (400 years); a well-formed rule with ``count``/``until`` stops far sooner.
_MAX_SCAN_DAYS = 400 * 366


def expand(freq: str, dtstart: datetime, *, interval: int = 1,
           count: int | None = None, until: datetime | None = None,
           wkst: int = 0, bymonth=None, bymonthday=None, byweekday=None,
           byhour=None, byminute=None, bysecond=None,
           bysetpos=None) -> list[datetime]:
    """Return the occurrences of one simple recurrence rule, ascending.

    ``freq`` is ``"YEARLY"``, ``"MONTHLY"``, ``"WEEKLY"`` or ``"DAILY"``.
    Exactly one of ``count`` / ``until`` must be given. ``byweekday`` entries
    are an ``int`` weekday or a ``(weekday, n)`` ordinal pair (``n`` in
    +/-1..53). Invalid dates such as February 30 never occur because only real
    calendar days are counted (RFC 5545 3.3.10, l. 2382).

    ``bysetpos`` is ``None`` or a list of ``int`` in 1..366 / -366..-1. It
    selects from the sorted candidates of one FREQ period (year, month, week
    from ``wkst``, day), counted from the start of the period, so candidates
    before ``dtstart`` take part in the positions. Only then are occurrences
    before ``dtstart`` dropped, followed by ``until`` and ``count``.
    """
    if freq not in _FREQS:
        raise ValueError(f"unsupported FREQ {freq!r}")  # RFC 5545 3.3.10, l. 2153
    if (count is None) == (until is None):
        # UNTIL and COUNT MUST NOT occur together, and one is required here to
        # keep the rule finite. RFC 5545 3.3.10, l. 2124-2125, 2270.
        raise ValueError("exactly one of count/until must be set")

    for term in byweekday or ():
        wd, n = term if isinstance(term, tuple) else (term, None)
        if not 0 <= wd <= 6:
            raise ValueError(f"weekday must be in 0..6, got {wd!r}")
        if n is None:
            continue
        if freq in ("DAILY", "WEEKLY"):
            # BYDAY MUST NOT have a numeric value unless FREQ is MONTHLY or
            # YEARLY. RFC 5545 3.3.10, l. 2312-2314.
            raise ValueError(f"ordinal BYDAY {term!r} is not allowed for {freq}")
        if n == 0 or abs(n) > 53:
            # The ordinal is +/-(1..53). RFC 5545 3.3.10, l. 2178 (ordwk).
            raise ValueError(f"BYDAY ordinal must be +/-1..53, got {n!r}")

    if bysetpos:
        for pos in bysetpos:
            if pos == 0 or abs(pos) > 366:
                # Valid values are 1 to 366 or -366 to -1.
                # RFC 5545 3.3.10, l. 2211-2213, 2376.
                raise ValueError(f"BYSETPOS must be +/-1..366, got {pos!r}")
        if not any((bymonth, bymonthday, byweekday, byhour, byminute,
                    bysecond)):
            # RFC 5545 3.3.10, l. 2372-2373.
            raise ValueError("BYSETPOS needs another BYxxx rule part")

    plain_wd, nth_wd = _split_weekdays(byweekday)
    months = set(bymonth) if bymonth is not None else None
    # Missing BYHOUR/BYMINUTE/BYSECOND are taken from DTSTART.
    # RFC 5545 3.3.10, l. 2388-2393, 2484-2490.
    hours = sorted(byhour) if byhour else [dtstart.hour]
    minutes = sorted(byminute) if byminute else [dtstart.minute]
    seconds = sorted(bysecond) if bysecond else [dtstart.second]

    occurrences: list[datetime] = []
    day = dtstart.date()
    if bysetpos:
        # The first set starts at the beginning of its period, which may lie
        # before DTSTART. RFC 5545 3.3.10, l. 2368-2369.
        day = _period_start(freq, day, wkst)
    pending: list[datetime] = []
    period = _period_start(freq, day, wkst)
    last_day = day + timedelta(days=_MAX_SCAN_DAYS)
    while True:
        if day > last_day:
            raise ValueError("rule did not terminate within 400 years")
        if bysetpos and _period_start(freq, day, wkst) != period:
            # The period just ended: select from its set (l. 2364-2367), drop
            # what precedes DTSTART, then apply UNTIL and COUNT
            # (l. 2418-2420). UNTIL is inclusive, l. 2255-2258.
            for occ in _select_positions(pending, bysetpos):
                if occ >= dtstart and (until is None or occ <= until):
                    occurrences.append(occ)
            pending = []
            period = _period_start(freq, day, wkst)
            if until is not None and day > until.date():
                break
            if count is not None and len(occurrences) >= count:
                break
        if _is_active_day(freq, dtstart, interval, wkst, day):
            if _is_selected_day(freq, dtstart, day, months, bymonthday,
                                plain_wd, nth_wd):
                for hour in hours:
                    for minute in minutes:
                        for second in seconds:
                            occ = datetime(day.year, day.month, day.day,
                                           hour, minute, second)
                            if bysetpos:
                                pending.append(occ)
                                continue
                            if occ < dtstart:
                                # Occurrences before DTSTART are never emitted;
                                # see the module docstring.
                                continue
                            if until is not None and occ > until:
                                continue  # UNTIL is inclusive, l. 2255-2258
                            occurrences.append(occ)
        if not bysetpos:
            if until is not None and day >= until.date():
                break  # every later day exceeds an inclusive UNTIL
            if count is not None and len(occurrences) >= count:
                break
        day += timedelta(days=1)

    if count is not None:
        # COUNT is evaluated after the BYxxx parts. RFC 5545 3.3.10, l. 2418-2420.
        occurrences = occurrences[:count]
    return occurrences


def _period_start(freq, day, wkst):
    """First day of the FREQ period containing ``day``.

    RFC 5545 3.3.10, l. 2366-2369 (the set is one interval of the rule).
    """
    if freq == "YEARLY":
        return date(day.year, 1, 1)
    if freq == "MONTHLY":
        return date(day.year, day.month, 1)
    if freq == "WEEKLY":
        return _week_start(day, wkst)
    return day


def _select_positions(candidates, bysetpos):
    """The ``bysetpos``-th elements of ``candidates``, ascending, once each.

    A negative position counts from the end; one outside the set selects
    nothing. RFC 5545 3.3.10, l. 2377-2380.
    """
    chosen = set()
    for pos in bysetpos:
        index = pos - 1 if pos > 0 else len(candidates) + pos
        if 0 <= index < len(candidates):
            chosen.add(index)
    return [candidates[i] for i in sorted(chosen)]


def _split_weekdays(byweekday):
    """Split BYDAY terms into plain weekdays and ``(weekday, n)`` ordinals."""
    plain, nth = [], []
    for term in byweekday or ():
        if isinstance(term, tuple):
            nth.append(term)
        else:
            plain.append(term)
    return set(plain), nth


def _is_active_day(freq, dtstart, interval, wkst, day):
    """True if ``day`` lies in an active INTERVAL period of ``freq``.

    INTERVAL counts periods of the rule's frequency starting from DTSTART.
    RFC 5545 3.3.10, l. 2247-2253.
    """
    if freq == "DAILY":
        return (day - dtstart.date()).days % interval == 0
    if freq == "MONTHLY":
        months = (day.year - dtstart.year) * 12 + (day.month - dtstart.month)
        return months % interval == 0
    if freq == "YEARLY":
        return (day.year - dtstart.year) % interval == 0
    # WEEKLY: whole weeks measured from the week containing DTSTART.
    # RFC 5545 3.3.10, l. 2349-2362 (WKST).
    weeks = (_week_start(day, wkst) - _week_start(dtstart.date(), wkst)).days
    return (weeks // 7) % interval == 0


def _week_start(day, wkst):
    # RFC 5545 3.3.10, l. 2349-2362: the week starts on ``wkst`` (default MO).
    return day - timedelta(days=(day.weekday() - wkst) % 7)


def _is_selected_day(freq, dtstart, day, months, bymonthday, plain_wd, nth_wd):
    """True if the calendar ``day`` passes the BYxxx day rules of ``freq``.

    The Expand/Limit behaviour per frequency is the table of RFC 5545 3.3.10,
    l. 2431-2451 (with the corrected Note 1/Note 2, erratum 3747, l. 2453-2459).
    """
    has_day_rule = bool(bymonthday or plain_wd or nth_wd)

    # BYMONTH is Limit except at YEARLY where it is Expand; when missing and no
    # day rule expands across months, the month comes from DTSTART.
    # RFC 5545 3.3.10, l. 2434, 2388-2393.
    if freq == "YEARLY":
        if months is not None:
            if day.month not in months:
                return False
        elif not has_day_rule and day.month != dtstart.month:
            return False
    elif months is not None and day.month not in months:
        return False

    if freq == "DAILY":
        # BYMONTHDAY and BYDAY are both Limit at DAILY (l. 2440, 2442).
        if bymonthday and not _monthday_matches(day, bymonthday):
            return False
        if plain_wd and day.weekday() not in plain_wd:
            return False
        return True

    if freq == "WEEKLY":
        # BYDAY is Expand at WEEKLY (l. 2442); the base weekday is DTSTART's.
        allowed = plain_wd if plain_wd else {dtstart.weekday()}
        if day.weekday() not in allowed:
            return False
        # BYMONTHDAY is N/A at WEEKLY (l. 2321-2322, 2440); if given anyway it
        # only restricts, which is not an RFC-conform rule.
        if bymonthday and not _monthday_matches(day, bymonthday):
            return False
        return True

    if freq == "MONTHLY":
        # BYDAY (l. 2442 Note 1, erratum 3747): Limit when BYMONTHDAY present,
        # otherwise special expand; ordinals are within the month.
        if bymonthday:
            if not _monthday_matches(day, bymonthday):
                return False
            if plain_wd or nth_wd:
                return _weekday_matches(day, plain_wd, nth_wd, "month")
            return True
        if plain_wd or nth_wd:
            return _weekday_matches(day, plain_wd, nth_wd, "month")
        # No day rule: base day-of-month from DTSTART, invalid dates skipped.
        # RFC 5545 3.3.10, l. 2382, 2388-2393.
        return day.day == dtstart.day

    # YEARLY (l. 2442 Note 2, errata 3779/1913 in docs/sources/rfc5545-errata.md):
    # ordinal is within the month when BYMONTH is present, otherwise within the
    # year.
    scope = "month" if months else "year"
    if bymonthday:
        if not _monthday_matches(day, bymonthday):
            return False
        if plain_wd or nth_wd:
            return _weekday_matches(day, plain_wd, nth_wd, scope)
        return True
    if plain_wd or nth_wd:
        return _weekday_matches(day, plain_wd, nth_wd, scope)
    # No day rule: DTSTART's month already checked above, so match its day.
    # RFC 5545 3.3.10, l. 2388-2393.
    return day.day == dtstart.day


def _monthday_matches(day, bymonthday):
    """True if ``day`` is one of the BYMONTHDAY values of its month.

    Negative values count from the end of the month. RFC 5545 3.3.10,
    l. 2318-2320.
    """
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    for value in bymonthday:
        target = value if value > 0 else days_in_month + value + 1
        if day.day == target:
            return True
    return False


def _weekday_matches(day, plain_wd, nth_wd, scope):
    """True if ``day`` matches a plain weekday or an ordinal ``(wd, n)``."""
    if day.weekday() in plain_wd:
        return True
    for wd, n in nth_wd:
        if day.weekday() == wd and _nth_weekday(day, wd, n, scope) == day:
            return True
    return False


def _nth_weekday(day, wd, n, scope):
    """The date of the ``n``-th weekday ``wd`` in ``day``'s month or year.

    ``None`` when the period has no such day, e.g. a fifth Friday in a month
    with only four (RFC 5545 3.3.10, l. 2303-2309; ordinal scope per errata
    1913/3779). Out-of-range ordinals therefore simply never match a day
    instead of raising.
    """
    if scope == "year":
        return _nth_weekday_of_year(day.year, wd, n)
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    if n >= 1:
        dom = 1 + (wd - date(day.year, day.month, 1).weekday()) % 7 + 7 * (n - 1)
        return date(day.year, day.month, dom) if dom <= days_in_month else None
    dom = days_in_month - (date(day.year, day.month, days_in_month).weekday()
                           - wd) % 7 + 7 * (n + 1)
    return date(day.year, day.month, dom) if dom >= 1 else None


def _nth_weekday_of_year(year, wd, n):
    """The date of the ``n``-th weekday ``wd`` in ``year`` (RFC l. 2303-2309)."""
    jan1 = date(year, 1, 1)
    length = date(year + 1, 1, 1).toordinal() - jan1.toordinal()
    if n >= 1:
        doy = 1 + (wd - jan1.weekday()) % 7 + 7 * (n - 1)
        return jan1 + timedelta(days=doy - 1) if doy <= length else None
    dec31 = jan1 + timedelta(days=length - 1)
    doy = length - (dec31.weekday() - wd) % 7 + 7 * (n + 1)
    return jan1 + timedelta(days=doy - 1) if doy >= 1 else None
