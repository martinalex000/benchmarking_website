"""Seed the database from config/seed_data.yaml.

Idempotent: safe to run multiple times; existing records are updated, not duplicated.

Usage::
    python -m backend.seed_db
    python -m backend.seed_db --dry-run
"""

from __future__ import annotations

import argparse
import logging

import re
import yaml
from thefuzz import process as fuzz_process

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant, Paper

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


def _build_dataset_variant_lookup(session) -> dict[str, int]:
    lookup: dict[str, int] = {}
    for variant in session.query(DatasetVariant).all():
        lookup.setdefault(variant.name.lower(), variant.id)
        if variant.dataset:
            lookup.setdefault(variant.dataset.name.lower(), variant.id)
    return lookup


def _resolve_dataset_variant_quiet(dataset_name: str, variant_map: dict[str, int]) -> int | None:
    key = dataset_name.strip().lower()
    if not key:
        return None
    if key in variant_map:
        return variant_map[key]
    if variant_map:
        min_score = 85 if len(key) <= 6 else 75
        best_match, score = fuzz_process.extractOne(key, list(variant_map.keys()))
        if score >= min_score:
            return variant_map[best_match]
    return None


def _prune_pending_datasets(session) -> int:
    """Remove pending_datasets entries that now resolve against the DB."""
    pending_path = cfg.data_dir / "pending_datasets.yaml"
    if not pending_path.exists():
        return 0

    try:
        entries = yaml.safe_load(pending_path.read_text(encoding="utf-8")) or []
    except Exception as exc:
        logger.warning("Could not read %s for stale-pending cleanup: %s", pending_path, exc)
        return 0

    if not isinstance(entries, list) or not entries:
        return 0

    variant_map = _build_dataset_variant_lookup(session)
    kept_entries: list[dict] = []
    removed = 0
    for entry in entries:
        if not isinstance(entry, dict):
            kept_entries.append(entry)
            continue
        dataset_name = str(entry.get("dataset") or "").strip()
        if dataset_name and _resolve_dataset_variant_quiet(dataset_name, variant_map) is not None:
            removed += 1
            continue
        kept_entries.append(entry)

    if removed:
        pending_path.write_text(
            yaml.dump(kept_entries, allow_unicode=True, sort_keys=False, default_flow_style=False),
            encoding="utf-8",
        )
        logger.info(
            "Removed %d stale pending dataset entr%s from %s",
            removed,
            "y" if removed == 1 else "ies",
            pending_path,
        )
    return removed


def seed(dry_run: bool = False) -> None:
    init_db()

    data = yaml.safe_load(_SEED_FILE.read_text(encoding="utf-8"))

    with session_scope() as session:
        for bm_data in data.get("benchmarks", []):
            short_name = _short_name(bm_data["name"])
            bm_defaults = {
                "url": bm_data.get("url"),
                "description": bm_data.get("description"),
                "short_name": short_name,
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
                ds = _upsert(
                    session, Dataset, {"name": ds_data["name"], "benchmark_id": bm.id}, ds_defaults
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
        session.flush()

        if not dry_run:
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
