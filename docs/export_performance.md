# Hugo export performance

Last updated: **2026-06-03** (batched DB sessions, line_profiler on datasets + papers).

## Production export order

`export_all` uses **one** `session_scope()` for the whole run:

1. All datasets (`export_dataset(..., session=session)`)
2. `benchmarks.json` (warm `_DATASET_EXPORT_META_CACHE`)
3. Development JSON + `site/content/dev/*.md`
4. All exportable papers (`export_paper(..., session=session)`)

Timing summary is printed via tqdm after each phase.

**Deploy:** `scripts/deploy.sh` runs `uv run python -m backend.export_to_hugo` before `hugo` unless you pass `--skip-export`. Generated paths `site/content/dev/`, `site/content/papers/`, etc. are gitignored — deploy without export yields no dev pages.

## Line profiler: dataset export (bottlenecks)

Profiled with `scripts/profile_export.py --line-profile-only --line-profile-dataset <id>` calling `_export_dataset_impl` (single session).

### D&D (id 51, ~1282 rows, ~3 MB `index.md`)

| Component | Wall (profiler) | % of `export_dataset` |
|-----------|-----------------|------------------------|
| **`yaml.dump` in `_write_md`** | **~23 s** | **~96%** |
| `_build_multi_metric_rows` | ~0.45 s | ~2% |
| `get_best_results_over_time` | ~0.08 s | &lt;1% |
| ORM fetch `.all()` | ~0.06 s | &lt;1% |

### Cora (id 37, ~1516 rows, ~1.5 MB `index.md`)

| Component | Wall (profiler) | % of `export_dataset` |
|-----------|-----------------|------------------------|
| **`yaml.dump` in `_write_md`** | **~11 s** | **~90%** |
| `_build_multi_metric_rows` | ~0.46 s | ~4% |
| `get_best_results_over_time` | ~0.23 s | ~2% |

**Why datasets dominate a full export (~22–29 s for 140 datasets):** Most wall time is **serializing huge YAML front matter** (full leaderboard embedded in each `index.md`), not SQL. Pivoting rows is secondary; large datasets (D&D, Cora, PubMed, CiteSeer) drive the tail.

### Paper export (2410.10320, 9 datasets, 126 results)

| Component | Wall (profiler) | Notes |
|-----------|-----------------|-------|
| **`yaml.dump` in `_write_md`** | **~1.8 s** | Large `results` / `results_grouped` front matter |
| `_global_ranks_for_dataset` (via cache) | ~1.5 s | First touch per dataset/metric; cached after |
| MRR (`_compute_paper_mrr`) | ~0.06 s | No YAML |

675 exportable papers × ~0.1–0.5 s typical ≈ **~1 min** matches observed runs; tail papers with many datasets higher.

## What helps next (without splitting data out of DB)

| Idea | Effort | Impact |
|------|--------|--------|
| **Done:** batched `session_scope` | Low | Modest (~5–15%): fewer commits; datasets still YAML-bound |
| **Done:** eager loads on dataset `Result` query | Low | Small on large pages (fetch already cheap vs dump) |
| Faster YAML (e.g. `ruamel.yaml` C loader, or dump only summary in FM + keep table in template) | Medium | **Large** on dataset phase |
| Skip milestones for variants with &gt;N rows | Low | Small–medium on huge datasets |
| Precomputed global ranks table | High | Helps paper phase first-hit |

## Reproduce

```bash
uv sync --group dev

# Full export (batched session + timing summary)
uv run python -m backend.export_to_hugo

# Backfill params (tqdm)
uv run python scripts/backfill_result_params.py

# Wall-clock (production order, all 140 datasets then paper sample)
uv run python scripts/profile_export.py --papers 100 --seed 42 --skip-dev \
  --report logs/export_profile.json

# Line profiler
uv run python scripts/profile_export.py --line-profile-only --line-profile-dataset 51 \
  --skip-benchmarks --skip-dev --papers 0 --datasets 0 \
  --line-profile-output logs/export_dataset_51.lines.txt
```

## Artifacts

| File | Purpose |
|------|---------|
| `logs/export_dataset_51.lines.txt` | D&D line profile |
| `logs/export_dataset_37.lines.txt` | Cora (wrapper; use `*_impl.lines.txt` after profile script update) |
| `logs/export_paper_2410.lines.txt` | Slow paper line profile |
