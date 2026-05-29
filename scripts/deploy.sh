#!/usr/bin/env bash
# deploy.sh — build and deploy Hugo site to production server via rsync/ssh
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

if ! command -v rsync >/dev/null 2>&1; then
  echo "Error: rsync is required for deployment but was not found in PATH." >&2
  exit 1
fi
if ! command -v tar >/dev/null 2>&1; then
  echo "Error: tar is required for deployment but was not found in PATH." >&2
  exit 1
fi

# Build Hugo site locally first.
echo "Building Hugo site locally..."
cd site
if [[ -n "$HUGO_BASE_URL" ]]; then
  "$HUGO_BIN" --minify --baseURL "$HUGO_BASE_URL"
else
  "$HUGO_BIN" --minify
fi
cd ..

echo "Syncing site/public/ to ${SSH_DEST}:${DEPLOY_PATH}/ ..."
if rsync \
  --archive \
  --delete \
  --compress \
  --human-readable \
  --itemize-changes \
  --stats \
  -e ssh \
  "${PROJECT_DIR}/site/public/" \
  "${SSH_DEST}:${DEPLOY_PATH}/"; then
  echo "Rsync deploy succeeded."
else
  echo "Rsync deploy failed; falling back to full tar upload via ssh..."

  REMOTE_PATH_Q="$(printf '%q' "$DEPLOY_PATH")"
  ssh "$SSH_DEST" "mkdir -p ${REMOTE_PATH_Q} && find ${REMOTE_PATH_Q} -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +"
  tar -C "${PROJECT_DIR}/site/public" -cf - . | ssh "$SSH_DEST" "tar -xf - -C ${REMOTE_PATH_Q}"
  echo "Fallback tar deploy succeeded."
fi

echo "Deploy complete."