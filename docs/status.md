# Status

Stand: 2026-11-15 (Lead-Sitzung 2, Gespräch mit der Visionärin / dem Visionär)

## Lage
Runde 1 ist beantwortet und im Brief eingetragen (rrule/relativedelta als Meilenstein 3, hypothesis 6.170.5 und tzdata 2026.6 gepinnt, Lead reproduziert und sucht Duplikate vor jedem Bericht, upstream-Commits nur mit `Assisted-by`). Es fehlt nur noch die ausdrückliche Bestätigung des Briefs; danach gehen die ersten Aufgaben raus.

## Risiken
- `swarvex.yaml` ist ungeprüft: Die Lead-Umgebung hat weder Netz noch das `swarvex`-CLI, und pip findet dort keine Pakete. Der erste Pipeline-Lauf auf `master` ist die Prüfung (Plan L1).
- `deadline=None` im Profil verhindert Flakiness durch langsame Sandboxes; dafür fallen Zeitprobleme nicht auf (gewollt, kein Claim betrifft Laufzeit).
- Lead-Budget 5 Mio. Tokens/Tag (nur Lead-Dienst): knappe Zyklen, Reviews vor Planung.
- Pins aus Websuche (PyPI war nicht abrufbar): hypothesis 6.170.5 (2026-10-20), tzdata 2026.6 (IANA 2026f). Gibt es eine Version nicht, schlägt `setup` fehl; dann korrigiere ich den Pin.

## Rulings
- Ruling: Alle Commits ohne `Co-authored-by` für KI, mit `Assisted-by`, auch im Fork. Grund: upstream-`AGENTS.md` und Vorgabe Q7; Commits bleiben ohne Umschreiben einreichbar. Kosten, falls falsch: keine.
- Ruling: Projektdokumente als `.md` unter `docs/`. Grund: Sphinx liest nur `.rst`, pytest sammelt nur `test_*.py`. Kosten, falls falsch: Dateien verschieben.
- Ruling: Hypothesis-Profil als pytest-Plugin `swarvex_tools/hypothesis_profile.py` (per `-p` geladen) statt Änderung an upstream `tests/conftest.py`. Grund: Upstream-Dateien bleiben gleich. Kosten, falls falsch: Profil in conftest verschieben.
- Ruling: Gemeinsame Strategien als `tests/property/strategies_<thema>.py`. Grund: `tests/property/` hat kein `__init__.py`, Import ohne Paketumbau. Kosten, falls falsch: umbenennen.
- Ruling: SPDX `Apache-2.0 AND BSD-3-Clause` nur in neuen Dateien außerhalb von `src/` und `tests/`. Grund: upstream führt keine Header. Kosten, falls falsch: Header ergänzen.

## Offene Freigaben
- Bestätigung des Briefs (gefragt am 2026-11-15).

## Nächste Schritte
1. Nach dem Ja: L1 (Pipeline-Lauf prüfen), L2 (`docs/claims.md`), dann T1/T2 als B-Aufgaben.
2. Danach T3/T4 (Orakel), dann Meilenstein 2 (Fuzz-Ziele).
