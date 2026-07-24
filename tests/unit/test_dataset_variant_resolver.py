"""Unit tests for shared dataset variant resolution helpers."""

from backend.dataset_variant_resolver import (
    build_dataset_variant_lookup,
    resolve_dataset_variant_quiet,
)


class _FakeDataset:
    def __init__(self, name: str):
        self.name = name


class _FakeVariant:
    def __init__(self, name: str, dataset_name: str, is_standard: bool = False):
        self.name = name
        self.dataset = _FakeDataset(dataset_name)
        self.is_standard = is_standard


class _FakeSession:
    def __init__(self, variants):
        self._variants = variants

    def query(self, *args):
        return self

    def all(self):
        return self._variants


def test_build_dataset_variant_lookup_includes_variant_and_dataset_names():
    lookup = build_dataset_variant_lookup(
        _FakeSession([_FakeVariant("Standard split", "Peptides-func")])
    )

    assert lookup["standard split"].name == "Standard split"
    assert lookup["peptides-func"].name == "Standard split"


def test_build_dataset_variant_lookup_prefers_standard_dataset_variant():
    lookup = build_dataset_variant_lookup(
        _FakeSession(
            [
                _FakeVariant("Random 10-fold", "Cora"),
                _FakeVariant("Planetoid split", "Cora", is_standard=True),
            ]
        )
    )

    assert lookup["cora"].name == "Planetoid split"


def test_resolve_dataset_variant_quiet_prefers_exact_match():
    variant = _FakeVariant("Standard split", "Peptides-func")

    resolved = resolve_dataset_variant_quiet(
        "Peptides-func",
        {"peptides-func": variant, "standard split": variant},
    )

    assert resolved is variant


def test_resolve_dataset_variant_quiet_supports_fuzzy_match():
    variant = _FakeVariant("Standard split", "Peptides-func")

    resolved = resolve_dataset_variant_quiet("peptides func", {"peptides-func": variant})

    assert resolved is variant


def test_resolve_dataset_variant_quiet_returns_none_for_unknown_dataset():
    assert resolve_dataset_variant_quiet("unknown dataset", {}) is None


def test_resolve_dataset_variant_quiet_does_not_cross_ogb_graph_families():
    molpcba = _FakeVariant("Standard split", "ogbg-molpcba")
    citation2 = _FakeVariant("Standard split", "ogbl-citation2")

    assert resolve_dataset_variant_quiet("ogbg-ppa", {"ogbg-molpcba": molpcba}) is None
    assert resolve_dataset_variant_quiet("ogbl-ppa", {"ogbl-citation2": citation2}) is None
