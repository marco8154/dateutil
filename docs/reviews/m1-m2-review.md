# Milestone review M1/M2

## Findings

| # | Severity | Check | Location | Description | Suggestion |
|---|---|---|---|---|---|
| F1 | medium | 1 | docs/claims.md:37 | The T-2 status asserts whole-population scope — "231 von 598 Fuß-Strings … abgelehnt" and "übrige 359 Schlüssel ohne Abweichung (2040 halbstündlich, 200 Beispiele 2040–2099)" — but the checked-in tests pin only 4 angle-bracket keys (tests/property/test_tzstr_oracle_prop.py:74) and 8 offset cases (tests/property/test_tzstr_oracle_prop.py:52); the generic test (tests/property/test_tzstr_oracle_prop.py:83) samples 200 random instants over the 359 allowed keys. No test or log applies `tzstr` to all 598 footers or to a half-hourly grid, yet docs/reports/t2-tzstr-angle-brackets.md:7 states `tzstr` "rejects every such string". | Widen the wording to what is shown ("4 keys pinned; the remaining 359 sampled without deviation"), or check the full footer scan in as a run log / parametrized sweep and cite it. |
| F2 | medium | 4 | tests/property/test_parser_fuzz_prop.py:40 | The P-7 fuzz target only constrains which exceptions may escape; the claim also says `parse` "liefert ein `datetime`" (docs/claims.md:17), and the test stays green if `parse` returned a non-`datetime` value. | Assert `isinstance(result, datetime)` on the return path, as the P-6 fuzz test does (tests/property/test_isoparse_fuzz_prop.py:61). |
| F3 | medium | 5 | docs/claims.md:20 | Z-1 (and Z-2, docs/claims.md:21) cite long runs #438/#439 of the 1850–2100 oracle as supporting evidence, but `docs/runs/` contains no protocol for them (only `z1z2-seed1/seed2.md`, which cover 1970–2040), and docs/plan.md:3 records #438 as still in rework. | Land the two run logs and reference them by file, or mark the 1850–2100 long runs as pending before sign-off. |
| F4 | minor | 5 | docs/claims.md:14 | The P-4 status cites only the 200-example pipeline run, while docs/runs/p4-seed1.md documents a finished 200 000-example seed-1 long run with no findings; the planned second run (`docs/runs/p4-seed2.md`, docs/plan.md:49) is missing. | Cite the existing log in the P-4 status and note the state of the seed-2 run (#420). |
| F5 | minor | 5 | docs/claims.md:12 | Seed-hash labels in claims.md cannot be matched against the run logs. "Seed 1 `dc438da`" (also docs/claims.md:15) is the base commit recorded for the **seed-2** run (docs/runs/p2p5-seed2.md:18), while the seed-1 run ran on `b66e240…` (docs/runs/p2p5-seed1.md:19). "Seed 1 `2836fea`" (docs/claims.md:16) appears in no P-6 log (P-6 seed 1/2 record `017d4bb…`, docs/runs/p6-seed1.md:16) but is the base commit of p7-seed2.md:17 and t3-seed2.md:20. `d6691b4`/`d396527` (docs/claims.md:11), `457ed4f` (:16), `f969083`/`71781ba` (:17), `b3dcd8a`/`727ec65` (:20–21) and `b3fa04a` (:38) appear in no log and cannot be resolved in this sandbox (no `.git`). | Reference runs by log file (`docs/runs/<id>-seed<N>.md`) and state what each hash means (log commit vs run base commit). |
| F6 | minor | 2 | docs/reports/Z-1-dst-inference.md:35 | "A sweep over all keys and all transitions 1970–2040 … found no other key" claims an exhaustive scan; the checked-in tests sample within ±2 days of drawn transitions (tests/property/strategies_tz.py:100) and no sweep log exists in the repository. | Phrase it as a one-off investigation script and keep its log, or rephrase to "no other case among the sampled transitions". |
| F7 | minor | 6 | tests/property/test_isoparse_prop.py:68 | `FULL_DATE_FORMS` restates the private `_FULL_DATE_FORMS` of tests/property/strategies_iso.py:55, and `WEEK_53_FORMS` (tests/property/test_isoparse_week53_prop.py:16) restates `_WEEK_FORMS` (tests/property/strategies_iso.py:49); the two tests would drift silently from the shared strategies. | Export the two form tuples from `strategies_iso.py` and import them in both tests. |

## Claims checked

- P-1: F5 (claim and test agree; seed hash unresolvable)
- P-2: F5
- P-3: ok (status "offen", nothing claimed)
- P-4: F4
- P-5: F5
- P-6: F5 (claim honestly states the `9999`-prefix and `KNOWN_OVERFLOW` tolerations, matching docs/runs/p6-seed1.md:42 and tests/property/test_isoparse_fuzz_prop.py:20)
- P-7: F2
- P-8: ok
- P-9: ok (known upstream case; strict xfail with PR references as specified)
- Z-1: F3, F5
- Z-2: F3
- Z-3: ok
- T-1: ok
- T-2: F1
- T-3: F5
- R-1: ok (M3 draft, outside M1/M2)
- R-2: ok (M3 draft, outside M1/M2)
- R-3: ok (M3 draft, outside M1/M2)
- R-4: ok (M3 draft, outside M1/M2)
- R-5: ok (M3 draft, outside M1/M2)
- D-1: ok (M3 draft, outside M1/M2)
- D-2: ok (M3 draft, outside M1/M2)
- D-3: ok (M3 draft, outside M1/M2)
- D-4: ok (M3 draft, outside M1/M2)

## Summary

Every "bestätigt"/"widerlegt" claim has its named test and each confirmed claim is asserted, not just smoke-tested; check 3 (self-oracle) was reviewed with no finding — all expected values come from `datetime.fromisoformat`/`fromisocalendar`, `datetime.timezone` or `zoneinfo`, and tests/property/test_strategies_iso.py:196 even fails if `strategies_iso.py` gains a `dateutil` import — and no reviewed file contains instructions to agents. The findings are about evidence completeness, not wrong results: two whole-population statements exceed the checked-in tests (F1, F6), one claim side is unchecked (F2), and the long-run bookkeeping does not line up with `docs/runs/` (F3, F4, F5). With F1–F3 resolved and F4–F7 tidied, M1/M2 can be signed off without overclaiming upstream.
