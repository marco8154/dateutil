# Plan

Stand: 2026-11-17 (Lead-Zyklus 47). Zyklus 47: M3 geschnitten (#456–#474, Schätzung 22); #455 gemergt (`cb51322`). Zyklus 43: #452 angenommen (Abgabe 555); #454/#455 folgen nach dem Merge automatisch. Zyklus 42: #453 angenommen (Abgabe 556); Reproduktion aller Berichtsentwürfe auf upstream `a78cbd8`; Duplikatsuche angefragt (Nachricht 53). Zyklus 41: Neu #454/#455 (lange Läufe P-7 mit Rückgabeprüfung, nach #452). Schätzung M2: 36. Zyklus 40: #438 und #451 angenommen; aus dem Review neu #453 (M1, Form-Tupel) und #452 (M2, P-7-Rückgabe). Schätzung M1: 14, M2: 34. Zyklus 39: Neu #451 (Meilenstein-Review M1/M2, Stufe A, unabhängig von M3). Schätzung M2: 33. Zyklus 38: #439 angenommen (Abgabe 551, Z-1/Z-2 weit Seed 2), #438 weiter in Nacharbeit. Zyklus 34: #438/#439 in Nacharbeit (Test hatte `max_examples=120`, behoben `b00b68e`; Lauf ≈ 100 min). Zyklus 33: #423/#424 angenommen (Z-3 lange Läufe), #414 gemergt (`b845c37`). Zyklus 24: Neu: #417–#426 (lange Läufe P-3, P-4, P-8, Z-1/Z-2, Z-3; #425/#426 nach #387). Angenommen: #411, #412, #416; #414 in Nacharbeit. Schätzung M2: 30. M3-Interview angefragt (Nachricht 52). Zyklus 23: #415/#416 (lange Läufe P-2/P-5). Zusätzlich gemergt: #379, #381, #391, #394–#396, #397, #398, #399, #408. In Peer-Review: #387, #409, #410, #413. Zyklus 22: #410–#414 (aus Funden 99–101). Gemergt: #376–#378, #386, #388, #389, #390, #392, #393, #402, #404, #405, #406, #407. #408 angenommen (Abgabe 477), Merge-Zug ausstehend. In Peer-Review: #387 (Abgabe 443). Frei: #394–#397, #409 u. a. #391 wartet auf #381. Claims T-1 bis T-3 freigegeben (Nachricht 44), P-9 freigegeben (Nachricht 43). Schätzung M1: 13 Aufgaben.
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
| #413 | `wall_times_near_transitions`: Zone je Datenquelle (`ZoneInfo.no_cache`, Fund 101) | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py` | #391 |
| #414 | Z-1/Z-2-Orakel 1850–2100: Zeitraum-Parameter in den Strategien, neues Modul `test_tz_oracle_wide_prop.py` (Fund 99) | B | `tests/property/strategies_tz.py`, `tests/property/test_strategies_tz.py`, `tests/property/test_tz_oracle_wide_prop.py`, `docs/reports/z1w-*.md` | #413 |
| #453 | Form-Tupel `FULL_DATE_FORMS`/`WEEK_DATE_FORMS` aus `strategies_iso` exportieren, in zwei Tests importieren (Review M1/M2, F7) | B | `tests/property/strategies_iso.py`, `tests/property/test_isoparse_prop.py`, `tests/property/test_isoparse_week53_prop.py` | – |

(#382–#385 geschlossen: gleiche Aufgaben ohne Berichtspfad, ersetzt durch #386–#389.)

P-9 und der Docstring-Fall sind freigegeben und upstream bekannt (Nachricht 43): kein Bericht, nur bekannte Fälle (#390).

## Meilenstein 2: Fuzz-Ziele
Fuzz-Ziele (Hypothesis, keine nativen Fuzzer) für `parse` (wirft nur ParserError/OverflowError), `isoparse` und `tzstr`/`tzical`; lange Läufe als `simulation`-Aufgaben mit Zweitlauf. Schätzung: 20 Aufgaben (inkl. langer Läufe für T-1/T-3).

| # | Aufgabe | Level | Pfade | hängt ab von |
|---|---|---|---|---|
| #392 | Fuzz-Ziel P-6: `isoparse` wirft nur `ValueError`; bekannter Fund `OverflowError` bei Jahr 9999 (`9999-W53-1`, `9999-12-31T24:00`) als xfail + Berichtsentwurf | B | `tests/property/test_isoparse_fuzz_prop.py`, `docs/reports/p6-*.md` | – (nutzt `strategies_iso`, gemergt) |
| #393 | Fuzz-Ziel P-7: `parse` wirft nur `ParserError`/`OverflowError` | B | `tests/property/test_parser_fuzz_prop.py`, `docs/reports/p7-*.md` | – |
| #394 / #395 | Langer Lauf P-6, 200 000 Beispiele, Seed 1 / Seed 2 (Zweitlauf), Protokoll | A (`simulation`) | `docs/runs/p6-seed1.md` / `docs/runs/p6-seed2.md` | #392 |
| #396 / #397 | Langer Lauf P-7, 200 000 Beispiele, Seed 1 / Seed 2 (Zweitlauf), Protokoll | A (`simulation`) | `docs/runs/p7-seed1.md` / `docs/runs/p7-seed2.md` | #393 |
| #398 / #399 | Langer Lauf P-1 (upstream `test_timespec_auto`), 200 000 Beispiele, Seed 1 / Seed 2, Protokoll (lokal: 5000 Beispiele 9 s) | A (`simulation`) | `docs/runs/p1-seed1.md` / `docs/runs/p1-seed2.md` | – |
| #402 | Fuzz-Ziel T-1 `tzstr`; bekannter Fund `TypeError` für `UTC`/`GMT` als xfail + Bericht | B | `tests/property/test_tzstr_fuzz_prop.py`, `docs/reports/t1-*.md` | – |
| #405 (ersetzt #403) | Orakel T-2 `tzstr` (Fuß-Strings aus tzdata) ↔ zoneinfo; `<…>`-Ablehnung und Übergangszeiten als xfail + zwei Berichte | B | `tests/property/test_tzstr_oracle_prop.py`, `docs/reports/t2-*.md` | – |
| #404 | Fuzz-Ziel T-3 `tzical`; bekannter Fund `OverflowError` bei kaputtem `DTSTART` als xfail + Bericht | B | `tests/property/test_tzical_fuzz_prop.py`, `docs/reports/t3-*.md` | – |
| #406 / #407 | Langer Lauf T-1, 200 000 Beispiele, Seed 1 / Seed 2 (lokal: 5000 Beispiele 8 s) | A (`simulation`) | `docs/runs/t1-seed1.md` / `docs/runs/t1-seed2.md` | #402 |
| #408 / #409 | Langer Lauf T-3, 200 000 Beispiele, Seed 1 / Seed 2 (lokal: 5000 Beispiele 10 s) | A (`simulation`) | `docs/runs/t3-seed1.md` / `docs/runs/t3-seed2.md` | #404 |
| #410 | P-6-Fuzz-Ziel: `OverflowError`-Ausnahme von `startswith("9999")` auf `KNOWN_OVERFLOW` (Wochendatum nach 31.12.9999, Stunde 24 am letzten Tag) einschränken (Fund 100) | B | `tests/property/test_isoparse_fuzz_prop.py`, `docs/reports/p6-*.md` | – |
| #411 / #412 | Langer Lauf P-6 mit eingeschränkter Ausnahme, Seed 3 / Seed 4 | A (`simulation`) | `docs/runs/p6-seed3.md` / `docs/runs/p6-seed4.md` | #410 |
| #415 / #416 | Langer Lauf P-2/P-5 (`test_isoparse_oracle_prop.py`, beide Tests), 200 000 Beispiele, Seed 1 / Seed 2 (lokal: 5000 Beispiele je Test 20 s) | A (`simulation`) | `docs/runs/p2p5-seed1.md` / `docs/runs/p2p5-seed2.md` | – (#379 gemergt) |
| #417 / #418 | Langer Lauf P-8 (`test_parser_roundtrip_prop.py`), 200 000 Beispiele, Seed 1 / Seed 2 | A (`simulation`) | `docs/runs/p8-seed1.md` / `docs/runs/p8-seed2.md` | – |
| #419 / #420 | Langer Lauf P-4 (`test_midnight_24_is_next_day`), 200 000 Beispiele, Seed 1 / Seed 2 | A (`simulation`) | `docs/runs/p4-seed1.md` / `docs/runs/p4-seed2.md` | – |
| #421 / #422 | Langer Lauf Z-1/Z-2 (`test_tz_oracle_prop.py`), 20 000 Beispiele (lokal 2000 in 125 s), Seed 1 / Seed 2 | A (`simulation`) | `docs/runs/z1z2-seed1.md` / `docs/runs/z1z2-seed2.md` | – |
| #423 / #424 | Langer Lauf Z-3 (`test_tz_helpers_prop.py`), 20 000 Beispiele (lokal 2000 in 170 s), Seed 1 / Seed 2 | A (`simulation`) | `docs/runs/z3-seed1.md` / `docs/runs/z3-seed2.md` | – |
| #425 / #426 | Langer Lauf P-3 (`test_isoparse_tz_prop.py`), 200 000 Beispiele, Seed 1 / Seed 2 | A (`simulation`) | `docs/runs/p3-seed1.md` / `docs/runs/p3-seed2.md` | #387 |
| #451 | Meilenstein-Review M1/M2 (nur lesen), Bericht `docs/reviews/m1-m2-review.md` | A (`review`) | `docs/reviews/m1-m2-review.md` | – |
| #452 | P-7-Fuzz-Ziel: Rückgabe von `parse` ist ein `datetime` (Review M1/M2, F2) | B | `tests/property/test_parser_fuzz_prop.py`, `docs/reports/p7-*.md` | – |
| #454 / #455 | Langer Lauf P-7 mit Rückgabeprüfung (`test_parser_fuzz_prop.py`), 200 000 Beispiele, Seed 3 / Seed 4 | A (`simulation`) | `docs/runs/p7-seed3.md` / `docs/runs/p7-seed4.md` | #452 |

## Meilenstein 3: rrule und relativedelta
Freigegeben 2026-11-17 (Nachricht 52: Q1–Q4 ja, Claims R-1 bis R-5, D-1 bis D-3 abgezeichnet; D-4 über Q3). Schätzung 22 Aufgaben (19 geschnitten, Rest: Meilenstein-Review und Puffer). Jede Testdatei gehört genau einer Aufgabe; die langen Läufe folgen automatisch nach dem Merge ihres Tests.

| Aufgabe | Inhalt | Stufe | Pfade | Hängt ab von |
|---|---|---|---|---|
| #456 | Strategie `rrule_kwargs()` (endliche Regeln, verankerte `byxxx`-Filter, `until`-Fenster je Frequenz) | B | `tests/property/strategies_rrule.py`, `test_strategies_rrule.py` | – |
| #457 | Strategien für `relativedelta` (`base_datetimes`, `relative_time_kwargs`, `relative_kwargs`, `absolute_kwargs`) | B | `tests/property/strategies_relativedelta.py`, `test_strategies_relativedelta.py` | – |
| #458 | RFC 5545 3.8.5.3: RRULE-Beispiele als JSON (`daten`, Rolle literature) | A | `tests/property/data/rfc5545_rrule_examples.json` | – |
| #459 | Golden-Test R-1 | B | `tests/property/test_rrule_rfc_golden.py`, `docs/reports/r1-*.md` | #458 |
| #460 | R-2 und R-5 | B | `tests/property/test_rrule_claims_prop.py`, `docs/reports/r2-*.md`, `r5-*.md` | #456 |
| #461 | R-3 (`count`, `before`, `after`, `between`, mit/ohne Cache) | B | `tests/property/test_rrule_query_prop.py`, `docs/reports/r3-*.md` | #456 |
| #462 | R-4 (`rrulestr(str(r))`) | B | `tests/property/test_rrule_roundtrip_prop.py`, `docs/reports/r4-*.md` | #456 |
| #463 | D-1 und D-2 | B | `tests/property/test_relativedelta_prop.py`, `docs/reports/d1-*.md`, `d2-*.md` | #457 |
| #464 | D-3 und D-4 | B | `tests/property/test_relativedelta_fields_prop.py`, `docs/reports/d3-*.md`, `d4-*.md` | #457 |
| #465 / #466 | Lange Läufe R-2/R-5, 20 000 Beispiele, Seed 1 / 2 | A (`simulation`) | `docs/runs/r2r5-seed1.md` / `-seed2.md` | #460 |
| #467 / #468 | Lange Läufe R-3, 20 000, Seed 1 / 2 | A | `docs/runs/r3-seed*.md` | #461 |
| #469 / #470 | Lange Läufe R-4, 20 000, Seed 1 / 2 | A | `docs/runs/r4-seed*.md` | #462 |
| #471 / #472 | Lange Läufe D-1/D-2, 200 000, Seed 1 / 2 | A | `docs/runs/d1d2-seed*.md` | #463 |
| #473 / #474 | Lange Läufe D-3/D-4, 200 000, Seed 1 / 2 | A | `docs/runs/d3d4-seed*.md` | #464 |
| später | Meilenstein-Review M3 (Stufe A, `review`, anderes Modell) | A | `docs/reviews/m3-review.md` | #459–#464 |
| später (nicht M3) | Brute-Force-Referenzgenerator für kleine Regeln | C | – | – |

## Lead-Pflichten pro Fund (vor dem Einreichen)
1. Duplikatsuche upstream (Issues und PRs, alle Zustände, mehrere Formulierungen; Befehle in `AGENTS.md` oben), Ergebnis im Berichtsentwurf.
2. Reproduktion auf aktuellem upstream-master, Commit-Hash im Berichtsentwurf.
3. Abzeichnung durch die Visionärin / den Visionär; höchstens 2 offene Berichte.
