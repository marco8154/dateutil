# `tz.tzstr` raises `TypeError` for time zone strings without an offset

Two ways to make `tz.tzstr` fail with `TypeError` on a plain `str` input,
found while fuzzing "any string yields a `tzinfo` or raises `ValueError`".

## Versions

- `dateutil`: 4.0.0 (`python -c "import dateutil; print(dateutil.__version__)"`)
- Python: 3.13.18 (`python --version`)
- Platform: Debian GNU/Linux 13 (trixie), x86-64

## Bug 1: `tzstr("UTC")` / `tzstr("GMT")`

```python
from dateutil import tz

tz.tzstr("UTC")   # TypeError
tz.tzstr("GMT")   # TypeError
```

`_parsetz` parses these as an abbreviation with no offset, so
`tzstr.__init__` multiplies `None` by -1 in the `GMT`/`UTC` branch
(`res.stdoffset *= -1`):

```
TypeError: unsupported operand type(s) for *=: 'NoneType' and 'int'
```

`tzstr("UTC0")` and `tzstr("EST")` work; only `GMT` and `UTC` reach the
multiplication with a missing offset. Strings whose abbreviation is `GMT` or
`UTC` plus ignorable separators (e.g. `"UTC,,,"`) fail the same way.

**Expected:** the `tzstr` docstring points at the
[GNU C Library TZ variable format](https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html),
where a TZ string without an offset is invalid. Either `ValueError` (like
every other unparseable string) or a usable UTC `tzinfo` — not `TypeError`.

## Bug 2: deprecated comma format with a missing standard offset

```python
from dateutil import tz

tz.tzstr(",0,0,0,0,0,0,0,0,0")   # TypeError
```

A shorter, more realistic input is the deprecated example from the docstring
with the offset digit dropped from the abbreviation:
`tz.tzstr("EST,4,0,6,7200,10,0,26,7200,3600")`.

In `_tzparser.parse` the deprecated branch adds the trailing DST offset value
to a standard offset that was never parsed:

```
res.dstoffset = (res.stdoffset + int(l[i]) * signal)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

**Expected:** `ValueError` (the string carries no standard offset, so it is
not a valid TZ string), and in no case `TypeError` — the `except
(IndexError, ValueError, AssertionError)` guard in `_tzparser.parse` shows the
intent is to report parse failures as `None` → `ValueError`.

## Duplicate search

TODO (lead)

## Reproduced on upstream master

TODO (lead)
