"""Paper storage — manages the per-paper folder structure.

Each paper lives under  papers/{arxiv_id}/
  ├── metadata.json          ← tracked in git; written once, never overwritten
  ├── overrides.yaml         ← tracked in git; human corrections; NEVER overwritten
  ├── paper.pdf              ← gitignored (reproducible download)
  ├── html/                  ← gitignored (reproducible download)
  │   └── index.html (+ linked assets)
  ├── extracted/
  │   ├── text.txt           ← gitignored (derived)
    │   ├── llm_output.yaml    ← gitignored (derived, default)
    │   ├── llm_output.json    ← legacy fallback (compatibility)
  │   └── results_human_readable.md  ← TRACKED in git (verification artifact)
  └── figures/
      └── main_figure.{png|jpg}  ← gitignored
"""

from __future__ import annotations

import contextlib
import json
import logging
import os
import tempfile
from datetime import UTC, datetime
from pathlib import Path

import yaml

from backend.config import cfg

logger = logging.getLogger(__name__)


def load_yaml_dict(path: Path) -> dict | None:
    """Load a YAML file and return its top-level mapping, or None on failure."""
    try:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data if isinstance(data, dict) else None
    except Exception as exc:
        logger.warning("Failed to load %s: %s", path, exc)
        return None


OVERRIDES_TEMPLATE = """\
# overrides.yaml — edit this file to correct extraction errors.
# This file is NEVER overwritten by the pipeline.
# Re-run `python -m backend.reapply_overrides --paper {arxiv_id}` after editing.

paper_arxiv_id: "{arxiv_id}"

# Mark results as problematic (shown in grey on the leaderboard).
# problematic_results:
#   - model: "GraphGPS"
#     dataset: "Peptides-func"
#     metric: "AP"
#     reason: "Uses non-standard evaluation protocol"

# Override extracted values with correct ones.
# result_overrides:
#   - model: "GraphGPS"
#     dataset: "Peptides-func"
#     metric: "AP"
#     correct_value: 0.6534
#     correct_std: 0.0042
#     reason: "LLM read wrong table row — see Table 3 in paper"

# Fix metadata (codebase URL, etc.).
# metadata_overrides:
#   codebase_url: "https://github.com/example/repo"

# Notes about non-standard splits used in this paper.
# dataset_split_notes:
#   - dataset: "Cora"
#     is_standard_split: false
#     note: "Uses random 10-fold split, not the Planetoid public split"
"""


class PaperStorage:
    """Manages the folder structure for a single paper."""

    def __init__(self, arxiv_id: str, papers_root: Path | None = None) -> None:
        self.arxiv_id = arxiv_id
        self.root = (papers_root or cfg.papers_dir) / arxiv_id
        self.html_dir = self.root / "html"
        self.extracted_dir = self.root / "extracted"
        self.figures_dir = self.root / "figures"
        self.latex_dir = self.root / "latex"

    # ── Paths ─────────────────────────────────────────────────────────────
    @property
    def pdf_path(self) -> Path:
        return self.root / "paper.pdf"

    @property
    def html_index_path(self) -> Path:
        return self.html_dir / "index.html"

    @property
    def text_path(self) -> Path:
        return self.extracted_dir / "text.txt"

    @property
    def llm_output_path(self) -> Path:
        yaml_path = self.extracted_dir / "llm_output.yaml"
        json_path = self.extracted_dir / "llm_output.json"
        if yaml_path.exists():
            return yaml_path
        if json_path.exists():
            return json_path
        return yaml_path

    @property
    def llm_output_yaml_path(self) -> Path:
        return self.extracted_dir / "llm_output.yaml"

    @property
    def llm_output_json_path(self) -> Path:
        return self.extracted_dir / "llm_output.json"

    @property
    def llm_calls_path(self) -> Path:
        return self.extracted_dir / "llm_calls.yaml"

    @property
    def human_readable_path(self) -> Path:
        return self.extracted_dir / "results_human_readable.md"

    @property
    def metadata_path(self) -> Path:
        return self.root / "metadata.json"

    @property
    def overrides_path(self) -> Path:
        return self.root / "overrides.yaml"

    @property
    def main_figure_path(self) -> Path | None:
        """Return path to the main figure if it exists, else None."""
        for ext in ("png", "jpg", "jpeg", "svg"):
            p = self.figures_dir / f"main_figure.{ext}"
            if p.exists():
                return p
        return None

    # ── Initialisation ────────────────────────────────────────────────────
    def ensure_dirs(self) -> None:
        """Create all subdirectories."""
        for d in (self.root, self.html_dir, self.extracted_dir, self.figures_dir, self.latex_dir):
            d.mkdir(parents=True, exist_ok=True)

    def init_paper(self, metadata: dict) -> None:
        """Create metadata.json and overrides.yaml template on first setup.

        Idempotent — will not overwrite existing files.
        """
        self.ensure_dirs()

        # metadata.json — written once; updated if explicitly called
        if not self.metadata_path.exists():
            meta = {
                "arxiv_id": self.arxiv_id,
                "created_at": datetime.now(UTC).isoformat(),
                **metadata,
            }
            self.metadata_path.write_text(
                json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            logger.info("Created metadata.json for %s", self.arxiv_id)

        # overrides.yaml — created once, NEVER overwritten
        if not self.overrides_path.exists():
            self.overrides_path.write_text(
                OVERRIDES_TEMPLATE.format(arxiv_id=self.arxiv_id), encoding="utf-8"
            )
            logger.info("Created overrides.yaml template for %s", self.arxiv_id)

    def update_metadata(self, updates: dict) -> None:
        """Merge updates into metadata.json using atomic write to prevent corruption."""
        self.ensure_dirs()
        existing: dict = {}
        if self.metadata_path.exists():
            with contextlib.suppress(ValueError, OSError):
                existing = json.loads(self.metadata_path.read_text(encoding="utf-8"))
        existing.update(updates)
        existing["updated_at"] = datetime.now(UTC).isoformat()
        content = json.dumps(existing, indent=2, ensure_ascii=False)
        tmp_fd, tmp_path = tempfile.mkstemp(
            dir=self.metadata_path.parent, suffix=".tmp", prefix="metadata_"
        )
        try:
            os.write(tmp_fd, content.encode("utf-8"))
            os.close(tmp_fd)
            os.replace(tmp_path, self.metadata_path)
        except Exception:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise

    def read_metadata(self) -> dict:
        """Read metadata.json, return empty dict if not present."""
        if not self.metadata_path.exists():
            return {}
        try:
            return json.loads(self.metadata_path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            return {}

    def load_llm_output(self) -> dict:
        """Load extraction output, preferring YAML and falling back to JSON."""
        path = self.llm_output_path
        if not path.exists():
            return {}
        try:
            text = path.read_text(encoding="utf-8")
            if path.suffix.lower() in {".yaml", ".yml"}:
                return yaml.safe_load(text) or {}
            return json.loads(text)
        except (ValueError, OSError, yaml.YAMLError):
            return {}

    def save_llm_output(self, payload: dict) -> Path:
        """Save extraction output in YAML format (project default) using atomic write."""
        self.extracted_dir.mkdir(parents=True, exist_ok=True)
        out_path = self.llm_output_yaml_path
        content = yaml.safe_dump(payload, allow_unicode=True, sort_keys=False)
        tmp_fd, tmp_path = tempfile.mkstemp(
            dir=self.extracted_dir, suffix=".tmp", prefix="llm_output_"
        )
        try:
            os.write(tmp_fd, content.encode("utf-8"))
            os.close(tmp_fd)
            os.replace(tmp_path, out_path)
        except Exception:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)
            raise
        return out_path

    def load_llm_calls(self) -> list[dict]:
        """Load structured call logs for the most recent extraction, if present."""
        if not self.llm_calls_path.exists():
            return []
        try:
            loaded = yaml.safe_load(self.llm_calls_path.read_text(encoding="utf-8")) or []
        except (ValueError, OSError, yaml.YAMLError):
            return []
        return loaded if isinstance(loaded, list) else []
