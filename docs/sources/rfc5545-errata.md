# RFC 5545 errata

Source: https://www.rfc-editor.org/errata/rfc5545 (machine-readable: https://www.rfc-editor.org/errata.json), fetched 2026-11-24.
All 39 errata for RFC 5545, sorted by section, with their status. Only **Verified** errata change the normative text; *Held for Document Update* errata are acknowledged but not applied; *Rejected* and *Reported* errata do not change the RFC. Texts are copied verbatim from the RFC Editor errata database.

Relevant to `rrule` (sections 3.3.5, 3.3.10, 3.8.2.4, 3.8.5.x): 1913 (3.3.10, Verified), 3405 (3.3.10., Rejected), 3747 (3.3.10, Verified), 3779 (3.3.10, Verified), 4271 (3.3.10, Verified), 4414 (3.3.10, Verified), 5215 (3.8.5.1, Rejected), 6316 (3.8.5.1, Reported), 2527 (3.8.5.2, Verified), 3883 (3.8.5.3, Verified), 5872 (3.8.5.3, Rejected), 5920 (3.8.5.3, Rejected), 6212 (3.8.5.3, Rejected)

| ID | Section | Status | Type |
|---|---|---|---|
| [1911](https://www.rfc-editor.org/errata/eid1911) | 2.1 | Verified | Technical |
| [2497](https://www.rfc-editor.org/errata/eid2497) | 2.1 (pg 7) | Verified | Editorial |
| [5602](https://www.rfc-editor.org/errata/eid5602) | 3.1.3 | Verified | Editorial |
| [3457](https://www.rfc-editor.org/errata/eid3457) | 3.2 | Rejected | Editorial |
| [2495](https://www.rfc-editor.org/errata/eid2495) | 3.2.7 | Held for Document Update | Editorial |
| [5505](https://www.rfc-editor.org/errata/eid5505) | 3.2.19 | Held for Document Update | Technical |
| [7332](https://www.rfc-editor.org/errata/eid7332) | 3.3.9 | Verified | Editorial |
| [1913](https://www.rfc-editor.org/errata/eid1913) | 3.3.10 | Verified | Technical |
| [3405](https://www.rfc-editor.org/errata/eid3405) | 3.3.10. | Rejected | Technical |
| [3747](https://www.rfc-editor.org/errata/eid3747) | 3.3.10 | Verified | Editorial |
| [3779](https://www.rfc-editor.org/errata/eid3779) | 3.3.10 | Verified | Technical |
| [4271](https://www.rfc-editor.org/errata/eid4271) | 3.3.10 | Verified | Technical |
| [4414](https://www.rfc-editor.org/errata/eid4414) | 3.3.10 | Verified | Editorial |
| [2676](https://www.rfc-editor.org/errata/eid2676) | 3.6.1 | Rejected | Technical |
| [6109](https://www.rfc-editor.org/errata/eid6109) | 3.6.1 | Verified | Technical |
| [1916](https://www.rfc-editor.org/errata/eid1916) | 3.6.4 | Verified | Technical |
| [5214](https://www.rfc-editor.org/errata/eid5214) | 3.6.5 | Rejected | Technical |
| [8398](https://www.rfc-editor.org/errata/eid8398) | 3.6.5 | Reported | Technical |
| [2677](https://www.rfc-editor.org/errata/eid2677) | 3.8.1.10 | Verified | Technical |
| [2516](https://www.rfc-editor.org/errata/eid2516) | 3.8.4.1 | Verified | Editorial |
| [7691](https://www.rfc-editor.org/errata/eid7691) | 3.8.4.2 | Verified | Technical |
| [5215](https://www.rfc-editor.org/errata/eid5215) | 3.8.5.1 | Rejected | Technical |
| [6316](https://www.rfc-editor.org/errata/eid6316) | 3.8.5.1 | Reported | Technical |
| [2527](https://www.rfc-editor.org/errata/eid2527) | 3.8.5.2 | Verified | Editorial |
| [3883](https://www.rfc-editor.org/errata/eid3883) | 3.8.5.3 | Verified | Technical |
| [5872](https://www.rfc-editor.org/errata/eid5872) | 3.8.5.3 | Rejected | Technical |
| [5920](https://www.rfc-editor.org/errata/eid5920) | 3.8.5.3 | Rejected | Technical |
| [6212](https://www.rfc-editor.org/errata/eid6212) | 3.8.5.3 | Rejected | Technical |
| [3038](https://www.rfc-editor.org/errata/eid3038) | 3.8.7.2 | Held for Document Update | Technical |
| [5082](https://www.rfc-editor.org/errata/eid5082) | 3.8.7.3 | Rejected | Technical |
| [4606](https://www.rfc-editor.org/errata/eid4606) | 3.8.8.3 | Rejected | Technical |
| [7945](https://www.rfc-editor.org/errata/eid7945) | 3.8.8.3 | Verified | Technical |
| [2039](https://www.rfc-editor.org/errata/eid2039) | 4 | Verified | Technical |
| [3740](https://www.rfc-editor.org/errata/eid3740) | 4 | Verified | Technical |
| [4149](https://www.rfc-editor.org/errata/eid4149) | 4 | Verified | Technical |
| [4150](https://www.rfc-editor.org/errata/eid4150) | 10.2 | Rejected | Editorial |
| [4626](https://www.rfc-editor.org/errata/eid4626) | A.1 | Held for Document Update | Editorial |
| [2038](https://www.rfc-editor.org/errata/eid2038) | Appendix A | Verified | Editorial |
| [5794](https://www.rfc-editor.org/errata/eid5794) | ToC | Verified | Editorial |

## Erratum 1911: section 2.1 (Verified, Technical)

**Original text:**

```text
| DQUOTE                 | 22                |
```

**Corrected text:**

```text
| DQUOTE                 | 34                |
```

**Notes:**

```text
The codepoint for the DQUOTE character was erroneously specified in hexadecimal instead of decimal.  Issue was found by Raimund Nisius.
```

## Erratum 2497: section 2.1 (pg 7) (Verified, Editorial)

**Original text:**

```text
+------------------------+-------------------+
              | Character name         | Decimal codepoint |
              +------------------------+-------------------+
              | HTAB                   | 9                 |
              | LF                     | 10                |
              | CR                     | 13                |
-->           | DQUOTE                 | 22                |
-->           | SPACE                  | 32                |
... table continues
```

**Corrected text:**

```text
+------------------------+-------------------+
              | Character name         | Decimal codepoint |
              +------------------------+-------------------+
              | HTAB                   | 9                 |
              | LF                     | 10                |
              | CR                     | 13                |
-->           | SPACE                  | 32                |
-->           | DQUOTE                 | 34                |
                                         ^^
                                         corrected value
...table continues
```

**Notes:**

```text
Correction to Table on page 7 of RFC updating the order of ASCII-US listing (decimal codepoint descending) and incorporating errata ID 1911(2009-10-13 - DQUOTE char listing shows hexadecimal value).
```

## Erratum 5602: section 3.1.3 (Verified, Editorial)

**Original text:**

```text
ATTACH;FMTTYPE=text/plain;ENCODING=BASE64;VALUE=BINARY:VGhlIH
      F1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4
```

**Corrected text:**

```text
ATTACH;FMTTYPE=text/plain;ENCODING=BASE64;VALUE=BINARY:VGhlIH
      F1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSBsYXp5IGRvZy4=
```

**Notes:**

```text
The base64 text used in the example misses the base64 padding.  RFC 5545 appears to be using base64 according to RFC 4648 Section 4 with padding throughout, except for this example.  (The corrected text decodes to "The quick brown fox jumps over the lazy dog.")  Beyond temporary confusion in implementers, it is possible that this example will turn up in a test suite and ultimately cause unnecessarily lenient behavior of decoders ("soup"); it should be either clarified that this lenient behavior is not the intention or the behavior should be codified.
```

## Erratum 3457: section 3.2 (Rejected, Editorial)

**Original text:**

```text
Property parameter values that contain the COLON, SEMICOLON, or COMMA
character separators MUST be specified as quoted-string text values.
```

**Corrected text:**

```text
Property parameter values that contain the COLON, SEMICOLON, COMMA or
SPACE character separators MUST be specified as quoted-string text
values.
```

**Notes:**

```text
Section "3.2.2. Common Name" gives an example with an double-quoted parameter value with a SPACE in it:

       ORGANIZER;CN="John Smith":mailto:jsmith@example.com
 --VERIFIER NOTES-- 
That example also shows a double-quoted parameter value with a "J" in it, but that doesn't mean that values that contain "J" MUST be quoted.  Examples are just examples, and any value MAY be quoted.

The ABNF is the definitive source.  The ABNF at the bottom of page 10 and top of page 11 (Section 3.1) says that non-quoted values may contain any number of characters from the SAFE-CHAR set, and that set includes WSP (SP and HTAB; see RFC 5234).  Quoting is not required on account of space characters.
```

## Erratum 2495: section 3.2.7 (Held for Document Update, Editorial)

**Original text:**

```text
Description: This property parameter identifies the inline encoding
    used in a property value.  The default encoding is "8BIT",
    corresponding to a property value consisting of text.  The
    "BASE64" encoding type corresponds to a property value encoded
    using the "BASE64" encoding defined in [RFC2045].
```

**Corrected text:**

```text
Description: This property parameter identifies the inline encoding
    used in a property value.  The default encoding is "8BIT",
    corresponding to a property value consisting of text.  The
    "BASE64" encoding type corresponds to a property value encoded
    using the "BASE64" encoding defined in [RFC4648].
                                            ^^^^^^^
```

**Notes:**

```text
Section "Format Definition" above the "Description" paragraph cites [RFC2045] as defining value "8BIT" and [RFC4648] covering value "BASE64".
```

## Erratum 5505: section 3.2.19 (Held for Document Update, Technical)

**Original text:**

```text
tzidparam  = "TZID" "=" [tzidprefix] paramtext
```

**Corrected text:**

```text
tzidparam  = "TZID" "=" [tzidprefix] param-value
```

**Notes:**

```text
TZID appears to be the only parameter defined 5545 whose value can not be a quoted string.  This is problematic in that time zone IDs such as "GMT-03:00" are beginning to appear (note the embedded colon).  RFC 6868 has no mechanism to quote a colon character, as it relies on such characters appearing within a quoted string.  I see no technical reason why a TZID parameter can not be quoted, and existing implementations already accept quoted TZIDs.
```

## Erratum 7332: section 3.3.9 (Verified, Editorial)

**Original text:**

```text
The period start at 18:00:00 on January 1, 1997 and lasting 5
hours and 30 minutes would be:

19970101T180000Z/PT5H30M
```

**Corrected text:**

```text
The period start at 18:00:00 on January 1, 1997 and lasting 5
hours and 30 minutes would be:

19970101T180000/PT5H30M
```

**Notes:**

```text
I do not know if this is an editorial or technical issue.

If I understand the datetime value (Section 3.3.5) correct the last character should only be "Z" if the value is in UTC.

In the first example in section 3.3.9 UTC is explicitely mentioned but not in the second example.
```

## Erratum 1913: section 3.3.10 (Verified, Technical)

**Original text:**

```text
represents the last Monday of the month.  The numeric value in a
BYDAY rule part with the FREQ rule part set to YEARLY corresponds
to an offset within the month when the BYMONTH rule part is
present, and corresponds to an offset within the year when the
BYWEEKNO or BYMONTH rule parts are present.  If an integer
```

**Corrected text:**

```text
represents the last Monday of the month.  The numeric value in a
BYDAY rule part with the FREQ rule part set to YEARLY corresponds
to an offset within the month when the BYMONTH rule part is
present, and corresponds to an offset within the year when the
BYWEEKNO or BYMONTH rule parts are not present.  If an integer
                                   ^^^
```

**Notes:**

```text
The original statement appears contradictory in itself.
```

## Erratum 3405: section 3.3.10. (Rejected, Technical)

**Original text:**

```text
weekday     = "SU" / "MO" / "TU" / "WE" / "TH" / "FR" / "SA"
       ;Corresponding to SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY,
       ;FRIDAY, and SATURDAY days of the week.
```

**Corrected text:**

```text
weekday     = "MO" / "TU" / "WE" / "TH" / "FR" / "SA" / "SU"
       ;Corresponding to MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY,
       ;SATURDAY, and SUNDAY days of the week.
```

**Notes:**

```text
It is worldwide accepted that a working business week begins with
a monday in all business related activities (stock exchange etc. etc).

See also:
       package Ada.Calendar.Formatting is
       -- Day of the week:
       type Day_Name is (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday);
 --VERIFIER NOTES-- 
This isn't an error in the document.  Regardless of your opinion of whether the week should begin on Sunday, Monday, or Thursday, ABNF does not create any particular ordering.  Implementations are always free to order them as they please.
```

## Erratum 3747: section 3.3.10 (Verified, Editorial)

**Original text:**

```text
+----------+--------+--------+-------+-------+------+-------+------+
   |          |SECONDLY|MINUTELY|HOURLY |DAILY  |WEEKLY|MONTHLY|YEARLY|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYMONTH   |Limit   |Limit   |Limit  |Limit  |Limit |Limit  |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYWEEKNO  |N/A     |N/A     |N/A    |N/A    |N/A   |N/A    |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYYEARDAY |Limit   |Limit   |Limit  |N/A    |N/A   |N/A    |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYMONTHDAY|Limit   |Limit   |Limit  |Limit  |N/A   |Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYDAY     |Limit   |Limit   |Limit  |Limit  |Expand|Note 1 |Note 2|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYHOUR    |Limit   |Limit   |Limit  |Expand |Expand|Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYMINUTE  |Limit   |Limit   |Expand |Expand |Expand|Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYSECOND  |Limit   |Expand  |Expand |Expand |Expand|Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYSETPOS  |Limit   |Limit   |Limit  |Limit  |Limit |Limit  |Limit |
   +----------+--------+--------+-------+-------+------+-------+------+

      Note 1:  Limit if BYMONTHDAY is present; otherwise, special expand
               for MONTHLY.

      Note 2:  Limit if BYYEARDAY or BYMONTHDAY is present; otherwise,
               special expand for WEEKLY if BYWEEKNO present; otherwise,
               special expand for MONTHLY if BYMONTH present; otherwise,
               special expand for YEARLY.
```

**Corrected text:**

```text
+----------+--------+--------+-------+-------+------+-------+------+
   |          |SECONDLY|MINUTELY|HOURLY |DAILY  |WEEKLY|MONTHLY|YEARLY|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYMONTH   |Limit   |Limit   |Limit  |Limit  |Limit |Limit  |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYWEEKNO  |N/A     |N/A     |N/A    |N/A    |N/A   |N/A    |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYYEARDAY |Limit   |Limit   |Limit  |N/A    |N/A   |N/A    |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYMONTHDAY|Limit   |Limit   |Limit  |Limit  |N/A   |Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYDAY     |Limit   |Limit   |Limit  |Limit  |Expand|Note 1 |Note 2|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYHOUR    |Limit   |Limit   |Limit  |Expand |Expand|Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYMINUTE  |Limit   |Limit   |Expand |Expand |Expand|Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYSECOND  |Limit   |Expand  |Expand |Expand |Expand|Expand |Expand|
   +----------+--------+--------+-------+-------+------+-------+------+
   |BYSETPOS  |Limit   |Limit   |Limit  |Limit  |Limit |Limit  |Limit |
   +----------+--------+--------+-------+-------+------+-------+------+

      Note 1:  Limit if BYMONTHDAY is present; otherwise, special expand
               for MONTHLY.

      Note 2:  Limit if BYYEARDAY or BYMONTHDAY is present; otherwise,
               special expand for YEARLY.
```

**Notes:**

```text
The change is to "Note 2":
Removed WEEKLY and MONTHLY clause as Note 2 only applies to FREQ = YEARLY.
```

## Erratum 3779: section 3.3.10 (Verified, Technical)

**Original text:**

```text
represents the last Monday of the month.  The numeric value in a
BYDAY rule part with the FREQ rule part set to YEARLY corresponds
to an offset within the month when the BYMONTH rule part is
present, and corresponds to an offset within the year when the
BYWEEKNO or BYMONTH rule parts are present.  If an integer
modifier is not present, it means all days of this type within the
specified frequency.  For example, within a MONTHLY rule, MO
represents all Mondays within the month.  The BYDAY rule part MUST
NOT be specified with a numeric value when the FREQ rule part is
not set to MONTHLY or YEARLY.  Furthermore, the BYDAY rule part
MUST NOT be specified with a numeric value with the FREQ rule part
set to YEARLY when the BYWEEKNO rule part is specified.
```

**Corrected text:**

```text
represents the last Monday of the month.  The numeric value in a
BYDAY rule part with the FREQ rule part set to YEARLY corresponds
to an offset within the month when the BYMONTH rule part is
present, and corresponds to an offset within the year when the
BYMONTH rule part is not present.  If an integer
modifier is not present, it means all days of this type within the
specified frequency.  For example, within a MONTHLY rule, MO
represents all Mondays within the month.  The BYDAY rule part MUST
NOT be specified with a numeric value when the FREQ rule part is
not set to MONTHLY or YEARLY.  Furthermore, the BYDAY rule part
MUST NOT be specified with a numeric value with the FREQ rule part
set to YEARLY when the BYWEEKNO rule part is specified.
```

**Notes:**

```text
Other than the missing 'not', pointed out in the errata 1913, the original text contradicts itself regarding BYWEEKNO.
At the beggining of the paragraph, it says that when using a YEARLY frequency with BYWEEKNO rule part, the integer part identifies an offset within the year (i.e. either in [-53, 0) or (0, 53], as it can be a week day in a valid week of the year, even if it is not clearly specified), but at the end of the paragraph, it states that offsets should not be specified in conjunction with a BYWEEKNO rule part.
```

## Erratum 4271: section 3.3.10 (Verified, Technical)

**Original text:**

```text
Recurrence rules may generate recurrence instances with an invalid
date (e.g., February 30) or nonexistent local time (e.g., 1:30 AM
on a day where the local time is moved forward by an hour at 1:00
AM).  Such recurrence instances MUST be ignored and MUST NOT be
counted as part of the recurrence set.
```

**Corrected text:**

```text
Recurrence rules may generate recurrence instances with an invalid
date (e.g., February 30). Such recurrence instances MUST be ignored
and MUST NOT be counted as part of the recurrence set.

Recurrence rules may generate recurrence instances with a nonexistent
local time ((e.g., 1:30 AM on a day where the local time is moved
forward by an hour at 1:00 AM).  Such recurrence instances are
handled as specified in Section 3.3.5.
```

**Notes:**

```text
The section about ignoring times that don't occur in the timezone of the expansion is contradicted by the later passage (p44):

"""If the computed local start time of a recurrence instance does not
exist, or occurs more than once, for the specified time zone, the
time of the recurrence instance is interpreted in the same manner
as an explicit DATE-TIME value describing that date and time, as
specified in Section 3.3.5."""

And this is the behaviour implemented by major clients such as Calendar.app and Google Calendar.
```

## Erratum 4414: section 3.3.10 (Verified, Editorial)

**Original text:**

```text
The UNTIL rule part defines a DATE or DATE-TIME value that bounds
      the recurrence rule in an inclusive manner.  If the value
      specified by UNTIL is synchronized with the specified recurrence,
      this DATE or DATE-TIME becomes the last instance of the
      recurrence.  The value of the UNTIL rule part MUST have the same
      value type as the "DTSTART" property.  Furthermore, if the
      "DTSTART" property is specified as a date with local time, then
      the UNTIL rule part MUST also be specified as a date with local
      time.  If the "DTSTART" property is specified as a date with UTC
      time or a date with local time and time zone reference, then the
      UNTIL rule part MUST be specified as a date with UTC time.  In the
      case of the "STANDARD" and "DAYLIGHT" sub-components the UNTIL
      rule part MUST always be specified as a date with UTC time.  If
      specified as a DATE-TIME value, then it MUST be specified in a UTC
      time format.  If not present, and the COUNT rule part is also not
      present, the "RRULE" is considered to repeat forever.
```

**Corrected text:**

```text
The UNTIL rule part defines a DATE or DATE-TIME value that bounds
      the recurrence rule in an inclusive manner.  If the value
      specified by UNTIL is synchronized with the specified recurrence,
      this DATE or DATE-TIME becomes the last instance of the
      recurrence.  The value of the UNTIL rule part MUST have the same
      value type as the "DTSTART" property.  Furthermore, if the
      "DTSTART" property is specified as a date with local time, then
      the UNTIL rule part MUST also be specified as a date with local
      time.  If the "DTSTART" property is specified as a date with UTC
      time or a date with local time and time zone reference, then the
      UNTIL rule part MUST be specified as a date with UTC time.  In the
      case of the "STANDARD" and "DAYLIGHT" sub-components the UNTIL
      rule part MUST always be specified as a date with UTC time.
      If not present, and the COUNT rule part is also not
      present, the "RRULE" is considered to repeat forever.
```

**Notes:**

```text
The following sentence from RFC 2445 should have been removed from the text.

      If
      specified as a DATE-TIME value, then it MUST be specified in a UTC
      time format.
```

## Erratum 2676: section 3.6.1 (Rejected, Technical)

**Original text:**

```text
; The following are OPTIONAL,
                  ; but MUST NOT occur more than once.
                  ;
                  class / created / description / geo /
                  last-mod / location / organizer / priority /
                  seq / status / summary / transp /
                  url / recurid /
                  ;
                  ; The following is OPTIONAL,
                  ; but SHOULD NOT occur more than once.
                  ;
                  rrule /
                  ;
                  ; Either 'dtend' or 'duration' MAY appear in
                  ; a 'eventprop', but 'dtend' and 'duration'
                  ; MUST NOT occur in the same 'eventprop'.
                  ;
                  dtend / duration /
                  ;
                  ; The following are OPTIONAL,
                  ; and MAY occur more than once.
                  ;
                  attach / attendee / categories / comment /
                  contact / exdate / rstatus / related /
                  resources / rdate / x-prop / iana-prop
                  ^^^^^^^^^
                  ;
```

**Corrected text:**

```text
; The following are OPTIONAL,
                  ; but MUST NOT occur more than once.
                  ;
                  class / created / description / geo /
                  last-mod / location / organizer / priority /
                  seq / status / summary / transp /
                  url / recurid / resources 
                                  ^^^^^^^^^
                  ;
                  ; The following is OPTIONAL,
                  ; but SHOULD NOT occur more than once.
                  ;
                  rrule /
                  ;
                  ; Either 'dtend' or 'duration' MAY appear in
                  ; a 'eventprop', but 'dtend' and 'duration'
                  ; MUST NOT occur in the same 'eventprop'.
                  ;
                  dtend / duration /
                  ;
                  ; The following are OPTIONAL,
                  ; and MAY occur more than once.
                  ;
                  attach / attendee / categories / comment /
                  contact / exdate / rstatus / related /
                  rdate / x-prop / iana-prop
                  ;
```

**Notes:**

```text
As per the definition of 'RESOURCES' in section 3.8.1.10,:

Conformance:  This property can be specified once in "VEVENT" or
      "VTODO" calendar component.

The text in the "VEVENT" definition has RESOURCES in the 'Option and MAY occur more than once.' section. The corrected text above corrects both sections;

1/ It is removed from the 'OPTIONAL/MAY occure more than once section.
2/ It is placed at the end of the 'OPTIONAL/MUST NOT occur more than once section.
 --VERIFIER NOTES-- 
The correct fix is listed in Erratum 2677 which was approved.
```

## Erratum 6109: section 3.6.1 (Verified, Technical)

**Original text:**

```text
The anniversary type of "VEVENT" can span more than one date (i.e., "DTEND"
property value is set to a calendar date after the "DTSTART" property value).
```

**Corrected text:**

```text
The anniversary type of "VEVENT" can span more than one date (i.e., "DTEND"
property value is set to a calendar date at least two days after the "DTSTART"
property value).
```

**Notes:**

```text
"DTEND" comes, by definition (3.8.2.2), always after "DTSTART". The span (duration) is the difference between the two.
```

## Erratum 1916: section 3.6.4 (Verified, Technical)

**Original text:**

```text
BEGIN:VFREEBUSY
  UID:19970901T115957Z-76A912@example.com
  DTSTAMP:19970901T120000Z
  ORGANIZER:jsmith@example.com
           ^
```

**Corrected text:**

```text
BEGIN:VFREEBUSY
  UID:19970901T115957Z-76A912@example.com
  DTSTAMP:19970901T120000Z
  ORGANIZER:mailto:jsmith@example.com
            ^^^^^^^
```

**Notes:**

```text
The last example in section 3.6.4 is missing "mailto:" after the "ORGANIZER:"
```

## Erratum 5214: section 3.6.5 (Rejected, Technical)

**Original text:**

```text
timezonec  = "BEGIN" ":" "VTIMEZONE" CRLF
                    *(
                    ;
                    ; 'tzid' is REQUIRED, but MUST NOT occur more
                    ; than once.
                    ;
                    tzid /
                    ;
                    ; 'last-mod' and 'tzurl' are OPTIONAL,
                    ; but MUST NOT occur more than once.
                    ;
                    last-mod / tzurl /
                    ;
                    ; One of 'standardc' or 'daylightc' MUST occur
                    ; and each MAY occur more than once.
                    ;
                    standardc / daylightc /
                    ;
                    ; The following are OPTIONAL,
                    ; and MAY occur more than once.
                    ;
                    x-prop / iana-prop
                    ;
                    )
                    "END" ":" "VTIMEZONE" CRLF
```

**Corrected text:**

```text
timezonec    = "BEGIN" ":" "VTIMEZONE" CRLF
                      timezoneprop timezonesubc
                      "END" ":" "VTIMEZONE" CRLF

       timezoneprop = *(
                      ;
                      ; 'tzid' is REQUIRED, but MUST NOT occur more
                      ; than once.
                      ;
                      tzid /
                      ;
                      ; 'last-mod' and 'tzurl' are OPTIONAL,
                      ; but MUST NOT occur more than once.
                      ;
                      last-mod / tzurl /
                      ;
                      ; The following are OPTIONAL,
                      ; and MAY occur more than once.
                      ;
                      x-prop / iana-prop
                      ;

       timezonesubc = *(
                      ;
                      ; One of 'standardc' or 'daylightc' MUST occur
                      ; and each MAY occur more than once.
                      ;
                      standardc / daylightc
                      ;
                      )
```

**Notes:**

```text
The definition of icalbody shows that calendar properties precede components. Some components may contains sub-components. For those that may:

The definition of eventc (section 3.6.1 - Event Component) also shows that properties precede sub-components.

The definition of todoc (section 3.6.2 - To-Do Component) also shows that properties precede sub-components.

However, the definition of timezonec (section 3.6.5 - Time Zone Component) shows that properties and sub-components may be intermingled. The corrected text assumes this was not intended.
 --VERIFIER NOTES-- 
The current ABNF doesn't appear to cause any interop problems, given that both ical4j and libical don't care about the order of properties and components within a VTIMEZONE component.

See https://mailarchive.ietf.org/arch/msg/calsify/x82GopunVcEh8y5UGSIsEIC3s6M/
```

## Erratum 8398: section 3.6.5 (Reported, Technical)

**Original text:**

```text
tzprop     = *(
                    ;
                    ; The following are REQUIRED,
                    ; but MUST NOT occur more than once.
                    ;
                    dtstart / tzoffsetto / tzoffsetfrom /
                    ;
                    ; The following is OPTIONAL,
                    ; but SHOULD NOT occur more than once.
                    ;
                    rrule /
                    ;
                    ; The following are OPTIONAL,
                    ; and MAY occur more than once.
                    ;
                    comment / rdate / tzname / x-prop / iana-prop
                    ;
                    )
```

**Corrected text:**

```text
tzprop     = *(
                    ;
                    ; The following are REQUIRED,
                    ; but MUST NOT occur more than once.
                    ;
                    dtstart / tzoffsetto / tzoffsetfrom /
                    ;
                    ; The following is OPTIONAL,
                    ; but SHOULD NOT occur more than once.
                    ;
                    rrule /
                    ;
                    ; The following are OPTIONAL,
                    ; and MAY occur more than once.
                    ;
                    comment / exdate / rdate / tzname / x-prop / iana-prop
                    ;
                    )
```

**Notes:**

```text
This proposal adds exdate to STANDARD and DAYLIGHT

tzprop does not include "exdate"
However, the exdate documentation states:

Conformance:  This property can be specified in recurring "VEVENT",
      "VTODO", and "VJOURNAL" calendar components as well as in the
      "STANDARD" and "DAYLIGHT" sub-components of the "VTIMEZONE"
      calendar component.
```

## Erratum 2677: section 3.8.1.10 (Verified, Technical)

**Original text:**

```text
Conformance:
This property can be specified once in "VEVENT" or "VTODO" calendar component.
                               ^^^^
```

**Corrected text:**

```text
Conformance:
This property can be specified in "VEVENT" or "VTODO" calendar component.
```

**Notes:**

```text
The word "once" was mistakenly introduced in RFC 5545.
RFC 2445 didn't have this issue.

Issues was previously reported by Dennis Gearon <gearond@sbcglobal.net>
(See Errata 2676) but proposed the wrong correction.
```

## Erratum 2516: section 3.8.4.1 (Verified, Editorial)

**Original text:**

```text
Example:  The following is an example of this property's use when
      another calendar user is acting on behalf of the "Attendee":

       ATTENDEE;SENT-BY=mailto:jan_doe@example.com;CN=John Smith:
        mailto:jsmith@example.com
```

**Corrected text:**

```text
Example:  The following is an example of this property's use when
      another calendar user is acting on behalf of the "Attendee":

       ATTENDEE;SENT-BY="mailto:jan_doe@example.com";CN=John Smith:
                        ^                          ^
        mailto:jsmith@example.com
```

**Notes:**

```text
In the specification for SENT-BY (3.2.18), the r-value MUST be explicitly bound by DQUOTEs (ABNF follows)

sentbyparam = "SENT-BY" "=" DQUOTE cal-address DQUOTE
```

## Erratum 7691: section 3.8.4.2 (Verified, Technical)

**Original text:**

```text
The following is an example of this property with an alternate
representation of an LDAP URI to a directory entry containing the
contact information:

CONTACT;ALTREP="ldap://example.com:6666/o=ABC%20Industries\,
 c=US???(cn=Jim%20Dolittle)":Jim Dolittle\, ABC Industries\,
 +1-919-555-1234
```

**Corrected text:**

```text
The following is an example of this property with an alternate
representation of an LDAP URI to a directory entry containing the
contact information:

CONTACT;ALTREP="ldap://example.com:6666/o=ABC%20Industries,
 c=US???(cn=Jim%20Dolittle)":Jim Dolittle\, ABC Industries\,
 +1-919-555-1234
```

**Notes:**

```text
Note that the original text has an escaped comma in the ALTREP parameter value at the end of the unfolded line.

The characters '\' and ',' are allowed in quoted parameter values.
This means that the URL must be parsed as
"ldap://example.com:6666/o=ABC%20Industries\,c=US???(cn=Jim%20Dolittle)"
but this is not a valid URI because of the extra backslash.

Because commas do not need to be escaped in quoted parameter values, I assume that this is an error and the comma should not have been quoted.
```

## Erratum 5215: section 3.8.5.1 (Rejected, Technical)

**Original text:**

```text
Purpose:  This property defines the list of DATE-TIME exceptions for
   recurring events, to-dos, journal entries, or time zone
   definitions.

...

   Conformance:  This property can be specified in recurring "VEVENT",
   "VTODO", and "VJOURNAL" calendar components as well as in the
   "STANDARD" and "DAYLIGHT" sub-components of the "VTIMEZONE"
   calendar component.
```

**Corrected text:**

```text
Purpose:  This property defines the list of DATE-TIME exceptions for
   recurring events, to-dos or journal entries.

...

   Conformance:  This property can be specified in recurring "VEVENT",
   "VTODO", and "VJOURNAL" calendar components.
```

**Notes:**

```text
Section 3.8.5.1 describes Exception Date-Times (EXDATE).

tzprop (section 3.6.5) does not allow EXDATE.

(Of course, the problem could be that 3.6.5 should include EXDATE.)
 --VERIFIER NOTES-- 
Excluding EXDATE from tzprop is the actual error and is worthy of a new errata.

See https://mailarchive.ietf.org/arch/msg/calsify/x82GopunVcEh8y5UGSIsEIC3s6M/
```

## Erratum 6316: section 3.8.5.1 (Reported, Technical)

**Original text:**

```text
Value Type:  The default value type for this property is DATE-TIME.
       The value type can be set to DATE.
```

**Corrected text:**

```text
Value Type:  The default value type for this property is DATE-TIME.
       The value type can be set to DATE.  This property MUST have the same
       value type as the "DTSTART" property contained within the
       recurring component.  Furthermore, this property MUST be specified
       as a date with local time if and only if the "DTSTART" property
       contained within the recurring component is specified as a date
       with local time.
```

**Notes:**

```text
EXDATE excludes a specific instance of a recurring event and therefore should have the same value type as DTSTART.  This is analogous to RECURRENCE-ID which overrides a specific instance and has the same value type as DTSTART.

I will note however that there is iCalendar data in the wild with DTSTART;VALUE=DATE-TIME and EXDATE;VALUE=DATE.  If this errata is rejected as incorrect, then a new errata should be opened with additional text describing how EXDATE;VALUE=DATE is supposed to be handled when DTSTART;VALUE=DATE-TIME.  For instance, does EXDATE;VALUE=DATE exclude ALL instances of a FREQ=HOURLY recurrence on the given day?
```

## Erratum 2527: section 3.8.5.2 (Verified, Editorial)

**Original text:**

```text
Example:  The following are examples of this property:

       RDATE:19970714T123000Z
       RDATE;TZID=America/New_York:19970714T083000

       RDATE;VALUE=PERIOD:19960403T020000Z/19960403T040000Z,
        19960404T010000Z/PT3H

       RDATE;VALUE=DATE:19970101,19970120,19970217,19970421
        19970526,19970704,19970901,19971014,19971128,19971129,19971225
```

**Corrected text:**

```text
Example:  The following are examples of this property:

       RDATE:19970714T123000Z
       RDATE;TZID=America/New_York:19970714T083000

       RDATE;VALUE=PERIOD:19960403T020000Z/19960403T040000Z,
        19960404T010000Z/PT3H

       RDATE;VALUE=DATE:19970101,19970120,19970217,19970421,
                                                           ^
        19970526,19970704,19970901,19971014,19971128,19971129,19971225
```

**Notes:**

```text
Comma missing at the fold boundary.
```

## Erratum 3883: section 3.8.5.3 (Verified, Technical)

**Original text:**

```text
Every 3 hours from 9:00 AM to 5:00 PM on a specific day:

       DTSTART;TZID=America/New_York:19970902T090000
       RRULE:FREQ=HOURLY;INTERVAL=3;UNTIL=19970902T170000Z

       ==> (September 2, 1997 EDT) 09:00,12:00,15:00
```

**Corrected text:**

```text
Every 3 hours from 9:00 AM to 5:00 PM on a specific day:

       DTSTART;TZID=America/New_York:19970902T090000
       RRULE:FREQ=HOURLY;INTERVAL=3;UNTIL=19970902T210000Z

       ==> (September 2, 1997 EDT) 09:00,12:00,15:00
```

**Notes:**

```text
The UNTIL rule part is specified with UTC time, which was four hours ahead of America/New_York on 19970902. So 170000Z would only be 1:00 PM on that day.

The corrected UNTIL rule matches the description (from 9 to 5).  Note that "UNTIL=19970902T190000Z" would have the same effect (the last event is at 3 PM in New York, which is 19:00 Z), but 21:00 Z is what matches the description.
```

## Erratum 5872: section 3.8.5.3 (Rejected, Technical)

**Original text:**

```text
Weekly on Tuesday and Thursday for five weeks:

       DTSTART;TZID=America/New_York:19970902T090000
       RRULE:FREQ=WEEKLY;UNTIL=19971007T000000Z;WKST=SU;BYDAY=TU,TH
```

**Corrected text:**

```text
Weekly on Tuesday and Thursday for five weeks:

       DTSTART;TZID=America/New_York:19970902T090000
       RRULE:FREQ=WEEKLY;UNTIL=19971002T000000Z;WKST=SU;BYDAY=TU,TH
```

**Notes:**

```text
The UNTIL rule is inclusive, and October 7, a Tuesday, should not be included.
 --VERIFIER NOTES-- 
Neil Jenkins wrote: This erratum is invalid. The original example, while slightly weird, is correct as is. The event's DTSTART time is 09:00 New York TIme, and the UNTIL time is 00:00 UTC, which is before this. Therefore you would not get a recurrence on the 7 Oct with this rule and so it would produce 10 occurrences, as specified. The "corrected text" is in fact invalid, as this would remove the 2nd Oct occurrence.
```

## Erratum 5920: section 3.8.5.3 (Rejected, Technical)

**Original text:**

```text
Every Friday the 13th, forever:

       DTSTART;TZID=America/New_York:19970902T090000
       EXDATE;TZID=America/New_York:19970902T090000
       RRULE:FREQ=MONTHLY;BYDAY=FR;BYMONTHDAY=13

       ==> (1998 9:00 AM EST) February 13;March 13;November 13
           (1999 9:00 AM EDT) August 13
           (2000 9:00 AM EDT) October 13
           ...
```

**Corrected text:**

```text
Every Friday the 13th, forever:

       DTSTART;TZID=America/New_York:19980213T090000
       RRULE:FREQ=MONTHLY;BYDAY=FR;BYMONTHDAY=13

       ==> (1998 9:00 AM EST) February 13;March 13;November 13
           (1999 9:00 AM EDT) August 13
           (2000 9:00 AM EDT) October 13
           ...
```

**Notes:**

```text
The "DTSTART" property is not synchronized with the recurrence rule.

Although it may be removed from the recurrence set by an "EXDATE" property, the description at the start of section 3.8.5.3 leaves no doubt that the "DTSTART" property should still be synchronized with the recurrence rule.
 --VERIFIER NOTES-- 
Rejected since it changes the intent of the example (showing exclusion the first instance).  The example should be something like the following (possibly to be reported in a new errata):

        DTSTART;TZID=America/New_York:19970613T090000
        EXDATE;TZID=America/New_York:19970613T090000

See https://mailarchive.ietf.org/arch/msg/calsify/x82GopunVcEh8y5UGSIsEIC3s6M/
```

## Erratum 6212: section 3.8.5.3 (Rejected, Technical)

**Original text:**

```text
Daily until December 24, 1997:

       DTSTART;TZID=America/New_York:19970902T090000
       RRULE:FREQ=DAILY;UNTIL=19971224T000000Z

       ==> (1997 9:00 AM EDT) September 2-30;October 1-25
           (1997 9:00 AM EST) October 26-31;November 1-30;December 1-23
```

**Corrected text:**

```text
Daily until December 24, 1997:

       DTSTART;TZID=America/New_York:19970902T090000
       RRULE:FREQ=DAILY;UNTIL=19971224T140000Z
                                       ^^
       ==> (1997 9:00 AM EDT) September 2-30;October 1-25
           (1997 9:00 AM EST) October 26-31;November 1-30;December 1-24
                                                                     ^^
```

**Notes:**

```text
The UNTIL rule part has value type DATE-TIME (same as DTSTART), but the introductory text "Daily until December 24, 1997" mentions a DATE only. Assuming that "until", like UNTIL, is inclusive, I would expect

    (1997 9:00 AM EST) December 24

to be the last instance, i.e. the unstated time is 9:00 AM. Translating to UTC you get

    19971224T140000Z

The same error occurs in all examples of section 3.8.5.3 with "December 24, 1997", four in all: pages 123 (above), 125 (twice) and 126. The resulting occurrences are only affected for pages 123 and 125 (second).
 --VERIFIER NOTES-- 
The example is correct as-is.  UNTIL does not have to match the recurrence pattern.

See https://mailarchive.ietf.org/arch/msg/calsify/x82GopunVcEh8y5UGSIsEIC3s6M/
```

## Erratum 3038: section 3.8.7.2 (Held for Document Update, Technical)

**Original text:**

```text
Value Type:  DATE-TIME

   Property Parameters:  IANA and non-standard property parameters can
      be specified on this property.

   Conformance:  This property MUST be included in the "VEVENT",
      "VTODO", "VJOURNAL", or "VFREEBUSY" calendar components.

   Description:  The value MUST be specified in the UTC time format.

      This property is also useful to protocols such as [2447bis] that
      have inherent latency issues with the delivery of content.  This
      property will assist in the proper sequencing of messages
      containing iCalendar objects.
```

**Corrected text:**

```text
Value Type:  DATE-TIME. The time value MUST be in the DATE WITH UTC
      TIME form defined for the DATE-TIME value type.

   Property Parameters:  IANA and non-standard property parameters can
      be specified on this property.

   Conformance:  This property MUST be included in the "VEVENT",
      "VTODO", "VJOURNAL", or "VFREEBUSY" calendar components.

   Description:  This property is also useful to protocols such as
      [2447bis] that have inherent latency issues with the delivery of
      content.  This property will assist in the proper sequencing of
      messages containing iCalendar objects.
```

**Notes:**

```text
Application of the DATE-TIME value type is inconsistent in the RFC, and can lead to ambiguity since DATE-TIME can take on three different forms. The wording for the corrected Value Type for DTSTAMP is similar to the DTSTART property's Value Type. This is to make it clear that the only acceptable form is DATE WITH UTC TIME. You can also see evidence of defining specificity inline with the Value Type in the GEO property.

The spec author comments: "To improve consistency, we should modify Section 3.8.7.2. Date-Time Stamp and Section 3.8.7.3. Last Modified to use the same phrasing as Section 3.8.7.1. Date-Time Created and Section 3.8.2.1. Date-Time Completed."
```

## Erratum 5082: section 3.8.7.3 (Rejected, Technical)

**Original text:**

```text
N/A
```

**Corrected text:**

```text
The value must not be in the future.
```

**Notes:**

```text
If future values are allowed for LAST-MODIFIED, it makes it very difficult for software to perform change management for a VEVENT.

Say for example, an event is imported from a source and the VEVENT has a future date. For example, December 20 2017 12:00:00Z

That event is then edited and assigned the actual correct date and time. Say August 9 2017 13:45:44Z.

Software that examines the VEVENT's LAST-MODIFIED to determine if the VEVENT record has been modified will not see the VEVENT is updated. 

In order for different systems to perform change management, the value for LAST-MODIFIED should NEVER be a future date.
 --VERIFIER NOTES-- 
The description of the property already implies that it is not in the future.  And any handling of clock skew is an iTIP/CalDAV protocol issue, NOT a data format issue.

See https://mailarchive.ietf.org/arch/msg/calsify/x82GopunVcEh8y5UGSIsEIC3s6M/
```

## Erratum 4606: section 3.8.8.3 (Rejected, Technical)

**Original text:**

```text
rstatus    = "REQUEST-STATUS" rstatparam ":"
                    statcode ";" statdesc [";" extdata]
```

**Corrected text:**

```text
rstatus    = "REQUEST-STATUS" statcode ":"
                    rstatparam ";" statdesc [";" extdata]
```

**Notes:**

```text
'rstatparam' and 'statcode' are interchanged.
 --VERIFIER NOTES-- 
The original text is correct: "rstatparam" defines the set of allowed *parameters* on the "REQUEST-STATUS" property. Parameters always occur immediately after the property name and before the ":" that separates the property value. The property *value* is a semicolon-separated structured text field with the first component being "statcode", and appears after the ":".
```

## Erratum 7945: section 3.8.8.3 (Verified, Technical)

**Original text:**

```text
rstatus    = "REQUEST-STATUS" rstatparam ":"
             statcode ";" statdesc [";" extdata]
```

**Corrected text:**

```text
rstatus    = "REQUEST-STATUS" rstatparam ":"
             statcode ";" statdesc [";" extdata] CRLF
```

**Notes:**

```text
All other properties are specified to end with a CRLF. There seems to be no reason for this property to be an exception.
```

## Erratum 2039: section 4 (Verified, Technical)

**Original text:**

```text
BEGIN:VALARM
       ACTION:AUDIO
       TRIGGER:19980403T120000Z
       ATTACH;FMTTYPE=audio/basic:http://example.com/pub/audio-
        files/ssbanner.aud
       REPEAT:4
       DURATION:PT1H
       END:VALARM
```

**Corrected text:**

```text
BEGIN:VALARM
       ACTION:AUDIO
       TRIGGER;VALUE=DATE-TIME:19980403T120000Z
       ATTACH;FMTTYPE=audio/basic:http://example.com/pub/audio-
        files/ssbanner.aud
       REPEAT:4
       DURATION:PT1H
       END:VALARM
```

**Notes:**

```text
The trigger is presented as a DATE-TIME, but the default type of this field is DURATION (3.8.6.3). Either the type must be specified (as per the corrected text), or specified in DURATION format.
```

## Erratum 3740: section 4 (Verified, Technical)

**Original text:**

```text
BEGIN:VTIMEZONE
       TZID:America/New_York
       BEGIN:STANDARD
       DTSTART:19981025T020000
       TZOFFSETFROM:-0400
       TZOFFSETTO:-0500
       TZNAME:EST
       END:STANDARD
       BEGIN:DAYLIGHT
       DTSTART:19990404T020000
       TZOFFSETFROM:-0500
       TZOFFSETTO:-0400
       TZNAME:EDT
       END:DAYLIGHT
       END:VTIMEZONE
```

**Corrected text:**

```text
BEGIN:VTIMEZONE
       TZID:America/New_York
       BEGIN:STANDARD
       DTSTART:19671029T020000
       RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU;UNTIL=20061029T060000Z
       TZOFFSETFROM:-0400
       TZOFFSETTO:-0500
       TZNAME:EST
       END:STANDARD
       BEGIN:DAYLIGHT
       DTSTART:19870405T020000
       RRULE:FREQ=YEARLY;BYMONTH=4;BYDAY=1SU;UNTIL=20060402T070000Z
       TZOFFSETFROM:-0500
       TZOFFSETTO:-0400
       TZNAME:EDT
       END:DAYLIGHT
       END:VTIMEZONE
```

**Notes:**

```text
The time zone specification in the original example does not cover the event in the example (which occurs on 19980312, before both of the listed onsets).

---- Verifier notes -----
The corrected text uses part of the VTIMEZONE definition in the example on page 68.
```

## Erratum 4149: section 4 (Verified, Technical)

**Original text:**

```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//RDU Software//NONSGML HandCal//EN
BEGIN:VFREEBUSY
ORGANIZER:mailto:jsmith@example.com
DTSTART:19980313T141711Z
DTEND:19980410T141711Z
```

**Corrected text:**

```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//RDU Software//NONSGML HandCal//EN
BEGIN:VFREEBUSY
UID:19970901T115957Z-76A912@example.com
DTSTAMP:19970901T120000Z
ORGANIZER:mailto:jsmith@example.com
DTSTART:19980313T141711Z
DTEND:19980410T141711Z
```

**Notes:**

```text
3.6.4 says
       fbprop     = *(
                  ;
                  ; The following are REQUIRED,
                  ; but MUST NOT occur more than once.
                  ;
                  dtstamp / uid /
```

## Erratum 4150: section 10.2 (Rejected, Editorial)

**Original text:**

```text
[TZDB]                 Eggert, P. and A.D. Olson, "Sources for Time
                          Zone and Daylight Saving Time Data",
                          July 2009,
                          <http://www.twinsun.com/tz/tz-link.htm>.
```

**Corrected text:**

```text
[TZDB]       Eggert, P. and A. Olson, "Sources for Time Zone and
                Daylight Saving Time Data", 1987,
                <ftp://ftp.iana.org/tz/code/tz-link.htm>.

              Internet Assigned Numbers Authority (IANA)
              "Time Zone Database"
                <http://www.iana.org/time-zones>.
```

**Notes:**

```text
The twinsun.com version is no longer maintained by the volunteer(s) tz@elsie.nci.nih.gov. The document and the tz database, have been adopted by members of IETF and iana.org. The database itself is public domain. 

The corrected text matches that of rfc6557 11.1.  Normative References [TZDB]



http://tools.ietf.org/html/rfc6557
http://www.iana.org/time-zones/repository/tz-link.html
http://www.iana.org/time-zones
 --VERIFIER NOTES-- 
The document was correct at the time it was published, so this report does not meet the formal criteria for errata.

That said, Peter is correct that the location of the time zone database has since changed, and readers should look to the new location, as he has specified in this report.
```

## Erratum 4626: section A.1 (Held for Document Update, Editorial)

**Original text:**

```text
[Missing item]
```

**Corrected text:**

```text
6.  The value of the "DUE" property MUST be strictly later in time than
    the value of the "DTSTART" property (as opposed to only "equal or
    later in time").
```

**Notes:**

```text
See http://www.ietf.org/mail-archive/web/calsify/current/msg02217.html
```

## Erratum 2038: section Appendix A (Verified, Editorial)

**Original text:**

```text
5.  The "DURATION" property can no longer appear in "VFREEBUSY"
       components.

A.2. Restrictions Removed
```

**Corrected text:**

```text
5.  The "DURATION" property can no longer appear in "VFREEBUSY"
       components.

   6.  Use of the "charset" Content-Type parameter in MIME transports 
       is now mandatory.

A.2. Restrictions Removed
```

**Notes:**

```text
One change is missing from the list of changes.
```

## Erratum 5794: section ToC (Verified, Editorial)

**Original text:**

```text
1.  Introduction  . . . . . . . . . . . . . . . . . . . . . . . .   5
   2.  Basic Grammar and Conventions . . . . . . . . . . . . . . . .   6
     2.1.  Formatting Conventions  . . . . . . . . . . . . . . . . .   6
     2.2.  Related Memos . . . . . . . . . . . . . . . . . . . . . .   7
   3.  iCalendar Object Specification  . . . . . . . . . . . . . . .   8
     3.1.  Content Lines . . . . . . . . . . . . . . . . . . . . . .   8
       3.1.1.  List and Field Separators . . . . . . . . . . . . . .  11
       3.1.2.  Multiple Values . . . . . . . . . . . . . . . . . . .  11
       3.1.3.  Binary Content  . . . . . . . . . . . . . . . . . . .  11
       3.1.4.  Character Set . . . . . . . . . . . . . . . . . . . .  12
     3.2.  Property Parameters . . . . . . . . . . . . . . . . . . .  12
       3.2.1.  Alternate Text Representation . . . . . . . . . . . .  13
       3.2.2.  Common Name . . . . . . . . . . . . . . . . . . . . .  15
       3.2.3.  Calendar User Type  . . . . . . . . . . . . . . . . .  15
       3.2.4.  Delegators  . . . . . . . . . . . . . . . . . . . . .  16
       3.2.5.  Delegatees  . . . . . . . . . . . . . . . . . . . . .  16
       3.2.6.  Directory Entry Reference . . . . . . . . . . . . . .  17
       3.2.7.  Inline Encoding . . . . . . . . . . . . . . . . . . .  17
       3.2.8.  Format Type . . . . . . . . . . . . . . . . . . . . .  18
       3.2.9.  Free/Busy Time Type . . . . . . . . . . . . . . . . .  19
       3.2.10. Language  . . . . . . . . . . . . . . . . . . . . . .  20
       3.2.11. Group or List Membership  . . . . . . . . . . . . . .  20
       3.2.12. Participation Status  . . . . . . . . . . . . . . . .  21
       3.2.13. Recurrence Identifier Range . . . . . . . . . . . . .  22
       3.2.14. Alarm Trigger Relationship  . . . . . . . . . . . . .  23
       3.2.15. Relationship Type . . . . . . . . . . . . . . . . . .  24
       3.2.16. Participation Role  . . . . . . . . . . . . . . . . .  25
       3.2.17. RSVP Expectation  . . . . . . . . . . . . . . . . . .  25
       3.2.18. Sent By . . . . . . . . . . . . . . . . . . . . . . .  26
       3.2.19. Time Zone Identifier  . . . . . . . . . . . . . . . .  26
       3.2.20. Value Data Types  . . . . . . . . . . . . . . . . . .  28
     3.3.  Property Value Data Types . . . . . . . . . . . . . . . .  29
       3.3.1.  Binary  . . . . . . . . . . . . . . . . . . . . . . .  29
       3.3.2.  Boolean . . . . . . . . . . . . . . . . . . . . . . .  30
       3.3.3.  Calendar User Address . . . . . . . . . . . . . . . .  30
       3.3.4.  Date  . . . . . . . . . . . . . . . . . . . . . . . .  31
       3.3.5.  Date-Time . . . . . . . . . . . . . . . . . . . . . .  31
       3.3.6.  Duration  . . . . . . . . . . . . . . . . . . . . . .  34
       3.3.7.  Float . . . . . . . . . . . . . . . . . . . . . . . .  35
       3.3.8.  Integer . . . . . . . . . . . . . . . . . . . . . . .  35
       3.3.9.  Period of Time  . . . . . . . . . . . . . . . . . . .  36
       3.3.10. Recurrence Rule . . . . . . . . . . . . . . . . . . .  37
       3.3.11. Text  . . . . . . . . . . . . . . . . . . . . . . . .  45
       3.3.12. Time  . . . . . . . . . . . . . . . . . . . . . . . .  46
       3.3.13. URI . . . . . . . . . . . . . . . . . . . . . . . . .  48
       3.3.14. UTC Offset  . . . . . . . . . . . . . . . . . . . . .  49
     3.4.  iCalendar Object  . . . . . . . . . . . . . . . . . . . .  49
     3.5.  Property  . . . . . . . . . . . . . . . . . . . . . . . .  50
     3.6.  Calendar Components . . . . . . . . . . . . . . . . . . .  50
       3.6.1.  Event Component . . . . . . . . . . . . . . . . . . .  52
       3.6.2.  To-Do Component . . . . . . . . . . . . . . . . . . .  56
       3.6.3.  Journal Component . . . . . . . . . . . . . . . . . .  58
       3.6.4.  Free/Busy Component . . . . . . . . . . . . . . . . .  60
       3.6.5.  Time Zone Component . . . . . . . . . . . . . . . . .  63
       3.6.6.  Alarm Component . . . . . . . . . . . . . . . . . . .  72
     3.7.  Calendar Properties . . . . . . . . . . . . . . . . . . .  77
       3.7.1.  Calendar Scale  . . . . . . . . . . . . . . . . . . .  77
       3.7.2.  Method  . . . . . . . . . . . . . . . . . . . . . . .  78
       3.7.3.  Product Identifier  . . . . . . . . . . . . . . . . .  79
       3.7.4.  Version . . . . . . . . . . . . . . . . . . . . . . .  80
     3.8.  Component Properties  . . . . . . . . . . . . . . . . . .  81
       3.8.1.  Descriptive Component Properties  . . . . . . . . . .  81
         3.8.1.1.  Attachment  . . . . . . . . . . . . . . . . . . .  81
         3.8.1.2.  Categories  . . . . . . . . . . . . . . . . . . .  82
         3.8.1.3.  Classification  . . . . . . . . . . . . . . . . .  83
         3.8.1.4.  Comment . . . . . . . . . . . . . . . . . . . . .  84
         3.8.1.5.  Description . . . . . . . . . . . . . . . . . . .  85
         3.8.1.6.  Geographic Position . . . . . . . . . . . . . . .  87
         3.8.1.7.  Location  . . . . . . . . . . . . . . . . . . . .  88
         3.8.1.8.  Percent Complete  . . . . . . . . . . . . . . . .  89
         3.8.1.9.  Priority  . . . . . . . . . . . . . . . . . . . .  90
         3.8.1.10. Resources . . . . . . . . . . . . . . . . . . . .  92
         3.8.1.11. Status  . . . . . . . . . . . . . . . . . . . . .  93
         3.8.1.12. Summary . . . . . . . . . . . . . . . . . . . . .  94
       3.8.2.  Date and Time Component Properties  . . . . . . . . .  95
         3.8.2.1.  Date-Time Completed . . . . . . . . . . . . . . .  95
         3.8.2.2.  Date-Time End . . . . . . . . . . . . . . . . . .  96
         3.8.2.3.  Date-Time Due . . . . . . . . . . . . . . . . . .  97
         3.8.2.4.  Date-Time Start . . . . . . . . . . . . . . . . .  99
         3.8.2.5.  Duration  . . . . . . . . . . . . . . . . . . . . 100
         3.8.2.6.  Free/Busy Time  . . . . . . . . . . . . . . . . . 101
         3.8.2.7.  Time Transparency . . . . . . . . . . . . . . . . 102
       3.8.3.  Time Zone Component Properties  . . . . . . . . . . . 103
         3.8.3.1.  Time Zone Identifier  . . . . . . . . . . . . . . 103
         3.8.3.2.  Time Zone Name  . . . . . . . . . . . . . . . . . 105
         3.8.3.3.  Time Zone Offset From . . . . . . . . . . . . . . 106
         3.8.3.4.  Time Zone Offset To . . . . . . . . . . . . . . . 106
         3.8.3.5.  Time Zone URL . . . . . . . . . . . . . . . . . . 107
       3.8.4.  Relationship Component Properties . . . . . . . . . . 108
         3.8.4.1.  Attendee  . . . . . . . . . . . . . . . . . . . . 108
         3.8.4.2.  Contact . . . . . . . . . . . . . . . . . . . . . 111

         3.8.4.3.  Organizer . . . . . . . . . . . . . . . . . . . . 113
         3.8.4.4.  Recurrence ID . . . . . . . . . . . . . . . . . . 114
         3.8.4.5.  Related To  . . . . . . . . . . . . . . . . . . . 117
         3.8.4.6.  Uniform Resource Locator  . . . . . . . . . . . . 118
         3.8.4.7.  Unique Identifier . . . . . . . . . . . . . . . . 119
       3.8.5.  Recurrence Component Properties . . . . . . . . . . . 120
         3.8.5.1.  Exception Date-Times  . . . . . . . . . . . . . . 120
         3.8.5.2.  Recurrence Date-Times . . . . . . . . . . . . . . 122
         3.8.5.3.  Recurrence Rule . . . . . . . . . . . . . . . . . 124
       3.8.6.  Alarm Component Properties  . . . . . . . . . . . . . 134
         3.8.6.1.  Action  . . . . . . . . . . . . . . . . . . . . . 134
         3.8.6.2.  Repeat Count  . . . . . . . . . . . . . . . . . . 135
         3.8.6.3.  Trigger . . . . . . . . . . . . . . . . . . . . . 135
       3.8.7.  Change Management Component Properties  . . . . . . . 138
         3.8.7.1.  Date-Time Created . . . . . . . . . . . . . . . . 138
         3.8.7.2.  Date-Time Stamp . . . . . . . . . . . . . . . . . 139
         3.8.7.3.  Last Modified . . . . . . . . . . . . . . . . . . 140
         3.8.7.4.  Sequence Number . . . . . . . . . . . . . . . . . 141
       3.8.8.  Miscellaneous Component Properties  . . . . . . . . . 142
         3.8.8.1.  IANA Properties . . . . . . . . . . . . . . . . . 142
         3.8.8.2.  Non-Standard Properties . . . . . . . . . . . . . 142
         3.8.8.3.  Request Status  . . . . . . . . . . . . . . . . . 144
   4.  iCalendar Object Examples . . . . . . . . . . . . . . . . . . 146
   5.  Recommended Practices . . . . . . . . . . . . . . . . . . . . 150
   6.  Internationalization Considerations . . . . . . . . . . . . . 151
   7.  Security Considerations . . . . . . . . . . . . . . . . . . . 151
   8.  IANA Considerations . . . . . . . . . . . . . . . . . . . . . 151
     8.1.  iCalendar Media Type Registration . . . . . . . . . . . . 151
     8.2.  New iCalendar Elements Registration . . . . . . . . . . . 155
       8.2.1.  iCalendar Elements Registration Procedure . . . . . . 155
       8.2.2.  Registration Template for Components  . . . . . . . . 155
       8.2.3.  Registration Template for Properties  . . . . . . . . 156
       8.2.4.  Registration Template for Parameters  . . . . . . . . 156
       8.2.5.  Registration Template for Value Data Types  . . . . . 157
       8.2.6.  Registration Template for Values  . . . . . . . . . . 157
     8.3.  Initial iCalendar Elements Registries . . . . . . . . . . 158
       8.3.1.  Components Registry . . . . . . . . . . . . . . . . . 158
       8.3.2.  Properties Registry . . . . . . . . . . . . . . . . . 158
       8.3.3.  Parameters Registry . . . . . . . . . . . . . . . . . 161
       8.3.4.  Value Data Types Registry . . . . . . . . . . . . . . 162
       8.3.5.  Calendar User Types Registry  . . . . . . . . . . . . 162
       8.3.6.  Free/Busy Time Types Registry . . . . . . . . . . . . 163
       8.3.7.  Participation Statuses Registry . . . . . . . . . . . 163
       8.3.8.  Relationship Types Registry . . . . . . . . . . . . . 164
       8.3.9.  Participation Roles Registry  . . . . . . . . . . . . 164
       8.3.10. Actions Registry  . . . . . . . . . . . . . . . . . . 165
       8.3.11. Classifications Registry  . . . . . . . . . . . . . . 165
       8.3.12. Methods Registry  . . . . . . . . . . . . . . . . . . 165
   9.  Acknowledgments . . . . . . . . . . . . . . . . . . . . . . . 165
   10. References  . . . . . . . . . . . . . . . . . . . . . . . . . 166
     10.1. Normative References  . . . . . . . . . . . . . . . . . . 166
     10.2. Informative References  . . . . . . . . . . . . . . . . . 167
   Appendix A.  Differences from RFC 2445  . . . . . . . . . . . . . 169
     A.1.  New Restrictions  . . . . . . . . . . . . . . . . . . . . 169
     A.2.  Restrictions Removed  . . . . . . . . . . . . . . . . . . 169
     A.3.  Deprecated Features . . . . . . . . . . . . . . . . . . . 169
```

**Corrected text:**

```text
1.  Introduction  . . . . . . . . . . . . . . . . . . . . . . . .   5
   2.  Basic Grammar and Conventions . . . . . . . . . . . . . . . .   6
     2.1.  Formatting Conventions  . . . . . . . . . . . . . . . . .   6
     2.2.  Related Memos . . . . . . . . . . . . . . . . . . . . . .   8
   3.  iCalendar Object Specification  . . . . . . . . . . . . . . .   8
     3.1.  Content Lines . . . . . . . . . . . . . . . . . . . . . .   9
       3.1.1.  List and Field Separators . . . . . . . . . . . . . .  11
       3.1.2.  Multiple Values . . . . . . . . . . . . . . . . . . .  12
       3.1.3.  Binary Content  . . . . . . . . . . . . . . . . . . .  12
       3.1.4.  Character Set . . . . . . . . . . . . . . . . . . . .  13
     3.2.  Property Parameters . . . . . . . . . . . . . . . . . . .  13
       3.2.1.  Alternate Text Representation . . . . . . . . . . . .  14
       3.2.2.  Common Name . . . . . . . . . . . . . . . . . . . . .  15
       3.2.3.  Calendar User Type  . . . . . . . . . . . . . . . . .  16
       3.2.4.  Delegators  . . . . . . . . . . . . . . . . . . . . .  17
       3.2.5.  Delegatees  . . . . . . . . . . . . . . . . . . . . .  17
       3.2.6.  Directory Entry Reference . . . . . . . . . . . . . .  18
       3.2.7.  Inline Encoding . . . . . . . . . . . . . . . . . . .  18
       3.2.8.  Format Type . . . . . . . . . . . . . . . . . . . . .  19
       3.2.9.  Free/Busy Time Type . . . . . . . . . . . . . . . . .  20
       3.2.10. Language  . . . . . . . . . . . . . . . . . . . . . .  21
       3.2.11. Group or List Membership  . . . . . . . . . . . . . .  21
       3.2.12. Participation Status  . . . . . . . . . . . . . . . .  22
       3.2.13. Recurrence Identifier Range . . . . . . . . . . . . .  23
       3.2.14. Alarm Trigger Relationship  . . . . . . . . . . . . .  24
       3.2.15. Relationship Type . . . . . . . . . . . . . . . . . .  25
       3.2.16. Participation Role  . . . . . . . . . . . . . . . . .  25
       3.2.17. RSVP Expectation  . . . . . . . . . . . . . . . . . .  26
       3.2.18. Sent By . . . . . . . . . . . . . . . . . . . . . . .  27
       3.2.19. Time Zone Identifier  . . . . . . . . . . . . . . . .  27
       3.2.20. Value Data Types  . . . . . . . . . . . . . . . . . .  29
     3.3.  Property Value Data Types . . . . . . . . . . . . . . . .  30
       3.3.1.  Binary  . . . . . . . . . . . . . . . . . . . . . . .  30
       3.3.2.  Boolean . . . . . . . . . . . . . . . . . . . . . . .  31
       3.3.3.  Calendar User Address . . . . . . . . . . . . . . . .  31
       3.3.4.  Date  . . . . . . . . . . . . . . . . . . . . . . . .  32
       3.3.5.  Date-Time . . . . . . . . . . . . . . . . . . . . . .  32
       3.3.6.  Duration  . . . . . . . . . . . . . . . . . . . . . .  35
       3.3.7.  Float . . . . . . . . . . . . . . . . . . . . . . . .  36
       3.3.8.  Integer . . . . . . . . . . . . . . . . . . . . . . .  37
       3.3.9.  Period of Time  . . . . . . . . . . . . . . . . . . .  37
       3.3.10. Recurrence Rule . . . . . . . . . . . . . . . . . . .  38
       3.3.11. Text  . . . . . . . . . . . . . . . . . . . . . . . .  45
       3.3.12. Time  . . . . . . . . . . . . . . . . . . . . . . . .  47
       3.3.13. URI . . . . . . . . . . . . . . . . . . . . . . . . .  49
       3.3.14. UTC Offset  . . . . . . . . . . . . . . . . . . . . .  49
     3.4.  iCalendar Object  . . . . . . . . . . . . . . . . . . . .  50
     3.5.  Property  . . . . . . . . . . . . . . . . . . . . . . . .  51
     3.6.  Calendar Components . . . . . . . . . . . . . . . . . . .  51
       3.6.1.  Event Component . . . . . . . . . . . . . . . . . . .  52
       3.6.2.  To-Do Component . . . . . . . . . . . . . . . . . . .  55
       3.6.3.  Journal Component . . . . . . . . . . . . . . . . . .  57
       3.6.4.  Free/Busy Component . . . . . . . . . . . . . . . . .  59
       3.6.5.  Time Zone Component . . . . . . . . . . . . . . . . .  62
       3.6.6.  Alarm Component . . . . . . . . . . . . . . . . . . .  71
     3.7.  Calendar Properties . . . . . . . . . . . . . . . . . . .  76
       3.7.1.  Calendar Scale  . . . . . . . . . . . . . . . . . . .  76
       3.7.2.  Method  . . . . . . . . . . . . . . . . . . . . . . .  77
       3.7.3.  Product Identifier  . . . . . . . . . . . . . . . . .  78
       3.7.4.  Version . . . . . . . . . . . . . . . . . . . . . . .  79
     3.8.  Component Properties  . . . . . . . . . . . . . . . . . .  80
       3.8.1.  Descriptive Component Properties  . . . . . . . . . .  80
         3.8.1.1.  Attachment  . . . . . . . . . . . . . . . . . . .  80
         3.8.1.2.  Categories  . . . . . . . . . . . . . . . . . . .  81
         3.8.1.3.  Classification  . . . . . . . . . . . . . . . . .  82
         3.8.1.4.  Comment . . . . . . . . . . . . . . . . . . . . .  83
         3.8.1.5.  Description . . . . . . . . . . . . . . . . . . .  84
         3.8.1.6.  Geographic Position . . . . . . . . . . . . . . .  85
         3.8.1.7.  Location  . . . . . . . . . . . . . . . . . . . .  87
         3.8.1.8.  Percent Complete  . . . . . . . . . . . . . . . .  88
         3.8.1.9.  Priority  . . . . . . . . . . . . . . . . . . . .  89
         3.8.1.10. Resources . . . . . . . . . . . . . . . . . . . .  91
         3.8.1.11. Status  . . . . . . . . . . . . . . . . . . . . .  92
         3.8.1.12. Summary . . . . . . . . . . . . . . . . . . . . .  93
       3.8.2.  Date and Time Component Properties  . . . . . . . . .  94
         3.8.2.1.  Date-Time Completed . . . . . . . . . . . . . . .  94
         3.8.2.2.  Date-Time End . . . . . . . . . . . . . . . . . .  95
         3.8.2.3.  Date-Time Due . . . . . . . . . . . . . . . . . .  96
         3.8.2.4.  Date-Time Start . . . . . . . . . . . . . . . . .  97
         3.8.2.5.  Duration  . . . . . . . . . . . . . . . . . . . .  99
         3.8.2.6.  Free/Busy Time  . . . . . . . . . . . . . . . . . 100
         3.8.2.7.  Time Transparency . . . . . . . . . . . . . . . . 101
       3.8.3.  Time Zone Component Properties  . . . . . . . . . . . 102
         3.8.3.1.  Time Zone Identifier  . . . . . . . . . . . . . . 102
         3.8.3.2.  Time Zone Name  . . . . . . . . . . . . . . . . . 103
         3.8.3.3.  Time Zone Offset From . . . . . . . . . . . . . . 104
         3.8.3.4.  Time Zone Offset To . . . . . . . . . . . . . . . 105
         3.8.3.5.  Time Zone URL . . . . . . . . . . . . . . . . . . 106
       3.8.4.  Relationship Component Properties . . . . . . . . . . 106
         3.8.4.1.  Attendee  . . . . . . . . . . . . . . . . . . . . 107
         3.8.4.2.  Contact . . . . . . . . . . . . . . . . . . . . . 109
         3.8.4.3.  Organizer . . . . . . . . . . . . . . . . . . . . 111
         3.8.4.4.  Recurrence ID . . . . . . . . . . . . . . . . . . 112
         3.8.4.5.  Related To  . . . . . . . . . . . . . . . . . . . 115
         3.8.4.6.  Uniform Resource Locator  . . . . . . . . . . . . 116
         3.8.4.7.  Unique Identifier . . . . . . . . . . . . . . . . 117
       3.8.5.  Recurrence Component Properties . . . . . . . . . . . 118
         3.8.5.1.  Exception Date-Times  . . . . . . . . . . . . . . 118
         3.8.5.2.  Recurrence Date-Times . . . . . . . . . . . . . . 120
         3.8.5.3.  Recurrence Rule . . . . . . . . . . . . . . . . . 122
       3.8.6.  Alarm Component Properties  . . . . . . . . . . . . . 132
         3.8.6.1.  Action  . . . . . . . . . . . . . . . . . . . . . 132
         3.8.6.2.  Repeat Count  . . . . . . . . . . . . . . . . . . 133
         3.8.6.3.  Trigger . . . . . . . . . . . . . . . . . . . . . 133
       3.8.7.  Change Management Component Properties  . . . . . . . 136
         3.8.7.1.  Date-Time Created . . . . . . . . . . . . . . . . 136
         3.8.7.2.  Date-Time Stamp . . . . . . . . . . . . . . . . . 137
         3.8.7.3.  Last Modified . . . . . . . . . . . . . . . . . . 138
         3.8.7.4.  Sequence Number . . . . . . . . . . . . . . . . . 138
       3.8.8.  Miscellaneous Component Properties  . . . . . . . . . 139
         3.8.8.1.  IANA Properties . . . . . . . . . . . . . . . . . 140
         3.8.8.2.  Non-Standard Properties . . . . . . . . . . . . . 140
         3.8.8.3.  Request Status  . . . . . . . . . . . . . . . . . 141
   4.  iCalendar Object Examples . . . . . . . . . . . . . . . . . . 144
   5.  Recommended Practices . . . . . . . . . . . . . . . . . . . . 147
   6.  Internationalization Considerations . . . . . . . . . . . . . 148
   7.  Security Considerations . . . . . . . . . . . . . . . . . . . 148
   8.  IANA Considerations . . . . . . . . . . . . . . . . . . . . . 149
     8.1.  iCalendar Media Type Registration . . . . . . . . . . . . 149
     8.2.  New iCalendar Elements Registration . . . . . . . . . . . 152
       8.2.1.  iCalendar Elements Registration Procedure . . . . . . 152
       8.2.2.  Registration Template for Components  . . . . . . . . 152
       8.2.3.  Registration Template for Properties  . . . . . . . . 153
       8.2.4.  Registration Template for Parameters  . . . . . . . . 153
       8.2.5.  Registration Template for Value Data Types  . . . . . 154
       8.2.6.  Registration Template for Values  . . . . . . . . . . 154
     8.3.  Initial iCalendar Elements Registries . . . . . . . . . . 155
       8.3.1.  Components Registry . . . . . . . . . . . . . . . . . 155
       8.3.2.  Properties Registry . . . . . . . . . . . . . . . . . 156
       8.3.3.  Parameters Registry . . . . . . . . . . . . . . . . . 158
       8.3.4.  Value Data Types Registry . . . . . . . . . . . . . . 159
       8.3.5.  Calendar User Types Registry  . . . . . . . . . . . . 160
       8.3.6.  Free/Busy Time Types Registry . . . . . . . . . . . . 160
       8.3.7.  Participation Statuses Registry . . . . . . . . . . . 161
       8.3.8.  Relationship Types Registry . . . . . . . . . . . . . 161
       8.3.9.  Participation Roles Registry  . . . . . . . . . . . . 162
       8.3.10. Actions Registry  . . . . . . . . . . . . . . . . . . 162
       8.3.11. Classifications Registry  . . . . . . . . . . . . . . 162
       8.3.12. Methods Registry  . . . . . . . . . . . . . . . . . . 163
   9.  Acknowledgments . . . . . . . . . . . . . . . . . . . . . . . 163
   10. References  . . . . . . . . . . . . . . . . . . . . . . . . . 164
     10.1. Normative References  . . . . . . . . . . . . . . . . . . 164
     10.2. Informative References  . . . . . . . . . . . . . . . . . 165
   Appendix A.  Differences from RFC 2445  . . . . . . . . . . . . . 167
     A.1.  New Restrictions  . . . . . . . . . . . . . . . . . . . . 167
     A.2.  Restrictions Removed  . . . . . . . . . . . . . . . . . . 167
     A.3.  Deprecated Features . . . . . . . . . . . . . . . . . . . 167
```

**Notes:**

```text
Most of the Table Of Contents gives wrong page numbers.

===== Verifier notes =====
Indeed: the character table in Section 2.1, which appears at the top of page 8 in the RFC, appears to have been added during final editing, and has thrown off the page numbering for all sections beginning with 2.2.
```
