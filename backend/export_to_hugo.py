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


def _write_md(path: Path, front_matter: dict, body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm_str = yaml.dump(front_matter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    path.write_text(f"---\n{fm_str}---\n\n{body}", encoding="utf-8")


# ── Paper export ──────────────────────────────────────────────────────────────


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

        # Group results by dataset name
        result_groups: dict[str, list[dict]] = {}
        for r in results:
            dv = r.dataset_variant
            ds_name = dv.dataset.name if dv else "Unknown"
            result_groups.setdefault(ds_name, []).append(
                {
                    "model": r.model.canonical_name if r.model else "",
                    "value": float(r.display_value) if r.display_value is not None else None,
                    "std": float(r.metric_std) if r.metric_std else None,
                    "metric": r.metric_name,
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

        results_for_fm: list[dict] = [
            {"dataset": ds, "rows": rows} for ds, rows in sorted(result_groups.items())
        ]

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
            "published_date": str(paper.published_date) if paper.published_date else "",
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
            results_raw = (
                session.query(Result)
                .filter_by(dataset_variant_id=v.id)
                .filter(Result.is_problematic.is_(None) | (Result.is_problematic == 0))
                .all()
            )

            if not results_raw:
                continue

            metric = primary_metric or (results_raw[0].metric_name if results_raw else "")
            if not primary_metric:
                primary_metric = metric
            higher_is_better = bool(results_raw[0].higher_is_better) if results_raw else True

            # Sort by value
            sorted_results = sorted(
                [r for r in results_raw if r.display_value is not None],
                key=lambda r: float(r.display_value),
                reverse=higher_is_better,
            )

            rows: list[dict] = []
            for r in sorted_results:
                paper = r.paper
                rows.append(
                    {
                        "model": r.model.canonical_name if r.model else "",
                        "value": float(r.display_value),
                        "std": float(r.metric_std) if r.metric_std else None,
                        "is_baseline": bool(r.is_baseline),
                        "is_overridden": bool(r.is_overridden),
                        "override_reason": r.override_reason or "",
                        "params_millions": (
                            r.model.size_params / 1_000_000
                            if r.model and r.model.size_params
                            else None
                        ),
                        "arxiv_id": paper.arxiv_id if paper else "",
                        "title": paper.title if paper else "",
                        "date": str(paper.published_date) if paper and paper.published_date else "",
                        "codebase_url": paper.codebase_url or "",
                    }
                )

            milestones = get_best_results_over_time(v.id, metric)

            variant_data.append(
                {
                    "slug": _slug(v.name),
                    "name": v.name,
                    "notes": v.notes or "",
                    "is_standard": bool(v.is_standard),
                    "results": rows,
                    "milestones_json": json.dumps(milestones),
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
                    "arxiv_id": b.arxiv_id or "",
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
    for arxiv_id in paper_ids:
        if export_paper(arxiv_id):
            ok += 1

    logger.info("Exported %d/%d papers", ok, len(paper_ids))

    ds_ok = sum(1 for did in dataset_ids if export_dataset(did))
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
