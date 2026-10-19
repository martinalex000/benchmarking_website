from experiments.table_provenance_experiment.check_setting_scope import guard_setting_scope


def row(origin="unclear", executed=False, reason="contradicted_setting"):
    return {
        "action": "propose_quarantine",
        "reason": reason,
        "proposed_num_runs": None,
        "verdict": {
            "setting_status": "contradicted",
            "origin_supported": True,
            "execution_supported": executed,
            "corrected_fact": {
                "origin": origin,
                "execution_evidence": [{"start_line": 1, "end_line": 1}],
            },
        },
        "correction": None,
    }


def test_unknown_execution_does_not_make_author_split_a_quarantine_reason():
    original = row()
    result = guard_setting_scope(original)
    assert result["action"] == "setting_scope_unresolved"
    assert original["action"] == "propose_quarantine"


def test_actual_ablation_exclusion_is_preserved():
    assert guard_setting_scope(row(reason="verifier_excluded"))["action"] == "propose_quarantine"


def test_supported_current_execution_preserves_protocol_exclusion():
    assert guard_setting_scope(row("self_evaluated", True))["action"] == "propose_quarantine"


def test_setting_only_repair_is_withheld_but_numeric_repair_survives():
    original = row()
    original["action"] = "origin_unresolved"
    original["correction"] = {
        "old": {"variant": "10-fold CV", "value": 0.5},
        "corrected": {"variant": "80/10/10 split", "value": 0.6},
    }
    result = guard_setting_scope(original)
    assert result["correction"]["corrected"] == {"variant": "10-fold CV", "value": 0.6}
    original["correction"]["corrected"]["value"] = 0.5
    assert guard_setting_scope(original)["correction"] is None
