# `tz.gettz(key).dst()` differs from `zoneinfo` for some transitions 1850-2100

When the same TZif data is loaded with `dateutil.tz.gettz(key)` and
`zoneinfo.ZoneInfo(key)`, `dst()` differs for 46 distinct zones at wall times
near transitions in 1850-2100 (74 key/source cases in total). `utcoffset()`
and `tzname()` agree at the same wall times; only `dst()` is inferred
differently.

This is not a broken contract: dateutil does not document that it matches
`zoneinfo`. TZif files do not store the DST amount, so both libraries infer
it, with different heuristics. This report lists where they disagree, in case
the maintainers consider aligning with `zoneinfo` (PEP 615) worthwhile.

## Versions

- `dateutil`: 4.0.0
- Python: 3.13.18
- Time zone data: `tzdata` package 2026.6 (IANA 2026f) and the system data in
  `/usr/share/zoneinfo` (IANA 2026f, Debian), each used as the only source
- Platform: Debian GNU/Linux 13 (trixie), x86-64

## Differences

Wall times are naive; `fold` is 0 or 1 as shown. The ``Data`` column is the
time zone data source under which the difference was observed. Each row is one
pinned strict-xfail case in
`tests/property/test_tz_oracle_wide_prop.py::test_gettz_dst_wide_examples`;
the table matches `WIDE_DST_CASES` row for row (74 cases, 46 distinct keys).

| Key | Wall time | fold | Data | `dst()` dateutil | `dst()` zoneinfo |
|---|---|---|---|---|---|
| `America/Bahia_Banderas` | 2010-04-04 04:00:00 | 0 | `tzpath` | 1:00:00 | 2:00:00 |
| `America/Coyhaique` | 1927-09-01 00:42:45 | 0 | `tzpath` | 1:00:00 | 0:42:45 |
| `America/Indiana/Tell_City` | 1969-04-27 04:00:00 | 0 | `tzpath` | 1:00:00 | 2:00:00 |
| `America/Inuvik` | 1979-04-29 04:00:00 | 0 | `tzpath` | 1:00:00 | 2:00:00 |
| `America/Montevideo` | 1923-10-01 01:00:00 | 0 | `tzpath` | 0:30:00 | 1:00:00 |
| `America/Punta_Arenas` | 1927-09-01 00:42:45 | 0 | `tzpath` | 1:00:00 | 0:42:45 |
| `America/Santiago` | 1927-09-01 00:42:45 | 0 | `tzpath` | 1:00:00 | 0:42:45 |
| `America/Scoresbysund` | 1981-03-29 02:00:00 | 0 | `tzpath` | 1:00:00 | 2:00:00 |
| `Asia/Hong_Kong` | 1941-10-01 03:30:00 | 1 | `tzpath` | 0:30:00 | -1 day, 23:30:00 |
| `Asia/Ust-Nera` | 1981-04-01 03:00:00 | 0 | `tzpath` | 1:00:00 | 3:00:00 |
| `Atlantic/Azores` | 1942-04-26 00:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Atlantic/Madeira` | 1942-04-26 00:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Amsterdam` | 1940-05-16 01:40:00 | 0 | `tzpath` | 1:00:00 | 1:40:00 |
| `Europe/Belfast` | 1941-05-04 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Berlin` | 1945-05-24 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Gibraltar` | 1941-05-04 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Guernsey` | 1947-04-13 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Isle_of_Man` | 1941-05-04 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Jersey` | 1947-04-13 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Kyiv` | 1941-09-19 23:00:00 | 1 | `tzpath` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Lisbon` | 1942-04-26 00:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/London` | 1941-05-04 03:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Madrid` | 1938-05-01 00:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Minsk` | 1941-06-27 23:00:00 | 1 | `tzpath` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Moscow` | 1921-03-21 00:00:00 | 0 | `tzpath` | 2:00:00 | 1:00:00 |
| `Europe/Riga` | 1941-06-30 23:00:00 | 1 | `tzpath` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Simferopol` | 1941-10-31 23:00:00 | 1 | `tzpath` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Tallinn` | 1941-09-14 23:00:00 | 1 | `tzpath` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Vilnius` | 1941-06-23 23:00:00 | 1 | `tzpath` | 1:00:00 | -1 day, 23:00:00 |
| `Pacific/Rarotonga` | 1978-11-12 01:00:00 | 0 | `tzpath` | 0:30:00 | 1:00:00 |
| `America/Bahia_Banderas` | 2010-04-04 04:00:00 | 0 | `tzdata` | 1:00:00 | 2:00:00 |
| `America/Coyhaique` | 1927-09-01 00:42:45 | 0 | `tzdata` | 1:00:00 | 0:42:45 |
| `America/Indiana/Tell_City` | 1969-04-27 04:00:00 | 0 | `tzdata` | 1:00:00 | 2:00:00 |
| `America/Indiana/Winamac` | 2007-03-11 04:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `America/Inuvik` | 1979-04-29 04:00:00 | 0 | `tzdata` | 1:00:00 | 2:00:00 |
| `America/Montevideo` | 1923-10-01 01:00:00 | 0 | `tzdata` | 0:30:00 | 1:00:00 |
| `America/Punta_Arenas` | 1927-09-01 00:42:45 | 0 | `tzdata` | 1:00:00 | 0:42:45 |
| `America/Santiago` | 1927-09-01 00:42:45 | 0 | `tzdata` | 1:00:00 | 0:42:45 |
| `America/Scoresbysund` | 1981-03-29 02:00:00 | 0 | `tzdata` | 1:00:00 | 2:00:00 |
| `Arctic/Longyearbyen` | 1945-05-24 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Asia/Hong_Kong` | 1941-10-01 03:30:00 | 1 | `tzdata` | 0:30:00 | -1 day, 23:30:00 |
| `Asia/Ust-Nera` | 1981-04-01 03:00:00 | 0 | `tzdata` | 1:00:00 | 3:00:00 |
| `Atlantic/Azores` | 1942-04-26 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Atlantic/Jan_Mayen` | 1945-05-24 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Atlantic/Madeira` | 1942-04-26 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Chile/Continental` | 1927-09-01 00:42:45 | 0 | `tzdata` | 1:00:00 | 0:42:45 |
| `Europe/Belfast` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Berlin` | 1945-05-24 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Copenhagen` | 1945-05-24 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Gibraltar` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Guernsey` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Isle_of_Man` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Jersey` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Kiev` | 1941-09-19 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Kyiv` | 1941-09-19 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Lisbon` | 1942-04-26 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/London` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Madrid` | 1938-05-01 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Minsk` | 1941-06-27 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Moscow` | 1921-03-21 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Oslo` | 1945-05-24 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Riga` | 1941-06-30 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Simferopol` | 1941-10-31 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Stockholm` | 1945-05-24 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Europe/Uzhgorod` | 1941-09-19 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Vilnius` | 1941-06-23 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `Europe/Zaporozhye` | 1941-09-19 23:00:00 | 1 | `tzdata` | 1:00:00 | -1 day, 23:00:00 |
| `GB` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `GB-Eire` | 1941-05-04 03:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `Hongkong` | 1941-10-01 03:30:00 | 1 | `tzdata` | 0:30:00 | -1 day, 23:30:00 |
| `Pacific/Rarotonga` | 1978-11-12 01:00:00 | 0 | `tzdata` | 0:30:00 | 1:00:00 |
| `Portugal` | 1942-04-26 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `W-SU` | 1921-03-21 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |
| `WET` | 1942-04-26 00:00:00 | 0 | `tzdata` | 2:00:00 | 1:00:00 |

## Notes

- The difference is purely in `dst()`; `utcoffset()` and `tzname()` agree at
  every wall time checked. No value is obviously right in every row.
- For `Asia/Hong_Kong` / `Hongkong` at `1941-10-01 03:30` with `fold=1`,
  `zoneinfo` returns a negative `dst()` (`-1 day, 23:30:00`, i.e. -30 minutes)
  while `dateutil` returns a positive one (`0:30:00`). The negative `dst()`
  comes from `zoneinfo` itself, not from dateutil; no historical explanation
  is implied by the data.
- `W-SU` is reported only under `tzdata`: under `tzpath` the key does not
  exist (`gettz("W-SU")` is None, `ZoneInfo.no_cache("W-SU")` raises
  `ZoneInfoNotFoundError`), so it cannot be compared there. Every other case
  loads under both libraries.

## Reproducer

```python
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil import tz

wall = datetime(1941, 10, 1, 3, 30)
key = "Asia/Hong_Kong"
print(wall.replace(fold=1, tzinfo=tz.gettz(key)).dst())          # 0:30:00
print(wall.replace(fold=1, tzinfo=ZoneInfo.no_cache(key)).dst())  # -1 day, 23:30:00
```

Both libraries must be pointed at the same source (``tzpath`` or ``tzdata``);
``zoneinfo`` is always loaded with ``ZoneInfo.no_cache``.

## Covered by

`tests/property/test_tz_oracle_wide_prop.py::test_gettz_dst_wide_examples`
(one strict xfail per case, `reason="docs/reports/z1w-dst-inference.md"`).
The generic test `test_gettz_matches_zoneinfo_wide` does not compare
`dst()` for these keys.

## Duplicate search

TODO (lead)

## Reproduced on upstream master

Reproduced on 2026-11-17 against upstream `master` at commit `a78cbd81d5d03b5f126eb36edb92bca78972c804` (2026-11-01, the current head), Python 3.13.18, system time zone data (Debian tzdata 2026f): `dst()` is `0:30:00` from `tz.gettz` and `-1 day, 23:30:00` from `zoneinfo`, as in the reproducer.
