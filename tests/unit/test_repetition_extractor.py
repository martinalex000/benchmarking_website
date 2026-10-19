"""Production API fails closed while retaining auditable calls."""

from types import SimpleNamespace

import pytest

from backend import repetition_extractor
from backend.llm_backends import LlmBackend, ModelRoute
from backend.llm_types import CallRecord
from backend.repetition_metadata import RepetitionFacts


def test_model_schema_requires_source_coordinates_not_generated_quotes():
    schema = repetition_extractor._response_schema(RepetitionFacts, "facts")
    evidence = schema["json_schema"]["schema"]["$defs"]["Evidence"]
    assert set(evidence["properties"]) == {"start_line", "end_line"}
    assert evidence["additionalProperties"] is False
    table = schema["json_schema"]["schema"]["$defs"]["TableFact"]
    assert "decision" in table["required"]
    assert table["properties"]["decision"]["enum"] == ["count", "excluded", "unknown", "special"]


def test_external_glm_route_is_explicit_and_does_not_fall_back_to_local(monkeypatch):
    monkeypatch.setattr(repetition_extractor.cfg, "llm_endpoint", "https://external.example/v1")
    monkeypatch.setattr(repetition_extractor.cfg, "llm_api_key", "test-key")

    route = repetition_extractor.external_glm_route()

    assert route.model_id == repetition_extractor.DEFAULT_MODEL
    assert route.backend.label == "external"
    assert route.backend.endpoint == "https://external.example/v1"


def test_repetition_preflight_uses_the_external_route_and_shared_gate(monkeypatch):
    record = SimpleNamespace(
        duration_s=0.5,
        input_chars=20,
        output_chars=5,
        prompt_tokens=4,
        completion_tokens=1,
        finish_reason="stop",
        success=True,
    )
    gate = object()
    route = ModelRoute(
        repetition_extractor.DEFAULT_MODEL,
        LlmBackend("external", "https://external.example/v1", "none"),
    )
    calls = []
    constructed = {}

    class FakeClient:
        model_name = repetition_extractor.DEFAULT_MODEL
        _call_log = [record]

        def __init__(self, **kwargs):
            constructed.update(kwargs)
            self.kwargs = kwargs
            self._client = SimpleNamespace(
                with_options=lambda **options: calls.append(("options", options)) or self
            )

        def _call(self, *args, **kwargs):
            calls.append((args, kwargs))
            return "I should follow the instruction and finish with READY."

    monkeypatch.setattr(repetition_extractor, "LLMExtractor", FakeClient)

    result = repetition_extractor.preflight_external_glm(
        gate, max_total_tokens=120_000, timeout=600, model_route=route
    )

    assert result["status"] == "passed"
    assert result["model"] == repetition_extractor.DEFAULT_MODEL
    assert constructed["enable_reasoning"] is False
    assert calls[0] == ("options", {"timeout": 600, "max_retries": 0})
    assert result["call"]["completion_tokens"] == 1
    assert calls[1][1] == {"max_tokens": 32, "call_type": "repetition_preflight"}


def test_repetition_preflight_rejects_non_ready_marker(monkeypatch):
    class FakeClient:
        model_name = repetition_extractor.DEFAULT_MODEL
        _call_log = []

        def __init__(self, **_kwargs):
            self._client = SimpleNamespace(with_options=lambda **_options: self)

        def _call(self, *_args, **_kwargs):
            return "The endpoint is NOT READY."

    monkeypatch.setattr(repetition_extractor, "LLMExtractor", FakeClient)
    route = ModelRoute(
        repetition_extractor.DEFAULT_MODEL,
        LlmBackend("external", "https://external.example/v1", "none"),
    )

    with pytest.raises(RuntimeError, match="expected READY marker"):
        repetition_extractor.preflight_external_glm(
            object(), max_total_tokens=120_000, timeout=600, model_route=route
        )


def fake_client(monkeypatch, answers, finish_reason="stop"):
    class Client:
        model_name = repetition_extractor.DEFAULT_MODEL

        def __init__(self, **kwargs):
            self._call_log = []
            self.answers = iter(answers)

        def _call_structured(self, system, content, **kwargs):
            assert kwargs["response_format"]["json_schema"]["strict"] is True
            self._call_log.append(
                CallRecord(
                    call_type=kwargs["call_type"],
                    system_prompt=system,
                    user_content=content,
                    reasoning_response="audit trace",
                    finish_reason=finish_reason,
                )
            )
            return next(self.answers)

    monkeypatch.setattr(repetition_extractor, "LLMExtractor", Client)


def test_truncated_facts_do_not_trigger_verification_or_accept_counts(monkeypatch):
    fake_client(monkeypatch, [{}], finish_reason="length")
    result = repetition_extractor.extract_repetition_metadata("source")
    assert result["validated"]["accepted"] == []
    assert "truncated" in result["error"]
    assert len(result["calls"]) == 1
    assert result["calls"][0]["reasoning_response"] == "audit trace"
    assert result["provenance"]["database_writes"] is False


def test_invalid_schema_preserves_call_and_returns_no_counts(monkeypatch):
    fake_client(monkeypatch, [{"invented": 5}])
    result = repetition_extractor.extract_repetition_metadata("source")
    assert result["validated"]["accepted"] == []
    assert "ValidationError" in result["error"]
    assert result["calls"]


def test_empty_success_has_independent_verification_and_separate_coverage(monkeypatch):
    fake_client(monkeypatch, [{"proposed_methods": [], "tables": []}, {"methods": []}])
    result = repetition_extractor.extract_repetition_metadata(
        r"\begin{wraptable}{r}{4cm}\caption{Setup}\end{wraptable}"
    )
    assert len(result["calls"]) == 2
    assert result["validated"]["accepted"] == []
    assert result["validated"]["coverage"]["missing_table_ids"] == [1]
