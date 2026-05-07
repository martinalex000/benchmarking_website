#!/usr/bin/env bash
# deploy.sh — build and rsync site to the production server
# Reads DEPLOY_USER, DEPLOY_HOST, DEPLOY_PATH from .env
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

# Load .env
if [[ -f .env ]]; then
  export $(grep -v '^#' .env | xargs)
fi

DEPLOY_USER="${DEPLOY_USER:-deploy}"
DEPLOY_HOST="${DEPLOY_HOST:?DEPLOY_HOST not set in .env}"
DEPLOY_PATH="${DEPLOY_PATH:-/var/www/graphbench}"
HUGO_BIN="${PROJECT_DIR}/bin/hugo"
[[ -x "$HUGO_BIN" ]] || HUGO_BIN="hugo"

echo "Building Hugo site…"
cd site
"$HUGO_BIN" --minify
cd ..

echo "Deploying to ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}"
rsync -avz --delete site/public/ "${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}/"

echo "Deploy complete."
