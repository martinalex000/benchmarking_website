"""Regression tests for multi-task LRGB extraction safeguards."""

from __future__ import annotations

from backend.llm_types import ExtractionOutput, ResultEntry


def test_protocol_decision_is_tri_state_and_coverage_is_explicit():
    output = ExtractionOutput(
        coverage_assessment="complete",
        results=[
            ResultEntry(
                model="GCN",
                dataset="Peptides-func",
                metric="AP",
                value=0.59,
                protocol_decision="standard",
            ),
            ResultEntry(
                model="GCN-LP",
                dataset="Peptides-func",
                metric="AP",
                value=0.40,
                protocol_decision="nonstandard",
            ),
        ],
    )

    assert output.coverage_assessment == "complete"
    assert {row.protocol_decision for row in output.results} == {"standard", "nonstandard"}
