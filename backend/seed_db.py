"""Seed the database from config/seed_data.yaml.

Idempotent: safe to run multiple times; existing records are updated, not duplicated.

Usage::
    python -m backend.seed_db
    python -m backend.seed_db --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import re

import yaml

from backend.config import cfg
from backend.dataset_variant_resolver import (
    build_dataset_variant_lookup,
    resolve_dataset_variant_quiet,
)
from backend.db import init_db, session_scope
from backend.models import (
    Benchmark,
    Dataset,
    DatasetVariant,
    Paper,
    PaperDatasetStatistics,
    PendingDataset,
    Result,
)

logger = logging.getLogger(__name__)

_SEED_FILE = cfg.base_dir / "config" / "seed_data.yaml"


def _short_name(name: str) -> str:
    """Make a filesystem/identifier-friendly short name from a display name."""
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "benchmark"


def _merge_benchmark_aliases(session, alias_to_canonical: dict[str, str]) -> None:
    for alias_name, canonical_name in alias_to_canonical.items():
        alias = session.query(Benchmark).filter_by(name=alias_name).first()
        canonical = session.query(Benchmark).filter_by(name=canonical_name).first()
        if alias is None or canonical is None or alias.id == canonical.id:
            continue

        logger.info("Merging benchmark alias %s into %s", alias_name, canonical_name)
        for dataset in list(alias.datasets):
            existing = (
                session.query(Dataset)
                .filter_by(name=dataset.name, benchmark_id=canonical.id)
                .first()
            )
            if existing is not None:
                logger.warning(
                    "Skipping duplicate dataset during benchmark merge: %s already exists under %s",
                    dataset.name,
                    canonical_name,
                )
                continue
            dataset.benchmark_id = canonical.id

        session.flush()
        remaining = session.query(Dataset).filter_by(benchmark_id=alias.id).count()
        if remaining == 0:
            session.delete(alias)


def _migrate_pending_yaml_to_db(session) -> int:
    """Import legacy data/pending_datasets.yaml entries into pending_datasets table."""
    pending_path = cfg.data_dir / "pending_datasets.yaml"
    if not pending_path.exists():
        return 0

    try:
        entries = yaml.safe_load(pending_path.read_text(encoding="utf-8")) or []
    except Exception as exc:
        logger.warning("Could not read %s for stale-pending cleanup: %s", pending_path, exc)
        return 0

    if not isinstance(entries, list):
        return 0

    existing = {
        (arxiv_id, dataset_name)
        for arxiv_id, dataset_name in session.query(
            PendingDataset.arxiv_id,
            PendingDataset.dataset_name,
        ).all()
    }

    imported = 0
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        arxiv_id = str(entry.get("arxiv_id") or "").strip()
        dataset_name = str(entry.get("dataset") or "").strip()
        if not arxiv_id or not dataset_name:
            continue
        key = (arxiv_id, dataset_name)
        if key in existing:
            continue

        metrics_seen = entry.get("metrics_seen")
        if not isinstance(metrics_seen, list):
            metrics_seen = []

        suggestion = entry.get("suggestion")
        if not isinstance(suggestion, dict):
            suggestion = {}

        status = str(entry.get("status") or "pending").strip().lower() or "pending"

        session.add(
            PendingDataset(
                arxiv_id=arxiv_id,
                paper_title=str(entry.get("paper_title") or "").strip() or None,
                dataset_name=dataset_name,
                metrics_seen=json.dumps(metrics_seen, ensure_ascii=False),
                suggestion=json.dumps(suggestion, ensure_ascii=False),
                status=status,
            )
        )
        existing.add(key)
        imported += 1

    if imported:
        logger.info(
            "Imported %d legacy pending dataset entr%s from %s into DB",
            imported,
            "y" if imported == 1 else "ies",
            pending_path,
        )
    return imported


def _prune_pending_datasets(session) -> int:
    """Mark pending_datasets rows as resolved when they now map to canonical datasets."""
    rows = session.query(PendingDataset).all()
    if not rows:
        return 0

    variant_map = build_dataset_variant_lookup(session)
    updated = 0

    for row in rows:
        resolved_variant = resolve_dataset_variant_quiet(row.dataset_name or "", variant_map)
        resolved_dataset_id = (
            resolved_variant.dataset.id if resolved_variant and resolved_variant.dataset else None
        )

        if resolved_dataset_id is not None:
            if row.status != "resolved" or row.resolved_dataset_id != resolved_dataset_id:
                row.status = "resolved"
                row.resolved_dataset_id = resolved_dataset_id
                updated += 1
            continue

        if row.status == "resolved" or row.resolved_dataset_id is not None:
            row.status = "pending"
            row.resolved_dataset_id = None
            updated += 1

    if updated:
        logger.info(
            "Updated %d pending dataset entr%s status based on canonical DB coverage",
            updated,
            "y" if updated == 1 else "ies",
        )
    return updated


def _merge_film_alias_dataset(session) -> None:
    """Merge the heterophilic Film alias into Actor and preserve MovieLens Film."""
    film = session.query(Dataset).filter_by(name="Film").first()
    actor = session.query(Dataset).filter_by(name="Actor").first()
    movielens = session.query(Dataset).filter_by(name="MovieLens Film").first()
    if film is None or actor is None or movielens is None:
        return

    actor_variant = (
        session.query(DatasetVariant).filter_by(dataset_id=actor.id, name="Standard split").first()
    )
    movie_variant = (
        session.query(DatasetVariant)
        .filter_by(dataset_id=movielens.id, name="Standard split")
        .first()
    )
    if actor_variant is None or movie_variant is None:
        return

    moved = 0
    for variant in list(film.variants):
        for result in list(variant.results):
            target_variant = (
                movie_variant if result.paper.arxiv_id == "1609.04508" else actor_variant
            )
            duplicate = (
                session.query(Result)
                .filter_by(
                    paper_id=result.paper_id,
                    model_id=result.model_id,
                    dataset_variant_id=target_variant.id,
                    metric_name=result.metric_name,
                )
                .first()
            )
            if duplicate is not None:
                logger.info(
                    "Dropping duplicate Film result %s while merging into %s",
                    result.id,
                    target_variant.dataset.name,
                )
                session.delete(result)
            else:
                result.dataset_variant = target_variant
                moved += 1

        stats = (
            session.query(PaperDatasetStatistics)
            .filter_by(dataset_id=film.id, dataset_variant_id=variant.id)
            .all()
        )
        for stat in stats:
            target_dataset = movie_variant.dataset if stat.paper.arxiv_id == "1609.04508" else actor
            target_variant = movie_variant if target_dataset is movielens else actor_variant
            duplicate = (
                session.query(PaperDatasetStatistics)
                .filter_by(paper_id=stat.paper_id, dataset_id=target_dataset.id)
                .first()
            )
            if duplicate is not None:
                session.delete(stat)
            else:
                stat.dataset = target_dataset
                stat.dataset_variant = target_variant

    session.flush()
    logger.info("Merged %d Film result rows into Actor/MovieLens Film", moved)
    session.delete(film)
    session.flush()


def _move_dataset_to_benchmark(
    session, dataset_name: str, source_name: str, target_name: str
) -> None:
    """Move a named dataset when a seed group was corrected after initial import."""
    source = session.query(Benchmark).filter_by(name=source_name).first()
    target = session.query(Benchmark).filter_by(name=target_name).first()
    if target is None:
        return
    if source is None:
        dataset = (
            session.query(Dataset).filter_by(name=dataset_name, benchmark_id=target.id).first()
        )
        if dataset is not None and dataset_name == "Deezer":
            dataset.description = (
                "Deezer Europe user friendship graph binary node classification (like/dislike), "
                "used in LINKX-style non-homophily evaluations."
            )
        return
    dataset = session.query(Dataset).filter_by(name=dataset_name, benchmark_id=source.id).first()
    if dataset is None:
        dataset = (
            session.query(Dataset).filter_by(name=dataset_name, benchmark_id=target.id).first()
        )
        if dataset is not None and dataset_name == "Deezer":
            dataset.description = (
                "Deezer Europe user friendship graph binary node classification (like/dislike), "
                "used in LINKX-style non-homophily evaluations."
            )
        return
    existing = session.query(Dataset).filter_by(name=dataset_name, benchmark_id=target.id).first()
    if existing is None:
        dataset.benchmark_id = target.id
        if dataset_name == "Deezer":
            dataset.description = (
                "Deezer Europe user friendship graph binary node classification (like/dislike), "
                "used in LINKX-style non-homophily evaluations."
            )
        logger.info("Moved dataset %s from %s to %s", dataset_name, source_name, target_name)
    else:
        logger.warning(
            "Keeping existing %s under %s; stale %s remains under %s",
            dataset_name,
            target_name,
            dataset_name,
            source_name,
        )


def _remove_empty_dataset(session, dataset_name: str, benchmark_name: str) -> None:
    """Remove a stale empty duplicate that would collide on the public slug."""
    benchmark = session.query(Benchmark).filter_by(name=benchmark_name).first()
    if benchmark is None:
        return
    dataset = session.query(Dataset).filter_by(name=dataset_name, benchmark_id=benchmark.id).first()
    if dataset is None:
        return
    has_results = (
        session.query(Result)
        .join(DatasetVariant, Result.dataset_variant_id == DatasetVariant.id)
        .filter(DatasetVariant.dataset_id == dataset.id)
        .first()
        is not None
    )
    has_stats = session.query(PaperDatasetStatistics).filter_by(dataset_id=dataset.id).first()
    if not has_results and has_stats is None:
        logger.info("Removing empty duplicate dataset %s from %s", dataset_name, benchmark_name)
        session.delete(dataset)


def _upsert_seed_dataset(
    session,
    benchmark: Benchmark,
    ds_data: dict,
    defaults: dict,
    move_from_benchmark: str | None = None,
) -> Dataset:
    """Create/update a dataset, optionally moving it from an old benchmark group."""
    dataset_name = ds_data["name"]
    ds = session.query(Dataset).filter_by(name=dataset_name, benchmark_id=benchmark.id).first()
    if ds is None and move_from_benchmark:
        source = session.query(Benchmark).filter_by(name=move_from_benchmark).first()
        if source is not None:
            ds = session.query(Dataset).filter_by(name=dataset_name, benchmark_id=source.id).first()
            if ds is not None:
                logger.info(
                    "Moving dataset %s from benchmark %s to %s",
                    dataset_name,
                    source.name,
                    benchmark.name,
                )
                ds.benchmark_id = benchmark.id

    if ds is None:
        ds = Dataset(name=dataset_name, benchmark_id=benchmark.id, **defaults)
        session.add(ds)
        session.flush()
    else:
        for key, value in defaults.items():
            if value is not None:
                setattr(ds, key, value)
    return ds


def seed(dry_run: bool = False) -> None:
    init_db()

    data = yaml.safe_load(_SEED_FILE.read_text(encoding="utf-8"))

    with session_scope() as session:
        for bm_data in data.get("benchmarks", []):
            short_name = _short_name(bm_data["name"])
            bm_defaults = {
                "url": bm_data.get("url"),
                "description": bm_data.get("description"),
                "source_papers": json.dumps(bm_data.get("source_papers", []), ensure_ascii=False),
                "short_name": short_name,
                "is_legacy": 1 if bm_data.get("is_legacy") else 0,
            }
            bm = _upsert(session, Benchmark, {"name": bm_data["name"]}, bm_defaults)
            logger.info("Benchmark: %s (id=%s)", bm.name, bm.id)

            # If an arXiv id is provided, ensure a Paper exists and link it
            arxiv_id = bm_data.get("arxiv_id")
            if arxiv_id:
                paper_defaults = {"title": bm.name, "is_benchmark_paper": 1}
                paper = _upsert(session, Paper, {"arxiv_id": arxiv_id}, paper_defaults)
                bm.paper_id = paper.id
                session.flush()

            for source in bm_data.get("source_papers", []):
                source_arxiv_id = str(source.get("arxiv_id") or "").strip()
                if not source_arxiv_id:
                    continue
                paper_defaults = {
                    "title": str(source.get("title") or bm.name),
                    "is_benchmark_paper": 1,
                }
                _upsert(session, Paper, {"arxiv_id": source_arxiv_id}, paper_defaults)

            for ds_data in bm_data.get("datasets", []):
                ds_defaults = {
                    "task_type": ds_data.get("task_type"),
                    "description": ds_data.get("description"),
                    "primary_metric": ds_data.get("primary_metric"),
                    "higher_is_better": 1 if ds_data.get("higher_is_better", True) else 0,
                    "domain": ds_data.get("domain"),
                    "pyg_url": ds_data.get("pyg_url"),
                    "num_graphs": ds_data.get("num_graphs"),
                    "avg_nodes": ds_data.get("avg_nodes"),
                    "avg_edges": ds_data.get("avg_edges"),
                    "num_classes": ds_data.get("num_classes"),
                }
                ds = _upsert_seed_dataset(
                    session,
                    bm,
                    ds_data,
                    ds_defaults,
                    bm_data.get("move_datasets_from"),
                )
                logger.info("  Dataset: %s (id=%s)", ds.name, ds.id)

                seen_variant_names: set[str] = set()
                for v_data in ds_data.get("variants", []):
                    seen_variant_names.add(v_data["name"])
                    v_defaults = {
                        "description": v_data.get("description"),
                        "num_graphs": v_data.get("num_graphs"),
                        "avg_nodes": v_data.get("avg_nodes"),
                        "avg_edges": v_data.get("avg_edges"),
                        "label_fraction": v_data.get("label_fraction"),
                        "split_type": v_data.get("split_type"),
                        "is_standard": 1 if v_data.get("is_standard", False) else 0,
                        "notes": v_data.get("notes"),
                    }
                    v = _upsert(
                        session,
                        DatasetVariant,
                        {"name": v_data["name"], "dataset_id": ds.id},
                        v_defaults,
                    )
                    logger.info("    Variant: %s (is_standard=%s)", v.name, v.is_standard)

                for existing_variant in list(ds.variants):
                    if existing_variant.name not in seen_variant_names:
                        logger.info("    Removing stale variant: %s", existing_variant.name)
                        session.delete(existing_variant)

        _merge_benchmark_aliases(session, {"TUDataset": "TU Dortmund"})
        _move_dataset_to_benchmark(session, "Deezer", "Heterophilic Graphs", "LINKX Benchmarks")
        _remove_empty_dataset(session, "Deezer", "Hypergraph Benchmarks")
        _merge_film_alias_dataset(session)
        session.flush()

        if not dry_run:
            _migrate_pending_yaml_to_db(session)
            _prune_pending_datasets(session)

        if dry_run:
            session.rollback()
            logger.info("Dry run — no changes committed")
        else:
            logger.info("Seed complete")


def _upsert(session, Model, lookup: dict, defaults: dict):
    """Get-or-create with update of defaults."""
    obj = session.query(Model).filter_by(**lookup).first()
    if obj is None:
        obj = Model(**lookup, **defaults)
        session.add(obj)
        session.flush()
    else:
        for k, v in defaults.items():
            if v is not None:
                setattr(obj, k, v)
    return obj


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Seed the database from config/seed_data.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    seed(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
