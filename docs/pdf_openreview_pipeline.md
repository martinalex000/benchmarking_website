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
- [ ] Validate redirects before following them in the PDF downloader.
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

## Agent handoff: pipeline architecture

The intended end-to-end flow is:

```text
OpenReview venue discovery
  -> fast graph-paper prefilter
  -> local/Semantic Scholar/arXiv-snapshot resolution
  -> arXiv-first source plan
  -> isolated source staging
  -> Marker PDF-to-Markdown conversion (PDF-only branch)
  -> configured-dataset result extraction
  -> structural, numeric, and provenance validation
  -> processed-paper/result-fingerprint duplicate gate
  -> human-readable dry-run audit
  -> explicit persistence and site export
```

The first four stages and single-PDF staging exist. The experiment proves the PDF conversion and
Markdown-table adapter, but they are not yet promoted into the production pipeline. Batch plan
export/staging, production Marker invocation, evidence-linked candidate storage, result-based
deduplication, and audited persistence remain to be implemented.

### Current components and ownership

- `backend/openreview_client.py` fetches and normalizes OpenReview submissions. It supports API v2
  and the API-v1 fallback needed by legacy ICLR `Blind_Submission` invitations.
- `scripts/openreview_stats.py` is the read-only discovery and source-planning entry point. It
  applies the fast filter, compares local and Semantic Scholar records, optionally scans the local
  arXiv snapshot, constructs `SourceDecision` objects, and prints the dry-run plan.
- `backend/openreview_pdf.py` validates URLs and atomically stages one OpenReview PDF. It does not
  touch the database or queue.
- `scripts/stage_openreview_pdf.py` is the manual CLI around that single-file downloader.
- `experiments/marker_docling_bakeoff/` contains the selected converter evidence and the temporary
  Markdown-table/downstream-comparison tools. These are experiment code, not production APIs.
- `backend/paper_matching.py` supplies title normalization and author-overlap helpers used during
  source resolution. Reuse its normalization rather than introducing a second title matcher.
- `backend/results_parser.py`, `backend/extraction_validation.py`, and the existing result models
  are the integration points for dataset restriction, normalized result keys/values, and final
  validation. Inspect existing patterns before adding PDF-specific persistence.
- `scripts/seed_openreview_venue.py` is an older mutating queue path. Do not route this new pipeline
  through it until source resolution, duplicate gating, and dry-run auditing are complete.

### Implemented source-decision contract

`SourceDecision` currently contains `note_id`, `title`, `action`, `source_kind`, `venue_id`,
`arxiv_id`, `pdf_url`, and an explainable `evidence` string. Its actions are:

- `skip-processed`: a local title/ID match already has result rows.
- `queue-arxiv`: use an arXiv source found in OpenReview, the local DB, Semantic Scholar, or the
  exact-title snapshot resolver.
- `queue-pdf`: no arXiv source was found and an OpenReview PDF is available.
- `review`: at least one source matcher was ambiguous; do not download automatically.
- `unavailable`: neither an arXiv source nor a PDF is available.

Resolution precedence is encoded in `resolve_submission_sources()` and must remain arXiv-first:
processed local paper, OpenReview arXiv ID, local arXiv match, Semantic Scholar arXiv match, exact
snapshot match, ambiguity review, and only then OpenReview PDF. At present decisions exist only in
memory and terminal output; there is no exported plan or stable resume manifest.

### State and artifact boundaries

- `.cache/openreview_stats/` holds untracked atomic JSON caches. Each cache wraps `version`,
  `source`, `query`, `fetched_at`, and `data`. Snapshot-resolution cache keys include snapshot path,
  size, mtime, and the normalized candidate set.
- `.cache/openreview_pdf_staging/<safe-venue>/<safe-note-id>.pdf` is the staged PDF. Its adjacent
  JSON sidecar records `note_id`, `venue_id`, source/final URLs, path, size, timestamp, and whether
  an existing valid PDF was reused.
- `.cache/pdf-table-bakeoff/` contains ignored converter and comparison output from the experiment.
- `papers/<arxiv-id>/latex/expanded.tex` remains authoritative whenever an arXiv version exists.
- `data/benchmarks.db`, the processing queue, and generated site data are outside the discovery and
  staging boundary. No current PDF/OpenReview command is authorized to mutate them.

Future batch work should export an immutable JSONL plan before downloading. Each row should retain
all `SourceDecision` fields plus a plan version, generation timestamp, venue, filter category,
source-resolution evidence, and enough snapshot/cache identity to reproduce the decision. Batch
staging should consume only `queue-pdf` rows, checkpoint each outcome, and refuse `review` or
`unavailable` rows. This proposed manifest does not exist yet.

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

## Operator workflow and reproducible commands

Use `uv`, keep its cache outside the home directory, and run expensive scans/conversions at low
priority. OpenReview access requires `OPENREVIEW_TOKEN`; obtain a short-lived token without storing
the password by running:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/openreview_login.py
```

Run source preflight with the local arXiv metadata snapshot. The snapshot scan is expensive, so
keep `nice -6`; subsequent identical runs reuse the cache:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run python \
  scripts/openreview_stats.py \
  --venue-id NeurIPS.cc/2024/Conference \
  --s2-venue NeurIPS --s2-year 2024 \
  --resolve-arxiv-snapshot --no-kaggle-categories \
  --show-source-decisions 20
```

For the other validated venues, substitute these triples:

```text
ICLR.cc/2022/Conference                 ICLR                2022
logconference.io/LOG/2022/Conference   Learning on Graphs  2022
logconference.io/LOG/2023/Conference   Learning on Graphs  2023
logconference.io/LOG/2024/Conference   Learning on Graphs  2024
```

Use `--refresh-cache` only for an intentional live refresh. `--no-cache` avoids both reads and
writes. `--no-compare-s2` permits a local/OpenReview-only run when Semantic Scholar is unavailable,
but its resulting PDF count is less reliable. `--no-filter` reports all venue submissions and must
not be treated as the ingestion candidate set. The fast filter is only a discovery prefilter; the
configured-dataset restriction still has to be enforced during extraction.

Stage a single `queue-pdf` decision manually by copying its exact note ID, venue ID, and PDF URL
from the source-decision report:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run python \
  scripts/stage_openreview_pdf.py \
  --note-id oEKFPSOWpp \
  --venue-id NeurIPS.cc/2024/Conference \
  --pdf-url 'https://openreview.net/pdf?id=oEKFPSOWpp'
```

The downloader accepts only an initial HTTPS `openreview.net` URL, sends the bearer token when
configured, limits downloads to 200 MB, checks the `%PDF-` signature, writes through `.pdf.part`,
and atomically writes provenance JSON. `--force` re-downloads; otherwise an existing
signature-valid PDF is reused. It currently validates only the header, not full PDF parseability;
the live checks used an additional PDF parser manually.

Before batch use, harden redirect handling. The current `requests.get(..., allow_redirects=True)`
follows redirects and validates `response.url` afterward, so an off-host redirect is rejected only
after the request has occurred. Replace this with redirect-by-redirect validation or disabled
automatic redirects, and add a regression test. This is a known safety gap in
`backend/openreview_pdf.py`.

Convert a staged PDF with the selected Marker configuration:

```bash
nice -6 .cache/pdf-table-bakeoff-env/bin/marker_single \
  .cache/openreview_pdf_staging/NeurIPS.cc_2024_Conference/oEKFPSOWpp.pdf \
  --output_dir .cache/pdf_pipeline_markdown/oEKFPSOWpp \
  --mode fast \
  --ocr_equations false \
  --ocr_inline_math false \
  --disable_image_extraction \
  --output_format markdown
```

The bake-off environment is local experimental state, not a declared project dependency. A
production implementation must pin/install Marker through a deliberate dependency boundary and
record converter name, version, flags, source PDF checksum, output checksum, runtime, and errors in
the candidate provenance. Do not silently fall back to full OCR or Docling.

For an arXiv/PDF comparison, use the scripts and exact examples in
`experiments/marker_docling_bakeoff/RESULTS.md`. `compare_table_values.py` is deterministic;
`run_source_extraction.py` calls the configured LLM endpoint and may be rate-limited. Neither
script writes extracted results to the database.

## Verification map

Focused offline validation for the implemented components:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run pytest -q \
  tests/unit/test_openreview.py \
  tests/unit/test_openreview_stats.py \
  tests/unit/test_openreview_pdf.py \
  tests/unit/test_compare_pdf_table_values.py \
  tests/unit/test_pdf_source_extraction.py \
  tests/unit/test_compare_pdf_source_results.py

UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run ruff check \
  backend/openreview_client.py backend/openreview_pdf.py \
  scripts/openreview_stats.py scripts/stage_openreview_pdf.py \
  experiments/marker_docling_bakeoff
```

Normal tests must mock OpenReview and Semantic Scholar at shared request/fixture boundaries; they
must not depend on DNS, credentials, or live venue state. Live validation is an explicit manual
integration run and should record date, cache policy, venue ID, counts, and sampled note IDs here.
Preserve unrelated local changes to the LFS-backed `data/benchmarks.db` during validation.

## Recommended continuation slices

Keep each slice independently testable and retain a no-database-write path throughout:

1. **Export a source plan.** Add `--output-plan PATH` to `openreview_stats.py`, serialize a
   versioned JSONL manifest atomically, and test stable ordering, complete evidence, ambiguity
   preservation, and identical cached reruns. Do not download in this step.
2. **Batch-stage only PDFs from a plan.** Add a separate CLI that accepts the manifest, refuses
   non-`queue-pdf` actions, calls `stage_openreview_pdf()`, records per-row success/error/reuse, and
   resumes without repeating completed items. First harden redirect handling; then test
   interruption, off-host redirects, and corrupt/partial artifacts.
3. **Promote PDF-to-Markdown conversion.** Wrap Marker in a backend module with an explicit command
   builder, timeout, low-priority execution, version capture, checksums, atomic output, and a
   per-paper provenance record. Promote the Markdown table adapter from the experiment rather than
   importing experiment code in production.
4. **Stage extraction candidates with evidence.** Restrict extraction to datasets already
   configured in the database/config, attach table/caption/row/column evidence to every value, and
   reject collapsed rows, missing values, unknown datasets, unit ambiguity, and range failures.
   Produce an audit artifact; do not persist leaderboard rows.
5. **Implement the processed-paper fingerprint gate.** Compare normalized result multisets and
   emit an explainable match report using the thresholds below. Validate changed-title positives
   and common-baseline negatives before allowing automatic skips/merges.
6. **Run a dry ingestion audit.** Sample all three venue families, measure automatic acceptance,
   review, rejection, and suspected false-positive rates, and manually inspect evidence. Only then
   design the explicit database persistence step.

The safest immediate next task is slice 1. It creates the stable handoff between read-only
discovery and every later stage without committing to a storage schema or converter integration.

## Implementation sequence

1. Add a source-resolution record that keeps OpenReview note ID, venue, PDF URL, resolved arXiv ID,
   selected source kind, and resolution evidence. **Completed.**
2. Extend the read-only OpenReview discovery output with the source-resolution decision and dry-run
   download counts. **Completed:** the report now distinguishes processed, planned arXiv, planned
   OpenReview PDF, review-required, and unavailable records. Use `--show-source-decisions [N]` to
   inspect per-paper evidence without downloading anything.
3. Resolve provisional PDF candidates against the local arXiv metadata snapshot by normalized
   title, with ambiguity reported rather than guessed. **Completed.**
4. Add a staged downloader with content validation and atomic files. **Single-file atomic staging
   and idempotent reuse completed; batch resume remains pending.**
5. Export a stable, versioned source-plan manifest. **Not started; recommended next step.**
6. Add resumable batch staging driven only by approved manifest actions. **Not started.**
7. Promote the Markdown table adapter and Marker wrapper into tested backend modules.
8. Add table-structure checks and evidence-linked result staging.
9. Add the result-fingerprint matcher and an explainable match report.
10. Run extraction without database writes and manually audit a representative sample.
11. Enable persistence only for candidates that pass all automatic gates or receive explicit
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
- `c7869d8` — add arXiv-first read-only source planning.
- `220a59f` — handle relative OpenReview PDF paths.
- `bd7e769` — support legacy OpenReview API-v1 submissions.
- `6518b01` — add exact-title local arXiv snapshot resolution.
- `1ae63b2` — add validated, atomic single-PDF staging.
- `71009d2` — consolidate Marker/Docling evidence and select Marker.

The current source resolver lives in `scripts/openreview_stats.py`. Ambiguous local or Semantic
Scholar matches block automatic PDF selection, even when an OpenReview PDF URL is present.

## Open questions

- Whether the staged downloader should use a new PDF-only candidate table or extend the existing
  paper candidate representation.
- The exact minimum fingerprint evidence for papers containing only one configured dataset.
- Whether the exported source plan should embed all OpenReview metadata or retain only the fields
  required for reproducible source selection and staging.
- Which PDF candidate/evidence records should be persistent database entities versus immutable
  audit files. Do not decide this before the dry extraction artifact is understood.
- Docling remains manual diagnostic tooling. Automatic fallback is out of scope until structural
  quality can be measured reliably enough to prevent row-association errors.
