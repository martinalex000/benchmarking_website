"""Exercise application/undo on a temporary SQLite backup, never on its source."""

from __future__ import annotations

import argparse
import sqlite3
import tempfile
from pathlib import Path

from backend.config import cfg
from backend.mapping.plan import digest, read_json
from backend.mapping.storage import apply_plan, rollback_plan


def table_fingerprints(db: sqlite3.Connection) -> dict:
    tables = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' "
        "AND name NOT LIKE 'sqlite_%' AND name!='mapping_change_batches' ORDER BY name"
    ).fetchall()
    fingerprints = {}
    for (name,) in tables:
        quoted = name.replace('"', '""')
        rows = db.execute(f'SELECT * FROM "{quoted}" ORDER BY rowid').fetchall()
        fingerprints[name] = digest([tuple(row) for row in rows])
    return fingerprints


def validate_on_copy(database: Path, plan: dict) -> dict:
    with tempfile.TemporaryDirectory(prefix="mapping-storage-validation-") as temporary:
        copy_path = Path(temporary) / "validation.sqlite"
        with (
            sqlite3.connect(database.resolve().as_uri() + "?mode=ro", uri=True) as source,
            sqlite3.connect(copy_path) as db,
        ):
            source.backup(db)
            before = table_fingerprints(db)
            receipt = apply_plan(db, plan)
            assert apply_plan(db, plan)["already_applied"]
            rollback_plan(db, receipt["plan_id"])
            if table_fingerprints(db) != before:
                raise ValueError("Rollback did not restore all original database tables")
            return {
                "papers": len(plan["papers"]),
                "rows_applied_on_copy": len(receipt["rows"]),
                "idempotency_verified": True,
                "rollback_restored_all_original_tables": True,
                "source_database_opened_read_only": True,
            }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--database", type=Path, default=cfg.db_path)
    args = parser.parse_args()
    result = validate_on_copy(args.database, read_json(args.plan))
    print(
        f"Temporary-copy validation: {result['papers']} papers, "
        f"{result['rows_applied_on_copy']} applied rows; idempotency and full rollback passed. "
        "Source database opened read-only."
    )


if __name__ == "__main__":
    main()
