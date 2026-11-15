# Status

Stand: 2026-11-15 (Lead-Zyklus 3, Lead-Dienst)

## Lage
Erster Pipeline-Lauf (Abgabe 438 zu #377) war rot schon auf der Basis: `setup` installierte als Nicht-root-Nutzer nach `~/.local`, das der Test-Schritt nicht sieht (`ModuleNotFoundError: hypothesis`). Behoben in `swarvex.yaml` (L1): `.venv` im Projekt, `TZ=America/New_York` wie upstream-CI, zwei `[tzpath]`-Tests abgewählt (Debian-tzdata im Image). Lokal mit dem neuen Vertrag: Basis 5059 grün, mit Abgabe 438 5105 grün. #377 angenommen (Merge-Zug prüft mit neuem Vertrag). Neu: #386 (P-8, frei), #387/#388 (P-3, P-4, warten auf #377), #389 (Z-3, wartet auf #378). Abgabe 439 (#378) ist noch in der Prüfung.

## Risiken
- `swarvex.yaml` ist ungeprüft: Die Lead-Umgebung hat weder Netz noch das `swarvex`-CLI. Die erste Abgabe (#377 oder #378) ist der erste Pipeline-Lauf; bei rotem `setup` liegt der Fehler bei mir (L1), nicht bei der Abgabe.
- `deadline=None` im Profil verhindert Flakiness durch langsame Sandboxes; dafür fallen Zeitprobleme nicht auf (gewollt, kein Claim betrifft Laufzeit).
- Lead-Budget 5 Mio. Tokens/Tag (nur Lead-Dienst): knappe Zyklen, Reviews vor Planung.
- Pins aus Websuche (PyPI war nicht abrufbar): hypothesis 6.170.5 (2026-10-20), tzdata 2026.6 (IANA 2026f). Gibt es eine Version nicht, schlägt `setup` fehl; dann korrigiere ich den Pin.

- GitHub Actions im Fork: `tests/test_tzpath_data.py::test_dst_matches_tzdata_zi[tzpath]` rot auf macOS (Casablanca, El_Aaiun, 2100/2400). Upstream `dateutil/dateutil` ist seit 2026-11-10 auf macOS ebenfalls rot (PR-Läufe 43319539839, 43319500377, 43247862099; Jobs 3.14 und 3.15 macos-latest), `a78cbd8` war am 2026-11-01 grün. Also Änderung der Runner-Daten (vermutlich Marokko-Änderung in tzdata 2026e/f), nicht unsere Commits. Lokal mit 2026f ist dateutil konsistent. Duplikatsuche (2026-11-15, Visionär:in): offener PR dateutil/dateutil#1667 „Fix dst() for zones that end in permanent DST“ (Maintainer, 2026-11-07), einziger Treffer für Africa/Casablanca und Africa/El_Aaiun. **Kein Bericht von uns.** Als bekannter Fall bei Z-1 in `docs/claims.md` und in Aufgabe #381 vermerkt. Der rote macOS-Job im Fork verschwindet, sobald #1667 upstream gemergt und von uns übernommen ist.

## Rulings
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
- Zyklus 3: Freigabe für Claim P-9 (Woche 53) und Docstring-Fix (Funde 67, 68), siehe Nachricht.
- Nachricht 41 (Freigabe Claims-Register) formal noch offen: Abzeichnung erfolgte im Lead-Gespräch; der Lead-Dienst entscheidet keine Freigaben, daher bitte unter „Mein Konto“ bestätigen, damit sie im öffentlichen Log steht.

## Nächste Schritte
1. Merge-Zug von #377 und nächsten Pipeline-Bericht prüfen: Ist L1 dort grün? Wenn `.venv` fehlt, Installationsort ändern.
2. Abgabe 439 (#378) reviewen, sobald geprüft.
3. Nach Antwort auf die Freigabe: Claim P-9 und Docstring-Fix (Funde 67, 68) als Aufgaben schneiden, sonst Funde verwerfen.
4. Vor Meilenstein 2: Fuzz-Claims ergänzen.
