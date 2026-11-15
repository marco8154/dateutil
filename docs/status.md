# Status

Stand: 2026-11-15 (Lead-Sitzung 2, Gespräch mit der Visionärin / dem Visionär)

## Lage
Brief bestätigt (`dbe1e9f`). Claims-Register als Entwurf (`docs/claims.md`, 11 Claims), Abzeichnung angefragt (Nachricht 41). Aufgaben: #377/#378 (Strategien, frei, sobald die Plattform main gelesen hat), #379/#381 (Orakel, warten auf #377/#378 und die Abzeichnung #376; #380 durch #381 ersetzt, mit bekanntem Fall #1667).

## Risiken
- `swarvex.yaml` ist ungeprüft: Die Lead-Umgebung hat weder Netz noch das `swarvex`-CLI. Die erste Abgabe (#377 oder #378) ist der erste Pipeline-Lauf; bei rotem `setup` liegt der Fehler bei mir (L1), nicht bei der Abgabe.
- `deadline=None` im Profil verhindert Flakiness durch langsame Sandboxes; dafür fallen Zeitprobleme nicht auf (gewollt, kein Claim betrifft Laufzeit).
- Lead-Budget 5 Mio. Tokens/Tag (nur Lead-Dienst): knappe Zyklen, Reviews vor Planung.
- Pins aus Websuche (PyPI war nicht abrufbar): hypothesis 6.170.5 (2026-10-20), tzdata 2026.6 (IANA 2026f). Gibt es eine Version nicht, schlägt `setup` fehl; dann korrigiere ich den Pin.

- GitHub Actions im Fork: `tests/test_tzpath_data.py::test_dst_matches_tzdata_zi[tzpath]` rot auf macOS (Casablanca, El_Aaiun, 2100/2400). Upstream `dateutil/dateutil` ist seit 2026-11-10 auf macOS ebenfalls rot (PR-Läufe 43319539839, 43319500377, 43247862099; Jobs 3.14 und 3.15 macos-latest), `a78cbd8` war am 2026-11-01 grün. Also Änderung der Runner-Daten (vermutlich Marokko-Änderung in tzdata 2026e/f), nicht unsere Commits. Lokal mit 2026f ist dateutil konsistent. Duplikatsuche (2026-11-15, Visionär:in): offener PR dateutil/dateutil#1667 „Fix dst() for zones that end in permanent DST“ (Maintainer, 2026-11-07), einziger Treffer für Africa/Casablanca und Africa/El_Aaiun. **Kein Bericht von uns.** Als bekannter Fall bei Z-1 in `docs/claims.md` und in Aufgabe #381 vermerkt. Der rote macOS-Job im Fork verschwindet, sobald #1667 upstream gemergt und von uns übernommen ist.

## Rulings
- Ruling: B-Aufgaben mit `min_trust` 0 statt 1. Grund: bisher nur eine beitragende Person mit Stufe 0; sonst nimmt niemand die Aufgaben. Kosten, falls falsch: mehr Nacharbeit, die Pipeline prüft trotzdem.
- Ruling: Strategien importieren kein dateutil, erwartete Werte nur mit `datetime.timezone`/`zoneinfo`. Grund: sonst prüft das Orakel dateutil gegen sich selbst. Kosten, falls falsch: keine.
- Ruling: Alle Commits ohne `Co-authored-by` für KI, mit `Assisted-by`, auch im Fork. Grund: upstream-`AGENTS.md` und Vorgabe Q7; Commits bleiben ohne Umschreiben einreichbar. Kosten, falls falsch: keine.
- Ruling: Projektdokumente als `.md` unter `docs/`. Grund: Sphinx liest nur `.rst`, pytest sammelt nur `test_*.py`. Kosten, falls falsch: Dateien verschieben.
- Ruling: Hypothesis-Profil als pytest-Plugin `swarvex_tools/hypothesis_profile.py` (per `-p` geladen) statt Änderung an upstream `tests/conftest.py`. Grund: Upstream-Dateien bleiben gleich. Kosten, falls falsch: Profil in conftest verschieben.
- Ruling: Gemeinsame Strategien als `tests/property/strategies_<thema>.py`. Grund: `tests/property/` hat kein `__init__.py`, Import ohne Paketumbau. Kosten, falls falsch: umbenennen.
- Ruling: SPDX `Apache-2.0 AND BSD-3-Clause` nur in neuen Dateien außerhalb von `src/` und `tests/`. Grund: upstream führt keine Header. Kosten, falls falsch: Header ergänzen.

## Offene Freigaben
- Abzeichnung `docs/claims.md` (Nachricht 41; Z-1 auf Wunsch zu „Erwartung“ geändert, Z-3 bleibt Vertrag) → danach #376 mit `complete_own_task` schließen.

## Nächste Schritte
1. Erste Abgabe: Pipeline-Bericht prüfen (L1), dann Review.
2. Nach Abzeichnung: #376 schließen; P-3, P-4, P-8, Z-3 als B-Aufgaben schneiden.
3. Vor Meilenstein 2: Fuzz-Claims ergänzen.
