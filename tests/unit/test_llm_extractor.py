"""Unit tests for LLM extractor helpers (no actual LLM calls)."""

import pytest
from backend.llm_extractor import (
    ExtractionOutput,
    LLMExtractor,
    ProposedModel,
    ResultEntry,
    BaselineModelInfo,
    _merge_extraction_outputs,
    _render_human_readable,
    _split_into_chunks,
    _title_looks_corrupted,
    FigureInfo,
)


def test_split_into_chunks_small():
    text = "a" * 100
    chunks = _split_into_chunks(text, 200)
    assert len(chunks) == 1
    assert chunks[0] == text


def test_split_into_chunks_large():
    paragraphs = ["word " * 50] * 20
    text = "\n\n".join(paragraphs)
    chunks = _split_into_chunks(text, 300)
    assert len(chunks) > 1
    for chunk in chunks:
        assert len(chunk) <= 300 + 300  # allow slight overshoot at boundary


def test_render_human_readable_basic():
    results_out = ExtractionOutput(
        proposed_model=ProposedModel(name="GraphGPS", params_millions=6.9),
        results=[
            ResultEntry(
                model="GraphGPS",
                is_proposed=True,
                dataset="Peptides-func",
                metric="AP",
                value=0.6535,
                std=0.004,
                higher_is_better=True,
            ),
            ResultEntry(
                model="GCN",
                is_proposed=False,
                dataset="Peptides-func",
                metric="AP",
                value=0.5930,
                higher_is_better=True,
            ),
        ],
        extraction_confidence="HIGH",
        extraction_notes="Clean tables.",
    )
    figure_out = FigureInfo(figure_id="Figure 1", caption_snippet="Architecture overview")
    md = _render_human_readable(
        arxiv_id="2206.08164",
        title="LRGB Paper",
        model_name="openai-gpt-oss120b",
        results_out=results_out,
        figure_out=figure_out,
        extraction_strategy="two-step",
        result_output_format="yaml",
        experiment_label=None,
        usage_summary={},
    )
    assert "GraphGPS" in md
    assert "6.9M params" in md
    assert "Peptides-func" in md
    assert "0.6535" in md
    assert "overrides.yaml" in md


def test_result_entry_coerces_string_value():
    r = ResultEntry(model="M", dataset="D", metric="AP", value="0.653")
    assert r.value == pytest.approx(0.653)


def test_result_entry_coerces_none_std():
    r = ResultEntry(model="M", dataset="D", metric="AP", value=0.5, std=None)
    assert r.std is None


def test_merge_extraction_outputs_dedupes_and_normalizes():
    merged = _merge_extraction_outputs(
        proposed_model=ProposedModel(name="GraphGPS"),
        baselines=[
            BaselineModelInfo(name="GCN"),
            BaselineModelInfo(name="gcn"),
        ],
        results=[
            ResultEntry(model="GCN", dataset="Peptides-func", metric="Test AP", value=0.6),
            ResultEntry(model="GCN", dataset="Peptides-func", metric="AP", value=0.61),
            ResultEntry(model="GraphGPS", dataset="Peptides-func", metric="Val AP", value=0.7),
        ],
        confidence_levels=["HIGH", "MEDIUM"],
        notes_parts=["part one", "part two"],
        normalise_metrics=True,
    )

    assert merged.extraction_confidence == "MEDIUM"
    assert merged.extraction_notes == "part one\npart two"
    assert [baseline.name for baseline in merged.baseline_models] == ["GCN"]
    assert len(merged.results) == 1
    assert merged.results[0].metric == "AP"
    assert merged.results[0].value == pytest.approx(0.6)


@pytest.mark.parametrize(
    ("title", "expected"),
    [
        (None, True),
        ("", True),
        ("arXiv:2401.17791", True),
        (": Broken Title", True),
        ("Graph\\Learning", True),
        ("Graph Learning: Benchmarks", False),
    ],
)
def test_title_looks_corrupted(title, expected):
    assert _title_looks_corrupted(title) is expected
