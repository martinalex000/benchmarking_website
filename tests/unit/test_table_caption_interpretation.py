"""Tests for table caption interpretation."""

from backend.table_caption_interpretation import (
    build_table_caption_policy_map,
    combined_merge_policy,
    interpret_table_caption,
    policy_for_table_ref,
    resolve_model_name_for_policy,
)


class _FakeTable:
    def __init__(self, number: int, caption: str) -> None:
        self.number = number
        self.caption = caption


def test_interpret_2406_table2_caption():
    caption = (
        "Node classification results over homophilous graphs (%). "
        "∗ indicates our implementation, while other results are taken from [12, 76]. "
        "The top 1st, 2nd and 3rd results are highlighted."
    )
    policy = interpret_table_caption(caption)
    assert policy.merge_equivalent_model_variants
    assert "*" in policy.equivalent_markers
    assert policy.values_are_percent


def test_resolve_graphgps_variants():
    caption = "* indicates our implementation, while other results are taken from [12]"
    policy = interpret_table_caption(caption)
    assert resolve_model_name_for_policy("GraphGPS*", policy) == "GraphGPS"
    assert resolve_model_name_for_policy("GraphGPS", policy) == "GraphGPS"


def test_policy_for_table_ref():
    tables = [
        _FakeTable(
            2,
            "* indicates our implementation, other results taken from [12]",
        )
    ]
    policies = build_table_caption_policy_map(tables)
    default = combined_merge_policy(policies)
    assert default is not None
    table_policy = policy_for_table_ref("Table 2", policies, default)
    assert table_policy is not None
    assert table_policy.merge_equivalent_model_variants


def test_no_merge_without_caption_hint():
    policy = interpret_table_caption("Benchmark results on ZINC.")
    assert not policy.merge_equivalent_model_variants


def test_ablation_caption_flagged():
    policy = interpret_table_caption("Ablation study: removing the attention block.")
    assert policy.is_ablation_or_diagnostic


def test_auxiliary_metric_caption_flagged():
    policy = interpret_table_caption("Correlation between accuracy and depth; accuracy ratio")
    assert policy.is_ablation_or_diagnostic


def test_is_ablation_table_ref():
    tables = [_FakeTable(5, "Ablation study on Cora")]
    policies = build_table_caption_policy_map(tables)
    from backend.table_caption_interpretation import is_ablation_table_ref

    assert is_ablation_table_ref("Table 5", policies)
    assert not is_ablation_table_ref("Table 2", policies)
