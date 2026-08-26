# Plan: Graph Learning Benchmarking Website

Updated: 2026-08-12

## Purpose

Maintain a self-hosted, static Hugo site that helps researchers discover graph-learning papers,
compare benchmark results, and inspect the evidence and protocol behind each row. SQLite is the
curated source of truth; paper downloads and extraction artifacts remain local workspace data.

## Current system

- **Discovery and queue:** citation discovery for LRGB and GraphBench, an ArXiv scanner, Semantic
  Scholar/OpenReview maintenance, and a shared queue driven by `scripts/queue_paper.py` and
  `scripts/process_papers.py`.
- **Paper pipeline:** HTML/PDF/LaTeX acquisition; configurable OpenAI-compatible LLM extraction;
  structured parsing into results, dataset statistics, and SOTA claims; manual corrections through
  per-paper `overrides.yaml` files.
- **Curation:** dataset variants, metric direction, model aliases, baseline aggregation, explicit
  protocol contracts and exclusions, anomaly detection, and export-time eligibility checks.
- **Site:** `backend/export_to_hugo.py` generates paper, dataset, benchmark-group, result, and
  development pages plus JSON data; Hugo templates and JavaScript provide leaderboards, charts,
  filters, comparison metadata, and mobile views.
- **Operations and quality:** `backend.pipeline` supports discover/download/extract/parse/export/
  build/run-all; `scripts/deploy.py` handles local and remote deployment; pytest, Ruff, Black,
  isort, Bandit, and pre-commit provide development checks.

Current database snapshot: 2,741 papers, 23 benchmarks, 142 datasets, 176 variants, 61,112 result
rows, and 8,616 pending-dataset records.

## Common commands

```bash
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv sync --group dev
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.seed_db
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/process_papers.py <arxiv-id>
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python -m backend.pipeline run-all --since 7d
UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/deploy.py --local
```

## Remaining work, ordered by significance

1. **Protect benchmark trust.** Complete the post-remediation audit in `mistakes.md`: verify
   protocol exclusions and export eligibility, check for overblocking, and finish the historical
   LRGB-loss recovery and row dispositions described in `LRGB_REGRESSION_REPORT.md`.
2. **Unify and complete paper metadata.** Consolidate the duplicate metadata cascades in
   `backend/extraction_runner.py` and `backend/results_parser.py`, then measure and backfill missing
   authors, dates, venues, source URLs, abstracts, and code links.
3. **Close benchmark coverage gaps.** Reconcile the pending-dataset queue and dataset statistics;
   import the canonical OGB results and sources; fill benchmark dates/papers; and make benchmark
   selection guidance visible on dataset pages.
4. **Make result provenance and baselines transparent.** Expose all papers contributing to an
   aggregated method result, compare reported baselines with historical values, improve model
   joining (including MLPs and Wisconsin cases), and retain clear source/table attribution.
5. **Harden and scale the pipeline.** Add ArXiv version-update processing, finish the
   `CODE_QUALITY_CHECKLIST.md` items, improve multi-endpoint/model benchmarking, and add a rendered
   regression check for key site views.
6. **Improve researcher-facing workflows.** Explain ranking and comparability plainly; add dataset
   side-by-side comparison, model-family exploration, contribution/feedback workflows, and RSS only
   after the data-quality foundations are stable.

## Deferred scope

Generation benchmarks and scattered emerging settings such as few-shot, contrastive/embedding,
and adversarial evaluation need explicit benchmark contracts before being added to standard
leaderboards. Keep them quarantined or separately labeled until then.

## Working documents

- `manual_todos.md` — personal, manually edited backlog.
- `CODE_QUALITY_CHECKLIST.md` — active engineering debt and regression awareness.
- `mistakes.md` — benchmark-quality audit.
- `SUSPICIOUS_TASK_PAPERS_REPORT.md` — anomaly-detector limitations and follow-ups.
- `LRGB_REGRESSION_REPORT.md` — historical overblocking and recovery context.
