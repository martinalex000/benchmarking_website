"""Tests for configurable LLM request retries."""

from types import SimpleNamespace

import pytest

import backend.llm_client as llm_client_module
from backend.config import cfg
from backend.llm_client import LLMClientMixin


def _response(content: str = "ok") -> SimpleNamespace:
    return SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=content))],
        usage=None,
    )


class _FakeCompletions:
    def __init__(self, outcomes: list[object]) -> None:
        self.outcomes = outcomes
        self.calls = 0
        self.kwargs: list[dict[str, object]] = []

    def create(self, **kwargs: object) -> SimpleNamespace:
        self.calls += 1
        self.kwargs.append(kwargs)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome  # type: ignore[return-value]


class _FakeLLMClient(LLMClientMixin):
    model_name = "fake-model"
    streaming = False

    def __init__(self, outcomes: list[object]) -> None:
        self.completions = _FakeCompletions(outcomes)
        self._client = SimpleNamespace(
            chat=SimpleNamespace(completions=self.completions),
        )
        self._call_log = []

    def _extra_body(self) -> None:
        return None


@pytest.fixture
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(llm_client_module.time, "sleep", lambda _seconds: None)


def test_call_succeeds_on_first_attempt(monkeypatch: pytest.MonkeyPatch, no_sleep: None) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 3)
    client = _FakeLLMClient([_response("success")])

    assert client._call("system", "user") == "success"
    assert client.completions.calls == 1


def test_call_passes_optional_response_format(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 0)
    client = _FakeLLMClient([_response("structured")])

    assert (
        client._call(
            "system",
            "user",
            response_format={"type": "json_object"},
        )
        == "structured"
    )
    assert client.completions.kwargs[0]["response_format"] == {"type": "json_object"}


def test_call_uses_max_retries_as_retries_after_initial_attempt(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 3)
    client = _FakeLLMClient([RuntimeError("failed")] * 4)

    with pytest.raises(RuntimeError, match="failed"):
        client._call("system", "user")

    assert client.completions.calls == 4


def test_call_succeeds_after_transient_failures(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 3)
    client = _FakeLLMClient([RuntimeError("temporary"), RuntimeError("temporary"), _response()])

    assert client._call("system", "user") == "ok"
    assert client.completions.calls == 3


def test_call_with_zero_retries_makes_one_attempt(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 0)
    client = _FakeLLMClient([RuntimeError("failed")])

    with pytest.raises(RuntimeError, match="failed"):
        client._call("system", "user")

    assert client.completions.calls == 1


def test_rate_limits_keep_retrying_through_shared_gate_after_retry_budget(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    class RateLimit(RuntimeError):
        status_code = 429

    class Gate:
        rate_limits = 0

        def __enter__(self):
            return self

        def __exit__(self, _exc_type, exc, _traceback):
            if getattr(exc, "status_code", None) == 429:
                self.rate_limits += 1
            return False

    monkeypatch.setattr(cfg, "llm_max_retries", 1)
    client = _FakeLLMClient([RateLimit("busy")] * 5 + [_response("recovered")])
    client.request_gate = Gate()

    assert client._call("system", "user") == "recovered"
    assert client.completions.calls == 6
    assert client.request_gate.rate_limits == 5


def test_non_rate_limit_failures_remain_bounded_after_rate_limit(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    class RateLimit(RuntimeError):
        status_code = 429

    class Gate:
        def __enter__(self):
            return self

        def __exit__(self, _exc_type, _exc, _traceback):
            return False

    monkeypatch.setattr(cfg, "llm_max_retries", 1)
    client = _FakeLLMClient([RateLimit("busy"), RuntimeError("offline")])
    client.request_gate = Gate()

    with pytest.raises(RuntimeError, match="offline"):
        client._call("system", "user")

    assert client.completions.calls == 2


def test_call_passes_configured_base_delay_to_backoff_policy(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    captured: dict[str, object] = {}
    original_wait_exponential = llm_client_module.wait_exponential

    def capture_wait_exponential(*args: object, **kwargs: object) -> object:
        captured.update(kwargs)
        return original_wait_exponential(*args, **kwargs)

    monkeypatch.setattr(cfg, "llm_max_retries", 1)
    monkeypatch.setattr(cfg, "llm_retry_base_delay", 1.5)
    monkeypatch.setattr(llm_client_module, "wait_exponential", capture_wait_exponential)
    client = _FakeLLMClient([RuntimeError("temporary"), _response()])

    assert client._call("system", "user") == "ok"
    assert captured == {"multiplier": 1.5, "max": 60}


def test_call_rereaises_final_exception_after_retries(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 2)
    final_exception = RuntimeError("final failure")
    client = _FakeLLMClient(
        [RuntimeError("first failure"), RuntimeError("second failure"), final_exception]
    )

    with pytest.raises(RuntimeError) as raised:
        client._call("system", "user")

    assert raised.value is final_exception
    assert client.completions.calls == 3


def test_retry_configuration_is_read_for_each_call(
    monkeypatch: pytest.MonkeyPatch, no_sleep: None
) -> None:
    monkeypatch.setattr(cfg, "llm_max_retries", 0)
    first_client = _FakeLLMClient([RuntimeError("first failure")])
    with pytest.raises(RuntimeError):
        first_client._call("system", "user")

    monkeypatch.setattr(cfg, "llm_max_retries", 2)
    second_client = _FakeLLMClient([RuntimeError("second failure")] * 3)
    with pytest.raises(RuntimeError):
        second_client._call("system", "user")

    assert first_client.completions.calls == 1
    assert second_client.completions.calls == 3
