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


def test_evaluate_records_database_snapshot_drift() -> None:
    annotation = _annotation("2304.10074", 20, 1)
    result = evaluation.evaluate(
        [annotation],
        {"2304.10074": {}},
        {"2304.10074": 0},
    )

    assert result["summary"]["database_snapshot"] == {
        "drift_count": 1,
        "drifts": [
            {
                "arxiv_id": "2304.10074",
                "annotation_count": 20,
                "current_database_count": 0,
            }
        ],
    }
    assert result["papers"][0]["database_result_count_drift"] is True


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


def test_markdown_truth_reads_checked_and_missing_datasets(tmp_path) -> None:
    review = tmp_path / "manual_review.md"
    review.write_text(
        """## 2508.05070 — TANGO

### Datasets currently in the database

- [x] Cora — `Standard split` (1 row)
- [x] ZINC — `Standard split` (1 row)

**Missing datasets (add names):**

- Peptides-func/struct, Amazon-ratings

### Methods currently in the database
""",
        encoding="utf-8",
    )

    truth = evaluation.load_markdown_dataset_truth(review, "2508.05070")

    assert truth is not None
    assert truth.expected_datasets == ("Cora", "ZINC", "Peptides-func", "Peptides-struct", "Amazon-ratings")
    assert truth.table_refs_complete is False


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


def test_yaml_audit_distinguishes_detection_from_database_promotion() -> None:
    annotation = _annotation("1903.02428", 0, 1)
    yaml_evidence = {
        "1903.02428": {
            evaluation._catalog_key("Cora"): evaluation.YamlDataset(
                names={"Cora"},
                result_rows=6,
                table_refs={"Table 1"},
                protocols={"nonstandard"},
            )
        }
    }
    tracked_keys = {
        evaluation._catalog_key(name)
        for name in ("Cora", "CiteSeer", "PubMed", "MUTAG", "IMDB-BINARY", "REDDIT-BINARY")
    }

    result = evaluation.evaluate(
        [annotation],
        {},
        {"1903.02428": 0},
        tracked_keys,
        yaml_evidence,
    )

    audits = {item["dataset"]: item for item in result["papers"][0]["yaml_dataset_audit"]}
    assert audits["Cora"]["yaml_detected"] is True
    assert audits["Cora"]["database_promoted"] is False
    assert audits["Cora"]["yaml_result_rows"] == 6
    assert audits["CiteSeer"]["yaml_detected"] is False
    assert result["summary"]["yaml_discovery"] == {
        "tracked_manual_positive_pairs": 6,
        "tracked_manual_missing_pairs": 6,
        "tracked_manual_missing_detected_in_yaml": 1,
        "tracked_manual_missing_with_yaml_rows": 1,
        "tracked_manual_missing_manifest_only": 0,
        "tracked_manual_missing_absent_from_yaml": 5,
        "tracked_manual_positive_detected_in_yaml": 1,
        "tracked_manual_positive_absent_from_yaml": 5,
    }
    assert result["summary"]["raw_detection"] == {
        "definition": (
            "Tracked dataset name present in a raw YAML result row or discovered_datasets "
            "manifest; strict papers only; table/protocol/database promotion ignored."
        ),
        "true_positive": 1,
        "false_positive": 0,
        "false_negative": 5,
        "false_positive_on_manual_positive_papers": 0,
        "false_positive_on_manual_negative_papers": 0,
        "precision": 1.0,
        "recall": pytest.approx(1 / 6),
        "f1": pytest.approx(2 / 7),
        "manifest_only": {
            "true_positive": 0,
            "false_positive": 0,
            "false_negative": 6,
            "precision": None,
            "recall": 0.0,
            "f1": 0.0,
        },
    }


def test_load_yaml_dataset_evidence_collects_rows_and_notes(tmp_path) -> None:
    artifact = tmp_path / "1903.02428" / "extracted" / "llm_output.yaml"
    artifact.parent.mkdir(parents=True)
    artifact.write_text(
        """
results:
  results:
    - dataset: Cora
      table_ref: Table 1
      protocol_decision: nonstandard
    - dataset: Cora
      table_ref: Table 2
      protocol_decision: standard
  discovered_datasets:
    - name: ZINC-12k
      table_refs: [Table 2]
  extraction_notes: "[Cora] retained both protocol variants"
  coverage_assessment: uncertain
""",
        encoding="utf-8",
    )

    evidence = evaluation.load_yaml_dataset_evidence(tmp_path, ["1903.02428"])
    cora = evidence["1903.02428"][evaluation._catalog_key("Cora")]
    assert cora.names == {"Cora"}
    assert cora.result_rows == 2
    assert cora.table_refs == {"Table 1", "Table 2"}
    assert cora.protocols == {"nonstandard", "standard"}
    assert cora.extraction_note == "[Cora] retained both protocol variants"
    zinc = evidence["1903.02428"][evaluation._catalog_key("ZINC-12k")]
    assert zinc.names == {"ZINC-12k"}
    assert zinc.discovered_manifest is True
    assert zinc.result_rows == 0
    assert zinc.table_refs == {"Table 2"}
    assert zinc.coverage_assessment == "uncertain"
