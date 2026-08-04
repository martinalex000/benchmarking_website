from pathlib import Path
from types import SimpleNamespace

from backend.mlp_comparison import (
    MLP_COMPARISON_COLORS,
    _classification_counts,
    _comparison_class,
    _worse_share,
    compare_results,
    write_comparison_figures,
    write_comparison_outputs,
)


def _result(
    model: str,
    value: float,
    paper: str,
    *,
    baseline: bool = False,
    std: float | None = None,
    feature_source: str | None = None,
    dataset_name: str = "SyntheticNodes",
    benchmark_name: str | None = None,
    benchmark_is_legacy: bool = False,
    protocol_note: str | None = None,
) -> SimpleNamespace:
    benchmark = (
        SimpleNamespace(name=benchmark_name, is_legacy=benchmark_is_legacy)
        if benchmark_name
        else None
    )
    dataset = SimpleNamespace(
        name=dataset_name,
        task_type="node_classification",
        primary_metric="Accuracy",
        benchmark=benchmark,
    )
    variant = SimpleNamespace(dataset=dataset, is_standard=1)
    return SimpleNamespace(
        effective_model_name=model,
        model=SimpleNamespace(canonical_name=model),
        dataset_variant=variant,
        metric_name="Accuracy",
        protocol_decision="standard",
        protocol_note=protocol_note,
        evaluation_task="node_classification",
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


def test_comparison_ties_use_combined_std_and_zero_for_missing_std() -> None:
    mlp = _result("MLP", 0.5, "mlp-paper", baseline=True, std=0.02)

    assert _comparison_class(_result("GCN", 0.529, "paper-tied", std=0.01), mlp, True) == "tied"
    assert _comparison_class(_result("GCN", 0.531, "paper-better", std=0.01), mlp, True) == "better"
    assert _comparison_class(_result("GCN", 0.51, "paper-missing", std=None), mlp, True) == "tied"
    assert _comparison_class(_result("GCN", 0.47, "paper-worse", std=None), mlp, True) == "worse"


def test_paper_figure_counts_include_ties_in_worse_percentage_denominator() -> None:
    counts = _classification_counts(
        [
            {"classification": "better"},
            {"classification": "tied"},
            {"classification": "worse"},
        ]
    )

    assert counts == {"better": 1, "tied": 1, "worse": 1}
    assert sum(counts.values()) == 3
    assert _worse_share(counts) == 100 / 3


def test_compare_results_applies_protocol_exclusions_before_selecting_mlp() -> None:
    results = [
        _result(
            "MLP",
            0.99,
            "2308.10737",
            baseline=True,
            dataset_name="CiteSeer",
            protocol_note="Planetoid fixed split",
        ),
        _result(
            "MLP",
            0.5,
            "valid-mlp",
            baseline=True,
            dataset_name="CiteSeer",
            protocol_note="Planetoid fixed split",
        ),
        _result(
            "GCN",
            0.8,
            "valid-method",
            dataset_name="CiteSeer",
            protocol_note="Planetoid fixed split",
        ),
    ]

    comparisons = compare_results(results, min_papers=1)

    assert len(comparisons) == 1
    assert comparisons[0]["mlp"]["value"] == 0.5
    assert comparisons[0]["paper_results"][0]["paper"] == "valid-method"


def test_compare_results_labels_legacy_and_replacement_heterophily_groups() -> None:
    results = []
    for dataset_name, benchmark_name, is_legacy in (
        ("LegacyNodes", "Heterophilic Graphs", True),
        ("ReplacementNodes", "Heterophily Benchmark", False),
    ):
        results.append(
            _result(
                "MLP",
                0.5,
                f"{dataset_name}-mlp",
                baseline=True,
                dataset_name=dataset_name,
                benchmark_name=benchmark_name,
                benchmark_is_legacy=is_legacy,
            )
        )
        results.append(
            _result(
                "GCN",
                0.6,
                f"{dataset_name}-gcn",
                dataset_name=dataset_name,
                benchmark_name=benchmark_name,
                benchmark_is_legacy=is_legacy,
            )
        )

    comparisons = compare_results(results, min_papers=1)

    assert {comparison["group"] for comparison in comparisons} == {
        "Heterophilic Graphs (legacy)",
        "Heterophily Benchmark (non-legacy)",
    }


def test_write_comparison_outputs_creates_json_csv_and_figure(tmp_path: Path) -> None:
    comparisons = compare_results(
        [_result("MLP", 0.5, "mlp-paper", baseline=True)]
        + [_result(f"Method-{i}", 0.6, f"paper-{i % 10}") for i in range(15)],
        min_papers=1,
    )

    paths = write_comparison_outputs(comparisons, tmp_path)
    figure_paths = write_comparison_figures(comparisons, tmp_path)

    assert all(path.exists() for path in (*paths, *figure_paths))
    assert paths[0].read_text(encoding="utf-8").startswith("[")
    assert "better_count" in paths[1].read_text(encoding="utf-8")


def test_mlp_comparison_uses_shared_semantic_colors() -> None:
    assert MLP_COMPARISON_COLORS == {
        "better": "#2F6690",
        "tied": "#F2A541",
        "worse": "#c43d4b",
    }
