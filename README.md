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

# the qwen model needs two gpus. Not clear which exact way to do the extraction is best.
uv run vllm serve Qwen/Qwen3.6-35B-A3B-FP8   --tensor-parallel-size 2   --max-model-len 32768   --gpu-memory-utilization 0.96   --enable-chunked-prefill   --max-num-seqs 128   --reasoning-parser qwen3

# this is the 4-bit version of the gemma4 model which can fit on a single gpu (~150t/s @8 parallel)
uv run vllm serve QuantTrio/gemma-4-31B-it-AWQ --quantization awq_marlin --limit-mm-per-prompt '{"image": 0, "audio": 0, "video": 0}' --gpu-memory-utilization 0.96   --max-num-batched-tokens 4096 --max_model_len=50000 --port 8773

# or on two gpus:
uv run vllm serve QuantTrio/gemma-4-31B-it-AWQ \
  --quantization awq_marlin \
  --tensor-parallel-size 2 \
  --limit-mm-per-prompt '{"image": 0, "audio": 0}' \
  --gpu-memory-utilization 0.95 \
  --max-num-batched-tokens 8192 \
  --max-model-len 50000 \
  --port 8773

# trying the MoE model
uv run vllm serve cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit --limit-mm-per-prompt '{"image": 0, "audio": 0}' --gpu-memory-utilization 0.92   --max-num-batched-tokens 4096 --max_model_len=50000 --port 8773   --tensor-parallel-size 2

# note that the model must match what has been started locally.
uv run python scripts/run_manual.py 2206.08164 
uv run python scripts/run_manual.py 2406.08993
uv run python scripts/run_manual.py 2411.05274  # DRAGON — tricky LRGB wrap-table / peptides extraction
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

### mark_priority_papers (for "seeding" the database after the extraction pipeline has been modified)
uv run python scripts/mark_priority_papers.py mark           # apply
uv run python scripts/mark_priority_papers.py mark --requeue # also reset done/failed/rejected → pending
uv run python scripts/mark_priority_papers.py mark --dry-run   # preview (18 papers)
uv run python scripts/mark_priority_papers.py export         # refresh list from DB  

### LaTeX table re-extraction (wraptable / sidewaystable parser fixes)
Server runbook: `config/latex_table_reextract_server.txt`

```bash
# Scan papers/ for wraptable, sidewaystable, and unparsed tabular rows
uv run python scripts/scan_latex_table_issues.py --write-list --export-json

# Mark flagged papers for LLM re-extraction (not parse-only)
uv run python scripts/mark_reextract_papers.py mark --requeue

# Process with --force so existing llm_output is replaced
uv run python scripts/todo_queue_dashboard.py --workers 10 --model primary --force
```

Development page: **Development → Problematic Papers** (after `export_to_hugo`).

---

### `scripts/find_citing_papers.py` — discover papers that cite a benchmark

Queries Semantic Scholar for all papers that cite a given arXiv paper, shows
their processing status in the local DB, and lets you interactively mark selected
papers as **manually important** in `todo_papers`. Processing happens separately
via the todo queue (see below).

```bash
# Find papers citing the LRGB benchmark paper
uv run python scripts/find_citing_papers.py 2206.08164

# Mark every citing paper with an arXiv ID as manually important (non-interactive)
uv run python scripts/find_citing_papers.py 2206.08164 --mark-all --limit 5000

# Limit to the 50 most recent citations
uv run python scripts/find_citing_papers.py 2206.08164 --limit 50

# Include papers already tracked in the DB
uv run python scripts/find_citing_papers.py 2206.08164 --show-all

# After marking papers, process with the dashboard
uv run python scripts/todo_queue_dashboard.py --workers 10
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
| `add` | Insert a paper; use `--important` for manual priority |
| `mark-important` | Mark an existing queue row as manually important |
| `unmark-important` | Clear the manual priority flag |
| `recompute-counts` | Refresh citation counters from DB state |

Both `process` and `worker` accept `--important-only` to restrict work to manually
important pending papers. With `process --important-only` and no explicit `--limit`,
all pending manually important papers are processed, then the command stops.

```bash
# Queue summary and top pending papers
uv run python scripts/todo_queue.py report

# Process more papers or use a different tier
uv run python scripts/todo_queue.py process --limit 10
uv run python scripts/todo_queue.py process --model fallback --limit 5

# Preview what would be processed
uv run python scripts/todo_queue.py process --dry-run --limit 20

# Add a paper manually (normal priority — behind high seen_count papers)
uv run python scripts/todo_queue.py add 2406.08993 --reason "found via citation crawl"

# Add with manual priority (processed before papers with higher seen_count)
uv run python scripts/todo_queue.py add 2406.08993 --important --reason "OGB leaderboard"

# Requeue existing terminal rows without marking them important
uv run python scripts/todo_queue.py requeue 2406.08993 2407.02263

# Mark an existing queue row as manually important (always requeues terminal rows and forces re-evaluation)
uv run python scripts/todo_queue.py mark-important 2406.08993
uv run python scripts/todo_queue.py unmark-important 2406.08993

# Process only manually important papers (until the important queue is empty)
uv run python scripts/todo_queue.py process --important-only

# Inspect queue state
uv run python scripts/todo_queue.py list --status all
```

Queue priority order: **`is_manually_important DESC`, then `seen_count DESC`, then oldest first**.
Manually important papers (marked via `--important` or `mark-important`) are always
claimed before papers discovered only via Semantic Scholar link density and are
processed with `--force`, so existing extraction is re-evaluated.

The `requeue` command moves existing `done`, `failed`, or `rejected` rows back to
`pending` and resets their queue attempt count without changing manual importance.
Run the dashboard with `--force` when these papers should be re-evaluated from
existing extraction artifacts.

#### Running many workers in parallel

Use the `worker` subcommand to saturate your GPU with concurrent extractions.
Each worker atomically claims exactly one pending paper before starting, so no
two active workers will process the same paper.  Processing claims have a
heartbeat and an ownership token. Workers that crash or are killed leave papers
in a `processing` state; these are automatically released back to `pending`
after 15 minutes so the next worker can retry them. A worker that loses its
claim cannot finalize over the newer owner.

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
    --output experiments/extraction/comparison.json \
    --log-dir experiments/extraction/logs

# Re-run planned models even when cached artifacts exist
uv run python scripts/compare_models.py --force

# Full runs also write aggregate JSON by default under experiments/extraction/
# Use --no-output to skip that file (paper artifacts are still saved)
```

Full runs persist extraction artifacts via the same ``process_paper`` path as
``run_manual`` (``llm_output.yaml``, ``llm_calls.yaml``, ``results_human_readable.md``).
Candidate models are stored under ``papers/<id>/extracted/experiments/compare-models-<slug>/``
with a compare-specific ``comparison.json``. On-disk results are reused automatically
and labeled ``[cached]`` or ``[auto-included]`` in the summary tables; ``--interactive``
model selection re-runs selected models.

### `scripts/compare_mlp_baseline.py` — compare node methods with MLP

Builds a reproducible comparison using standard, non-problematic node-classification or
node-regression results. Plain MLP rows are curated through the shared leaderboard eligibility
rules; LLM-augmented MLPs and confirmed noncanonical rows are excluded. Each paper contributes
its best eligible non-MLP result, including baseline methods.

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/compare_mlp_baseline.py
```

The default output directory is `experiments/mlp_baseline_comparison/` and contains the
reproducibility script `compare_mlp_baseline.py`, JSON/CSV records, a plain text summary, and
updated `better_tied_worse.png`/`.pdf` figures. No significance test is applied. Run the
adjacent script to regenerate exactly those outputs:

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/mlp_baseline_comparison/compare_mlp_baseline.py
```

### `experiments/extraction/validate_extraction.py` — fixed dataset-only validation

Runs the publication validation cohort in `config/extraction_validation.yaml` using only
the two-step RAG extraction path, without benchmarking dataset discovery. Every model receives
the same manifest-defined datasets;
the manifest fixes the exact model roster, model roles, comparison reference, and validation
revision. The runner refuses to start if any required model is unavailable. Reports, incremental
run state, and manual-review matrices are written under `experiments/extraction_validation/`.

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/extraction/validate_extraction.py

# Check that the exact required roster is reachable without starting the experiment
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/extraction/validate_extraction.py \
  --preflight-only

# Override the default of three simultaneous paper jobs for each model
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python experiments/extraction/validate_extraction.py \
  --workers-per-model 2
```

Use `--force` to ignore validation caches. Caches are isolated by the manifest digest, which
includes its explicit validation revision; main website extraction artifacts are never reused or
overwritten. Failures are recorded without stopping unrelated jobs, and cause a nonzero exit after
the partial report has been written.

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

# 6. Run one paper as a smoke test
uv run scripts/run_manual.py 2206.08164

# 7. Re-export and rebuild the site after extraction
uv run -m backend.export_to_hugo
```

Notes:

- Keep `.env`, `papers/`, `logs/`, and `benchmarks.db` on persistent local storage.
- `papers/` is intentionally git-ignored; this is where downloads, extraction artifacts,
  and local overrides live on the server.
- The normal refresh loop is: crawl or process papers, run parsing/extraction, then
  `uv run python -m backend.export_to_hugo`; a full export also runs Hugo with
  `--cleanDestinationDir` automatically.
- `uv run python -m backend.seed_db` is safe to re-run after dataset changes; it now also
  imports legacy pending-dataset YAML entries (if present) and marks DB-backed pending rows
  as `resolved` once they map to canonical datasets.
- For a production deployment, serve `site/public/` as static pages
```

---

### `scripts/repopulate_db.py` — reset extraction state and prime the important queue

Maintenance script for bulk refreshes after parser/extractor changes. It finds papers
that already have benchmark results in the database, optionally wipes the DB and their
LLM artifacts, then marks those papers as manually important in `todo_papers` for
parallel re-processing.

```bash
# Preview the reset + queue plan
uv run python scripts/repopulate_db.py --clean --dry-run

# Full clean slate: wipe DB, delete LLM outputs for papers with results, re-seed, queue
uv run python scripts/repopulate_db.py --clean

# Also purge outdated llm_output artifacts from every papers/<id>/ directory
uv run python scripts/repopulate_db.py --clean --delete-all-llm-outputs

# Limit to specific papers that already have stored results
uv run python scripts/repopulate_db.py --clean --paper 2206.08164 2309.00367

# Re-parse existing llm_output artifacts without new LLM calls
uv run python scripts/repopulate_db.py --skip-extract
```

After priming, process the queue with the dashboard:

```bash
uv run python scripts/todo_queue_dashboard.py --workers 10
```

Notes:

- Only papers with at least one stored `results` row are queued — papers that were merely
  downloaded or extracted without parsed benchmark results are ignored.
- `--delete-all-llm-outputs` removes `llm_output*` files under every `papers/<id>/extracted/`
  directory, even for papers that are not re-queued.
- With `--clean`, the script wipes the DB, deletes LLM outputs, **re-seeds from
  `config/seed_data.yaml`**, and only then primes the important queue.
- Dry-run and completion output stay compact at scale: LLM deletions are reported as
  file/paper counts, and the queue plan shows totals plus a small sample table.
- `--skip-extract` only re-reads the main `papers/<id>/extracted/llm_output.json` artifacts.
- Files under `papers/<id>/extracted/experiments/<label>/` are side-by-side comparison artifacts and do not affect
  the normal parse/export path unless you explicitly copy or promote them yourself.
- Run `uv run python -m backend.export_to_hugo` after workers finish.

---

### `scripts/run_pipeline.sh` — cron-friendly batch runner

Shell wrapper around `python -m backend.pipeline run-all --all` that activates the
virtual environment and writes a timestamped log under `logs/`.

```bash
bash scripts/run_pipeline.sh
bash scripts/run_pipeline.sh --model fallback
```

---

### `scripts/deploy.py` — build and deploy the static site

Builds the Hugo site and deploys via zstd-compressed tar archives over `scp`/`ssh`.
Figures (`figures/`) are split into a separate archive so day-to-day deploys can send
only the increment (HTML/CSS/JS) after an initial full run.

```bash
# First deploy (or when figures changed): upload figures + increment archives
uv run python scripts/deploy.py --full

# Routine deploy: upload increment only (reuses latest figures archive on server)
uv run python scripts/deploy.py
uv run python scripts/deploy.py --skip-export   # Hugo rebuild only, no DB export
```

`scripts/deploy.sh` is a thin wrapper around the same command.

Archives are stored outside the web root at `~/deploy/` on the server (not web-accessible).
Archive names:
`{hostname}-{YYYYMMDDHHMM}-figures.tar.zst` / `...-increment.tar.zst`.

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

After editing this file, re-export and rebuild:

```bash
uv run python -m backend.export_to_hugo
cd site && /snap/bin/hugo --minify
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

After editing the file, re-parse any affected papers to see the fix immediately:

```bash
uv run python -m backend.results_parser 2206.08164
uv run python -m backend.export_to_hugo
```

Or for a full comparison re-run:

```bash
uv run python scripts/compare_models.py --paper 2206.08164 --force
```

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
