# 0001: Neuer Code unter Apache-2.0 und BSD-3-Clause

Stand: 2026-11-15 · entschieden durch die Visionärin / den Visionär

## Kontext
Upstream-`LICENSE`: Beiträge seit 2017-12-01 stehen unter Apache-2.0, und die BSD-3-Clause gilt für den gesamten Code, auch den unter Apache-2.0. Das Projekt war mit Apache-2.0 allein angelegt.

## Entscheidung
Neuer Code und neue Tests stehen unter Apache-2.0 und BSD-3-Clause, genau wie upstream. Neue Dateien, die nicht aus upstream stammen, tragen `# SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause`; Dateien unter `tests/` und `src/` folgen der upstream-Konvention (kein Header).

## Folgen
Fixes und Tests sind ohne Neulizenzierung upstream einreichbar. Beitragende bestätigen mit der Abgabe beide Lizenzen. Texte bleiben CC BY 4.0.
