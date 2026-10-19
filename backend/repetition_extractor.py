"""Opt-in extraction API for proposed-method counts and explicitly evaluated baselines."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict
from datetime import UTC, datetime
from pathlib import Path

from backend.config import cfg
from backend.llm_backends import LlmBackend, ModelRoute
from backend.llm_model_options import extra_body_for_model
from backend.llm_tasks import LLMExtractor
from backend.repetition_metadata import (
    RepetitionFacts,
    Verification,
    table_inventory,
    table_outcomes,
    validate_repetitions,
)

DEFAULT_MODEL = "zai-org/GLM-5.3-Flash"
MAX_REPETITION_TOTAL_TOKENS = 900_000
_PROMPTS = Path(__file__).with_name("prompts")


def external_glm_route() -> ModelRoute:
    """Pin production repetition work to the configured external GLM endpoint."""
    endpoint = (cfg.llm_endpoint or "").strip()
    if not endpoint:
        raise RuntimeError("No external LLM endpoint is configured for GLM repetition work")
    backend = LlmBackend("external", endpoint, cfg.llm_api_key or "none")
    return ModelRoute(DEFAULT_MODEL, backend)


def external_glm_routes() -> dict[str, ModelRoute]:
    """Return the independently keyed GLM-Flash workers that are configured."""
    routes = {"primary": external_glm_route()}
    endpoint = (cfg.llm_glm_flash_second_endpoint or "").strip()
    api_key = (cfg.llm_glm_flash_second_api_key or "").strip()
    if bool(endpoint) != bool(api_key):
        raise RuntimeError("The second GLM-Flash endpoint and API key must be configured together")
    if endpoint and api_key:
        routes["second"] = ModelRoute(
            "glm-5.3-flash",
            LlmBackend("external-second", endpoint, api_key),
        )
    return routes


def preflight_external_glm(
    request_gate,
    *,
    max_total_tokens: int,
    timeout: int,
    model_route: ModelRoute | None = None,
) -> dict:
    """Verify the exact external GLM route before launching a paper cohort."""
    route = model_route or external_glm_route()
    client = LLMExtractor(
        model_tier=route.model_id,
        result_output_format="json",
        enable_reasoning=False,
        max_total_tokens=max_total_tokens,
        model_route=route,
    )
    client._client = client._client.with_options(timeout=timeout, max_retries=0)
    client.request_timeout_seconds = timeout
    client.request_gate = request_gate
    response = client._call(
        "Verify this configured GLM inference endpoint. Reply with READY only.",
        "Reply READY.",
        max_tokens=32,
        call_type="repetition_preflight",
    )
    if re.search(r"\b(?:not|never|cannot)\s+ready\b", response, re.IGNORECASE) or not re.search(
        r"\bREADY\b", response, re.IGNORECASE
    ):
        raise RuntimeError("GLM repetition preflight did not return the expected READY marker")
    record = client._call_log[-1]
    result = {
        "status": "passed",
        "checked_at": datetime.now(UTC).isoformat(),
        "model": route.model_id,
        "endpoint": route.backend.label,
        "response": response,
        "call": {
            "duration_s": record.duration_s,
            "input_chars": record.input_chars,
            "output_chars": record.output_chars,
            "prompt_tokens": record.prompt_tokens,
            "completion_tokens": record.completion_tokens,
            "finish_reason": record.finish_reason,
            "success": record.success,
        },
    }
    if getattr(request_gate, "enforce_rate_limits", False):
        result["rate_limit_probe"] = client._probe_usage_limits()
    return result


def _response_schema(schema_model: type, name: str) -> dict:
    schema = schema_model.model_json_schema()
    evidence = schema.get("$defs", {}).get("Evidence")
    if evidence:
        # Only source coordinates are generated; original quotes are resolved locally.
        evidence["properties"].pop("quote", None)
        evidence["required"] = ["start_line", "end_line"]
    table = schema.get("$defs", {}).get("TableFact")
    if table:
        table["required"] = list(dict.fromkeys([*table["required"], "decision"]))
        table["properties"]["decision"] = {
            "type": "string",
            "enum": ["count", "excluded", "unknown", "special"],
        }
    return {
        "type": "json_schema",
        "json_schema": {
            "name": name,
            "strict": True,
            "schema": schema,
        },
    }


def repetition_input(source: str, *, paper_id: str = "", hints: list[str] | None = None) -> str:
    inventory = table_inventory(source)
    captions = [
        {key: value for key, value in table.items() if key != "body"} for table in inventory
    ]
    return (
        "ALL SOURCE TABLE ENVIRONMENTS AND FULL CAPTIONS (coverage inventory):\n"
        + json.dumps(captions, ensure_ascii=False)
        + f"\nPAPER {paper_id}\nStored model-name hints, not origin/proposed ground truth:\n"
        + json.dumps(hints or [], ensure_ascii=False)
        + "\nPRIMARY SOURCE WITH ORIGINAL LINE NUMBERS (no prefix truncation):\n"
        + "\n".join(f"[L{i}] {line}" for i, line in enumerate(source.splitlines(), 1))
    )


def _repetition_client(
    *,
    model: str,
    enable_reasoning: bool,
    max_total_tokens: int | None,
    request_extra_body: dict | None,
    request_timeout_seconds: int | None,
    request_gate,
    model_route: ModelRoute | None,
) -> LLMExtractor:
    client = LLMExtractor(
        model_tier=model,
        streaming=True,
        result_output_format="json",
        enable_reasoning=enable_reasoning,
        max_total_tokens=max_total_tokens,
        model_route=model_route,
    )
    if request_extra_body is not None:
        client.request_extra_body = request_extra_body
    if request_timeout_seconds is not None:
        client.request_timeout_seconds = request_timeout_seconds
    if request_gate is not None:
        client.request_gate = request_gate
        # Expose every 429 to the shared key gate; do not hide SDK-internal retries.
        client._client.max_retries = 0
    return client


def _repetition_provenance(
    source: str,
    paper_id: str,
    client: LLMExtractor,
    *,
    enable_reasoning: bool,
    max_tokens: int,
    max_total_tokens: int | None,
    request_extra_body: dict | None,
    request_timeout_seconds: int | None,
    prompt_directory: Path | None,
) -> dict:
    prompts = prompt_directory or _PROMPTS
    facts_prompt = (prompts / "repetition_metadata.txt").read_text()
    verify_prompt = (prompts / "repetition_verification.txt").read_text()
    return {
        "paper_id": paper_id,
        "model": client.model_name,
        "model_options": request_extra_body
        if request_extra_body is not None
        else extra_body_for_model(client.model_name, enable_reasoning=enable_reasoning),
        "max_completion_tokens": max_tokens,
        "max_total_tokens": max_total_tokens or cfg.llm_max_total_tokens,
        "request_timeout_seconds": request_timeout_seconds or cfg.llm_timeout,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prompt_sha256": {
            "facts": hashlib.sha256(facts_prompt.encode()).hexdigest(),
            "verification": hashlib.sha256(verify_prompt.encode()).hexdigest(),
        },
        "table_id_namespace": "source_environment_ordinal",
        "database_writes": False,
    }


def _failed_phase(source: str, provenance: dict, exc: Exception, calls: list[dict]) -> dict:
    error = f"{type(exc).__name__}: {exc}"
    return {
        "provenance": provenance,
        "error": error,
        "validated": {
            "accepted": [],
            "table_outcomes": table_outcomes(None, source, {}, error=error),
        },
        "calls": calls,
    }


def extract_repetition_facts_phase(
    source: str,
    *,
    paper_id: str = "",
    hints: list[str] | None = None,
    model: str = DEFAULT_MODEL,
    enable_reasoning: bool = True,
    max_tokens: int = 24_000,
    max_total_tokens: int | None = None,
    prompt_directory: Path | None = None,
    request_extra_body: dict | None = None,
    request_timeout_seconds: int | None = None,
    request_gate=None,
    model_route: ModelRoute | None = None,
) -> dict:
    """Run phase 1 of the whole-paper extraction and preserve its call record."""
    client = _repetition_client(
        model=model,
        enable_reasoning=enable_reasoning,
        max_total_tokens=max_total_tokens,
        request_extra_body=request_extra_body,
        request_timeout_seconds=request_timeout_seconds,
        request_gate=request_gate,
        model_route=model_route,
    )
    provenance = _repetition_provenance(
        source,
        paper_id,
        client,
        enable_reasoning=enable_reasoning,
        max_tokens=max_tokens,
        max_total_tokens=max_total_tokens,
        request_extra_body=request_extra_body,
        request_timeout_seconds=request_timeout_seconds,
        prompt_directory=prompt_directory,
    )
    try:
        raw = client._call_structured(
            (prompt_directory or _PROMPTS / "").joinpath("repetition_metadata.txt").read_text(),
            repetition_input(source, paper_id=paper_id, hints=hints),
            call_type="repetition_facts",
            output_format="json",
            max_tokens=max_tokens,
            response_format=_response_schema(RepetitionFacts, "repetition_facts"),
        )
        if client._call_log[-1].finish_reason == "length":
            raise ValueError("Repetition facts truncated; no counts accepted")
        facts = RepetitionFacts.model_validate(raw)
        return {
            "provenance": provenance,
            "facts": facts.model_dump(),
            "calls": [asdict(c) for c in client._call_log],
        }
    except Exception as exc:
        return _failed_phase(
            source,
            provenance,
            exc,
            [asdict(call) for call in client._call_log],
        )


def _repetition_feedback(validated: dict) -> dict:
    """Describe deterministic validation failures for a targeted verifier retry."""
    feedback = {
        "coverage": validated.get("coverage", {}),
        "methods": [],
    }
    for item in validated.get("withheld", []):
        flags = item.get("flags", [])
        if flags == ["ablation_variant_not_eligible"]:
            continue
        feedback["methods"].append(
            {
                "table_id": item.get("table_id"),
                "name": item.get("name"),
                "candidate_repetitions": item.get("candidate_repetitions"),
                "flags": flags,
            }
        )
    return feedback


def verify_repetition_phase(
    source: str,
    facts_payload: dict,
    *,
    hints: list[str] | None = None,
    enable_reasoning: bool = True,
    request_gate=None,
    request_route: ModelRoute | None = None,
    prompt_directory: Path | None = None,
) -> dict:
    """Verify facts with up to three targeted, source-grounded feedback rounds."""
    provenance = facts_payload["provenance"]
    prior_calls = list(facts_payload.get("calls", []))
    if facts_payload.get("error"):
        return _failed_phase(
            source,
            provenance,
            ValueError(f"Phase 1 failed: {facts_payload['error']}"),
            prior_calls,
        )
    facts = RepetitionFacts.model_validate(facts_payload["facts"])
    model = provenance["model"]
    client = _repetition_client(
        model=model,
        enable_reasoning=enable_reasoning,
        max_total_tokens=provenance.get("max_total_tokens"),
        request_extra_body=provenance.get("model_options"),
        request_timeout_seconds=provenance.get("request_timeout_seconds"),
        request_gate=request_gate,
        model_route=request_route,
    )
    prompts = prompt_directory or _PROMPTS
    content = repetition_input(source, paper_id=provenance["paper_id"], hints=hints)
    base_content = content + "\nUNTRUSTED METADATA (not source evidence):\n"
    base_content += facts.model_dump_json()
    base_content += "\nREQUIRED VERDICT KEYS (copy exactly; do not expand variants):\n"
    base_content += json.dumps(
        [{"table_id": t.table_id, "name": m.name} for t in facts.tables for m in t.methods]
    )
    feedback: dict = {}
    previous_verification: dict | None = None
    calls = list(prior_calls)
    try:
        for round_index in range(3):
            verifier_content = (
                base_content
                + "\nTARGETED VALIDATION FEEDBACK (resolve against source; do not force acceptance):\n"
                + json.dumps(feedback, ensure_ascii=False)
            )
            if previous_verification is not None:
                verifier_content += (
                    "\nPREVIOUS VERIFIER OUTPUT (preserve correct source-grounded decisions; "
                    "repair only issues identified by feedback):\n"
                    + json.dumps(previous_verification, ensure_ascii=False)
                )
            raw = client._call_structured(
                (prompts / "repetition_verification.txt").read_text(),
                verifier_content,
                call_type=(
                    "repetition_verification"
                    if round_index == 0
                    else f"repetition_verification_feedback_{round_index}"
                ),
                output_format="json",
                max_tokens=int(provenance["max_completion_tokens"]),
                response_format=_response_schema(Verification, "repetition_verification"),
            )
            if client._call_log[-1].finish_reason == "length":
                raise ValueError("Repetition verification truncated; no counts accepted")
            verification = Verification.model_validate(raw)
            validated = validate_repetitions(facts, verification, source)
            previous_verification = verification.model_dump()
            feedback = _repetition_feedback(validated)
            if not feedback["methods"] and not any(feedback["coverage"].values()):
                break
        calls.extend(asdict(call) for call in client._call_log)
        return {
            "provenance": provenance,
            "facts": facts.model_dump(),
            "verification": verification.model_dump(),
            "validated": validated,
            "verification_feedback_rounds": len(client._call_log),
            "calls": calls,
        }
    except Exception as exc:
        return _failed_phase(
            source,
            provenance,
            exc,
            prior_calls + [asdict(call) for call in client._call_log],
        )


def extract_repetition_metadata(
    source: str,
    *,
    paper_id: str = "",
    hints: list[str] | None = None,
    model: str = DEFAULT_MODEL,
    enable_reasoning: bool = True,
    max_tokens: int = 24_000,
    max_total_tokens: int | None = None,
    prompt_directory: Path | None = None,
    request_extra_body: dict | None = None,
    request_timeout_seconds: int | None = None,
    request_gate=None,
    model_route: ModelRoute | None = None,
) -> dict:
    """Extract, independently verify, then fail closed. Does not alter results or DB.

    The caller's configured token budget still applies. Oversized inputs fail closed rather
    than dropping appendices or silently fabricating unknown counts.
    """
    content = repetition_input(source, paper_id=paper_id, hints=hints)
    client = LLMExtractor(
        model_tier=model,
        streaming=True,
        result_output_format="json",
        enable_reasoning=enable_reasoning,
        max_total_tokens=max_total_tokens,
        model_route=model_route,
    )
    if request_extra_body is not None:
        client.request_extra_body = request_extra_body
    if request_timeout_seconds is not None:
        client.request_timeout_seconds = request_timeout_seconds
    if request_gate is not None:
        client.request_gate = request_gate
        # Expose every 429 to the shared key gate; do not hide SDK-internal retries.
        client._client.max_retries = 0
    prompts = prompt_directory or _PROMPTS
    facts_prompt = (prompts / "repetition_metadata.txt").read_text()
    verify_prompt = (prompts / "repetition_verification.txt").read_text()
    provenance = {
        "paper_id": paper_id,
        "model": client.model_name,
        "model_options": request_extra_body
        if request_extra_body is not None
        else extra_body_for_model(client.model_name, enable_reasoning=enable_reasoning),
        "max_completion_tokens": max_tokens,
        "max_total_tokens": max_total_tokens or cfg.llm_max_total_tokens,
        "request_timeout_seconds": request_timeout_seconds or cfg.llm_timeout,
        "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
        "prompt_sha256": {
            "facts": hashlib.sha256(facts_prompt.encode()).hexdigest(),
            "verification": hashlib.sha256(verify_prompt.encode()).hexdigest(),
        },
        "table_id_namespace": "source_environment_ordinal",
        "database_writes": False,
    }
    try:
        raw = client._call_structured(
            facts_prompt,
            content,
            call_type="repetition_facts",
            output_format="json",
            max_tokens=max_tokens,
            response_format=_response_schema(RepetitionFacts, "repetition_facts"),
        )
        if client._call_log[-1].finish_reason == "length":
            raise ValueError("Repetition facts truncated; no counts accepted")
        facts = RepetitionFacts.model_validate(raw)
        verifier_content = content + "\nUNTRUSTED METADATA (not source evidence):\n"
        verifier_content += facts.model_dump_json()
        verifier_content += "\nREQUIRED VERDICT KEYS (copy exactly; do not expand variants):\n"
        verifier_content += json.dumps(
            [{"table_id": t.table_id, "name": m.name} for t in facts.tables for m in t.methods]
        )
        raw_verification = client._call_structured(
            verify_prompt,
            verifier_content,
            call_type="repetition_verification",
            output_format="json",
            max_tokens=max_tokens,
            response_format=_response_schema(Verification, "repetition_verification"),
        )
        if client._call_log[-1].finish_reason == "length":
            raise ValueError("Repetition verification truncated; no counts accepted")
        verification = Verification.model_validate(raw_verification)
        return {
            "provenance": provenance,
            "facts": facts.model_dump(),
            "verification": verification.model_dump(),
            "validated": validate_repetitions(facts, verification, source),
            "calls": [asdict(call) for call in client._call_log],
        }
    except Exception as exc:
        # Preserve the exact calls even if strict schema validation fails.
        return {
            "provenance": provenance,
            "error": f"{type(exc).__name__}: {exc}",
            "validated": {
                "accepted": [],
                "table_outcomes": table_outcomes(
                    None, source, {}, error=f"{type(exc).__name__}: {exc}"
                ),
            },
            "calls": [asdict(call) for call in client._call_log],
        }
