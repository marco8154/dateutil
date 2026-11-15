# Plan

Stand: 2026-11-15 (Lead-Zyklus 5). Erledigt: #376, #377, #378; in Peer-Review: #379, #381, #386, #387, #388, #389. Neu: #390 (frei), #391 (wartet auf #381, #389). Brief bestätigt (`dbe1e9f`), Claims-Register abgezeichnet, P-9 freigegeben (Nachricht 43). Schätzung M1: 11 Aufgaben.
Lead-Budget: 5 Mio. Tokens/Tag (nur Lead-Dienst).

## Meilenstein 1: Hypothesis-Grundgerüst (parser, tz)
Ziel: gemeinsame Strategien, mit denen jeder Claim als kleine B-Aufgabe testbar wird.

| # | Aufgabe | Level | Pfade | hängt ab von |
|---|---|---|---|---|
| L1 (keine Aufgabe) | Pipeline grün auf `master`: `.venv`, `TZ`, zwei `[tzpath]`-Tests abgewählt (Zyklus 3); Test-Schritt als `swarvex_tools/run_tests.sh` (Zyklus 5, `3c7bb15`) | D (Lead) | `swarvex.yaml`, `swarvex_tools/run_tests.sh` | – |
| #376 | `docs/claims.md`: erste Claims zu isoparse, parse, tz | D (Lead), Abnahme Visionär:in | `docs/claims.md` | Brief |
| #377 | Strategien Datum/Zeit/ISO-8601-Strings: `tests/property/strategies_iso.py` + Selbsttests | B | `tests/property/strategies_iso.py`, `tests/property/test_strategies_iso.py` | – |
| #378 | Strategien Zeitzonen (IANA-Schlüssel aus `zoneinfo.available_timezones()`, Instants um Übergänge): `tests/property/strategies_tz.py` + Selbsttests | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py` | – |
| #379 | Orakel `isoparse` ↔ `datetime.fromisoformat` | B | `tests/property/test_isoparse_oracle_prop.py` | #376, #377 |
| #381 (ersetzt #380) | Orakel `tz.gettz` ↔ `zoneinfo.ZoneInfo` (utcoffset, dst, fold); beide über Fixture `tz_source` aus derselben Quelle | B | `tests/property/test_tz_oracle_prop.py` | #376, #378 |
| #386 | P-8: `parse(dt.isoformat())` liefert `dt` | B | `tests/property/test_parser_roundtrip_prop.py`, `docs/reports/p8-*.md` | – |
| #387 | P-3: isoparse-Offsets → `tz.UTC` / `tzoffset` | B | `tests/property/test_isoparse_tz_prop.py`, `docs/reports/p3-*.md` | #377 |
| #388 | P-4: `24:00` → 00:00 des Folgetags | B | `tests/property/test_isoparse_prop.py` (anhängen), `docs/reports/p4-*.md` | #377 |
| #389 | Z-3: `datetime_exists`/`datetime_ambiguous`/`resolve_imaginary` gegen zoneinfo | B | `tests/property/test_tz_helpers_prop.py`, `docs/reports/z3-*.md` | #378 |
| #390 | Bekannte Fälle P-9 (Woche 53, upstream #1457 u. a.) und Docstring (#1629/#1630) als `xfail(strict=True)` | B | `tests/property/test_isoparse_week53_prop.py` | – |
| #391 | `strategies_tz.transitions`: Cache je Datenquelle (Fund 74) | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py` | #381, #389 |

(#382–#385 geschlossen: gleiche Aufgaben ohne Berichtspfad, ersetzt durch #386–#389.)

P-9 und der Docstring-Fall sind freigegeben und upstream bekannt (Nachricht 43): kein Bericht, nur bekannte Fälle (#390).

## Meilenstein 2: Fuzz-Ziele
Nach M1: Fuzz-Ziele (Hypothesis, keine nativen Fuzzer) für `parse` (wirft nur ParserError/OverflowError), `isoparse` und `tzstr`/`tzical`; lange Läufe als `simulation`-Aufgaben mit Zweitlauf.
Kandidat P-6 (aus Zyklus 5): `isoparse("9999-W53-1")` wirft `OverflowError` statt `ValueError`.

## Meilenstein 3 (später): rrule und relativedelta
`rrule` gegen RFC 5545, `relativedelta`. Vor dem Start ein kleines Interview (Umfang, Orakel).

## Lead-Pflichten pro Fund (vor dem Einreichen)
1. Duplikatsuche upstream (Issues und PRs, alle Zustände, mehrere Formulierungen; Befehle in `AGENTS.md` oben), Ergebnis im Berichtsentwurf.
2. Reproduktion auf aktuellem upstream-master, Commit-Hash im Berichtsentwurf.
3. Abzeichnung durch die Visionärin / den Visionär; höchstens 2 offene Berichte.
