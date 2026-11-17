# `tzstr` misapplies the transition time of TZ strings from TZif footers

Comparing `tzstr(footer, posix_offset=True)` with `zoneinfo` built from the
same TZif file (`tzdata` 2026.6) at UTC instants after the zone's last
transition, four footer patterns give a different `utcoffset()` than the
GNU TZ format prescribes.

## Versions

- `dateutil`: 4.0.0 (`python -c "import dateutil; print(dateutil.__version__)"`)
- Python: 3.13.18 (`python --version`)
- `tzdata`: 2026.6
- Platform: Debian GNU/Linux 13 (trixie), x86-64

## Differences

| Zone | Footer | UTC instant | `utcoffset` zoneinfo | `utcoffset` tzstr |
|---|---|---|---|---|
| `Asia/Beirut` | `EET-2EEST,M3.5.0/0,M10.5.0/0` | 2040-10-27 21:00 | +2:00 | +3:00 |
| `Asia/Gaza`, `Asia/Hebron` | `EET-2EEST,M3.4.4/50,M10.4.4/50` | 2090-03-25 00:00 | +3:00 | +2:00 |
| `Asia/Jerusalem`, `Asia/Tel_Aviv`, `Israel` | `IST-2IDT,M3.4.4/26,M10.5.0` | 2040-03-23 00:00 | +3:00 | +2:00 |
| `Europe/Dublin`, `Eire` | `IST-1GMT0,M10.5.0,M3.5.0/1` | 2040-10-28 01:00 | +0:00 | +1:00 |

The expected value is the one `zoneinfo` (and glibc `localtime`) give, since
the footer is a GNU TZ variable string. Scanning half-hourly, `tzstr`
applied the spring transition days late (Gaza/Hebron, Jerusalem), and the autumn transition 24 h late (Beirut) and 1 h late
(Dublin); the wrong offsets persist well after each instant in the table.

### `/0`: transition at midnight

`M10.5.0/0` is the last Sunday of October at 00:00 local time, i.e. DST ends
2040-10-27 21:00 UTC for Beirut; `tzstr` ends it only 24 h later.

```python
from datetime import datetime, timedelta, timezone
from dateutil import tz

u = datetime(2040, 10, 27, 21, 0, tzinfo=timezone.utc)
tzn = tz.tzstr("EET-2EEST,M3.5.0/0,M10.5.0/0", posix_offset=True)
assert u.astimezone(tzn).utcoffset() == timedelta(hours=2)  # actual: 3:00
```

### `/50` and `/26`: transition times at or beyond 24 h

The GNU format allows the time to reach 167 h; `M3.4.4/50` (Gaza) is 02:00 on
the second day after the fourth Thursday of March, i.e. DST starts 2090-03-25
00:00 UTC (Gaza's TZif file has explicit transitions until 2086, so the footer
governs from then on); `M3.4.4/26` (Jerusalem) starts 2040-03-23 00:00 UTC.
`tzstr` applied the transitions days later.

```python
u = datetime(2090, 3, 25, 0, 0, tzinfo=timezone.utc)
tzn = tz.tzstr("EET-2EEST,M3.4.4/50,M10.4.4/50", posix_offset=True)
assert u.astimezone(tzn).utcoffset() == timedelta(hours=3)  # actual: 2:00

u = datetime(2040, 3, 23, 0, 0, tzinfo=timezone.utc)
tzn = tz.tzstr("IST-2IDT,M3.4.4/26,M10.5.0", posix_offset=True)
assert u.astimezone(tzn).utcoffset() == timedelta(hours=3)  # actual: 2:00
```

### Negative DST: `IST-1GMT0`

Ireland keeps `IST` (+1) as standard time and has `GMT` (0) as its DST, a
negative DST delta. DST ends 2040-10-28 01:00 UTC; `tzstr` ends it one hour
late.

```python
u = datetime(2040, 10, 28, 1, 0, tzinfo=timezone.utc)
tzn = tz.tzstr("IST-1GMT0,M10.5.0,M3.5.0/1", posix_offset=True)
assert u.astimezone(tzn).utcoffset() == timedelta(0)  # actual: 1:00
```

Covered by `tests/property/test_tzstr_oracle_prop.py::
test_tzstr_known_offset_differences`
(`xfail(strict=True)`, one pinned instant per key).

## Duplicate search

TODO (lead)

## Reproduced on upstream master

Reproduced on 2026-11-17 against upstream `master` at commit `a78cbd81d5d03b5f126eb36edb92bca78972c804` (2026-11-01, the current head), Python 3.13.18: all four assertions fail with the offsets noted as "actual" (3:00, 2:00, 2:00, 1:00).
