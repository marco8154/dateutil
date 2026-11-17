# `tz.tzical` raises `OverflowError` for a malformed `DTSTART` in VTIMEZONE

`tzical` parses any invalid iCalendar input as `ValueError`, but a `DTSTART`
value in a `VTIMEZONE` component that is a long digit string escapes as
`OverflowError` instead. Found while fuzzing "any string yields an object or
raises `ValueError`".

## Minimal reproducer

```python
import io
from dateutil import tz

ical = "\n".join([
    "BEGIN:VTIMEZONE",
    "BEGIN:STANDARD",
    "DTSTART:1970102503000",
    "TZOFFSETFROM:+0200",
    "TZOFFSETTO:+0100",
    "END:STANDARD",
])

tz.tzical(io.StringIO(ical))
```

```
OverflowError: Python int too large to convert to C int
```

A realistic trigger is a `DTSTART` missing its `T` separator:
`DTSTART:1970102503000` instead of `DTSTART:19701025T030000`.

## Versions

- `dateutil`: 4.0.0 (`python -c "import dateutil; print(dateutil.__version__)"`)
- Python: 3.13.18 (`python --version`)
- Platform: Debian GNU/Linux 13 (trixie), x86-64

## Call chain

`tzical._parse_rfc` forwards the `DTSTART` line unchanged to
`rrule.rrulestr` (`tz.py:826`), which parses the value with
`dateutil.parser.parse` (`rrule.py:1617`). Without the `T`, the parser reads
the 13-digit string as a year (`year=1970102503000`) and
`parser._build_naive` passes it to `datetime.replace` (`_parser.py:1229`):

```
OverflowError: Python int too large to convert to C int
```

The `try: ... except ValueError: raise ParserError(...)` guard around
`_build_naive` in `parser.parse` (`_parser.py:643–644`) catches only
`ValueError`, so the `OverflowError` propagates through
`rrule._rrulestr._parse_rfc` and `tzical._parse_rfc` unchanged.

**Expected:** `ValueError`. Every other invalid property in `_parse_rfc` is
reported as `ValueError` ("invalid offset", "unknown component",
"unsupported property", ...), and a `DTSTART` value that is not
`YYYYMMDDTHHMMSS` is invalid under RFC 5545, so it should be rejected as
`ValueError` and in no case surface as `OverflowError`.

## Duplicate search

TODO (lead)

## Reproduced on upstream master

Reproduced on 2026-11-17 against upstream `master` at commit `a78cbd81d5d03b5f126eb36edb92bca78972c804` (2026-11-01, the current head), Python 3.13.18: the call raises `OverflowError: Python int too large to convert to C int`.
