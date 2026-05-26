"""Database connection and session management."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from backend.config import cfg
from backend.models import Base


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


def init_db(db_path: str | None = None) -> Engine:
    """Create tables and return the engine. Safe to call multiple times."""
    global _engine, _SessionFactory
    cfg.ensure_dirs()
    _engine = _get_engine(db_path)
    Base.metadata.create_all(_engine)
    _migrate_db(_engine)
    _SessionFactory = sessionmaker(bind=_engine, expire_on_commit=False)
    return _engine


def _migrate_db(engine: Engine) -> None:
    """Apply lightweight schema migrations for columns added after initial creation."""
    _add_column_if_missing(engine, "results", "uses_external_data", "INTEGER")
    # todo_papers counters
    _add_column_if_missing(engine, "todo_papers", "cited_by_count", "INTEGER")
    _add_column_if_missing(engine, "todo_papers", "cites_existing_count", "INTEGER")
    # pending_datasets columns (table is created via metadata if missing)
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


def _add_column_if_missing(engine: Engine, table: str, column: str, col_type: str) -> None:
    with engine.connect() as conn:
        existing = {
            row[1]
            for row in conn.execute(__import__("sqlalchemy").text(f"PRAGMA table_info({table})"))
        }
        if column not in existing:
            conn.execute(
                __import__("sqlalchemy").text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}")
            )
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
