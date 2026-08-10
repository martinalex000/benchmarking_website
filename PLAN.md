# Plan: Graph Learning Benchmarking Website

## Overview

Static Hugo website with automated Python backend pipeline. Discovers graph learning papers via
(a) citation networks of benchmark papers (LRGB, GraphBench) and (b) a continuous ArXiv scanner.
Downloads papers, extracts results with a configurable LLM, and generates leaderboards with
trend charts. All manual corrections live in `overrides.yaml` text files tracked in git — the
database is never edited directly.

**Legend**: 🟢 NOW = implement in initial pass | 🔵 FUTURE = deferred

---

## Phase 0: Git & Project Structure [🟢 NOW]

1. Write `PLAN.md` as the very first file
2. `git init`, initial commit; all subsequent phases end with a `git commit`
3. Directory skeleton:
   ```
   benchmarking_website/
   ├── backend/           Python scripts
   ├── bin/               Local binaries (hugo, etc.)
   ├── config/
   │   ├── prompts/       LLM prompt templates
   │   ├── llm_config.yaml
   │   └── seed_data.yaml
   ├── data/              SQLite DB (gitignored)
   ├── papers/            Per-paper folders (selective gitignore)
   ├── site/              Hugo project
   ├── scripts/           Shell/CLI wrappers
   ├── tests/
   │   ├── unit/
   │   ├── integration/
   │   └── fixtures/
   └── logs/              gitignored
   ```
4. `.gitignore` — ignores PDFs, HTML downloads, DB files, logs; tracks overrides.yaml,
   metadata.json, results_human_readable.md per paper
5. `.env.example` — template for LLM endpoint and API key vars

---

## Phase 1: Database Schema [🟢 NOW]

Tables:
- **`benchmarks`** — id, name, short_name, paper_id (FK), description, url
- **`datasets`** — id, benchmark_id (FK), name, domain, task_type, default_metric,
  higher_is_better, num_graphs, avg_nodes, avg_edges, num_classes
- **`dataset_variants`** — id, dataset_id (FK), name, description, num_graphs, avg_nodes,
  label_fraction, split_type, `is_standard` (bool), notes
  → Handles Cora splits, ZINC full/subset, different label fractions, etc.
- **`papers`** — id, arxiv_id (UNIQUE), `arxiv_version`, title, authors (JSON), abstract,
  publication_date, pdf_path, html_path, main_figure_path, codebase_url,
  extraction_status, `extraction_model`, `discovery_source`, is_benchmark_paper
- **`models`** — id, name, `canonical_name`, paper_id (FK), `size_params`, model_type,
  is_baseline
- **`model_aliases`** — id, model_id (FK), alias (for fuzzy baseline grouping)
- **`results`** — id, paper_id, model_id, dataset_variant_id, metric_name, `metric_value`,
  **`metric_std`** (nullable), is_baseline, source_paper_id, `is_problematic`,
  `is_overridden`, `override_value`, `override_std`, `override_reason`, `override_source`
- **`pipeline_runs`** — audit trail per paper per stage

Files: `config/schema.sql`, `backend/models.py`, `backend/db.py`

---

## Phase 2: Python Environment & Config [🟢 NOW]

- `uv` project; `pyproject.toml` with all dependencies
- `config/llm_config.yaml` — three model tiers:
  - `primary: openai-gpt-oss120b` — full extraction
  - `fallback: minimax` — if primary insufficient
  - `small: gemma-3-27b` — cheap tasks (relevance checks)
- `backend/config.py` — loads `.env` + yaml; tier switchable via `--model` CLI flag

---

## Phase 3: Citation-Based Discovery [🟢 NOW]

`backend/citation_finder.py` — uses `scholarly` to find papers citing:
- LRGB: arXiv:2206.08164
- GraphBench: arXiv:2512.04475

Rate-limited, retry via `tenacity`. Persists to `papers` table.
CLI: `python -m backend.citation_finder --benchmark lrgb`

---

## Phase 4: ArXiv Scanner [🟢 NOW]

`backend/arxiv_scanner.py` — two-stage filtering:
1. **Stage 1 (cheap)** — `small_model` on title+abstract → `{is_graph_learning, confidence}`
2. **Stage 2 (deeper)** — `primary_model` on full metadata → `{has_benchmark_results, datasets_mentioned}`

CLI: `python -m backend.arxiv_scanner --days 7`
`--update-versions` flag: 🔵 FUTURE (see Phase 15)

---

## Phase 5: Paper Acquisition & Storage [🟢 NOW]

- `backend/paper_storage.py` — manages `papers/{arxiv_id}/` folder; auto-creates
  `metadata.json`; an `overrides.yaml` is created only when a paper needs a manual correction
- `backend/arxiv_downloader.py` — HTML preferred + PDF always downloaded (TikZ extraction);
  records `arxiv_version`
- `backend/alternative_downloader.py` — OpenReview/ACM/IEEE fallback

---

## Phase 6: Text & Figure Extraction [🟢 NOW]

- `backend/html_parser.py` — BeautifulSoup/lxml; text, tables as Markdown, figure captions
- `backend/pdf_parser.py` — PyMuPDF; two-column layout handling
- `backend/figure_extractor.py` — downloads/renders main figure; TikZ → 300dpi PNG from PDF

---

## Phase 7: LLM Extraction Pipeline [🟢 NOW]

Prompt templates (in `config/prompts/`):
- `result_extraction.txt` → JSON: `{models, results:[{model,dataset,metric,value,std,...}]}`
- `figure_detection.txt` → identify architecture diagram (not result plots)
- `baseline_identification.txt` → distinguish proposed model vs baselines
- `model_size.txt` → extract parameter counts

`backend/llm_extractor.py`:
- `LLMExtractor(model_tier='primary')` — switchable at runtime
- Chunked processing; Pydantic validation; retry on malformed JSON
- Saves: `extracted/llm_output.json` (raw), **`extracted/results_human_readable.md`** (tracked
  in git — primary human-verification artifact)

Human-readable format:
```markdown
# Extraction: {title}
Model: openai-gpt-oss120b | Date: 2026-05-07 | Confidence: HIGH

## Proposed: GraphGPS (6.9M params)
## Datasets: Peptides-func, Peptides-struct

### Peptides-func — AP ↑
| Model | AP | ±Std | Baseline? |
| GraphGPS | 0.6534 | 0.0042 | No |
| GCN | 0.5930 | 0.0023 | Yes |

## Extraction Notes
{LLM notes on ambiguous values, unclear tables}
```

---

## Phase 8: Override & Correction System [🟢 NOW]

`papers/{arxiv_id}/overrides.yaml` — optional manual corrections, **never overwritten by pipeline**:
```yaml
problematic_results:
  - model: GraphGPS
    dataset: Peptides-func
    metric: AP
    reason: "uses non-standard evaluation protocol"

result_overrides:
  - model: GraphGPS
    dataset: Peptides-func
    metric: AP
    correct_value: 0.6534
    correct_std: 0.0042
    reason: "LLM read wrong table row, see Table 3"

metadata_overrides:
  codebase_url: "https://github.com/example/repo"

dataset_split_notes:
  - dataset: Cora
    is_standard_split: false
    note: "random 10-fold split, not Planetoid public split"
```

- `backend/override_handler.py` — `load_overrides()`, `apply_overrides()`
- `backend/reapply_overrides.py` — re-apply all overrides without re-running LLM

---

## Phase 9: Results Parser & Baseline Aggregation [🟢 NOW]

- `backend/results_parser.py` — LLM JSON → DB records; fuzzy dataset variant resolution;
  handles mean±std strings; skips `is_overridden=True` records
- `backend/baseline_aggregator.py` — groups by `canonical_name` + aliases (`thefuzz`);
  computes min, max, mean, std-across-papers, count, earliest date, best-performing paper;
  exposes `get_baseline_summary(dataset_variant_id, metric_name)`

---

## Phase 10: Hugo Static Site [🟢 NOW]

`backend/export_to_hugo.py` — reads DB, generates:
- `site/content/datasets/{variant_slug}.md`
- `site/content/papers/{arxiv_id}.md`
- `site/content/leaderboards/{dataset_variant_slug}.md`

Hugo layouts:
- `layouts/papers/single.html` — paper with main figure, proposed results, baselines
- `layouts/datasets/single.html` — stats + leaderboard + chart
- `layouts/partials/result-table.html` — sortable table
- `layouts/partials/baseline-summary.html` — grouped baseline ranges

`site/static/js/leaderboard.js` — Chart.js best-over-time step chart:
- Step-function line (monotonically improving); model name label at each step
- All other dots with hover tooltip (model, paper, params, date)
- **Std toggle** — error bars on dots, ±std column in table
- **Table↔chart hover sync** — row hover highlights dot (yellow ring); dot hover highlights row
- Sortable columns; show/hide baselines toggle
- Color coding: problematic → grey; overridden → amber; best → green
- Dataset variant dropdown with non-standard-split warnings

---

## Phase 11: Pipeline Orchestration [🟢 NOW]

`backend/pipeline.py` — argparse CLI:
- Subcommands: `discover`, `download`, `extract [--model tier]`, `aggregate`, `export`,
  `build`, `run-all [--since date] [--force]`
- `rich` progress display; logs to `logs/YYYY-MM-DD.log`

`backend/pipeline_state.py` — `pipeline_runs` table; `should_process()` to skip unchanged;
max 3 retries with exponential backoff

---

## Phase 12: Automation Scripts [🟢 NOW]

- `python -m backend.pipeline run-all` — canonical batch pipeline entry point
- `scripts/process_papers.py` — direct paper processing and the live queue dashboard
- `scripts/deploy.py` — Hugo export/build and deployment entry point
- Cron should invoke `uv run python -m backend.pipeline run-all` from the repository root.

---

## Phase 13: Tests [🟢 NOW]

- `tests/unit/test_override_handler.py`
- `tests/unit/test_baseline_aggregator.py`
- `tests/unit/test_results_parser.py`
- `tests/unit/test_llm_extractor.py`
- `tests/unit/test_citation_finder.py`
- `tests/unit/test_arxiv_scanner.py`
- `tests/integration/test_full_pipeline.py`
- `tests/fixtures/` — sample HTML/PDF, mock LLM responses

---

## Phase 14: Initial Data Seeding [🟢 NOW]

`config/seed_data.yaml` — LRGB (5 datasets + variants), GraphBench, classic datasets
(Cora: Planetoid/random splits; ZINC: full/subset)

`backend/seed_db.py` — idempotent loader

---

## 🔵 FUTURE Phase 15: ArXiv Version Tracking

Schema supports it (`arxiv_version` column). Logic not yet implemented.
- `backend/version_checker.py` — detect new versions; re-download + re-extract;
  preserve all overrides

---

## 🔵 FUTURE Phase 16: User Feedback & Contributions

- Feedback button per result row → form with correct value + reason
- "Suggest a paper" form on Benchmarks page
- GitHub-based PR workflow for corrections

---

## 🔵 FUTURE Phase 17: Advanced UI

- Dataset variant side-by-side comparison
- Model family tree visualization
- Multi-dataset chart overlay
- RSS feed

---

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Hugo static site | Fast builds, works for large sites, simple Go templating |
| SQLite initially | Portable, no server overhead; schema portable to PostgreSQL |
| HTML ArXiv preferred | Better table structure vs PDF |
| PDF always downloaded | Needed for TikZ/vector figure extraction |
| `overrides.yaml` in git | Never overwritten; single source of truth for corrections |
| `results_human_readable.md` in git | Primary verification artifact; reviewable as diffs |
| Three LLM tiers | small=cheap relevance; primary=extraction; fallback=quality fallback |
| `dataset_variants` table | Handles all benchmark variant complexity without ambiguity |
| `metric_std` in results | Enables ± in table and error bars in chart |
| ArXiv scanner (NOW) | Finds newer papers not yet citing benchmark papers directly |
| Direct citations only | 2nd degree deferred |
| uv package manager | Modern, fast, good dependency resolution |
