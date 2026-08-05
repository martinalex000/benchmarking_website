import pytest

from backend.paper_task_anomaly import (
    ResultRow,
    aggregate_rows,
    build_report,
    score_observations,
    write_json_report,
)


def _row(
    paper_id: int,
    value: float,
    *,
    dataset_id: int = 1,
    metric: str = "Accuracy",
) -> ResultRow:
    return ResultRow(
        paper_id=paper_id,
        arxiv_id=f"paper-{paper_id}",
        title=f"Paper {paper_id}",
        dataset_id=dataset_id,
        dataset="Cora",
        task_type="node_classification",
        primary_metric="Accuracy",
        metric=metric,
        value=value,
        evaluation_task="node_classification",
        protocol_decision="standard",
    )


def test_aggregate_rows_uses_every_result_mean_per_paper_dataset_metric() -> None:
    rows = [_row(1, 0.7), _row(1, 0.8), _row(1, 0.9), _row(1, 0.5, metric="F1")]

    observations = aggregate_rows(rows, min_results=2)

    assert len(observations) == 1
    observation = observations[0]
    assert observation.result_count == 3
    assert observation.value_mean == pytest.approx(0.8)
    assert round(observation.value_std, 6) == round(0.08164965809277262, 6)


def test_robust_statistics_flag_a_shifted_paper() -> None:
    rows = []
    for paper_id in range(1, 13):
        center = 0.8 + paper_id * 0.001
        rows.extend(_row(paper_id, center + offset) for offset in (-0.01, 0.0, 0.01))
    rows.extend(_row(99, value) for value in (0.10, 0.11, 0.12))
    observations = aggregate_rows(rows)

    score_observations(
        observations,
        min_cohort_size=8,
        min_cluster_size=3,
        robust_threshold=4.5,
    )

    outlier = next(item for item in observations if item.paper_id == 99)
    assert outlier.suspicious
    assert "robust_statistical_outlier" in outlier.reasons


def test_hdbscan_preserves_large_and_small_dense_clusters() -> None:
    rows = []
    for paper_id in range(1, 31):
        center = 0.80 + (paper_id % 5) * 0.001
        rows.extend(_row(paper_id, center + offset) for offset in (-0.002, 0.0, 0.002))
    for paper_id in range(31, 38):
        center = 0.20 + (paper_id % 3) * 0.001
        rows.extend(_row(paper_id, center + offset) for offset in (-0.001, 0.0, 0.001))
    observations = aggregate_rows(rows)

    score_observations(
        observations,
        min_cohort_size=8,
        min_cluster_size=5,
        robust_threshold=100.0,
    )

    large_labels = {item.cluster_label for item in observations if item.paper_id <= 30}
    small_labels = {item.cluster_label for item in observations if 31 <= item.paper_id <= 37}
    assert len(small_labels) == 1
    assert -1 not in large_labels | small_labels
    assert large_labels.isdisjoint(small_labels)


def test_report_ranks_papers_by_their_most_suspicious_dataset() -> None:
    observations = aggregate_rows(
        [
            *[_row(1, value) for value in (0.7, 0.8, 0.9)],
            *[_row(2, value) for value in (0.1, 0.2, 0.3)],
        ]
    )
    observations[0].suspicious = True
    observations[0].reasons = ["robust_statistical_outlier"]
    observations[0].robust_distance = 5.0
    observations[1].suspicious = True
    observations[1].reasons = ["robust_statistical_outlier"]
    observations[1].robust_distance = 9.0

    report = build_report(observations, robust_threshold=4.5, config={})

    assert [paper["arxiv_id"] for paper in report["papers"]] == ["paper-2", "paper-1"]


def test_cluster_report_is_json_serializable(tmp_path) -> None:
    rows = []
    for paper_id in range(1, 13):
        rows.extend(_row(paper_id, 0.7 + paper_id * 0.01 + offset) for offset in (0, 0.01, 0.02))
    observations = aggregate_rows(rows)
    score_observations(observations, min_cohort_size=8, min_cluster_size=3)
    report = build_report(observations, robust_threshold=4.5, config={})

    output = tmp_path / "report.json"
    write_json_report(output, report)

    assert output.read_text(encoding="utf-8").startswith("{")
