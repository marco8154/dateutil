# Review R-1 (RFC-5545-Golden-Test)

Stand: 2026-11-27 (Lead-Zyklus 171) · Prüfer: Lead (eigenes Review, kein Peer-Review) · Basis `bcc2f7c`

## Geprüft

| Punkt | Ergebnis |
|---|---|
| Daten | 42 Einträge in `tests/property/data/rfc5545_rrule_examples_{1,2}.json`, je `id` = RRULE-Zeile in `docs/sources/rfc5545.txt`; im Zyklus 147 maschinell gegen die RFC geprüft (rrule wörtlich außer L7290 = Erratum 3883, `complete:false` genau bei offenen Listen). Kein Eintrag mit leerem `expected`, 14 mit `complete:false`. |
| Test | `tests/property/test_rrule_rfc_golden.py`: ein Fall je Eintrag, `rrulestr(regel, dtstart=…)` mit Zone aus `tz.gettz(tzid)`; vollständige Listen als Ganzes, offene als Präfix; Vergleich in Wandzeit, Zone je Termin geprüft. `test_data_files_present` sichert 2 Dateien und 42 Einträge. |
| Orakel | Erwartete Termine kommen nur aus den Daten (RFC-Text), nicht aus dateutil. |
| Lauf | lokal 43 passed (42 Beispiele + Datenprüfung), kein skip, kein xfail. |
| Frequenzen | DAILY, WEEKLY, MONTHLY, YEARLY, HOURLY, MINUTELY; alle BY-Teile der RFC-Beispiele (auch BYSETPOS, BYWEEKNO, BYYEARDAY). |

## Grenzen

- Präfix-Vergleich bei offenen Regeln: Termine nach dem letzten RFC-Termin sind nicht geprüft (die RFC nennt keine).
- `rrulestr` nur mit `dtstart`-Argument, nicht mit `DTSTART`-Zeile im Text; R-4 (Rundweg) deckt den Textweg anders ab.
- Zonen nur über `dateutil.tz.gettz`; die Zonenlogik ist Z-1, nicht R-1.

## Ergebnis

R-1 bestätigt für alle 42 RRULE-Beispiele von RFC 5545 3.8.5.3 (mit Erratum 3883). Kein Fund, kein Bericht.
