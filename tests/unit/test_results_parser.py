"""Unit tests for results_parser value parsing and fuzzy matching."""
import pytest
from backend.results_parser import parse_value_std, resolve_dataset_variant


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
        def query(self, *a): return self
        def all(self): return []

    result = rdv("Peptides-func", FakeSession(), variant_map)
    assert result == 10


def test_resolve_fuzzy(tmp_path):
    from backend.results_parser import resolve_dataset_variant as rdv

    class FakeSession:
        def query(self, *a): return self
        def all(self): return []

    variant_map = {"peptides-func": 10}
    result = rdv("peptides func", FakeSession(), variant_map)
    assert result == 10


def test_resolve_no_match():
    from backend.results_parser import resolve_dataset_variant as rdv

    class FakeSession:
        def query(self, *a): return self
        def all(self): return []

    result = rdv("completely_unknown_dataset_xyz", FakeSession(), {})
    assert result is None
