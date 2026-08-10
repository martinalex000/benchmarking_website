"""Tests for deployment target selection."""

from __future__ import annotations

import sys
from pathlib import Path

from scripts import deploy


def test_both_deploys_server_then_github_pages(monkeypatch, tmp_path: Path):
    monkeypatch.setattr(deploy.cfg, "base_dir", tmp_path)
    monkeypatch.setattr(deploy.cfg, "deploy_host", "server.example.com")
    monkeypatch.setattr(deploy.cfg, "deploy_user", "deployer")
    monkeypatch.setattr(deploy.cfg, "deploy_path", "/var/www/graphbench")
    monkeypatch.setattr(deploy.cfg, "build_host", "")

    calls: list[str] = []
    archive_paths = (
        tmp_path / "figures.tar.zst",
        tmp_path / "increment.tar.zst",
        "figures.tar.zst",
        "increment.tar.zst",
        "archive-prefix",
    )

    monkeypatch.setattr(deploy, "require_build_tools", lambda: None)
    monkeypatch.setattr(deploy, "ssh_run", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        deploy,
        "remote_paths",
        lambda *_args, **_kwargs: ("/home/deployer/deploy", "/var/www/graphbench"),
    )
    monkeypatch.setattr(deploy, "unpack_remotely", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(deploy, "build_archives", lambda *_args, **_kwargs: archive_paths)
    monkeypatch.setattr(deploy, "persist_deploy_archives", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        deploy,
        "deploy_archives",
        lambda *_args, **_kwargs: calls.append("server"),
    )
    monkeypatch.setattr(
        deploy,
        "deploy_github_pages",
        lambda *_args, **_kwargs: calls.append("github-pages"),
    )
    monkeypatch.setattr(sys, "argv", ["deploy.py", "--both", "--skip-export"])

    deploy.main()

    assert calls == ["server", "github-pages"]
