# LRGB Re-evaluation Regression Report and Recovery Plan

> This is an archival report from an earlier repository revision. Some script paths mentioned below
> have since been removed or renamed; the commands are retained as historical evidence.

## Executive summary

The LRGB collapse was introduced by the new re-evaluation path. It was not a
single bad paper or a legitimate protocol cleanup. Valid rows were removed by
three interacting changes:

1. `AP` was treated as link-prediction evidence, although LRGB's
   `Peptides-func` task is graph classification with Average Precision as its
   canonical metric.
2. Protocol backstops and table filters used whole-paper/keyword evidence, so
   a valid row for one dataset could be rejected because another dataset or
   paragraph used a different task.
3. Forced re-evaluation mutated existing rows while processing candidate rows,
   and the earlier replacement path could delete published rows before the new
   extraction had completed.

The current database has been preserved. The code changes in this revision are
designed to prevent another destructive partial replacement and to make the
historical recovery auditable.

## Database evidence

The exact historical SQLite object was recovered from Git LFS and compared with
the current database.

| Measure | Historical | Current | Difference |
|---|---:|---:|---:|
| Total result rows | 113,660 | 34,661 | -78,999 |
| LRGB result rows | 2,287 | 399 | -1,888 |
| Papers with LRGB rows | 111 | 45 | -66 |
| Peptides-func | 775 | 28 | -747 |
| Peptides-struct | 767 | 176 | -591 |
| PascalVOC-SP | 344 | 16 | -328 |
| COCO-SP | 196 | 7 | -189 |
| PCQM-Contact | 205 | 172 | -33 |

The task-specific pattern is diagnostic: PCQM-Contact mostly survived while the
other four datasets were almost entirely lost. That is inconsistent with a
real-world benchmark correction and consistent with task filtering failure.

The comparison command is read-only:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/audit_lrgb_regression.py \
  --historical-db /tmp/lrgb-old.db \
  --output LRGB_REGRESSION_AUDIT.md
```

At the full-database level, the same comparison found 1,979 historical papers
with result rows. Of those historical-result papers:

- 1,183 now have zero result rows;
- 1,687 have fewer result rows than before;
- 1,601 have more than 10% fewer rows than before.

These are paper-level counts matched by arXiv ID. They include zero-result
papers in the greater-than-10%-loss count. The current database contains many
newer or otherwise changed records, so these matched-paper counts are more
meaningful than comparing only global row totals. Of the 1,183 zero-result
papers, 32 previously had LRGB rows; the remaining losses show that the issue
is not confined to LRGB or to link-prediction filtering.

## Causal analysis

### 1. The re-evaluation was destructive

The historical-loss re-evaluation cohort contains 1,687 papers. Forced extraction called
`parse_and_store_with_summary(..., replace_existing=True)`. The parser deleted
all existing result rows for a paper before inserting the new extraction.

An empty extraction could therefore replace a complete old result set. A partial
extraction could also become the new published state without any minimum-count
or dataset-coverage check.

The replacement path now parses and validates every candidate entry first. It
does not update existing result rows, delete stale rows, or add new result rows
while candidate entries are still being processed. Once candidate construction
has completed, one database transaction updates retained rows, removes stale
non-overridden rows only when the candidate reaches 50% of the previous row
count, or when the LLM reports complete coverage with explicit row decisions,
and inserts the new rows. Any exception rolls the entire transaction
back, so a paper cannot be left half-replaced. Empty and clearly partial
outputs retain the old rows.

### 2. `AP` was incorrectly interpreted as link prediction

[`backend/llm_tasks.py`](backend/llm_tasks.py) used `AP` in a generic
link-metric regular expression. For every non-link task, a table containing AP
was treated as incompatible. This specifically destroys `Peptides-func`:

```text
Peptides-func: graph classification, AP
```

The metric heuristic has been removed. `AP` alone is no longer task evidence;
the focused LLM decision determines whether the current table is link
prediction or graph classification.

### 3. Protocol decisions use focused LLM context

[`backend/results_parser.py`](backend/results_parser.py) scanned the full paper
for strings such as `link prediction`, `all nodes`, `graph generation`, and
`domain adaptation`. LRGB is intrinsically multi-task, so these terms are
expected to occur even when the current result row is valid.

For example, the official LRGB paper contains valid rows for node
classification, graph classification, graph regression, and link prediction.
The same paper also naturally discusses all five tasks. A whole-paper scan
cannot identify which task a particular table row belongs to.

The per-dataset extraction call now receives the selected table body and
caption plus paragraphs that mention the dataset or reference the selected
table number/LaTeX label. It is instructed to distinguish unrelated task
mentions elsewhere from the task actually evaluated in the current table.

Each row receives an LLM decision: `standard`, `nonstandard`, or `uncertain`.
Only explicit `nonstandard` rows are excluded. `uncertain` rows are retained
and stored with `evaluation_task`, `protocol_decision`, and `protocol_note` for
review. Deterministic keywords no longer reject tables or rows.

### 4. Task detection was too eager and broad

The task gate had several independent ways to reject valid results:

- the table filter inferred link prediction from metric names, including AP;
- a table containing any link-prediction phrase could be discarded for a
  graph/node task even when the table mixed tasks or datasets;
- versioned extractions were required to provide both a matching
  `evaluation_task` and `uses_standard_protocol=true`; missing fields or an
  uncertain `false` value were treated as incompatibility;
- broad protocol markers such as `out-of-distribution`, `domain adaptation`,
  `backdoor attack`, and `graph generation` were treated as proof that the
  current row was noncanonical.

The loss distribution supports treating this as a high-recall extraction
failure rather than a narrow LRGB bug. Among historical rows belonging to
papers that now have no result rows, the largest benchmark groups were
`classic` (29,187 rows), `heterophilic-graphs` (11,316), `tu-dortmund` (7,983),
and `ogb` (4,296). The dominant task families were node classification (48,095
rows) and graph classification (12,001), not link prediction (182).

The task logic is now deliberately conservative:

- AP and other metric names are not task evidence;
- table selection is only a candidate step; selected tables are not rejected by
  keyword task filters;
- the LLM evaluates the table/caption/local experiment context per result row;
- explicit non-standard rows may be dropped, so papers can legitimately have
  fewer rows than the historical database;
- missing or ambiguous protocol fields become `uncertain` and are retained;
- complete coverage is required before stale rows can be deleted based on a
  reduced result set.

This does not make every extracted row canonical automatically. It shifts
uncertain cases from silent deletion to auditable extraction, where the dataset,
task, metric, table reference, and protocol note can be reviewed together.

### 5. Table-level filtering discarded mixed-task LRGB tables

The extractor selected tables per dataset, but then applied a deterministic
table-wide task filter. A table containing several metrics or multiple LRGB
tasks could be removed even when it contained valid rows for the requested
dataset.

The AP false positive has been removed. Selected tables now go directly to the
focused LLM extraction, where row-level task validation is authoritative.

### 6. Official LRGB paper control case

Historical database: 40 rows for arXiv:2206.08164, eight per dataset.

Current extraction artifact:

- 8 COCO-SP rows
- 8 PascalVOC-SP rows
- 8 PCQM-Contact rows
- 0 Peptides-func rows
- 0 Peptides-struct rows

The artifact itself says the Peptides tables were skipped because they appeared
to use a different task. The database retained only the PCQM-Contact rows.
This confirms that the loss occurred during the new extraction/filtering path,
not because the official paper lacks those results.

## Citation-focused findings

Semantic Scholar recorded 30 papers with `cited_by:2206.08164`. None currently
contributes LRGB rows, and the `papers.discovery_source` field remains mostly
`manual`; citation provenance is stored indirectly in `todo_papers.seen_from`.

The most important connected historical-result papers are:

- `2303.06147` — Exphormer
- `2305.08018` — DRew
- `2309.00367` — Where Did the Gap Go?
- `2205.12454` — Recipe for a General, Powerful, Scalable Graph Transformer
- `2212.13350` — A Generalization of ViT/MLP-Mixer to Graphs
- `2401.01233` — GEN
- `2412.01519` — ReHub
- `2502.09263` — Can Classic GNNs Be Strong Baselines
- `2501.17901` — Molecular fingerprints are strong models for peptide function prediction

These papers should be the first recovery cohort after the official benchmark
paper because they provide independent cross-checks of the benchmark tables.

## Implemented changes

- Removed the generic `AP` link-prediction heuristic.
- Restricted protocol backstops to explicit row-local task evidence.
- Made missing/uncertain protocol declarations non-fatal.
- Preserved existing rows for empty forced extractions.
- Completed candidate validation before any result-row mutation.
- Added tri-state LLM protocol decisions and focused table-reference context.
- Added persistent protocol metadata to result rows.
- Added the historical-loss re-evaluation list with 1,687 papers.
- Marked all 1,687 loss-cohort papers manually important and pending.
- Added full-paper loss counts to the audit command.
- Added a 50% minimum candidate coverage threshold before stale-row deletion.
- Retained overridden rows during replacement.
- Added LRGB task-filtering and protocol-regression tests.
- Added the read-only `scripts/audit_lrgb_regression.py` comparison command.

## Recovery plan

1. Run the 1,687-paper historical-loss queue with forced extraction.
2. Re-run targeted LRGB extraction for `2206.08164` using the known five-dataset
   manifest and exact table references.
3. Reparse the connected papers listed above after the filtering fix.
4. Compare every recovered row against historical values, current extraction
   artifacts, table references, and overrides.
5. Mark every historical row as recovered, replaced, intentionally excluded,
   or requiring manual review.
6. Only then merge validated rows into the current database and regenerate the
   Hugo export.

Do not restore the historical database wholesale: unrelated protocol cleanup
and newer papers must remain in the current version.

## Acceptance criteria

- The current database remains preserved until validated recovery is complete.
- The official LRGB paper has reviewed coverage for all five datasets.
- `Peptides-func` AP rows are not rejected as link prediction.
- A paper mentioning multiple tasks does not lose valid rows for unrelated tasks.
- Missing or ambiguous task metadata does not silently discard a result row.
- Explicitly non-standard experiments can be excluded and reduce row counts.
- Empty or partial forced extractions cannot silently erase published results.
- Candidate parsing completes before replacement mutates result rows.
- Every historical LRGB row has an explicit disposition.
- Citation-connected papers have been audited.
- Regression tests prevent recurrence.
