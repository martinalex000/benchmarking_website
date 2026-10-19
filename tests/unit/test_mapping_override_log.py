import json

from experiments.table_provenance_experiment.mapping_override_log import (
    override_counts,
    write_override_log,
)


def test_repairs_count_changed_fields_and_unique_rows():
    old = {"value": 0.5, "std": 0.1, "metric": "Accuracy", "model": "GCN", "variant": ""}
    result = override_counts(
        [
            {
                "result_id": 1,
                "action": "propose_count",
                "num_runs": None,
                "proposed_num_runs": 5,
                "correction": {
                    "old": old,
                    "corrected": {**old, "std": 0.001, "metric": "F1", "model": "GAT"},
                },
            },
            {
                "result_id": 2,
                "action": "origin_unresolved",
                "correction": None,
                "withheld_repair": {"old": old, "corrected": {**old, "value": 0.9}},
            },
            {
                "result_id": 3,
                "action": "propose_count",
                "num_runs": 5,
                "proposed_num_runs": 5,
                "correction": None,
            },
        ]
    )
    assert result["rows_with_proposed_changes"] == 1
    assert result["rows_with_field_repairs"] == 1
    assert result["types"]["std"] == 1
    assert result["types"]["metric"] == 1
    assert result["types"]["method"] == 1
    assert result["types"]["num_runs"] == 1
    assert result["types"]["mean"] == 0
    assert result["decisions"]["origin_unresolved"] == 1


def test_dispositions_are_separate_from_repairs():
    result = override_counts(
        [
            {"result_id": 1, "action": "copied_excluded"},
            {"result_id": 2, "action": "propose_quarantine", "reason": "verifier_excluded"},
            {"result_id": 3, "action": "call_failed"},
        ]
    )
    assert result["rows_with_proposed_changes"] == 2
    assert result["rows_with_field_repairs"] == 0
    assert result["types"]["copied_exclusion"] == 1
    assert result["types"]["quarantine"] == 1
    assert result["quarantine_reasons"] == {"verifier_excluded": 1}


def test_log_is_counts_only_and_includes_pending_papers(tmp_path):
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {
                "papers": [
                    {"paper_id": "one", "title": "First paper"},
                    {"paper_id": "two", "title": "Pending paper"},
                ]
            }
        )
    )
    folder = tmp_path / "papers" / "one"
    folder.mkdir(parents=True)
    (folder / "assessment.json").write_text('{"state": "complete"}')
    (folder / "proposals.json").write_text(
        json.dumps(
            [
                {
                    "result_id": 987654321,
                    "action": "propose_count",
                    "num_runs": None,
                    "proposed_num_runs": 42,
                    "value": 0.123456789,
                },
            ]
        )
    )
    first = write_override_log(tmp_path).read_text()
    assert "First paper" in first and "Pending paper" in first
    assert "state=pending" in first
    assert "num_runs=1" in first
    assert "987654321" not in first and "0.123456789" not in first
    assert first == write_override_log(tmp_path).read_text()


def test_batch_analysis_automatically_writes_override_log(tmp_path):
    from experiments.table_provenance_experiment.run_mapping_batch import analyze

    (tmp_path / "manifest.json").write_text(
        json.dumps({"papers": [{"paper_id": "one", "title": "First paper", "rows": 1}]})
    )
    folder = tmp_path / "papers" / "one"
    folder.mkdir(parents=True)
    (folder / "assessment.json").write_text(
        json.dumps(
            {
                "state": "complete",
                "actions": {"origin_unresolved": 1},
                "repair_proposals": 0,
            }
        )
    )
    (folder / "proposals.json").write_text(
        json.dumps(
            [
                {
                    "result_id": 1,
                    "model": "GCN",
                    "dataset": "ZINC",
                    "variant": "",
                    "value": 0.1,
                    "std": 0.01,
                    "action": "origin_unresolved",
                    "proposed_num_runs": None,
                    "correction": None,
                }
            ]
        )
    )
    analyze(tmp_path)
    assert "origin_unresolved=1" in (tmp_path / "override_counts.log").read_text()
    assert "override_counts.log" in (tmp_path / "summary.md").read_text()
