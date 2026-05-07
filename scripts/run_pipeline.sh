#!/usr/bin/env bash
# run_pipeline.sh — cron-friendly pipeline runner
# Usage: ./scripts/run_pipeline.sh [--force] [--model fallback]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Activate uv-managed environment
source .venv/bin/activate 2>/dev/null || true

ARGS="$*"
LOG_FILE="logs/pipeline_$(date +%Y%m%d_%H%M%S).log"
mkdir -p logs

echo "[$(date -Iseconds)] Starting pipeline run" | tee -a "$LOG_FILE"
python -m backend.pipeline run-all --all $ARGS 2>&1 | tee -a "$LOG_FILE"
echo "[$(date -Iseconds)] Pipeline run complete" | tee -a "$LOG_FILE"
