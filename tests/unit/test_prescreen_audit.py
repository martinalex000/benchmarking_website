from experiments.prescreen_validation.prescreen_audit import (
    AuditPaper,
    DatasetMatcher,
    DownstreamEvidence,
    classify_cohorts,
    extend_review_csv,
    extend_review_markdown,
    load_existing_review_rows,
    render_review,
    review_category,
    select_review_additions,
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
    matched_tier: str = "specific",
) -> AuditPaper:
    return AuditPaper(
        arxiv_id=arxiv_id,
        title="Title",
        abstract="Abstract",
        decision=decision,
        matched_tier=matched_tier,
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


def test_review_additions_only_fill_missing_category_targets() -> None:
    rows = [
        _row("specific-old", "rejected"),
        _row("specific-new", "rejected"),
        _row("graph-old", "rejected", matched_tier="graph"),
        _row("graph-new", "rejected", matched_tier="graph"),
        _row("zero-old", "accepted", artifact_results=0),
        _row("zero-new", "accepted", artifact_results=0),
        _row("positive-control", "accepted", artifact_results=8),
    ]
    existing_ids = {"specific-old", "graph-old", "zero-old", "positive-control"}

    additions = select_review_additions(
        rows,
        existing_ids,
        {
            "rejected_specific": 2,
            "rejected_graph": 2,
            "accepted_zero_artifact_results": 2,
        },
        seed=7,
    )

    assert {row.arxiv_id for row in additions} == {
        "specific-new",
        "graph-new",
        "zero-new",
    }
    assert {review_category(row) for row in additions} == {
        "rejected_specific",
        "rejected_graph",
        "accepted_zero_artifact_results",
    }


def test_review_csv_extension_preserves_manual_fields(tmp_path) -> None:
    path = tmp_path / "review.csv"
    path.write_text(
        "arxiv_id,cohort,manual_should_pass,manual_notes\nold,rejected_specific,1,keep this note\n",
        encoding="utf-8",
    )
    addition = _row("new", "rejected")
    addition.cohort = "rejected_specific"

    extend_review_csv(path, [addition])
    rows, _ = load_existing_review_rows(path)

    assert [row["arxiv_id"] for row in rows] == ["old", "new"]
    assert rows[0]["manual_should_pass"] == "1"
    assert rows[0]["manual_notes"] == "keep this note"
    assert rows[1]["manual_should_pass"] == ""


def test_review_markdown_extension_preserves_existing_text(tmp_path) -> None:
    path = tmp_path / "manual_review.md"
    old = _row("old", "rejected")
    old.cohort = "rejected_specific"
    original = render_review([old], seed=1).replace(
        "### Evidence revealed after manual judgment",
        "MY MANUAL NOTE\n\n### Evidence revealed after manual judgment",
    )
    path.write_text(original, encoding="utf-8")
    addition = _row("new", "accepted", artifact_results=0)
    addition.cohort = "accepted_zero_artifact_results"

    extend_review_markdown(path, [addition], seed=1)
    extended = path.read_text(encoding="utf-8")

    assert "MY MANUAL NOTE" in extended
    assert extended.index("## 1. arXiv:old") < extended.index("## 2. arXiv:new")
    assert extended.index("## 2. arXiv:new") < extended.index(
        "## Optional rejected-paper downstream check"
    )
