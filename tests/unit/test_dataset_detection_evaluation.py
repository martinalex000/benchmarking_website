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
    assert "Confirmed LLM false positive" in report
    assert "different Amazon dataset version" in report
    assert "- **Dataset-specific manual findings:**" in report
    assert "  - **Amazon2M:**" in report
    assert "Absolute counts: TP 1, FP 1, TN 0, FN 0" in report
    assert "precision fraction 1/2, recall fraction 1/1" in report


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
    assert evaluation._catalog_key("ZINC-12k") == evaluation._catalog_key("ZINC")


def test_follow_up_adjudications_enter_strict_metrics() -> None:
    annotations = [
        _annotation("1710.03059", 4, 1),
        _annotation("1905.12560", 4, 2),
        _annotation("2403.07954", 3, 3),
    ]
    database_evidence = {
        "1710.03059": {
            evaluation._name_key(name): _stored(name, "Table 1")
            for name in ("CiteSeer", "Cora", "PPI", "PubMed")
        },
        "1905.12560": {
            evaluation._name_key(name): _stored(name, "Table 1")
            for name in ("COLLAB", "CSL", "MUTAG", "PROTEINS")
        },
        "2403.07954": {
            evaluation._name_key(name): _stored(name, "Table 1")
            for name in ("Actor", "Penn94", "Squirrel")
        },
    }

    result = evaluation.evaluate(
        annotations,
        database_evidence,
        {"1710.03059": 4, "1905.12560": 4, "2403.07954": 3},
        {
            evaluation._catalog_key(name)
            for name in (
                "Actor",
                "Chameleon",
                "CiteSeer",
                "COLLAB",
                "Cora",
                "CSL",
                "IMDB-BINARY",
                "IMDB-MULTI",
                "MUTAG",
                "ogbn-arxiv",
                "Penn94",
                "PPI",
                "PROTEINS",
                "PubMed",
                "Squirrel",
            )
        },
    )

    summary = result["summary"]
    assert summary["strict_paper_count"] == 3
    assert summary["qualified_paper_count"] == 0
    assert summary["paper_level"]["true_positive"] == 3
    assert summary["dataset_level"]["true_positive"] == 11
    assert summary["dataset_level"]["false_negative"] == 7
    assert summary["dataset_level"]["false_positive"] == 0
    assert summary["table_reference_level"]["false_negative"] == 8
    assert summary["table_reference_level"]["false_positive"] == 3
    assert summary["manual_adjudication"] == {
        "confirmed_dataset_false_negatives": 7,
        "confirmed_dataset_false_positives": 0,
        "confirmed_table_false_negatives": 8,
        "confirmed_table_false_positives": 3,
        "unresolved_dataset_discrepancies": 0,
        "unresolved_table_discrepancies": 0,
    }
    assert summary["tracking_scope"]["strict_manual_dataset_pairs_excluded"] == 4
