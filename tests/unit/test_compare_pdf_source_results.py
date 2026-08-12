from backend.llm_extractor import ExtractionOutput, ResultEntry
from experiments.marker_docling_bakeoff.compare_source_results import compare_outputs


def test_compare_outputs_reports_strict_and_method_agnostic_matches() -> None:
    reference = ExtractionOutput(
        results=[
            ResultEntry(model="Proposed", dataset="Cora", metric="Accuracy", value=91.0),
            ResultEntry(model="GCN", dataset="Cora", metric="Accuracy", value=80.0),
        ]
    )
    candidate = ExtractionOutput(
        results=[
            ResultEntry(model="New name", dataset="Cora", metric="Accuracy", value=0.91),
            ResultEntry(model="GCN", dataset="Cora", metric="Accuracy", value=79.0),
            ResultEntry(model="Extra", dataset="Cora", metric="Accuracy", value=70.0),
        ]
    )

    stats = compare_outputs(reference, candidate)

    assert stats.reference_rows == 2
    assert stats.candidate_rows == 3
    assert stats.matching_keys == 1
    assert stats.matching_values == 0
    assert stats.value_mismatches == 1
    assert stats.missing_keys == 1
    assert stats.extra_keys == 2
    assert stats.relaxed_value_matches == 1
    assert stats.strict_recall == 0
    assert stats.relaxed_recall == 0.5
