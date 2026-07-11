"""Read-only result indexes shared by a full Hugo export."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any

from sqlalchemy.orm import joinedload

from backend.models import DatasetVariant, Result


@dataclass
class ExportContext:
    """Keep export result lookups in memory instead of re-querying SQLite."""

    results_by_paper: dict[int, list[Result]] = field(default_factory=dict)
    results_by_variant: dict[int, list[Result]] = field(default_factory=dict)
    results_by_dataset_metric: dict[tuple[str, str], list[Result]] = field(default_factory=dict)

    @classmethod
    def load(cls, session: Any) -> ExportContext:
        results = (
            session.query(Result)
            .options(
                joinedload(Result.model),
                joinedload(Result.paper),
                joinedload(Result.dataset_variant).joinedload(DatasetVariant.dataset),
            )
            .filter(Result.is_problematic == 0)
            .all()
        )
        by_paper: dict[int, list[Result]] = defaultdict(list)
        by_variant: dict[int, list[Result]] = defaultdict(list)
        by_dataset_metric: dict[tuple[str, str], list[Result]] = defaultdict(list)
        for result in results:
            by_paper[result.paper_id].append(result)
            by_variant[result.dataset_variant_id].append(result)
            dataset = result.dataset_variant.dataset if result.dataset_variant else None
            if dataset:
                by_dataset_metric[(dataset.name, result.metric_name)].append(result)
        return cls(dict(by_paper), dict(by_variant), dict(by_dataset_metric))

    def attach(self, session: Any) -> None:
        session.info["export_context"] = self

    @staticmethod
    def from_session(session: Any) -> ExportContext | None:
        return getattr(session, "info", {}).get("export_context")

    def paper_results(self, paper_id: int) -> list[Result]:
        return self.results_by_paper.get(paper_id, [])

    def variant_results(self, variant_id: int) -> list[Result]:
        return self.results_by_variant.get(variant_id, [])

    def dataset_metric_results(self, dataset_name: str, metric_name: str) -> list[Result]:
        return self.results_by_dataset_metric.get((dataset_name, metric_name), [])
