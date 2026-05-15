# Graph Learning Benchmarking Website

A self-hosted static website that tracks and visualises state-of-the-art results
across graph learning benchmarks. Papers are discovered automatically or added
manually; an LLM pipeline extracts benchmark results; human corrections are applied
through `overrides.yaml` files per paper.

---

## Quick start

```bash
git clone <repo-url>
cd benchmarking_website

# Copy the env template and fill in your LLM credentials
cp .env.example .env
$EDITOR .env

# Install all dependencies (Python 3.12+, uv required)
uv sync --group dev

# Seed the database with benchmark/dataset definitions
uv run python -m backend.seed_db

# Process your first paper
uv run python scripts/run_manual.py 2206.08164
```

---

## LLM configuration

The pipeline uses an **OpenAI-compatible** API endpoint.

### `.env` — secrets (never commit this file)

| Variable | Required | Description |
|---|---|---|
| `LLM_ENDPOINT` | **yes** | Base URL, e.g. `https://api.example.com/v1` |
| `LLM_API_KEY` | **yes** | API key for that endpoint |
| `LLM_MODEL_PRIMARY` | no | Override primary model (default from `llm_config.yaml`) |
| `LLM_MODEL_FALLBACK` | no | Override fallback model |
| `LLM_MODEL_SMALL` | no | Override small/cheap model used for screening |

### `config/llm_config.yaml` — non-secret model settings

Default model names, temperature, token limits, and retry config.
`.env` values override the YAML when both are set.

### Verify your endpoint

```bash
# List all models the endpoint serves and check your configured tiers
uv run python scripts/list_models.py

# Point at a different endpoint
uv run python scripts/list_models.py --endpoint https://api.example.com/v1 --api-key sk-xxx
```

---

## Main scripts

### `scripts/run_manual.py` — process a single paper

The primary interactive tool. Downloads, extracts, stores, and exports one paper.
Prints live progress for every LLM call (call type, input/output size, TTFT,
tok/s, discovered datasets, and tables selected).

```bash
# Basic: download + extract + store + export
uv run python scripts/run_manual.py 2206.08164

# Full arXiv URL also works
uv run python scripts/run_manual.py https://arxiv.org/abs/2206.08164

# Re-run extraction only (keep existing download)
uv run python scripts/run_manual.py 2206.08164 --skip-download --force

# Skip the abstract screening step and go straight to full extraction
uv run python scripts/run_manual.py 2206.08164 --skip-screen

# Use a different model tier
uv run python scripts/run_manual.py 2206.08164 --model fallback
uv run python scripts/run_manual.py 2206.08164 --model small

# Legacy single-shot extraction (no dataset discovery step)
uv run python scripts/run_manual.py 2206.08164 --oneshot

# Run all three model tiers and compare their outputs side by side
uv run python scripts/run_manual.py 2206.08164 --compare-models

# Re-download everything and re-extract
uv run python scripts/run_manual.py 2206.08164 --force-download

# Skip extraction and only re-parse + export (after manual override edits)
uv run python scripts/run_manual.py 2206.08164 --skip-download --skip-extract
```

If extraction fails, an `errors.log` entry and a full Markdown conversation log
(`extraction_error_<timestamp>.md`) are written to `papers/<id>/extracted/`.

---

### `scripts/find_citing_papers.py` — discover papers that cite a benchmark

Queries Semantic Scholar for all papers that cite a given arXiv paper, shows
their processing status in the local DB, and lets you interactively queue them
for processing via `run_manual.py`.

```bash
# Find papers citing the LRGB benchmark paper
uv run python scripts/find_citing_papers.py 2206.08164

# Limit to the 50 most recent citations
uv run python scripts/find_citing_papers.py 2206.08164 --limit 50

# Include papers already tracked in the DB
uv run python scripts/find_citing_papers.py 2206.08164 --show-all
```

Set `S2_API_KEY` in your environment to avoid Semantic Scholar rate limits.

---

### `scripts/compare_models.py` — benchmark LLM extraction quality

Runs every available model on papers that have a known-good baseline extraction
and measures hits, misses, value errors, and hallucination rate. Outputs a rich
recall/precision summary per model.

```bash
# Run all models on all papers with a baseline
uv run python scripts/compare_models.py

# Limit to specific papers or models
uv run python scripts/compare_models.py --paper 2206.08164 2309.00367
uv run python scripts/compare_models.py --model gemma-3-27b-it qwen3.5-27b

# Skip slow or irrelevant models
uv run python scripts/compare_models.py --skip-model teuken-7b-instruct-research

# Save detailed results + full conversation logs
uv run python scripts/compare_models.py \
    --output experiments/comparison.json \
    --log-dir experiments/logs
```

---

### `scripts/set_dataset_stats.py` — update dataset statistics in the DB

Writes graph count, node/edge counts, and class counts for LRGB and OGB
datasets into the database. Run once after seeding, or when metadata changes.

```bash
uv run python scripts/set_dataset_stats.py

# Also re-export Hugo content immediately after
uv run python scripts/set_dataset_stats.py --export
```

---

### `scripts/list_models.py` — check available models at your endpoint

```bash
uv run python scripts/list_models.py
```

Prints all model IDs from `GET /v1/models` and marks which configured tiers
(primary / fallback / small) are present. Exits 1 if any are missing.

---

## Corrections and overrides

Results are never edited in the database directly. Create or edit
`papers/<id>/overrides.yaml` to correct extraction errors. This file is never
overwritten by the pipeline.

```yaml
# papers/2206.08164/overrides.yaml
paper_arxiv_id: "2206.08164"

result_overrides:
  - model: "GraphGPS"
    dataset: "Peptides-func"
    metric: "AP"
    correct_value: 0.6534
    correct_std: 0.0042
    reason: "LLM read wrong table row — see Table 3"

metadata_overrides:
  codebase_url: "https://github.com/example/repo"
```

After editing, re-apply overrides and re-export:

```bash
# One paper
uv run python -m backend.reapply_overrides --paper 2206.08164

# All papers, then re-export
uv run python -m backend.reapply_overrides
uv run python -m backend.export_to_hugo
```

### Dataset-level display overrides (website presentation)

Dataset page presentation overrides are configured in:

`config/dataset_overrides.yaml`

Use this file to control which metric columns are shown on dataset detail pages.

```yaml
datasets:
  Texas:
    display_metrics: ["Accuracy"]
```

After editing this file, re-export and rebuild:

```bash
uv run python -m backend.export_to_hugo
cd site && /snap/bin/hugo --minify
```

This is dataset-level (not paper-level), and affects all dataset pages for that dataset.

---

## Editing dataset descriptive text

Dataset descriptions shown on the website are sourced from the database field `Dataset.description`.

Primary edit location:

- `config/seed_data.yaml` (benchmark and dataset definitions, including `description`)

How to apply description changes:

```bash
# if you changed seeded benchmark/dataset metadata
uv run python -m backend.seed_db

# regenerate Hugo content and static site
uv run python -m backend.export_to_hugo
cd site && /snap/bin/hugo --minify
```

If you only need to adjust website presentation (not DB semantic metadata), prefer `config/dataset_overrides.yaml` for display-only controls such as `display_metrics`.

---

## Statistics on landing page vs datasets page

The two pages use different aggregation paths, so counts can differ:

- Landing page: aggregates from `site/data/benchmarks.json` (raw DB-oriented counts with problematic rows excluded).
- Datasets overview: aggregates from exported dataset pages in `site/content/datasets/` (deduplicated leaderboard rows and exported-page scope).

For user-facing leaderboard presentation, the datasets-overview counts are typically the more conservative numbers.
See Development page: `Development -> Statistics Sources & Discrepancies`.

---

## Local preview

```bash
cd site && /snap/bin/hugo server --bind 0.0.0.0 -p 1313
# Open http://localhost:1313
```

---

## Bulk pipeline (automated processing)

For batch processing, all stages are sub-commands of `backend.pipeline`:

```bash
# Full end-to-end run
uv run python -m backend.pipeline run-all

# Individual stages
uv run python -m backend.pipeline discover    # scan arXiv + citations for new papers
uv run python -m backend.pipeline download    # fetch PDFs + HTML
uv run python -m backend.pipeline extract     # LLM extraction (quiet/batch mode)
uv run python -m backend.pipeline parse       # write LLM output to SQLite
uv run python -m backend.pipeline aggregate   # compute leaderboard aggregates
uv run python -m backend.pipeline export      # write Hugo markdown + data files
uv run python -m backend.pipeline build       # run Hugo static site generator
```

Batch extraction runs with `verbose=False`. Use `run_manual.py` for interactive
extraction with live call-by-call progress output.

---

## Deployment

Set `DEPLOY_USER`, `DEPLOY_HOST`, and `DEPLOY_PATH` in `.env`, then:

```bash
bash scripts/deploy.sh
```

---

## Database

SQLite at `data/benchmarks.db`. Reset and re-seed:

```bash
rm data/benchmarks.db
uv run python -m backend.seed_db
```

Schema source of truth: `config/schema.sql`. ORM: `backend/models.py`.

---

## Project structure

```
benchmarking_website/
├── scripts/               Interactive tools (primary workflow)
│   ├── run_manual.py      Process a single paper end-to-end
│   ├── find_citing_papers.py  Discover papers via Semantic Scholar
│   ├── compare_models.py  Compare LLM extraction quality
│   ├── set_dataset_stats.py   Update dataset statistics in DB
│   └── list_models.py     Check available LLM models
├── backend/               Pipeline modules (batch / automated use)
│   ├── llm_extractor.py   All LLM calls + extraction orchestration
│   ├── pipeline.py        CLI for all pipeline stages
│   ├── results_parser.py  Parse LLM JSON → DB rows
│   ├── export_to_hugo.py  Write Hugo content and data files
│   ├── seed_db.py         Seed benchmarks/datasets from YAML
│   └── reapply_overrides.py  Apply overrides.yaml files
├── config/
│   ├── schema.sql         Authoritative SQL schema
│   ├── seed_data.yaml     Benchmark/dataset definitions
│   ├── llm_config.yaml    LLM model config (non-secret)
│   └── prompts/           LLM system-prompt templates
├── site/                  Hugo static site
│   ├── hugo.toml
│   ├── layouts/           HTML templates
│   └── content/           Generated markdown (do not edit manually)
├── papers/                Per-paper folder (PDF, HTML, extracted/, overrides.yaml)
├── data/                  SQLite database (gitignored)
├── tests/                 pytest test suite
├── .env.example           Environment variable template
└── pyproject.toml
```
