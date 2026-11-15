# Status

Stand: 2026-11-15 (Lead-Sitzung 2, im Gespräch mit der Visionärin / dem Visionär)

## Lage
Vorgaben zu Lizenz, Umgebung, Reihenfolge und Budget sind im Brief eingetragen. Grundlage gelegt: `swarvex.yaml`, festes Hypothesis-Profil, Projektabschnitt in `AGENTS.md`, `docs/plan.md`. Q1–Q10 aus Runde 1 sind noch offen; ohne Bestätigung des Briefs gehen keine Aufgaben raus.

## Risiken
- `swarvex.yaml` ist ungeprüft: Die Lead-Umgebung hat weder Netz noch das `swarvex`-CLI, und pip findet dort keine Pakete. Der erste Pipeline-Lauf auf `master` ist die Prüfung (Plan L1).
- `deadline=None` im Profil verhindert Flakiness durch langsame Sandboxes; dafür fallen Zeitprobleme nicht auf (gewollt, kein Claim betrifft Laufzeit).
- Token-Budget 5 Mio./Tag, geteilt mit dem Lead-Runner: wenige offene Aufgaben, knappe Zyklen.

## Rulings
- Ruling: Projektdokumente als `.md` unter `docs/`. Grund: Sphinx liest nur `.rst`, pytest sammelt nur `test_*.py`. Kosten, falls falsch: Dateien verschieben.
- Ruling: Hypothesis-Profil als pytest-Plugin `swarvex_tools/hypothesis_profile.py` (per `-p` geladen) statt Änderung an upstream `tests/conftest.py`. Grund: Upstream-Dateien bleiben gleich. Kosten, falls falsch: Profil in conftest verschieben.
- Ruling: Gemeinsame Strategien als `tests/property/strategies_<thema>.py`. Grund: `tests/property/` hat kein `__init__.py`, Import ohne Paketumbau. Kosten, falls falsch: umbenennen.
- Ruling: SPDX `Apache-2.0 AND BSD-3-Clause` nur in neuen Dateien außerhalb von `src/` und `tests/`. Grund: upstream führt keine Header. Kosten, falls falsch: Header ergänzen.

## Offene Freigaben
- Q1–Q10 (Nachricht 40) und danach die Bestätigung des Briefs.

## Nächste Schritte
1. Nach dem Ja: L1 (Pipeline-Lauf prüfen), L2 (`docs/claims.md`), dann T1/T2 als B-Aufgaben.
2. Danach T3/T4 (Orakel), dann Meilenstein 2 (Fuzz-Ziele).
