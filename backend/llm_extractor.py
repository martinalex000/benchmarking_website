"""Public API and CLI for the LLM extraction pipeline.

Implementation details live in :mod:`backend.llm_tasks`; this module remains
the stable import path used by the pipeline and command-line tooling.
"""

from __future__ import annotations

from backend.llm_metadata import (
    fetch_arxiv_authors,
    fetch_arxiv_metadata,
    fetch_semantic_scholar_published_date,
)
from backend.llm_tasks import LLMExtractor, run_extraction, run_figure_detection
from backend.llm_types import (
    BaselineModelInfo,
    CallRecord,
    DatasetInfo,
    DatasetList,
    DatasetStatisticsEntry,
    DatasetStatisticsOutput,
    ExtractionOutput,
    FigureInfo,
    ModelMetadataEnrichmentEntry,
    ModelMetadataEnrichmentOutput,
    ModelSizeEntry,
    ProposedModel,
    ResultEntry,
    ScreenResult,
    SotaClaimEntry,
    SotaClaimOutput,
    SotaClaimRestriction,
)

__all__ = [
    "BaselineModelInfo",
    "CallRecord",
    "DatasetInfo",
    "DatasetList",
    "DatasetStatisticsEntry",
    "DatasetStatisticsOutput",
    "ExtractionOutput",
    "FigureInfo",
    "LLMExtractor",
    "ModelMetadataEnrichmentEntry",
    "ModelMetadataEnrichmentOutput",
    "ModelSizeEntry",
    "ProposedModel",
    "ResultEntry",
    "ScreenResult",
    "SotaClaimEntry",
    "SotaClaimOutput",
    "SotaClaimRestriction",
    "fetch_arxiv_authors",
    "fetch_arxiv_metadata",
    "fetch_semantic_scholar_published_date",
    "run_extraction",
    "run_figure_detection",
]


if __name__ == "__main__":
    from backend.llm_tasks import main

    main()
