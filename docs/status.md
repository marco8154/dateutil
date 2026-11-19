# Status

Stand: 2026-11-19 (Lead-Zyklus 92, Lead-Dienst)

## Lage
Zyklus 92 (Anlass: Nachrichten 71/72 offen, 0 freie Aufgaben bei 0 aktiven Agenten). Merge-Zug hat #518/#519 geliefert (`50293b4`, `d3c7b69`): R-2 count mit Zone doppelt bestätigt. **Abgabe 664 (#523, SPDX entfernen)** inhaltlich geprüft: entfernt die Zeile aus genau den 11 Dateien, die `grep -rln SPDX tests/` auf master liefert, sonst nichts; erster Pipeline-Bericht grün (5231 passed). Annahme abgelehnt, weil die Prüfung noch läuft („checking“) → nächster Zyklus annehmen. Kein neuer Schnitt (Ruling Zyklus 76). 71/72 und 57 weiter ohne Antwort; 443, 531, 533, 538 weiter im Peer-Review-Stau (ältester ≈ 79 h).

Zyklus 91 (Anlass: Nachrichten 71/72 offen, 0 freie Aufgaben bei 0 aktiven Agenten). Keine Änderung: keine Abgabe zur Prüfung, 2 Abgaben im Merge-Zug (u. a. #519), 3 Aufgaben blockiert (werden ohne Lead frei, #523 nach dem Merge). Kein neuer Schnitt (Ruling Zyklus 76; bei 0 aktiven Agenten würde ein Schnitt nur liegen). 71/72 und 57 weiter ohne Antwort; 443, 531, 533, 538 weiter im Peer-Review-Stau (ältester ≈ 78 h).

Zyklus 90 (Anlass: Abgabe 657 geprüft, Nachrichten 71/72 offen, 0 freie Aufgaben bei 0 aktiven Agenten). **657 (#519, Seed 2) angenommen**: 20 000 passing, 0 failing, sha256 stimmt mit master; R-2 count mit Zone damit doppelt bestätigt, sobald der Merge-Zug beide Protokolle liefert. #523 (SPDX) wird danach von selbst frei. Kein neuer Schnitt (Ruling Zyklus 76). 71/72 und 57 weiter ohne Antwort; 443, 531, 533, 538 weiter im Peer-Review-Stau.

Zyklus 89 (Anlass: Nachrichten 71/72 offen, 0 freie Aufgaben bei 0 aktiven Agenten). Abgabe 657 (#519, R-2 count mit Zone, Seed 2) inhaltlich geprüft: 20 000 passing, 0 failing, sha256 stimmt mit master; Annahme noch nicht möglich (Pipeline-Prüfung läuft), folgt im nächsten Zyklus. Keine Funde offen. Kein neuer Schnitt (Ruling Zyklus 76). 71/72 und 57 weiter ohne Antwort; 443, 531, 533, 538 weiter im Peer-Review-Stau.

Zyklus 88 (Anlass: Abgabe 654 geprüft, Nachrichten 71/72 offen, 0 freie Aufgaben bei 0 aktiven Agenten). **654 (#518, langer Lauf R-2 count mit Zone, Seed 1) angenommen**: 20 000 passing, 0 failing, keine Funde; sha256 der Testdatei stimmt mit master. #519 (Seed 2) liegt als Abgabe 657 in der Pipeline; #523 folgt nach #518–#520 von selbst. `docs/claims.md` R-2: #517 gemergt, r2r5tz-Läufe gemergt. Kein neuer Schnitt (Ruling Zyklus 76: M4 erst nach Antwort auf Nachricht 72; 0 aktive Agenten). 71/72 und 57 brauchen Handgriffe der Person außerhalb der Sandbox (GitHub-Suche, RFC-Text einchecken). 443, 531, 533, 538 weiter im Peer-Review-Stau (ältester ≈ 78 h). Lage-Abschnitt gekürzt: ältere Zyklen stehen in `git log -p docs/status.md`.

## Risiken
- Abgaben 440–444, 446 haben Pipeline-Berichte vom alten, kaputten Test-Schritt (Gegenprobe „Basis rot“). Peer-Reviewer:innen sollten das wissen; der Merge-Zug prüft sie mit `run_tests.sh` neu.
- Peer-Review hängt an Agenten anderer Personen; ohne sie stauen sich eigene Abgaben. Falls das anhält: Visionär:in fragen, ob weitere Beitragende geworben werden können.
- Abgabe 446: mit `-n auto` ~55 s für eine Datei, weil jeder Worker `transitions()` neu rechnet; Gesamtlauf lokal 86–98 s, unkritisch.
- `deadline=None` im Profil verhindert Flakiness durch langsame Sandboxes; dafür fallen Zeitprobleme nicht auf (gewollt, kein Claim betrifft Laufzeit).
- Lead-Budget 5 Mio. Tokens/Tag (nur Lead-Dienst): knappe Zyklen, Reviews vor Planung.
- Pins aus Websuche (PyPI war nicht abrufbar): hypothesis 6.170.5 (2026-10-20), tzdata 2026.6 (IANA 2026f). Gibt es eine Version nicht, schlägt `setup` fehl; dann korrigiere ich den Pin.

- GitHub Actions im Fork: `tests/test_tzpath_data.py::test_dst_matches_tzdata_zi[tzpath]` rot auf macOS (Casablanca, El_Aaiun, 2100/2400). Upstream `dateutil/dateutil` ist seit 2026-11-10 auf macOS ebenfalls rot (PR-Läufe 43319539839, 43319500377, 43247862099; Jobs 3.14 und 3.15 macos-latest), `a78cbd8` war am 2026-11-01 grün. Also Änderung der Runner-Daten (vermutlich Marokko-Änderung in tzdata 2026e/f), nicht unsere Commits. Lokal mit 2026f ist dateutil konsistent. Duplikatsuche (2026-11-15, Visionär:in): offener PR dateutil/dateutil#1667 „Fix dst() for zones that end in permanent DST“ (Maintainer, 2026-11-07), einziger Treffer für Africa/Casablanca und Africa/El_Aaiun. **Kein Bericht von uns.** Als bekannter Fall bei Z-1 in `docs/claims.md` und in Aufgabe #381 vermerkt. Der rote macOS-Job im Fork verschwindet, sobald #1667 upstream gemergt und von uns übernommen ist.

## Rulings
- Ruling: Claims R-2/R-4/R-5 auch mit zeitzonenbehaftetem `dtstart` prüfen (#493/#494), ohne neue Claims: gleicher Claim, größerer getesteter Raum (wie #414 für Z-1). Grund: Freigabe M3 deckt die Claims, nicht nur naive Zeiten. Kosten, falls falsch: Visionär:in stuft den R-4-Fund als außerhalb des Claims ein; dann bleibt er Berichtsentwurf.
- Ruling: M3-Testdateien je Claim-Gruppe getrennt (R-3 → `test_rrule_query_prop.py`, D-3/D-4 → `test_relativedelta_fields_prop.py`), Register angepasst. Grund: parallele Aufgaben schreiben nie in dieselbe Datei. Kosten, falls falsch: zwei Dateien mehr.
- Ruling: `strategies_rrule.py` darf die Frequenz-Konstanten aus `dateutil.rrule` importieren (reine `int`-Namen), sonst nichts aus dateutil. Grund: lesbarer, kein Erwartungswert hängt daran. Kosten, falls falsch: Konstanten als Zahlen nachschreiben.
- Ruling: R-1-Daten als Aufgabe für direkt verbundene Agenten (`daten`), weil Sandboxes und Lead-Dienst die RFC nicht abrufen können; Prüfung durch Peer-Review und Stichprobe. Kosten, falls falsch: ein falsch abgeschriebenes Beispiel erscheint als Scheinfund; der Golden-Test darf die Daten nicht ändern, meldet Zweifel aber.
- Ruling: Property-Tests in `tests/property/` setzen kein `max_examples`; Prüfung in `run_tests.sh`, lange Läufe protokollieren die Hypothesis-Statistik. Grund: Ein Deckel im Test überschrieb `SWARVEX_MAX_EXAMPLES` unbemerkt (#438/#439). Kosten, falls falsch: Ein Test, der wirklich weniger Beispiele braucht, muss das anders lösen (z. B. schnellere Strategie).
- Ruling: In Lauf-Protokollen gilt der Basis-Commit der Aufgabe (`task_details` → `base_commit`) als Commit; künftige Lauf-Aufgaben nennen ihn statt `git rev-parse HEAD`. Grund: Die Sandbox der Beitragenden hat kein `git` (Fund 96). Kosten, falls falsch: keine, die sha256 der Testdatei sichert den Stand zusätzlich.
- Ruling: Test-Schritt in `swarvex_tools/run_tests.sh` statt inline in `swarvex.yaml`. Grund: Die Pipeline zerlegte die zitierten `--deselect`-Argumente. Kosten, falls falsch: Pfad oder Shell des Skripts anpassen.
- Ruling: Docstring-Fall (#1629) als `xfail(strict=True)` auf den Docstring-Text, wie von der Visionärin / dem Visionär verlangt. Grund: so fällt die upstream-Korrektur auf. Kosten, falls falsch: ein Test, der Text statt Verhalten prüft.
- Ruling: Pipeline-Abhängigkeiten in `.venv` im Projektordner statt `pip --user`. Grund: Der Sandbox-Nutzer ist nicht root, `~/.local` aus `setup` war im Test-Schritt nicht sichtbar. Kosten, falls falsch: Test-Schritt findet `.venv/bin/python` nicht (klare Meldung), dann anderer Installationsort.
- Ruling: `TZ=America/New_York` im Test-Schritt, wie upstream `.github/workflows/validate.yml`. Grund: Mit lokaler Zone UTC scheitert upstream `test_gettz_local_abbreviation_without_time_zone_data` (`gettz("UTC")` liefert `tzutc`). Kosten, falls falsch: keine, gleiche Bedingung wie upstream.
- Ruling: `test_gettz_link[tzpath-Europe/Monaco-Europe/Paris]` und `test_dst_matches_tzdata_zi[tzpath]` abgewählt. Grund: Sie lesen die System-Zonendaten des Images (Debian tzdata 2026f-0+deb13u1, Monaco und Guernsey eigene Zonen statt Links), nicht dateutil-Verhalten; die `[tzdata]`-Varianten laufen weiter gegen die gepinnten Daten. Kosten, falls falsch: eine Abweichung in den System-Daten bleibt unbemerkt; der Z-1-Test (#381) prüft mit `tz_source` beide Quellen.
- Ruling: B-Aufgaben mit `min_trust` 0 statt 1. Grund: bisher nur eine beitragende Person mit Stufe 0; sonst nimmt niemand die Aufgaben. Kosten, falls falsch: mehr Nacharbeit, die Pipeline prüft trotzdem.
- Ruling: Strategien importieren kein dateutil, erwartete Werte nur mit `datetime.timezone`/`zoneinfo`. Grund: sonst prüft das Orakel dateutil gegen sich selbst. Kosten, falls falsch: keine.
- Ruling: Alle Commits ohne `Co-authored-by` für KI, mit `Assisted-by`, auch im Fork. Grund: upstream-`AGENTS.md` und Vorgabe Q7; Commits bleiben ohne Umschreiben einreichbar. Kosten, falls falsch: keine.
- Ruling: Projektdokumente als `.md` unter `docs/`. Grund: Sphinx liest nur `.rst`, pytest sammelt nur `test_*.py`. Kosten, falls falsch: Dateien verschieben.
- Ruling: Hypothesis-Profil als pytest-Plugin `swarvex_tools/hypothesis_profile.py` (per `-p` geladen) statt Änderung an upstream `tests/conftest.py`. Grund: Upstream-Dateien bleiben gleich. Kosten, falls falsch: Profil in conftest verschieben.
- Ruling: Gemeinsame Strategien als `tests/property/strategies_<thema>.py`. Grund: `tests/property/` hat kein `__init__.py`, Import ohne Paketumbau. Kosten, falls falsch: umbenennen.
- Ruling: SPDX `Apache-2.0 AND BSD-3-Clause` nur in neuen Dateien außerhalb von `src/` und `tests/`. Grund: upstream führt keine Header. Kosten, falls falsch: Header ergänzen.

## Offene Freigaben
- Nachricht 72 (2026-11-19, Frage): Q1 Duplikatsuche R-4, Q2 Meilenstein M4 (Brute-Force-Referenz für rrule, Claim R-7).
- Nachricht 71 (2026-11-18, Frage): RFC-5545-Text und Errata-Auszug nach `docs/sources/` einchecken (R-1).
- Nachricht 57 (2026-11-17): Upstream-Berichte T-3 und P-6 einreichen (höchstens 2 offen); danach Reihenfolge T-2a, T-2b, Z-1+Z-1w als ein Issue, T-1 als Kommentar an #1432.

## Nächste Schritte
0. R-4-Bericht: Reproduktion erledigt (Zyklus 76); Duplikatsuche liegt als Nachricht 72 Q1 bei der Visionärin / dem Visionär — Treffer in den Abschnitt „Duplicate search“ eintragen. Nachricht 72 Q2 (M4): bei Ja M4 interviewen/schneiden (Referenzmodul C, Orakel B, 2 lange Läufe A, Review A; Claim R-7 in `docs/claims.md`).
1. Nachricht 71 (RFC-Text): sobald `docs/sources/rfc5545.txt` auf master liegt, #458 neu schneiden (Quelle = lokale Datei im Kontext, kein Netz nötig) und #459 danach; danach eigenes kleines Review R-1 (`docs/reviews/m3-r1-review.md`, nach #459). Bei „R-1 raus“: `docs/out-of-scope.md`.
2. M3: D-5 und R-6 bestätigt (#510/#511/#513/#514 angenommen), #515 umgesetzt. #517 angenommen (Zyklus 83); offen: #518 angenommen (Zyklus 88), #519 angenommen (Zyklus 90, Abgabe 657), #520 angenommen (Zyklus 85), #523 (SPDX entfernen) als Abgabe 664 geprüft, Annahme nach Pipeline-Ende. Nach Merge von #523: Prüfung `grep -rln SPDX tests/` leer als Schritt in `swarvex_tools/run_tests.sh` (eigene Arbeit, geschützt).
3. D-2-Bericht: Empfehlung **nicht upstream** (Nachricht 66). Bericht bleibt Entwurf.
4. Nachricht 57: Issue-Nummern von T-3 und P-6 in die xfail-Gründe und `docs/claims.md` eintragen, sobald die Visionärin / der Visionär sie schickt; dann nächste zwei Berichte vorschlagen. Danach M1/M2-Abzeichnung.
5. Peer-Reviews 443 (#387, P-3), 531/533 (#417/#418, P-8), 538 (#420, P-4 Seed 2) abwarten (eigene Person; brauchen Agenten einer anderen Person); danach Laufzahlen in `docs/claims.md` (P-3 nach #425/#426).
6. Merge-Zug: erledigt (Zyklus 87), D-5/R-6-Protokolle auf master.
