"""Reasoning capture is opt-in and never used as source evidence."""

from types import SimpleNamespace

import pytest

from backend.llm_client import LLMClientMixin
from backend.llm_model_options import extra_body_for_model


@pytest.mark.parametrize("streaming", [True, False])
def test_reasoning_field_is_preserved_separately_from_answer(streaming):
    message = SimpleNamespace(content='{"count":5}', reasoning_content="check outer repeats")
    choice = SimpleNamespace(message=message, delta=message, finish_reason="stop")
    response = SimpleNamespace(choices=[choice], usage=None)
    completions = SimpleNamespace(
        create=lambda **kwargs: iter([response]) if streaming else response
    )
    client = LLMClientMixin()
    client.model_name = "zai-org/GLM-5.3-Flash"
    client.enable_reasoning = True
    client.streaming = streaming
    client._client = SimpleNamespace(chat=SimpleNamespace(completions=completions))
    client._call_log = []
    assert client._call_once("system", "user") == '{"count":5}'
    assert client._call_log[-1].reasoning_response == "check outer repeats"
    assert client._call_log[-1].finish_reason == "stop"


def test_glm_default_unchanged_with_task_specific_opt_in():
    model = "zai-org/GLM-5.3-Flash"
    assert extra_body_for_model(model)["chat_template_kwargs"]["enable_thinking"] is False
    assert (
        extra_body_for_model(model, enable_reasoning=True)["chat_template_kwargs"][
            "enable_thinking"
        ]
        is True
    )


def test_gpt_oss_reasoning_is_task_specific():
    assert extra_body_for_model("openai/gpt-oss-120b") == {"reasoning_effort": "none"}
    assert extra_body_for_model("openai/gpt-oss-120b", enable_reasoning=True) == {
        "reasoning_effort": "low"
    }


def test_explicit_thinking_override_does_not_change_other_client_defaults():
    client = LLMClientMixin()
    client.model_name = "openai/gpt-oss-120b"
    client.enable_reasoning = True
    client.request_extra_body = {"reasoning_effort": "high"}
    assert client._extra_body() == {"reasoning_effort": "high"}
    other = LLMClientMixin()
    other.model_name = client.model_name
    other.enable_reasoning = True
    assert other._extra_body() == {"reasoning_effort": "low"}


def test_thinking_only_budget_exhaustion_preserves_trace_and_is_not_retried():
    message = SimpleNamespace(content="", reasoning_content="budget used up")
    choice = SimpleNamespace(message=message, finish_reason="length")
    response = SimpleNamespace(choices=[choice], usage=None)
    client = LLMClientMixin()
    client.model_name = "zai-org/GLM-5.3-Flash"
    client.streaming = False
    client._client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=lambda **kwargs: response))
    )
    client._call_log = []
    with pytest.raises(ValueError, match="completion budget"):
        client._call_once("system", "user")
    assert client._call_log[-1].reasoning_response == "budget used up"


def test_task_context_budget_does_not_mutate_global_configuration():
    from backend.config import cfg

    before = cfg.llm_max_total_tokens
    client = LLMClientMixin()
    client.max_total_tokens = 1
    with pytest.raises(ValueError, match="total token budget"):
        client._call_once("this prompt is too large", "source")
    assert cfg.llm_max_total_tokens == before


def test_long_thinking_timeout_is_task_local():
    from backend.config import cfg

    captured = {}
    message = SimpleNamespace(content='{"ok":true}', reasoning_content="check")
    response = SimpleNamespace(
        choices=[SimpleNamespace(message=message, finish_reason="stop")], usage=None
    )

    def create(**kwargs):
        captured.update(kwargs)
        return response

    client = LLMClientMixin()
    client.model_name = "openai/gpt-oss-120b"
    client.streaming = False
    client.request_timeout_seconds = 600
    client._call_log = []
    client._client = SimpleNamespace(
        chat=SimpleNamespace(completions=SimpleNamespace(create=create))
    )
    before = cfg.llm_timeout
    client._call_once("system", "source")
    assert captured["timeout"].connect == 600
    assert captured["timeout"].read == 60
    assert cfg.llm_timeout == before
