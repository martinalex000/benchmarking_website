"""Unit tests for scripts.list_models reasoning checks."""

from scripts.list_models import _has_reasoning_trace, is_chat_model_for_reasoning_check


def test_is_chat_model_for_reasoning_check_skips_non_chat_models():
    assert not is_chat_model_for_reasoning_check("BAAI/bge-reranker-v2-m3")
    assert not is_chat_model_for_reasoning_check("openai/whisper-large-v3")
    assert not is_chat_model_for_reasoning_check("alias-reasoning")
    assert is_chat_model_for_reasoning_check("moonshotai/Kimi-K2.6")


def test_has_reasoning_trace_detects_reasoning_content():
    body = (
        '{"choices":[{"message":{"content":"OK","reasoning_content":"thinking..."}}]}'
    )
    assert _has_reasoning_trace(body)


def test_has_reasoning_trace_is_false_without_reasoning_fields():
    body = '{"choices":[{"message":{"content":"OK"}}]}'
    assert not _has_reasoning_trace(body)
