"""Tests for per-paper storage initialization."""

from __future__ import annotations

import json

from backend.paper_storage import PaperStorage


def test_init_paper_does_not_create_override_template(tmp_path):
    storage = PaperStorage("2401.00001", papers_root=tmp_path)

    storage.init_paper({"title": "Example"})

    assert json.loads(storage.metadata_path.read_text(encoding="utf-8"))["title"] == "Example"
    assert not storage.overrides_path.exists()


def test_init_paper_preserves_existing_override(tmp_path):
    storage = PaperStorage("2401.00001", papers_root=tmp_path)
    storage.ensure_dirs()
    storage.overrides_path.write_text(
        'paper_arxiv_id: "2401.00001"\nresult_overrides: []\n', encoding="utf-8"
    )

    storage.init_paper({"title": "Example"})

    assert storage.overrides_path.read_text(encoding="utf-8") == (
        'paper_arxiv_id: "2401.00001"\nresult_overrides: []\n'
    )
