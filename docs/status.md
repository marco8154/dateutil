# Status

Stand: 2026-11-15 (Lead-Zyklus 1)

## Lage
Projekt neu angelegt. Phase 0 (Projektinterview) läuft: Entwurf `docs/project-brief.md` steht, Runde 1 (10 Fragen) ist als Nachricht an die Visionärin / den Visionär gegangen. Noch keine Aufgaben: ohne bestätigten Brief geht keine raus (LEAD.md Regel 2).

## Fakten aus der Recherche
- Fork = upstream master `a78cbd8`; upstream hat schon `tests/property/` (isoparse, parser, tz, rrule).
- Es gibt kein `swarvex.yaml`; die lokale `.venv` enthält weder pytest noch hypothesis noch dateutil. Die Pipeline braucht also ein eigenes `setup` (Installation von `requirements-dev.txt` und dem Paket), bevor Code-Aufgaben rausgehen.
- Upstream verlangt menschliche Prüfung vor jedem Issue/PR/Kommentar und hält `parser.parse` eingefroren (`AGENTS.md`).

## Rulings
- Ruling: Projektdokumente als `.md` unter `docs/` — Sphinx liest nur `.rst`, pytest sammelt nur `test_*.py`, also stören sie den upstream-Build nicht — Kosten falls falsch: Dateien verschieben.

## Offene Freigaben
- Runde 1 des Interviews (Nachricht „Projektinterview Runde 1“).

## Nächste Schritte
1. Antworten in den Brief eintragen, ggf. Runde 2, dann Bestätigung einholen.
2. Phase 1: `swarvex.yaml` (setup, deterministisches Hypothesis-Profil), Projektabschnitt in `AGENTS.md`, `docs/claims.md`, `docs/plan.md`.
3. Erste Aufgaben (Level A/B): Claims je Modul, Orakel tz↔zoneinfo, isoparse↔fromisoformat.
