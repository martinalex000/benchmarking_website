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

# start local LLM
uv run vllm serve cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit --limit-mm-per-prompt '{"image": 0, "audio": 0, "video": 0}' --gpu-memory-utilization 0.92   --max-num-batched-tokens 4096 --max_model_len=50000 --port 8773   --tensor-parallel-size 2

# note that the model must match what has been started locally.
uv run python scripts/process_papers.py 2206.08164
uv run python scripts/process_papers.py 2406.08993
uv run python scripts/process_papers.py 2411.05274  # DRAGON — tricky LRGB wrap-table / peptides extraction
```

The repository keeps `papers/` as a local workspace directory only. Generated
downloads, extracted artifacts, and overrides live there on each instance, but are
not committed to git.

### arXiv metadata statistics

Download the Cornell/Kaggle metadata snapshot and generate category, keyword, and
database-recall reports. The snapshot and reports are stored under
`papers/arxiv-metadata/` and remain untracked.

```bash
uv run python scripts/prescreen_kaggle_arxiv.py download
uv run python scripts/prescreen_kaggle_arxiv.py stats
```

##### Resume the LLM screening queue
uv run python scripts/prescreen_kaggle_arxiv.py screen \
  --workers 8


---

## LLM configuration

### `.env` — secrets (never commit this file)

| Variable | Required | Description |
|---|---|---|
| `LLM_ENDPOINT` | **yes** | Base URL, e.g. `https://api.example.com/v1` (openai-compatible)|
| `LLM_API_KEY` | **yes** | API key for that endpoint |
| `LLM_MODEL_PRIMARY` | no | Primary model for extraction and complex reasoning |
| `LLM_MODEL_FALLBACK` | no | Fallback model if the primary output is poor |
| `LLM_MODEL_SMALL` | no | Small/cheap model used for screening |

### Local vLLM + Qwen example

```bash
# .env values for local server (see above)
LLM_ENDPOINT=http://127.0.0.1:8000/v1
LLM_API_KEY=local-dev
LLM_MODEL_PRIMARY=Qwen/Qwen3.6-35B-A3B-FP8
LLM_MODEL_FALLBACK=Qwen/Qwen3.6-35B-A3B-FP8
LLM_MODEL_SMALL=Qwen/Qwen3.6-35B-A3B-FP8
```

Important: the configured `LLM_MODEL_*` values must match the exact model IDs returned by `GET /v1/models`.

### Verify your endpoint

```bash
# List reachable models and check configured tiers
uv run python scripts/test_llms.py

# Probe reachable chat models and verify reasoning is disabled
uv run python scripts/test_llms.py ping

# Print current rate-limit headers for all reachable models
uv run python scripts/test_llms.py --rate-limits
```

---
## Usage reference

### Choose the workflow

Use the script entry points for day-to-day, interactive work:

- `scripts/process_papers.py` processes one paper or runs the queue dashboard.
- `scripts/queue_paper.py` adds papers to the shared queue.
- `scripts/maintenance.py` refreshes metadata and performs database maintenance.
- `scripts/deploy.py` exports and builds the site, then optionally deploys it.

Use `backend.pipeline` for unattended or stage-by-stage batch runs:

```bash
# Run discovery, download, extraction, parsing, export, and Hugo build
uv run python -m backend.pipeline run-all --since 7d

# Run individual batch stages when debugging or resuming a run
uv run python -m backend.pipeline download
uv run python -m backend.pipeline extract --model primary
uv run python -m backend.pipeline parse
uv run python -m backend.pipeline export
uv run python -m backend.pipeline build
```

### Paper processing

```bash
uv run python scripts/process_papers.py 2206.08164
uv run python scripts/process_papers.py dashboard
uv run python scripts/queue_paper.py 2206.08164
uv run python scripts/queue_paper.py --file config/priority_papers.txt --important --yes
```

---
### `scripts/process_papers.py` — process papers directly or from the queue

The primary interactive tool. Downloads, extracts, stores, and exports one paper.
Prints live progress for every LLM call (call type, input/output size, TTFT,
tok/s, discovered datasets, and tables selected).

```bash
# Basic: download + extract + store + export
uv run python scripts/process_papers.py 2206.08164

# Re-run extraction only (keep existing download)
uv run python scripts/process_papers.py 2206.08164 --force

# Skip the abstract screening step and go straight to full extraction
uv run python scripts/process_papers.py 2206.08164 --skip-screen

# Use a different model or model tier
uv run python scripts/process_papers.py 2206.08164 --model fallback
```

If extraction fails, an `errors.log` entry and a full Markdown conversation log
(`extraction_error_<timestamp>.md`) are written to `papers/<id>/extracted/`.
The stored extraction model is the actual `model_used` from `llm_output.json`,
so automatic fallback runs are recorded under the model that really produced the extraction.

Cache semantics:

- The canonical extraction artifact is `papers/<id>/extracted/llm_output.json`.
- Normal parsing and export read that main file, not anything under `papers/<id>/extracted/experiments/`.
- If the main `llm_output.json` was produced by the configured fallback tier, a later `--model primary`
  run will intentionally skip overwriting it. If you want to force a new primary/qwen extraction for that paper,
  delete the main `papers/<id>/extracted/llm_output.json` first and rerun extraction.

---  
  
### `scripts/maintenance.py` — common maintenance operations

Use this entry point for Semantic Scholar queue maintenance and broad metadata
maintenance. Specialized subcommands are available through `--help`.

```bash
# Refresh the todo queue from a specific seed
uv run python scripts/maintenance.py todo --seed 2206.08164

# Re-crawl a seed even if it is marked complete
uv run python scripts/maintenance.py todo --seed 2206.08164 --force

# Preview the complete maintenance run
uv run python scripts/maintenance.py all --dry-run

# Preview result rows excluded by protocol curation rules
uv run python scripts/maintenance.py exclusions --dry-run

# Apply the exclusion cleanup after reviewing the preview
uv run python scripts/maintenance.py exclusions --yes
```

If `--seed` is omitted, `todo` crawls all database papers missing complete
Semantic Scholar data. Use `uv run python scripts/maintenance.py --help` to
see metadata backfill and venue-repair subcommands.

---

### Queue processing

Use `queue_paper.py` to add papers and `process_papers.py` for direct processing
or the live multi-worker dashboard. The dashboard handles queue claiming,
parallel workers, retries, and queue status internally.

```bash
# Add papers to the normal queue
uv run python scripts/queue_paper.py 2406.08993

# Add papers with manual priority, requeueing terminal rows when needed
uv run python scripts/queue_paper.py --file config/priority_papers.txt --important --yes

# Process one paper directly
uv run python scripts/process_papers.py 2406.08993

# Process the queue with the live dashboard
uv run python scripts/process_papers.py dashboard --workers 10 --model primary
```

Manually important papers are processed before ordinary queue entries and are
re-evaluated with force. Use `--force` on the dashboard when deliberately
reprocessing existing extraction artifacts. After a batch run, refresh the Hugo
data files with:

```bash
uv run python scripts/deploy.py --local
```

---

### `scripts/test_llms.py` — check available models and endpoints

```bash
uv run python scripts/test_llms.py
uv run python scripts/test_llms.py ping MODEL_NAME
uv run python scripts/test_llms.py metrics
```

Use `--rate-limits` (also accepted as `--rate-limit`) with the default command to add request,
token, and other rate-limit columns to the reachable-models table. With `ping`, it adds the
rate-limit headers for the selected models. The rate-limit probes run with up to 20 workers and a
progress indicator; with `--rate-limits`, the inventory lists only models that support chat requests.

---

### `scripts/deploy.py` — build and deploy the static site

Builds the Hugo site and synchronizes the generated tree incrementally over SFTP using
`rclone`. Images are compared by size; other generated files are always refreshed so
Hugo's regenerated modification times do not cause incorrect skips.

```bash
# First deploy (or when figures changed)
uv run python scripts/deploy.py --full

# Routine deploy: synchronize the generated tree and delete stale files
uv run python scripts/deploy.py                 # to the configured SFTP host
uv run python scripts/deploy.py --local         # Export and serve locally until Ctrl+C
uv run python scripts/deploy.py --both          # Deploy to the server and GitHub Pages (not local!)
```


Local deploy archives are stored under `deploy-archives/` for `--upload-only` retries.

Requires `DEPLOY_USER`, `DEPLOY_HOST`, and `DEPLOY_PATH` in `.env`.
The deployment host must provide SFTP access; install `rclone` locally.

Github points to: `https://github.com/graphlearningbenchmarks/graphlearningbenchmarks.github.io`

If you deploy under a subpath such as `https://somedomain.com/graphlearningbenchmarks/`, also set:

```bash
HUGO_BASE_URL=https://somedomain.com/graphlearningbenchmarks/
```

Manual deployment using:
```bash
cd site
hugo --baseURL "https://research.uni-leipzig.de/graphlearningbenchmarks/"
scp -r public/* webspace:webdir/
```

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

# Correct architecture type, per-result parameter count (millions), or external-data flag.
# Keys match result.model.name (lowercase). Parameter counts live on results only.
model_metadata_overrides:
  - model: "GraphGPS"
    model_type: hybrid
    params_millions: 6.9
    uses_external_data: false
    reason: "Table 2 lists 6.9M params; trained on benchmark split only"
```

`model_metadata_overrides` sets `Result.params_millions` and `Result.uses_external_data`
per paper, and `Model.model_type` for architecture badges. Well-known OGB baseline
families also have defaults in `config/model_metadata_defaults.yaml` (architecture only).

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

This is dataset-level (not paper-level), and affects all dataset pages for that dataset.

### Post-extraction dataset alias normalisation

When an LLM returns a slightly wrong dataset name (e.g. ``Computer`` instead of
``Amazon-Computers``, or ``Ppi`` instead of ``PPI``), the pipeline can rewrite the
name automatically before parsing.  This avoids false "misses" and
hallucinations in ``compare_models.py`` and prevents duplicate/unmatched rows in
the database.

Edit the alias map here:

`config/dataset_aliases.yaml`

```yaml
# Keys   — raw names as returned by the LLM
# Values — canonical names the pipeline understands
aliases:
  Computer: Amazon-Computers
  Photo: Amazon-Photo
  Ppi: PPI
```

The lookup is case-insensitive; leading/trailing whitespace is stripped.  Aliases
are applied **after** extraction but **before** fuzzy dataset matching, so a
fixed alias short-circuits the fuzzy matcher entirely.

---

## Editing dataset descriptive text

Dataset descriptions shown on the website are sourced from the database field `Dataset.description`.

Primary edit location:

- `config/seed_data.yaml` (benchmark and dataset definitions, including `description`)

---

## Project structure

```
benchmarking_website/
├── scripts/               Interactive tools (primary workflow)
│   ├── process_papers.py  Process papers directly or from the queue
│   ├── queue_paper.py     Add papers to the processing queue
│   ├── maintenance.py     Run metadata and queue maintenance
│   ├── deploy.py          Build and deploy the static site
│   └── test_llms.py       Check configured LLM endpoints
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
│   ├── llm_config.yaml    LLM runtime settings (non-secret)
│   └── prompts/           LLM system-prompt templates
├── site/                  Hugo static site
│   ├── hugo.toml
│   ├── layouts/           HTML templates
│   └── content/           Generated markdown (do not edit manually)
├── papers/                Per-paper folder (PDF, HTML, extracted/, optional overrides.yaml)
├── data/                  SQLite database 
├── tests/                 pytest test suite
├── .env.example           Environment variable template
└── pyproject.toml
```
