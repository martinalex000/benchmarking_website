# Marker vs. Docling PDF table extraction bake-off

Date: 2026-08-12

## Decision

Use **Marker fast mode with equation and inline-math OCR disabled, while retaining table
fallback**. This is the selected PDF-to-Markdown backend for papers without a usable arXiv
version:

```text
--mode fast
--ocr_equations false
--ocr_inline_math false
--disable_image_extraction
--output_format markdown
```

This is intentionally not Marker's `--disable_ocr` option: that option also disables table
fallback. Docling accurate table mode with OCR disabled remains a manual diagnostic fallback.
Heavy commands must run at low priority with `nice -6`.

The choice prioritizes faithful method-row-to-value association over a small increase in raw
numeric recall. That is the safer trade-off for a precision-first leaderboard.

## Tested configurations

- Marker 2.0.0, fast mode, full OCR disabled.
- Marker 2.0.0, fast mode, equation and inline-math OCR disabled, table fallback retained.
- Marker 2.0.0, fast mode, default OCR behavior.
- Docling 2.119.0, accurate table mode, OCR disabled.

The converters ran in the isolated CPU-only environment
`.cache/pdf-table-bakeoff-env`. Generated PDFs, Markdown, timing logs, and downstream JSON are
ignored under `.cache/pdf-table-bakeoff/` and are not required by the test suite.

## Evaluation cohort

Each paper had a local PDF and authoritative `papers/<arxiv-id>/latex/expanded.tex` source:

- `2205.12454`
- `2305.08018`
- `2405.16435`
- `2110.14446`
- `2305.18407`
- `2502.09263`

The expanded cohort contained 47 LaTeX reference tables and included dense and layout-heavy
cases.

## Deterministic table-value evidence

The numeric comparison treats normalized number occurrences in parsed LaTeX tables as the
reference. It is a cheap structural pre-screen, not a semantic correctness metric.

| Paper | Marker tables | Marker values | Marker recall | Marker precision | Docling tables | Docling values | Docling recall | Docling precision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `2205.12454` | 18/17 | 1096/1251 | 87.6% | 97.2% | 18/17 | 1096/1251 | 87.6% | 97.2% |
| `2305.08018` | 4/4 | 472/474 | 99.6% | 99.8% | 4/4 | 472/474 | 99.6% | 99.8% |
| `2405.16435` | 13/14 | 1330/1407 | 94.5% | 99.8% | 14/14 | 1348/1407 | 95.8% | 99.0% |
| `2110.14446` | 11/11 | 331/825 | 40.1% | 28.0% | 11/11 | 331/825 | 40.1% | 28.0% |
| `2305.18407` | 19/19 | 1127/1284 | 87.8% | 96.5% | 19/19 | 1186/1284 | 92.4% | 97.9% |
| `2502.09263` | 17/17 | 1725/1819 | 94.8% | 94.5% | 17/17 | 1719/1819 | 94.5% | 94.7% |

The values column is `matched/reference`; precision additionally accounts for all candidate
values. `2110.14446` is a shared pathological case for this metric: both converters produced
1,184 candidate values against 825 LaTeX values, so it is excluded from the aggregate below.

Across the other five papers:

- Marker: 92.2% recall and 97.0% precision.
- Docling: 93.4% recall and 97.2% precision.

## Row structure, runtime, and memory

Across all six outputs, Marker emitted 82 pipe tables with 1,093 data rows; Docling emitted 83
pipe tables with 813 data rows. Docling collapsed multiple model rows on every paper and did so
severely on five of six papers. This is the key safety concern: values may survive while their
association with the correct method does not.

Selected expanded-cohort measurements:

| Paper | Marker time | Marker max RSS | Docling time | Docling max RSS |
| --- | ---: | ---: | ---: | ---: |
| `2110.14446` | 34.12 s | 1,072,268 KB | 115.44 s | 2,451,964 KB |
| `2305.18407` | 107.13 s | 1,307,888 KB | 149.63 s | 2,363,164 KB |
| `2502.09263` | 33.68 s | 1,070,720 KB | 176.13 s | 3,001,120 KB |

Marker was generally two to five times faster and used roughly half the peak memory. Full Marker
OCR was not worthwhile: on `2205.12454` it took 595.3 seconds versus about 12 seconds without OCR,
while recall changed from 87.6% to 88.3% and precision fell from 97.2% to 95.8%. The default OCR
run on `2405.16435` was stopped after more than 12 minutes because formula OCR dominated runtime.

## Downstream semantic evidence

The same restricted benchmark-result extractor was run on authoritative LaTeX and each Markdown
candidate. This probes whether dataset, metric, method, and value remain associated.

- `2305.08018`, restricted to Peptides-func and QM9: Marker had 44.7% strict and relaxed recall,
  with 18 matching-key value mismatches, largely due to missed QM9 unit scaling. Docling had 92.1%
  strict recall, 94.7% relaxed recall, and no matching-key value mismatches.
- `2405.16435`, restricted to Cora and Tox21: Marker had 60.9% strict recall, 69.6% relaxed recall,
  and no matching-key value mismatches. Docling had 52.2% strict recall, 69.6% relaxed recall, and
  two value mismatches caused by collapsed baseline/proposed-model rows.
- `2305.18407` was incomplete because the configured LLM endpoint hit token-rate limits and a
  timeout. Its partial output is excluded from the backend decision.

Candidate precision against the LaTeX extraction is not a true false-positive rate because the
LaTeX extraction itself may omit valid results. The manual row-structure audit and matching-key
value errors therefore carry more weight than candidate-row counts alone.

## Reproduction

Run all heavyweight commands with `nice -6`. Converter CLIs may vary across versions, so confirm
their help output before repeating the experiment.

```bash
nice -6 .cache/pdf-table-bakeoff-env/bin/marker_single \
  papers/2305.08018/paper.pdf \
  --output_dir .cache/pdf-table-bakeoff/marker-table-fallback \
  --mode fast \
  --ocr_equations false \
  --ocr_inline_math false \
  --disable_image_extraction \
  --output_format markdown
```

```bash
nice -6 .cache/pdf-table-bakeoff-env/bin/docling \
  convert \
  papers/2305.08018/paper.pdf \
  --to md \
  --output .cache/pdf-table-bakeoff/docling-no-ocr \
  --no-ocr \
  --table-mode accurate
```

Compare table values against local LaTeX:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run python \
  experiments/marker_docling_bakeoff/compare_table_values.py \
  2305.08018 .cache/pdf-table-bakeoff/marker-table-fallback/paper/paper.md
```

Run restricted extraction once for LaTeX and once for converter Markdown:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run python \
  experiments/marker_docling_bakeoff/run_source_extraction.py \
  2305.08018 --datasets Peptides-func QM9 \
  --output .cache/pdf-table-bakeoff/results/2305.08018-latex.json

UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run python \
  experiments/marker_docling_bakeoff/run_source_extraction.py \
  2305.08018 --datasets Peptides-func QM9 \
  --markdown .cache/pdf-table-bakeoff/marker-table-fallback/paper/paper.md \
  --output .cache/pdf-table-bakeoff/results/2305.08018-marker.json
```

Compare semantic outputs:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache nice -6 uv run python \
  experiments/marker_docling_bakeoff/compare_source_results.py \
  .cache/pdf-table-bakeoff/results/2305.08018-latex.json \
  .cache/pdf-table-bakeoff/results/2305.08018-marker.json
```

## Included scripts

- `compare_table_values.py`: deterministic normalized-number comparison between LaTeX and
  Markdown tables.
- `run_source_extraction.py`: restricted extraction over either authoritative LaTeX or parsed
  Markdown tables.
- `compare_source_results.py`: strict and method-name-relaxed comparison of extracted result
  rows.

These measurements select a converter; they are not ingestion acceptance criteria. PDF-derived
results must still pass the configured-dataset allow-list, structural ambiguity checks, unit and
range validation, duplicate gating, and evidence review before leaderboard persistence.
