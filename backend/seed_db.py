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
                }
                ds = _upsert(
                    session, Dataset, {"name": ds_data["name"], "benchmark_id": bm.id}, ds_defaults
                )
                logger.info("  Dataset: %s (id=%s)", ds.name, ds.id)

                for v_data in ds_data.get("variants", []):
                    v_defaults = {
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
