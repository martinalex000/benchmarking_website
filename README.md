# Graph Learning Benchmarking Website

A self-hosted static website that tracks and visualises state-of-the-art results
across graph learning benchmarks. Papers are discovered automatically via an
LLM-powered pipeline; human corrections are applied through `overrides.yaml` files.

---

## Quick start

```bash
git clone <repo-url>
cd benchmarking_website

# Copy the env template and fill in your LLM credentials (see section below)
cp .env.example .env
$EDITOR .env

# Install all dependencies (Python 3.12+, uv required)
uv sync --group dev

# Seed the database with benchmark/dataset definitions
python -m backend.seed_db

# Run the full pipeline (discover → download → extract → parse → aggregate → export → build)
python -m backend.pipeline run-all
```

---

## LLM configuration

The pipeline uses an **OpenAI-compatible** API endpoint. All configuration lives
in two places:

### 1. `.env` — secrets (never commit this file)

| Variable | Required | Description |
|---|---|---|
| `LLM_ENDPOINT` | **yes** | Base URL of your LLM server, e.g. `https://api.example.com/v1` |
| `LLM_API_KEY` | **yes** | API key for that endpoint |
| `LLM_MODEL_PRIMARY` | no | Override the primary model (default: `openai-gpt-oss120b`) |
| `LLM_MODEL_FALLBACK` | no | Override the fallback model (default: `minimax`) |
| `LLM_MODEL_SMALL` | no | Override the small/cheap model (default: `gemma-3-27b`) |

Copy `.env.example` → `.env` and set `LLM_ENDPOINT` and `LLM_API_KEY` at minimum.

### 2. `config/llm_config.yaml` — non-secret model settings

Default model names, temperature, retry counts, and token limits live here.
`.env` values override the YAML if both are set.

### Check which models your endpoint actually serves

```bash
uv run python scripts/list_models.py
```

This queries `GET /v1/models`, prints all available model IDs, then checks
whether your configured `primary`, `fallback`, and `small` model names match.
Exits 1 if any are missing so you can update `.env` / `config/llm_config.yaml`.

---

## Pipeline commands

All pipeline stages are sub-commands of `python -m backend.pipeline`:

```bash
# Full end-to-end run
python -m backend.pipeline run-all

# Individual stages
python -m backend.pipeline discover      # arXiv + citation scanning for new papers
python -m backend.pipeline download      # fetch PDFs
python -m backend.pipeline extract       # LLM extraction of results from PDFs
python -m backend.pipeline parse         # write LLM output to SQLite
python -m backend.pipeline aggregate     # compute leaderboard aggregates
python -m backend.pipeline export        # write Hugo markdown + data files
python -m backend.pipeline build         # run Hugo static site generator

# Debug logging
python -m backend.pipeline run-all --verbose
```

### Manual paper processing

Process a single paper (useful for testing or re-processing):

```bash
python scripts/run_manual.py 2206.08164
python scripts/run_manual.py 2206.08164 --model fallback
python scripts/run_manual.py 2206.08164 --skip-download   # re-extract only
```

The script prints download size (MB), whether an HTML version was available,
which model is being used, and how many result rows were stored.

If extraction fails with a model-not-found error, check what models your
endpoint actually serves:

```bash
uv run python scripts/list_models.py
```

---

## Corrections and overrides

Results are never edited directly in the database. Instead, create or edit an
`overrides.yaml` file in the paper's data directory:

```
papers/
└── 2206.08164/
    ├── paper.pdf
    ├── extraction.json        ← raw LLM output (do not edit)
    └── overrides.yaml         ← your corrections go here
```

Example `overrides.yaml`:

```yaml
results:
  - dataset: Peptides-func
    model: GPS
    metric_name: AP
    metric_value: 0.6535
    override_reason: "Typo in LLM extraction; corrected from paper Table 2"
```

After editing, re-apply overrides:

```bash
# Re-apply overrides for one paper
python -m backend.reapply_overrides --paper 2206.08164

# Re-apply all overrides, then re-export and rebuild
python -m backend.reapply_overrides
python -m backend.pipeline aggregate
```

---

## Local preview

```bash
cd site
/snap/bin/hugo server --buildDrafts
# Open http://localhost:1313
```

---

## Deployment

Edit `DEPLOY_USER`, `DEPLOY_HOST`, and `DEPLOY_PATH` in `.env`, then:

```bash
bash scripts/deploy.sh
```

---

## Database

SQLite database at `data/benchmarks.db` (WAL mode). Reset and re-seed:

```bash
rm data/benchmarks.db
python -m backend.seed_db
```

Schema source of truth: `config/schema.sql`. ORM: `backend/models.py`.

---

## Code formatting

All Python is formatted with **black** (line length 100). A pre-commit hook
runs black automatically on every commit.

```bash
# Format manually
uv run black .

# Install the pre-commit hook (already done after uv sync)
uv run pre-commit install
```

---

## Project structure

```
benchmarking_website/
├── backend/               Python pipeline modules
│   ├── models.py          SQLAlchemy ORM (source of truth for DB schema)
│   ├── db.py              DB session management
│   ├── pipeline.py        CLI entry point for all pipeline stages
│   ├── arxiv_scanner.py   Discover papers from arXiv
│   ├── citation_finder.py Follow citations to baseline papers
│   ├── llm_extractor.py   LLM calls for result extraction
│   ├── results_parser.py  Parse LLM JSON → DB rows
│   ├── baseline_aggregator.py  Leaderboard aggregation
│   ├── export_to_hugo.py  Write Hugo content and data files
│   ├── seed_db.py         Seed benchmarks/datasets from YAML
│   └── reapply_overrides.py  Apply overrides.yaml files
├── config/
│   ├── schema.sql         Authoritative SQL schema
│   ├── seed_data.yaml     Benchmark/dataset definitions
│   └── llm_config.yaml    LLM model config (non-secret)
├── site/                  Hugo static site
│   ├── hugo.toml          Hugo configuration
│   ├── layouts/           HTML templates
│   ├── assets/            CSS / JS
│   └── content/           Generated markdown (do not edit manually)
├── scripts/               Helper shell scripts
├── tests/                 pytest test suite
├── data/                  SQLite database (gitignored)
├── papers/                Downloaded PDFs + per-paper overrides.yaml
├── .env.example           Environment variable template
└── pyproject.toml         Python project config
```
