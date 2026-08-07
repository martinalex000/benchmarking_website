"""Tests for the consolidated maintenance CLI."""

from __future__ import annotations

import sqlite3

from scripts import maintenance


def test_todo_dispatches_force_and_seed(monkeypatch):
    calls = []
    monkeypatch.setattr(maintenance, "backfill_todo", lambda **kwargs: calls.append(kwargs))

    assert maintenance.main(["todo", "--seed", "2206.08164", "--force"]) == 0

    assert calls == [
        {
            "db_path": None,
            "limit": 5000,
            "seed": ["2206.08164"],
            "top": 15,
            "force": True,
        }
    ]


def test_all_runs_conservative_venue_repair(monkeypatch):
    events = []
    monkeypatch.setattr(
        maintenance,
        "print_info",
        lambda **kwargs: events.append(("info", kwargs)),
    )
    monkeypatch.setattr(
        maintenance,
        "backfill_authors",
        lambda **kwargs: events.append(("authors", kwargs)),
    )
    monkeypatch.setattr(
        maintenance,
        "backfill_publication",
        lambda **kwargs: events.append(("publication", kwargs)),
    )
    monkeypatch.setattr(
        maintenance,
        "repair_venues",
        lambda **kwargs: events.append(("repair-venues", kwargs)),
    )
    monkeypatch.setattr(
        maintenance,
        "backfill_todo",
        lambda **kwargs: events.append(("todo", kwargs)),
    )

    assert (
        maintenance.main(
            [
                "all",
                "--dry-run",
                "--include-all",
                "--limit",
                "7",
                "--seed",
                "2206.08164",
                "--force",
            ]
        )
        == 0
    )

    assert [name for name, _kwargs in events] == [
        "info",
        "authors",
        "publication",
        "repair-venues",
        "todo",
    ]
    assert events[3][1]["include_known_wrong"] is False
    assert events[4][1]["force"] is True


def test_crawl_retries_locked_database_and_preserves_force(monkeypatch):
    calls = []

    def fake_crawl(_client, _connection, seed, limit, force):
        calls.append((seed, limit, force))
        if len(calls) < 3:
            raise sqlite3.OperationalError("database is locked")
        return {"citations": 1}

    monkeypatch.setattr(maintenance, "crawl_seed", fake_crawl)
    monkeypatch.setattr(maintenance, "_is_sqlite_lock_error", lambda _exc: True)
    monkeypatch.setattr(maintenance.time, "sleep", lambda _seconds: None)

    result = maintenance._crawl_seed_with_retries(None, None, "2206.08164", 25, True)

    assert result == {"citations": 1}
    assert calls == [
        ("2206.08164", 25, True),
        ("2206.08164", 25, True),
        ("2206.08164", 25, True),
    ]
