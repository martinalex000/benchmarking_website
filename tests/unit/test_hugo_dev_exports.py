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
    monkeypatch.setattr(export_to_hugo, "_STATIC", site_dir / "static")
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


def test_create_dev_pages_exports_sota_claims(monkeypatch, tmp_path):
    import json

    from backend.models import Paper, PaperSotaClaim

    _configure_temp_workspace(monkeypatch, tmp_path)
    init_db()

    with session_scope() as session:
        paper = Paper(
            arxiv_id="2301.00001",
            title="Claim Paper",
            published_date="2023-01-15",
            extraction_status="extracted",
        )
        session.add(paper)
        session.flush()
        session.add(
            PaperSotaClaim(
                paper_id=paper.id,
                raw_sentence="We achieve state-of-the-art performance.",
                claim_summary="Overall SOTA",
                datasets=json.dumps(["Cora"]),
                scope="restricted",
                restrictions=json.dumps(
                    [{"type": "model_class", "description": "message-passing only"}]
                ),
            )
        )
        create_dev_pages(session=session)

    sota_md = tmp_path / "workspace" / "site" / "content" / "dev" / "sota-claims.md"
    assert sota_md.is_file()
    body = sota_md.read_text(encoding="utf-8")
    assert "SOTA Claims" in body
    assert "All extracted claims" in body
    assert "Unrestricted claim audit" in body
    assert "state-of-the-art" in body


def test_long_dev_tables_are_exported_as_lazy_json(monkeypatch, tmp_path):
    import json

    from backend import export_to_hugo

    _configure_temp_workspace(monkeypatch, tmp_path)
    dev_path = tmp_path / "workspace" / "site" / "content" / "dev" / "long-table.md"
    lines = ["## Details", "", "| Name | Value |", "|---|---|"]
    lines.extend(f"| item {index} | {index} |" for index in range(50))

    export_to_hugo._write_md(dev_path, {"title": "Long table", "type": "dev"}, "\n".join(lines))

    body = dev_path.read_text(encoding="utf-8")
    payload_path = (
        tmp_path / "workspace" / "site" / "static" / "data" / "development" / "long-table.json"
    )
    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    assert "dev_table_json" in body
    assert "| item 0 |" not in body
    assert payload["schema_version"] == 1
    assert len(payload["tables"][0]["rows"]) == 50
