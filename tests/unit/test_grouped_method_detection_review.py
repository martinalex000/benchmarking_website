from experiments.extraction_validation.method_detection import compile_grouped_review as review
from experiments.extraction_validation.method_detection import prepare_review


def _method(name: str, datasets: tuple[str, ...]) -> prepare_review.MethodEvidence:
    return prepare_review.MethodEvidence(
        name=name,
        raw_names=(name,),
        datasets=datasets,
        table_refs=("Table 1",),
        dataset_table_pairs=tuple(f"{dataset} @ Table 1" for dataset in datasets),
        result_count=len(datasets),
        role="baseline",
        problematic_count=0,
    )


def test_render_group_separates_common_and_partial_methods() -> None:
    group = review.DatasetGroup(
        name="Citation networks",
        datasets=("Cora", "CiteSeer"),
        reason="Shared panel.",
    )
    raw_rows = [
        {"dataset": "Cora", "method": "GCN", "table_ref": "Table 1"},
        {"dataset": "Cora", "method": "GAT", "table_ref": "Table 1"},
        {"dataset": "CiteSeer", "method": "GCN", "table_ref": "Table 1"},
    ]

    markdown = "\n".join(review._render_group(1, group, raw_rows, [_method("GCN", ("Cora",))]))

    assert "Raw methods on every detected dataset:** `GCN`" in markdown
    assert "`GAT` — `Cora`" in markdown
    assert "Stored method names after filtering/normalization:** `GCN`" in markdown
    assert "**Missing methods:**" in markdown
    assert "**Detection / normalization comments:**" in markdown


def test_render_group_exposes_dataset_without_raw_rows() -> None:
    group = review.DatasetGroup(
        name="Anomaly detection",
        datasets=("Amazon", "YelpChi"),
        reason="Shared panel.",
    )

    markdown = "\n".join(
        review._render_group(
            1,
            group,
            [{"dataset": "Amazon", "method": "GCN", "table_ref": "Table 3"}],
            [],
        )
    )

    assert "Datasets with no raw result rows:** `YelpChi`" in markdown
