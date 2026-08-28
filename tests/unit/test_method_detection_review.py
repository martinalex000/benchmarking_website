from pathlib import Path

from experiments.extraction_validation.method_detection import prepare_review as review


def _paper(index: int = 1) -> review.ReviewPaper:
    return review.ReviewPaper(
        index=index,
        arxiv_id="1234.56789",
        cohort="with_database_results",
        title="Example paper",
        source_pdf=Path("paper.pdf"),
    )


def _evidence(name: str = "GCN") -> review.MethodEvidence:
    return review.MethodEvidence(
        name=name,
        raw_names=(name,),
        datasets=("Cora",),
        table_refs=("Table 2",),
        dataset_table_pairs=("Cora @ Table 2",),
        result_count=3,
        role="baseline",
        problematic_count=0,
    )


def test_build_review_rows_puts_summary_before_sorted_methods() -> None:
    paper = _paper()
    rows = review.build_review_rows(
        [paper],
        {paper.arxiv_id: [_evidence("GraphSAGE"), _evidence("GCN")]},
        {paper.arxiv_id: 6},
    )

    assert rows[0]["row_type"] == "paper_summary"
    assert rows[0]["database_method_count"] == "2"
    assert [row["database_method"] for row in rows[1:]] == ["GCN", "GraphSAGE"]
    assert rows[1]["manual_decision"] == ""


def test_markdown_exposes_fast_review_fields_and_evidence() -> None:
    paper = _paper()

    markdown = review.render_review_markdown(
        [paper], {paper.arxiv_id: [_evidence()]}, {paper.arxiv_id: 3}
    )

    assert "manual_decision" in markdown
    assert "manual_missing_methods" in markdown
    assert "[1234.56789.pdf](pdfs/with_database_results/1234.56789.pdf)" in markdown
    assert "**GCN** — 3 rows; baseline; Cora @ Table 2" in markdown


def test_method_role_reports_mixed_rows() -> None:
    assert review._method_role(4, 4) == "baseline"
    assert review._method_role(4, 0) == "non-baseline"
    assert review._method_role(4, 2) == "mixed"
