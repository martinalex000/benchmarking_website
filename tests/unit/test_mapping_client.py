from types import SimpleNamespace

import pytest

from backend import llm_tasks
from backend.llm_backends import LlmBackend, ModelRoute
from backend.mapping import client as mapping
from backend.repetition_extractor import DEFAULT_MODEL


def test_explicit_route_does_not_probe_or_resolve_models(monkeypatch):
    monkeypatch.setattr(llm_tasks.cfg, "model_for_tier", lambda tier: tier)
    monkeypatch.setattr(
        llm_tasks,
        "client_params_for_model",
        lambda model: pytest.fail("Unexpected model discovery"),
    )
    monkeypatch.setattr(llm_tasks, "OpenAI", lambda **kwargs: SimpleNamespace(**kwargs))
    route = ModelRoute(DEFAULT_MODEL, LlmBackend("external", "https://example.invalid/v1", "none"))
    client = llm_tasks.LLMExtractor(model_tier=DEFAULT_MODEL, model_route=route)
    assert client.model_name == DEFAULT_MODEL
    assert client._client.base_url == route.backend.endpoint
    assert client._model_route == route
    with pytest.raises(ValueError, match="does not match"):
        llm_tasks.LLMExtractor(model_tier="wrong", model_route=route)


def test_mapping_client_uses_glm_thinking_large_budget_and_shared_gate(monkeypatch):
    captured = {}

    def fake(**kwargs):
        captured.update(kwargs)
        return SimpleNamespace(_client=SimpleNamespace(with_options=lambda **options: options))

    monkeypatch.setattr(mapping, "LLMExtractor", fake)
    route = ModelRoute(DEFAULT_MODEL, LlmBackend("external", "https://example.invalid/v1", "none"))
    monkeypatch.setattr(mapping, "external_glm_route", lambda: route)
    gate = object()
    client = mapping.mapping_client(gate)
    assert captured["model_tier"] == DEFAULT_MODEL
    assert captured["enable_reasoning"] is True
    assert captured["max_total_tokens"] == 1_000_000
    assert client.request_gate is gate
    assert client.request_timeout_seconds == 1800
    assert client.request_read_timeout_seconds == 1800
    assert client._client == {"timeout": 1800, "max_retries": 0}


def test_deepseek_route_uses_the_configured_external_endpoint(monkeypatch):
    monkeypatch.setattr(mapping.cfg, "llm_endpoint", "https://llm.example/v1")
    monkeypatch.setattr(mapping.cfg, "llm_api_key", "test-key")

    route = mapping.mapping_route(mapping.DEEPSEEK_FLASH_MODEL)

    assert route.model_id == mapping.DEEPSEEK_FLASH_MODEL
    assert route.backend.endpoint == "https://llm.example/v1"
    assert route.backend.api_key == "test-key"
    with pytest.raises(ValueError, match="Unsupported mapping model"):
        mapping.mapping_route("another/model")


def test_second_glm_flash_key_keeps_provider_model_name_and_own_credentials(monkeypatch):
    monkeypatch.setattr(mapping.cfg, "llm_endpoint", "https://primary.example/v1")
    monkeypatch.setattr(mapping.cfg, "llm_api_key", "primary-secret")
    monkeypatch.setattr(mapping.cfg, "llm_glm_flash_second_endpoint", "")
    monkeypatch.setattr(mapping.cfg, "llm_glm_flash_second_api_key", "second-secret")

    route = mapping.mapping_route(mapping.SECOND_GLM_FLASH_ROUTE)

    assert route.model_id == "glm-5.3-flash"
    assert route.backend.label == "external-glm-flash-second-key"
    assert route.backend.endpoint == "https://primary.example/v1"
    assert route.backend.api_key == "second-secret"


def test_second_glm_flash_client_uses_independent_quota_gate(monkeypatch):
    captured = {}

    class FakeExtractor:
        def __init__(self, **kwargs):
            captured.update(kwargs)
            self._client = SimpleNamespace(with_options=lambda **options: options)

    gate = SimpleNamespace(for_model=lambda model: f"gate:{model}")
    route = ModelRoute(
        "glm-5.3-flash",
        LlmBackend("external-glm-flash-second-key", "https://example.invalid/v1", "key"),
    )
    monkeypatch.setattr(mapping, "LLMExtractor", FakeExtractor)
    monkeypatch.setattr(mapping, "mapping_route", lambda _model: route)

    client = mapping.mapping_client(gate, model=mapping.SECOND_GLM_FLASH_ROUTE)

    assert captured["model_tier"] == "glm-5.3-flash"
    assert captured["model_route"] == route
    assert client.request_gate == f"gate:{mapping.SECOND_GLM_FLASH_ROUTE}"


def test_preflight_uses_the_shared_gate_and_persists_compact_call_metadata(monkeypatch):
    record = SimpleNamespace(
        duration_s=0.5,
        input_chars=20,
        output_chars=5,
        prompt_tokens=4,
        completion_tokens=1,
        finish_reason="stop",
        success=True,
    )
    calls = []
    client = SimpleNamespace(
        model_name=DEFAULT_MODEL,
        _call_log=[record],
        _call=lambda *args, **kwargs: calls.append((args, kwargs)) or "READY",
    )
    gate = object()
    monkeypatch.setattr(
        mapping,
        "mapping_client",
        lambda supplied, **kwargs: (
            client if supplied is gate and kwargs == {"enable_reasoning": False} else None
        ),
    )

    result = mapping.preflight_glm(gate)

    assert result["status"] == "passed"
    assert result["model"] == DEFAULT_MODEL
    assert result["call"]["completion_tokens"] == 1
    assert calls[0][1] == {"max_tokens": 32, "call_type": "mapping_preflight"}


def test_preflight_records_truncation_without_failing_connectivity(monkeypatch):
    record = SimpleNamespace(
        duration_s=0.5,
        input_chars=20,
        output_chars=5,
        prompt_tokens=4,
        completion_tokens=32,
        finish_reason="length",
        success=True,
    )
    client = SimpleNamespace(
        model_name=DEFAULT_MODEL,
        _call_log=[record],
        _call=lambda *_args, **_kwargs: "READY",
    )
    monkeypatch.setattr(mapping, "mapping_client", lambda _gate, **_kwargs: client)

    result = mapping.preflight_glm(object())

    assert result["status"] == "passed"
    assert result["response_truncated"] is True
    assert result["call"]["finish_reason"] == "length"


def test_preflight_checks_completed_inference_not_instruction_adherence(monkeypatch):
    record = SimpleNamespace(
        duration_s=0.5,
        input_chars=20,
        output_chars=21,
        prompt_tokens=4,
        completion_tokens=6,
        finish_reason="stop",
        success=True,
    )
    client = SimpleNamespace(
        model_name=DEFAULT_MODEL,
        _call_log=[record],
        _call=lambda *_args, **_kwargs: "A completed response.",
    )
    monkeypatch.setattr(mapping, "mapping_client", lambda _gate, **_kwargs: client)

    result = mapping.preflight_glm(object())

    assert result["status"] == "passed"
    assert result["response"] == "A completed response."
    assert result["response_truncated"] is False


def test_long_read_timeout_reaches_actual_request(monkeypatch):
    from tests.unit.test_llm_client import _FakeLLMClient, _response

    client = _FakeLLMClient([_response("ok")])
    client.request_timeout_seconds = 1800
    client.request_read_timeout_seconds = 1800
    assert client._call("system", "user") == "ok"
    assert client.completions.kwargs[0]["timeout"].read == 1800
