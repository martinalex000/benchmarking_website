import json

import pytest

from experiments.table_provenance_experiment import compare_repetition_models as comparison
from experiments.table_provenance_experiment.compile_manual_validation import (
    compile_report,
    pdf_pages,
)


def test_pdf_pages_only_reports_normalized_verbatim_match():
    assert pdf_pages("We repeat five times", "Cover\fWe repeat\n five times\fEnd") == [2]
    assert pdf_pages("We repeat five times", "We rerun five times") == []


def test_compile_refuses_before_correction_review(tmp_path):
    (tmp_path / "manifest.json").write_text('{"papers":[]}')
    notes = tmp_path / "notes.json"
    notes.write_text('{"correction_review_complete":false}')
    with pytest.raises(ValueError, match="must finish"):
        compile_report(tmp_path, notes)
    assert not (tmp_path / "README.md").exists()


def test_unknown_agreement_does_not_justify_expansion_and_origins_are_separate(
    tmp_path, monkeypatch
):
    reference = tmp_path / "review.json"
    records = []
    for index in range(15):
        paper = str(index)
        folder = tmp_path / "papers" / paper
        folder.mkdir(parents=True)
        (folder / "analysis.json").touch()
        records.append({"paper_id": paper, "analysis": str(tmp_path / f"glm_{paper}.json")})
    reference.write_text(json.dumps({"records": records}))

    def summarize(path):
        return {
            "error": None,
            "tables": {"1": [("withheld", None, None, "unknown", "self_evaluated")]},
            "origins": {
                "1": [
                    {
                        "name": "Baseline",
                        "origin": "copied" if path.name.startswith("glm") else "self_evaluated",
                    }
                ]
            },
            "prompt_sha256": {"facts": "same", "verification": "same"},
        }

    monkeypatch.setattr(comparison, "summarize", summarize)
    result = comparison.compare(reference, tmp_path)
    assert result["agreement_fraction"] == 1
    assert result["copied_vs_self_origin_conflicts"] == 15
    assert not result["expansion_gate_passed"]


def test_variant_count_collapsing_does_not_change_accepted_count_set():
    protocol = ("accepted", 5, 10, "repeated_cv", "self_evaluated")
    assert comparison.accepted_protocols([protocol, protocol]) == [(5, 10, "repeated_cv")]
