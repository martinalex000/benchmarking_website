"""Seed the database from config/seed_data.yaml.

Idempotent: safe to run multiple times; existing records are updated, not duplicated.

Usage::
    python -m backend.seed_db
    python -m backend.seed_db --dry-run
"""
from __future__ import annotations

import argparse
import logging

import yaml

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Benchmark, Dataset, DatasetVariant

logger = logging.getLogger(__name__)

_SEED_FILE = cfg.base_dir / "config" / "seed_data.yaml"


def seed(dry_run: bool = False) -> None:
    init_db()

    data = yaml.safe_load(_SEED_FILE.read_text(encoding="utf-8"))

    with session_scope() as session:
        for bm_data in data.get("benchmarks", []):
            bm = _upsert(
                session, Benchmark,
                {"name": bm_data["name"]},
                {
                    "arxiv_id": bm_data.get("arxiv_id"),
                    "url": bm_data.get("url"),
                    "description": bm_data.get("description"),
                },
            )
            logger.info("Benchmark: %s (id=%s)", bm.name, bm.id)

            for ds_data in bm_data.get("datasets", []):
                ds = _upsert(
                    session, Dataset,
                    {"name": ds_data["name"], "benchmark_id": bm.id},
                    {
                        "task_type": ds_data.get("task_type"),
                        "description": ds_data.get("description"),
                        "primary_metric": ds_data.get("primary_metric"),
                        "higher_is_better": ds_data.get("higher_is_better", True),
                        "domain": ds_data.get("domain"),
                    },
                )
                logger.info("  Dataset: %s (id=%s)", ds.name, ds.id)

                for v_data in ds_data.get("variants", []):
                    v = _upsert(
                        session, DatasetVariant,
                        {"name": v_data["name"], "dataset_id": ds.id},
                        {
                            "is_standard": v_data.get("is_standard", False),
                            "notes": v_data.get("notes"),
                        },
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
