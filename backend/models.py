"""SQLAlchemy ORM models — mirrors config/schema.sql exactly."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from enum import StrEnum

from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
    event,
)
from sqlalchemy.orm import DeclarativeBase, relationship


def _utcnow() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


AuthorRecord = dict[str, str | None]


def author_display_name(author: str | AuthorRecord) -> str:
    if isinstance(author, str):
        return author.strip()
    if isinstance(author, dict):
        return str(author.get("name") or "").strip()
    return ""


def normalize_author_entry(author: str | AuthorRecord) -> AuthorRecord:
    if isinstance(author, str):
        return {
            "name": author.strip(),
            "orcid": None,
            "s2_author_id": None,
            "s2_url": None,
        }
    if isinstance(author, dict):
        return {
            "name": str(author.get("name") or "").strip(),
            "orcid": author.get("orcid") or None,
            "s2_author_id": author.get("s2_author_id") or None,
            "s2_url": author.get("s2_url") or None,
        }
    return {"name": "", "orcid": None, "s2_author_id": None, "s2_url": None}


class TodoPaperStatus(StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    DONE = "done"
    FAILED = "failed"
    REJECTED = "rejected"


TODO_PAPER_FILTER_VALUES = tuple(status.value for status in TodoPaperStatus) + ("all",)


def todo_paper_status_from_exit_code(returncode: int) -> TodoPaperStatus:
    if returncode == 0:
        return TodoPaperStatus.DONE
    if returncode == 2:
        return TodoPaperStatus.REJECTED
    return TodoPaperStatus.FAILED


class Base(DeclarativeBase):
    pass


# ─────────────────────────────────────────────────────────────────────────────
class Benchmark(Base):
    __tablename__ = "benchmarks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    short_name = Column(String, nullable=False, unique=True)
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="SET NULL"), nullable=True)
    description = Column(Text)
    url = Column(String)
    source_papers = Column(Text)  # JSON list of benchmark/dataset source papers
    is_legacy = Column(Integer, nullable=False, default=0)
    created_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", foreign_keys=[paper_id], back_populates="benchmark_entry")
    datasets = relationship("Dataset", back_populates="benchmark")


# ─────────────────────────────────────────────────────────────────────────────
class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    benchmark_id = Column(Integer, ForeignKey("benchmarks.id", ondelete="SET NULL"))
    name = Column(String, nullable=False)
    short_description = Column(Text)  # One-line dataset-index summary
    description = Column(Text)
    detailed_description = Column(Text)  # JSON object of researched detail sections
    sources = Column(Text)  # JSON list of source/provenance records
    domain = Column(String)  # chemistry, social, citation, computer_vision
    task_type = Column(String)  # node_classification, graph_classification, …
    primary_metric = Column(String)  # AP, Accuracy, MAE, F1
    higher_is_better = Column(Integer, nullable=False, default=1)
    pyg_url = Column(String)  # Link to PyTorch Geometric dataset page, if available
    num_graphs = Column(Integer)
    avg_nodes = Column(Float)
    avg_edges = Column(Float)
    num_classes = Column(Integer)
    extra_stats = Column(Text)  # JSON dict of additional metrics
    created_at = Column(String, nullable=False, default=_utcnow)

    benchmark = relationship("Benchmark", back_populates="datasets")
    variants = relationship(
        "DatasetVariant", back_populates="dataset", cascade="all, delete-orphan"
    )


# ─────────────────────────────────────────────────────────────────────────────
class DatasetVariant(Base):
    __tablename__ = "dataset_variants"
    __table_args__ = (UniqueConstraint("dataset_id", "name"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    num_graphs = Column(Integer)
    avg_nodes = Column(Float)
    avg_edges = Column(Float)
    label_fraction = Column(Float)
    split_type = Column(String)  # fixed, random, scaffold, stratified
    is_standard = Column(Integer, nullable=False, default=1)
    notes = Column(Text)  # warning shown on website (e.g. "non-standard split")
    extra_stats = Column(Text)  # JSON dict of additional metrics
    created_at = Column(String, nullable=False, default=_utcnow)

    dataset = relationship("Dataset", back_populates="variants")
    results = relationship("Result", back_populates="dataset_variant", cascade="all, delete-orphan")


# ─────────────────────────────────────────────────────────────────────────────
class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    arxiv_id = Column(String, unique=True)
    arxiv_version = Column(Integer)
    title = Column(String, nullable=False)
    _authors = Column("authors", Text)  # stored as JSON
    abstract = Column(Text)
    published_date = Column(String)  # YYYY-MM-DD
    venue = Column(String)
    pdf_path = Column(String)
    html_path = Column(String)
    main_figure_path = Column(String)
    codebase_url = Column(String)
    extraction_status = Column(String, nullable=False, default="pending")
    extraction_model = Column(String)
    discovery_source = Column(String)
    is_benchmark_paper = Column(Integer, nullable=False, default=0)
    created_at = Column(String, nullable=False, default=_utcnow)
    updated_at = Column(String, nullable=False, default=_utcnow)

    benchmark_entry = relationship(
        "Benchmark", foreign_keys="Benchmark.paper_id", back_populates="paper", uselist=False
    )
    models = relationship("Model", back_populates="paper")
    results = relationship(
        "Result",
        foreign_keys="Result.paper_id",
        back_populates="paper",
        cascade="all, delete-orphan",
    )
    pipeline_runs = relationship(
        "PipelineRun", back_populates="paper", cascade="all, delete-orphan"
    )

    @property
    def authors(self) -> list[AuthorRecord]:
        if self._authors is None:
            return []
        try:
            raw = json.loads(self._authors)
        except (ValueError, TypeError):
            raw = [self._authors]
        if not isinstance(raw, list):
            return []
        return [normalize_author_entry(entry) for entry in raw if author_display_name(entry)]

    @authors.setter
    def authors(self, value: list[str | AuthorRecord] | str) -> None:
        if isinstance(value, list):
            normalized = [
                normalize_author_entry(entry) for entry in value if author_display_name(entry)
            ]
            self._authors = json.dumps(normalized, ensure_ascii=False)
        else:
            self._authors = value


# ─────────────────────────────────────────────────────────────────────────────
# todo_papers — administrative queue for papers to process
# ─────────────────────────────────────────────────────────────────────────────
class TodoPaper(Base):
    __tablename__ = "todo_papers"
    __table_args__ = (
        Index("idx_todo_status", "status"),
        Index("idx_todo_created_at", "created_at"),
        Index("idx_todo_seen_count", "seen_count"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    arxiv_id = Column(String, unique=True, nullable=False)
    title = Column(String)
    reason = Column(Text)
    added_by = Column(String)
    status = Column(
        String, nullable=False, default=TodoPaperStatus.PENDING.value
    )  # pending | processing | done | failed | rejected
    attempts = Column(Integer, nullable=False, default=0)
    last_attempt_at = Column(String)
    processing_token = Column(String)
    note = Column(Text)
    created_at = Column(String, nullable=False, default=_utcnow)
    cited_by_count = Column(Integer, nullable=False, default=0)
    cites_existing_count = Column(Integer, nullable=False, default=0)
    seen_count = Column(Integer, nullable=False, default=0)
    seen_from = Column(Text)
    first_seen_at = Column(String)
    is_manually_important = Column(Integer, nullable=False, default=0)


# ─────────────────────────────────────────────────────────────────────────────
class PendingDataset(Base):
    """Queue of datasets discovered by extraction but not yet canonicalized."""

    __tablename__ = "pending_datasets"
    __table_args__ = (
        UniqueConstraint("arxiv_id", "dataset_name"),
        Index("idx_pending_datasets_status", "status"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    arxiv_id = Column(String, nullable=False)
    paper_title = Column(String)
    dataset_name = Column(String, nullable=False)
    metrics_seen = Column(Text)  # JSON list[str]
    suggestion = Column(Text)  # JSON object from dataset_autoseed prompt
    discovery_payload = Column(Text)  # normalized DatasetInfo JSON observation
    status = Column(String, nullable=False, default="pending")
    resolved_dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="SET NULL"))
    created_at = Column(String, nullable=False, default=_utcnow)
    updated_at = Column(String, nullable=False, default=_utcnow)

    resolved_dataset = relationship("Dataset", foreign_keys=[resolved_dataset_id])

    @property
    def metrics_seen_list(self) -> list[str]:
        if not self.metrics_seen:
            return []
        try:
            loaded = json.loads(self.metrics_seen)
            if isinstance(loaded, list):
                return [str(item) for item in loaded if str(item).strip()]
        except (ValueError, TypeError):
            return []
        return []

    @metrics_seen_list.setter
    def metrics_seen_list(self, value: list[str]) -> None:
        self.metrics_seen = json.dumps(value, ensure_ascii=False)

    @property
    def suggestion_obj(self) -> dict:
        if not self.suggestion:
            return {}
        try:
            loaded = json.loads(self.suggestion)
            if isinstance(loaded, dict):
                return loaded
        except (ValueError, TypeError):
            return {}
        return {}

    @suggestion_obj.setter
    def suggestion_obj(self, value: dict) -> None:
        self.suggestion = json.dumps(value, ensure_ascii=False)

    @property
    def discovery_payload_obj(self) -> dict:
        if not self.discovery_payload:
            return {}
        try:
            loaded = json.loads(self.discovery_payload)
            return loaded if isinstance(loaded, dict) else {}
        except (ValueError, TypeError):
            return {}

    @discovery_payload_obj.setter
    def discovery_payload_obj(self, value: dict) -> None:
        self.discovery_payload = json.dumps(value, ensure_ascii=False, sort_keys=True)


# ─────────────────────────────────────────────────────────────────────────────
class PaperDatasetStatistics(Base):
    """Paper-reported dataset statistics extracted from research papers."""

    __tablename__ = "paper_dataset_statistics"
    __table_args__ = (
        UniqueConstraint("paper_id", "dataset_id"),
        Index("idx_paper_dataset_stats_dataset", "dataset_id"),
        Index("idx_paper_dataset_stats_status", "match_status"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="CASCADE"), nullable=False)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"), nullable=False)
    dataset_variant_id = Column(Integer, ForeignKey("dataset_variants.id", ondelete="SET NULL"))
    num_graphs = Column(Integer)
    avg_nodes = Column(Float)
    avg_edges = Column(Float)
    num_classes = Column(Integer)
    extra_stats = Column(Text)  # JSON dict
    raw_values = Column(Text)  # JSON dict of original strings
    precision_hints = Column(Text)  # JSON dict
    source_ref = Column(String)
    confidence = Column(String)
    match_status = Column(String, nullable=False, default="pending")
    mismatch_fields = Column(Text)  # JSON list
    match_details = Column(Text)  # JSON dict
    extracted_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", foreign_keys=[paper_id])
    dataset = relationship("Dataset", foreign_keys=[dataset_id])
    dataset_variant = relationship("DatasetVariant", foreign_keys=[dataset_variant_id])


# ─────────────────────────────────────────────────────────────────────────────
class PaperSotaClaim(Base):
    """SOTA performance claims extracted from paper prose."""

    __tablename__ = "paper_sota_claims"
    __table_args__ = (
        Index("idx_paper_sota_claims_paper", "paper_id"),
        Index("idx_paper_sota_claims_scope", "scope"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="CASCADE"), nullable=False)
    raw_sentence = Column(Text, nullable=False)
    claim_summary = Column(Text)
    datasets = Column(Text)  # JSON list of dataset name strings
    metrics = Column(Text)  # JSON list
    claim_type = Column(String)
    scope = Column(String, nullable=False, default="unclear")
    restrictions = Column(Text)  # JSON list of {type, description}
    source_ref = Column(String)
    confidence = Column(String)
    extracted_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", foreign_keys=[paper_id])


# ─────────────────────────────────────────────────────────────────────────────
class Model(Base):
    __tablename__ = "models"
    __table_args__ = (UniqueConstraint("canonical_name"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    canonical_name = Column(String, nullable=False)
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="SET NULL"))
    model_type = Column(String)  # gnn | graph_transformer | hybrid | llm | walk | svm_kernel | ...
    is_baseline = Column(Integer, nullable=False, default=0)
    created_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", back_populates="models")
    aliases = relationship("ModelAlias", back_populates="model", cascade="all, delete-orphan")
    results = relationship("Result", back_populates="model")


# ─────────────────────────────────────────────────────────────────────────────
class ModelAlias(Base):
    __tablename__ = "model_aliases"
    __table_args__ = (UniqueConstraint("alias"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    model_id = Column(Integer, ForeignKey("models.id", ondelete="CASCADE"), nullable=False)
    alias = Column(String, nullable=False)

    model = relationship("Model", back_populates="aliases")


# ─────────────────────────────────────────────────────────────────────────────
class Result(Base):
    __tablename__ = "results"
    __table_args__ = (
        UniqueConstraint("paper_id", "model_id", "dataset_variant_id", "metric_name"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="CASCADE"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id", ondelete="CASCADE"), nullable=False)
    dataset_variant_id = Column(
        Integer, ForeignKey("dataset_variants.id", ondelete="CASCADE"), nullable=False
    )
    metric_name = Column(String, nullable=False)
    metric_value = Column(Float, nullable=False)
    metric_std = Column(Float)  # ±std over seeds/folds
    is_baseline = Column(Integer, nullable=False, default=0)
    source_paper_id = Column(Integer, ForeignKey("papers.id", ondelete="SET NULL"))
    higher_is_better = Column(Integer, nullable=False, default=1)
    table_ref = Column(String)  # e.g. "Table 1"
    source_ref = Column(String)  # "this paper" or "Author Year"
    extraction_model = Column(String)  # model that extracted this result
    variant_inference_reason = Column(Text)
    evaluation_task = Column(String)
    protocol_decision = Column(String)
    protocol_note = Column(Text)
    uses_external_data = Column(Integer)  # 1=yes, 0=no, NULL=unknown
    input_feature_source = Column(String)
    feature_source_evidence = Column(Text)
    model_name_override = Column(String)
    params_millions = Column(Float)  # paper-local parameter count in millions
    # Human correction columns
    is_problematic = Column(Integer, nullable=False, default=0)
    problematic_reason = Column(Text)
    is_overridden = Column(Integer, nullable=False, default=0)
    override_value = Column(Float)
    override_std = Column(Float)
    override_reason = Column(Text)
    override_source = Column(String)  # path to the overrides.yaml that set this
    created_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", foreign_keys=[paper_id], back_populates="results")
    model = relationship("Model", back_populates="results")
    dataset_variant = relationship("DatasetVariant", back_populates="results")
    source_paper = relationship("Paper", foreign_keys=[source_paper_id])

    @property
    def display_value(self) -> float:
        """Return override_value if overridden, else metric_value."""
        return (
            self.override_value
            if self.is_overridden and self.override_value is not None
            else self.metric_value
        )

    @property
    def display_std(self) -> float | None:
        """Return override_std if overridden, else metric_std."""
        return self.override_std if self.is_overridden else self.metric_std

    @property
    def effective_model_name(self) -> str:
        """Return the curated model name used for grouping and comparisons."""
        return self.model_name_override or (self.model.canonical_name if self.model else "")


# ─────────────────────────────────────────────────────────────────────────────
class PipelineRun(Base):
    __tablename__ = "pipeline_runs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="SET NULL"))
    stage = Column(String, nullable=False)
    status = Column(String, nullable=False)  # success | failed | skipped
    model_used = Column(String)
    error_message = Column(Text)
    started_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", back_populates="pipeline_runs")


# ─────────────────────────────────────────────────────────────────────────────
class PaperCandidate(Base):
    """Audit log of every paper seen during discovery — including those filtered out.

    Tracks the full funnel:
      arXiv / Scholar fetch → stage1 relevance filter → stage2 benchmark check → accepted
    """

    __tablename__ = "paper_candidates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    arxiv_id = Column(String, unique=True)
    title = Column(String, nullable=False)
    abstract = Column(Text)
    published_date = Column(String)
    _authors = Column("authors", Text)  # JSON list
    categories = Column(Text)  # JSON list of arXiv categories

    # How the paper was discovered
    discovery_source = Column(String)  # arxiv_scanner | lrgb_citation | graphbench_citation
    discovery_detail = Column(Text)  # human-readable, e.g. "arXiv cs.LG sweep 7d"

    # Stage 1 — cheap LLM relevance filter
    stage1_passed = Column(Integer)  # NULL=not run, 0=failed, 1=passed
    stage1_confidence = Column(Float)
    stage1_reason = Column(Text)

    # Stage 2 — LLM benchmark presence check
    stage2_passed = Column(Integer)  # NULL=not run, 0=failed, 1=passed
    stage2_confidence = Column(Float)
    stage2_reason = Column(Text)
    stage2_datasets = Column(Text)  # JSON list of mentioned dataset names

    # Final disposition
    final_status = Column(
        String
    )  # accepted | rejected_stage1 | rejected_stage2 | duplicate | already_known
    paper_id = Column(Integer, ForeignKey("papers.id", ondelete="SET NULL"))

    created_at = Column(String, nullable=False, default=_utcnow)

    paper = relationship("Paper", foreign_keys=[paper_id])

    @property
    def authors(self) -> list[str]:
        if self._authors is None:
            return []
        try:
            return json.loads(self._authors)
        except (ValueError, TypeError):
            return [self._authors]

    @authors.setter
    def authors(self, value: list[str] | str) -> None:
        if isinstance(value, list):
            self._authors = json.dumps(value, ensure_ascii=False)
        else:
            self._authors = value


# ─────────────────────────────────────────────────────────────────────────────
# Auto-update updated_at on Paper saves
# ─────────────────────────────────────────────────────────────────────────────
@event.listens_for(Paper, "before_update")
def _paper_before_update(mapper, connection, target):  # noqa: ARG001
    target.updated_at = _utcnow()


@event.listens_for(PendingDataset, "before_update")
def _pending_dataset_before_update(mapper, connection, target):  # noqa: ARG001
    target.updated_at = _utcnow()
