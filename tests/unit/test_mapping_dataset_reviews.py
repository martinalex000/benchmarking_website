import hashlib
import json

import pytest

from backend.mapping.datasets import (
    load_reviews,
    project_row,
    restore_row,
    row_digest,
    validated_projection,
)
from backend.mapping.source import method_key, printed_matches, printed_numbers


def fixtures(tmp_path):
    source = "Dataset Amazon is used for the benchmark."
    row = {
        "result_id": 11,
        "model": "GraphTOP",
        "dataset": "Amazon2M",
        "variant": "standard",
        "metric": "Accuracy",
        "value": 0.5,
        "std": 0.01,
        "table_ref": None,
        "source_ref": None,
        "evaluation_task": "node classification",
        "protocol_decision": None,
        "protocol_note": None,
        "num_runs": None,
    }
    review = {
        "result_id": 11,
        "reviewer": "human_user",
        "authorization": "Correct this row to Amazon-ratings",
        "old_dataset": row["dataset"],
        "corrected_dataset": "Amazon-ratings",
        "corrected_dataset_id": 75,
        "source_dataset": "Amazon",
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "old_row_sha256": row_digest(row),
        "evidence": [{"start_line": 1, "end_line": 1}],
    }
    folder = tmp_path / "paper"
    folder.mkdir()
    review_path = folder / "reviewed_datasets.json"
    review_path.write_text(json.dumps([review]))
    manifest_paper = {
        "input_sha256": {
            "reviewed_datasets.json": hashlib.sha256(review_path.read_bytes()).hexdigest()
        }
    }
    candidate = {"dataset": "Amazon", "table_id": 1}
    return source, row, review, folder, manifest_paper, candidate


def test_review_projects_source_identity_and_restores_original_snapshot(tmp_path):
    source, row, review, folder, manifest_paper, candidate = fixtures(tmp_path)
    records = load_reviews(folder, manifest_paper)

    assert project_row(row, source, records)["dataset"] == "Amazon"
    proposal = restore_row(
        {**row, "action": "propose_count", "selected_candidate": candidate},
        row,
        source,
        records,
    )
    assert proposal["dataset"] == "Amazon2M"
    assert proposal["dataset_identity_review"] == review
    assert validated_projection(proposal, source, records)["dataset"] == "Amazon"


def test_dataset_review_rejects_stale_rows_and_modified_file(tmp_path):
    source, row, review, folder, manifest_paper, _ = fixtures(tmp_path)
    altered_row = {**row, "value": 0.6}
    with pytest.raises(ValueError, match="Stale, unbound or unauthorized"):
        project_row(altered_row, source, [review])

    (folder / "reviewed_datasets.json").write_text("[]")
    with pytest.raises(ValueError, match="authorization changed"):
        load_reviews(folder, manifest_paper)


def test_restore_with_wrong_source_candidate_abstains(tmp_path):
    source, row, review, _, _, _ = fixtures(tmp_path)
    proposal = restore_row(
        {
            **row,
            "action": "propose_count",
            "proposed_num_runs": 5,
            "selected_candidate": {"dataset": "Amazon2M"},
        },
        row,
        source,
        [review],
    )

    assert proposal["action"] == "dataset_identity_unresolved"
    assert proposal["proposed_num_runs"] is None
    assert "dataset_identity_review" not in proposal


def test_source_numeric_guard_handles_latex_subscripts_and_format_arguments():
    cell = r"$\bf{25.50_{\pm 4.11}}$"
    assert printed_numbers(cell) == ["25.50", "4.11"]
    assert printed_matches(25.5, 0.255, 100, cell)
    assert printed_matches(4.11, 0.0411, 100, cell)
    assert printed_numbers(r"\color[HTML]{000000} 25.50") == ["25.50"]


def test_method_identity_normalization_preserves_modifiers():
    assert method_key("GCN+") != method_key("GCN")
    assert method_key("GCN*") != method_key("GCN")
