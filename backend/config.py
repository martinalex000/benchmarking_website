"""Central configuration — loads .env and config/llm_config.yaml.

Usage:
    from backend.config import cfg

All paths are absolute Path objects resolved relative to the project root.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

import yaml
from dotenv import load_dotenv

# ── Project root (two levels up from this file: backend/ → project root) ──────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
_ARXIV_ID_RE = re.compile(r"^(?:arXiv:)?(\d{4}\.\d{4,5})(?:v\d+)?$", re.IGNORECASE)

# Load .env from project root (silently skip if not present)
load_dotenv(PROJECT_ROOT / ".env", override=False)


def _read_llm_config() -> dict:
    path = PROJECT_ROOT / "config" / "llm_config.yaml"
    if not path.exists():
        return {}
    with path.open() as fh:
        return yaml.safe_load(fh) or {}


_llm_cfg = _read_llm_config()

_DEFAULT_MODEL_PRIMARY = "openai-gpt-oss120b"
_DEFAULT_MODEL_FALLBACK = "minimax"
_DEFAULT_MODEL_SMALL = "gemma-3-27b"


class Config:
    """Single object holding all runtime configuration."""

    # ── Paths ──────────────────────────────────────────────────────────────
    project_root: Path = PROJECT_ROOT
    # Backwards-compatible alias used by older code
    base_dir: Path = PROJECT_ROOT
    data_dir: Path = PROJECT_ROOT / "data"
    papers_dir: Path = PROJECT_ROOT / "papers"
    datasets_dir: Path = PROJECT_ROOT / "datasets"
    logs_dir: Path = PROJECT_ROOT / "logs"
    site_dir: Path = PROJECT_ROOT / "site"
    config_dir: Path = PROJECT_ROOT / "config"
    prompts_dir: Path = PROJECT_ROOT / "config" / "prompts"

    db_path: Path = PROJECT_ROOT / "data" / "benchmarks.db"

    # ── LLM endpoint ───────────────────────────────────────────────────────
    llm_endpoint: str = os.environ.get("LLM_ENDPOINT", _llm_cfg.get("endpoint", ""))
    llm_api_key: str = os.environ.get("LLM_API_KEY", "")

    # Support both descriptive names and the existing numbered endpoint credentials.
    llm_glm_flash_second_endpoint: str = os.environ.get(
        "LLM_GLM_FLASH_SECOND_ENDPOINT", os.environ.get("LLM_ENDPOINT2", "")
    )
    llm_glm_flash_second_api_key: str = os.environ.get(
        "LLM_GLM_FLASH_SECOND_API_KEY", os.environ.get("LLM_API_KEY2", "")
    )

    # Optional separate local vLLM server (compare_models merges with llm_endpoint).
    llm_local_endpoint: str = os.environ.get("LLM_LOCAL_ENDPOINT", "")
    llm_local_api_key: str = os.environ.get("LLM_LOCAL_API_KEY", "")

    # ── Model tiers ────────────────────────────────────────────────────────
    # Model tiers are configured only through environment variables.
    model_primary: str = os.environ.get("LLM_MODEL_PRIMARY", _DEFAULT_MODEL_PRIMARY)
    model_fallback: str = os.environ.get("LLM_MODEL_FALLBACK", _DEFAULT_MODEL_FALLBACK)
    model_small: str = os.environ.get("LLM_MODEL_SMALL", _DEFAULT_MODEL_SMALL)

    # ── LLM generation parameters ──────────────────────────────────────────
    llm_max_tokens: int = int(_llm_cfg.get("max_tokens", 50_000))
    llm_max_total_tokens: int = int(_llm_cfg.get("max_total_tokens", 50_000))
    llm_temperature: float = float(_llm_cfg.get("temperature", 0.1))
    llm_timeout: int = int(_llm_cfg.get("timeout_seconds", 120))
    llm_max_retries: int = int(_llm_cfg.get("max_retries", 3))
    llm_retry_base_delay: float = float(_llm_cfg.get("retry_base_delay", 5))

    # ── Pipeline limits ────────────────────────────────────────────────────
    max_papers_per_run: int = int(_llm_cfg.get("max_papers_per_run", 0))

    # ── Deployment ─────────────────────────────────────────────────────────
    deploy_user: str = os.environ.get("DEPLOY_USER", "")
    deploy_host: str = os.environ.get("DEPLOY_HOST", "")
    deploy_path: str = os.environ.get("DEPLOY_PATH", "")
    build_host: str = os.environ.get("BUILD_HOST", "")
    build_user: str = os.environ.get("BUILD_USER", "")
    build_project_root: str = os.environ.get("BUILD_PROJECT_ROOT", "")
    # Fast local disk on the build host for Hugo output and deploy archives (e.g. /tmp/ritzert).
    build_tmp_dir: str = os.environ.get("BUILD_TMP_DIR", "")
    # Persistent deploy archives on the build host (default: BUILD_PROJECT_ROOT/deploy-archives).
    build_archive_dir: str = os.environ.get("BUILD_ARCHIVE_DIR", "")

    # ── External APIs ──────────────────────────────────────────────────────
    semantic_scholar_api_key: str = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    openreview_username: str = os.environ.get("OPENREVIEW_USERNAME", "")
    openreview_password: str = os.environ.get("OPENREVIEW_PASSWORD", "")
    openreview_token: str = os.environ.get("OPENREVIEW_TOKEN", "")
    # When true, skip export.arxiv.org metadata calls (use S2/local/OpenReview only).
    skip_arxiv_metadata_api: bool = os.environ.get("SKIP_ARXIV_METADATA_API", "").lower() in {
        "1",
        "true",
        "yes",
    }

    def model_for_tier(self, tier: str) -> str:
        """Return the model name for a given tier string.

        Accepts 'primary', 'fallback', 'small', or an explicit model name.
        """
        mapping = {
            "primary": self.model_primary,
            "fallback": self.model_fallback,
            "small": self.model_small,
        }
        return mapping.get(tier, tier)  # fallback: treat tier as explicit model name

    def ensure_dirs(self) -> None:
        """Create required directories if they don't exist."""
        for d in (self.data_dir, self.papers_dir, self.datasets_dir, self.logs_dir):
            d.mkdir(parents=True, exist_ok=True)


def normalize_arxiv_id(raw: str) -> str:
    """Normalize an arXiv ID to canonical form (e.g., '2206.08164v1' → '2206.08164')."""
    match = _ARXIV_ID_RE.fullmatch(str(raw or "").strip())
    if not match:
        raise ValueError(f"Invalid arXiv ID: {raw!r}")
    return match.group(1)


# Singleton instance — import and use directly
cfg = Config()
