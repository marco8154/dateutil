# Claims-Register

Stand: 2026-11-15 · Entwurf des Leads · **abgezeichnet: noch nicht** (Visionär:in, einmalig)

Quelle aller Claims: `dateutil/dateutil` @ `a78cbd8`; Zeilen beziehen sich auf diesen Stand. Ein Claim gilt nur für den getesteten Eingaberaum (Säule 5). „Vertrag“ = dokumentiert; „Erwartung“ = nicht dokumentiert, ein Verstoß ist ein Fund, aber kein Vertragsbruch, und so wird er auch berichtet.

Toleranz: alle Claims sind exakt (gleiche Werte bzw. gleiche Ausnahmeklasse); keine numerische Toleranz.

| ID | Quelle | Claim in unseren Worten | Art | Abnahme (Test) | Hängt ab von | Status |
|---|---|---|---|---|---|---|
| P-1 | `isoparser.py:58–118` (Formate) | `isoparse(dt.isoformat(sep))` liefert dieselbe Wandzeit und denselben Offset wie `dt` | Vertrag | `tests/property/test_isoparse_prop.py::test_timespec_auto` (upstream) | – | offen |
| P-2 | `isoparser.py:68–106` | Für jeden String in der dokumentierten Grammatik, den auch `datetime.fromisoformat` annimmt, liefern beide denselben Wert und denselben `utcoffset()` | Vertrag (Orakel) | `tests/property/test_isoparse_oracle_prop.py` | – | offen |
| P-3 | `isoparser.py:108–111` | Offsets gleich UTC (`Z`, `+00:00`, `+0000`, `+00`) ergeben `tz.UTC`, alle anderen ein `tzoffset` mit genau diesem Offset | Vertrag | `tests/property/test_isoparse_tz_prop.py` | – | offen |
| P-4 | `isoparser.py:91–93` | `24:00` (mit allen erlaubten Formen von Minuten/Sekunden = 0) ergibt 00:00 des Folgetags | Vertrag | `tests/property/test_isoparse_prop.py` (neuer Test) | – | offen |
| P-5 | `isoparser.py:78–82` | `YYYY-Www-D` ergibt das Datum mit `date.fromisocalendar(YYYY, ww, D)` | Vertrag (Orakel) | `tests/property/test_isoparse_oracle_prop.py` | – | offen |
| P-6 | Rückgabe/Fehler von `isoparse` | Für beliebige Strings wirft `isoparse` nur `ValueError` (oder liefert ein `datetime`) | Erwartung | Fuzz-Ziel, Meilenstein 2 | – | offen |
| P-7 | `_parser.py:1350–1357` | `parse(s)` wirft für beliebige Strings nur `ParserError` oder `OverflowError` (oder liefert ein `datetime`) | Vertrag | Fuzz-Ziel, Meilenstein 2 | – | offen |
| P-8 | `_parser.py` (Vertrag mit `isoformat`, Brief F2b) | `parse(dt.isoformat())` liefert `dt` (Wandzeit und Offset) | Erwartung | `tests/property/test_parser_roundtrip_prop.py` | – | offen |
| Z-1 | `tz.py:890 ff.` (`gettz`), PEP 615 | Für jeden IANA-Schlüssel und jeden Zeitpunkt liefern `tz.gettz(k)` und `zoneinfo.ZoneInfo(k)` aus derselben Datenquelle gleiche `utcoffset()`, `dst()` und `tzname()`, für `fold=0` und `fold=1` | Erwartung (Orakel; dateutil dokumentiert die Gleichheit mit zoneinfo nicht) | `tests/property/test_tz_oracle_prop.py` | – | offen |
| Z-2 | `tz.py` (`tzinfo.fromutc`) | Für jeden Schlüssel: `dt.astimezone(z).astimezone(UTC) == dt` für UTC-Zeitpunkte | Vertrag | `tests/property/test_tz_oracle_prop.py` | Z-1 | offen |
| Z-3 | `tz.py:1258–1345` | `datetime_exists`, `datetime_ambiguous` und `resolve_imaginary` stimmen mit der Definition über `fold`/`utcoffset` von `zoneinfo` überein | Vertrag (Orakel) | `tests/property/test_tz_helpers_prop.py` | Z-1 | offen |

## Bekannte Fälle (schon upstream, kein eigener Bericht)
| Claim | Fall | Upstream | Behandlung im Test |
|---|---|---|---|
| Z-1 | `dst()` für `Africa/Casablanca` und `Africa/El_Aaiun` nach dem letzten Übergang; hängt von der tzdata-Version ab (lässt upstream `test_dst_matches_tzdata_zi[tzpath]` auf macOS seit 2026-11-10 scheitern; mit tzdata 2026f konsistent) | offener PR dateutil/dateutil#1667 „Fix dst() for zones that end in permanent DST“ (Maintainer, 2026-11-07); Duplikatsuche 2026-11-15 durch Visionär:in: einziger Treffer | eigener Test, `xfail(strict=False)`, im generischen Z-1-Test wird `dst()` für diese Schlüssel nicht verglichen (Aufgabe #381) |

## Später (Meilenstein 2)
Fuzz-Ziele für P-6, P-7 sowie `tzstr` und `tzical` (Claims werden vor Meilenstein 2 ergänzt, neue IDs).

## Regeln
- IDs werden nie wiederverwendet; ein geänderter Claim bekommt eine neue Version (`Z-1.2`).
- Ein widerlegter Claim ist ein Ergebnis: Test mit `xfail(strict=True)` und Berichtsentwurf in `docs/reports/`.
