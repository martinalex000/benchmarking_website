"""Unit tests for model name resolution helpers."""

from thefuzz import fuzz as fuzz_lib

from backend.model_name_resolution import (
    model_family_token,
    model_family_token_for_metadata,
    model_names_fuzzy_compatible,
    normalize_model_name_for_resolution,
    ogb_dataset_families_compatible,
)


def test_normalize_virt_abbreviation():
    assert normalize_model_name_for_resolution("GCN + Virt. Node") == "GCN + Virtual Node"
    assert normalize_model_name_for_resolution("GIN + Virt Node") == "GIN + Virtual Node"


def test_normalize_strips_role_suffix():
    assert normalize_model_name_for_resolution("IPR-MPNN (ours)") == "IPR-MPNN"


def test_normalize_preserves_implementation_asterisk():
    """Asterisk stripping is caption-driven, not unconditional normalization."""
    assert normalize_model_name_for_resolution("GraphGPS*") == "GraphGPS*"


def test_model_family_token():
    assert model_family_token("GCN + Virtual Node") == "gcn"
    assert model_family_token("GIN + Virtual Node") == "gin"
    assert model_family_token("R-GCN") == "r-gcn"
    assert model_family_token("Graph SAGE") == "graphsage"


def test_model_family_token_for_metadata():
    assert model_family_token_for_metadata("GCN + Virtual Node") == "gcn"
    assert model_family_token_for_metadata("TransE (5x dim)") == "transe"
    assert model_family_token_for_metadata("R-GCN") == "rgcn"
    assert model_family_token_for_metadata("Node2Vec") == "node2vec"
def test_gin_gcn_not_fuzzy_compatible():
    a = "GIN + Virtual Node"
    b = "GCN + Virtual Node"
    score = fuzz_lib.token_sort_ratio(a.lower(), b.lower())
    assert score >= 88
    assert not model_names_fuzzy_compatible(a, b, score, 88)


def test_gcn_virt_spelling_variants_compatible():
    a = "GCN + Virt. Node"
    b = "GCN + Virtual Node"
    score = fuzz_lib.token_sort_ratio(a.lower(), b.lower())
    assert model_names_fuzzy_compatible(a, b, score, 88)


def test_ogb_dataset_family_guard():
    assert not ogb_dataset_families_compatible("ogbg-ppa", "ogbl-ppa")
    assert not ogb_dataset_families_compatible("ogbn-arxiv", "ogbg-molpcba")
    assert ogb_dataset_families_compatible("ogbg-ppa", "ogbg-molhiv")


def test_temporal_tgb_datasets_do_not_fuzzy_match_ogb_link_datasets():
    assert not ogb_dataset_families_compatible("tgbl-wiki", "ogbl-wikikg2")
    assert ogb_dataset_families_compatible("tgbl-wiki", "tgbl-flight")
