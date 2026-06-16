"""Tests for caption-driven model variant merging during stabilization."""

from backend.llm_extractor import ExtractionOutput, ResultEntry, _stabilize_model_names


class _FakeTable:
    def __init__(self, number: int, caption: str) -> None:
        self.number = number
        self.caption = caption


def test_stabilize_merges_graphgps_variants_from_caption():
    extraction = ExtractionOutput(
        results=[
            ResultEntry(
                model="GraphGPS",
                dataset="Cora",
                metric="Accuracy",
                value=0.9119,
                table_ref="Table 2",
            ),
            ResultEntry(
                model="GraphGPS*",
                dataset="Cora",
                metric="Accuracy",
                value=0.9179,
                table_ref="Table 2",
            ),
        ],
    )
    tables = [
        _FakeTable(
            2,
            "* indicates our implementation, while other results are taken from [12, 76].",
        )
    ]
    _stabilize_model_names(extraction, tables=tables)
    assert len(extraction.results) == 1
    assert extraction.results[0].model == "GraphGPS"
    assert extraction.results[0].value == 0.9179
