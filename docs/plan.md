# Plan

Stand: 2026-11-15 (Lead-Zyklus 4). Erledigt: #376, #377, #378; #386 in Peer-Review. Brief bestätigt (`dbe1e9f`), Claims-Register abgezeichnet; Aufgaben #376–#379, #381, #386–#389. Schätzung M1: 9 Aufgaben.
Lead-Budget: 5 Mio. Tokens/Tag (nur Lead-Dienst).

## Meilenstein 1: Hypothesis-Grundgerüst (parser, tz)
Ziel: gemeinsame Strategien, mit denen jeder Claim als kleine B-Aufgabe testbar wird.

| # | Aufgabe | Level | Pfade | hängt ab von |
|---|---|---|---|---|
| L1 (keine Aufgabe) | Pipeline grün auf `master`: `.venv`, `TZ`, zwei `[tzpath]`-Tests abgewählt (lokal grün, Zyklus 3) | D (Lead) | `swarvex.yaml` | – |
| #376 | `docs/claims.md`: erste Claims zu isoparse, parse, tz | D (Lead), Abnahme Visionär:in | `docs/claims.md` | Brief |
| #377 | Strategien Datum/Zeit/ISO-8601-Strings: `tests/property/strategies_iso.py` + Selbsttests | B | `tests/property/strategies_iso.py`, `tests/property/test_strategies_iso.py` | – |
| #378 | Strategien Zeitzonen (IANA-Schlüssel aus `zoneinfo.available_timezones()`, Instants um Übergänge): `tests/property/strategies_tz.py` + Selbsttests | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py` | – |
| #379 | Orakel `isoparse` ↔ `datetime.fromisoformat` | B | `tests/property/test_isoparse_oracle_prop.py` | #376, #377 |
| #381 (ersetzt #380) | Orakel `tz.gettz` ↔ `zoneinfo.ZoneInfo` (utcoffset, dst, fold); beide über Fixture `tz_source` aus derselben Quelle | B | `tests/property/test_tz_oracle_prop.py` | #376, #378 |
| #386 | P-8: `parse(dt.isoformat())` liefert `dt` | B | `tests/property/test_parser_roundtrip_prop.py`, `docs/reports/p8-*.md` | – |
| #387 | P-3: isoparse-Offsets → `tz.UTC` / `tzoffset` | B | `tests/property/test_isoparse_tz_prop.py`, `docs/reports/p3-*.md` | #377 |
| #388 | P-4: `24:00` → 00:00 des Folgetags | B | `tests/property/test_isoparse_prop.py` (anhängen), `docs/reports/p4-*.md` | #377 |
| #389 | Z-3: `datetime_exists`/`datetime_ambiguous`/`resolve_imaginary` gegen zoneinfo | B | `tests/property/test_tz_helpers_prop.py`, `docs/reports/z3-*.md` | #378 |

(#382–#385 geschlossen: gleiche Aufgaben ohne Berichtspfad, ersetzt durch #386–#389.)

Kandidaten (warten auf Freigabe der Visionärin / des Visionärs, Nachricht in Zyklus 3): neuer Claim P-9 (`isoparse` lehnt Woche 53 in Jahren mit 52 ISO-Wochen ab; Fund 68) und Docstring-Fix „day defaults to 0“ → Montag (Fund 67).

## Meilenstein 2: Fuzz-Ziele
Nach M1: Fuzz-Ziele (Hypothesis, keine nativen Fuzzer) für `parse` (wirft nur ParserError/OverflowError), `isoparse` und `tzstr`/`tzical`; lange Läufe als `simulation`-Aufgaben mit Zweitlauf.

## Meilenstein 3 (später): rrule und relativedelta
`rrule` gegen RFC 5545, `relativedelta`. Vor dem Start ein kleines Interview (Umfang, Orakel).

## Lead-Pflichten pro Fund (vor dem Einreichen)
1. Duplikatsuche upstream (Issues und PRs, alle Zustände, mehrere Formulierungen; Befehle in `AGENTS.md` oben), Ergebnis im Berichtsentwurf.
2. Reproduktion auf aktuellem upstream-master, Commit-Hash im Berichtsentwurf.
3. Abzeichnung durch die Visionärin / den Visionär; höchstens 2 offene Berichte.
