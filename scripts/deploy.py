#!/usr/bin/env python3
"""Build and deploy the Hugo site via zstd tar archives over ssh/rsync."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shlex
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
INCREMENT_SUFFIX = "-increment.tar.zst"
FIGURES_SUFFIX = "-figures.tar.zst"


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


def download_archive(ssh_dest: str, remote_path: str, local_path: Path) -> None:
    source = f"{ssh_dest}:{remote_path}"
    log_remote("rsync", f"{source} -> {local_path}")
    subprocess.run(
        ["rsync", "-ah", "--info=progress2", "-e", rsync_ssh_shell(), source, str(local_path)],
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
    suffix = FIGURES_SUFFIX
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


def normalize_host_id(hostname: str) -> str:
    return hostname.split(".")[0].replace(" ", "_").replace("/", "_")


def local_host_id() -> str:
    return normalize_host_id(socket.gethostname())


def remote_host_id(ssh_dest: str) -> str:
    return normalize_host_id(ssh_capture(ssh_dest, "hostname").strip())


def resolve_hugo_bin(project_dir: Path) -> Path:
    hugo_bin = project_dir / "bin" / "hugo"
    if not hugo_bin.is_file() or not os.access(hugo_bin, os.X_OK):
        hugo_bin = Path(require_cmd("hugo"))
    return hugo_bin


def archive_names(host_id: str, stamp: str | None = None) -> tuple[str, str, str]:
    stamp = stamp or datetime.now().strftime("%Y%m%d%H%M")
    prefix = f"{host_id}-{stamp}"
    return prefix, f"{prefix}{FIGURES_SUFFIX}", f"{prefix}{INCREMENT_SUFFIX}"


def host_id_from_archive_name(name: str) -> str:
    for suffix in (FIGURES_SUFFIX, INCREMENT_SUFFIX):
        if name.endswith(suffix):
            stamp_start = len(name) - len(suffix) - 12
            if stamp_start > 0:
                return name[:stamp_start]
    sys.exit(f"ERROR: Could not parse host id from archive name: {name}")


def list_staging_archives(names: list[str]) -> tuple[str | None, str]:
    figures_name = None
    increment_name = ""
    for name in names:
        if name.endswith(INCREMENT_SUFFIX):
            increment_name = name
        elif name.endswith(FIGURES_SUFFIX):
            figures_name = name
    if not increment_name:
        sys.exit("ERROR: Build did not produce an increment archive.")
    return figures_name, increment_name


def require_build_tools(*, check_hugo: bool = True) -> None:
    for cmd in ("ssh", "rsync", "tar", "zstd"):
        require_cmd(cmd)
    tar_help = subprocess.run(["tar", "--help"], capture_output=True, text=True, check=False)
    if "--zstd" not in tar_help.stdout + tar_help.stderr:
        sys.exit("ERROR: tar on this system does not support --zstd.")
    if check_hugo:
        require_cmd("hugo")


def ssh_dest_for(host: str, user: str) -> str:
    return f"{user}@{host}" if user else host


def build_archives(
    project_dir: Path,
    staging_dir: Path,
    *,
    full: bool,
    skip_export: bool,
    hugo_base_url: str,
    host_id: str,
) -> tuple[Path | None, Path, str | None, str, str]:
    """Export, build Hugo, and create deploy archives in staging_dir."""
    prefix, figures_name, increment_name = archive_names(host_id)
    figures_archive = staging_dir / figures_name
    increment_archive = staging_dir / increment_name
    hugo_bin = resolve_hugo_bin(project_dir)

    with tempfile.TemporaryDirectory(prefix=".deploy-build-", dir=project_dir) as build_dir:
        build = Path(build_dir)

        if not skip_export:
            print("Exporting Hugo content from database (includes site/content/dev)...")
            subprocess.run(
                [sys.executable, "-m", "backend.export_to_hugo"], check=True, cwd=project_dir
            )

        print(f"Building Hugo site to {build_dir}...")
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

        built_figures: Path | None = None
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
            built_figures = figures_archive

        print(f"Creating increment archive {increment_name}...")
        subprocess.run(
            ["tar", "-C", build_dir, "--zstd", "--exclude=figures", "-cf", increment_archive, "."],
            check=True,
        )
        print(increment_archive)

    return built_figures, increment_archive, figures_name if full else None, increment_name, prefix


def run_remote_build(
    build_ssh_dest: str,
    project_root: str,
    remote_staging: str,
    *,
    full: bool,
    skip_export: bool,
    hugo_base_url: str,
) -> None:
    deploy_script = f"{project_root}/scripts/deploy.py"
    cmd = [
        f"cd {shlex.quote(project_root)}",
        "&&",
        "uv",
        "run",
        "python",
        shlex.quote(deploy_script),
        "--build-only",
        "--staging-dir",
        shlex.quote(remote_staging),
    ]
    if full:
        cmd.append("--full")
    if skip_export:
        cmd.append("--skip-export")

    remote_env = ""
    if hugo_base_url:
        remote_env = f"HUGO_BASE_URL={shlex.quote(hugo_base_url)} "

    ssh_run(build_ssh_dest, "sh", "-c", remote_env + " ".join(cmd))


def fetch_remote_archives(
    build_ssh_dest: str,
    remote_staging: str,
    local_staging: Path,
) -> tuple[Path | None, Path, str | None, str, str]:
    try:
        output = ssh_capture(build_ssh_dest, "ls", "-1", remote_staging)
    except subprocess.CalledProcessError as exc:
        sys.exit(f"ERROR: Could not list remote build staging dir {remote_staging}: {exc}")

    figures_name, increment_name = list_staging_archives(
        [line.strip() for line in output.splitlines() if line.strip()]
    )
    prefix = increment_name.removesuffix(INCREMENT_SUFFIX)

    figures_archive: Path | None = None
    if figures_name:
        figures_archive = local_staging / figures_name
        print(f"Downloading {figures_name} from build host...")
        download_archive(build_ssh_dest, f"{remote_staging}/{figures_name}", figures_archive)

    increment_archive = local_staging / increment_name
    print(f"Downloading {increment_name} from build host...")
    download_archive(build_ssh_dest, f"{remote_staging}/{increment_name}", increment_archive)

    return figures_archive, increment_archive, figures_name, increment_name, prefix


def deploy_archives(
    ssh_dest: str,
    remote_archive: str,
    remote_deploy: str,
    *,
    full: bool,
    no_delete: bool,
    host_id: str,
    figures_name: str | None,
    increment_name: str,
    prefix: str,
    figures_archive: Path | None,
    increment_archive: Path,
) -> None:
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

    reuse_figures_archive = False
    if full and figures_archive and figures_name:
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

    mode_label = "full" if full else "incremental"
    print(f"Running {mode_label} deploy from {host_id} ({prefix})...")

    if full and not no_delete:
        unpack_remotely(ssh_dest, remote_deploy, remote_archive, clear_site=True)

    to_upload: list[tuple[Path, str]] = [(increment_archive, increment_name)]
    to_extract: list[tuple[Path, str]] = [(increment_archive, increment_name)]
    if full and figures_name:
        if reuse_figures_archive:
            if not no_delete and figures_archive:
                to_extract.insert(0, (figures_archive, figures_name))
        elif figures_archive:
            to_upload.insert(0, (figures_archive, figures_name))
            to_extract.insert(0, (figures_archive, figures_name))

    for local_path, remote_name in to_upload:
        upload_archive(ssh_dest, local_path, f"{remote_archive}/{remote_name}")

    for local_path, _remote_name in to_extract:
        extract_archive(ssh_dest, remote_deploy, local_path)

    keep_figures = figures_name if full else baseline
    if keep_figures:
        maybe_prune_old_archives(ssh_dest, remote_archive, host_id, keep_figures)

    try:
        unpack_remotely(ssh_dest, remote_deploy, remote_archive, fix_permissions=True)
    except subprocess.CalledProcessError:
        print(f"Hint: Manual fix: chmod -R 755 {remote_deploy}", file=sys.stderr)
        sys.exit("ERROR: Failed to set 755 permissions on deployed files.")


def validate_build_host_settings() -> tuple[str, str]:
    build_host = cfg.build_host.strip()
    build_project_root = cfg.build_project_root.strip()
    if not build_host:
        return "", ""
    if not build_project_root:
        sys.exit("ERROR: BUILD_PROJECT_ROOT is empty. Set it when BUILD_HOST is configured.")
    if not build_project_root.startswith("/"):
        sys.exit("ERROR: BUILD_PROJECT_ROOT must be an absolute path on the build host.")
    return build_host, build_project_root


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
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="Build archives only; do not deploy (used on remote build hosts).",
    )
    parser.add_argument(
        "--staging-dir",
        type=Path,
        help="Directory for deploy archives (required with --build-only).",
    )
    args = parser.parse_args()

    full = args.full
    hugo_base_url = os.environ.get("HUGO_BASE_URL", "")

    if args.build_only:
        if not args.staging_dir:
            sys.exit("ERROR: --staging-dir is required with --build-only.")
        require_build_tools()
        project_dir = cfg.base_dir
        args.staging_dir.mkdir(parents=True, exist_ok=True)
        host_id = local_host_id()
        build_archives(
            project_dir,
            args.staging_dir,
            full=full,
            skip_export=args.skip_export,
            hugo_base_url=hugo_base_url,
            host_id=host_id,
        )
        return

    deploy_host = cfg.deploy_host
    deploy_path = (cfg.deploy_path or DEFAULT_DEPLOY_PATH).rstrip("/")
    if not deploy_host:
        sys.exit("ERROR: DEPLOY_HOST is empty. Set it in .env.")
    if not deploy_path:
        sys.exit("ERROR: DEPLOY_PATH is empty. Set it in .env.")

    build_host, build_project_root = validate_build_host_settings()
    require_build_tools(check_hugo=not bool(build_host))

    ssh_dest = ssh_dest_for(deploy_host, cfg.deploy_user)

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

    with tempfile.TemporaryDirectory(prefix=".deploy-staging-", dir=cfg.base_dir) as staging_dir:
        staging = Path(staging_dir)

        if build_host:
            build_ssh_dest = ssh_dest_for(build_host, cfg.build_user)
            print(f"Checking SSH connectivity to build host {build_ssh_dest}...")
            try:
                ssh_run(build_ssh_dest, "true")
            except subprocess.CalledProcessError:
                print(
                    f"Hint: Verify your ssh config/keys with: ssh {build_ssh_dest}",
                    file=sys.stderr,
                )
                sys.exit("ERROR: SSH connectivity check to build host failed.")

            remote_staging = ""
            try:
                remote_staging = ssh_capture(
                    build_ssh_dest,
                    "mktemp",
                    "-d",
                    f"{build_project_root}/.deploy-remote-staging.XXXXXX",
                ).strip()
                if not remote_staging:
                    sys.exit("ERROR: Could not create remote build staging directory.")

                print(f"Building archives on {build_ssh_dest} ({build_project_root})...")
                run_remote_build(
                    build_ssh_dest,
                    build_project_root,
                    remote_staging,
                    full=full,
                    skip_export=args.skip_export,
                    hugo_base_url=hugo_base_url,
                )

                figures_archive, increment_archive, figures_name, increment_name, prefix = (
                    fetch_remote_archives(build_ssh_dest, remote_staging, staging)
                )
                host_id = host_id_from_archive_name(increment_name)
            finally:
                if remote_staging:
                    try:
                        ssh_run(build_ssh_dest, "rm", "-rf", "--", remote_staging)
                    except subprocess.CalledProcessError:
                        print(
                            f"Warning: Could not remove remote staging dir {remote_staging}",
                            file=sys.stderr,
                        )
        else:
            host_id = local_host_id()
            figures_archive, increment_archive, figures_name, increment_name, prefix = build_archives(
                cfg.base_dir,
                staging,
                full=full,
                skip_export=args.skip_export,
                hugo_base_url=hugo_base_url,
                host_id=host_id,
            )

        deploy_archives(
            ssh_dest,
            remote_archive,
            remote_deploy,
            full=full,
            no_delete=args.no_delete,
            host_id=host_id,
            figures_name=figures_name,
            increment_name=increment_name,
            prefix=prefix,
            figures_archive=figures_archive,
            increment_archive=increment_archive,
        )

    print("Deploy complete.")


if __name__ == "__main__":
    main()
