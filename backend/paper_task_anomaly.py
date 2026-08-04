"""Detect papers whose per-dataset result distributions look unusual."""

from __future__ import annotations

import csv
import json
import math
import sqlite3
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.cluster import HDBSCAN


@dataclass(frozen=True)
class ResultRow:
    paper_id: int
    arxiv_id: str
    title: str
    dataset_id: int
    dataset: str
    task_type: str
    primary_metric: str
    metric: str
    value: float
    evaluation_task: str
    protocol_decision: str


@dataclass
class Observation:
    paper_id: int
    arxiv_id: str
    title: str
    dataset_id: int
    dataset: str
    task_type: str
    primary_metric: str
    metric: str
    result_count: int
    value_mean: float
    value_std: float
    evaluation_tasks: list[str]
    protocol_decisions: list[str]
    cohort_size: int = 0
    mean_robust_z: float | None = None
    std_robust_z: float | None = None
    robust_distance: float | None = None
    cluster_label: int | None = None
    cluster_size: int | None = None
    cluster_fraction: float | None = None
    cluster_probability: float | None = None
    cluster_noise: bool = False
    minority_cluster: bool = False
    suspicious: bool = False
    reasons: list[str] | None = None


def _finite(value: Any) -> float | None:
    try:
        converted = float(value)
    except (TypeError, ValueError):
        return None
    return converted if math.isfinite(converted) else None


def _read_rows(db_path: Path, *, include_problematic: bool = False) -> list[ResultRow]:
    """Read result means from an immutable SQLite connection."""
    resolved = db_path.resolve()
    connection = sqlite3.connect(f"file:{resolved}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    query = """
        SELECT
            p.id AS paper_id,
            COALESCE(p.arxiv_id, '') AS arxiv_id,
            p.title,
            d.id AS dataset_id,
            d.name AS dataset,
            COALESCE(d.task_type, '') AS task_type,
            COALESCE(d.primary_metric, '') AS primary_metric,
            r.metric_name AS metric,
            CASE
                WHEN r.is_overridden = 1 AND r.override_value IS NOT NULL
                THEN r.override_value
                ELSE r.metric_value
            END AS value,
            COALESCE(r.evaluation_task, '') AS evaluation_task,
            COALESCE(r.protocol_decision, '') AS protocol_decision
        FROM results r
        JOIN papers p ON p.id = r.paper_id
        JOIN dataset_variants dv ON dv.id = r.dataset_variant_id
        JOIN datasets d ON d.id = dv.dataset_id
        WHERE (:include_problematic = 1 OR COALESCE(r.is_problematic, 0) = 0)
    """
    try:
        records = connection.execute(
            query, {"include_problematic": int(include_problematic)}
        ).fetchall()
    finally:
        connection.close()

    rows: list[ResultRow] = []
    for record in records:
        value = _finite(record["value"])
        if value is None:
            continue
        rows.append(
            ResultRow(
                paper_id=int(record["paper_id"]),
                arxiv_id=str(record["arxiv_id"]),
                title=str(record["title"]),
                dataset_id=int(record["dataset_id"]),
                dataset=str(record["dataset"]),
                task_type=str(record["task_type"]),
                primary_metric=str(record["primary_metric"]),
                metric=str(record["metric"]),
                value=value,
                evaluation_task=str(record["evaluation_task"]),
                protocol_decision=str(record["protocol_decision"]),
            )
        )
    return rows


def aggregate_rows(rows: list[ResultRow], *, min_results: int = 3) -> list[Observation]:
    """Aggregate all extracted means for each paper, dataset, and metric."""
    grouped: dict[tuple[int, int, str], list[ResultRow]] = defaultdict(list)
    for row in rows:
        metric_key = row.metric.strip().casefold()
        grouped[(row.paper_id, row.dataset_id, metric_key)].append(row)

    observations: list[Observation] = []
    for group in grouped.values():
        if len(group) < min_results:
            continue
        first = group[0]
        values = np.asarray([row.value for row in group], dtype=float)
        evaluation_tasks = sorted({row.evaluation_task for row in group if row.evaluation_task})
        protocol_decisions = sorted(
            {row.protocol_decision for row in group if row.protocol_decision}
        )
        observations.append(
            Observation(
                paper_id=first.paper_id,
                arxiv_id=first.arxiv_id,
                title=first.title,
                dataset_id=first.dataset_id,
                dataset=first.dataset,
                task_type=first.task_type,
                primary_metric=first.primary_metric,
                metric=first.metric,
                result_count=len(group),
                value_mean=float(np.mean(values)),
                value_std=float(np.std(values, ddof=0)),
                evaluation_tasks=evaluation_tasks,
                protocol_decisions=protocol_decisions,
            )
        )
    return observations


def _robust_location_scale(values: np.ndarray) -> tuple[float, float]:
    center = float(np.median(values))
    mad = float(np.median(np.abs(values - center)))
    scale = 1.4826 * mad
    if scale <= 1e-12:
        q25, q75 = np.quantile(values, [0.25, 0.75])
        scale = float((q75 - q25) / 1.349)
    if scale <= 1e-12:
        scale = float(np.std(values))
    return center, scale


def _score_robust_statistics(observations: list[Observation], *, min_cohort_size: int) -> None:
    cohorts: dict[tuple[int, str], list[Observation]] = defaultdict(list)
    for observation in observations:
        cohorts[(observation.dataset_id, observation.metric.strip().casefold())].append(observation)

    for cohort in cohorts.values():
        for observation in cohort:
            observation.cohort_size = len(cohort)
        if len(cohort) < min_cohort_size:
            continue

        means = np.asarray([item.value_mean for item in cohort], dtype=float)
        spreads = np.asarray([item.value_std for item in cohort], dtype=float)
        mean_center, mean_scale = _robust_location_scale(means)
        std_center, std_scale = _robust_location_scale(spreads)
        for observation in cohort:
            mean_z = (observation.value_mean - mean_center) / mean_scale if mean_scale else 0.0
            std_z = (observation.value_std - std_center) / std_scale if std_scale else 0.0
            observation.mean_robust_z = float(mean_z)
            observation.std_robust_z = float(std_z)
            observation.robust_distance = float(math.hypot(mean_z, std_z))


def _signed_log1p(value: float) -> float:
    return math.copysign(math.log1p(abs(value)), value)


def _standardize_features(features: np.ndarray) -> np.ndarray:
    standardized = np.zeros_like(features, dtype=float)
    for column in range(features.shape[1]):
        values = features[:, column]
        center, scale = _robust_location_scale(values)
        if scale > 1e-12:
            standardized[:, column] = (values - center) / scale
    return standardized


def _score_clusters(
    observations: list[Observation], *, min_cohort_size: int, min_cluster_size: int
) -> None:
    """Cluster paper summaries within each comparable dataset/metric cohort."""
    cohorts: dict[tuple[int, str], list[Observation]] = defaultdict(list)
    for observation in observations:
        cohorts[(observation.dataset_id, observation.metric.strip().casefold())].append(observation)

    for cohort in cohorts.values():
        if len(cohort) < max(min_cohort_size, min_cluster_size * 2):
            continue
        features = np.asarray(
            [[_signed_log1p(item.value_mean), math.log1p(item.value_std)] for item in cohort],
            dtype=float,
        )
        features = _standardize_features(features)
        model = HDBSCAN(
            min_cluster_size=min_cluster_size,
            min_samples=max(2, min_cluster_size // 2),
            cluster_selection_method="eom",
            allow_single_cluster=True,
            copy=True,
        )
        labels = model.fit_predict(features)
        probabilities = model.probabilities_
        cluster_sizes = Counter(int(label) for label in labels if label >= 0)
        largest_cluster = max(cluster_sizes.values(), default=0)
        for observation, label, probability in zip(cohort, labels, probabilities, strict=True):
            observation.cluster_label = int(label)
            observation.cluster_probability = float(probability)
            observation.cluster_noise = bool(label == -1)
            observation.cluster_size = cluster_sizes.get(int(label), 0)
            if label >= 0:
                observation.cluster_fraction = observation.cluster_size / len(cohort)
                observation.minority_cluster = bool(
                    observation.cluster_size < largest_cluster / 2
                    and observation.cluster_fraction <= 0.2
                )


def score_observations(
    observations: list[Observation],
    *,
    min_cohort_size: int = 8,
    min_cluster_size: int = 5,
    robust_threshold: float = 4.5,
    include_cluster_only: bool = False,
) -> list[Observation]:
    """Attach statistical and clustering signals to observations."""
    _score_robust_statistics(observations, min_cohort_size=min_cohort_size)
    _score_clusters(
        observations,
        min_cohort_size=min_cohort_size,
        min_cluster_size=min_cluster_size,
    )
    for observation in observations:
        reasons: list[str] = []
        if (
            observation.robust_distance is not None
            and observation.robust_distance >= robust_threshold
        ):
            reasons.append("robust_statistical_outlier")
        if observation.cluster_noise:
            reasons.append("hdbscan_noise")
        elif observation.minority_cluster:
            reasons.append("hdbscan_minority_cluster")
        if "nonstandard" in observation.protocol_decisions:
            reasons.append("stored_nonstandard_protocol")
        observation.reasons = reasons
        statistical_or_protocol = bool(
            "robust_statistical_outlier" in reasons or "stored_nonstandard_protocol" in reasons
        )
        cluster_signal = bool("hdbscan_noise" in reasons or "hdbscan_minority_cluster" in reasons)
        observation.suspicious = statistical_or_protocol or (
            include_cluster_only and cluster_signal
        )
    return observations


def _observation_score(observation: Observation, robust_threshold: float) -> float:
    robust_score = (observation.robust_distance or 0.0) / robust_threshold
    cluster_score = 1.0 if observation.cluster_noise else 0.0
    protocol_score = 1.0 if "nonstandard" in observation.protocol_decisions else 0.0
    return max(robust_score, cluster_score, protocol_score)


def build_report(
    observations: list[Observation],
    *,
    robust_threshold: float,
    config: dict[str, Any],
) -> dict[str, Any]:
    """Aggregate suspicious dataset observations into a ranked paper report."""
    by_paper: dict[int, list[Observation]] = defaultdict(list)
    for observation in observations:
        if observation.suspicious:
            by_paper[observation.paper_id].append(observation)

    papers: list[dict[str, Any]] = []
    for paper_observations in by_paper.values():
        first = paper_observations[0]
        paper_score = max(_observation_score(item, robust_threshold) for item in paper_observations)
        details = []
        for observation in sorted(
            paper_observations,
            key=lambda item: _observation_score(item, robust_threshold),
            reverse=True,
        ):
            payload = asdict(observation)
            payload.pop("paper_id")
            payload.pop("title")
            payload.pop("arxiv_id")
            payload["score"] = round(_observation_score(observation, robust_threshold), 6)
            details.append(payload)
        papers.append(
            {
                "arxiv_id": first.arxiv_id,
                "title": first.title,
                "score": round(paper_score, 6),
                "suspicious_observation_count": len(paper_observations),
                "observations": details,
            }
        )
    papers.sort(key=lambda item: (-item["score"], item["arxiv_id"], item["title"]))

    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "config": config,
        "counts": {
            "observations_scored": len(observations),
            "suspicious_observations": sum(item.suspicious for item in observations),
            "suspicious_papers": len(papers),
            "clustering_candidates": sum(
                item.cluster_noise or item.minority_cluster for item in observations
            ),
        },
        "papers": papers,
    }


def run(
    db_path: Path,
    *,
    min_results: int = 3,
    min_cohort_size: int = 8,
    min_cluster_size: int = 5,
    robust_threshold: float = 4.5,
    include_problematic: bool = False,
    include_cluster_only: bool = False,
) -> dict[str, Any]:
    rows = _read_rows(db_path, include_problematic=include_problematic)
    observations = aggregate_rows(rows, min_results=min_results)
    score_observations(
        observations,
        min_cohort_size=min_cohort_size,
        min_cluster_size=min_cluster_size,
        robust_threshold=robust_threshold,
        include_cluster_only=include_cluster_only,
    )
    config = {
        "db_path": str(db_path),
        "min_results": min_results,
        "min_cohort_size": min_cohort_size,
        "min_cluster_size": min_cluster_size,
        "robust_threshold": robust_threshold,
        "include_problematic": include_problematic,
        "include_cluster_only": include_cluster_only,
    }
    return build_report(observations, robust_threshold=robust_threshold, config=config)


def write_json_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "arxiv_id",
        "title",
        "paper_score",
        "dataset",
        "task_type",
        "metric",
        "primary_metric",
        "result_count",
        "value_mean",
        "value_std",
        "cohort_size",
        "mean_robust_z",
        "std_robust_z",
        "robust_distance",
        "cluster_label",
        "cluster_size",
        "cluster_probability",
        "reasons",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for paper in report["papers"]:
            for observation in paper["observations"]:
                writer.writerow(
                    {
                        "arxiv_id": paper["arxiv_id"],
                        "title": paper["title"],
                        "paper_score": paper["score"],
                        **{key: observation.get(key) for key in columns[3:-1]},
                        "reasons": ";".join(observation.get("reasons") or []),
                    }
                )
