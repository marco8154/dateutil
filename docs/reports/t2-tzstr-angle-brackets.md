# `tz.tzstr` rejects the `<…>` abbreviations of the GNU TZ format

`tzstr` documents its input format as the
[GNU C Library: TZ Variable](https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html).
That format allows a time zone abbreviation to be wrapped in `<…>` so that it
may contain digits, `+` and `-` (e.g. `<-03>`, `<+1030>`). `tzstr` rejects
such strings with `ValueError: unknown string format` (all four footer
strings of this kind pinned in the test fail this way).

## Versions

- `dateutil`: 4.0.0 (`python -c "import dateutil; print(dateutil.__version__)"`)
- Python: 3.13.18 (`python --version`)
- `tzdata`: 2026.6
- Platform: Debian GNU/Linux 13 (trixie), x86-64

## Reproducer

```python
from dateutil import tz

tz.tzstr("<-03>3")            # ValueError: unknown string format
tz.tzstr("<+04>-4")           # ValueError: unknown string format
```

**Expected:** the same `tzinfo` as the unbracketed equivalents, e.g.
`tz.tzstr("<-03>3") == tz.tzstr("ART3")` (UTC−3); instead `tzstr` raises.

## Scope

This is not a corner case of hand-written strings: 231 of the 598 POSIX TZ
strings in the footers of the TZif files shipped by `tzdata` 2026.6 use `<…>`
abbreviations, so `tzstr(footer, posix_offset=True)` cannot reproduce any of
those zones. Examples (the exact footer text of the zone):

| Zone | Footer |
|---|---|
| `America/Argentina/Buenos_Aires` | `<-03>3` |
| `Asia/Dubai` | `<+04>-4` |
| `America/Santiago` | `<-04>4<-03>,M9.1.6/24,M4.1.6/24` |
| `Australia/Lord_Howe` | `<+1030>-10:30<+11>-11,M10.1.0,M4.1.0` |

Covered by `tests/property/test_tzstr_oracle_prop.py::
test_tzstr_angle_bracket_abbreviations`
(`xfail(strict=True, raises=ValueError)`).

## Duplicate search

TODO (lead)

## Reproduced on upstream master

TODO (lead)
