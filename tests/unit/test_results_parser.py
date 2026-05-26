"""Unit tests for results_parser value parsing and fuzzy matching."""

import pytest
from backend.results_parser import (
    _infer_zinc_variant,
    _load_variant_map,
    parse_value_std,
    resolve_dataset_variant,
)


def test_parse_plain_float():
    val, std = parse_value_std(0.653)
    assert val == pytest.approx(0.653)
    assert std is None


def test_parse_plusminus_string():
    val, std = parse_value_std("0.653 ± 0.004")
    assert val == pytest.approx(0.653)
    assert std == pytest.approx(0.004)


def test_parse_paren_std():
    val, std = parse_value_std("0.653(0.004)")
    assert val == pytest.approx(0.653)
    assert std == pytest.approx(0.004)


def test_parse_none():
    val, std = parse_value_std(None)
    assert val is None
    assert std is None


def test_parse_invalid_string():
    val, std = parse_value_std("n/a")
    assert val is None


def test_parse_integer():
    val, std = parse_value_std(1)
    assert val == 1.0
    assert std is None


def test_resolve_exact(tmp_path):
    """resolve_dataset_variant with exact match."""
    variant_map = {"peptides-func": 10, "standard split": 10}
    # Import the function directly; no DB session needed for this test
    from backend.results_parser import resolve_dataset_variant as rdv

    class FakeSession:
        def query(self, *a):
            return self

        def all(self):
            return []

    result = rdv("Peptides-func", FakeSession(), variant_map)
    assert result == 10


def test_resolve_fuzzy(tmp_path):
    from backend.results_parser import resolve_dataset_variant as rdv

    class FakeSession:
        def query(self, *a):
            return self

        def all(self):
            return []

    variant_map = {"peptides-func": 10}
    result = rdv("peptides func", FakeSession(), variant_map)
    assert result == 10


def test_resolve_no_match():
    from backend.results_parser import resolve_dataset_variant as rdv

    class FakeSession:
        def query(self, *a):
            return self

        def all(self):
            return []

    result = rdv("completely_unknown_dataset_xyz", FakeSession(), {})
    assert result is None


class _FakeDataset:
    def __init__(self, name: str):
        self.name = name


class _FakeVariant:
    def __init__(self, variant_id: int, name: str, dataset_name: str):
        self.id = variant_id
        self.name = name
        self.dataset = _FakeDataset(dataset_name)


class _FakeSessionWithVariants:
    def __init__(self, variants):
        self._variants = variants

    def query(self, *args):
        return self

    def all(self):
        return self._variants


def test_load_variant_map_prefers_zinc_subset_for_plain_name():
    session = _FakeSessionWithVariants(
        [
            _FakeVariant(21, "Subset (12k)", "ZINC"),
            _FakeVariant(22, "Full", "ZINC"),
        ]
    )

    variant_map = _load_variant_map(session)

    assert variant_map["zinc"] == 21
    assert variant_map["zinc subset"] == 21
    assert variant_map["zinc full"] == 22


def test_resolve_zinc_plain_name_uses_subset_variant():
    variant_map = {
        "zinc": 21,
        "subset (12k)": 21,
        "zinc subset": 21,
        "full": 22,
        "zinc full": 22,
    }

    class FakeSession:
        def query(self, *a):
            return self

        def all(self):
            return []

    assert resolve_dataset_variant("ZINC", FakeSession(), variant_map) == 21
    assert resolve_dataset_variant("ZINC full", FakeSession(), variant_map) == 22


def test_infer_zinc_variant_from_table_ref_full():
    variant_map = {
        "zinc subset": 21,
        "subset (12k)": 21,
        "zinc full": 22,
        "full": 22,
    }

    entry = {"dataset": "ZINC", "metric": "MAE", "value": 0.088, "table_ref": "tab:zinc_full"}

    assert _infer_zinc_variant(entry, variant_map, paper_text="") == 22


def test_infer_zinc_variant_from_paper_stats_subset():
    variant_map = {
        "zinc subset": 21,
        "subset (12k)": 21,
        "zinc full": 22,
        "full": 22,
    }

    paper_text = "ZINC contains 12K molecular graphs from the ZINC database."
    entry = {"dataset": "ZINC", "metric": "MAE", "value": 0.11}

    assert _infer_zinc_variant(entry, variant_map, paper_text=paper_text) == 21


def test_infer_zinc_variant_uses_value_fallback_when_paper_mentions_both():
    variant_map = {
        "zinc subset": 21,
        "subset (12k)": 21,
        "zinc full": 22,
        "full": 22,
    }

    paper_text = "ZINC subset has 12,000 graphs while ZINC Full has 249,456 graphs."

    full_entry = {"dataset": "ZINC", "metric": "MAE", "value": 0.025}
    subset_entry = {"dataset": "ZINC", "metric": "MAE", "value": 0.123}

    assert _infer_zinc_variant(full_entry, variant_map, paper_text=paper_text) == 22
    assert _infer_zinc_variant(subset_entry, variant_map, paper_text=paper_text) == 21
