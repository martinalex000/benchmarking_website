import pytest

from experiments.extraction_validation.dataset_detection import evaluate_review as evaluation


def _annotation(arxiv_id: str, result_count: int, paper_index: int) -> dict[str, str]:
    return {
        "paper_index": str(paper_index),
        "arxiv_id": arxiv_id,
        "cohort": "with_database_results" if result_count else "zero_database_results",
        "title": arxiv_id,
        "database_result_count": str(result_count),
        "manual_experiment_compatible": "",
        "manual_compatibility_reason": "",
        "manual_notes": "",
    }


def _stored(name: str, table_ref: str) -> evaluation.DatabaseDataset:
    return evaluation.DatabaseDataset(
        name=name,
        table_refs={table_ref},
        result_rows=1,
        protocols={"standard"},
    )


def test_evaluate_separates_qualified_papers_from_strict_metrics() -> None:
    annotations = [
        _annotation("2304.10074", 20, 1),
        _annotation("2401.14155", 4, 2),
        _annotation("2010.05788", 0, 3),
    ]
    database_evidence = {
        "2304.10074": {
            evaluation._name_key("ogbl-collab"): _stored("ogbl-collab", "Table 2"),
            evaluation._name_key("ogbl-ddi"): _stored("ogbl-ddi", "Table 1"),
            evaluation._name_key("ogbl-citation2"): _stored("ogbl-citation2", "Table 1"),
            evaluation._name_key("ogbl-ppa"): _stored("ogbl-ppa", "Table 1"),
        },
        "2401.14155": {evaluation._name_key("Amazon2M"): _stored("Amazon2M", "Table 2")},
    }

    result = evaluation.evaluate(
        annotations,
        database_evidence,
        {"2304.10074": 20, "2401.14155": 4, "2010.05788": 0},
    )

    assert result["summary"]["strict_paper_count"] == 2
    assert result["summary"]["qualified_paper_count"] == 1
    assert result["summary"]["paper_level"]["true_positive"] == 1
    assert result["summary"]["paper_level"]["false_positive"] == 1
    assert result["summary"]["dataset_level"]["true_positive"] == 4
    assert result["summary"]["dataset_level"]["false_positive"] == 1
    assert result["summary"]["table_reference_level"]["true_positive"] == 4


def test_normalization_and_wilson_interval() -> None:
    assert evaluation._name_key("Peptides-func") == "peptidesfunc"
    assert evaluation._table_key("Table 04") == "table04"
    interval = evaluation._wilson(15, 16)
    assert interval is not None
    assert interval[0] == pytest.approx(0.7168, abs=0.0001)
    assert interval[1] == pytest.approx(0.9889, abs=0.0001)


def test_report_names_llm_as_evaluated_system() -> None:
    annotations = [
        _annotation("2304.10074", 20, 1),
        _annotation("2401.14155", 4, 2),
    ]
    database_evidence = {
        "2304.10074": {evaluation._name_key("ogbl-collab"): _stored("ogbl-collab", "Table 2")},
        "2401.14155": {evaluation._name_key("Amazon2M"): _stored("Amazon2M", "Table 2")},
    }
    result = evaluation.evaluate(
        annotations,
        database_evidence,
        {"2304.10074": 20, "2401.14155": 4},
    )

    report = evaluation.render_report(result, "test-hash")

    assert "System being evaluated:** the LLM-derived extraction" in report
    assert "precision and recall below measure the LLM/database output, not the human" in report
    assert "Candidate LLM false negative" in report
    assert "Candidate LLM false positive" in report


def test_perfect_match_message_precedes_itemization() -> None:
    annotation = _annotation("2304.10074", 4, 1)
    database_evidence = {
        "2304.10074": {
            evaluation._name_key("ogbl-collab"): _stored("ogbl-collab", "Table 2"),
            evaluation._name_key("ogbl-ddi"): _stored("ogbl-ddi", "Table 1"),
            evaluation._name_key("ogbl-citation2"): _stored("ogbl-citation2", "Table 1"),
            evaluation._name_key("ogbl-ppa"): _stored("ogbl-ppa", "Table 1"),
        }
    }
    result = evaluation.evaluate([annotation], database_evidence, {"2304.10074": 4})

    report = evaluation.render_report(result, "test-hash")
    heading_position = report.index("### 2304.10074")
    perfect_position = report.index("**Perfect manual–LLM match:**", heading_position)
    itemization_position = report.index("- **Manual reference status:**", heading_position)

    assert heading_position < perfect_position < itemization_position


def test_dataset_names_use_consistent_natural_order() -> None:
    assert evaluation._sorted_names(["ZINC-12k", "cora", "ZINC-2k", "CiteSeer"]) == [
        "CiteSeer",
        "cora",
        "ZINC-2k",
        "ZINC-12k",
    ]
