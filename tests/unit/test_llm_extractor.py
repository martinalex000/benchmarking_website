"""Unit tests for LLM extractor helpers (no actual LLM calls)."""

from types import SimpleNamespace

import pytest

from backend.latex_source import _expand_user_macros
from backend.llm_extractor import (
    BaselineModelInfo,
    DatasetInfo,
    DatasetList,
    ExtractionOutput,
    FigureInfo,
    LLMExtractor,
    ProposedModel,
    ResultEntry,
    _extract_proposed_model_hint,
    _matches_proposed_model_name,
    _merge_extraction_outputs,
    _normalise_model_name_text,
    _rename_generic_proposed_rows,
    _render_human_readable,
    _split_into_chunks,
    _title_looks_corrupted,
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


def test_expand_user_macros_supports_zero_arg_unbraced_newcommand():
    tex, macro_map = _expand_user_macros(
        r"\newcommand\modelname[0]{FPS-T}\nThe method is \modelname{}."
    )

    assert macro_map["modelname"] == "FPS-T"
    assert "FPS-T{}" in tex or "FPS-T" in tex


def test_extract_proposed_model_hint_prefers_title_prefix():
    hint = _extract_proposed_model_hint(
        "GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal Architecture",
        "We compare our method against GraphGPS and GIN.",
    )

    assert hint == "GraphMinNet"


def test_extract_proposed_model_hint_prefers_short_abbreviation_from_intro():
    hint = _extract_proposed_model_hint(
        "Curve Your Attention: Mixed-Curvature Transformers for Graph Representation Learning",
        "The resulting model, which we name as Fully Product-Stereographic Transformer (FPS-T), takes advantage of long-range interactions.",
    )

    assert hint == "FPS-T"


def test_normalise_model_name_text_converts_common_greek_to_unicode():
    assert _normalise_model_name_text(r"G-\DeltaUQ") == "G-ΔUQ"
    assert _normalise_model_name_text(r"\kappa-GCN") == "κ-GCN"


def test_matches_proposed_model_name_accepts_variant_rows():
    assert _matches_proposed_model_name("GCN + RandAlign", "RandAlign") is True
    assert _matches_proposed_model_name("LargeGT-local", "LargeGT") is True
    assert _matches_proposed_model_name("PIGN + GCN", "PIGN") is True


def test_rename_generic_proposed_rows_uses_intro_hint():
    extraction = ExtractionOutput(
        proposed_model=ProposedModel(name="Ours"),
        results=[
            ResultEntry(
                model="Ours", is_proposed=True, dataset="MNIST", metric="Accuracy", value=0.9
            ),
            ResultEntry(
                model="GCN", is_proposed=False, dataset="MNIST", metric="Accuracy", value=0.8
            ),
        ],
    )

    _rename_generic_proposed_rows(extraction, "GraphMinNet")

    assert extraction.proposed_model is not None
    assert extraction.proposed_model.name == "GraphMinNet"
    assert extraction.results[0].model == "GraphMinNet"


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


def test_extract_results_two_step_retries_after_empty_latex_discovery(monkeypatch):
    extractor = LLMExtractor()
    fallback_calls: list[tuple[str, str]] = []

    latex_paper = SimpleNamespace(
        tables=[],
        experiment_text="We evaluate CRAWL on ZINC and a subgraph counting task.",
        intro_text="",
        all_table_captions="Performance on ZINC and subgraph counting.",
        section_headings="Experiments\nAppendix Results",
    )

    monkeypatch.setattr(
        extractor,
        "discover_datasets_from_latex",
        lambda paper: DatasetList(),
    )

    def fake_discover_datasets(paper_text: str, tables_text: str) -> DatasetList:
        fallback_calls.append((paper_text, tables_text))
        return DatasetList(
            datasets=[
                DatasetInfo(name="subgraph counting"),
                DatasetInfo(name="ZINC"),
            ]
        )

    monkeypatch.setattr(extractor, "discover_datasets", fake_discover_datasets)
    monkeypatch.setattr(
        "backend.llm_extractor._ripgrep_dataset_name_hits",
        lambda text, source_path=None, limit=80: ["ZINC"],
    )
    monkeypatch.setattr(extractor, "_read_result_prompt", lambda full_mode=False: "prompt")
    monkeypatch.setattr(
        extractor,
        "_build_rag_context",
        lambda rag_text, ds_tables, ds_name, already_selected=False: (
            f"context for {ds_name}",
            {
                "paragraphs_selected": 1,
                "paragraphs_total": 1,
                "tables_selected": 0,
                "tables_total": 0,
                "table_selection_mode": "all",
                "context_total_chars": 10,
            },
        ),
    )

    def fake_extract_results_chunk(prompt: str, text: str, call_type: str = "extract_results"):
        dataset = text.split('FOCUS: Extract results ONLY for the dataset "', 1)[1].split('".', 1)[
            0
        ]
        return ExtractionOutput(
            results=[
                ResultEntry(
                    model="CRAWL", is_proposed=True, dataset=dataset, metric="AP", value=0.8
                )
            ]
        )

    monkeypatch.setattr(extractor, "_extract_results_chunk", fake_extract_results_chunk)

    result = extractor.extract_results_two_step(
        paper_text="CRAWL evaluates on ZINC.",
        tables=[],
        latex_paper=latex_paper,
    )

    assert len(fallback_calls) == 1
    assert {entry.dataset for entry in result.results} == {"ZINC", "subgraph counting"}
    assert result.extraction_notes != "Dataset discovery returned no datasets."
