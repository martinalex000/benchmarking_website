#!/usr/bin/env bash
# deploy.sh — build and deploy Hugo site via sshfs mount + rsync delta sync
# Reads DEPLOY_USER, DEPLOY_HOST, DEPLOY_PATH, and optional HUGO_BASE_URL from .env
set -euo pipefail

DELETE_MODE=true

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-delete)
      DELETE_MODE=false
      shift
      ;;
    *)
      echo "Usage: $0 [--no-delete]" >&2
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

err() {
  echo "ERROR: $*" >&2
}

hint() {
  echo "Hint: $*" >&2
}

die() {
  err "$*"
  exit 1
}

require_cmd() {
  local cmd="$1"
  command -v "$cmd" >/dev/null 2>&1 || die "Required command '$cmd' not found in PATH."
}

cleanup() {
  if [[ -n "${BUILD_DIR:-}" ]]; then
    rm -rf "$BUILD_DIR" >/dev/null 2>&1 || true
  fi

  if [[ -n "${MOUNT_POINT:-}" ]] && mountpoint -q "$MOUNT_POINT" 2>/dev/null; then
    if command -v fusermount >/dev/null 2>&1; then
      fusermount -u "$MOUNT_POINT" >/dev/null 2>&1 || true
    elif command -v umount >/dev/null 2>&1; then
      umount "$MOUNT_POINT" >/dev/null 2>&1 || true
    fi

    if mountpoint -q "$MOUNT_POINT" 2>/dev/null; then
      err "Could not unmount $MOUNT_POINT automatically."
      hint "Run manually: fusermount -u '$MOUNT_POINT' (or: umount '$MOUNT_POINT')."
    else
      echo "Unmounted ${MOUNT_POINT}"
    fi
  fi

  if [[ -n "${MOUNT_POINT:-}" ]]; then
    rmdir "$MOUNT_POINT" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

require_cmd uv
require_cmd ssh
require_cmd sshfs
require_cmd rsync
require_cmd mountpoint
require_cmd mktemp

# Load config using Python (handles .env parsing correctly)
CONFIG_OUTPUT="$(uv run python -c "
import sys
sys.path.insert(0, '.')
from backend.config import cfg
print(f'DEPLOY_USER={cfg.deploy_user}')
print(f'DEPLOY_HOST={cfg.deploy_host}')
print(f'DEPLOY_PATH={cfg.deploy_path}')
import os
hugo_url = os.environ.get('HUGO_BASE_URL', '')
print(f'HUGO_BASE_URL={hugo_url}')
")"
eval "$CONFIG_OUTPUT"

DEPLOY_USER="${DEPLOY_USER:-}" # Optional: empty means rely on ssh/config
DEPLOY_HOST="${DEPLOY_HOST:-}"
DEPLOY_PATH="${DEPLOY_PATH:-/var/www/graphbench}"

[[ -n "$DEPLOY_HOST" ]] || die "DEPLOY_HOST is empty. Set it in .env."
[[ -n "$DEPLOY_PATH" ]] || die "DEPLOY_PATH is empty. Set it in .env."

if [[ -n "$DEPLOY_USER" ]]; then
  SSH_DEST="${DEPLOY_USER}@${DEPLOY_HOST}"
else
  SSH_DEST="${DEPLOY_HOST}"
fi

HUGO_BASE_URL="${HUGO_BASE_URL:-}"
HUGO_BIN="${PROJECT_DIR}/bin/hugo"
[[ -x "$HUGO_BIN" ]] || HUGO_BIN="hugo"
require_cmd "$HUGO_BIN"

MOUNT_POINT="$(mktemp -d /tmp/deploy-XXXXXX)"
BUILD_DIR="$(mktemp -d "${PROJECT_DIR}/.deploy-build-XXXXXX")"

SSHFS_OPTS="${SSHFS_OPTS:-reconnect,ServerAliveInterval=15,ServerAliveCountMax=3}"

echo "Checking SSH connectivity to ${SSH_DEST}..."
if ! ssh -o BatchMode=yes -o ConnectTimeout=10 "$SSH_DEST" true; then
  hint "Verify your ssh config/keys with: ssh ${SSH_DEST}"
  die "SSH connectivity check failed."
fi

echo "Mounting ${SSH_DEST}:${DEPLOY_PATH} via sshfs at ${MOUNT_POINT}..."
if ! sshfs -o "$SSHFS_OPTS" "${SSH_DEST}:${DEPLOY_PATH}" "$MOUNT_POINT"; then
  hint "Verify destination exists and is accessible: ssh ${SSH_DEST} 'ls -ld ${DEPLOY_PATH}'"
  hint "Try mounting manually for detailed diagnostics: sshfs ${SSH_DEST}:${DEPLOY_PATH} ${MOUNT_POINT}"
  hint "If sshfs is blocked by hosting policy, direct rsync is an alternative:"
  hint "  rsync -avz --delete site/public/ ${SSH_DEST}:${DEPLOY_PATH}/"
  die "Failed to mount remote deployment path via sshfs."
fi

mountpoint -q "$MOUNT_POINT" || die "sshfs command returned, but ${MOUNT_POINT} is not a mounted filesystem."

WRITE_TEST="${MOUNT_POINT}/.deploy-write-test-$$"
if ! : >"$WRITE_TEST"; then
  hint "The mounted path may be read-only or permission-restricted."
  hint "Check remote ownership/ACLs for ${DEPLOY_PATH}."
  die "Mounted path is not writable."
fi
rm -f "$WRITE_TEST"

echo "Ensuring ${DEPLOY_PATH} has correct permissions on remote..."
ssh -o BatchMode=yes -o ConnectTimeout=10 "$SSH_DEST" "chmod 755 '${DEPLOY_PATH}'"

echo "Building Hugo site locally to ${BUILD_DIR}..."
cd site
if [[ -n "$HUGO_BASE_URL" ]]; then
  "$HUGO_BIN" --minify --baseURL "$HUGO_BASE_URL" -d "$BUILD_DIR"
else
  "$HUGO_BIN" --minify -d "$BUILD_DIR"
fi
cd ..

[[ -d "$BUILD_DIR" ]] || die "Hugo build did not produce output in ${BUILD_DIR}."

FILE_COUNT=$(find "$BUILD_DIR" -type f | wc -l)
[[ "$FILE_COUNT" -gt 0 ]] || die "Hugo build produced no files in ${BUILD_DIR}. Check build output above."

echo "Rsync delta sync to mounted target..."
RSYNC_OPTS=(--archive --no-group --compress --human-readable --itemize-changes --stats --progress)
if [[ "$DELETE_MODE" == "true" ]]; then
  RSYNC_OPTS+=(--delete)
fi

if ! rsync "${RSYNC_OPTS[@]}" \
  "${BUILD_DIR}/" \
  "${MOUNT_POINT}/"; then
  hint "Inspect mount health: ls -la ${MOUNT_POINT}"
  hint "Check free space remotely: ssh ${SSH_DEST} 'df -h ${DEPLOY_PATH}'"
  die "Rsync transfer to sshfs mount failed."
fi

echo "Verifying sync (rsync dry-run must report no pending changes)..."
VERIFY_OPTS=(--archive --no-group --itemize-changes --dry-run)
if [[ "$DELETE_MODE" == "true" ]]; then
  VERIFY_OPTS+=(--delete)
fi
VERIFY_OUTPUT="$(rsync "${VERIFY_OPTS[@]}" "${BUILD_DIR}/" "${MOUNT_POINT}/")"
if [[ -n "$VERIFY_OUTPUT" ]]; then
  echo "$VERIFY_OUTPUT" | sed -n '1,40p' >&2
  hint "Pending changes after sync indicate incomplete deployment or unstable mount state."
  hint "Retry deploy once; if it persists, remount and rerun."
  die "Post-sync verification failed."
fi

echo "Deploy complete and verified."