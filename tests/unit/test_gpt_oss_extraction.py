"""Unit tests for gpt-oss-specific extraction helpers."""

from types import SimpleNamespace

from backend.llm_extractor import LLMExtractor
from backend.llm_model_options import (
    context_limits_for_model,
    extraction_max_tokens_for_model,
    is_gpt_oss_model,
)
from backend.llm_postprocessing import _sanitize_text


def test_is_gpt_oss_model_aliases():
    assert is_gpt_oss_model("openai-gpt-oss-120b")
    assert is_gpt_oss_model("openai-gpt-oss120b")
    assert not is_gpt_oss_model("glm-4.7")


def test_context_limits_for_gpt_oss_are_tighter():
    text_limit, table_limit = context_limits_for_model("openai-gpt-oss-120b")
    assert text_limit < 10_000
    assert table_limit < 10_000
    default_text, default_table = context_limits_for_model("glm-4.7")
    assert default_text == 10_000
    assert default_table == 10_000


def test_extraction_max_tokens_for_gpt_oss():
    assert extraction_max_tokens_for_model("openai-gpt-oss-120b") == 50_000
    assert extraction_max_tokens_for_model("glm-4.7") == 50_000


def test_sanitize_text_strips_control_chars():
    dirty = "valid\x0ctext\x1fmore"
    assert _sanitize_text(dirty) == "validtextmore"


def test_build_rag_context_sanitizes_table_markdown():
    table = SimpleNamespace(
        number=3,
        label="tab:cora-results",
        caption="Results",
        markdown="GCN\x0c | 0.85",
    )
    context, stats = LLMExtractor._build_rag_context(
        "Intro mentions Cora dataset.\n\nTable~3 uses the standard node split.\n\n"
        "This paragraph discusses unrelated link prediction.\n\n",
        [table],
        "Cora",
        max_text_chars=1000,
        max_table_chars=1000,
    )
    assert "\x0c" not in context
    assert "0.85" in context
    assert "standard node split" in context
    assert stats["dataset"] == "Cora"


def test_build_rag_context_puts_selection_reasoning_before_table():
    table = SimpleNamespace(number=3, caption="Results", markdown="| Cham. | 0.85 |")
    context, _ = LLMExtractor._build_rag_context(
        "The paper defines Chameleon as the target dataset.",
        [table],
        "Chameleon",
        max_text_chars=1000,
        max_table_chars=1000,
        already_selected=True,
        selection_rationale="Table 3 reports the Chameleon benchmark; its abbreviated column is Cham.",
    )
    assert context.index("Table 3 reports the Chameleon benchmark") < context.index("| Cham. |")


def test_build_tables_only_context():
    table = SimpleNamespace(caption="T1", markdown="| m | 1 |")
    ctx = LLMExtractor._build_tables_only_context([table], max_table_chars=500)
    assert "TABLES" in ctx
    assert "| m | 1 |" in ctx
