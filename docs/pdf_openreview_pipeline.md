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
- [x] Implement read-only, arXiv-first source resolution and dry-run action counts.
- [x] Resolve exact normalized titles against the local arXiv metadata snapshot.
- [x] Implement validated, atomic single-PDF staging and test representative venues.
- [ ] Add batch staging driven directly by an exported source plan.
- [ ] Implement result-based processed-paper detection.
- [ ] Implement PDF extraction as a first-class, staged pipeline source.
- [x] Test read-only source planning on NeurIPS 2024.
- [x] Test read-only source planning on ICLR 2022.
- [x] Test read-only source planning on LoG 2022, 2023, and 2024.
- [x] Test one staged download from NeurIPS 2024, ICLR 2022, and LoG 2022.
- [ ] Test batch staging, interruption, and resume behavior.
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

### Live validation log

NeurIPS 2024 source planning completed on 2026-08-12 using cached OpenReview and Semantic Scholar
responses and the current fast prefilter:

- 4,236 OpenReview submissions.
- 519 fast-filter hits: 192 specific and 327 unspecific graph matches.
- 35 already processed locally with results.
- 310 planned arXiv sources.
- 174 planned OpenReview PDF sources.
- No ambiguous or unavailable source decisions in this run.

These are discovery-stage counts, not final benchmark eligibility. Extraction remains restricted to
the configured dataset allow-list. The first live detail report also found and fixed handling of
relative OpenReview PDF paths in Rich terminal output; no papers were downloaded.

ICLR 2022 source planning completed on 2026-08-12 after adding an authenticated API-v1 fallback
for legacy `Blind_Submission` invitations:

- 2,617 OpenReview submissions.
- 324 fast-filter hits: 193 specific and 131 unspecific graph matches.
- 24 already processed locally with results.
- 60 planned arXiv sources.
- 240 planned OpenReview PDF sources.
- No ambiguous or unavailable source decisions in this run.

The initial API-v2-only query incorrectly returned zero submissions. Semantic Scholar matched only
76 of the 324 filter hits, so an additional arXiv-resolution route should be evaluated before
accepting all 240 records as genuinely PDF-only. No papers were downloaded.

LoG source planning completed for all available conference years on 2026-08-12:

- LoG 2022: 84 submissions; 81 filter hits; 5 processed; 12 arXiv recovered locally; 63
  provisionally PDF-only; 1 unavailable.
- LoG 2023: 70 submissions; 61 filter hits; 8 processed; 7 arXiv recovered locally; 46
  provisionally PDF-only.
- LoG 2024: 75 submissions; 72 filter hits; 10 processed; 3 arXiv recovered locally; 59
  provisionally PDF-only.

Semantic Scholar's `Learning on Graphs` venue/year bulk query returned no candidates for any of
the three years. Therefore, these PDF counts are explicitly provisional. Add a local arXiv
metadata title resolver before staged download testing so that available arXiv sources are not
missed. No papers were downloaded.

The exact-title arXiv snapshot resolver was subsequently applied. It does not fuzzy-guess and
reports duplicate-title ambiguity instead of selecting a source. Final source-preflight counts are:

- NeurIPS 2024: 35 processed, 361 planned arXiv, 123 planned PDF, 0 ambiguous.
- ICLR 2022: 24 processed, 154 planned arXiv, 145 planned PDF, 1 ambiguous.
- LoG 2022: 5 processed, 53 planned arXiv, 23 planned PDF, 0 ambiguous.
- LoG 2023: 8 processed, 35 planned arXiv, 18 planned PDF, 0 ambiguous.
- LoG 2024: 10 processed, 40 planned arXiv, 22 planned PDF, 0 ambiguous.

Snapshot resolution is opt-in through `--resolve-arxiv-snapshot` because it streams the 5.4 GB
metadata file. Results are cached by snapshot identity and candidate set. Use
`--no-kaggle-categories` during source preflight to avoid a second optional metadata scan.

### Staged download validation

The isolated downloader was tested live on 2026-08-12. It accepts only HTTPS OpenReview hosts,
uses the configured bearer token, enforces a 200 MB limit, validates the `%PDF-` signature, writes
through a `.part` file, records sidecar provenance, and reuses an existing valid PDF.

- NeurIPS 2024 `oEKFPSOWpp`: 15,651,340 bytes, 23 pages.
- ICLR 2022 `2RNpZ8S4alJ`: 6,275,713 bytes, 15 pages.
- LoG 2022 `oqf2GRYTET`: 312,453 bytes, 8 pages.

All three parsed successfully as PDF 1.5 and no partial files remained. Repeating the NeurIPS
command exercised the idempotent reuse path. The first anonymous request received HTTP 403 and
left no staged file; authenticated access was then added and tested. Artifacts remain ignored
under `.cache/openreview_pdf_staging/` and no queue or database rows were changed.

## Implementation sequence

1. Add a source-resolution record that keeps OpenReview note ID, venue, PDF URL, resolved arXiv ID,
   selected source kind, and resolution evidence. **Completed.**
2. Extend the read-only OpenReview discovery output with the source-resolution decision and dry-run
   download counts. **Completed:** the report now distinguishes processed, planned arXiv, planned
   OpenReview PDF, review-required, and unavailable records. Use `--show-source-decisions [N]` to
   inspect per-paper evidence without downloading anything.
3. Resolve provisional PDF candidates against the local arXiv metadata snapshot by normalized
   title, with ambiguity reported rather than guessed. **Completed.**
4. Add a staged downloader with content validation and resumable, atomic files. **Single-file
   atomic staging and idempotent reuse completed; batch resume remains pending.**
5. Promote the Markdown table adapter from the experiment into a tested backend module.
6. Add table-structure checks and evidence-linked result staging.
7. Add the result-fingerprint matcher and an explainable match report.
8. Run the three venue tests and inspect false matches and missed matches.
9. Run extraction without database writes and manually audit a representative sample.
10. Enable persistence only for candidates that pass all automatic gates or receive explicit
   approval.

## Existing experiment tooling

- `experiments/marker_docling_bakeoff/compare_table_values.py`: deterministic LaTeX/Markdown numeric
  pre-screen.
- `experiments/marker_docling_bakeoff/run_source_extraction.py`: restricted downstream extraction over
  LaTeX or parsed Markdown tables.
- `experiments/marker_docling_bakeoff/compare_source_results.py`: strict and relaxed comparison of
  downstream result rows.
- `experiments/marker_docling_bakeoff/RESULTS.md`: reproducible configurations, measurements,
  limitations, and the backend decision.

Relevant commits:

- `cf09b1b` — add the PDF extraction bake-off harness.
- `e54ef4e` — parse PDF Markdown tables for extraction comparison.

The current source resolver lives in `scripts/openreview_stats.py`. Ambiguous local or Semantic
Scholar matches block automatic PDF selection, even when an OpenReview PDF URL is present.

## Open questions

- Whether the staged downloader should use a new PDF-only candidate table or extend the existing
  paper candidate representation.
- The exact minimum fingerprint evidence for papers containing only one configured dataset.
- Whether Docling should be invoked automatically after a Marker structural-quality failure or
  remain a manual diagnostic tool.
- Which LoG years and OpenReview venue IDs should be included in the first live download test.
