#!/usr/bin/env bash
# deploy.sh — build and deploy Hugo site to production server via sshfs
# Reads DEPLOY_USER, DEPLOY_HOST, DEPLOY_PATH, and optional HUGO_BASE_URL from .env
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

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

# Deployment configuration
DEPLOY_USER="${DEPLOY_USER:-}"       # Optional: empty means rely on ssh/config
DEPLOY_HOST="${DEPLOY_HOST:?DEPLOY_HOST not set in .env}"
DEPLOY_PATH="${DEPLOY_PATH:-/var/www/graphbench}"

# Build SSH destination: with user or without (relies on ssh/config)
if [[ -n "$DEPLOY_USER" ]]; then
  SSH_DEST="${DEPLOY_USER}@${DEPLOY_HOST}"
else
  SSH_DEST="${DEPLOY_HOST}"
fi

HUGO_BASE_URL="${HUGO_BASE_URL:-}"
HUGO_BIN="${PROJECT_DIR}/bin/hugo"
[[ -x "$HUGO_BIN" ]] || HUGO_BIN="hugo"

# Create temporary mount point and ensure cleanup on exit
MOUNT_POINT="/tmp/deploy-$$"
cleanup() {
  if mountpoint -q "$MOUNT_POINT" 2>/dev/null; then
    fusermount -u "$MOUNT_POINT" 2>/dev/null || umount "$MOUNT_POINT" 2>/dev/null || true
    echo "Unmounted ${MOUNT_POINT}"
  fi
  rmdir "$MOUNT_POINT" 2>/dev/null || true
}
trap cleanup EXIT

# Mount remote directory via sshfs
mkdir -p "$MOUNT_POINT"
echo "Mounting ${SSH_DEST}:${DEPLOY_PATH} via sshfs..."
sshfs "${SSH_DEST}:${DEPLOY_PATH}" "$MOUNT_POINT"

# Build Hugo site directly to the mounted remote directory
echo "Building and deploying Hugo site..."
cd site
if [[ -n "$HUGO_BASE_URL" ]]; then
  "$HUGO_BIN" --minify --baseURL "$HUGO_BASE_URL" --destination "$MOUNT_POINT"
else
  "$HUGO_BIN" --minify --destination "$MOUNT_POINT"
fi
cd ..

# Cleanup is handled by the EXIT trap
echo "Deploy complete."