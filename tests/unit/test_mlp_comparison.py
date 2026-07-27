from pathlib import Path
from types import SimpleNamespace

from backend.mlp_comparison import compare_results, write_comparison_outputs


def _result(
    model: str,
    value: float,
    paper: str,
    *,
    baseline: bool = False,
    std: float | None = None,
    feature_source: str | None = None,
) -> SimpleNamespace:
    dataset = SimpleNamespace(
        name="SyntheticNodes",
        task_type="node_classification",
        primary_metric="Accuracy",
    )
    variant = SimpleNamespace(dataset=dataset, is_standard=1)
    return SimpleNamespace(
        effective_model_name=model,
        model=SimpleNamespace(canonical_name=model),
        dataset_variant=variant,
        metric_name="Accuracy",
        protocol_decision="standard",
        is_problematic=0,
        display_value=value,
        display_std=std,
        higher_is_better=True,
        is_baseline=baseline,
        input_feature_source=feature_source,
        paper=SimpleNamespace(arxiv_id=paper, title=f"Paper {paper}"),
    )


def test_compare_results_deduplicates_methods_and_counts_ties() -> None:
    results = [_result("MLP", 0.5, "mlp-paper", baseline=True, std=0.01)]
    for index in range(16):
        value = 0.6 if index < 8 else 0.5 if index < 12 else 0.4
        results.append(_result(f"Method-{index}", value, f"paper-{index % 10}"))
    # A second report of Method-0 must not create a second method count.
    results.append(_result("Method-0", 0.55, "paper-extra"))
    results.append(_result("LLM+MLP", 0.99, "llm-paper", feature_source="llm_features"))

    comparisons = compare_results(results)

    assert len(comparisons) == 1
    comparison = comparisons[0]
    assert comparison["method_count"] == 16
    assert comparison["group"] == "Other benchmarks"
    assert comparison["paper_count"] == 11
    assert comparison["better_count"] == 8
    assert comparison["tied_count"] == 4
    assert comparison["worse_count"] == 4
    assert comparison["at_least_mlp_count"] == 12
    assert comparison["sota"]["value"] == 0.6


def test_compare_results_requires_both_coverage_thresholds() -> None:
    results = [_result("MLP", 0.5, "mlp-paper", baseline=True)]
    results.extend(_result(f"Method-{i}", 0.6, f"paper-{i % 9}") for i in range(15))

    assert compare_results(results) == []
    assert len(compare_results(results, min_papers=1)) == 1


def test_write_comparison_outputs_creates_json_csv_and_figure(tmp_path: Path) -> None:
    comparisons = compare_results(
        [_result("MLP", 0.5, "mlp-paper", baseline=True)]
        + [_result(f"Method-{i}", 0.6, f"paper-{i % 10}") for i in range(15)],
        min_papers=1,
    )

    paths = write_comparison_outputs(comparisons, tmp_path)

    assert all(path.exists() for path in paths)
    assert paths[0].read_text(encoding="utf-8").startswith("[")
    assert "better_count" in paths[1].read_text(encoding="utf-8")
