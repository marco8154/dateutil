# Nicht im Umfang

Bewusst nicht gemacht, mit Grund, damit es niemand erneut vorschlägt. „Später“ heißt: kann als eigener Meilenstein wiederkommen, nur mit Freigabe der Visionärin / des Visionärs.

| Was | Status | Grund | Entschieden |
|---|---|---|---|
| R-7-Referenz mit `BYSETPOS` | später | Die Brute-Force-Referenz irrt hier am ehesten; erst den Kern (Expand/Limit) prüfen | Nachricht 72 Q2, 2026-11-24 |
| R-7-Referenz mit `BYWEEKNO` | später | wie `BYSETPOS`: ISO-Wochenzählung mit `WKST` ist fehleranfällig in der Referenz | Nachricht 72 Q2, 2026-11-24 |
| R-7-Referenz mit `BYYEARDAY`, `BYEASTER`, HOURLY/MINUTELY/SECONDLY, Zeitzonen | später | `rrule_kwargs()` erzeugt `BYYEARDAY`/`BYEASTER` nicht; M4 ist auf kleine naive Regeln DAILY bis YEARLY begrenzt (Ruling Zyklus 145) | Lead, 2026-11-24 |
| Upstream-Bericht D-2 (`(dt + rd) - rd`) | nicht | kein Fehler in dateutil, die Erwartung war zu weit (Nachricht 66) | Lead-Empfehlung, 2026-11-18 |
| Upstream-Bericht R-4 (`str(rrule)` verliert die Zone) | nicht | upstream bekannt: #348, #637, #806/#1631; ein Kommentar auf #637 nur auf ausdrückliche Anweisung | Nachricht 72 Q1, 2026-11-24 |
