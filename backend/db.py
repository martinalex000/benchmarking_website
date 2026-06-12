"""Database connection and session management."""

from __future__ import annotations

import re
from collections.abc import Generator
from contextlib import contextmanager
from dataclasses import dataclass

from sqlalchemy import create_engine, event, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from backend.config import cfg
from backend.models import Base

# Safe SQL identifier: starts with letter/underscore, then alphanumerics + underscores
_SQL_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _validate_sql_identifier(name: str, kind: str = "identifier") -> str:
    if not _SQL_IDENTIFIER_RE.match(name):
        raise ValueError(f"Unsafe SQL {kind}: {name!r}")
    return name


def _get_engine(db_path: str | None = None) -> Engine:
    path = db_path or str(cfg.db_path)
    engine = create_engine(
        f"sqlite:///{path}",
        connect_args={"check_same_thread": False},
        echo=False,
    )
    return engine


# Enable WAL mode and foreign keys for every new SQLite connection
@event.listens_for(Engine, "connect")
def _set_sqlite_pragmas(dbapi_conn, _connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("PRAGMA journal_mode = WAL")
    cursor.close()


# Module-level engine and session factory (lazy-initialised)
_engine: Engine | None = None
_SessionFactory: sessionmaker | None = None


@dataclass(frozen=True)
class Migration:
    name: str
    apply: callable


def _migration_results_additional_columns(engine: Engine) -> None:
    _add_column_if_missing(engine, "results", "uses_external_data", "INTEGER")
    _add_column_if_missing(engine, "results", "variant_inference_reason", "TEXT")


def _migration_pending_datasets_columns(engine: Engine) -> None:
    _add_column_if_missing(engine, "pending_datasets", "paper_title", "TEXT")
    _add_column_if_missing(engine, "pending_datasets", "metrics_seen", "TEXT")
    _add_column_if_missing(engine, "pending_datasets", "suggestion", "TEXT")
    _add_column_if_missing(engine, "pending_datasets", "status", "TEXT")
    _add_column_if_missing(
        engine,
        "pending_datasets",
        "resolved_dataset_id",
        "INTEGER REFERENCES datasets(id) ON DELETE SET NULL",
    )
    _add_column_if_missing(engine, "pending_datasets", "updated_at", "TEXT")


def _migration_todo_queue_columns(engine: Engine) -> None:
    _add_column_if_missing(engine, "todo_papers", "cited_by_count", "INTEGER NOT NULL DEFAULT 0")
    _add_column_if_missing(
        engine,
        "todo_papers",
        "cites_existing_count",
        "INTEGER NOT NULL DEFAULT 0",
    )
    _add_column_if_missing(engine, "todo_papers", "seen_count", "INTEGER NOT NULL DEFAULT 0")
    _add_column_if_missing(engine, "todo_papers", "seen_from", "TEXT")
    _add_column_if_missing(engine, "todo_papers", "first_seen_at", "TEXT")
    _add_column_if_missing(
        engine, "todo_papers", "is_manually_important", "INTEGER NOT NULL DEFAULT 0"
    )


def _migration_todo_queue_indexes(engine: Engine) -> None:
    _ensure_index(
        engine,
        "idx_todo_created_at",
        "CREATE INDEX IF NOT EXISTS idx_todo_created_at ON todo_papers(created_at)",
    )
    _ensure_index(
        engine,
        "idx_todo_seen_count",
        "CREATE INDEX IF NOT EXISTS idx_todo_seen_count ON todo_papers(seen_count)",
    )


def _migration_results_model_metadata(engine: Engine) -> None:
    _add_column_if_missing(engine, "results", "params_millions", "REAL")


def _migration_dataset_extra_stats(engine: Engine) -> None:
    _add_column_if_missing(engine, "datasets", "extra_stats", "TEXT")
    _add_column_if_missing(engine, "dataset_variants", "extra_stats", "TEXT")


def _migration_benchmark_is_legacy(engine: Engine) -> None:
    _add_column_if_missing(engine, "benchmarks", "is_legacy", "INTEGER NOT NULL DEFAULT 0")
    with engine.connect() as conn:
        conn.execute(
            text(
                "UPDATE benchmarks SET is_legacy = 1 "
                "WHERE name IN ('Classic', 'TU Dortmund') AND is_legacy = 0"
            )
        )
        conn.commit()


def _migration_todo_manual_importance(engine: Engine) -> None:
    # Added after 003 was already applied on some DBs without this column.
    _add_column_if_missing(
        engine, "todo_papers", "is_manually_important", "INTEGER NOT NULL DEFAULT 0"
    )


MIGRATIONS: tuple[Migration, ...] = (
    Migration("001_results_additional_columns", _migration_results_additional_columns),
    Migration("002_pending_datasets_columns", _migration_pending_datasets_columns),
    Migration("003_todo_queue_columns", _migration_todo_queue_columns),
    Migration("004_todo_queue_indexes", _migration_todo_queue_indexes),
    Migration("005_results_model_metadata", _migration_results_model_metadata),
    Migration("006_dataset_extra_stats", _migration_dataset_extra_stats),
    Migration("007_benchmark_is_legacy", _migration_benchmark_is_legacy),
    Migration("008_todo_manual_importance", _migration_todo_manual_importance),
)


def init_db(db_path: str | None = None) -> Engine:
    """Create tables and return the engine. Safe to call multiple times."""
    global _engine, _SessionFactory
    cfg.ensure_dirs()
    _engine = _get_engine(db_path)
    Base.metadata.create_all(_engine)
    _apply_migrations(_engine)
    _SessionFactory = sessionmaker(bind=_engine, expire_on_commit=False)
    return _engine


def _apply_migrations(engine: Engine) -> None:
    """Apply tracked schema migrations in order."""
    _ensure_migration_table(engine)
    applied = _get_applied_migrations(engine)
    for migration in MIGRATIONS:
        if migration.name in applied:
            continue
        migration.apply(engine)
        _record_migration(engine, migration.name)


def _ensure_migration_table(engine: Engine) -> None:
    with engine.connect() as conn:
        conn.execute(
            text(
                """
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    name TEXT PRIMARY KEY,
                    applied_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
                )
                """
            )
        )
        conn.commit()


def _get_applied_migrations(engine: Engine) -> set[str]:
    with engine.connect() as conn:
        rows = conn.execute(text("SELECT name FROM schema_migrations ORDER BY name")).fetchall()
    return {row[0] for row in rows}


def _record_migration(engine: Engine, name: str) -> None:
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO schema_migrations(name) VALUES (:name)"), {"name": name})
        conn.commit()


def _add_column_if_missing(engine: Engine, table: str, column: str, col_type: str) -> None:
    _validate_sql_identifier(table, "table")
    _validate_sql_identifier(column, "column")
    # Validate column type: allow common SQLite types + REFERENCES + NOT NULL + DEFAULT
    if not re.match(
        r"^[A-Z]+(?:\s*\(\d+\))?(?:\s+NOT\s+NULL)?(?:\s+DEFAULT\s+[^,]+)?(?:\s+REFERENCES\s+[A-Za-z_][A-Za-z0-9_]*\([A-Za-z_][A-Za-z0-9_]*\)\s+ON\s+DELETE\s+(SET\s+NULL|CASCADE|RESTRICT|NO\s+ACTION))?$",
        col_type,
        re.IGNORECASE,
    ):
        raise ValueError(f"Unsafe column type: {col_type!r}")
    with engine.connect() as conn:
        existing = {
            row[1]
            for row in conn.execute(text(f"PRAGMA table_info({_validate_sql_identifier(table)})"))
        }
        if column not in existing:
            conn.execute(
                text(
                    f"ALTER TABLE {_validate_sql_identifier(table)} "
                    f"ADD COLUMN {_validate_sql_identifier(column)} {col_type}"
                )
            )
            conn.commit()


def _ensure_index(engine: Engine, index_name: str, create_sql: str) -> None:
    _validate_sql_identifier(index_name, "index")
    with engine.connect() as conn:
        existing = {
            row[0]
            for row in conn.execute(
                text("SELECT name FROM sqlite_master WHERE type='index' AND name = :name"),
                {"name": index_name},
            )
        }
        if index_name not in existing:
            conn.execute(text(create_sql))
            conn.commit()


def get_engine() -> Engine:
    if _engine is None:
        init_db()
    return _engine  # type: ignore[return-value]


def get_session_factory() -> sessionmaker:
    if _SessionFactory is None:
        init_db()
    return _SessionFactory  # type: ignore[return-value]


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    """Context manager providing a transactional DB session.

    Example::
        with session_scope() as session:
            session.add(paper)
    """
    factory = get_session_factory()
    session: Session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
