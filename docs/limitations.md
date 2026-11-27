# Grenzen der Ergebnisse

Stand: 439d2560939138263f004b762c45c21d3fdf5b08

Grundlage ist `docs/claims.md`; bei Widerspruch gilt das Register.

## Allgemeine Grenzen

- Getestete Quelle ist `dateutil/dateutil` @ `a78cbd8`; andere Stände sind nicht geprüft (`docs/claims.md`).
- Ein Claim gilt nur für den getesteten Eingaberaum (`docs/claims.md`, `docs/project-brief.md` Säule 5).
- Ein Test zeigt eine Eigenschaft für den getesteten Bereich. „Bestätigt im getesteten Raum“ ist kein Beweis (`docs/project-brief.md`, Säule 5).
- Die Pipeline nutzt ein festes Hypothesis-Profil: derandomisiert, 200 Beispiele für die meisten Claims (`docs/claims.md`, `docs/project-brief.md` F5).
- Lange Läufe sind einzelne Seeds (meist Seed 1 und 2) mit der in der Status-Spalte genannten Beispielzahl (`docs/claims.md`).
- `tzdata` ist gepinnt (2026.6 für T-2); `dateutil.tz` und `zoneinfo` lesen dieselben Daten (`docs/claims.md`, `docs/project-brief.md` F4b). Andere Datenstände sind nicht geprüft.
- Alle Claims sind exakt; es gibt keine numerische Toleranz (`docs/claims.md`).
- „Erwartung“ ist nicht dokumentiert: ein Verstoß ist ein Fund, kein Vertragsbruch (`docs/claims.md`).

## Je Claim

| ID | Status (aus claims.md) | Getesteter Raum | Nicht abgedeckt | Beleg |
|---|---|---|---|---|
| P-1 | bestätigt im getesteten Raum | upstream-Test; 2 × 200 000 Beispiele | keine Grenze im Register genannt | `tests/property/test_isoparse_prop.py`, `docs/runs/p1-seed1.md`, `docs/runs/p1-seed2.md` |
| P-2 | bestätigt im getesteten Raum | 200 Beispiele Pipeline; 2 × 200 000 mit P-5; nur Strings, die auch `fromisoformat` annimmt | keine Grenze im Register genannt | `tests/property/test_isoparse_oracle_prop.py`, `docs/runs/p2p5-seed1.md`, `docs/runs/p2p5-seed2.md` |
| P-3 | bestätigt im getesteten Raum | 200 Beispiele Pipeline; 2 × `max_examples=200 000` | ausgeführte Anzahl der langen Läufe nicht protokolliert | `tests/property/test_isoparse_tz_prop.py`, `docs/runs/p3-seed1.md`, `docs/runs/p3-seed2.md` |
| P-4 | bestätigt im getesteten Raum | 200 Beispiele Pipeline; 2 × 200 000 | keine Grenze im Register genannt | `tests/property/test_isoparse_prop.py`, `docs/runs/p4-seed1.md`, `docs/runs/p4-seed2.md` |
| P-5 | bestätigt im getesteten Raum | 200 Beispiele Pipeline; 2 × 200 000 mit P-2 | Docstring-Fall „day defaults to 0“ (siehe Abschnitt 4); geprüft wird das Verhalten (Montag) | `tests/property/test_isoparse_oracle_prop.py`, `docs/runs/p2p5-seed1.md`, `docs/runs/p2p5-seed2.md` |
| P-6 | widerlegt | beliebige Strings; 2 × 200 000 (Seed 1/2), danach 2 × 200 000 mit eingeschränkter Duldung `KNOWN_OVERFLOW` (Seed 3/4) | die ersten Läufe duldeten jeden `OverflowError` mit Präfix `9999` | `tests/property/test_isoparse_fuzz_prop.py`, `docs/runs/p6-seed1.md`, `docs/runs/p6-seed2.md`, `docs/runs/p6-seed3.md`, `docs/runs/p6-seed4.md` |
| P-7 | bestätigt im getesteten Raum | beliebige Strings; 200 Beispiele Pipeline; 2 × 200 000 (Ausnahmen), Seed 3 und 4 mit 200 000 (auch Rückgabe `datetime`) | keine Grenze im Register genannt | `tests/property/test_parser_fuzz_prop.py`, `docs/runs/p7-seed1.md`, `docs/runs/p7-seed2.md`, `docs/runs/p7-seed3.md`, `docs/runs/p7-seed4.md` |
| P-8 | bestätigt im getesteten Raum | 200 Beispiele Pipeline; 2 × 200 000 | keine Grenze im Register genannt | `tests/property/test_parser_roundtrip_prop.py`, `docs/runs/p8-seed1.md`, `docs/runs/p8-seed2.md` |
| P-9 | bekannt upstream (xfail strict); weder bestätigt noch widerlegt im Register | `isoparse("2017-W53-1")` als gepinnter Fall | Docstring sichert die Strenge ausdrücklich nicht zu (Erwartung); kein Berichtsentwurf | `tests/property/test_isoparse_week53_prop.py` |
| Z-1 | widerlegt (für `dst()`) | `utcoffset()`, `tzname()`, `dst()`, `fold` 0/1; Übergänge 1970–2040 und 1850–2100; 2 × 20 000 je Test, je Zeitraum | `Africa/Casablanca` und `Africa/El_Aaiun`: `dst()` im generischen Test nicht verglichen; Winamac 2007 nur mit `tzdata` | `tests/property/test_tz_oracle_prop.py`, `docs/runs/z1z2-seed1.md`, `docs/runs/z1z2-seed2.md`, `docs/runs/z1z2w-seed1.md`, `docs/runs/z1z2w-seed2.md` |
| Z-2 | bestätigt im getesteten Raum | 200 Beispiele je Quelle; Übergänge 1970–2040 und 1850–2100; 2 × 20 000 je Zeitraum | keine Grenze im Register genannt | `tests/property/test_tz_oracle_prop.py`, `docs/runs/z1z2-seed1.md`, `docs/runs/z1z2-seed2.md`, `docs/runs/z1z2w-seed1.md`, `docs/runs/z1z2w-seed2.md` |
| Z-3 | bestätigt im getesteten Raum | 200 Beispiele Pipeline; 2 × 20 000 je Test | keine Grenze im Register genannt | `tests/property/test_tz_helpers_prop.py`, `docs/runs/z3-seed1.md`, `docs/runs/z3-seed2.md` |
| T-1 | widerlegt | beliebige Strings; 2 × 200 000 mit den zwei bekannten `TypeError`-Pfaden geduldet | ein Fix nur für Pfad (1) stellt den Claim nicht her | `tests/property/test_tzstr_fuzz_prop.py`, `docs/runs/t1-seed1.md`, `docs/runs/t1-seed2.md` |
| T-2 | widerlegt | POSIX-TZ-Strings aus `tzdata` 2026.6; UTC-Zeitpunkte nach dem letzten Übergang; 359 übrige Schlüssel ohne Abweichung (Stichprobe: 200 Beispiele 2040–2099) | Zahl „231 von 598“ stammt aus einer einmaligen, nicht eingecheckten Durchsicht; kein langer Lauf im Register genannt | `tests/property/test_tzstr_oracle_prop.py` |
| T-3 | widerlegt | beliebige Strings; 2 × 200 000 | keine Grenze im Register genannt | `tests/property/test_tzical_fuzz_prop.py`, `docs/runs/t3-seed1.md`, `docs/runs/t3-seed2.md` |
| R-1 | bestätigt | alle 42 RFC-Beispiele (soweit in `rrule` ausdrückbar) | Beispiele, die `rrule` nicht ausdrücken kann | `tests/property/test_rrule_rfc_golden.py`, `docs/reviews/m3-r1-review.md` |
| R-2 | bestätigt im getesteten Raum | Pipeline-Profil; 2 × 20 000 mit R-5, naiver `dtstart`; mit Zone 2 × 20 000 je Test; `count`-Hälfte mit Zone: Pipeline-Profil, Seeds 1 und 2 ohne Fund | Strategieraum wie bei R-5 (siehe dort) | `tests/property/test_rrule_claims_prop.py`, `docs/runs/r2r5-seed1.md`, `docs/runs/r2r5-seed2.md`, `docs/runs/r2r5tz-seed1.md`, `docs/runs/r2r5tz-seed2.md`, `docs/runs/r2tzcount-seed1.md`, `docs/runs/r2tzcount-seed2.md` |
| R-3 | bestätigt im getesteten Raum | Pipeline-Profil; 2 × 20 000 je Test, naiv und mit Zone | keine Grenze im Register genannt | `tests/property/test_rrule_query_prop.py`, `tests/property/test_rrule_query_tz_prop.py`, `docs/runs/r3-seed1.md`, `docs/runs/r3-seed2.md`, `docs/runs/r3tz-seed1.md`, `docs/runs/r3tz-seed2.md` |
| R-4 | bestätigt im getesteten Raum, nur für naiven `dtstart`; mit Zone widerlegt | Pipeline-Profil; 2 × 20 000 (naiv) | mit Zone: `str(r)` verliert die Zone; upstream bekannt, kein Bericht | `tests/property/test_rrule_roundtrip_prop.py`, `docs/runs/r4-seed1.md`, `docs/runs/r4-seed2.md`, `docs/reports/r4-rrule-str-drops-tzinfo.md` |
| R-5 | bestätigt im getesteten Raum | Pipeline-Profil; 2 × 20 000 mit R-2 | nur einfache Wochentage ohne Ordinalzahl; `bymonthday`/`byweekday` bei YEARLY/MONTHLY und `byweekday` bei WEEKLY nur einwertig; kein `byweekno`/`byyearday`/`bysetpos`/`byeaster`; Filter enthalten immer den `dtstart`-Anker | `tests/property/test_rrule_claims_prop.py`, `docs/runs/r2r5-seed1.md`, `docs/runs/r2r5-seed2.md` |
| R-6 | bestätigt im getesteten Raum | 2 × 20 000 Beispiele; Lead-Vorprüfungen | nur naiver `dtstart`; Grenzen der Strategie `rrule_kwargs()` | `tests/property/test_rruleset_prop.py`, `docs/runs/r6-seed1.md`, `docs/runs/r6-seed2.md` |
| R-7 | widerlegt für gemischte BYDAY-Listen; sonst bestätigt im getesteten Raum | eng: `rrule_kwargs()`, YEARLY/MONTHLY/WEEKLY/DAILY, `until` ≤ `dtstart` + 731 Tage, 2 × 20 000; weit: `count` 1–50, `interval` 1–4, `wkst`, `dtstart` 1890–2210, mehrere Werte je Filter, ordinale BYDAY (rein ordinal), YEARLY ohne BYMONTH, 2 × 5 000 | Filter enthalten immer den `dtstart`-Anker; gemischte BYDAY-Listen (einfach + ordinal) liefern `[]` (Fund, xfail strict); BYSETPOS, BYWEEKNO, BYYEARDAY, BYEASTER, HOURLY/MINUTELY/SECONDLY, Zonen; WEEKLY mit `bymonthday` ist keine RFC-Konformität | `tests/property/test_rrule_reference_prop.py`, `tests/property/test_rrule_reference_wide_prop.py`, `tests/property/rrule_reference.py`, `docs/runs/r7-seed1.md`, `docs/runs/r7-seed2.md`, `docs/runs/r7wide-seed1.md`, `docs/runs/r7wide-seed2.md`, `docs/reviews/m4-review.md`, `docs/reports/r7-wide-mixed-byday.md`, `docs/out-of-scope.md` |
| D-1 | bestätigt im getesteten Raum | Pipeline-Profil; 2 × 200 000 | keine Grenze im Register genannt | `tests/property/test_relativedelta_prop.py`, `docs/runs/d1d2-seed1.md`, `docs/runs/d1d2-seed2.md` |
| D-2 | widerlegt | `datetime(2021, 1, 28) + relativedelta(months=1, days=3)` und Rückweg | Erwartung war zu weit gefasst; engere Fassung D-2.1; Lead-Empfehlung: nicht upstream melden | `tests/property/test_relativedelta_prop.py`, `docs/reports/d2-relativedelta-roundtrip.md` |
| D-2.1 | bestätigt im getesteten Raum | nur `years`/`months`, `dt.day <= 28`; 2 × 200 000 | nur naive `datetime` | `tests/property/test_relativedelta_prop.py`, `docs/runs/d1d2-seed1.md`, `docs/runs/d1d2-seed2.md` |
| D-3 | bestätigt im getesteten Raum | Pipeline-Profil; 2 × 200 000 mit D-4 | keine Grenze im Register genannt | `tests/property/test_relativedelta_fields_prop.py`, `docs/runs/d3d4-seed1.md`, `docs/runs/d3d4-seed2.md` |
| D-4 | bestätigt im getesteten Raum | `rd` nur mit relativen Feldern (auch gebrochen); Pipeline-Profil; 2 × 200 000 mit D-3 | `rd` mit absoluten Feldern und `weekday` | `tests/property/test_relativedelta_fields_prop.py`, `docs/runs/d3d4-seed1.md`, `docs/runs/d3d4-seed2.md` |
| D-5 | bestätigt im getesteten Raum | naive Zeitpunkte 0001–9999; 2 × 200 000 | Upstream-PR #1676 (offen) ändert die Aufteilung auf `seconds`/`microseconds`; D-5 prüft das Additionsergebnis | `tests/property/test_relativedelta_diff_prop.py`, `docs/runs/d5-seed1.md`, `docs/runs/d5-seed2.md` |

## Widerlegte Claims und Berichte

- P-6: `isoparse` wirft `OverflowError` für `9999-W53-1` und `9999-12-31T24:00`. Bericht `docs/reports/p6-isoparse-overflowerror.md`, upstream eingereicht als dateutil/dateutil#1684.
- Z-1: `dst()` weicht in 8 Zonen von `zoneinfo` ab (1970–2040), in 74 weiteren Fällen bei 1850–2100. Berichte `docs/reports/Z-1-dst-inference.md`, `docs/reports/z1w-dst-inference.md`. Bekannter Upstream-Fall: `Africa/Casablanca`/`Africa/El_Aaiun`, offener PR dateutil/dateutil#1667, kein eigener Bericht.
- T-1: `tzstr` wirft `TypeError` für `tzstr("UTC")`/`tzstr("GMT")` und für das Komma-Altformat ohne Standard-Offset. Bericht `docs/reports/t1-tzstr-typeerror.md`; bekannter Upstream-Fall: #1432, #1402, PRs #1453, #1530, #1563.
- T-2: `tzstr(s, posix_offset=True)` lehnt Fuß-Strings mit `<…>` ab und weicht bei Beirut, Gaza/Hebron, Jerusalem, Dublin ab. Berichte `docs/reports/t2-tzstr-angle-brackets.md`, `docs/reports/t2-tzstr-transition-times.md`; bekannter Upstream-Fall Beirut: #1289, PR #1596.
- T-3: `tzical` wirft `OverflowError` für `DTSTART:1970102503000`. Bericht `docs/reports/t3-tzical-overflowerror.md`, upstream eingereicht als dateutil/dateutil#1683.
- R-4 (mit Zone): `str(rrule)` schreibt `DTSTART` ohne Zone, der Rundweg liefert naive Termine. Bericht `docs/reports/r4-rrule-str-drops-tzinfo.md`; upstream bekannt: #348, #637, #603/#604, #806 mit PR #1631; kein Bericht.
- R-7 (gemischte BYDAY-Liste): `rrule(MONTHLY, byweekday=[MO, FR(-1)], …)` liefert `[]`. Berichtsentwurf `docs/reports/r7-wide-mixed-byday.md`; Duplikatsuche upstream offen.
- D-2: `(dt + rd) - rd` kehrt bei Tagen über eine Monatsgrenze nicht zurück. Bericht `docs/reports/d2-relativedelta-roundtrip.md`; Erwartung zu weit, Ersatz D-2.1.

## Nicht untersucht

- R-7-Referenz mit `BYSETPOS`: später.
- R-7-Referenz mit `BYWEEKNO`: später.
- R-7-Referenz mit `BYYEARDAY`, `BYEASTER`, HOURLY/MINUTELY/SECONDLY und Zeitzonen: später.
- Upstream-Bericht zu D-2: nicht, kein Fehler in dateutil.
- Upstream-Bericht zu R-4 (`str(rrule)` verliert die Zone): nicht, upstream bekannt.
