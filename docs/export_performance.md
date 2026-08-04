# Hugo export performance

## Current re-profile: 2026-08-03

Caching the dataset-to-paper mapping fixed the dominant paper-path regression. The
remaining paper cost is now concentrated in first-touch ranking, at-publication history,
and MRR queries.

### Evidence

The production-order harness was run against the current database (2,740 papers, 1,341
exportable papers, 64,413 result rows), using the same 50-paper sample before and after
the cache change:

| Measurement | Before cache | After cache |
|---|---:|---:|
| Result-bearing papers | 25 | 25 |
| Paper phase total | 51.90 s | 6.28 s |
| Mean / median | 2.08 s / 2.49 s | 0.25 s / 0.074 s |
| P90 / maximum | 3.30 s / 4.07 s | 0.54 s / 2.50 s |

The cache adds a one-time 3.12 s benchmark-phase cost to build the mapping. That is a
single export-run cost instead of a repeated cost for every paper.

The production-warm instrumentation run for paper `2310.13845` fell from 4.42 s to
2.43 s. The cached paper-path breakdown is:

| Component | Calls | Time | Finding |
|---|---:|---:|---|
| `_dataset_paper_ids` | 1 | ~0 s | Cache hit; the mapping is built once in the benchmark phase |
| `_global_ranks_for_dataset` | 7 | 0.74 s | First-touch global model rankings |
| `_global_best_per_model_as_of_date_excluding_paper` | 7 | 0.94 s | Reads/builds at-publication timelines |
| `_dataset_paper_count_for_metric` | 7 | 0.69 s | Additional full result queries used by MRR |
| `_compute_paper_mrr` | 1 | 0.70 s | Includes the per-dataset MRR queries above |
| `_write_md` | 1 | 0.02 s | YAML front matter is not the current dominant cost |

The component timings overlap when nested, so they must not be summed. A cProfile run
confirms the original shape: `_dataset_paper_ids` was the largest single operation,
followed by ORM result loading and `result_is_leaderboard_eligible` evaluation. It is
now cached at the existing export-cache boundary. The call originates from
[`_export_paper_impl`](../backend/export_to_hugo.py) while building benchmark/dataset
ordering, near line 2723.

### What slows it down

1. The first paper touching each dataset/metric pays for global ranking and
   at-publication history queries. These are cached across the run, but the caches are
   not precomputed and the MRR path also issues per-dataset paper-count queries.
2. The historical YAML bottleneck remains relevant for large dataset pages, as recorded
   below, but it does not explain the current paper slowdown.

### Recommended fix order

1. Reduce the one-time paper-ID query to scalar `dataset_id, paper_id` rows and push the stable filters
   (`is_standard`, `protocol_decision`, problematic status) into SQL. Preserve the
   remaining curation rules in a narrowly scoped eligibility pass.
2. Precompute/cache dataset paper counts and, if paper export remains expensive after
   that, prewarm global ranks and at-publication timelines once per dataset/metric.
3. Keep YAML optimizations as a separate dataset-page project; they are not the first
   lever for the current paper regression.

The older profiling harness output in `logs/export_profile_final_20260711.json` reported
a much lower median because it included many papers with no exportable results and came
from before the current paper-ordering work. It should not be used as the current
per-paper baseline.

Historical baseline last updated: **2026-06-03** (batched DB sessions, line_profiler on
datasets + papers).

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
