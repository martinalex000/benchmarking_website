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
uv run vllm serve Qwen/Qwen3.6-35B-A3B-FP8   --tensor-parallel-size 2   --max-model-len 32768   --gpu-memory-utilization 0.92   --enable-chunked-prefill   --max-num-seqs 128   --reasoning-parser qwen3

uv run python scripts/run_manual.py 2206.08164
```

The repository now keeps `papers/` as a local workspace directory only. Generated
downloads, extracted artifacts, and overrides live there on each instance, but are
not committed to git.

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
# List all models the endpoint serves and check your configured tiers
uv run python scripts/list_models.py
```

---
## Script reference

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

# Review and import unresolved datasets queued during extraction
uv run python scripts/run_manual.py --import-pending
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

### `scripts/find_citing_papers.py` — discover papers that cite a benchmark

Queries Semantic Scholar for all papers that cite a given arXiv paper, shows
their processing status in the local DB, and lets you interactively queue them
for processing via `run_manual.py`.

This is an interactive inspection tool. It does **not** maintain the persistent
`todo_papers` queue; use `scripts/find_todo_semanticscholar.py` for that.

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

### `scripts/find_todo_semanticscholar.py` — canonical Semantic Scholar todo-queue updater

This is the canonical script for keeping `todo_papers` current from Semantic Scholar.
For each seed paper, it fetches both:

- incoming links: papers that cite the seed (`cited_by:<seed>`)
- outgoing links: papers referenced by the seed (`references_from:<seed>`)

It adds newly discovered arXiv papers to `todo_papers`, de-duplicates repeated
observations, recomputes:

- `seen_count` from unique observations
- `cited_by_count` from unique `references_from:*` links
- `cites_existing_count` from unique `cited_by:*` links

It also marks todo rows as `done` once the paper already exists in the local corpus,
and refreshes generated development/admin exports such as `site/data/todo_papers.json`.

```bash
# Crawl a specific seed paper
uv run python scripts/find_todo_semanticscholar.py --seed 2206.08164

# Crawl several benchmark seeds in one run
uv run python scripts/find_todo_semanticscholar.py \
  --seed 2206.08164 \
  --seed 2512.04475 \
  --top 25

# Re-crawl a seed even if it already appears in s2_crawl_state
uv run python scripts/find_todo_semanticscholar.py --seed 2206.08164 --force
```

Important: if `--seed` is omitted, the script crawls **all uncrawled papers already in the DB**.
That is useful for broad refreshes, but it is much heavier than a single-seed update.

---

### `scripts/todo_queue.py` — unified todo-queue interface

This is the main user-facing interface for `todo_papers`.

```bash
# Show all subcommands and options
uv run python scripts/todo_queue.py --help

# Subcommand-specific help
uv run python scripts/todo_queue.py worker --help
uv run python scripts/todo_queue.py process --help
```

Subcommands:

| Subcommand | Purpose |
|---|---|
| `worker` | Atomically claim and process one pending paper, then exit (parallel-safe) |
| `process` | Sequentially process the next N pending papers |
| `report` | Queue summary and top pending papers |
| `list` | Raw queue rows |
| `add` | Insert a manual priority paper |
| `recompute-counts` | Refresh citation counters from DB state |

```bash
# Queue summary and top pending papers
uv run python scripts/todo_queue.py report

# Process more papers or use a different tier
uv run python scripts/todo_queue.py process --limit 10
uv run python scripts/todo_queue.py process --model fallback --limit 5

# Preview what would be processed
uv run python scripts/todo_queue.py process --dry-run --limit 20

# Add a paper manually
uv run python scripts/todo_queue.py add 2406.08993 --reason "manually prioritized"

# Inspect queue state
uv run python scripts/todo_queue.py list --status all
```

#### Running many workers in parallel

Use the `worker` subcommand to saturate your GPU with concurrent extractions.
Each worker atomically claims exactly one pending paper before starting, so no
two workers will ever process the same paper.  Workers that crash or are killed
leave papers in a `processing` state; these are automatically released back to
`pending` after 15 minutes so the next worker can retry them.

```bash
# Launch 10 parallel workers, each writing its own log file
for i in $(seq 1 10); do
  uv run python scripts/todo_queue.py worker --model primary \
    >> logs/worker_$i.log 2>&1 &
done
wait
echo "All workers finished."
```

Each worker invocation processes exactly one paper and exits, so the loop above
runs all 10 workers concurrently.  To keep feeding papers to idle GPUs, wrap the
worker in a loop:

```bash
# Continuous worker: keeps running until the queue is empty
while true; do
  uv run python scripts/todo_queue.py worker --model primary >> logs/worker.log 2>&1
  # Exit if nothing was processed (queue exhausted)
  grep -q "No pending todo papers" logs/worker.log && break
done
```

Or use GNU `parallel` / `xargs` for a fixed pool:

```bash
seq 1 200 | xargs -P 10 -I{} \
  uv run python scripts/todo_queue.py worker --model primary
```

If you prefer a single live UI (Docker-pull style) with one persistent row per
worker, use the dashboard runner:

```bash
uv run python scripts/todo_queue_dashboard.py --workers 10 --model primary

# Optional: kill workers that produce no output for too long (default: 20 min)
uv run python scripts/todo_queue_dashboard.py --workers 10 --model primary \
  --inactivity-timeout-min 20

# Diagnostics: heartbeat + automatic thread dump when UI render loop stalls
uv run python scripts/todo_queue_dashboard.py --workers 10 --model primary \
  --diag-log-path logs/todo_queue_dashboard.log \
  --diag-heartbeat-sec 2 \
  --diag-stall-sec 15
```

It shows, per worker: arXiv ID, paper title (truncated), current phase
(download/pre-screen/discovery/per-dataset extraction), elapsed time,
last-update age (`Upd`), and a rolling summary (including refs-at-start,
datasets, results, and proposed model).

The dashboard also includes:

- a **Finished papers** window (one line per completed paper with summary)
- a **Recent worker output** window for rolling raw log lines

The header also shows queue statistics (refreshed whenever a new job is
claimed):

- total papers currently in `todo_papers`
- maximum `seen_count` (max references observed so far)

The header also includes a live `ui_tick` clock. If shared state is briefly
contended, the dashboard keeps rendering from a cached snapshot and labels this
state, so the interface remains interactive instead of freezing.

For freeze investigations, the dashboard writes diagnostics to
`logs/todo_queue_dashboard.log` (configurable via `--diag-log-path`). When the
UI render loop appears stalled longer than `--diag-stall-sec`, it appends a
full all-thread Python stack dump to that same log file.

Use **Up/Down** arrow keys (or **k/j**) to scroll only the Finished papers
window while the rest of the dashboard keeps updating live.

Use **+** to add one worker at runtime.
Use **-** to drain one worker at runtime (it exits gracefully after finishing
its current paper and does not claim another).

When a worker has not produced output for 10 seconds, its `Upd` value is
highlighted to make potential stalls visible immediately.
Workers also retry transient empty-queue claim races before switching to idle,
which avoids false "queue empty" exits under high concurrency.

After all workers finish, refresh the Hugo data files once:

```bash
uv run python -m backend.export_to_hugo
```

> **Note:** Workers always skip per-paper Hugo export (`--skip-export` is
> passed automatically) to avoid redundant rebuilds during batch runs.

---

### Legacy queue wrappers

`scripts/find_todo_papers.py` and `scripts/process_todo_list.py` now forward into `scripts/todo_queue.py` for backwards compatibility. New usage should prefer the unified interface above.

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

### `scripts/test_model_ping.py` — low-level endpoint/model diagnostic

Use this when a model appears reachable but returns empty content, unusual finish
reasons, or suspicious rate-limit behavior.

```bash
uv run python scripts/test_model_ping.py MiniMaxAI/MiniMax-M2.5
uv run python scripts/test_model_ping.py moonshotai/Kimi-K2.6

---

## Fresh server setup
```bash
git clone <repo-url>
cd benchmarking_website

# 2. Install Python dependencies
uv sync

# 3. Configure secrets
cp .env.example .env
$EDITOR .env

# 4. Seed canonical benchmark + dataset metadata
uv run -m backend.seed_db

# 5. Build local generated state (note the "-m")
uv run -m backend.export_to_hugo
hugo --source site

# 6. Run one paper as a smoke test
uv run scripts/run_manual.py 2206.08164

# 7. Re-export and rebuild the site after extraction
uv run -m backend.export_to_hugo
hugo --source site
```

Notes:

- Keep `.env`, `papers/`, `logs/`, and `benchmarks.db` on persistent local storage.
- `papers/` is intentionally git-ignored; this is where downloads, extraction artifacts,
  and local overrides live on the server.
- The normal refresh loop is: crawl or process papers, run parsing/extraction, then
  `uv run python -m backend.export_to_hugo` and `hugo --source site`.
- `uv run python -m backend.seed_db` is safe to re-run after dataset changes; it now also
  imports legacy pending-dataset YAML entries (if present) and marks DB-backed pending rows
  as `resolved` once they map to canonical datasets.
- For a production deployment, serve `site/public/` as static pages
```

---

### `scripts/repopulate_db.py` — re-extract or re-parse the existing corpus

Maintenance script for bulk refreshes over the already-downloaded `papers/` corpus.
Use it after major parser/extractor changes when you want to re-run extraction,
re-parse existing artifacts, or rebuild from a clean database without re-downloading PDFs.

```bash
# Re-parse existing llm_output.json files without new LLM calls
uv run python scripts/repopulate_db.py --skip-extract

# Clean DB + re-extract everything with the fallback model, then export
uv run python scripts/repopulate_db.py --clean --model fallback --export
```

Notes:

- `--skip-extract` only re-reads the main `papers/<id>/extracted/llm_output.json` artifacts.
- Files under `papers/<id>/extracted/experiments/<label>/` are side-by-side comparison artifacts and do not affect
  the normal parse/export path unless you explicitly copy or promote them yourself.
- If a paper's main `llm_output.json` was produced by the fallback tier, bulk `--model primary` runs will skip it by design.
  Remove that main file first if you want `repopulate_db.py` to replace it with a fresh primary/qwen extraction.

---

### `scripts/run_pipeline.sh` — cron-friendly batch runner

Shell wrapper around `python -m backend.pipeline run-all --all` that activates the
virtual environment and writes a timestamped log under `logs/`.

```bash
bash scripts/run_pipeline.sh
bash scripts/run_pipeline.sh --model fallback
```

---

### `scripts/deploy.sh` — build and deploy the static site

Builds the Hugo site and rsyncs `site/public/` to the configured deployment target.

```bash
bash scripts/deploy.sh
```

Requires `DEPLOY_USER`, `DEPLOY_HOST`, and `DEPLOY_PATH` in `.env`.

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
cd site && ruv run hugo
```

If you only need to adjust website presentation (not DB semantic metadata), prefer `config/dataset_overrides.yaml` for display-only controls such as `display_metrics`.

*Note*: the landing page text is in `site/layouts/index.html`.

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

To preview subpath deployments locally, pass the same base URL you will deploy with:

```bash
cd site && /snap/bin/hugo server --bind 0.0.0.0 -p 1313 --baseURL http://localhost:1313/graphlearningbenchmarks/
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
│   ├── llm_config.yaml    LLM runtime settings (non-secret)
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
