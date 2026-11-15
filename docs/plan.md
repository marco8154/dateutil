# Plan

Stand: 2026-11-15. Brief bestätigt (`dbe1e9f`), Claims-Register abgezeichnet; Aufgaben #376–#379, #381. Schätzung M1: 9 Aufgaben.
Lead-Budget: 5 Mio. Tokens/Tag (nur Lead-Dienst).

## Meilenstein 1: Hypothesis-Grundgerüst (parser, tz)
Ziel: gemeinsame Strategien, mit denen jeder Claim als kleine B-Aufgabe testbar wird.

| # | Aufgabe | Level | Pfade | hängt ab von |
|---|---|---|---|---|
| L1 (keine Aufgabe) | Pipeline grün auf `master` (erster Lauf von `swarvex.yaml`) | D (Lead) | `swarvex.yaml` | – |
| #376 | `docs/claims.md`: erste Claims zu isoparse, parse, tz | D (Lead), Abnahme Visionär:in | `docs/claims.md` | Brief |
| #377 | Strategien Datum/Zeit/ISO-8601-Strings: `tests/property/strategies_iso.py` + Selbsttests | B | `tests/property/strategies_iso.py`, `tests/property/test_strategies_iso.py` | – |
| #378 | Strategien Zeitzonen (IANA-Schlüssel aus `zoneinfo.available_timezones()`, Instants um Übergänge): `tests/property/strategies_tz.py` + Selbsttests | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py` | – |
| #379 | Orakel `isoparse` ↔ `datetime.fromisoformat` | B | `tests/property/test_isoparse_oracle_prop.py` | #376, #377 |
| #381 (ersetzt #380) | Orakel `tz.gettz` ↔ `zoneinfo.ZoneInfo` (utcoffset, dst, fold); beide über Fixture `tz_source` aus derselben Quelle | B | `tests/property/test_tz_oracle_prop.py` | #376, #378 |

Noch zu schneiden in M1: P-3 (UTC-Offsets), P-4 (24:00), P-8 (parse-Roundtrip), Z-3 (tz-Hilfsfunktionen).

## Meilenstein 2: Fuzz-Ziele
Nach M1: Fuzz-Ziele (Hypothesis, keine nativen Fuzzer) für `parse` (wirft nur ParserError/OverflowError), `isoparse` und `tzstr`/`tzical`; lange Läufe als `simulation`-Aufgaben mit Zweitlauf.

## Meilenstein 3 (später): rrule und relativedelta
`rrule` gegen RFC 5545, `relativedelta`. Vor dem Start ein kleines Interview (Umfang, Orakel).

## Lead-Pflichten pro Fund (vor dem Einreichen)
1. Duplikatsuche upstream (Issues und PRs, alle Zustände, mehrere Formulierungen; Befehle in `AGENTS.md` oben), Ergebnis im Berichtsentwurf.
2. Reproduktion auf aktuellem upstream-master, Commit-Hash im Berichtsentwurf.
3. Abzeichnung durch die Visionärin / den Visionär; höchstens 2 offene Berichte.
