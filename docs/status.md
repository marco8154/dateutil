# Status

Stand: 2026-11-16 (Lead-Zyklus 10, Lead-Dienst)

## Lage
Zyklus 10: Wieder nur Anlass Nachricht 44 (eigene Freigabe-Anfrage, wartet auf die Visionärin / den Visionär). Unverändert: 9 Abgaben ohne Peer-Review (älteste 5,4 h), keine aktiven Agenten, #398/#399 frei. Nichts zu tun. Versehen: Die Commits `70bc7c5` (Zyklus 9) und `fde4c39` (Zyklus 10) tragen einen `Co-Authored-By`-Trailer für die KI, entgegen der Ruling unten und `AGENTS.md`. Sie sind schon gepusht; die Historie schreibe ich nicht um (nur Status-Commits, gehen nie upstream). Ab jetzt wieder `Assisted-by`.

Zyklus 9: Anlass war nur die eigene offene Freigabe-Anfrage (Nachricht 44, wartet auf die Visionärin / den Visionär). Keine neuen Peer-Reviews, keine Funde, keine aktiven Agenten; frei bleiben #398/#399 (Angebot ≥ Nachfrage). Nichts weiter zu tun.

Zyklus 8: Keine neuen Peer-Reviews; die 9 Abgaben (440–444, 446, 447, 449, 450) stammen alle von Agenten der eigenen Person und warten weiter. Nachricht 44 (T-1 bis T-3) weiter offen. Keine Funde gemeldet. Gegen Leerlauf ohne Freigabe: #398/#399, lange Läufe für P-1 (upstream `test_timespec_auto`, schon auf `master`, daher sofort frei), Seed 1/2, je 200 000 Beispiele (lokal 5000 in 9 s, also ~7 min). Schätzung M2 auf 12 Aufgaben.

Zyklus 7: Abgaben 449 (#392, P-6) und 450 (#393, P-7) sind in der Pipeline grün (je 5124 passed; 449: 19 xfailed inkl. der zwei 9999-Fälle) und erfüllen laut Diff alle Kriterien. Eigene Person: Review-Fragen gesetzt, warten auf Peer-Review (jetzt 9 Abgaben). P-7: keine Funde. Gegen Leerlauf: `swarvex_tools/hypothesis_profile.py` kann lange Läufe (`SWARVEX_MAX_EXAMPLES`, dann `--hypothesis-seed` statt derandomisiert; lokal geprüft: gleicher Seed gleiche Eingaben, Standard 200 unverändert), Commit `030ba69`. Damit #394–#397 (lange Läufe P-6/P-7, je Erst- und Zweitlauf mit Seed 1/2, Level A `simulation`), freigeschaltet nach Merge von #392/#393. Claims T-1 bis T-3 (`tzstr`, `tzical`) als Entwurf in `docs/claims.md`, Freigabe angefragt (Nachricht 44). Lokale Probe zu T-2 (vorläufig): `tzstr` lehnt 231 tzdata-Fuß-Strings mit `<…>`-Abkürzungen ab; 6 Zonen (Beirut, Gaza, Hebron, Jerusalem u. a.) mit Übergangszeiten `/0`, `/26`, `/50` weichen von zoneinfo ab.

Zyklus 6: Erster Pipeline-Lauf mit `swarvex_tools/run_tests.sh` (Abgabe 447 zu #390) ist grün: 5123 passed, 19 xfailed, beide neuen Tests xfailed. Damit ist L1 in der Pipeline bestätigt. Abgabe 447 erfüllt alle Kriterien (Diff geprüft); eigene Person: Review-Fragen gesetzt, wartet auf Peer-Review. Engpass ist Peer-Review (7 Abgaben, alle von Agenten der eigenen Person, keine aktiven Agenten anderer Personen). Gegen Leerlauf M2 begonnen: #392 (Fuzz P-6 `isoparse`) und #393 (Fuzz P-7 `parse`), beide ohne Abhängigkeit frei. Lokal auf `master` bestätigt: `isoparse("9999-W53-1")` und `isoparse("9999-12-31T24:00")` werfen `OverflowError` (P-6 widerlegt, vorläufig; Test und Berichtsentwurf kommen mit #392).

Zyklus 5: Die Pipeline lief seit Zyklus 4 nie wirklich: Sie meldete `sh: Unterminated quoted string` für die `--deselect`-Argumente in `swarvex.yaml` (Funde 72, 73, 75, 78), und die Gegenprobe galt deshalb als „Basis rot“. Behoben in `3c7bb15`: Der Test-Schritt ist jetzt `sh swarvex_tools/run_tests.sh` (L1). Lokal damit: Basis 5123 grün; mit allen sechs Abgaben zusammen (440–444, 446) 5140 passed, 21 xfailed, 8 xpassed, zweimal gleich (deterministisch). Alle sechs Abgaben stammen von Agenten der eigenen Person: nicht annehmbar, Review-Fragen gesetzt, warten auf Peer-Review. Nachricht 43 freigegeben: P-9 in `docs/claims.md`, Woche 53 und Docstring als bekannte Fälle (upstream #1457 u. a., #1629/#1630), Aufgabe #390. Fund 74 (Cache in `strategies_tz.transitions` über Datenquellen hinweg) → Aufgabe #391 (wartet auf #381, #389). Funde 67, 68, 72–75, 78 erledigt.

Abgabe 442 (#381) widerlegt Z-1 für `dst()` in 8 Zonen (strict xfail, Berichtsentwurf `docs/reports/Z-1-dst-inference.md`). Laut Bericht liegt der Fehler meist bei `zoneinfo` (z. B. Vilnius −1:00); nur Winamac 2007 (nur Quelle `tzdata`) spricht gegen dateutil. Vor einem upstream-Bericht klären: nur den dateutil-Fall berichten, nicht die zoneinfo-Fälle.

Zyklus 4: #377 und #378 sind gemergt (Merge-Zug grün mit dem neuen Vertrag, L1 bestätigt). Frei: #379, #381, #387, #388, #389; keine aktiven Agenten. Abgabe 440 (#386, P-8, eigene Person) lief auf Basis `c12d244`, also mit dem alten Vertrag: Pipeline-Bericht rot auch ohne Beitrag, der Test lief nie. Lokal auf `master` mit `.venv` grün (TZ=America/New_York und UTC, je 200 Beispiele × 2 Separatoren). Eigene Abgabe: nicht annehmbar, Review-Fragen gesetzt, wartet auf Peer-Review. Funde 70 (Sandbox ohne Abhängigkeiten, alter Vertrag) und 71 (`parse` → `tzlocal` bei lokaler Zone UTC, eingefrorenes Verhalten, Offset korrekt) verworfen. Nachricht 43 (P-9, Docstring) weiter offen.

Zyklus 3: Erster Pipeline-Lauf (Abgabe 438 zu #377) war rot schon auf der Basis: `setup` installierte als Nicht-root-Nutzer nach `~/.local`, das der Test-Schritt nicht sieht (`ModuleNotFoundError: hypothesis`). Behoben in `swarvex.yaml` (L1): `.venv` im Projekt, `TZ=America/New_York` wie upstream-CI, zwei `[tzpath]`-Tests abgewählt (Debian-tzdata im Image). Lokal mit dem neuen Vertrag: Basis 5059 grün, mit Abgabe 438 5105 grün. #377 (Abgabe 438) und #378 (Abgabe 439, lokal 5077 grün) angenommen; der Merge-Zug prüft sie mit dem neuen Vertrag. Nach dem Merge frei: #379, #381, #387, #388, #389. Sofort frei: #386 (P-8).

## Risiken
- Abgaben 440–444, 446 haben Pipeline-Berichte vom alten, kaputten Test-Schritt (Gegenprobe „Basis rot“). Peer-Reviewer:innen sollten das wissen; der Merge-Zug prüft sie mit `run_tests.sh` neu.
- Peer-Review hängt an Agenten anderer Personen; ohne sie stauen sich eigene Abgaben. Falls das anhält: Visionär:in fragen, ob weitere Beitragende geworben werden können.
- Abgabe 446: mit `-n auto` ~55 s für eine Datei, weil jeder Worker `transitions()` neu rechnet; Gesamtlauf lokal 86–98 s, unkritisch.
- `deadline=None` im Profil verhindert Flakiness durch langsame Sandboxes; dafür fallen Zeitprobleme nicht auf (gewollt, kein Claim betrifft Laufzeit).
- Lead-Budget 5 Mio. Tokens/Tag (nur Lead-Dienst): knappe Zyklen, Reviews vor Planung.
- Pins aus Websuche (PyPI war nicht abrufbar): hypothesis 6.170.5 (2026-10-20), tzdata 2026.6 (IANA 2026f). Gibt es eine Version nicht, schlägt `setup` fehl; dann korrigiere ich den Pin.

- GitHub Actions im Fork: `tests/test_tzpath_data.py::test_dst_matches_tzdata_zi[tzpath]` rot auf macOS (Casablanca, El_Aaiun, 2100/2400). Upstream `dateutil/dateutil` ist seit 2026-11-10 auf macOS ebenfalls rot (PR-Läufe 43319539839, 43319500377, 43247862099; Jobs 3.14 und 3.15 macos-latest), `a78cbd8` war am 2026-11-01 grün. Also Änderung der Runner-Daten (vermutlich Marokko-Änderung in tzdata 2026e/f), nicht unsere Commits. Lokal mit 2026f ist dateutil konsistent. Duplikatsuche (2026-11-15, Visionär:in): offener PR dateutil/dateutil#1667 „Fix dst() for zones that end in permanent DST“ (Maintainer, 2026-11-07), einziger Treffer für Africa/Casablanca und Africa/El_Aaiun. **Kein Bericht von uns.** Als bekannter Fall bei Z-1 in `docs/claims.md` und in Aufgabe #381 vermerkt. Der rote macOS-Job im Fork verschwindet, sobald #1667 upstream gemergt und von uns übernommen ist.

## Rulings
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
- Nachricht 44: Claims T-1 bis T-3 (`tzstr`, `tzical`) freigeben. Danach drei B-Aufgaben (siehe Plan).

## Nächste Schritte
0. Bei Freigabe von Nachricht 44: T-1, T-2, T-3 als B-Aufgaben schneiden (T-2: Funde `<…>`-Ablehnung und Übergangszeiten außerhalb 0–24 h je als eigener xfail mit Bericht; vor Bericht Duplikatsuche, z. B. upstream-Issues zu „tzstr angle brackets“).
1. Peer-Reviews der Abgaben 440–444, 446, 447, 449, 450 abwarten; Nacharbeit-Begründungen lesen. Merge-Zug-Lauf prüfen.
2. Abgaben zu #391, #394–#397 und #398/#399 reviewen (P-1 nach beiden Läufen ohne Fund: „bestätigt im getesteten Raum“ mit Laufzahlen). Nach Merge von #392: Berichtsentwurf P-6 mit Duplikatsuche und Reproduktion upstream ergänzen, dann Freigabe.
3. Nach Merge von #381: Z-1 in `docs/claims.md` auf „widerlegt für `dst()`“ setzen; Berichtsentwurf Z-1 kürzen auf den dateutil-Fall (Winamac), Duplikatsuche und Reproduktion upstream, dann Freigabe.
4. Nach den Merges: Claims-Status P-2 bis P-5, P-8, Z-2, Z-3 auf „bestätigt im getesteten Raum“ setzen.
5. Nach Merge von #393: P-7 auf „bestätigt im getesteten Raum“ (200 Beispiele), nach #396/#397 mit Laufzahlen ergänzen.
