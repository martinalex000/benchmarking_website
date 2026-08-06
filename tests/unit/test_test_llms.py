"""Unit tests for scripts.test_llms reasoning checks."""

from scripts.test_llms import (
    _format_rate_limits,
    _has_reasoning_trace,
    is_chat_model_for_reasoning_check,
    metric_values,
)


def test_is_chat_model_for_reasoning_check_skips_non_chat_models():
    assert not is_chat_model_for_reasoning_check("BAAI/bge-reranker-v2-m3")
    assert not is_chat_model_for_reasoning_check("openai/whisper-large-v3")
    assert not is_chat_model_for_reasoning_check("alias-reasoning")
    assert is_chat_model_for_reasoning_check("moonshotai/Kimi-K2.6")


def test_has_reasoning_trace_detects_reasoning_content():
    body = '{"choices":[{"message":{"content":"OK","reasoning_content":"thinking..."}}]}'
    assert _has_reasoning_trace(body)


def test_has_reasoning_trace_is_false_without_reasoning_fields():
    body = '{"choices":[{"message":{"content":"OK"}}]}'
    assert not _has_reasoning_trace(body)


def test_format_rate_limits_reports_windows_and_burst():
    headers = {
        "x-ratelimit-limit-minute": "100",
        "x-ratelimit-remaining-minute": "97",
        "ratelimit-limit": "10",
        "ratelimit-remaining": "9",
        "ratelimit-reset": "2s",
    }

    formatted = _format_rate_limits(headers)

    assert "minute: 97/100" in formatted
    assert "burst: 9/10 reset=2s" in formatted


def test_format_rate_limits_handles_missing_headers():
    assert _format_rate_limits({}) == "not reported"


def test_metric_values_filters_by_metric_and_label():
    metrics = """
vllm:prompt_tokens_total{engine=\"0\"} 10
vllm:prompt_tokens_total{engine=\"1\"} 20
vllm:prompt_tokens_by_source_total{source=\"local_compute\"} 7
vllm:prompt_tokens_by_source_total{source=\"cache\"} 99
"""

    assert metric_values(metrics, "vllm:prompt_tokens_total") == [10.0, 20.0]
    assert metric_values(
        metrics,
        "vllm:prompt_tokens_by_source_total",
        'source="local_compute"',
    ) == [7.0]
