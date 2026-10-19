"""Alias scope and bookkeeping must not create semantic changes."""

from types import SimpleNamespace

import pytest

from backend.result_mapping_checks import equivalent_number, same_dataset, sole_verified_selection


@pytest.mark.parametrize(
    "stored,source", [("ZINC", "ZINC12K"), ("ZINC", "ZINC-12K"), ("Cora", "CORA")]
)
def test_supported_dataset_aliases(stored, source):
    assert same_dataset(stored, source)


@pytest.mark.parametrize("source", ["ZINC-Full", "ZINC250K", "PCQM4Mv2"])
def test_zinc_subset_does_not_match_full_or_other_datasets(source):
    assert not same_dataset("ZINC", source)


def test_float_noise_is_not_a_repair_but_null_and_zero_are_distinct():
    assert equivalent_number(0.123, 0.12300000000000001)
    assert not equivalent_number(None, 0)
    assert not equivalent_number(0.123, 0.124)
    assert not equivalent_number(float("nan"), float("nan"))


def test_multiple_verified_candidates_are_never_selected_implicitly():
    verdict = SimpleNamespace(selected_candidate_index=None, verified_candidate_indices=[0, 1])
    assert sole_verified_selection(verdict) is verdict


def test_sole_verified_candidate_can_fill_omitted_selection():
    class Verdict(SimpleNamespace):
        def model_copy(self, update, deep):
            return Verdict(**{**self.__dict__, **update})

    verdict = Verdict(
        selected_candidate_index=None,
        verified_candidate_indices=[0],
        corrected_fact=SimpleNamespace(candidates=[object()]),
    )
    result = sole_verified_selection(verdict)
    assert result.selected_candidate_index == 0
    assert verdict.selected_candidate_index is None
