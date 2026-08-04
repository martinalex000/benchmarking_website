#!/usr/bin/env python3
"""Build and deploy the Hugo site via SSH archives or GitHub Pages."""

from __future__ import annotations

import argparse
import hashlib
import os
import posixpath
import re
import shlex
import shutil
import socket
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import cfg

DEFAULT_DEPLOY_PATH = "/var/www/graphbench"
REMOTE_ARCHIVE_NAME = "deploy"
BUILD_ARCHIVE_SUBDIR = "deploy-archives"
SSH_OPTS = [
    "-o",
    "BatchMode=yes",
    "-o",
    "ConnectTimeout=60",
    "-o",
    "ServerAliveInterval=30",
    "-o",
    "ServerAliveCountMax=3",
    "-o",
    "ClearAllForwardings=yes",
    "-o",
    "WarnWeakCrypto=no",
]
DEPLOY_FILE_MODE = 0o755
GITHUB_PAGES_BRANCH_DEFAULT = "main"
GITHUB_PAGES_COMMIT_MESSAGE_DEFAULT = "Deploy Hugo site"
GITHUB_PAGES_REPO_DEFAULT = (
    "https://github.com/graphlearningbenchmarks/graphlearningbenchmarks.github.io"
)
GITHUB_PAGES_SSH_KEY_DEFAULT = Path.home() / ".ssh" / "graphlearningbenchmarks"
JPEGOPTIM_MARKER = ".jpegoptim"
MAX_IMAGE_SHORT_EDGE = 768
IMAGE_SUFFIXES = frozenset({".png", ".jpg", ".jpeg", ".webp"})
FIGURES_NAME_RE = re.compile(r"^-(\d{12})-figures\.tar\.zst$")
EXPORT_NAME_RE = re.compile(r"^-(\d{12})-export\.tar\.zst$")
INCREMENT_NAME_RE = re.compile(r"^-(\d{12})-increment\.tar\.zst$")
INCREMENT_SUFFIX = "-increment.tar.zst"
FIGURES_SUFFIX = "-figures.tar.zst"
EXPORT_SUFFIX = "-export.tar.zst"
STAGING_DIR_RE = re.compile(r"^/.+/\.deploy-remote-staging\.[A-Za-z0-9]{6}$")
ARCHIVE_NAME_RE = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._-]*-\d{12}-(?:figures|increment|export)\.tar\.zst$"
)
# Paths we must never pass to rm/clear helpers.
_BLOCKED_RM_PREFIXES = (
    "/",
    "/bin",
    "/etc",
    "/home",
    "/lib",
    "/root",
    "/tmp",  # nosec B108 — blocked path prefix, not a temp file usage
    "/usr",
    "/var",
)


def _normalize_remote_path(path: str) -> str:
    return path.strip().rstrip("/")


def _refuse_unsafe_rm_path(path: str, *, label: str, min_depth: int = 3) -> str:
    """Validate an absolute remote path before any destructive operation."""
    normalized = _normalize_remote_path(path)
    if not normalized:
        sys.exit(f"ERROR: Refusing {label}: path is empty.")
    if not normalized.startswith("/"):
        sys.exit(f"ERROR: Refusing {label}: path must be absolute ({normalized!r}).")
    if normalized in _BLOCKED_RM_PREFIXES:
        sys.exit(f"ERROR: Refusing {label}: blocked path {normalized!r}.")
    parts = [part for part in normalized.split("/") if part]
    if len(parts) < min_depth:
        sys.exit(
            f"ERROR: Refusing {label}: path too shallow ({normalized!r}); "
            f"need at least {min_depth} components."
        )
    return normalized


def _validate_remote_staging_dir(path: str, *, parent: str) -> str:
    normalized = _refuse_unsafe_rm_path(path, label="remote staging cleanup", min_depth=2)
    parent_norm = _normalize_remote_path(parent)
    if not normalized.startswith(f"{parent_norm}/"):
        sys.exit(
            f"ERROR: Refusing remote staging cleanup: {normalized!r} is not under {parent_norm!r}."
        )
    if normalized == parent_norm:
        sys.exit(f"ERROR: Refusing remote staging cleanup: path equals parent {parent_norm!r}.")
    if not STAGING_DIR_RE.fullmatch(normalized):
        sys.exit(
            f"ERROR: Refusing remote staging cleanup: {normalized!r} "
            "does not match .deploy-remote-staging.XXXXXX."
        )
    return normalized


def _validate_remote_deploy_dir(path: str) -> str:
    return _refuse_unsafe_rm_path(path, label="site tree clear", min_depth=3)


def _remote_parent(path: str) -> str:
    return posixpath.dirname(_normalize_remote_path(path))


def _remote_name(path: str) -> str:
    return posixpath.basename(_normalize_remote_path(path))


def _validate_remote_site_staging_dir(path: str, *, deploy_dir: str) -> str:
    normalized = _refuse_unsafe_rm_path(path, label="site staging cleanup", min_depth=3)
    deploy_norm = _validate_remote_deploy_dir(deploy_dir)
    parent = _remote_parent(deploy_norm)
    name = _remote_name(normalized)
    expected_prefix = f".{_remote_name(deploy_norm)}.deploy-next."
    if not normalized.startswith(f"{parent}/"):
        sys.exit(f"ERROR: Refusing site staging cleanup: {normalized!r} is not under {parent!r}.")
    if normalized == deploy_norm:
        sys.exit(f"ERROR: Refusing site staging cleanup: path equals deploy dir {deploy_norm!r}.")
    if not name.startswith(expected_prefix) or not re.fullmatch(
        rf"{re.escape(expected_prefix)}[A-Za-z0-9]{{6}}",
        name,
    ):
        sys.exit(
            f"ERROR: Refusing site staging cleanup: {normalized!r} "
            f"does not match {expected_prefix}XXXXXX."
        )
    return normalized


def _validate_remote_archive_name(name: str) -> str:
    base = Path(name).name
    if base != name or ".." in name or "/" in name:
        sys.exit(f"ERROR: Refusing archive delete: invalid name {name!r}.")
    if not ARCHIVE_NAME_RE.fullmatch(base):
        sys.exit(f"ERROR: Refusing archive delete: unexpected archive name {base!r}.")
    return base


def safe_remove_remote_staging_dir(ssh_dest: str, staging_dir: str, *, parent: str) -> None:
    validated = _validate_remote_staging_dir(staging_dir, parent=parent)
    staging_q = shlex.quote(validated)
    parent_q = shlex.quote(_normalize_remote_path(parent))
    remote_shell = (
        f"staging={staging_q} && parent={parent_q} && "
        f'case "$staging" in "$parent"/.deploy-remote-staging.*) ;; '
        f'*) echo "ERROR: refusing remote staging cleanup: $staging" >&2; exit 1;; esac && '
        f'if [ -d "$staging" ]; then find "$staging" -mindepth 1 -maxdepth 1 -exec rm -r -- {{}} +; rmdir "$staging"; fi'
    )
    ssh_run(ssh_dest, remote_shell)


def create_remote_site_staging_dir(ssh_dest: str, remote_deploy: str) -> str:
    deploy = _validate_remote_deploy_dir(remote_deploy)
    template = f"{_remote_parent(deploy)}/.{_remote_name(deploy)}.deploy-next.XXXXXX"
    staging = ssh_capture(ssh_dest, "mktemp", "-d", template).strip()
    if not staging:
        sys.exit("ERROR: Could not create remote site staging directory.")
    return _validate_remote_site_staging_dir(staging, deploy_dir=deploy)


def safe_remove_remote_site_staging_dir(
    ssh_dest: str,
    staging_dir: str,
    *,
    deploy_dir: str,
) -> None:
    validated = _validate_remote_site_staging_dir(staging_dir, deploy_dir=deploy_dir)
    staging_q = shlex.quote(validated)
    remote_shell = (
        f"staging={staging_q} && "
        f'if [ -d "$staging" ]; then find "$staging" -mindepth 1 -maxdepth 1 -exec rm -r -- {{}} +; rmdir "$staging"; fi'
    )
    ssh_run(ssh_dest, remote_shell)


def safe_swap_remote_site_tree(ssh_dest: str, remote_deploy: str, staging_dir: str) -> None:
    deploy = _validate_remote_deploy_dir(remote_deploy)
    staging = _validate_remote_site_staging_dir(staging_dir, deploy_dir=deploy)
    deploy_q = shlex.quote(deploy)
    staging_q = shlex.quote(staging)
    remote_shell = (
        f"deploy={deploy_q} && staging={staging_q} && "
        f'backup="${{deploy}}.deploy-prev.$$" && '
        f'[ -d "$deploy" ] && [ -d "$staging" ] || exit 1; '
        f'mv "$deploy" "$backup" || exit 1; '
        f'if mv "$staging" "$deploy"; then '
        f'if [ -d "$backup" ]; then '
        f'find "$backup" -mindepth 1 -maxdepth 1 -exec rm -r -- {{}} + && rmdir "$backup" '
        f'|| echo "Warning: deployed, but could not remove $backup" >&2; '
        f"fi; "
        f"else "
        f'mv "$backup" "$deploy"; '
        f'echo "ERROR: failed to promote staged site; restored previous site" >&2; '
        f"exit 1; "
        f"fi"
    )
    ssh_run(ssh_dest, remote_shell)


def safe_remove_remote_archive(
    ssh_dest: str,
    remote_archive: str,
    archive_name: str,
) -> None:
    validated_name = _validate_remote_archive_name(archive_name)
    archive_root = _refuse_unsafe_rm_path(remote_archive, label="archive delete", min_depth=2)
    remote_path = f"{archive_root}/{validated_name}"
    remote_q = shlex.quote(remote_path)
    remote_shell = (
        f"target={remote_q} && "
        f'[ -f "$target" ] || exit 0; '
        f'case "$(basename "$target")" in '
        f"*-????????????-figures.tar.zst|*-????????????-increment.tar.zst|"
        f"*-????????????-export.tar.zst) "
        f'rm -f -- "$target" ;; '
        f'*) echo "ERROR: refusing archive delete: $target" >&2; exit 1;; esac'
    )
    ssh_run(ssh_dest, remote_shell)


def log_remote(kind: str, detail: str) -> None:
    print(f"remote {kind}: {detail}")


def ssh_run(ssh_dest: str, *remote_cmd: str) -> None:
    """Run a command on the remote host via its login shell.

    Pass a single *remote_cmd* string for compound shell scripts (``cd … && …``).
    """
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


def run_rsync(cmd: list[str], *, retries: int = 3, retry_delay_s: float = 5.0) -> None:
    """Run rsync with retries for flaky HPC login-node SSH connections."""
    for attempt in range(1, retries + 1):
        try:
            subprocess.run(cmd, check=True)
            return
        except subprocess.CalledProcessError as exc:
            if attempt >= retries:
                raise
            print(
                f"Warning: rsync failed (attempt {attempt}/{retries}): {exc}",
                file=sys.stderr,
            )
            time.sleep(retry_delay_s)


def upload_archive(ssh_dest: str, local_path: Path, remote_path: str) -> None:
    target = f"{ssh_dest}:{remote_path}"
    log_remote("rsync", f"{local_path} -> {target}")
    run_rsync(
        ["rsync", "-ah", "--info=progress2", "-e", rsync_ssh_shell(), str(local_path), target],
    )


def download_archive(ssh_dest: str, remote_path: str, local_path: Path) -> None:
    source = f"{ssh_dest}:{remote_path}"
    log_remote("rsync", f"{source} -> {local_path}")
    run_rsync(
        ["rsync", "-ah", "--info=progress2", "-e", rsync_ssh_shell(), source, str(local_path)],
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


def extract_remote_archive(
    ssh_dest: str,
    remote_deploy: str,
    remote_archive_path: str,
    *,
    label: str,
) -> None:
    """Extract a remote .tar.zst archive via local zstd into a remote target dir."""
    log_remote(
        "ssh",
        f"{ssh_dest} cat {remote_archive_path}  |  zstd -d -c  |  "
        f"{ssh_dest} tar -xf - -C {remote_deploy}",
    )
    read_archive = subprocess.Popen(
        ["ssh", *SSH_OPTS, ssh_dest, "cat", remote_archive_path],
        stdout=subprocess.PIPE,
    )
    zstd = subprocess.Popen(
        ["zstd", "-d", "-c"],
        stdin=read_archive.stdout,
        stdout=subprocess.PIPE,
    )
    ssh = subprocess.Popen(
        ["ssh", *SSH_OPTS, ssh_dest, "tar", "-xf", "-", "-C", remote_deploy],
        stdin=zstd.stdout,
    )
    read_archive.stdout.close()
    zstd.stdout.close()
    print(f"Extracting remote {label}...")
    if read_archive.wait() != 0:
        raise subprocess.CalledProcessError(read_archive.returncode, read_archive.args)
    if zstd.wait() != 0:
        raise subprocess.CalledProcessError(zstd.returncode, zstd.args)
    if ssh.wait() != 0:
        raise subprocess.CalledProcessError(ssh.returncode, ssh.args)


def remote_home(ssh_dest: str) -> str:
    for remote_cmd in (("pwd",), ("cd ~ && pwd",)):
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
    fix_permissions: bool = False,
) -> None:
    if prepare:
        ssh_run(ssh_dest, "mkdir", "-p", remote_archive)
        ssh_run(ssh_dest, "mkdir", "-p", remote_deploy)
        ssh_run(ssh_dest, "test", "-w", remote_deploy)

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


def _latest_timestamped_archive(
    names: list[str],
    host_id: str,
    stamp_re: re.Pattern[str],
) -> str | None:
    best_name = ""
    best_stamp = ""
    for name in names:
        match = stamp_re.search(name.removeprefix(f"{host_id}"))
        if match and match.group(1) > best_stamp:
            best_stamp = match.group(1)
            best_name = name
    return best_name or None


def latest_figure_archive(names: list[str], host_id: str) -> str | None:
    return _latest_timestamped_archive(names, host_id, FIGURES_NAME_RE)


def latest_export_archive(names: list[str], host_id: str) -> str | None:
    return _latest_timestamped_archive(names, host_id, EXPORT_NAME_RE)


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
        safe_remove_remote_archive(ssh_dest, remote_archive, name)


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


def run_hugo_build(project_dir: Path, build_dir: str | Path, *, hugo_base_url: str) -> None:
    hugo_cmd = [
        "uv",
        "run",
        "hugo",
        "--minify",
        "--cleanDestinationDir",
        "--source",
        "site",
        "-d",
        str(build_dir),
    ]
    if hugo_base_url:
        hugo_cmd.extend(["--baseURL", hugo_base_url])
    subprocess.run(hugo_cmd, check=True, cwd=project_dir)


def _image_dimensions(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["magick", str(path), "-auto-orient", "-format", "%w %h", "info:"],
        check=True,
        capture_output=True,
        text=True,
    )
    try:
        width, height = (int(value) for value in result.stdout.split())
    except ValueError as exc:
        raise RuntimeError(f"Could not read dimensions for {path}") from exc
    return width, height


def _image_target_dimensions(width: int, height: int) -> tuple[int, int]:
    short_edge = min(width, height)
    if short_edge <= MAX_IMAGE_SHORT_EDGE:
        return width, height
    scale = MAX_IMAGE_SHORT_EDGE / short_edge
    return max(1, round(width * scale)), max(1, round(height * scale))


def normalize_image_tree(figures_dir: Path) -> dict[str, str]:
    """Convert figures to marked JPEGs and return old-to-new relative URL mappings.

    The marker in the filename makes this operation idempotent: a later deployment
    will not invoke jpegoptim again for an image that has already been processed.
    Smaller images are not upscaled; larger images have their short edge reduced to
    768 pixels.
    """
    require_cmd("magick")
    require_cmd("jpegoptim")
    if not figures_dir.is_dir():
        return {}

    replacements: dict[str, str] = {}
    normalized_count = 0
    reused_count = 0
    for source in sorted(figures_dir.rglob("*")):
        if not source.is_file() or source.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        if source.suffix.lower() == ".jpg" and source.stem.endswith(JPEGOPTIM_MARKER):
            continue

        target = source.with_name(f"{source.stem}{JPEGOPTIM_MARKER}.jpg")
        if target.exists() and target.stat().st_mtime >= source.stat().st_mtime:
            reused_count += 1
            replacements["/" + source.relative_to(figures_dir.parent).as_posix()] = (
                "/" + target.relative_to(figures_dir.parent).as_posix()
            )
            source.unlink()
            continue

        width, height = _image_dimensions(source)
        target_width, target_height = _image_target_dimensions(width, height)
        temporary = target.with_name(f".{target.stem}.tmp.jpg")
        try:
            subprocess.run(
                [
                    "magick",
                    str(source),
                    "-auto-orient",
                    "-resize",
                    f"{target_width}x{target_height}!",
                    "-background",
                    "white",
                    "-alpha",
                    "remove",
                    "-alpha",
                    "off",
                    "-colorspace",
                    "sRGB",
                    "-quality",
                    "88",
                    str(temporary),
                ],
                check=True,
            )
            subprocess.run(
                ["jpegoptim", "--strip-all", "--max=88", "--quiet", str(temporary)],
                check=True,
            )
            temporary.replace(target)
        finally:
            temporary.unlink(missing_ok=True)

        old_url = "/" + source.relative_to(figures_dir.parent).as_posix()
        new_url = "/" + target.relative_to(figures_dir.parent).as_posix()
        replacements[old_url] = new_url
        source.unlink()
        normalized_count += 1

    print(
        f"Normalized {normalized_count} images in {figures_dir} "
        f"({reused_count} existing marked outputs reused)."
    )
    return replacements


def rewrite_image_references(root: Path, replacements: dict[str, str]) -> int:
    """Update text references after image filenames are normalized."""
    if not replacements or not root.exists():
        return 0
    text_suffixes = {".html", ".md", ".json", ".xml", ".txt", ".css", ".js"}
    changed_files = 0
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = content
        for old_url, new_url in replacements.items():
            updated = updated.replace(old_url, new_url)
            updated = updated.replace(old_url.removeprefix("/"), new_url.removeprefix("/"))
        if updated != content:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
    return changed_files


def github_pages_git_env() -> dict[str, str]:
    key = Path(
        os.environ.get("GITHUB_PAGES_SSH_KEY", str(GITHUB_PAGES_SSH_KEY_DEFAULT))
    ).expanduser()
    if not key.is_file():
        sys.exit(f"ERROR: GitHub Pages SSH key not found: {key}")
    env = os.environ.copy()
    env["GIT_SSH_COMMAND"] = shlex.join(["ssh", "-i", str(key), "-o", "IdentitiesOnly=yes"])
    return env


def github_pages_git_remote(repo_url: str) -> str:
    """Use the SSH transport for GitHub URLs so the configured deploy key is used."""
    prefix = "https://github.com/"
    if repo_url.startswith(prefix):
        return f"git@github.com:{repo_url.removeprefix(prefix).removesuffix('.git')}.git"
    return repo_url


def _git(
    project_dir: Path, *args: str, capture_output: bool = False
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=project_dir,
        check=True,
        capture_output=capture_output,
        text=True if capture_output else None,
        env=github_pages_git_env(),
    )


def github_pages_checkout(project_dir: Path) -> tuple[Path, str]:
    repo_url = os.environ.get("GITHUB_PAGES_REPO", GITHUB_PAGES_REPO_DEFAULT).strip()
    repo = github_pages_git_remote(repo_url)
    branch = os.environ.get("GITHUB_PAGES_BRANCH", GITHUB_PAGES_BRANCH_DEFAULT).strip()
    checkout = Path(
        os.environ.get("GITHUB_PAGES_DIR", str(project_dir / ".github-pages")).strip()
    ).expanduser()
    if checkout.resolve() == project_dir.resolve():
        sys.exit("ERROR: GITHUB_PAGES_DIR must be separate from the source checkout.")

    if not checkout.exists():
        checkout.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--branch", branch, "--single-branch", repo, str(checkout)],
            check=True,
            env=github_pages_git_env(),
        )
    elif not (checkout / ".git").exists():
        sys.exit(f"ERROR: GITHUB_PAGES_DIR is not a Git checkout: {checkout}")
    else:
        status = _git(checkout, "status", "--porcelain", capture_output=True).stdout
        if status.strip():
            sys.exit(f"ERROR: GitHub Pages checkout has local changes: {checkout}")
        _git(checkout, "fetch", "origin", branch)
        _git(checkout, "checkout", branch)
        _git(checkout, "pull", "--ff-only", "origin", branch)
    return checkout, branch


def deploy_github_pages(project_dir: Path, *, skip_export: bool) -> None:
    """Push the prepared Hugo source tree to a separate github.io checkout."""
    require_cmd("git")
    require_cmd("rsync")
    checkout, branch = github_pages_checkout(project_dir)
    with tempfile.TemporaryDirectory(
        prefix=".github-pages-source-", dir=build_work_parent(project_dir)
    ) as tmp:
        source_dir = Path(tmp)
        prepare_hugo_content(project_dir, local_host_id(), skip_export=skip_export)
        shutil.copytree(
            project_dir / "site",
            source_dir,
            ignore=shutil.ignore_patterns("public", "resources", ".hugo_build.lock"),
            dirs_exist_ok=True,
        )
        figures_dir = source_dir / "static" / "figures"
        replacements = normalize_image_tree(figures_dir)
        changed_references = rewrite_image_references(source_dir / "content", replacements)
        print(f"Updated image references in {changed_references} generated files.")

        subprocess.run(
            [
                "rsync",
                "-a",
                "--delete",
                "--exclude=.git/",
                "--exclude=.github/",
                "--exclude=CNAME",
                f"{source_dir}/",
                f"{checkout}/",
            ],
            check=True,
        )

    status = _git(checkout, "status", "--porcelain", capture_output=True).stdout
    if not status.strip():
        print("GitHub Pages output is unchanged; no commit or push needed.")
        return

    _git(checkout, "add", "-A")
    staged = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=checkout, check=False)
    if staged.returncode == 0:
        print("GitHub Pages index is unchanged after staging; no commit or push needed.")
        return
    if staged.returncode != 1:
        sys.exit("ERROR: Could not inspect staged GitHub Pages changes.")
    commit_message = os.environ.get(
        "GITHUB_PAGES_COMMIT_MESSAGE", GITHUB_PAGES_COMMIT_MESSAGE_DEFAULT
    )
    _git(checkout, "commit", "-m", commit_message)
    _git(checkout, "push", "origin", branch)
    print(f"GitHub Pages deploy complete: {checkout} ({branch}).")


def archive_names(host_id: str, stamp: str | None = None) -> tuple[str, str, str]:
    stamp = stamp or datetime.now().strftime("%Y%m%d%H%M")
    prefix = f"{host_id}-{stamp}"
    return prefix, f"{prefix}{FIGURES_SUFFIX}", f"{prefix}{INCREMENT_SUFFIX}"


def host_id_from_archive_name(name: str) -> str:
    for suffix in (FIGURES_SUFFIX, INCREMENT_SUFFIX):
        if name.endswith(suffix):
            stamp_start = len(name) - len(suffix) - 12
            if stamp_start > 0:
                return name[:stamp_start].removesuffix("-")
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


def require_build_tools() -> None:
    for cmd in ("ssh", "rsync", "tar", "zstd", "uv"):
        require_cmd(cmd)
    tar_help = subprocess.run(["tar", "--help"], capture_output=True, text=True, check=False)
    if "--zstd" not in tar_help.stdout + tar_help.stderr:
        sys.exit("ERROR: tar on this system does not support --zstd.")


def require_deploy_tools() -> None:
    for cmd in ("ssh", "rsync", "tar", "zstd"):
        require_cmd(cmd)


def ssh_dest_for(host: str, user: str) -> str:
    return f"{user}@{host}" if user else host


def build_work_parent(project_dir: Path) -> Path:
    """Return the parent directory for Hugo build temp dirs (prefer fast local disk)."""
    tmp = cfg.build_tmp_dir.strip()
    if tmp:
        parent = Path(tmp)
        parent.mkdir(parents=True, exist_ok=True)
        return parent
    return project_dir


def remote_staging_parent(build_project_root: str) -> str:
    """Return the parent path for remote deploy archive staging."""
    tmp = cfg.build_tmp_dir.strip()
    if tmp:
        return tmp.rstrip("/")
    return build_project_root.rstrip("/")


def resolve_build_archive_dir(project_dir: Path) -> Path:
    """Return the persistent figures archive directory for a build host."""
    configured = cfg.build_archive_dir.strip()
    if configured:
        return Path(configured)
    return project_dir / BUILD_ARCHIVE_SUBDIR


def list_persisted_figure_names(archive_dir: Path, host_id: str) -> list[str]:
    if not archive_dir.is_dir():
        return []
    prefix = f"{host_id}-"
    return [
        path.name
        for path in archive_dir.iterdir()
        if path.is_file() and path.name.startswith(prefix) and path.name.endswith(FIGURES_SUFFIX)
    ]


def list_increment_archive_names(directory: Path, host_id: str | None = None) -> list[str]:
    if not directory.is_dir():
        return []
    return [
        path.name
        for path in directory.iterdir()
        if path.is_file()
        and path.name.endswith(INCREMENT_SUFFIX)
        and (host_id is None or path.name.startswith(f"{host_id}-"))
    ]


def find_latest_local_increment(search_dirs: list[Path]) -> tuple[Path, str] | None:
    best_dir: Path | None = None
    best_name = ""
    best_stamp = ""
    for directory in search_dirs:
        for name in list_increment_archive_names(directory):
            host_id = host_id_from_archive_name(name)
            match = INCREMENT_NAME_RE.search(name.removeprefix(host_id))
            if match and match.group(1) > best_stamp:
                best_stamp = match.group(1)
                best_name = name
                best_dir = directory
    if best_dir and best_name:
        return best_dir, best_name
    return None


def resolve_local_figures_archive(
    project_dir: Path,
    staging_dir: Path,
    prefix: str,
    host_id: str,
) -> tuple[Path | None, str | None]:
    figures_name = f"{prefix}{FIGURES_SUFFIX}"
    archive_dir = resolve_build_archive_dir(project_dir)
    for directory in (staging_dir, archive_dir):
        path = directory / figures_name
        if path.is_file():
            return path, figures_name
    latest_name = latest_figure_archive(list_persisted_figure_names(archive_dir, host_id), host_id)
    if latest_name:
        return archive_dir / latest_name, latest_name
    return None, None


def find_local_deploy_archives(
    project_dir: Path,
    *,
    full: bool,
) -> tuple[Path | None, Path, str | None, str, str, str]:
    archive_dir = resolve_build_archive_dir(project_dir)
    search_dirs = [archive_dir, *sorted(project_dir.glob(".deploy-staging-*"), reverse=True)]
    latest = find_latest_local_increment(search_dirs)
    if not latest:
        sys.exit(
            "ERROR: No local deploy archives found. "
            f"Looked under {archive_dir}/ and .deploy-staging-* in {project_dir}."
        )

    staging_dir, increment_name = latest
    increment_archive = staging_dir / increment_name
    host_id = host_id_from_archive_name(increment_name)
    prefix = increment_name.removesuffix(INCREMENT_SUFFIX)
    print(f"Using local increment archive {increment_archive}")

    figures_archive, figures_name = resolve_local_figures_archive(
        project_dir, staging_dir, prefix, host_id
    )
    if full:
        if not figures_archive:
            sys.exit(
                "ERROR: --full --upload-only needs a local figures archive. "
                f"None found for prefix {prefix} under {archive_dir}/."
            )
        print(f"Using local figures archive {figures_archive}")
    elif figures_archive:
        print(f"Using local figures archive {figures_archive} if needed for bootstrap")

    return figures_archive, increment_archive, figures_name, increment_name, prefix, host_id


def persist_figures_archive(project_dir: Path, source: Path, figures_name: str) -> Path:
    archive_dir = resolve_build_archive_dir(project_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)
    dest = archive_dir / figures_name
    shutil.copy2(source, dest)
    print(f"Stored figures archive at {dest}")
    return dest


def persist_increment_archive(project_dir: Path, source: Path, increment_name: str) -> Path:
    archive_dir = resolve_build_archive_dir(project_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)
    dest = archive_dir / increment_name
    shutil.copy2(source, dest)
    print(f"Stored increment archive at {dest}")
    return dest


def persist_deploy_archives(
    project_dir: Path,
    increment_archive: Path,
    increment_name: str,
    figures_archive: Path | None,
    figures_name: str | None,
) -> None:
    """Keep local copies of deploy archives for --upload-only retries."""
    persist_increment_archive(project_dir, increment_archive, increment_name)
    if not figures_archive or not figures_name or not figures_archive.is_file():
        return
    dest = resolve_build_archive_dir(project_dir) / figures_name
    if dest.exists() and file_sha256(dest) == file_sha256(figures_archive):
        return
    persist_figures_archive(project_dir, figures_archive, figures_name)


def stage_persisted_figures(
    project_dir: Path,
    staging_dir: Path,
    host_id: str,
) -> tuple[Path | None, str | None]:
    """Copy the latest persisted figures archive into staging for deploy."""
    archive_dir = resolve_build_archive_dir(project_dir)
    latest_name = latest_figure_archive(list_persisted_figure_names(archive_dir, host_id), host_id)
    if not latest_name:
        return None, None
    source = archive_dir / latest_name
    dest = staging_dir / latest_name
    shutil.copy2(source, dest)
    print(f"Using persisted figures archive {source}")
    return dest, latest_name


EXPORT_SNAPSHOT_PATHS = (
    "site/content",
    "site/data",
    "site/static/figures",
    "site/static/data/datasets",
)


def export_artifacts_ready(project_dir: Path) -> bool:
    benchmarks = project_dir / "site/data/benchmarks.json"
    content = project_dir / "site/content"
    chart_data = project_dir / "site/static/data/datasets"
    if not benchmarks.is_file() or not content.is_dir():
        return False
    if not chart_data.is_dir() or not any(chart_data.rglob("*.json")):
        return False
    return any(content.rglob("*.md"))


def list_persisted_export_names(archive_dir: Path, host_id: str) -> list[str]:
    if not archive_dir.is_dir():
        return []
    prefix = f"{host_id}-"
    return [
        path.name
        for path in archive_dir.iterdir()
        if path.is_file() and path.name.startswith(prefix) and path.name.endswith(EXPORT_SUFFIX)
    ]


def persist_export_snapshot(project_dir: Path, host_id: str) -> Path | None:
    paths = [rel for rel in EXPORT_SNAPSHOT_PATHS if (project_dir / rel).exists()]
    if not paths:
        return None
    stamp = datetime.now().strftime("%Y%m%d%H%M")
    name = f"{host_id}-{stamp}{EXPORT_SUFFIX}"
    archive_dir = resolve_build_archive_dir(project_dir)
    archive_dir.mkdir(parents=True, exist_ok=True)
    dest = archive_dir / name
    subprocess.run(
        ["tar", "-C", str(project_dir), "--zstd", "-cf", str(dest), *paths],
        check=True,
    )
    print(f"Stored export snapshot at {dest}")
    return dest


def restore_latest_export(project_dir: Path, host_id: str) -> bool:
    archive_dir = resolve_build_archive_dir(project_dir)
    latest_name = latest_export_archive(list_persisted_export_names(archive_dir, host_id), host_id)
    if not latest_name:
        return False
    source = archive_dir / latest_name
    print(f"Restoring export snapshot {source}...")
    subprocess.run(
        ["tar", "-C", str(project_dir), "--zstd", "-xf", str(source)],
        check=True,
    )
    return True


def prepare_hugo_content(
    project_dir: Path,
    host_id: str,
    *,
    skip_export: bool,
) -> None:
    if skip_export:
        if export_artifacts_ready(project_dir):
            print("Skipping export; reusing existing Hugo content in site/...")
            return
        if restore_latest_export(project_dir, host_id):
            print("Skipping export; restored latest export snapshot.")
            return
        sys.exit(
            "ERROR: --skip-export requested but no Hugo export found. "
            "Run a deploy without --skip-export first."
        )

    print("Exporting Hugo content from database (includes site/content/dev)...")
    subprocess.run(
        [sys.executable, "-m", "backend.export_to_hugo", "--skip-build"],
        check=True,
        cwd=project_dir,
    )
    persist_export_snapshot(project_dir, host_id)


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
    work_parent = build_work_parent(project_dir)
    include_figures = full
    if (
        not include_figures
        and latest_figure_archive(
            list_persisted_figure_names(resolve_build_archive_dir(project_dir), host_id),
            host_id,
        )
        is None
    ):
        print("No persisted figures archive; including figures in this build.")
        include_figures = True

    built_figures: Path | None = None
    staged_figures_name: str | None = None

    with tempfile.TemporaryDirectory(prefix=".deploy-build-", dir=work_parent) as build_dir:
        build = Path(build_dir)

        prepare_hugo_content(project_dir, host_id, skip_export=skip_export)

        print(f"Building Hugo site to {build_dir}...")
        run_hugo_build(project_dir, build_dir, hugo_base_url=hugo_base_url)

        files = list(build.rglob("*"))
        if not any(p.is_file() for p in files):
            sys.exit(f"ERROR: Hugo build produced no files in {build_dir}.")

        print("Normalizing build tree permissions to 755...")
        for path in files:
            path.chmod(DEPLOY_FILE_MODE)

        figures_dir = build / "figures"
        has_figures = figures_dir.is_dir() and any(p.is_file() for p in figures_dir.rglob("*"))
        if has_figures:
            print(f"Creating figures archive {figures_name}...")
            subprocess.run(
                ["tar", "-C", build_dir, "--zstd", "-cf", figures_archive, "figures"], check=True
            )
            print(figures_archive)
            built_figures = figures_archive
            persist_figures_archive(project_dir, figures_archive, figures_name)
            staged_figures_name = figures_name
        elif include_figures:
            sys.exit(f"ERROR: No figures found in {figures_dir}. Run export before a full deploy.")

        print(f"Creating increment archive {increment_name}...")
        subprocess.run(
            ["tar", "-C", build_dir, "--zstd", "--exclude=figures", "-cf", increment_archive, "."],
            check=True,
        )
        print(increment_archive)
        persist_increment_archive(project_dir, increment_archive, increment_name)

    if not built_figures:
        built_figures, staged_figures_name = stage_persisted_figures(
            project_dir, staging_dir, host_id
        )

    return (
        built_figures,
        increment_archive,
        staged_figures_name,
        increment_name,
        prefix,
    )


def run_remote_build(
    build_ssh_dest: str,
    project_root: str,
    remote_staging: str,
    *,
    full: bool,
    skip_export: bool,
    hugo_base_url: str,
) -> None:
    staging_q = shlex.quote(remote_staging)
    script_q = shlex.quote("scripts/deploy.py")

    exports: list[str] = []
    if hugo_base_url:
        exports.append(f"export HUGO_BASE_URL={shlex.quote(hugo_base_url)}")
    build_tmp = cfg.build_tmp_dir.strip()
    if build_tmp:
        exports.append(f"export BUILD_TMP_DIR={shlex.quote(build_tmp)}")
    export_cmd = " && ".join(exports)
    if export_cmd:
        export_cmd += " && "

    deploy_flags = ""
    if full:
        deploy_flags += " --full"
    if skip_export:
        deploy_flags += " --skip-export"

    remote_shell = (
        f'cd {shlex.quote(project_root)} || {{ echo "ERROR: cannot cd to {project_root}" >&2; exit 1; }} && '
        f"{export_cmd}"
        # A positive niceness lowers CPU priority on the remote build host.
        f"nice -n 10 uv run --no-sync python {script_q} "
        f"--build-only --staging-dir {staging_q}{deploy_flags}"
    )
    ssh_run(build_ssh_dest, remote_shell)


def fetch_remote_archives(
    build_ssh_dest: str,
    remote_staging: str,
    local_staging: Path,
    *,
    build_project_root: str = "",
) -> tuple[Path | None, Path, str | None, str, str]:
    try:
        output = ssh_capture(build_ssh_dest, "ls", "-1", remote_staging)
    except subprocess.CalledProcessError as exc:
        sys.exit(f"ERROR: Could not list remote build staging dir {remote_staging}: {exc}")

    names = [line.strip() for line in output.splitlines() if line.strip()]
    figures_name, increment_name = list_staging_archives(names)
    prefix = increment_name.removesuffix(INCREMENT_SUFFIX)

    figures_archive: Path | None = None
    if figures_name:
        figures_archive = local_staging / figures_name
        print(f"Downloading {figures_name} from build host staging...")
        download_archive(build_ssh_dest, f"{remote_staging}/{figures_name}", figures_archive)
    elif build_project_root:
        host_id = host_id_from_archive_name(increment_name)
        archive_dir = resolve_build_archive_dir(Path(build_project_root))
        latest_name = latest_figure_archive(
            list_persisted_figure_names(archive_dir, host_id),
            host_id,
        )
        if latest_name:
            figures_name = latest_name
            figures_archive = local_staging / figures_name
            remote_path = f"{archive_dir}/{figures_name}"
            print(f"Downloading persisted {figures_name} from build host...")
            download_archive(build_ssh_dest, remote_path, figures_archive)

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
    host_id: str,
    figures_name: str | None,
    increment_name: str,
    prefix: str,
    figures_archive: Path | None,
    increment_archive: Path,
) -> None:
    baseline: str | None = None
    bootstrap_figures = False
    update_figures = False
    if not full:
        baseline = latest_figure_archive(
            list_remote_figure_archives(ssh_dest, remote_archive, host_id),
            host_id,
        )
        if not baseline:
            if figures_archive and figures_name:
                print(
                    f"No figures archive for {host_id} on server; "
                    f"bootstrapping with {figures_name}..."
                )
                bootstrap_figures = True
                baseline = figures_name
            else:
                print(
                    "ERROR: Incremental deploy needs a figures archive from this machine on the server.",
                    file=sys.stderr,
                )
                print(
                    f"ERROR: None found for host {host_id} under {remote_archive}/.",
                    file=sys.stderr,
                )
                print(
                    f"Hint: Run a full deploy first: {Path(__file__).name} --full",
                    file=sys.stderr,
                )
                sys.exit(1)
        else:
            print(f"Using baseline figure archive: {baseline}")
            if figures_archive and figures_name:
                remote_figures_path = f"{remote_archive}/{baseline}"
                remote_hash = remote_file_sha256(ssh_dest, remote_figures_path)
                local_hash = file_sha256(figures_archive)
                if not remote_hash or remote_hash != local_hash:
                    print(f"Figures changed; uploading {figures_name}...")
                    update_figures = True
                    baseline = figures_name

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

    to_upload: list[tuple[Path, str]] = [(increment_archive, increment_name)]
    figure_extract_local: tuple[Path, str] | None = None
    figure_extract_remote: str | None = None
    if (
        bootstrap_figures
        and figures_archive
        and figures_name
        or update_figures
        and figures_archive
        and figures_name
    ):
        to_upload.insert(0, (figures_archive, figures_name))
        figure_extract_local = (figures_archive, figures_name)
    elif full and figures_name:
        if reuse_figures_archive:
            if figures_archive:
                figure_extract_local = (figures_archive, figures_name)
            else:
                figure_extract_remote = figures_name
        elif figures_archive:
            to_upload.insert(0, (figures_archive, figures_name))
            figure_extract_local = (figures_archive, figures_name)
    elif not full:
        if figures_archive and figures_name:
            figure_extract_local = (figures_archive, figures_name)
        elif baseline:
            figure_extract_remote = baseline

    if not figure_extract_local and not figure_extract_remote:
        sys.exit("ERROR: Deploy cannot construct staged site without a figures archive.")

    for local_path, remote_name in to_upload:
        upload_archive(ssh_dest, local_path, f"{remote_archive}/{remote_name}")

    staging_dir = create_remote_site_staging_dir(ssh_dest, remote_deploy)
    promoted = False
    try:
        print(f"Extracting deploy archives into remote staging dir: {staging_dir}")
        if figure_extract_local:
            local_path, _remote_name = figure_extract_local
            extract_archive(ssh_dest, staging_dir, local_path)
        elif figure_extract_remote:
            extract_remote_archive(
                ssh_dest,
                staging_dir,
                f"{remote_archive}/{figure_extract_remote}",
                label=figure_extract_remote,
            )
        extract_archive(ssh_dest, staging_dir, increment_archive)
        unpack_remotely(ssh_dest, staging_dir, remote_archive, fix_permissions=True)
        safe_swap_remote_site_tree(ssh_dest, remote_deploy, staging_dir)
        promoted = True
    finally:
        if not promoted:
            try:
                safe_remove_remote_site_staging_dir(
                    ssh_dest,
                    staging_dir,
                    deploy_dir=remote_deploy,
                )
            except subprocess.CalledProcessError:
                print(
                    f"Warning: Could not remove remote site staging dir {staging_dir}",
                    file=sys.stderr,
                )

    keep_figures = figures_name if full else baseline
    if keep_figures:
        maybe_prune_old_archives(ssh_dest, remote_archive, host_id, keep_figures)


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
        "--github-pages",
        action="store_true",
        help="Build and push the site to a separate GitHub Pages checkout.",
    )
    parser.add_argument(
        "--skip-export",
        action="store_true",
        help=(
            "Skip database export; reuse existing site/ content or restore the latest "
            "export snapshot from deploy-archives/."
        ),
    )
    parser.add_argument(
        "--upload-only",
        action="store_true",
        help=(
            "Skip build; upload and deploy the latest local archives "
            "(for retry after an aborted deploy)."
        ),
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

    if args.upload_only and args.build_only:
        sys.exit("ERROR: --upload-only cannot be used with --build-only.")
    if args.upload_only and args.skip_export:
        sys.exit("ERROR: --upload-only cannot be used with --skip-export.")
    if args.github_pages and (
        args.full or args.incremental or args.upload_only or args.build_only or args.staging_dir
    ):
        sys.exit(
            "ERROR: --github-pages cannot be combined with --full, --incremental, "
            "--upload-only, --build-only, or --staging-dir."
        )

    full = args.full
    hugo_base_url = os.environ.get("HUGO_BASE_URL", "")

    if args.github_pages:
        deploy_github_pages(cfg.base_dir, skip_export=args.skip_export)
        return

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
    require_deploy_tools() if args.upload_only else require_build_tools()

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

    if args.upload_only:
        (
            figures_archive,
            increment_archive,
            figures_name,
            increment_name,
            prefix,
            host_id,
        ) = find_local_deploy_archives(cfg.base_dir, full=full)
        deploy_archives(
            ssh_dest,
            remote_archive,
            remote_deploy,
            full=full,
            host_id=host_id,
            figures_name=figures_name,
            increment_name=increment_name,
            prefix=prefix,
            figures_archive=figures_archive,
            increment_archive=increment_archive,
        )
        print("Deploy complete.")
        return

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
                staging_parent = remote_staging_parent(build_project_root)
                if cfg.build_tmp_dir.strip():
                    ssh_run(build_ssh_dest, "mkdir", "-p", staging_parent)
                remote_staging = ssh_capture(
                    build_ssh_dest,
                    "mktemp",
                    "-d",
                    f"{staging_parent}/.deploy-remote-staging.XXXXXX",
                ).strip()
                if not remote_staging:
                    sys.exit("ERROR: Could not create remote build staging directory.")

                build_tmp_note = ""
                if cfg.build_tmp_dir.strip():
                    build_tmp_note = f", build tmp {cfg.build_tmp_dir.strip()}"
                print(
                    f"Building archives on {build_ssh_dest} "
                    f"({build_project_root}{build_tmp_note})..."
                )
                archive_dir = resolve_build_archive_dir(Path(build_project_root))
                ssh_run(build_ssh_dest, "mkdir", "-p", str(archive_dir))
                run_remote_build(
                    build_ssh_dest,
                    build_project_root,
                    remote_staging,
                    full=full,
                    skip_export=args.skip_export,
                    hugo_base_url=hugo_base_url,
                )

                figures_archive, increment_archive, figures_name, increment_name, prefix = (
                    fetch_remote_archives(
                        build_ssh_dest,
                        remote_staging,
                        staging,
                        build_project_root=build_project_root,
                    )
                )
                host_id = host_id_from_archive_name(increment_name)
            finally:
                if remote_staging:
                    try:
                        safe_remove_remote_staging_dir(
                            build_ssh_dest,
                            remote_staging,
                            parent=staging_parent,
                        )
                    except subprocess.CalledProcessError:
                        print(
                            f"Warning: Could not remove remote staging dir {remote_staging}",
                            file=sys.stderr,
                        )
        else:
            host_id = local_host_id()
            figures_archive, increment_archive, figures_name, increment_name, prefix = (
                build_archives(
                    cfg.base_dir,
                    staging,
                    full=full,
                    skip_export=args.skip_export,
                    hugo_base_url=hugo_base_url,
                    host_id=host_id,
                )
            )

        persist_deploy_archives(
            cfg.base_dir,
            increment_archive,
            increment_name,
            figures_archive,
            figures_name,
        )

        deploy_archives(
            ssh_dest,
            remote_archive,
            remote_deploy,
            full=full,
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
