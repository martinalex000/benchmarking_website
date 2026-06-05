"""Tests for development Hugo export helpers."""

from __future__ import annotations

from pathlib import Path

import yaml

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.hugo_dev_exports import create_conferences_page, create_dev_pages


def _configure_temp_workspace(monkeypatch, tmp_path: Path) -> None:
    root = tmp_path / "workspace"
    data_dir = root / "data"
    site_dir = root / "site"
    config_dir = root / "config"

    for directory in (data_dir, site_dir, config_dir):
        directory.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(cfg, "project_root", root)
    monkeypatch.setattr(cfg, "base_dir", root)
    monkeypatch.setattr(cfg, "data_dir", data_dir)
    monkeypatch.setattr(cfg, "papers_dir", root / "papers")
    monkeypatch.setattr(cfg, "logs_dir", root / "logs")
    monkeypatch.setattr(cfg, "site_dir", site_dir)
    monkeypatch.setattr(cfg, "config_dir", config_dir)
    monkeypatch.setattr(cfg, "db_path", data_dir / "benchmarks.db")

    import backend.db as db_module
    from backend import export_to_hugo

    db_module._engine = None
    db_module._SessionFactory = None

    monkeypatch.setattr(export_to_hugo, "_SITE_DIR", site_dir)
    monkeypatch.setattr(export_to_hugo, "_CONTENT", site_dir / "content")
    monkeypatch.setattr(export_to_hugo, "_DATA_DIR", site_dir / "data")
    export_to_hugo.clear_export_caches()


def test_create_conferences_page_exports_section_index(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        create_conferences_page(session=session)

    conferences_md = tmp_path / "workspace" / "site" / "content" / "conferences" / "_index.md"
    assert conferences_md.is_file()

    front_matter, _body = conferences_md.read_text(encoding="utf-8").split("---", 2)[1:]
    metadata = yaml.safe_load(front_matter)

    assert metadata["title"] == "Conferences"


def test_create_dev_pages_does_not_export_conferences_under_dev(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        create_dev_pages(session=session)

    dev_conferences_md = tmp_path / "workspace" / "site" / "content" / "dev" / "conferences.md"
    assert not dev_conferences_md.is_file()


def test_create_dev_pages_exports_baseline_improvements(monkeypatch, tmp_path):
    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        create_dev_pages(session=session)

    improvements_md = (
        tmp_path / "workspace" / "site" / "content" / "dev" / "baseline-improvements.md"
    )
    assert improvements_md.is_file()

    front_matter, body = improvements_md.read_text(encoding="utf-8").split("---", 2)[1:]
    metadata = yaml.safe_load(front_matter)

    assert metadata["title"] == "Baseline Improvements"
    assert "baseline and proposed" in metadata["description"]
    assert "## At-Publication Improvements" in body
