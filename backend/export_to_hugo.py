"""Export DB contents to Hugo markdown content files.

Generates:
  site/content/papers/{arxiv_id}/index.md
  site/content/datasets/{dataset_slug}/index.md
  site/data/benchmarks.json

Also copies main figures to site/static/figures/{arxiv_id}/

Usage::
    python -m backend.export_to_hugo
    python -m backend.export_to_hugo --paper 2206.08164
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from backend.baseline_aggregator import get_baseline_summary, get_best_results_over_time
from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Paper, Result
from backend.paper_storage import PaperStorage

logger = logging.getLogger(__name__)

_SITE_DIR = cfg.base_dir / "site"
_CONTENT = _SITE_DIR / "content"
_DATA_DIR = _SITE_DIR / "data"
_STATIC = _SITE_DIR / "static"


# ── Helpers ───────────────────────────────────────────────────────────────────


def _slug(name: str) -> str:
    """Convert a string to a URL-safe slug."""
    return re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")


def _fmt_date(date_str: str | None) -> str:
    """Format a YYYY-MM-DD date string as 'Mon YYYY' (e.g. 'Jun 2022'). Returns '' on failure."""
    if not date_str:
        return ""
    try:
        return datetime.fromisoformat(date_str[:10]).strftime("%b %Y")
    except ValueError:
        return date_str


def _write_md(path: Path, front_matter: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_str = yaml.dump(front_matter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    path.write_text(f"---\n{fm_str}---\n\n{body}", encoding="utf-8")


# ── Paper export ──────────────────────────────────────────────────────────────


def _pivot_paper_rows(rows: list[dict], primary_metric: str | None) -> dict:
    """Pivot flat per-metric paper rows into multi-metric format (like dataset pages).

    Input rows have fields: model, value, std, metric, is_baseline, params_millions, …
    Output has each model once with metric_values / metric_stds parallel arrays.
    """
    # Collect metrics in order of first appearance; primary goes first
    seen_metrics: list[str] = list(dict.fromkeys(r["metric"] for r in rows if r.get("metric")))
    if primary_metric and primary_metric in seen_metrics:
        seen_metrics = [primary_metric] + [m for m in seen_metrics if m != primary_metric]
    elif not primary_metric and seen_metrics:
        primary_metric = seen_metrics[0]

    # Group by model (first appearance determines metadata)
    seen_models: list[str] = []
    model_first: dict[str, dict] = {}
    model_vals: dict[str, dict[str, tuple]] = {}  # model -> {metric -> (val, std)}
    for r in rows:
        model = r.get("model") or ""
        if model not in model_first:
            seen_models.append(model)
            model_first[model] = r
            model_vals[model] = {}
        m = r.get("metric") or ""
        if m and m not in model_vals[model]:
            model_vals[model][m] = (r.get("value"), r.get("std"))

    # Sort by primary metric value
    higher = bool(rows[0].get("higher_is_better", True)) if rows else True

    def _sort_key(model: str) -> tuple:
        pval = model_vals[model].get(primary_metric or "", (None, None))[0]
        if pval is None:
            return (1, 0.0)
        return (0, -pval if higher else pval)

    seen_models.sort(key=_sort_key)

    pivoted: list[dict] = []
    for model in seen_models:
        first = model_first[model]
        metric_values = [model_vals[model].get(m, (None, None))[0] for m in seen_metrics]
        metric_stds = [model_vals[model].get(m, (None, None))[1] for m in seen_metrics]
        pivoted.append(
            {
                "model": model,
                "metric_values": metric_values,
                "metric_stds": metric_stds,
                "is_baseline": first.get("is_baseline", False),
                "is_overridden": first.get("is_overridden", False),
                "override_reason": first.get("override_reason", ""),
                "params_millions": first.get("params_millions"),
            }
        )

    return {"rows": pivoted, "metrics": seen_metrics, "primary_metric": primary_metric}


def export_paper(arxiv_id: str) -> bool:
    """Export a single paper's page to Hugo content."""
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        if paper is None:
            logger.warning("Paper arXiv:%s not found in DB", arxiv_id)
            return False

        results = (
            session.query(Result)
            .filter_by(paper_id=paper.id)
            .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
            .all()
        )

        # Group results by dataset name, tracking metric/direction per group
        result_groups: dict[str, list[dict]] = {}
        result_group_meta: dict[str, dict] = {}
        for r in results:
            dv = r.dataset_variant
            ds_name = dv.dataset.name if dv else "Unknown"
            if ds_name not in result_group_meta:
                # Prefer the dataset's declared primary_metric over the first result's metric
                primary = (
                    dv.dataset.primary_metric
                    if dv and dv.dataset and dv.dataset.primary_metric
                    else r.metric_name
                )
                result_group_meta[ds_name] = {
                    "metric": primary,
                    "higher_is_better": bool(r.higher_is_better),
                }
            result_groups.setdefault(ds_name, []).append(
                {
                    "model": r.model.canonical_name if r.model else "",
                    "value": float(r.display_value) if r.display_value is not None else None,
                    "std": float(r.metric_std) if r.metric_std else None,
                    "metric": r.metric_name,
                    "higher_is_better": bool(r.higher_is_better),
                    "is_baseline": bool(r.is_baseline),
                    "is_overridden": bool(r.is_overridden),
                    "override_reason": r.override_reason or "",
                    "params_millions": (
                        r.model.size_params / 1_000_000 if r.model and r.model.size_params else None
                    ),
                    "table_ref": r.table_ref or "",
                    "source_ref": r.source_ref or "",
                }
            )

        results_for_fm: list[dict] = []
        for ds, rows in sorted(result_groups.items()):
            meta = result_group_meta[ds]
            distinct_metrics = list(dict.fromkeys(r["metric"] for r in rows if r.get("metric")))
            if len(distinct_metrics) > 1:
                pivoted = _pivot_paper_rows(rows, meta["metric"])
                results_for_fm.append(
                    {
                        "dataset": ds,
                        "is_multi_metric": True,
                        "rows": pivoted["rows"],
                        "metrics": pivoted["metrics"],
                        "primary_metric": pivoted["primary_metric"],
                        "higher_is_better": meta["higher_is_better"],
                    }
                )
            else:
                results_for_fm.append(
                    {
                        "dataset": ds,
                        "rows": rows,
                        "metric": meta["metric"],
                        "higher_is_better": meta["higher_is_better"],
                    }
                )

        # Main figure
        storage = PaperStorage(arxiv_id)
        main_figure_hugo: str | None = None
        if storage.main_figure_path and storage.main_figure_path.exists():
            dest = _STATIC / "figures" / arxiv_id / storage.main_figure_path.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(storage.main_figure_path, dest)
            main_figure_hugo = f"/figures/{arxiv_id}/{storage.main_figure_path.name}"

        front_matter: dict[str, Any] = {
            "title": paper.title or arxiv_id,
            "arxiv_id": arxiv_id,
            "authors": paper.authors or [],
            "published_date": _fmt_date(paper.published_date),
            "abstract": paper.abstract or "",
            "codebase_url": paper.codebase_url or "",
            "extraction_model": paper.extraction_model or "",
            "results": results_for_fm,
        }
        if main_figure_hugo:
            front_matter["main_figure"] = main_figure_hugo

        out_path = _CONTENT / "papers" / arxiv_id / "index.md"
        _write_md(out_path, front_matter)
        logger.info("Exported paper %s → %s", arxiv_id, out_path)
        return True


# ── Dataset export ────────────────────────────────────────────────────────────


def _build_multi_metric_rows(
    all_results: list,
    primary_metric: str,
) -> tuple[list[str], bool, list[dict]]:
    """Pivot results by (canonical_model_name, arxiv_id) to produce a multi-metric table.

    Returns:
        metrics_ordered  – metric names, primary metric first then alphabetically
        higher_is_better – derived from primary metric rows
        rows             – one dict per (model, paper) with parallel metric_values / metric_stds
    """
    # Discover all distinct metrics; primary goes first
    metric_set: set[str] = {r.metric_name for r in all_results}
    metrics_ordered = sorted(metric_set - {primary_metric})
    if primary_metric in metric_set:
        metrics_ordered = [primary_metric] + metrics_ordered

    # higher_is_better from the primary metric rows
    hib = True
    for r in all_results:
        if r.metric_name == primary_metric and r.higher_is_better is not None:
            hib = bool(r.higher_is_better)
            break

    # Group by (canonical_model_name, arxiv_id)
    groups: dict[tuple, dict] = {}
    for r in all_results:
        model_name = r.model.canonical_name if r.model else ""
        paper = r.paper
        arxiv_id = paper.arxiv_id if paper else ""
        key = (model_name, arxiv_id)
        if key not in groups:
            groups[key] = {
                "model": model_name,
                "is_baseline": bool(r.is_baseline),
                "is_overridden": bool(r.is_overridden),
                "override_reason": r.override_reason or "",
                "params_millions": (
                    r.model.size_params / 1_000_000 if r.model and r.model.size_params else None
                ),
                "arxiv_id": arxiv_id,
                "title": paper.title if paper else "",
                "date": _fmt_date(paper.published_date) if paper else "",
                "date_iso": (paper.published_date[:10] if paper and paper.published_date else ""),
                "codebase_url": paper.codebase_url or "",
                "uses_external_data": None,
                "_vals": {},
            }
        # uses_external_data: prefer True > False > None across metrics for this (model, paper)
        ued = r.uses_external_data
        if ued == 1:
            groups[key]["uses_external_data"] = True
        elif ued == 0 and groups[key]["uses_external_data"] is None:
            groups[key]["uses_external_data"] = False
        val = float(r.display_value) if r.display_value is not None else None
        std = float(r.metric_std) if r.metric_std is not None else None
        groups[key]["_vals"][r.metric_name] = (val, std)

    # Sort by primary metric value
    def _sort_key(g: dict) -> tuple:
        pval = g["_vals"].get(primary_metric, (None, None))[0]
        if pval is None:
            return (1, 0.0)
        return (0, -pval if hib else pval)

    sorted_groups = sorted(groups.values(), key=_sort_key)

    rows: list[dict] = []
    for g in sorted_groups:
        metric_values = []
        metric_stds = []
        for m in metrics_ordered:
            val, std = g["_vals"].get(m, (None, None))
            metric_values.append(val)
            metric_stds.append(std)
        row = {k: v for k, v in g.items() if k != "_vals"}
        row["metric_values"] = metric_values
        row["metric_stds"] = metric_stds
        rows.append(row)

    return metrics_ordered, hib, rows


def export_dataset(dataset_id: int) -> bool:
    """Export a dataset page with all variants and leaderboard data."""
    with session_scope() as session:
        ds = session.get(Dataset, dataset_id)
        if ds is None:
            return False

        variants = (
            session.query(DatasetVariant)
            .filter_by(dataset_id=dataset_id)
            .order_by(DatasetVariant.is_standard.desc(), DatasetVariant.name)
            .all()
        )

        if not variants:
            logger.debug("Dataset %s has no variants — skipping export", ds.name)
            return False

        # Determine primary metric from the first variant that has results
        primary_metric = ds.primary_metric or ""
        higher_is_better = True

        variant_data: list[dict] = []
        for v in variants:
            all_results = (
                session.query(Result)
                .filter_by(dataset_variant_id=v.id)
                .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
                .all()
            )

            if not all_results:
                continue

            # Determine which metric to display: prefer primary_metric if it exists in results
            available_metrics = {r.metric_name for r in all_results}
            if primary_metric and primary_metric in available_metrics:
                metric = primary_metric
            else:
                # Fall back to the most-common metric among results
                from collections import Counter

                metric = Counter(r.metric_name for r in all_results).most_common(1)[0][0]
                if not primary_metric:
                    primary_metric = metric

            # Build pivoted multi-metric rows (primary metric first, then sorted)
            metrics_ordered, higher_is_better, rows = _build_multi_metric_rows(all_results, metric)

            milestones = get_best_results_over_time(v.id, metric)

            variant_data.append(
                {
                    "slug": _slug(v.name),
                    "name": v.name,
                    "notes": v.notes or "",
                    "is_standard": bool(v.is_standard),
                    "primary_metric": metric,
                    "higher_is_better": higher_is_better,
                    "metrics": metrics_ordered,
                    "rows": rows,
                    "milestones": milestones,
                }
            )

        if not variant_data:
            return False

        benchmark_name = ds.benchmark.name if ds.benchmark else ""
        front_matter: dict[str, Any] = {
            "title": ds.name,
            "slug": _slug(ds.name),
            "benchmark": benchmark_name,
            "task_type": ds.task_type or "",
            "description": ds.description or "",
            "primary_metric": primary_metric,
            "higher_is_better": higher_is_better,
            "pyg_url": ds.pyg_url or "",
            "stats": (
                {
                    "num_graphs": ds.num_graphs,
                    "avg_nodes": round(ds.avg_nodes, 2) if ds.avg_nodes is not None else None,
                    "avg_edges": round(ds.avg_edges, 2) if ds.avg_edges is not None else None,
                    "num_classes": ds.num_classes,
                }
                if any(
                    x is not None
                    for x in [ds.num_graphs, ds.avg_nodes, ds.avg_edges, ds.num_classes]
                )
                else None
            ),
            "variants": variant_data,
        }

        out_path = _CONTENT / "datasets" / _slug(ds.name) / "index.md"
        _write_md(out_path, front_matter)
        logger.info("Exported dataset %s → %s", ds.name, out_path)
        return True


# ── Benchmark data file ───────────────────────────────────────────────────────


def export_benchmarks_data() -> None:
    """Write site/data/benchmarks.json for the homepage."""
    _DATA_DIR.mkdir(parents=True, exist_ok=True)

    with session_scope() as session:
        benchmarks = session.query(Benchmark).all()
        data: list[dict] = []
        for b in benchmarks:
            datasets_info = []
            for ds in b.datasets:
                variants = [v for v in ds.variants if v.is_standard]
                datasets_info.append(
                    {
                        "name": ds.name,
                        "slug": _slug(ds.name),
                        "task_type": ds.task_type or "",
                        "variants": [{"name": v.name, "slug": _slug(v.name)} for v in variants],
                    }
                )
            data.append(
                {
                    "name": b.name,
                    "slug": _slug(b.name),
                    "description": b.description or "",
                    "arxiv_id": b.paper.arxiv_id if b.paper else "",
                    "paper_title": b.paper.title if b.paper else "",
                    "datasets": datasets_info,
                }
            )

    (_DATA_DIR / "benchmarks.json").write_text(
        json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("Wrote %s", _DATA_DIR / "benchmarks.json")


# ── Full export ───────────────────────────────────────────────────────────────


def export_all(arxiv_ids: list[str] | None = None) -> None:
    """Export all papers and datasets (or just the specified papers)."""
    from tqdm import tqdm

    init_db()

    export_benchmarks_data()

    with session_scope() as session:
        if arxiv_ids:
            papers = session.query(Paper).filter(Paper.arxiv_id.in_(arxiv_ids)).all()
        else:
            papers = session.query(Paper).all()
        paper_ids = [p.arxiv_id for p in papers]

        dataset_ids = [ds.id for ds in session.query(Dataset).all()]

    ok = 0
    for arxiv_id in tqdm(paper_ids, desc="Exporting papers", unit="paper", leave=True):
        if export_paper(arxiv_id):
            tqdm.write(f"  ✓  {arxiv_id}")
            ok += 1
        else:
            tqdm.write(f"  ✗  {arxiv_id}  (skipped — no results)")

    logger.info("Exported %d/%d papers", ok, len(paper_ids))

    ds_ok = 0
    for did in tqdm(dataset_ids, desc="Exporting datasets", unit="dataset", leave=True):
        if export_dataset(did):
            ds_ok += 1

    logger.info("Exported %d/%d datasets", ds_ok, len(dataset_ids))


# ── CLI ───────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Export DB to Hugo content files")
    parser.add_argument(
        "--paper", "-p", nargs="+", metavar="ARXIV_ID", help="Export only specific papers"
    )
    args = parser.parse_args(argv)
    export_all(arxiv_ids=args.paper)


if __name__ == "__main__":
    main()
