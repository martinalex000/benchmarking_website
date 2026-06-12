"""Unit tests for model metadata default lookups."""

from backend.model_metadata_defaults import lookup_default_model_type, lookup_model_type


def test_lookup_default_model_type_ogb_baselines():
    assert lookup_default_model_type("GCN + Virtual Node") == "gnn"
    assert lookup_default_model_type("Node2Vec") == "walk"
    assert lookup_default_model_type("MLP") == "other_traditional"


def test_lookup_model_type_prefers_paper_extraction():
    type_lookup = {"graphgps": "hybrid"}
    assert lookup_model_type("GraphGPS", type_lookup) == "hybrid"


def test_lookup_model_type_falls_back_to_family_and_defaults():
    type_lookup: dict[str, str | None] = {}
    defaults = {"gcn": "gnn", "node2vec": "walk"}
    assert lookup_model_type("GCN + Add. Feat.", type_lookup, defaults=defaults) == "gnn"
    assert lookup_model_type("Node2Vec", type_lookup, defaults=defaults) == "walk"
