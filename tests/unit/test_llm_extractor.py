"""Unit tests for LLM extractor helpers (no actual LLM calls)."""

import pytest
from backend.llm_extractor import (
    ExtractionOutput,
    LLMExtractor,
    ProposedModel,
    ResultEntry,
    _render_human_readable,
    _split_into_chunks,
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
