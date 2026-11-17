# `tz.gettz(key).dst()` differs from `zoneinfo` around some transitions

When the same TZif data is loaded with `dateutil.tz.gettz(key)` and
`zoneinfo.ZoneInfo(key)`, `dst()` differs for eight zones at wall times near
transitions. `utcoffset()` and `tzname()` agree at the same wall times.

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

Wall times are naive with `fold=0`.

| Key | Wall time | `utcoffset` | `dst` dateutil | `dst` zoneinfo | Data |
|---|---|---|---|---|---|
| `America/Bahia_Banderas` | 2010-04-04 04:00 | -5:00 | 1:00 | 2:00 | both |
| `America/Indiana/Tell_City` | 1970-04-26 03:00 | -4:00 | 1:00 | 2:00 | both |
| `America/Indiana/Winamac` | 2007-03-11 04:00 | -4:00 | 2:00 | 1:00 | `tzdata` only |
| `America/Inuvik` | 1979-04-29 04:00 | -6:00 | 1:00 | 2:00 | both |
| `America/Scoresbysund` | 1981-03-29 02:00 | 0:00 | 1:00 | 2:00 | both |
| `Asia/Ust-Nera` | 1981-04-01 03:00 | +12:00 | 1:00 | 3:00 | both |
| `Europe/Vilnius` | 1998-03-29 03:00 | +2:00 | 1:00 | -1:00 | `tzdata` only |
| `Pacific/Rarotonga` | 1978-11-12 01:00 | -9:30 | 0:30 | 1:00 | both |

A one-off investigation script (not part of the test suite) over all keys and
all transitions 1970–2040 (exact transition, ±1 µs, ±1 h, +1 day, both folds)
found no other key with a different `dst()`, and no key with a different
`utcoffset()` or `tzname()`; the property tests sample these transitions and
agree. Neither value is obviously
right in every row (e.g. `zoneinfo`'s -1:00 for Vilnius while on CEST).

```python
from datetime import datetime
from zoneinfo import ZoneInfo
from dateutil import tz

wall = datetime(1970, 4, 26, 3)
key = "America/Indiana/Tell_City"
print(wall.replace(tzinfo=tz.gettz(key)).dst())          # 1:00:00
print(wall.replace(tzinfo=ZoneInfo.no_cache(key)).dst())  # 2:00:00
```

Covered by `tests/property/test_tz_oracle_prop.py::
test_gettz_dst_matches_zoneinfo_examples` (`xfail(strict=True)`, one pinned
wall time per key). The generic test `test_gettz_matches_zoneinfo` does not
compare `dst()` for these keys.

## Duplicate search

TODO (lead)

## Reproduced on upstream master

TODO (lead)
