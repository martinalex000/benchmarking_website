from backend import repetition_chunks
from backend.repetition_chunks import connect


def test_apply_requests_confirmation_when_some_papers_are_not_ready(tmp_path, monkeypatch):
    database = tmp_path / "queue.sqlite3"
    root = tmp_path / "artifacts"
    root.mkdir()
    (root / "database_rows_snapshot.json").write_text("{}")
    monkeypatch.setattr(repetition_chunks, "queue_database_path", lambda _: database)

    with connect(database) as db:
        db.execute("CREATE TABLE papers (paper_id TEXT, status TEXT, analysis_path TEXT)")
        db.executemany(
            "INSERT INTO papers VALUES (?, ?, NULL)",
            [("ready-paper", "ready"), ("queued-paper", "queued")],
        )

    result = repetition_chunks.apply_ready(root)

    assert result == {
        "confirmation_required": True,
        "ready_papers": 1,
        "incomplete_papers": {"queued": 1},
    }
    with connect(database) as db:
        assert (
            db.execute("SELECT status FROM papers WHERE paper_id='ready-paper'").fetchone()[0]
            == "ready"
        )
