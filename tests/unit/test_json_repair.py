"""Tests for truncated JSON recovery."""

from backend.json_repair import _close_truncated_json, parse_json_lenient


def test_close_truncated_json_object():
    closed = _close_truncated_json('{"results": [{"model": "GIN", "value": 0.1')
    parsed = parse_json_lenient(closed)
    assert isinstance(parsed, dict)
    assert parsed["results"][0]["model"] == "GIN"


def test_salvage_results_array_from_truncated_payload():
    raw = (
        '{"proposed_model": null, "baseline_models": [], "results": ['
        '{"model": "GIN", "dataset": "QM9", "metric": "gap", "value": 0.04}, '
        '{"model": "GIN", "dataset": "QM9", "metric": "mu", "value": 0.03'
    )
    parsed = parse_json_lenient(raw)
    assert isinstance(parsed, dict)
    assert len(parsed["results"]) >= 1
    assert parsed["results"][0]["metric"] == "gap"


def test_parse_json_lenient_rejects_garbage():
    assert parse_json_lenient("not json at all") is None


def test_salvage_truncated_dataset_statistics_payload():
    raw = (
        '{\n  "datasets": [\n    {\n      "name": "QM9",\n'
        '      "variant": "Standard split",\n'
        '      "num_graphs": 134000,\n'
        '      "avg_nodes": 18.0,\n'
        '      "avg_edges": null,\n'
        '      "num_classes": null,\n'
        '      "raw_valu'
    )
    parsed = parse_json_lenient(raw)
    assert isinstance(parsed, dict)
    assert parsed["datasets"][0]["name"] == "QM9"
    assert parsed["datasets"][0]["num_graphs"] == 134000
