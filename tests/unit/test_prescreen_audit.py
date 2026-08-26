from experiments.prescreen_validation.prescreen_audit import (
    AuditPaper,
    DatasetMatcher,
    DownstreamEvidence,
    _allocate_sample_size,
    classify_cohorts,
    select_review_cohort,
    summarize,
)


def _row(
    arxiv_id: str,
    decision: str,
    *,
    mentions: list[str] | None = None,
    exact_mentions: list[str] | None = None,
    screener_datasets: list[str] | None = None,
    artifact_results: int | None = None,
) -> AuditPaper:
    return AuditPaper(
        arxiv_id=arxiv_id,
        title="Title",
        abstract="Abstract",
        decision=decision,
        matched_tier="specific",
        confidence=0.8,
        reason="reason",
        screener_datasets=screener_datasets or [],
        abstract_dataset_mentions=mentions or [],
        abstract_exact_case_mentions=exact_mentions or [],
        full_text_available=False,
        full_text_dataset_mentions=[],
        downstream=DownstreamEvidence(artifact_result_count=artifact_results),
    )


def test_dataset_matcher_uses_boundaries_and_tracks_exact_case() -> None:
    matcher = DatasetMatcher(["Cora", "QM9", "Amazon-Photo"])

    found, exact = matcher.find("We evaluate cora, QM9, and Amazon-Photo; not coral reefs.")

    assert found == ["Amazon-Photo", "Cora", "QM9"]
    assert exact == ["Amazon-Photo", "QM9"]


def test_classification_separates_review_strata() -> None:
    rows = [
        _row("1", "rejected", exact_mentions=["Cora"]),
        _row("2", "rejected"),
        _row("3", "accepted", artifact_results=0),
        _row("4", "accepted", artifact_results=8),
    ]

    cohorts = classify_cohorts(rows)

    assert {name: [row.arxiv_id for row in values] for name, values in cohorts.items()} == {
        "rejected_suspicious": ["1"],
        "rejected_control": ["2"],
        "accepted_zero_artifact_results": ["3"],
        "accepted_positive_control": ["4"],
    }


def test_summary_keeps_raw_and_stored_zero_counts_separate() -> None:
    raw_zero = _row("1", "accepted", artifact_results=0)
    raw_zero.downstream = DownstreamEvidence(
        extraction_status="extracted", stored_result_count=4, artifact_result_count=0
    )
    stored_zero = _row("2", "accepted", artifact_results=9)
    stored_zero.downstream = DownstreamEvidence(
        extraction_status="quarantined_method_name",
        stored_result_count=0,
        artifact_result_count=9,
    )
    rejected = _row("3", "rejected", screener_datasets=["Cora"])
    rows = [raw_zero, stored_zero, rejected]

    summary = summarize(rows, classify_cohorts(rows))

    assert summary["accepted_downstream"]["zero_raw_artifact_results"] == 1
    assert summary["accepted_downstream"]["zero_stored_results"] == 1
    assert summary["rejected_evidence"]["prioritized_as_suspicious"] == 1


def test_default_allocation_is_three_two_three_two() -> None:
    assert _allocate_sample_size(10) == {
        "rejected_suspicious": 3,
        "rejected_control": 2,
        "accepted_zero_artifact_results": 3,
        "accepted_positive_control": 2,
    }


def test_review_cohort_prioritizes_downstream_contradiction() -> None:
    weak_rejection = _row("1", "rejected", exact_mentions=["Cora"])
    strong_rejection = _row("2", "rejected", artifact_results=4)
    rows = [
        weak_rejection,
        strong_rejection,
        _row("3", "rejected"),
        _row("4", "accepted", artifact_results=0),
        _row("5", "accepted", artifact_results=8),
    ]

    selected = select_review_cohort(classify_cohorts(rows), sample_size=4, seed=7)

    assert [row.arxiv_id for row in selected if row.cohort == "rejected_suspicious"] == ["2"]
