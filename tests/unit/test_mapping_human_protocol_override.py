import hashlib
from pathlib import Path
from types import SimpleNamespace

from backend.mapping import decisions, worker
from backend.mapping.binding import apply_human_protocol_review, check_binding
from backend.mapping.repair_feedback import configuration_axis_repair_errors
from backend.mapping.safety import safe_assignment


def protocol():
    return {
        "design": "repeated_cv",
        "training_repetitions": None,
        "cv_folds": 10,
        "cv_repetitions": 10,
        "dataset_splits": None,
        "repetitions_per_split": None,
        "reported_runs": 10,
        "variability_scope": "cv_runs",
        "evidence": [{"start_line": 1, "end_line": 1}, {"start_line": 2, "end_line": 2}],
        "scope_evidence": [{"start_line": 1, "end_line": 2}],
        "explanation": "Ten complete 10-fold cross-validation repetitions.",
        "cv_repeat_unit": "full_cv",
    }


def test_model_repair_must_preserve_an_optimizer_stored_in_model_name():
    row = {"model": "Muon", "variant": "Standard split"}
    candidate = {
        "configuration_axes": {
            "backbone": "GotenNet",
            "optimizer": "Muon",
            "split": "Standard split",
        }
    }
    dropped = {"corrected": {"model": "GotenNet", "variant": "Standard split"}}
    preserved = {"corrected": {"model": "GotenNet", "variant": "Standard split, Muon optimizer"}}

    assert "optimizer=Muon" in configuration_axis_repair_errors(row, candidate, dropped)[0]
    assert configuration_axis_repair_errors(row, candidate, preserved) == []

    proposal = {
        **row,
        "action": "propose_count",
        "proposed_num_runs": 100,
        "selected_candidate": {
            **candidate,
            "table_id": 1,
            "method": "GotenNet",
            "protocol": protocol(),
        },
        "verdict": {"corrected_fact": {"origin": "self_evaluated"}},
        "correction": {
            "old": {
                "value": 0.1,
                "std": 0.01,
                "model": "Muon",
                "variant": "Standard split",
            },
            "corrected": {
                "value": 0.1,
                "std": 0.01,
                "model": "GotenNet",
                "variant": "Standard split",
            },
        },
    }
    safe = safe_assignment(proposal, [], "", [])
    assert safe["action"] == "configuration_scope_unresolved"
    assert safe["proposed_num_runs"] is None


def test_optimizer_header_cannot_be_mistaken_for_the_source_model():
    row = {
        "result_id": 2,
        "model": "Muon",
        "variant": "Standard split",
        "action": "propose_count",
        "proposed_num_runs": 4,
        "selected_candidate": {
            "table_id": 2,
            "method": "Muon",
            "configuration_axes": {
                "backbone": "GotenNet",
                "optimizer": "Muon",
                "split": "Standard split",
            },
        },
        "verdict": {"corrected_fact": {"origin": "self_evaluated"}},
        "correction": None,
    }

    errors = configuration_axis_repair_errors(row, row["selected_candidate"], None)
    assert errors and "method 'Muon'" in errors[0] and "backbone 'GotenNet'" in errors[0]

    safe = safe_assignment(row, [], "", [])
    assert safe["action"] == "configuration_scope_unresolved"
    assert safe["proposed_num_runs"] is None


def test_pooling_method_is_not_mistaken_for_its_backbone():
    row = {"model": "DiffPool", "variant": "10-fold CV"}
    candidate = {
        "method": "DiffPool",
        "configuration_axes": {"backbone": "GCN", "pooling": "DiffPool"},
    }

    assert configuration_axis_repair_errors(row, candidate, None) == []


def test_copied_row_with_wrong_configuration_identity_is_withheld():
    row = {
        "result_id": 3,
        "model": "GRAND-GAT",
        "variant": "Standard split",
        "value": 0.7067,
        "std": 0.0128,
        "action": "copied_excluded",
        "selected_candidate": {
            "table_id": 2,
            "method": "GRAND",
            "configuration_axes": {"diffusion": "GRAND-GAT"},
        },
        "correction": {
            "old": {
                "value": 0.7067,
                "std": 0.0128,
                "model": "GRAND-GAT",
                "variant": "Standard split",
            },
            "corrected": {
                "value": 0.7067,
                "std": 0.0128,
                "model": "GRAND",
                "variant": "Standard split",
            },
        },
        "verdict": {
            "corrected_fact": {
                "origin": "copied",
                "origin_evidence": [{"start_line": 1, "end_line": 1}],
            }
        },
    }
    hints = [
        {
            "result_id": 3,
            "matches": [{"model": "GRAND-GAT", "value": 0.7067, "std": 0.0128}],
        }
    ]

    safe = safe_assignment(row, [], "Results are taken from earlier work.", hints)

    assert safe["action"] == "configuration_scope_unresolved"
    assert safe.get("correction") is None
    assert safe["withheld_configuration_axis_repair"] == row["correction"]


def test_user_review_resolves_only_the_verified_table_method_scope(monkeypatch):
    source = "10-fold cross-validation.\nWe perform overall experiments 10 times.\nSEP-G & 0.5 \\\\"
    selected = {
        "table_id": 1,
        "displayed_mean": 0.5,
        "displayed_std": None,
        "divisor": 1,
        "method": "SEP-G",
        "dataset": "IMDB-MULTI",
        "metric": "Accuracy",
        "configuration": "10-fold CV",
        "eligibility": "benchmark",
        "main_experiment": True,
        "row_evidence": {"start_line": 3, "end_line": 3},
        "column_evidence": {"start_line": 1, "end_line": 1},
        "cell_evidence": {"start_line": 3, "end_line": 3},
        "protocol": {
            **protocol(),
            "design": "single_cv",
            "cv_repetitions": 1,
            "variability_scope": "unknown",
            "cv_repeat_unit": "unknown",
        },
        "cell_column_index": 1,
        "configuration_axes": {"split": "10-fold CV"},
        "identity_evidence": [{"start_line": 1, "end_line": 1}],
    }
    fact_candidate = {**selected}
    row = {
        "result_id": 243620,
        "action": "protocol_input_unresolved",
        "proposed_num_runs": None,
        "selected_candidate": selected,
        "verdict": {
            "result_id": 243620,
            "corrected_fact": {"origin": "self_evaluated", "candidates": [fact_candidate]},
            "selected_candidate_index": 0,
            "verified_candidate_indices": [0],
            "origin_supported": True,
            "execution_supported": True,
            "protocol_supported": True,
        },
    }
    review = {
        "table_id": 1,
        "method": "SEP-G",
        "count": 100,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "protocol": protocol(),
        "evidence": protocol()["evidence"],
        "scope_evidence": protocol()["scope_evidence"],
        "interpretation": "Ten complete CV repetitions, giving 100 trained models.",
        "reviewer": "human_user",
        "authorization": "User approved 100 models for ten complete CV repetitions.",
    }
    monkeypatch.setattr(decisions, "grounded_candidate", lambda candidate, _source: candidate)
    monkeypatch.setattr(decisions, "grounded_column", lambda _candidate, _source: True)
    monkeypatch.setattr(decisions, "grounded_protocol", lambda *_args, **_kwargs: True)

    updated, accepted = apply_human_protocol_review(row, source, [review])
    key = {
        "table_id": 1,
        "method": {"name": "SEP-G", "origin": "self_evaluated", "status": "unknown"},
        "previous_verdict": {},
    }
    bound = check_binding(updated, [key], source, [accepted])

    assert updated["action"] == "propose_count"
    assert updated["proposed_num_runs"] == 100
    assert updated["selected_candidate"]["protocol"]["cv_repeat_unit"] == "full_cv"
    assert bound["action"] == "propose_count"
    assert bound["protocol_binding"]["status"] == "independently_verified_protocol_override"
    new_method = check_binding(updated, [], source)
    assert new_method["action"] == "propose_count"
    assert new_method["protocol_binding"]["status"] == "source_verified_new_method_scope"

    unsupported = {
        **updated,
        "verdict": {**updated["verdict"], "execution_supported": False},
    }
    assert check_binding(unsupported, [], source)["action"] == "protocol_binding_unresolved"


def test_user_protocol_review_does_not_override_copied_or_ablation_rows(monkeypatch):
    source = "10-fold cross-validation.\nWe perform overall experiments 10 times.\n"
    row = {
        "result_id": 1,
        "action": "copied_excluded",
        "verdict": {
            "corrected_fact": {"origin": "copied"},
            "origin_supported": True,
            "execution_supported": True,
        },
    }
    review = {
        "table_id": 1,
        "method": "SEP-G",
        "count": 100,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "reviewer": "human_user",
        "authorization": "Approved for this method.",
    }

    updated, accepted = apply_human_protocol_review(row, source, [review])

    assert updated is row
    assert accepted is None


def test_missing_protocol_scope_requests_targeted_verifier_review(monkeypatch):
    verdict = SimpleNamespace(
        protocol_scope_review=None,
        origin_supported=True,
        execution_supported=True,
        corrected_fact=SimpleNamespace(origin="self_evaluated"),
        result_id=42,
    )
    monkeypatch.setattr(
        worker,
        "propose",
        lambda *_args, **_kwargs: {"action": "propose_count", "proposed_num_runs": 30},
    )
    monkeypatch.setattr(
        worker,
        "safe_assignment",
        lambda *_args, **_kwargs: {
            "action": "protocol_input_unresolved",
            "protocol_binding": {"status": "upstream_unknown_or_conflict"},
        },
    )
    rows = [{"result_id": 42}]

    feedback = worker.protocol_scope_feedback(
        rows, SimpleNamespace(verdicts=[verdict]), [], [], "source", Path("paper")
    )

    assert 42 in feedback
    assert "Independently review the exact table/method" in feedback[42]
    assert "otherwise leave it null" in feedback[42]


def test_source_verified_row_count_can_fill_unknown_prior_but_not_conflict(monkeypatch):
    source = "10-fold cross-validation.\nWe perform overall experiments 10 times.\nSEP-G & 0.5 \\\\"
    selected = {
        "table_id": 1,
        "displayed_mean": 0.5,
        "displayed_std": None,
        "divisor": 1,
        "method": "SEP-G",
        "dataset": "IMDB-MULTI",
        "metric": "Accuracy",
        "configuration": "10-fold CV",
        "eligibility": "benchmark",
        "main_experiment": True,
        "row_evidence": {"start_line": 3, "end_line": 3},
        "column_evidence": {"start_line": 1, "end_line": 1},
        "cell_evidence": {"start_line": 3, "end_line": 3},
        "protocol": protocol(),
        "cell_column_index": 1,
        "configuration_axes": {"split": "10-fold CV"},
        "identity_evidence": [{"start_line": 1, "end_line": 1}],
    }
    row = {
        "result_id": 7,
        "action": "propose_count",
        "proposed_num_runs": 100,
        "selected_candidate": selected,
        "protocol": protocol(),
        "verdict": {
            "origin_supported": True,
            "execution_supported": True,
            "protocol_supported": True,
            "corrected_fact": {"origin": "self_evaluated"},
        },
    }
    unknown = {
        "table_id": 1,
        "method": {"name": "SEP-G", "origin": "self_evaluated", "status": "complex"},
        "previous_verdict": {"benchmark_supported": True, "origin_supported": True},
    }
    known_conflict = {
        "table_id": 1,
        "method": {
            "name": "SEP-G",
            "origin": "self_evaluated",
            "status": "simple",
            "design": "repeated_training",
            "repetitions": 10,
        },
        "previous_verdict": {
            "benchmark_supported": True,
            "origin_supported": True,
            "count_supported": True,
            "unit_correct": True,
            "uniform_datasets": True,
        },
    }
    copied_prior = {
        "table_id": 1,
        "table_role": "benchmark",
        "method": {"name": "SEP-G", "origin": "copied", "status": "simple"},
        "previous_verdict": {
            "benchmark_supported": True,
            "origin_supported": False,
            "count_supported": False,
            "unit_correct": False,
            "uniform_datasets": False,
        },
    }
    monkeypatch.setattr(decisions, "grounded_candidate", lambda candidate, _source: candidate)
    monkeypatch.setattr(decisions, "grounded_column", lambda _candidate, _source: True)
    monkeypatch.setattr(decisions, "grounded_protocol", lambda *_args, **_kwargs: True)

    accepted = check_binding(row, [unknown], source)
    rejected = check_binding(row, [known_conflict], source)
    missing_key = check_binding(row, [], source)
    copied = check_binding(row, [copied_prior], source)

    assert accepted["action"] == "propose_count"
    assert accepted["protocol_binding"]["status"] == "source_verified_unknown_prior"
    assert rejected["action"] == "protocol_input_conflict"
    assert missing_key["action"] == "propose_count"
    assert missing_key["protocol_binding"]["status"] == "source_verified_new_method_scope"
    assert copied["action"] == "protocol_input_unresolved"
