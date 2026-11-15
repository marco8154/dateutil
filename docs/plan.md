# Plan

Stand: 2026-11-15. Q1–Q10 beantwortet; Aufgaben gehen raus, sobald der Brief bestätigt ist.
Lead-Budget: 5 Mio. Tokens/Tag (nur Lead-Dienst).

## Meilenstein 1: Hypothesis-Grundgerüst (parser, tz)
Ziel: gemeinsame Strategien, mit denen jeder Claim als kleine B-Aufgabe testbar wird.

| # | Aufgabe (Entwurf) | Level | Pfade | hängt ab von |
|---|---|---|---|---|
| L1 | Pipeline grün auf `master` (erster Lauf von `swarvex.yaml`) | D (Lead) | `swarvex.yaml` | – |
| L2 | `docs/claims.md`: erste Claims zu isoparse, parse, tz | D (Lead), Abnahme Visionär:in | `docs/claims.md` | Brief |
| T1 | Strategien Datum/Zeit/ISO-8601-Strings: `tests/property/strategies_iso.py` + Selbsttests | B | `tests/property/strategies_iso.py`, `tests/property/test_strategies_iso.py` | L1 |
| T2 | Strategien Zeitzonen (IANA-Schlüssel aus `zoneinfo.available_timezones()`, Instants um Übergänge): `tests/property/strategies_tz.py` + Selbsttests | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py` | L1 |
| T3 | Orakel `isoparse` ↔ `datetime.fromisoformat` | B | `tests/property/test_isoparse_oracle_prop.py` | T1, L2 |
| T4 | Orakel `tz.gettz` ↔ `zoneinfo.ZoneInfo` (utcoffset, dst, fold); beide über Fixture `tz_source` aus derselben Quelle | B | `tests/property/test_tz_oracle_prop.py` | T2, L2 |

## Meilenstein 2: Fuzz-Ziele
Nach M1: Fuzz-Ziele (Hypothesis, keine nativen Fuzzer) für `parse` (wirft nur ParserError/OverflowError), `isoparse` und `tzstr`/`tzical`; lange Läufe als `simulation`-Aufgaben mit Zweitlauf.

## Meilenstein 3 (später): rrule und relativedelta
`rrule` gegen RFC 5545, `relativedelta`. Vor dem Start ein kleines Interview (Umfang, Orakel).

## Lead-Pflichten pro Fund (vor dem Einreichen)
1. Duplikatsuche upstream (Issues und PRs, alle Zustände, mehrere Formulierungen; Befehle in `AGENTS.md` oben), Ergebnis im Berichtsentwurf.
2. Reproduktion auf aktuellem upstream-master, Commit-Hash im Berichtsentwurf.
3. Abzeichnung durch die Visionärin / den Visionär; höchstens 2 offene Berichte.
