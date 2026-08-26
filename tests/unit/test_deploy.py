"""Tests for deployment target selection."""

from __future__ import annotations

import sys
from pathlib import Path

from scripts import deploy


def test_ssh_options_are_supported_by_older_clients():
    assert "WarnWeakCrypto=no" not in deploy.SSH_OPTS
    assert "StrictHostKeyChecking=no" in deploy.SSH_OPTS
    assert "UserKnownHostsFile=/dev/null" in deploy.SSH_OPTS


def test_rclone_sync_uses_size_only_for_images_and_ignores_times_elsewhere(tmp_path: Path):
    image_command = deploy._rclone_sync_command(
        tmp_path / "rclone.conf",
        tmp_path / "site",
        "deploy:webdir",
        images=True,
    )
    other_command = deploy._rclone_sync_command(
        tmp_path / "rclone.conf",
        tmp_path / "site",
        "deploy:webdir",
        images=False,
    )

    assert "--size-only" in image_command
    assert "--ignore-times" not in image_command
    assert "--ignore-times" in other_command
    assert "--size-only" not in other_command
    assert image_command[-1] == other_command[-1] == "deploy:webdir"


def test_rclone_config_disables_known_hosts_validation(monkeypatch, tmp_path: Path):
    monkeypatch.setattr(deploy.Path, "home", lambda: tmp_path)
    ssh_dir = tmp_path / ".ssh"
    ssh_dir.mkdir()
    (ssh_dir / "config").write_text("Host webspace\n    HostName example.org\n")
    known_hosts = ssh_dir / "known_hosts"
    known_hosts.write_text("example.org ssh-ed25519 AAAA\n")
    monkeypatch.setattr(
        deploy,
        "resolve_sftp_endpoint",
        lambda _dest: ("example.org", "glb", 22),
    )

    config_path = deploy.rclone_config("webspace")
    try:
        config = config_path.read_text()
    finally:
        config_path.unlink()

    assert "shell_type = none" in config
    assert "known_hosts_file" not in config


def test_sftp_connectivity_uses_batch_subsystem(monkeypatch, tmp_path: Path):
    ssh_dir = tmp_path / ".ssh"
    ssh_dir.mkdir()
    (ssh_dir / "config").write_text("Host webspace\n    HostName example.org\n")
    monkeypatch.setattr(deploy.Path, "home", lambda: tmp_path)
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))

    monkeypatch.setattr(deploy.subprocess, "run", fake_run)
    deploy.check_sftp_connectivity("webspace")

    assert calls[0][0][:3] == ["sftp", "-F", str(ssh_dir / "config")]
    assert calls[0][0][-3:] == ["-b", "-", "webspace"]
    assert calls[0][1] == {"input": "", "text": True, "check": True}


def test_normalize_sftp_permissions_uses_deployed_paths(monkeypatch, tmp_path: Path):
    (tmp_path / "js").mkdir()
    (tmp_path / "js" / "dataset-page.js").write_text("console.log('ok');")
    monkeypatch.setattr(deploy.Path, "home", lambda: tmp_path)
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))

    monkeypatch.setattr(deploy.subprocess, "run", fake_run)
    deploy.normalize_sftp_permissions("webspace", "webdir", tmp_path)

    assert calls[0][0][:2] == ["sftp", "-q"]
    assert "chmod 755 webdir/js/*" in calls[0][1]["input"]
    assert calls[0][1]["check"] is True
    assert calls[0][1]["stdout"] is deploy.subprocess.DEVNULL


def test_both_deploys_server_then_github_pages(monkeypatch, tmp_path: Path, capsys):
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

    monkeypatch.setattr(deploy, "require_build_tools", lambda **_kwargs: None)
    monkeypatch.setattr(deploy, "require_deploy_tools", lambda: None)
    monkeypatch.setattr(deploy, "check_sftp_connectivity", lambda *_args: None)
    monkeypatch.setattr(deploy, "ssh_run", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(deploy, "build_archives", lambda *_args, **_kwargs: archive_paths)
    monkeypatch.setattr(deploy, "persist_deploy_archives", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(
        deploy,
        "sync_deploy_tree",
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
    output_lines = capsys.readouterr().out.splitlines()
    assert output_lines[0].startswith("Deployment controller host: ")
    assert output_lines[1].startswith("Archive build host: ")
    assert (
        output_lines[2]
        == "Deployment target: deployer@server.example.com:/var/www/graphbench and GitHub Pages"
    )


def test_local_allows_skip_export(monkeypatch, tmp_path: Path):
    monkeypatch.setattr(deploy.cfg, "base_dir", tmp_path)
    monkeypatch.setattr(deploy, "require_cmd", lambda _cmd: None)
    calls: list[tuple[Path, bool]] = []
    monkeypatch.setattr(
        deploy,
        "run_local_server",
        lambda project_dir, *, skip_export: calls.append((project_dir, skip_export)),
    )
    monkeypatch.setattr(sys, "argv", ["deploy.py", "--local", "--skip-export"])

    deploy.main()

    assert calls == [(tmp_path, True)]
