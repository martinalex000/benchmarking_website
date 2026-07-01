"""Tests for problematic LaTeX papers dev export."""

from __future__ import annotations

import json

import yaml

from backend.db import init_db, session_scope
from backend.hugo_dev_exports import _write_problematic_latex_papers_page, create_dev_pages


def _configure_temp_workspace(monkeypatch, tmp_path):
    root = tmp_path / "workspace"
    data_dir = root / "site" / "data"
    content_dev = root / "site" / "content" / "dev"
    data_dir.mkdir(parents=True)
    content_dev.mkdir(parents=True)

    monkeypatch.setattr("backend.config.cfg.project_root", root)
    monkeypatch.setattr("backend.config.cfg.site_dir", root / "site")

    import backend.db as db_module
    from backend import export_to_hugo

    db_module._engine = None
    db_module._SessionFactory = None
    monkeypatch.setattr(export_to_hugo, "_SITE_DIR", root / "site")
    monkeypatch.setattr(export_to_hugo, "_CONTENT", root / "site" / "content")
    monkeypatch.setattr(export_to_hugo, "_DATA_DIR", data_dir)

    payload = {
        "scanned_at": "2026-07-01T12:00:00+00:00",
        "papers": [
            {
                "arxiv_id": "2411.05274",
                "title": "DRAGON",
                "issues": [
                    {
                        "kind": "wraptable",
                        "detail": "Contains 1 wraptable environment(s)",
                        "sample_lines": [],
                    }
                ],
            }
        ],
    }
    (data_dir / "problematic_latex_papers.json").write_text(json.dumps(payload), encoding="utf-8")
    return export_to_hugo, content_dev


def test_problematic_papers_dev_page_renders_scan_json(monkeypatch, tmp_path):
    export_to_hugo, content_dev = _configure_temp_workspace(monkeypatch, tmp_path)
    _write_problematic_latex_papers_page(export_to_hugo, content_dev)

    md_path = content_dev / "problematic-papers.md"
    assert md_path.is_file()
    body = md_path.read_text(encoding="utf-8")
    assert "2411.05274" in body
    assert "wraptable" in body
    assert "latex_table_reextract_server.txt" in body


def test_create_dev_pages_includes_problematic_papers(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()
    with session_scope() as session:
        create_dev_pages(session=session)

    md_path = tmp_path / "workspace" / "site" / "content" / "dev" / "problematic-papers.md"
    assert md_path.is_file()
    front_matter = yaml.safe_load(md_path.read_text(encoding="utf-8").split("---", 2)[1])
    assert front_matter["title"] == "Problematic Papers"
