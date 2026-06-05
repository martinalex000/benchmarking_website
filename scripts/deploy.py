#!/usr/bin/env python3
"""Build and deploy the Hugo site via zstd tar archives over ssh/rsync."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import socket
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import cfg

DEFAULT_DEPLOY_PATH = "/var/www/graphbench"
REMOTE_ARCHIVE_NAME = "deploy"
SSH_OPTS = ["-o", "BatchMode=yes", "-o", "ConnectTimeout=10"]
DEPLOY_FILE_MODE = 0o755
FIGURES_NAME_RE = re.compile(r"^-(\d{12})-figures\.tar\.zst$")


def log_remote(kind: str, detail: str) -> None:
    print(f"remote {kind}: {detail}")


def ssh_run(ssh_dest: str, *remote_cmd: str) -> None:
    log_remote("ssh", f"{ssh_dest} {subprocess.list2cmdline(list(remote_cmd))}")
    subprocess.run(["ssh", *SSH_OPTS, ssh_dest, *remote_cmd], check=True)


def ssh_capture(ssh_dest: str, *remote_cmd: str) -> str:
    log_remote("ssh", f"{ssh_dest} {subprocess.list2cmdline(list(remote_cmd))}")
    result = subprocess.run(
        ["ssh", *SSH_OPTS, ssh_dest, *remote_cmd],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def rsync_ssh_shell() -> str:
    return subprocess.list2cmdline(["ssh", *SSH_OPTS])


def upload_archive(ssh_dest: str, local_path: Path, remote_path: str) -> None:
    target = f"{ssh_dest}:{remote_path}"
    log_remote("rsync", f"{local_path} -> {target}")
    subprocess.run(
        ["rsync", "-ah", "--info=progress2", "-e", rsync_ssh_shell(), str(local_path), target],
        check=True,
    )


def report_transfer_progress(label: str, sent: int, total: int) -> None:
    pct = sent * 100 // total if total else 100
    print(
        f"\r{label}: {pct:3d}% ({format_size(sent)}/{format_size(total)})",
        end="",
        flush=True,
    )


def extract_archive(ssh_dest: str, remote_deploy: str, local_path: Path) -> None:
    size = local_path.stat().st_size
    label = f"Extracting {local_path.name}"
    log_remote(
        "ssh",
        f"{ssh_dest} tar -xf - -C {remote_deploy}  <  zstd -d -c {local_path}",
    )
    zstd = subprocess.Popen(["zstd", "-d", "-c"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ssh = subprocess.Popen(
        ["ssh", *SSH_OPTS, ssh_dest, "tar", "-xf", "-", "-C", remote_deploy],
        stdin=zstd.stdout,
    )
    zstd.stdout.close()
    try:
        with open(local_path, "rb") as src:
            sent = 0
            while chunk := src.read(1024 * 1024):
                zstd.stdin.write(chunk)
                sent += len(chunk)
                report_transfer_progress(label, sent, size)
        zstd.stdin.close()
        if ssh.wait() != 0:
            raise subprocess.CalledProcessError(ssh.returncode, ssh.args)
        if zstd.wait() != 0:
            raise subprocess.CalledProcessError(zstd.returncode, zstd.args)
    finally:
        print()


def remote_home(ssh_dest: str) -> str:
    for remote_cmd in (("pwd",), ("sh", "-c", "cd; pwd")):
        try:
            home = ssh_capture(ssh_dest, *remote_cmd).strip()
            if home:
                return home
        except subprocess.CalledProcessError:
            continue
    sys.exit("ERROR: Could not resolve remote home directory.")


def remote_paths(ssh_dest: str, deploy_path: str) -> tuple[str, str]:
    home = remote_home(ssh_dest)
    archive = f"{home}/{REMOTE_ARCHIVE_NAME}"
    deploy = deploy_path if deploy_path.startswith("/") else f"{home}/{deploy_path}"
    return archive, deploy


def unpack_remotely(
    ssh_dest: str,
    remote_deploy: str,
    remote_archive: str,
    *,
    prepare: bool = False,
    clear_site: bool = False,
    fix_permissions: bool = False,
) -> None:
    if prepare:
        ssh_run(ssh_dest, "mkdir", "-p", remote_archive)
        ssh_run(ssh_dest, "mkdir", "-p", remote_deploy)
        ssh_run(ssh_dest, "test", "-w", remote_deploy)

    if clear_site:
        ssh_run(
            ssh_dest,
            "find",
            remote_deploy,
            "-mindepth",
            "1",
            "-maxdepth",
            "1",
            "-exec",
            "rm",
            "-rf",
            "--",
            "{}",
            "+",
        )

    if fix_permissions:
        ssh_run(ssh_dest, "chmod", "-R", "755", "--", remote_deploy)


def list_remote_figure_archives(ssh_dest: str, remote_archive: str, host_id: str) -> list[str]:
    try:
        output = ssh_capture(ssh_dest, "ls", "-1", remote_archive)
    except subprocess.CalledProcessError:
        return []
    prefix = f"{host_id}-"
    suffix = "-figures.tar.zst"
    return [
        Path(line).name
        for line in output.splitlines()
        if line.strip().startswith(prefix) and line.strip().endswith(suffix)
    ]


def archive_created_at(name: str, host_id: str) -> datetime | None:
    match = FIGURES_NAME_RE.search(name.removeprefix(host_id))
    if not match:
        return None
    return datetime.strptime(match.group(1), "%Y%m%d%H%M")


def remote_archive_size(ssh_dest: str, remote_archive: str, name: str) -> int | None:
    try:
        output = ssh_capture(ssh_dest, "stat", "-c", "%s", f"{remote_archive}/{name}")
    except subprocess.CalledProcessError:
        return None
    return int(output.strip())


def format_size(size: int) -> str:
    if size >= 1024 * 1024:
        return f"{size / (1024 * 1024):.1f}M"
    if size >= 1024:
        return f"{size / 1024:.1f}K"
    return f"{size}B"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def remote_file_sha256(ssh_dest: str, remote_path: str) -> str | None:
    try:
        output = ssh_capture(ssh_dest, "sha256sum", remote_path)
    except subprocess.CalledProcessError:
        return None
    return output.split(maxsplit=1)[0]


def latest_figure_archive(names: list[str], host_id: str) -> str | None:
    best_name = ""
    best_stamp = ""
    for name in names:
        match = FIGURES_NAME_RE.search(name.removeprefix(f"{host_id}"))
        if match and match.group(1) > best_stamp:
            best_stamp = match.group(1)
            best_name = name
    return best_name or None


def maybe_prune_old_archives(
    ssh_dest: str,
    remote_archive: str,
    host_id: str,
    keep_name: str,
) -> None:
    archives = list_remote_figure_archives(ssh_dest, remote_archive, host_id)
    old = [name for name in archives if name != keep_name]
    if len(archives) <= 1 or not old:
        return

    print(f"\nFigure archives from {host_id} on server:")
    for name in archives:
        label = "keep" if name == keep_name else "old"
        created = archive_created_at(name, host_id)
        created_text = created.strftime("%Y-%m-%d %H:%M") if created else "unknown date"
        size = remote_archive_size(ssh_dest, remote_archive, name)
        size_text = format_size(size) if size is not None else "unknown size"
        print(f"  {label:4}  {name}  {size_text:>8}  {created_text}")

    if not sys.stdin.isatty():
        print("Keeping older figure archives (non-interactive).")
        return

    answer = input("Delete older figure archives? [Y/n] ").strip().lower()
    if answer in {"n", "no"}:
        print("Keeping older figure archives.")
        return

    for name in old:
        print(f"Deleting {name}...")
        ssh_run(ssh_dest, "rm", "-f", "--", f"{remote_archive}/{name}")


def require_cmd(name: str) -> str:
    from shutil import which

    path = which(name)
    if not path:
        sys.exit(f"ERROR: Required command '{name}' not found in PATH.")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and deploy the Hugo site.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--full", action="store_true", help="Upload figures and increment archives.")
    mode.add_argument(
        "--incremental",
        action="store_true",
        help="Upload increment only (default).",
    )
    parser.add_argument(
        "--no-delete",
        action="store_true",
        help="Do not clear the remote site tree before extracting (full mode).",
    )
    parser.add_argument(
        "--skip-export",
        action="store_true",
        help="Skip database export before Hugo build.",
    )
    args = parser.parse_args()

    full = args.full

    deploy_host = cfg.deploy_host
    deploy_path = (cfg.deploy_path or DEFAULT_DEPLOY_PATH).rstrip("/")
    if not deploy_host:
        sys.exit("ERROR: DEPLOY_HOST is empty. Set it in .env.")
    if not deploy_path:
        sys.exit("ERROR: DEPLOY_PATH is empty. Set it in .env.")

    ssh_dest = f"{cfg.deploy_user}@{deploy_host}" if cfg.deploy_user else deploy_host
    hugo_base_url = os.environ.get("HUGO_BASE_URL", "")
    project_dir = cfg.base_dir
    hugo_bin = project_dir / "bin" / "hugo"
    if not hugo_bin.is_file() or not os.access(hugo_bin, os.X_OK):
        hugo_bin = Path(require_cmd("hugo"))

    for cmd in ("ssh", "rsync", "tar", "zstd"):
        require_cmd(cmd)
    tar_help = subprocess.run(["tar", "--help"], capture_output=True, text=True, check=False)
    if "--zstd" not in tar_help.stdout + tar_help.stderr:
        sys.exit("ERROR: tar on this system does not support --zstd.")

    host_id = socket.gethostname().split(".")[0].replace(" ", "_").replace("/", "_")
    stamp = datetime.now().strftime("%Y%m%d%H%M")
    prefix = f"{host_id}-{stamp}"
    figures_name = f"{prefix}-figures.tar.zst"
    increment_name = f"{prefix}-increment.tar.zst"

    print(f"Checking SSH connectivity to {ssh_dest}...")
    try:
        ssh_run(ssh_dest, "true")
    except subprocess.CalledProcessError:
        print(f"Hint: Verify your ssh config/keys with: ssh {ssh_dest}", file=sys.stderr)
        sys.exit("ERROR: SSH connectivity check failed.")

    remote_archive = ""
    remote_deploy = ""
    try:
        remote_archive, remote_deploy = remote_paths(ssh_dest, deploy_path)
        print(f"Remote archive dir: {remote_archive}")
        print(f"Remote deploy dir: {remote_deploy}")
        unpack_remotely(ssh_dest, remote_deploy, remote_archive, prepare=True)
    except subprocess.CalledProcessError:
        sys.exit(
            f"ERROR: Remote deployment path is missing or not writable: {deploy_path} "
            f"(resolved deploy dir: {remote_deploy or '?'})"
        )

    baseline: str | None = None
    if not full:
        baseline = latest_figure_archive(
            list_remote_figure_archives(ssh_dest, remote_archive, host_id),
            host_id,
        )
        if not baseline:
            print(
                "ERROR: Incremental deploy needs a figures archive from this machine on the server.",
                file=sys.stderr,
            )
            print(f"ERROR: None found for host {host_id} under {remote_archive}/.", file=sys.stderr)
            print(f"Hint: Run a full deploy first: {Path(__file__).name} --full", file=sys.stderr)
            sys.exit(1)
        print(f"Using baseline figure archive: {baseline}")

    with (
        tempfile.TemporaryDirectory(prefix=".deploy-build-", dir=project_dir) as build_dir,
        tempfile.TemporaryDirectory(prefix=".deploy-staging-", dir=project_dir) as staging_dir,
    ):
        build = Path(build_dir)
        staging = Path(staging_dir)
        figures_archive = staging / figures_name
        increment_archive = staging / increment_name

        if not args.skip_export:
            print("Exporting Hugo content from database (includes site/content/dev)...")
            subprocess.run(
                [sys.executable, "-m", "backend.export_to_hugo"], check=True, cwd=project_dir
            )

        print(f"Building Hugo site locally to {build_dir}...")
        hugo_cmd = [str(hugo_bin), "--minify", "-d", build_dir]
        if hugo_base_url:
            hugo_cmd.extend(["--baseURL", hugo_base_url])
        subprocess.run(hugo_cmd, check=True, cwd=project_dir / "site")

        files = list(build.rglob("*"))
        if not any(p.is_file() for p in files):
            sys.exit(f"ERROR: Hugo build produced no files in {build_dir}.")

        print("Normalizing build tree permissions to 755...")
        for path in files:
            path.chmod(DEPLOY_FILE_MODE)

        reuse_figures_archive = False
        if full:
            figures_dir = build / "figures"
            if not figures_dir.is_dir() or not any(p.is_file() for p in figures_dir.rglob("*")):
                sys.exit(
                    f"ERROR: No figures found in {figures_dir}. Run export before a full deploy."
                )
            print(f"Creating figures archive {figures_name}...")
            subprocess.run(
                ["tar", "-C", build_dir, "--zstd", "-cf", figures_archive, "figures"], check=True
            )
            print(figures_archive)

            latest_figures = latest_figure_archive(
                list_remote_figure_archives(ssh_dest, remote_archive, host_id),
                host_id,
            )
            if latest_figures:
                remote_figures_path = f"{remote_archive}/{latest_figures}"
                remote_hash = remote_file_sha256(ssh_dest, remote_figures_path)
                local_hash = file_sha256(figures_archive)
                if remote_hash and remote_hash == local_hash:
                    print(f"Figures unchanged; reusing remote archive {latest_figures}")
                    figures_name = latest_figures
                    reuse_figures_archive = True

        print(f"Creating increment archive {increment_name}...")
        subprocess.run(
            ["tar", "-C", build_dir, "--zstd", "--exclude=figures", "-cf", increment_archive, "."],
            check=True,
        )
        print(increment_archive)

        mode_label = "full" if full else "incremental"
        print(f"Running {mode_label} deploy from {host_id} ({prefix})...")

        if full and not args.no_delete:
            unpack_remotely(ssh_dest, remote_deploy, remote_archive, clear_site=True)

        to_upload: list[tuple[Path, str]] = [(increment_archive, increment_name)]
        to_extract: list[tuple[Path, str]] = [(increment_archive, increment_name)]
        if full:
            if reuse_figures_archive:
                if not args.no_delete:
                    to_extract.insert(0, (figures_archive, figures_name))
            else:
                to_upload.insert(0, (figures_archive, figures_name))
                to_extract.insert(0, (figures_archive, figures_name))

        for local_path, remote_name in to_upload:
            upload_archive(ssh_dest, local_path, f"{remote_archive}/{remote_name}")

        for local_path, _remote_name in to_extract:
            extract_archive(ssh_dest, remote_deploy, local_path)

        keep_figures = figures_name if full else baseline
        maybe_prune_old_archives(ssh_dest, remote_archive, host_id, keep_figures)

        try:
            unpack_remotely(ssh_dest, remote_deploy, remote_archive, fix_permissions=True)
        except subprocess.CalledProcessError:
            print(f"Hint: Manual fix: chmod -R 755 {remote_deploy}", file=sys.stderr)
            sys.exit("ERROR: Failed to set 755 permissions on deployed files.")

    print("Deploy complete.")


if __name__ == "__main__":
    main()
