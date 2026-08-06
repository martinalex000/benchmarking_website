from pathlib import Path

import pytest

from scripts import queue_paper


def test_collects_positional_and_file_ids_in_order(tmp_path: Path):
    path = tmp_path / "papers.txt"
    path.write_text(
        "# Priority papers\n2406.08993v2  # duplicate below\n\n2206.08164\n",
        encoding="utf-8",
    )

    assert queue_paper.collect_arxiv_ids(["https://arxiv.org/abs/2406.08993"], path) == [
        "2406.08993",
        "2206.08164",
    ]


def test_invalid_input_rejects_entire_collection():
    with pytest.raises(ValueError, match="not-an-id"):
        queue_paper.collect_arxiv_ids(["2206.08164", "not-an-id"], None)


def test_default_adds_normal_priority_paper(monkeypatch):
    calls = []

    def fake_add(arxiv_id, **kwargs):
        calls.append((arxiv_id, kwargs))
        return True, f"Added {arxiv_id} to todo queue"

    monkeypatch.setattr(queue_paper, "add_todo_paper", fake_add)

    assert queue_paper.main(["2206.08164"]) == 0
    assert calls == [
        (
            "2206.08164",
            {"added_by": "queue_paper.py", "is_manually_important": False},
        )
    ]


def test_important_flag_marks_paper_important(monkeypatch):
    calls = []

    def fake_add(arxiv_id, **kwargs):
        calls.append((arxiv_id, kwargs))
        return True, f"Added {arxiv_id} to todo queue (manually important)"

    monkeypatch.setattr(queue_paper, "add_todo_paper", fake_add)

    assert queue_paper.main(["2206.08164", "--important"]) == 0
    assert calls[0][1]["is_manually_important"] is True


def test_dry_run_does_not_touch_queue(monkeypatch):
    monkeypatch.setattr(
        queue_paper,
        "add_todo_paper",
        lambda *_args, **_kwargs: pytest.fail("queue should not be changed"),
    )

    assert queue_paper.main(["2206.08164", "--dry-run"]) == 0


def test_export_queue_file_writes_papers_and_important_rows(tmp_path, monkeypatch):
    monkeypatch.setattr(
        queue_paper,
        "_paper_rows",
        lambda: [("2206.08164", "Paper title")],
    )
    monkeypatch.setattr(
        queue_paper,
        "_important_rows",
        lambda: [("2206.08164", "Paper title"), ("2406.08993", "Important paper")],
    )

    output = tmp_path / "priority.txt"
    assert queue_paper.export_queue_file(output) == 3

    content = output.read_text(encoding="utf-8")
    assert "2206.08164  # Paper title" in content
    assert "2406.08993  # Important paper" in content
    assert "queue_paper.py --file" in content
