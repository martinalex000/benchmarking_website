"""Unit tests for scripts.test_llms reasoning checks."""

from backend.config import cfg
from scripts import test_llms
from scripts.test_llms import (
    _format_rate_limits,
    _has_reasoning_trace,
    _resolve_api_target,
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


def test_api_key_env_uses_named_key_and_configured_endpoint(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY_SECOND", "test-key")
    monkeypatch.setattr(cfg, "llm_endpoint", "https://api.example/v1")

    assert _resolve_api_target(None, None, None, "LLM_API_KEY_SECOND") == (
        "https://api.example/v1",
        "test-key",
    )


def test_ping_cli_routes_with_named_endpoint_and_key(monkeypatch):
    monkeypatch.setenv("LLM_ENDPOINT2", "https://api2.example/v1")
    monkeypatch.setenv("LLM_API_KEY2", "test-key-2")
    captured = {}

    def fake_run_check(**kwargs):
        captured.update(kwargs)
        return 0

    monkeypatch.setattr(test_llms, "_run_check", fake_run_check)

    assert (
        test_llms.main(
            [
                "ping",
                "example-model",
                "--endpoint-env",
                "LLM_ENDPOINT2",
                "--api-key-env",
                "LLM_API_KEY2",
                "--rate-limit",
            ]
        )
        == 0
    )
    assert captured == {
        "endpoint": "https://api2.example/v1",
        "api_key": "test-key-2",
        "ping": True,
        "model_ids": ["example-model"],
        "rate_limits": True,
    }


def test_api_key_env_requires_a_configured_key(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY_SECOND", raising=False)

    try:
        _resolve_api_target(None, None, None, "LLM_API_KEY_SECOND")
    except ValueError as exc:
        assert "LLM_API_KEY_SECOND" in str(exc)
    else:
        raise AssertionError("Expected a missing environment variable to fail")


def test_api_key_override_requires_endpoint(monkeypatch):
    monkeypatch.setattr(cfg, "llm_endpoint", "")

    try:
        _resolve_api_target(None, None, "test-key", None)
    except ValueError as exc:
        assert "requires --endpoint" in str(exc)
    else:
        raise AssertionError("Expected an endpoint requirement to fail")


def test_endpoint_env_requires_a_configured_endpoint(monkeypatch):
    monkeypatch.delenv("LLM_ENDPOINT2", raising=False)

    try:
        _resolve_api_target(None, "LLM_ENDPOINT2", None, None)
    except ValueError as exc:
        assert "LLM_ENDPOINT2" in str(exc)
    else:
        raise AssertionError("Expected a missing endpoint variable to fail")


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
