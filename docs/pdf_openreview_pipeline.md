# PDF/OpenReview Pipeline Plan

Last updated: 2026-08-12

## Goal

Ingest relevant OpenReview papers that have no usable arXiv version while preserving the
existing preference for authoritative local LaTeX. Only configured benchmark datasets are in
scope. The pipeline must favor precision over coverage: uncertain results are staged for review
and never written directly to the leaderboard.

## Current status

- [x] Build an isolated CPU-only Marker/Docling evaluation environment.
- [x] Compare Marker fast, Marker with OCR disabled, and Marker with formula OCR disabled while
  retaining table fallback.
- [x] Compare Docling accurate table mode with OCR disabled.
- [x] Evaluate six local papers with both PDF and authoritative LaTeX sources.
- [x] Add deterministic table-value and downstream extraction comparison tools.
- [x] Add a Markdown pipe-table adapter for the existing extraction pipeline.
- [x] Select the initial PDF backend and settings.
- [ ] Implement source resolution and staged OpenReview PDF downloads.
- [ ] Implement result-based processed-paper detection.
- [ ] Implement PDF extraction as a first-class, staged pipeline source.
- [ ] Test venue discovery and downloads on NeurIPS 2024, ICLR 2022, and LoG venues.
- [ ] Run a dry ingestion audit before enabling database writes.
- [ ] Ingest approved PDF-only papers.

## Source preference

Use this order for every candidate:

1. Existing local arXiv LaTeX source.
2. Newly resolved arXiv source, when OpenReview metadata or external metadata provides an ID.
3. OpenReview PDF only when no usable arXiv version can be resolved.

Never process both the arXiv and OpenReview representations as separate papers. Source
resolution and duplicate gating must happen before a paper enters the extraction queue.

## PDF backend decision

Use Marker fast mode with equation and inline-math OCR disabled, while keeping table fallback
enabled. Conceptually, the relevant options are:

```text
--mode fast
--ocr_equations false
--ocr_inline_math false
--disable_image_extraction
--output_format markdown
```

Do not use `--disable_ocr` for production: it also removes table fallback. Do not use full OCR by
default: it was dramatically slower and provided little useful table improvement.

Keep Docling accurate/no-OCR available as a diagnostic fallback, not as the default. Docling
retained slightly more numeric content but repeatedly merged multiple model rows into one
Markdown row or cell. That damages method-to-value association and is unsafe for a
precision-first leaderboard.

All heavyweight local commands, including conversion, installation, and batch extraction, must
run with `nice -6`.

## Evaluation evidence

The six-paper cohort was:

- `2205.12454`
- `2305.08018`
- `2405.16435`
- `2110.14446`
- `2305.18407`
- `2502.09263`

The added papers contributed 47 LaTeX reference tables and included dense and layout-heavy
cases.

Across the five papers without the shared pathological numeric-comparison case:

- Marker: 92.2% numeric recall and 97.0% numeric precision.
- Docling: 93.4% numeric recall and 97.2% numeric precision.

Across all six Markdown outputs:

- Marker preserved 1,093 table data rows.
- Docling preserved 813 table data rows.
- Marker detected 82 pipe tables; Docling detected 83.

Docling collapsed rows on every paper, severely on five of six. Marker was generally two to five
times faster and used roughly half the peak memory.

The downstream extraction comparison also showed why numeric recall alone is insufficient:

- On `2305.08018`, Docling matched 92.1% of strict LaTeX result keys and 94.7% under relaxed
  method-name matching, with no matching-key value errors. Marker matched 44.7% and exposed 18
  value mismatches, largely from missed QM9 unit scaling.
- On `2405.16435`, Marker achieved 60.9% strict recall with no matching-key value errors. Docling
  achieved 52.2% strict recall with two value errors caused by collapsed baseline/proposed-model
  rows. Relaxed recall was 69.6% for both.
- A third semantic case on `2305.18407` was incomplete because the configured endpoint hit its
  token rate limit and timeout. Its partial output must not be used for backend comparison.

These measurements are bake-off evidence, not ingestion acceptance criteria. Generated artifacts
are stored under the ignored `.cache/pdf-table-bakeoff/` directory.

## Extraction safety gates

PDF-derived output must be staged before persistence. A candidate result is eligible for review
only when all of the following hold:

- The dataset resolves to the configured benchmark allow-list.
- The numeric value is present in a selected Markdown table.
- Dataset, metric, method row, and value column can be associated without a merged-row ambiguity.
- Metric direction, units, and plausible range pass existing validation.
- The source table and caption are retained as evidence.
- The extraction does not show suspicious row collapsing or multiple method names in one row key.

Low-confidence, structurally ambiguous, unit-ambiguous, or unmatched rows must be rejected or sent
to manual review. They must not be accepted merely because an LLM produced valid output syntax.

## Processed-paper gate

Resolve possible duplicates in stages:

1. Exact arXiv ID or stable external identifier: automatic match.
2. Strong normalized title and author match: automatic match when unambiguous.
3. Result fingerprint: compare normalized `(dataset variant, metric, value)` multisets, preserving
   duplicate occurrences.
4. Model-aware result agreement and proposed-method-name similarity: strong supporting signals,
   but not mandatory because method extraction is brittle.
5. Ambiguous matches: manual review; never automatically merge two existing papers.

For an automatic result-fingerprint match, start with conservative requirements:

- At least 90% bidirectional result agreement.
- At least six matching values.
- Evidence across at least two datasets or four distinct dataset/metric groups.
- Values compared with metric-appropriate tolerances after unit normalization.
- No contradictory result group with the same dataset/metric but materially different values.

Title similarity, author overlap, and proposed-method similarity should raise confidence. Exact or
near-exact result agreement may still match changed titles without a method-name match. Common
baseline values alone must not be sufficient.

## Download and venue test plan

Implement the downloader behind a dry-run/staging boundary and test one venue at a time:

1. NeurIPS 2024.
2. ICLR 2022.
3. Confirm available LoG venue identifiers, then test each selected LoG conference.

For each venue, report before downloading:

- Total submissions and unique OpenReview note IDs.
- arXiv coverage and PDF-only candidates.
- Candidates already matched locally by ID, title/authors, or result fingerprint.
- Candidates passing the configured dataset prefilter.
- Planned arXiv downloads versus planned OpenReview PDF downloads.
- Ambiguous records requiring review.

Download into a staging directory first. Test pagination, retries, size/content-type validation,
partial-download cleanup, idempotency, and resume behavior. Network-facing tests should use mocked
fixture boundaries in the normal test suite; live venue checks are explicit integration runs.

## Implementation sequence

1. Add a source-resolution record that keeps OpenReview note ID, venue, PDF URL, resolved arXiv ID,
   selected source kind, and resolution evidence.
2. Extend the read-only OpenReview discovery output with the source-resolution decision and dry-run
   download counts.
3. Add a staged downloader with content validation and resumable, atomic files.
4. Promote the Markdown table adapter from the experiment into a tested backend module.
5. Add table-structure checks and evidence-linked result staging.
6. Add the result-fingerprint matcher and an explainable match report.
7. Run the three venue tests and inspect false matches and missed matches.
8. Run extraction without database writes and manually audit a representative sample.
9. Enable persistence only for candidates that pass all automatic gates or receive explicit
   approval.

## Existing experiment tooling

- `experiments/pdf_extraction/compare_table_values.py`: deterministic LaTeX/Markdown numeric
  pre-screen.
- `experiments/pdf_extraction/run_source_extraction.py`: restricted downstream extraction over
  LaTeX or parsed Markdown tables.
- `experiments/pdf_extraction/compare_source_results.py`: strict and relaxed comparison of
  downstream result rows.

Relevant commits:

- `cf09b1b` — add the PDF extraction bake-off harness.
- `e54ef4e` — parse PDF Markdown tables for extraction comparison.

## Open questions

- Whether the staged downloader should use a new PDF-only candidate table or extend the existing
  paper candidate representation.
- The exact minimum fingerprint evidence for papers containing only one configured dataset.
- Whether Docling should be invoked automatically after a Marker structural-quality failure or
  remain a manual diagnostic tool.
- Which LoG years and OpenReview venue IDs should be included in the first live download test.
