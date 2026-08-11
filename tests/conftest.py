"""Shared test isolation fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def reset_database_engine():
    """Prevent temporary SQLite engines from leaking into later tests."""
    yield

    import backend.db as db_module

    db_module._engine = None
    db_module._SessionFactory = None
