"""Shared test isolation fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def reset_database_engine():
    """Prevent temporary SQLite engines from leaking into later tests."""
    yield

    import backend.db as db_module
    import backend.results_parser as results_parser

    db_module._engine = None
    db_module._SessionFactory = None
    results_parser._DATASET_ALIAS_MAP = None
    results_parser._AMBIGUOUS_DATASET_NAMES = None
    results_parser._PROTOCOL_EXCLUSIONS = None
    results_parser._PROTOCOL_CONTRACTS = None
