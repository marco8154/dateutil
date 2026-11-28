# Nicht im Umfang

Bewusst nicht gemacht, mit Grund, damit es niemand erneut vorschlägt. „Später“ heißt: kann als eigener Meilenstein wiederkommen, nur mit Freigabe der Visionärin / des Visionärs.

| Was | Status | Grund | Entschieden |
|---|---|---|---|
| R-7-Referenz mit `BYSETPOS` | jetzt M5 (Claim R-8) | war „später“ (Nachricht 72 Q2); freigegeben als M5 | Nachricht 129, 2026-11-28 |
| R-7-Referenz mit `BYWEEKNO` | später | wie `BYSETPOS`: ISO-Wochenzählung mit `WKST` ist fehleranfällig in der Referenz | Nachricht 72 Q2, 2026-11-24 |
| R-7-Referenz mit `BYYEARDAY`, `BYEASTER`, HOURLY/MINUTELY/SECONDLY, Zeitzonen | später | `rrule_kwargs()` erzeugt `BYYEARDAY`/`BYEASTER` nicht; M4 ist auf kleine naive Regeln DAILY bis YEARLY begrenzt (Ruling Zyklus 145) | Lead, 2026-11-24 |
| Upstream-Bericht D-2 (`(dt + rd) - rd`) | nicht | kein Fehler in dateutil, die Erwartung war zu weit (Nachricht 66) | Lead-Empfehlung, 2026-11-18 |
| Upstream-Bericht R-4 (`str(rrule)` verliert die Zone) | nicht | upstream bekannt: #348, #637, #806/#1631; ein Kommentar auf #637 nur auf ausdrückliche Anweisung | Nachricht 72 Q1, 2026-11-24 |
| Upstream-Bericht R-7 (gemischte `BYDAY`-Liste liefert Schnittmenge) | nicht | upstream bekannt: #1588 (offen), PR #1589 (offen), PR #1610 (geschlossen); strict-xfail meldet einen Merge von #1589 als XPASS | Nachricht 123, 2026-11-28 |
