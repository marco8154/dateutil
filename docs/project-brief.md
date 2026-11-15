# Projektbrief: dateutil absichern

> Ergebnis des Projektinterviews (LEAD.md, Phase 0). Aufgaben entstehen erst, wenn die Visionärin / der Visionär ihn bestätigt.
> Stand: 2026-11-15 · Interviewrunden: 1 (beantwortet) · **bestätigt: 2026-11-15 (Stand `dbe1e9f`)**

## Entscheidungen (harte Fakten)

Zustände: **entschieden**, **Empfehlung angenommen**, **delegiert** (Lead entschied mit Grund), **offen** (nur spätere Äste, mit vorläufigem Wert), **Vorschlag** (Runde 1 gestellt, Antwort steht aus).

| ID | Entscheidung | Ergebnis | Zustand | Runde | Grund / Quelle |
|---|---|---|---|---|---|
| G1/F1 | Typ | Forschung, Art `verification` (Test und Prüfung einer Open-Source-Komponente) | entschieden | Wizard | Projektanlage |
| G2 | Kern in einem Satz | Wir prüfen mit Property-Tests, Fuzzing und Vergleichsorakeln, ob `dateutil.parser` und `dateutil.tz` halten, was sie versprechen, und melden jeden Fund mit Test upstream. | entschieden | Wizard | Vision |
| G9 | Lizenz Code / Texte | Neuer Code und Tests: Apache-2.0 **und** BSD-3-Clause (wie upstream `LICENSE`), damit Fixes upstream angenommen werden; Texte CC BY 4.0 | entschieden | 2026-11-15 | Visionär:in; ADR `docs/decisions/0001-lizenz.md` |
| G10 | Projektsprache | Deutsch für Aufgaben und Projektdokumente; Code, Testnamen und Upstream-Berichte Englisch | entschieden / Empfehlung angenommen (Upstream Englisch, Q7) | Wizard / 1 | |
| G13 | Bestehendes | Fork `marco8154/dateutil` = upstream `dateutil/dateutil` master `a78cbd8` (Release-Vorbereitung 4.0.0, 2026-11-01). Upstream hat bereits `tests/property/` (4 Dateien, ~290 Zeilen Hypothesis) | Fakt | – | `git ls-remote`, 2026-11-15 |
| F2 | Quelle, gepinnt | upstream `a78cbd8`; Module `parser` (`parse`, `isoparse`) und `tz`; Updates von upstream als eigene Aufgabe | Empfehlung angenommen | 1 | Q1 |
| F2b | Schwerpunkt | Funde in `isoparse` und `tz`; bei `parse()` nur Vertragsfragen (wirft nur `ParserError`/`OverflowError`, liest `isoformat()`-Ausgaben korrekt) | Empfehlung angenommen (M1, M2) | 1 | Q2 |
| F2c | Teststruktur | `tests/property/` nach upstream-Konvention; Projektdokumente als `.md` unter `docs/` | Empfehlung angenommen | 1 | Q3 |
| F3 | Ansprüche (Claims) | Register `docs/claims.md`, Entwurf durch Lead nach Bestätigung, einmal abgezeichnet durch Visionär:in | Empfehlung angenommen | 1 | Q10 |
| F4 | Werkzeuge | CPython 3.13, pytest, hypothesis, freezegun (aus `requirements-dev.txt`); Orakel aus der Standardbibliothek; keine neuen Abhängigkeiten ohne Freigabe. `hypothesis` und `tzdata` fest gepinnt (`swarvex_tools/constraints.txt`) | entschieden | 1 | Q5 |
| F4b | Gleiche Zeitzonendaten | Beim Vergleich `dateutil.tz` ↔ `zoneinfo` lesen beide dieselben Daten: Fixture `tz_source` aus `tests/conftest.py` (beide teilen `TZPATH`; Quelle `tzdata` = gepinntes Paket) | entschieden | 1 | Q5 |
| F5 | Rechenzeit | Pipeline < 10 min, deterministisch; lange Fuzz-Läufe als `simulation`-Aufgaben auf Rechnern der Beitragenden, Seed und Befund eingecheckt, Zweitlauf bestätigt | Empfehlung angenommen | 1 | Q6 |
| F10 | Umgebung | `swarvex.yaml`: `SETUPTOOLS_SCM_PRETEND_VERSION=4.0.0` (hatch-vcs findet im Sandbox-Klon keine Version), Installation im `setup`, Tests offline mit festem Hypothesis-Profil (`swarvex_tools/hypothesis_profile.py`) | entschieden | 2026-11-15 | Visionär:in |
| F11 | Reihenfolge | Zuerst Hypothesis-Grundgerüst für `parser` und `tz`, danach Fuzz-Ziele | entschieden | 2026-11-15 | Visionär:in |
| F12 | Token-Budget | 5 Mio. Tokens/Tag nur für den Lead-Dienst; der Runner der Visionärin / des Visionärs zählt nicht dazu | entschieden | 2026-11-15 | Visionär:in; Folge: Lead-Zyklen knapp, Reviews vor Planung |
| F6 | Daten | nur tzdata (gemeinfrei) aus dem Paket `tzdata` bzw. `/usr/share/zoneinfo`; keine personenbezogenen Daten | delegiert | – | nichts zu entscheiden |
| F7 | Upstream-Kontakt | Berichte als Entwurf in `docs/reports/` (Englisch, nach upstream `CONTRIBUTING.md`); Versand nur durch die Visionärin / den Visionär, höchstens 2 offene Berichte. Vor dem Einreichen: Lead reproduziert den Fund auf dem aktuellen upstream-master und macht die Duplikatsuche (Issues und PRs, auch geschlossene; Sandboxes der Beitragenden haben kein Netz). Commits für upstream: kein `Co-authored-by` für KI, nur `Assisted-by:` | entschieden | 1 | Q7 |
| F7b | Umgang mit Funden | Test mit `@pytest.mark.xfail(strict=True, reason=<Bericht>)` bis upstream fixt; Fix erst nach Zustimmung der Maintainer im Issue | Empfehlung angenommen | 1 | Q8 |
| F8 | Ethik / Dual Use | keine Risiken (Testcode für eine Datumsbibliothek) | delegiert | – | |
| G6 | Erfolgskriterien | siehe unten; „CI“ = swarvex-Pipeline und GitHub Actions des Forks (schaltet Visionär:in ein); Übernahme durch upstream erhofft, kein Kriterium | Empfehlung angenommen | 1 | Q4 |
| G4/G5 | Säulen / Nicht-Ziele | siehe unten; `rrule` (Maßstab RFC 5545) und `relativedelta` sind ein späterer Meilenstein, kein Nicht-Ziel | entschieden | 1 | Q2/Q9 |
| G20 | Rolle der Visionärin / des Visionärs | zeichnet ab: Claims-Register (einmal), jeden Upstream-Bericht vor dem Versand, Releases; alles andere entscheidet der Lead und protokolliert es | Empfehlung angenommen | 1 | Q10 |
| F9 | Veröffentlichung | Upstream-Issues/PRs; `CITATION.cff` später | offen, vorläufig: keine eigene Veröffentlichung außer Fork und Berichten | – | späterer Ast |

## In einem Satz
Wir prüfen mit Property-Tests, Fuzzing und Vergleichsorakeln, ob `dateutil.parser` und `dateutil.tz` halten, was sie versprechen, und jeder Fund wird ein Test und ein Bericht an die Maintainer.

## Rahmen
| | |
|---|---|
| Typ | Forschung / Verifikation einer Bibliothek |
| Quelle | `dateutil/dateutil` @ `a78cbd8` |
| Stack | Python 3.13 (Pipeline), pytest, hypothesis |
| Lizenz | Apache-2.0 und BSD-3-Clause (Code), CC BY 4.0 (Texte) |
| Sprache | Projekt Deutsch; Code und Upstream-Texte Englisch |

## Säulen
1. **Maschine entscheidet:** jeder Claim ist ein Test, der grün oder rot ist; keine Meinungsfragen.
2. **Upstream-tauglich:** Tests folgen den Konventionen von upstream (`tests/property/`, `AGENTS.md`, `CONTRIBUTING.md`), damit ein Fund ohne Umbau als PR taugt.
3. **Deterministisch:** feste Hypothesis-Profile in der Pipeline; jeder Fund hat ein festes `@example`.
4. **Rücksicht auf Maintainer:** wenige, knappe, geprüfte Berichte; nie ein Duplikat, nie automatisch gepostet.
5. **Nicht mehr behaupten als gezeigt:** ein Test zeigt eine Eigenschaft für den getesteten Bereich, nicht Korrektheit.

## Nicht-Ziele
- Kein Umbau oder Refactoring von dateutil; Fixes nur, wenn Maintainer sie wollen.
- Keine Verhaltensänderung an `parser.parse` (upstream eingefroren), außer bei klar spezifiziertem Vertrag.
- `easter` und `tzwin` sind nicht im Umfang. (`rrule` und `relativedelta`: späterer Meilenstein, siehe unten.)
- Kein eigenes Paket, kein Fork-Release auf PyPI.
- Keine Fuzzer mit nativer Kompilierung (z. B. Atheris) in der Pipeline.

## Meilensteine
1. Hypothesis-Grundgerüst für `parser` und `tz`, zwei Vergleichsorakel.
2. Fuzz-Ziele (Hypothesis) für `parse`, `isoparse`, `tzstr`/`tzical`.
3. Später: `rrule` gegen RFC 5545 und `relativedelta` (eigenes kleines Interview vor dem Start).

## Erfolgskriterien Version 1 (Meilensteine 1 und 2)
- [ ] `docs/claims.md` mit mindestens 10 Claims zu `isoparse`, `parse` und `tz`, jeder mit Testpfad.
- [ ] Alle Claims laufen als Property-Tests in der swarvex-Pipeline und in GitHub Actions des Forks, deterministisch.
- [ ] Zwei Vergleichsorakel: `dateutil.tz` gegen `zoneinfo` (gleiche tzdata), `isoparse` gegen `datetime.fromisoformat`.
- [ ] Jeder Fund hat einen Test (xfail strict bis zum Fix) und einen Berichtsentwurf in `docs/reports/`; mindestens ein Bericht ist upstream eingereicht.

## Ressourcen
- Schwarm: erwartet 1–5 Agenten; keine Assets, kein Spendenbudget nötig.
- Lead: 5 Mio. Tokens/Tag.

## Bestehendes und Unantastbares
- Upstream-Code unter `src/` wird in Aufgaben nur für Fixes zu bestätigten Funden geändert.
- Upstream-`AGENTS.md`, `CONTRIBUTING.md`, CI-Workflows bleiben inhaltlich upstream-gleich (Projektregeln kommen als eigener Abschnitt dazu).
