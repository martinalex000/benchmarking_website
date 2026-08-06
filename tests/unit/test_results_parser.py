"""Unit tests for results_parser value parsing and fuzzy matching."""

from types import SimpleNamespace

import pytest

from backend.models import Result
from backend.qm9_targets import normalize_qm9_metric
from backend.results_parser import (
    _apply_feature_source_model_name,
    _dataset_metric_value_is_valid,
    _infer_zinc_variant,
    _load_variant_map,
    _protocol_decision,
    _update_result,
    normalize_dataset_alias,
    normalize_percentage_metric,
    parse_extracted_bool,
    parse_optional_extracted_bool,
    parse_value_std,
    resolve_dataset_variant,
    resolve_dataset_variant_with_reason,
    result_is_leaderboard_eligible,
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


def test_update_result_clears_stale_nullable_fields():
    result = Result(
        metric_value=0.8,
        metric_std=0.02,
        uses_external_data=1,
        params_millions=12.5,
        extraction_model="old-model",
    )

    changed = _update_result(
        result,
        {"value": 0.81, "uses_external_data": None},
        "new-model",
        params_millions=None,
        params_present=True,
    )

    assert changed is True
    assert result.metric_value == pytest.approx(0.81)
    assert result.metric_std is None
    assert result.uses_external_data is None
    assert result.params_millions is None
    assert result.extraction_model == "new-model"


def test_update_result_persists_feature_provenance():
    result = Result(input_feature_source="raw_features")

    changed = _update_result(
        result,
        {
            "input_feature_source": "llm_features",
            "feature_source_evidence": "DeBERTa embeddings",
        },
        "new-model",
    )

    assert changed is True
    assert result.input_feature_source == "llm_features"
    assert result.feature_source_evidence == "DeBERTa embeddings"


def test_compact_feature_provenance_renames_mlp():
    entry = {"model": "MLP", "f": "slm_features", "x": "DeBERTa embeddings"}

    _apply_feature_source_model_name(entry)

    assert entry["model"] == "MLP+LLM_features"
    assert entry["input_feature_source"] == "llm_features"
    assert entry["feature_source_evidence"] == "DeBERTa embeddings"


def test_parse_integer():
    val, std = parse_value_std(1)
    assert val == 1.0
    assert std is None


def test_parse_scientific_notation_values():
    val, std = parse_value_std("1.2e-3")
    assert val == pytest.approx(0.0012)
    assert std is None

    val, std = parse_value_std("1e-3 ± 2e-4")
    assert val == pytest.approx(0.001)
    assert std == pytest.approx(0.0002)


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
    def __init__(self, variant_id: int, name: str, dataset_name: str, is_standard: bool = False):
        self.id = variant_id
        self.name = name
        self.dataset = _FakeDataset(dataset_name)
        self.is_standard = is_standard


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


def test_load_variant_map_prefers_standard_variant_for_plain_dataset_name():
    session = _FakeSessionWithVariants(
        [
            _FakeVariant(60, "Random 10-fold", "Cora", is_standard=False),
            _FakeVariant(59, "Planetoid split", "Cora", is_standard=True),
        ]
    )

    variant_map = _load_variant_map(session)

    assert variant_map["cora"] == 59


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

    variant_id, reason = _infer_zinc_variant(entry, variant_map, paper_text="")
    assert variant_id == 22
    assert "entry cue matched full" in reason


def test_infer_zinc_variant_from_paper_stats_subset():
    variant_map = {
        "zinc subset": 21,
        "subset (12k)": 21,
        "zinc full": 22,
        "full": 22,
    }

    paper_text = "ZINC contains 12K molecular graphs from the ZINC database."
    entry = {"dataset": "ZINC", "metric": "MAE", "value": 0.11}

    variant_id, reason = _infer_zinc_variant(entry, variant_map, paper_text=paper_text)
    assert variant_id == 21
    assert "paper text matched subset" in reason


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

    full_variant_id, full_reason = _infer_zinc_variant(
        full_entry, variant_map, paper_text=paper_text
    )
    subset_variant_id, subset_reason = _infer_zinc_variant(
        subset_entry, variant_map, paper_text=paper_text
    )

    assert full_variant_id == 22
    assert "mae fallback" in full_reason
    assert subset_variant_id == 21
    assert "mae fallback" in subset_reason


def test_qm9_metric_normalization_via_module():
    assert normalize_qm9_metric("HOMO-LUMO gap") == "gap"
    assert normalize_qm9_metric("MAE") is None


def test_percentage_normalization_does_not_treat_gap_as_ap():
    val, std = normalize_percentage_metric("gap", 2.5, 0.1)
    assert val == pytest.approx(2.5)
    assert std == pytest.approx(0.1)


@pytest.mark.parametrize(
    ("metric", "value", "expected"),
    [
        ("AP", 44.2, 0.442),
        ("mAP", 44.2, 0.442),
        ("Accuracy", 91.0, 0.91),
        ("Micro-F1", 72.5, 0.725),
        ("Hits@50", 66.0, 0.66),
    ],
)
def test_percentage_normalization_recognizes_percentage_metrics(metric, value, expected):
    val, _std = normalize_percentage_metric(metric, value, None)
    assert val == pytest.approx(expected)


def test_parse_extracted_bool_handles_string_false():
    assert parse_extracted_bool("False", default=True) is False
    assert parse_extracted_bool("true", default=False) is True
    assert parse_optional_extracted_bool("0") is False
    assert parse_optional_extracted_bool("1") is True
    assert parse_optional_extracted_bool("unknown") is None


def test_ogb_dataset_alias_code2():
    variant_map = {"ogbg-code2": 45, "ogbg-molpcba": 24}
    variant_id, reason = resolve_dataset_variant_with_reason("ogbg-code2", None, variant_map)
    assert variant_id == 45
    assert reason == "dataset: exact match"


def test_ogb_ppa_does_not_fuzzy_match_molpcba():
    variant_map = {"ogbg-molpcba": 24}
    variant_id, reason = resolve_dataset_variant_with_reason("ogbg-ppa", None, variant_map)
    assert variant_id is None


def test_qm7_does_not_fuzzy_match_qm7b():
    variant_id, reason = resolve_dataset_variant_with_reason("QM7", None, {"qm7b": 12})
    assert variant_id is None
    assert reason == "dataset: ambiguous generic name"


def test_ogbl_ppa_does_not_fuzzy_match_citation2():
    variant_map = {"ogbl-citation2": 53}
    variant_id, reason = resolve_dataset_variant_with_reason("ogbl-ppa", None, variant_map)
    assert variant_id is None
    assert reason == "dataset: unresolved"


def test_ogb_ppa_exact_match():
    variant_map = {"ogbg-ppa": 99}
    variant_id, reason = resolve_dataset_variant_with_reason("ogbg-ppa", None, variant_map)
    assert variant_id == 99
    assert reason == "dataset: exact match"


def test_dataset_alias_normalization_in_resolve():
    variant_map = {"amazon-computers": 67, "ogbn-arxiv": 47}
    variant_id, reason = resolve_dataset_variant_with_reason("Computers", None, variant_map)
    assert variant_id == 67
    assert reason == "dataset: exact match"

    variant_id, reason = resolve_dataset_variant_with_reason("arXiv", None, variant_map)
    assert variant_id is None
    assert reason == "dataset: ambiguous arXiv label"


def test_ambiguous_generic_dataset_name_is_not_fuzzy_matched():
    variant_id, reason = resolve_dataset_variant_with_reason(
        "Amazon",
        None,
        {"amazon2m": 12, "amazon-ratings": 13},
    )

    assert variant_id is None
    assert reason == "dataset: ambiguous generic name"


def test_dataset_variant_resolution_rejects_conflicting_full_qualifier():
    variant_id, reason = resolve_dataset_variant_with_reason(
        "CiteSeer-Full", None, {"citeseer": 41, "planetoid split": 41}
    )

    assert variant_id is None
    assert reason == "dataset: unresolved"


def test_protocol_contract_requires_canonical_split_evidence():
    variant = SimpleNamespace(
        is_standard=True,
        split_type="fixed",
        dataset=SimpleNamespace(name="CiteSeer", task_type="node_classification"),
    )
    assert (
        _protocol_decision(
            {
                "evaluation_task": "node_classification",
                "protocol_decision": "standard",
                "protocol_note": "Planetoid fixed split from Yang et al.",
            },
            variant,
        )
        == "standard"
    )
    assert (
        _protocol_decision(
            {
                "evaluation_task": "node_classification",
                "protocol_decision": "standard",
                "protocol_note": "Five-fold cross-validation.",
            },
            variant,
        )
        == "nonstandard"
    )


def test_qm9_requires_split_evidence_even_with_standard_decision():
    variant = SimpleNamespace(
        is_standard=True,
        split_type="random",
        dataset=SimpleNamespace(name="QM9", task_type="graph_regression"),
    )

    assert (
        _protocol_decision(
            {
                "evaluation_task": "graph_regression",
                "protocol_decision": "standard",
                "protocol_note": "MAE on QM9 targets.",
            },
            variant,
        )
        == "uncertain"
    )


def test_film_alias_uses_movie_lens_exception_for_its_distinct_graph():
    assert normalize_dataset_alias("Film") == "Actor"
    assert normalize_dataset_alias("Film", arxiv_id="1609.04508") == "MovieLens Film"


def test_wisconsin_contract_distinguishes_geom_masks_from_new_random_splits():
    variant = SimpleNamespace(
        is_standard=True,
        split_type="fixed",
        dataset=SimpleNamespace(name="Wisconsin", task_type="node_classification"),
    )

    assert (
        _protocol_decision(
            {
                "evaluation_task": "node_classification",
                "protocol_decision": "standard",
                "protocol_note": (
                    "10 random splits from Pei et al. 2020 with 48/32/20 train/validation/test"
                ),
            },
            variant,
        )
        == "standard"
    )
    assert (
        _protocol_decision(
            {
                "evaluation_task": "node_classification",
                "protocol_decision": "standard",
                "protocol_note": "10 random splits with 60%/20%/20% partitions",
            },
            variant,
        )
        == "nonstandard"
    )
    assert (
        _protocol_decision(
            {
                "evaluation_task": "node_classification",
                "protocol_decision": "standard",
                "protocol_note": "Standard node classification task on Wisconsin.",
            },
            variant,
        )
        == "uncertain"
    )


def test_stored_wisconsin_rows_apply_manual_curation_and_audited_notes():
    variant = SimpleNamespace(
        is_standard=True,
        split_type="fixed",
        dataset=SimpleNamespace(name="Wisconsin", task_type="node_classification"),
    )
    common = {
        "dataset_variant": variant,
        "effective_model_name": "Model",
        "metric_name": "Accuracy",
        "evaluation_task": "node_classification",
        "protocol_decision": "standard",
        "protocol_note": "Standard node classification task.",
    }

    valid = SimpleNamespace(
        **common,
        paper=SimpleNamespace(arxiv_id="2504.19785"),
    )
    excluded = SimpleNamespace(
        **common,
        paper=SimpleNamespace(arxiv_id="2604.01878"),
    )

    assert result_is_leaderboard_eligible(valid)
    assert not result_is_leaderboard_eligible(excluded)


def test_qm9_gap_zero_is_rejected_but_positive_gap_is_valid():
    assert not _dataset_metric_value_is_valid("QM9", "gap", 0.0)
    assert _dataset_metric_value_is_valid("QM9", "gap", 0.043)


def test_percentage_metrics_reject_negative_sentinels():
    assert not _dataset_metric_value_is_valid("MUTAG", "Accuracy", -1.0)
    assert not _dataset_metric_value_is_valid("Cora", "Accuracy", 1.01)
    assert _dataset_metric_value_is_valid("Cora", "Accuracy", 0.91)


def test_error_metrics_reject_negative_missing_value_sentinels():
    assert not _dataset_metric_value_is_valid("MD17", "MAE", -1.0)
    assert not _dataset_metric_value_is_valid("ZINC", "RMSE", -0.1)
    assert _dataset_metric_value_is_valid("MD17", "MAE", 0.145)
