"""Unit tests for LLM extractor helpers (no actual LLM calls)."""

from types import SimpleNamespace

import pytest

from backend.latex_source import _expand_user_macros
from backend.llm_client import LLMWallClockTimeout
from backend.llm_extractor import (
    BaselineModelInfo,
    CallRecord,
    DatasetInfo,
    DatasetList,
    ExtractionOutput,
    FigureInfo,
    LLMExtractor,
    ModelSizeEntry,
    ProposedModel,
    ResultEntry,
)
from backend.llm_metadata import _title_looks_corrupted
from backend.llm_postprocessing import (
    _apply_identified_proposed_model,
    _apply_sizes,
    _expand_extraction_payload,
    _extract_proposed_model_hint,
    _matches_proposed_model_name,
    _merge_extraction_outputs,
    _merge_size_entries,
    _normalise_known_model_qualifiers,
    _normalise_model_name_text,
    _rename_generic_proposed_rows,
    _render_human_readable,
    _split_into_chunks,
)
from backend.llm_tasks import (
    _dataset_checkpoint_fingerprint,
    _load_dataset_checkpoint,
    _prefer_method_acronym,
    _proposed_model_context,
    _save_dataset_checkpoint,
)


def test_split_into_chunks_small():
    text = "a" * 100
    chunks = _split_into_chunks(text, 200)
    assert len(chunks) == 1
    assert chunks[0] == text


def test_gemma_yaml_extraction_uses_compact_result_prompt():
    extractor = LLMExtractor.__new__(LLMExtractor)
    extractor.model_name = "google/gemma-4-31B-it"
    extractor.result_output_format = "yaml"

    prompt = extractor._read_result_prompt()

    assert "COLUMN GROUP GUIDE" in prompt
    assert "m: <exact model name>" in prompt
    assert "omit all other keys" in prompt


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


def test_dataset_checkpoint_round_trip_and_fingerprint_validation(tmp_path):
    output = ExtractionOutput(
        results=[ResultEntry(model="GNN", dataset="Cora", metric="Accuracy", value=0.81)]
    )
    fingerprint = _dataset_checkpoint_fingerprint(
        model_name="gemma",
        output_format="yaml",
        prompt="prompt",
        user_content="Cora context",
    )

    _save_dataset_checkpoint(
        tmp_path,
        "Cora",
        fingerprint=fingerprint,
        output=output,
    )

    loaded = _load_dataset_checkpoint(tmp_path, "Cora", fingerprint=fingerprint)
    assert loaded is not None
    assert loaded.results[0].value == pytest.approx(0.81)
    assert _load_dataset_checkpoint(tmp_path, "Cora", fingerprint="changed") is None


def test_streaming_call_enforces_total_wall_clock_timeout(monkeypatch):
    class FakeStream:
        def __init__(self):
            self.closed = False

        def __iter__(self):
            yield SimpleNamespace(usage=None, choices=[])

        def close(self):
            self.closed = True

    stream = FakeStream()
    create_calls = []

    def create(**kwargs):
        create_calls.append(kwargs)
        return stream

    extractor = object.__new__(LLMExtractor)
    extractor.model_name = "gemma"
    extractor.streaming = True
    extractor._call_log = []
    extractor._client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=create))
    )
    times = iter([0.0, 121.0, 122.0])
    monkeypatch.setattr("backend.llm_client.time.perf_counter", lambda: next(times))
    monkeypatch.setattr("backend.llm_client.cfg.llm_timeout", 120)

    with pytest.raises(LLMWallClockTimeout, match="120s"):
        extractor._call("system", "user")

    assert len(create_calls) == 1
    assert stream.closed is True


def test_screen_paper_can_raise_instead_of_failing_open(monkeypatch):
    extractor = object.__new__(LLMExtractor)
    extractor._progress_callback = None
    extractor._call_log = []
    monkeypatch.setattr(extractor, "_read_prompt", lambda _filename: "prompt")
    monkeypatch.setattr(
        extractor,
        "_call_json",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(RuntimeError("unavailable")),
    )

    with pytest.raises(RuntimeError, match="unavailable"):
        extractor.screen_paper("title", "abstract", fail_open=False)

    result = extractor.screen_paper("title", "abstract")
    assert result.has_benchmark_results is True
    assert result.has_new_benchmark is True


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
    assert merged.results[0].value == pytest.approx(0.61)


def test_merge_extraction_outputs_separates_mlp_feature_sources():
    merged = _merge_extraction_outputs(
        proposed_model=ProposedModel(name="Method"),
        baselines=[],
        results=[
            ResultEntry(
                model="MLP",
                dataset="Cora",
                metric="Accuracy",
                value=0.71,
                input_feature_source="raw_features",
            ),
            ResultEntry(
                model="MLP",
                dataset="Cora",
                metric="Accuracy",
                value=0.83,
                input_feature_source="llm_features",
                feature_source_evidence="BERT embeddings used for all baselines",
            ),
        ],
        confidence_levels=["HIGH"],
        notes_parts=[],
    )

    assert len(merged.results) == 2
    by_source = {result.input_feature_source: result for result in merged.results}
    assert by_source["raw_features"].model == "MLP"
    assert by_source["llm_features"].model == "MLP+LLM_features"


def test_mlp_name_is_not_renamed_for_non_llm_external_features():
    merged = _merge_extraction_outputs(
        proposed_model=ProposedModel(name="Method"),
        baselines=[],
        results=[
            ResultEntry(
                model="MLP (tuned)",
                dataset="Cora",
                metric="Accuracy",
                value=0.71,
                input_feature_source="other_external_features",
            ),
            ResultEntry(
                model="MLP+C&S",
                dataset="Cora",
                metric="Accuracy",
                value=0.8,
                input_feature_source="llm_features",
            ),
        ],
        confidence_levels=["HIGH"],
        notes_parts=[],
    )

    assert [result.model for result in merged.results] == ["MLP (tuned)", "MLP+C&S"]


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


def test_identified_proposed_model_resolves_our_variants_and_keeps_scientific_parentheses():
    extraction = ExtractionOutput(
        results=[
            ResultEntry(
                model="Our(GCN)",
                dataset="Wisconsin",
                metric="Accuracy",
                value=0.87,
            ),
            ResultEntry(
                model="Ours(3-hop)",
                dataset="Wisconsin",
                metric="Accuracy",
                value=0.88,
            ),
            ResultEntry(
                model="MLP (tuned)",
                dataset="Cora",
                metric="Accuracy",
                value=0.69,
            ),
            ResultEntry(
                model="SE(3)-DDM",
                dataset="QM9",
                metric="MAE",
                value=0.1,
            ),
        ]
    )

    _apply_identified_proposed_model(
        extraction,
        ProposedModel(
            name="FSGNN",
            supporting_sentence="We propose Feature Selection Graph Neural Network (FSGNN).",
        ),
    )

    assert [row.model for row in extraction.results] == ["FSGNN", "FSGNN", "MLP", "SE(3)-DDM"]
    assert [row.is_proposed for row in extraction.results] == [True, True, False, False]
    assert extraction.proposed_model is not None
    assert extraction.proposed_model.supporting_sentence.startswith("We propose")


def test_identified_hint_does_not_replace_explicit_proposed_model_name():
    extraction = ExtractionOutput(
        proposed_model=ProposedModel(name="Optimized GAE"),
        results=[
            ResultEntry(
                model="Optimized GAE",
                is_proposed=True,
                dataset="ogbl-ddi",
                metric="Hits@20",
                value=0.9443,
            )
        ],
    )

    _apply_identified_proposed_model(extraction, ProposedModel(name="MPNN"))

    assert extraction.proposed_model is not None
    assert extraction.proposed_model.name == "Optimized GAE"
    assert extraction.results[0].model == "Optimized GAE"


def test_tuned_qualifier_normalization_is_specific():
    assert _normalise_known_model_qualifiers("MLP (tuned)") == "MLP"
    assert _normalise_known_model_qualifiers("SE(3)-DDM") == "SE(3)-DDM"


def test_proposed_model_context_contains_name_and_evidence():
    context = _proposed_model_context(
        ProposedModel(name="A-DGN", supporting_sentence="We call our method A-DGN.")
    )
    assert "Paper-defined proposed model: A-DGN" in context
    assert "Supporting sentence: We call our method A-DGN." in context


def test_prefer_method_acronym_uses_explicit_paper_abbreviation():
    assert (
        _prefer_method_acronym(
            "Anti-Symmetric Deep Graph Network",
            "We present Anti-Symmetric Deep Graph Networks (A-DGNs).",
        )
        == "A-DGN"
    )
    assert _prefer_method_acronym("SE(3)-DDM", "We compare SE(3)-DDM.") == "SE(3)-DDM"


def test_deterministic_table_matching_uses_caption_header_and_body_and_fuzzy_fallback():
    tables = [
        SimpleNamespace(number=3, caption="Results for the Actor benchmark", header=[], body=""),
        SimpleNamespace(number=4, caption="Results for Roman Empire", header=[], body=""),
        SimpleNamespace(
            number=6,
            caption="Main benchmark results",
            header=["Dataset", "Actor", "Accuracy"],
            body="GCN | 0.82",
        ),
    ]

    numbers, fields = LLMExtractor._deterministic_table_matches("Actor", tables)

    assert numbers == [3, 6]
    assert fields == {3: ["caption"], 6: ["header"]}

    fuzzy_table = SimpleNamespace(number=7, caption="Results for Peptid-func", header=[], body="")
    assert LLMExtractor._deterministic_table_matches("Peptides-func", [fuzzy_table])[0] == [7]


@pytest.mark.parametrize(
    ("dataset_name", "table_label"),
    [
        ("ogbg-molpcba", "OGB-MolPCBA"),
        ("ogbn-products", "ogb-products"),
        ("ogbl-citation2", "Citation2"),
        ("ogbt-example", "ogbx-example"),
    ],
)
def test_deterministic_table_matching_accepts_ogb_naming_variants(dataset_name, table_label):
    table = SimpleNamespace(number=1, caption="", header=[table_label], body="")

    numbers, fields = LLMExtractor._deterministic_table_matches(dataset_name, [table])

    assert numbers == [1]
    assert fields == {1: ["header"]}


def test_normal_extraction_context_includes_grouped_column_guide_and_raw_table():
    table_body = r"""
        \begin{tabular}{@{}l|cc|cc@{}}
        \toprule
        Dataset & \multicolumn{2}{c|}{Cora} & \multicolumn{2}{c}{ogbn-papers100M} \\
        Metric & Acc & Time & Acc & Time \\
        \midrule
        SGC & 85.8 & 0.13 & 63.3 & 19212 \\
        \bottomrule
        \end{tabular}
    """
    table = SimpleNamespace(
        number=1,
        caption="Main benchmark results",
        body=table_body,
        markdown=table_body,
        label="tab:main",
    )

    context, _ = LLMExtractor._build_rag_context(
        "The experiments use the standard split.",
        [table],
        "ogbn-papers100M",
        already_selected=True,
    )

    guide_start = context.index("=== COLUMN GROUP GUIDE")
    raw_table_start = context.index("\\begin{tabular}")
    assert guide_start < raw_table_start
    assert "dataset 'ogbn-papers100M'" in context
    assert "63.3" in context


def test_small_table_sets_pass_all_tables_without_selection(monkeypatch):
    extractor = LLMExtractor()
    tables = [
        SimpleNamespace(number=3, caption="Actor results", header=[], body=""),
        SimpleNamespace(number=4, caption="Roman Empire results", header=[], body=""),
        SimpleNamespace(number=5, caption="Appendix results", header=[], body=""),
    ]

    def fail_call_json(*_args, **_kwargs):
        raise AssertionError("selector was called")

    monkeypatch.setattr(extractor, "_call_json", fail_call_json)

    assert extractor.select_tables_for_dataset("Actor", tables) == tables
    selected = extractor.select_tables_for_all_datasets([DatasetInfo(name="Actor")], tables)
    assert selected["Actor"] == tables
    assert "all 3 tables passed directly" in extractor._last_table_selection_rationales["Actor"]


def test_table_selection_falls_back_to_deterministic_matches_and_records_metadata(monkeypatch):
    extractor = LLMExtractor()
    tables = [
        SimpleNamespace(number=3, caption="Actor results", header=[], body=""),
        SimpleNamespace(number=4, caption="Roman Empire results", header=[], body=""),
        SimpleNamespace(number=5, caption="Other results", header=[], body=""),
        SimpleNamespace(number=6, caption="More results", header=[], body=""),
        SimpleNamespace(number=7, caption="Appendix", header=[], body=""),
    ]

    def fake_call_json(*_args, **_kwargs):
        extractor._call_log.append(
            CallRecord(call_type="select_tables:all", system_prompt="", user_content="")
        )
        return {"Actor": []}

    monkeypatch.setattr(extractor, "_call_json", fake_call_json)
    selected = extractor.select_tables_for_all_datasets([DatasetInfo(name="Actor")], tables)

    assert [table.number for table in selected["Actor"]] == [3]
    assert extractor._call_log[-1].extra["deterministic_table_matches"] == {"Actor": [3]}


def test_unexplained_nonmatching_selection_is_discarded_but_explained_override_is_allowed(
    monkeypatch,
):
    extractor = LLMExtractor()
    tables = [
        SimpleNamespace(number=3, caption="Actor results", header=[], body=""),
        SimpleNamespace(number=4, caption="Roman Empire results", header=[], body=""),
        SimpleNamespace(number=5, caption="Other results", header=[], body=""),
        SimpleNamespace(number=6, caption="More results", header=[], body=""),
        SimpleNamespace(number=7, caption="Appendix", header=[], body=""),
    ]
    responses = iter(
        [
            {"Actor": {"relevant_table_numbers": [4], "explanation": ""}},
            {
                "Actor": {
                    "relevant_table_numbers": [4],
                    "explanation": "The caption is omitted because this is the Actor table.",
                }
            },
        ]
    )

    monkeypatch.setattr(extractor, "_call_json", lambda *_args, **_kwargs: next(responses))
    assert (
        extractor.select_tables_for_all_datasets([DatasetInfo(name="Actor")], tables)["Actor"] == []
    )
    assert extractor.select_tables_for_all_datasets([DatasetInfo(name="Actor")], tables)[
        "Actor"
    ] == [tables[1]]


def test_small_table_sets_extract_tables_without_dataset_name_match(monkeypatch):
    extractor = LLMExtractor()
    extracted_tables = []

    monkeypatch.setattr(extractor, "_read_result_prompt", lambda *_args, **_kwargs: "prompt")

    def fake_extract(*_args, **kwargs):
        extracted_tables.append(kwargs["ds_tables"])
        return ExtractionOutput()

    monkeypatch.setattr(extractor, "_extract_dataset_with_retries", fake_extract)
    table = SimpleNamespace(number=1, caption="Results for Roman Empire", markdown="scores")
    output = extractor.extract_results_two_step(
        "paper text",
        [table],
        known_datasets=[DatasetInfo(name="Actor")],
    )

    assert output.results == []
    assert extracted_tables == [[table]]


def test_single_pass_dataset_extraction_keeps_experiment_context(monkeypatch):
    extractor = LLMExtractor()
    captured: list[str] = []

    def fake_extract(_prompt, content, **_kwargs):
        captured.append(content)
        return ExtractionOutput()

    monkeypatch.setattr(extractor, "_extract_results_chunk", fake_extract)
    monkeypatch.setattr(extractor, "_fire_progress", lambda: None)

    extractor._extract_dataset_with_retries(
        "prompt",
        dataset_name="CiteSeer",
        ds_tables=[SimpleNamespace(caption="CiteSeer results", markdown="scores")],
        focus_prefix="FOCUS\n",
        full_context="EXPERIMENT PROSE: this is a clustering task\nTABLE: scores",
        rag_stats={},
        call_type="extract_dataset:CiteSeer",
        max_table_chars=1_000,
        single_pass=True,
    )

    assert len(captured) == 1
    assert "this is a clustering task" in captured[0]


def test_dataset_focus_prefix_contains_selection_rationale_rules():
    extractor = LLMExtractor()
    prefix = extractor._dataset_focus_prefix(
        "Actor",
        intro_model_hint=None,
        identified_proposed_model=None,
        metric_constraint="",
        selection_rationale="Actor appears in tables: 3\nMODEL SELECTION EXPLANATION: renamed table",
    )
    assert "extract only explicit entries" in prefix.lower()
    assert "return no results" in prefix.lower()
    assert "do not copy" in prefix.lower()
    assert "MODEL SELECTION EXPLANATION: renamed table" in prefix


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
        main_tex="",
        sections=[],
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
        "backend.llm_tasks._ripgrep_dataset_name_hits",
        lambda text, source_path=None, limit=80: ["ZINC"],
    )
    monkeypatch.setattr(extractor, "_read_result_prompt", lambda full_mode=False: "prompt")
    monkeypatch.setattr(
        extractor,
        "_build_rag_context",
        lambda rag_text, ds_tables, ds_name, already_selected=False, **_kwargs: (
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

    def fake_extract_results_chunk(
        prompt: str,
        text: str,
        call_type: str = "extract_results",
        max_tokens: int | None = None,
    ):
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
    assert result.results == []
    assert "No tables were selected" in result.extraction_notes


def test_extract_results_chunk_falls_back_between_yaml_and_json(monkeypatch):
    extractor = LLMExtractor(result_output_format="yaml")
    call_formats: list[str] = []

    def fake_call_structured(
        prompt: str,
        text: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
        output_format: str = "json",
    ):
        call_formats.append(output_format)
        if output_format == "yaml":
            raise ValueError("yaml parse failed")
        return {
            "proposed_model": {"name": "GraphGPS"},
            "baseline_models": [],
            "results": [
                {
                    "model": "GraphGPS",
                    "is_proposed": True,
                    "dataset": "Peptides-func",
                    "metric": "AP",
                    "value": 0.6535,
                    "higher_is_better": True,
                }
            ],
            "extraction_confidence": "HIGH",
            "extraction_notes": "json fallback",
        }

    monkeypatch.setattr(extractor, "_call_structured", fake_call_structured)

    result = extractor._extract_results_chunk("prompt", "paper text", call_type="extract_dataset")

    assert call_formats == ["yaml", "json"]
    assert result.proposed_model is not None
    assert result.proposed_model.name == "GraphGPS"
    assert result.results[0].dataset == "Peptides-func"


def test_extract_results_chunk_does_not_retry_format_after_transport_timeout(monkeypatch):
    extractor = LLMExtractor(result_output_format="yaml")
    call_formats: list[str] = []

    def fake_call_structured(*_args, output_format="json", **_kwargs):
        call_formats.append(output_format)
        raise LLMWallClockTimeout("timed out")

    monkeypatch.setattr(extractor, "_call_structured", fake_call_structured)

    with pytest.raises(LLMWallClockTimeout, match="timed out"):
        extractor._extract_results_chunk("prompt", "paper text")

    assert call_formats == ["yaml"]


def test_extract_results_chunk_wraps_top_level_result_rows(monkeypatch):
    extractor = LLMExtractor(result_output_format="json")

    monkeypatch.setattr(
        extractor,
        "_call_structured",
        lambda *_args, **_kwargs: [
            {
                "model": "GraphGPS",
                "dataset": "Cora",
                "metric": "Accuracy",
                "value": 0.81,
            }
        ],
    )

    result = extractor._extract_results_chunk("prompt", "paper text", call_type="extract_dataset")

    assert len(result.results) == 1
    assert result.results[0].dataset == "Cora"
    assert result.results[0].value == pytest.approx(0.81)


def test_apply_sizes_merges_proposed_and_baselines():
    extraction = ExtractionOutput(
        proposed_model=ProposedModel(name="GraphGPS"),
        baseline_models=[BaselineModelInfo(name="GINE + RWSE")],
        results=[],
    )
    sizes = [
        ModelSizeEntry(
            model_name="GraphGPS (ours)",
            matched_result_name="GraphGPS",
            params_millions=6.9,
        ),
        ModelSizeEntry(
            model_name="GINE+RWSE",
            matched_result_name="GINE + RWSE",
            params_millions=2.1,
        ),
    ]
    _apply_sizes(extraction, sizes)
    assert extraction.proposed_model.params_millions == pytest.approx(6.9)
    assert extraction.baseline_models[0].params_millions == pytest.approx(2.1)


def test_merge_size_entries_prefers_existing_then_fills_gaps():
    primary = [ModelSizeEntry(model_name="GraphGPS", params_millions=6.9)]
    secondary = [
        ModelSizeEntry(model_name="GraphGPS", params_exact=6_900_000),
        ModelSizeEntry(model_name="GCN", params_millions=1.2),
    ]
    merged = _merge_size_entries(primary, secondary)
    by_name = {entry.model_name.lower(): entry for entry in merged}
    assert by_name["graphgps"].params_millions == pytest.approx(6.9)
    assert by_name["graphgps"].params_exact == 6_900_000
    assert by_name["gcn"].params_millions == pytest.approx(1.2)


def test_merge_size_entries_keeps_dataset_specific_counts_separate():
    entries = _merge_size_entries(
        [
            ModelSizeEntry(
                model_name="GatedGCN-VN",
                dataset="LRGB",
                params_millions=0.5,
            )
        ],
        [
            ModelSizeEntry(
                model_name="GatedGCN-VN",
                dataset="ogbg-molpcba",
                params_millions=57.0,
            )
        ],
    )

    assert {(entry.dataset, entry.params_millions) for entry in entries} == {
        ("LRGB", 0.5),
        ("ogbg-molpcba", 57.0),
    }


def test_expand_extraction_payload_includes_compact_model_metadata():
    expanded = _expand_extraction_payload(
        {
            "proposed_model_name": "GraphGPS",
            "proposed_model_type": "hybrid",
            "proposed_params_millions": 6.9,
            "baseline_model_names": ["GCN"],
            "baseline_model_types": {"GCN": "gnn"},
            "baseline_params_millions": {"GCN": 1.2},
            "results": [],
            "confidence": "HIGH",
            "notes": "",
        }
    )
    assert expanded["proposed_model"]["model_type"] == "hybrid"
    assert expanded["proposed_model"]["params_millions"] == pytest.approx(6.9)
    assert expanded["baseline_models"][0]["model_type"] == "gnn"
    assert expanded["baseline_models"][0]["params_millions"] == pytest.approx(1.2)
