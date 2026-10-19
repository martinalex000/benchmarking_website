from backend.mapping.binding import check_binding, method_identity_conflict, source_method_key
from backend.mapping.source import method_key


def candidate(method, column=1):
    return {
        "table_id": 1,
        "method": method,
        "row_evidence": {"start_line": 2, "end_line": 2},
        "cell_evidence": {"start_line": 2, "end_line": 2},
        "cell_column_index": column,
    }


def prior_key(method):
    return {
        "table_id": 1,
        "method": {"name": method, "origin": "self_evaluated", "status": "simple", "design": "repeated_training", "repetitions": 100},
        "previous_verdict": {
            "benchmark_supported": True,
            "origin_supported": True,
            "count_supported": True,
            "unit_correct": True,
            "uniform_datasets": True,
        },
    }


def row(selected):
    return {
        "result_id": 7,
        "action": "propose_count",
        "proposed_num_runs": 100,
        "selected_candidate": selected,
    }


def test_source_method_modifier_is_part_of_binding_identity():
    source = "\\begin{tabular}{lc}\nGCN+ & 0.9 \\\\\n\\end{tabular}"
    selected = candidate("GCN+")

    assert source_method_key(selected, source) == method_key("GCN+")
    assert not method_identity_conflict(selected, source)
    assert check_binding(row(selected), [prior_key("GCN")], source)["action"] == (
        "protocol_binding_unresolved"
    )


def test_modifier_mismatch_cannot_inherit_count_from_plain_method():
    source = "\\begin{tabular}{lc}\nGCN+ & 0.9 \\\\\n\\end{tabular}"
    selected = candidate("GCN")

    result = check_binding(row(selected), [prior_key("GCN")], source)

    assert method_identity_conflict(selected, source)
    assert result["protocol_binding"]["status"] == "source_method_identity_conflict"
    assert result["action"] == "protocol_binding_unresolved"
    assert result["proposed_num_runs"] is None
