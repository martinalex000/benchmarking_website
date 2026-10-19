"""Read-only enforcement and competing-presentation checks for the held-out batch."""

import sqlite3
from types import SimpleNamespace

import pytest

from experiments.table_provenance_experiment import run_mapping_batch as batch


def test_source_first_keeps_fallible_metric_but_hides_old_numbers(tmp_path):
    import json

    (tmp_path / "protocol_keys.json").write_text("{}")
    row = {
        "result_id": 1,
        "model": "GCN",
        "dataset": "Deezer",
        "variant": "",
        "metric": "ROC-AUC",
        "value": 0.123456789,
        "std": 0.987654321,
    }
    content = batch.source_first_content(tmp_path, "Source", "test", [row])
    identities = json.loads(content.split("TARGET IDENTITIES", 1)[1].split("\n")[1])
    assert identities[0]["metric"] == "ROC-AUC"
    assert "value" not in identities[0]
    assert "std" not in identities[0]
    assert "fallible requested quantity" in content


def verdict(presentations):
    span = {"start_line": 1, "end_line": 1}
    protocol = {
        "design": "unknown",
        "training_repetitions": None,
        "cv_folds": None,
        "cv_repetitions": None,
        "dataset_splits": None,
        "repetitions_per_split": None,
        "reported_runs": None,
        "variability_scope": "unknown",
        "evidence": [],
        "scope_evidence": [],
        "explanation": "Unknown",
    }
    candidate = {
        "table_id": 1,
        "displayed_mean": 0.1581,
        "displayed_std": 0.0026,
        "divisor": 1,
        "method": "GCN-Virtual Node",
        "dataset": "OGBG-CODE2",
        "metric": "F1",
        "configuration": "same",
        "eligibility": "benchmark",
        "main_experiment": True,
        "row_evidence": span,
        "column_evidence": span,
        "cell_evidence": span,
        "protocol": protocol,
    }
    fact = {
        "result_id": 1,
        "candidates": [candidate],
        "origin": "copied",
        "origin_evidence": [span],
        "execution_evidence": [],
        "repair": None,
        "explanation": "Copied",
    }
    return batch.BatchVerdict.model_validate(
        {
            "result_id": 1,
            "corrected_fact": fact,
            "verified_candidate_indices": [0],
            "origin_supported": True,
            "execution_supported": False,
            "protocol_supported": False,
            "repair_supported": False,
            "setting_status": "supported",
            "eligibility": "benchmark",
            "explanation": "Checked",
            "presentations": presentations,
        }
    )


def review(table_id, decision="same_experiment"):
    return {
        "table_id": table_id,
        "decision": decision,
        "evidence": [{"start_line": 1, "end_line": 1}],
        "explanation": "Checked",
    }


def test_competing_screen_finds_other_value_not_only_stored_number():
    source = (
        "\\begin{table}\nMethod & OGBG-CODE2 \\\\\n"
        "GCN-Virtual Node & 0.1595 $\\pm$ 0.0018 \\\\\n\\end{table}\n"
        "\\appendix\n\\begin{table}\nMethod & OGBG-CODE2 \\\\\n"
        "GCN-Virtual Node & 0.1581 $\\pm$ 0.0026 \\\\\n\\end{table}\n"
    )
    row = {"model": "GCN-Virtual Node", "dataset": "OGBG-CODE2"}
    assert batch.competing_tables(row, source) == [1, 2]


def test_competing_review_cannot_drop_main_presentation():
    output = verdict([review(1)])
    assert "competing_presentations_unreviewed" in batch.coverage_flags(output, [1, 2], "source")
    output = verdict([review(1), review(2)])
    assert "same_experiment_candidate_omitted" in batch.coverage_flags(output, [1, 2], "source")


def test_other_configurations_do_not_force_an_unrelated_numeric_repair():
    output = verdict([review(1), review(2, "different_configuration")])
    assert batch.coverage_flags(output, [1, 2], "source") == []


def test_ungrounded_or_duplicate_reviews_are_not_coverage_proof():
    output = verdict([review(1), review(1)])
    assert "duplicate_presentation_review" in batch.coverage_flags(output, [1], "source")
    output.presentations[0].evidence[0].end_line = 99
    assert "presentation_evidence_missing" in batch.coverage_flags(output, [1], "source")


def test_prior_ablation_exclusion_is_local_to_actual_selected_table():
    result = {"model": "Own", "selected_candidate": {"table_id": 1, "method": "Own"}}
    keys = [
        {
            "table_id": 2,
            "method": {"name": "Own"},
            "previous_verdict": {
                "benchmark_supported": False,
                "explanation": "This is an ablation variant",
            },
        }
    ]
    assert not batch.prior_ablation_excluded(result, keys)
    result["selected_candidate"]["table_id"] = 2
    assert batch.prior_ablation_excluded(result, keys)


def test_database_connection_refuses_writes(tmp_path, monkeypatch):
    path = tmp_path / "fixture.db"
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE sample (value INTEGER)")
    monkeypatch.setattr(batch, "cfg", SimpleNamespace(db_path=path))
    with batch.readonly() as db:
        with pytest.raises(sqlite3.OperationalError):
            db.execute("INSERT INTO sample VALUES (1)")
        assert db.execute("SELECT count(*) FROM sample").fetchone()[0] == 0


def test_explicit_daytime_override_is_experiment_only():
    from datetime import datetime
    from zoneinfo import ZoneInfo

    gate = batch.ExperimentGate(maximum=20, daytime_streams=2)
    gate.now = lambda: datetime(2026, 10, 7, 12, tzinfo=ZoneInfo("Europe/Berlin"))
    assert gate.limit == 2
    gate.now = lambda: datetime(2026, 10, 7, 23, tzinfo=ZoneInfo("Europe/Berlin"))
    assert gate.limit == 4
    assert batch.ExperimentGate(maximum=20).daytime_streams == 1


def test_invalid_cell_anchor_triggers_targeted_feedback():
    output = verdict([review(1)])
    errors = batch.grounding_errors(batch.BatchVerdicts(verdicts=[output]), "Protocol prose")
    assert len(errors) == 1
    assert "cell_evidence" in errors[0]


def test_comment_tables_are_not_competing_published_presentations():
    source = "\\begin{table}\nMethod & Cora \\\\\nOwn & 0.8 \\\\\n\\end{table}\n% \\begin{table}\n% Method & Cora \\\\\n% Own & 0.9 \\\\\n% \\end{table}"
    row = {"model": "Own", "dataset": "Cora"}
    assert batch.competing_tables(row, source) == [1, 2]
    assert batch.competing_tables(row, source, ignore_comments=True) == [1]
    assert batch.active_source_lines(r"Accuracy (\%) & 80 % discarded")[0] == r"Accuracy (\%) & 80 "
