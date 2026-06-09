"""Dataset statistics workspace — per-dataset, per-paper YAML artifacts."""

from __future__ import annotations

import logging
import re
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml

from backend.config import cfg

logger = logging.getLogger(__name__)


def slugify_dataset_name(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower())
    return slug.strip("-")


class DatasetStatsStorage:
    """Manage dataset-centric statistics files under datasets/{slug}/papers/{arxiv_id}.yaml."""

    def __init__(self, datasets_root: Path | None = None) -> None:
        self.root = datasets_root or cfg.datasets_dir

    def dataset_dir(self, dataset_name: str) -> Path:
        return self.root / slugify_dataset_name(dataset_name)

    def paper_stats_path(self, dataset_name: str, arxiv_id: str) -> Path:
        return self.dataset_dir(dataset_name) / "papers" / f"{arxiv_id}.yaml"

    def save_paper_stats(
        self,
        dataset_name: str,
        arxiv_id: str,
        payload: dict[str, Any],
    ) -> Path:
        path = self.paper_stats_path(dataset_name, arxiv_id)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fh:
            yaml.safe_dump(payload, fh, sort_keys=False, allow_unicode=True)
        logger.info("Saved dataset stats: %s", path)
        return path

    def load_paper_stats(self, dataset_name: str, arxiv_id: str) -> dict[str, Any] | None:
        path = self.paper_stats_path(dataset_name, arxiv_id)
        if not path.exists():
            return None
        with path.open(encoding="utf-8") as fh:
            return yaml.safe_load(fh)

    def list_paper_stats_for_arxiv(self, arxiv_id: str) -> list[tuple[str, Path]]:
        """Return (dataset_slug, path) for all stats files for a given paper."""
        if not self.root.exists():
            return []
        found: list[tuple[str, Path]] = []
        for dataset_dir in self.root.iterdir():
            if not dataset_dir.is_dir():
                continue
            path = dataset_dir / "papers" / f"{arxiv_id}.yaml"
            if path.exists():
                found.append((dataset_dir.name, path))
        return found

    def list_all_paper_stats(self) -> list[Path]:
        if not self.root.exists():
            return []
        return sorted(self.root.glob("*/papers/*.yaml"))

    @staticmethod
    def build_payload(
        *,
        arxiv_id: str,
        paper_title: str,
        dataset_entry: dict[str, Any],
        extraction_model: str,
    ) -> dict[str, Any]:
        return {
            "arxiv_id": arxiv_id,
            "paper_title": paper_title,
            "extracted_at": datetime.now(UTC).isoformat(),
            "extraction_model": extraction_model,
            **dataset_entry,
        }
