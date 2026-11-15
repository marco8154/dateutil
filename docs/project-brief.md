# Projektbrief: dateutil absichern

> Ergebnis des Projektinterviews (LEAD.md, Phase 0). Aufgaben entstehen erst, wenn die Visionärin / der Visionär ihn bestätigt.
> Stand: 2026-11-15 · Interviewrunden: 1 (gestellt, Antwort offen) · bestätigt: **noch nicht**

## Entscheidungen (harte Fakten)

Zustände: **entschieden**, **Empfehlung angenommen**, **delegiert** (Lead entschied mit Grund), **offen** (nur spätere Äste, mit vorläufigem Wert), **Vorschlag** (Runde 1 gestellt, Antwort steht aus).

| ID | Entscheidung | Ergebnis | Zustand | Runde | Grund / Quelle |
|---|---|---|---|---|---|
| G1/F1 | Typ | Forschung, Art `verification` (Test und Prüfung einer Open-Source-Komponente) | entschieden | Wizard | Projektanlage |
| G2 | Kern in einem Satz | Wir prüfen mit Property-Tests, Fuzzing und Vergleichsorakeln, ob `dateutil.parser` und `dateutil.tz` halten, was sie versprechen, und melden jeden Fund mit Test upstream. | entschieden | Wizard | Vision |
| G9 | Lizenz Code / Texte | Apache-2.0 / CC BY 4.0 | entschieden | Wizard | passt zu upstream (Beiträge seit 2017-12-01 unter Apache-2.0, `LICENSE`) |
| G10 | Projektsprache | Deutsch für Aufgaben und Projektdokumente; Code, Testnamen und Upstream-Berichte Englisch | entschieden / Vorschlag (Upstream Englisch) | Wizard / 1 | |
| G13 | Bestehendes | Fork `marco8154/dateutil` = upstream `dateutil/dateutil` master `a78cbd8` (Release-Vorbereitung 4.0.0, 2026-11-01). Upstream hat bereits `tests/property/` (4 Dateien, ~290 Zeilen Hypothesis) | Fakt | – | `git ls-remote`, 2026-11-15 |
| F2 | Quelle, gepinnt | upstream `a78cbd8`; Module `parser` (`parse`, `isoparse`) und `tz` | Vorschlag | 1 | Q1 |
| F3 | Ansprüche (Claims) | Register `docs/claims.md`, Entwurf durch Lead nach Bestätigung | Vorschlag | 1 | Q2 |
| F4 | Werkzeuge | CPython 3.13, pytest, hypothesis, freezegun (aus `requirements-dev.txt`); keine neuen Abhängigkeiten ohne Freigabe | Vorschlag | 1 | Q5 |
| F5 | Rechenzeit | Pipeline < 10 min, deterministisch; lange Fuzz-Läufe als `simulation`-Aufgaben auf Rechnern der Beitragenden | Vorschlag | 1 | Q6 |
| F6 | Daten | nur tzdata (gemeinfrei) aus dem Paket `tzdata` bzw. `/usr/share/zoneinfo`; keine personenbezogenen Daten | delegiert | – | nichts zu entscheiden |
| F7 | Upstream-Kontakt | Berichte als Entwurf im Repo, Versand nur durch einen Menschen | Vorschlag | 1 | Q7; upstream `AGENTS.md` verlangt menschliche Prüfung |
| F8 | Ethik / Dual Use | keine Risiken (Testcode für eine Datumsbibliothek) | delegiert | – | |
| G6 | Erfolgskriterien | siehe unten | Vorschlag | 1 | Q4 |
| G4/G5 | Säulen / Nicht-Ziele | siehe unten | Vorschlag | 1 | Q9 |
| G20 | Rolle der Visionärin / des Visionärs | zeichnet ab: Claims-Register, jeden Upstream-Bericht, Releases | Vorschlag | 1 | Q10 |
| F9 | Veröffentlichung | Upstream-Issues/PRs; `CITATION.cff` später | offen, vorläufig: keine eigene Veröffentlichung außer Fork und Berichten | – | späterer Ast |

## In einem Satz
Wir prüfen mit Property-Tests, Fuzzing und Vergleichsorakeln, ob `dateutil.parser` und `dateutil.tz` halten, was sie versprechen, und jeder Fund wird ein Test und ein Bericht an die Maintainer.

## Rahmen
| | |
|---|---|
| Typ | Forschung / Verifikation einer Bibliothek |
| Quelle | `dateutil/dateutil` @ `a78cbd8` |
| Stack | Python 3.13 (Pipeline), pytest, hypothesis |
| Lizenz | Apache-2.0 (Code), CC BY 4.0 (Texte) |
| Sprache | Projekt Deutsch; Code und Upstream-Texte Englisch |

## Säulen (Vorschlag)
1. **Maschine entscheidet:** jeder Claim ist ein Test, der grün oder rot ist; keine Meinungsfragen.
2. **Upstream-tauglich:** Tests folgen den Konventionen von upstream (`tests/property/`, `AGENTS.md`, `CONTRIBUTING.md`), damit ein Fund ohne Umbau als PR taugt.
3. **Deterministisch:** feste Hypothesis-Profile in der Pipeline; jeder Fund hat ein festes `@example`.
4. **Rücksicht auf Maintainer:** wenige, knappe, geprüfte Berichte; nie ein Duplikat, nie automatisch gepostet.
5. **Nicht mehr behaupten als gezeigt:** ein Test zeigt eine Eigenschaft für den getesteten Bereich, nicht Korrektheit.

## Nicht-Ziele (Vorschlag)
- Kein Umbau oder Refactoring von dateutil; Fixes nur, wenn Maintainer sie wollen.
- Keine Verhaltensänderung an `parser.parse` (upstream eingefroren), außer bei klar spezifiziertem Vertrag.
- `rrule`, `relativedelta`, `easter`, `tzwin` sind nicht im Umfang.
- Kein eigenes Paket, kein Fork-Release auf PyPI.
- Keine Fuzzer mit nativer Kompilierung (z. B. Atheris) in der Pipeline.

## Erfolgskriterien Version 1 (Vorschlag)
- [ ] `docs/claims.md` mit mindestens 10 Claims zu `isoparse`, `parse` und `tz`, jeder mit Testpfad.
- [ ] Alle Claims laufen als Property-Tests in der swarvex-Pipeline und in GitHub Actions des Forks, deterministisch.
- [ ] Mindestens ein Vergleichsorakel: `dateutil.tz` gegen `zoneinfo`, `isoparse` gegen `datetime.fromisoformat`.
- [ ] Jeder Fund hat einen Test (xfail strict bis zum Fix) und einen Berichtsentwurf in `docs/reports/`; mindestens ein Bericht ist upstream eingereicht.

## Ressourcen
- Schwarm: erwartet 1–5 Agenten; keine Assets, kein Spendenbudget nötig.

## Bestehendes und Unantastbares
- Upstream-Code unter `src/` wird in Aufgaben nur für Fixes zu bestätigten Funden geändert.
- Upstream-`AGENTS.md`, `CONTRIBUTING.md`, CI-Workflows bleiben inhaltlich upstream-gleich (Projektregeln kommen als eigener Abschnitt dazu).
