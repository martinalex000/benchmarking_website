"""Explicit Flash-model routing, with one shared limiter per run."""

from datetime import UTC, datetime

from backend.config import cfg
from backend.llm_backends import LlmBackend, ModelRoute
from backend.llm_tasks import LLMExtractor
from backend.repetition_extractor import DEFAULT_MODEL, external_glm_route

DEEPSEEK_FLASH_MODEL = "deepseek-ai/DeepSeek-V4.1-Flash"
GLM_MODEL = "zai-org/GLM-5.3"
SECOND_GLM_FLASH_MODEL = "glm-5.3-flash"
SECOND_GLM_FLASH_ROUTE = "glm-5.3-flash-second-key"
SUPPORTED_MODELS = frozenset(
    {DEFAULT_MODEL, DEEPSEEK_FLASH_MODEL, GLM_MODEL, SECOND_GLM_FLASH_ROUTE}
)


def mapping_endpoint_pool(model: str) -> str:
    """Return the independently rate-limited endpoint/key pool for a route."""
    if model == SECOND_GLM_FLASH_ROUTE:
        return "second-key"
    if model in SUPPORTED_MODELS:
        return "primary-key"
    raise ValueError(f"Unsupported mapping model: {model}")


def mapping_route(model: str) -> ModelRoute:
    if model == DEFAULT_MODEL:
        return external_glm_route()
    if model == SECOND_GLM_FLASH_ROUTE:
        endpoint = (cfg.llm_glm_flash_second_endpoint or cfg.llm_endpoint).strip()
        api_key = cfg.llm_glm_flash_second_api_key
        if not endpoint or not api_key:
            raise RuntimeError(
                "The second GLM-Flash route needs LLM_GLM_FLASH_SECOND_API_KEY and "
                "either LLM_GLM_FLASH_SECOND_ENDPOINT or LLM_ENDPOINT"
            )
        backend = LlmBackend("external-glm-flash-second-key", endpoint, api_key)
        return ModelRoute(SECOND_GLM_FLASH_MODEL, backend)
    if model not in SUPPORTED_MODELS:
        raise ValueError(f"Unsupported mapping model: {model}")
    endpoint = (cfg.llm_endpoint or "").strip()
    if not endpoint:
        raise RuntimeError("No external LLM endpoint is configured for mapping")
    backend = LlmBackend("external", endpoint, cfg.llm_api_key or "none")
    return ModelRoute(model, backend)


def mapping_client(
    gate, *, model: str = DEFAULT_MODEL, enable_reasoning: bool = True
) -> LLMExtractor:
    route = mapping_route(model)
    client = LLMExtractor(
        model_tier=route.model_id,
        result_output_format="json",
        enable_reasoning=enable_reasoning,
        max_total_tokens=1_000_000,
        model_route=route,
    )
    # Retry policy and key-wide cooldown are managed by our shared request gate,
    # not hidden SDK retries that could bypass it.
    client._client = client._client.with_options(timeout=1800, max_retries=0)
    client.request_timeout_seconds = 1800
    client.request_read_timeout_seconds = 1800
    client.request_gate = gate.for_model(model) if hasattr(gate, "for_model") else gate
    return client


def preflight_model(gate, model: str) -> dict:
    """Confirm inference for one configured model before scheduling its papers."""
    client = (
        mapping_client(gate, enable_reasoning=False)
        if model == DEFAULT_MODEL
        else mapping_client(gate, model=model, enable_reasoning=False)
    )
    response = client._call(
        "Return READY.",
        "READY",
        max_tokens=32,
        call_type="mapping_preflight",
    )
    record = client._call_log[-1]
    if not record.success or not response.strip():
        raise RuntimeError(f"{model} preflight returned no usable response")
    return {
        "status": "passed",
        "checked_at": datetime.now(UTC).isoformat(),
        "model": client.model_name,
        "response": response,
        "response_truncated": record.finish_reason == "length",
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


def preflight_glm(gate) -> dict:
    """Backward-compatible GLM preflight for the default production route."""
    return preflight_model(gate, DEFAULT_MODEL)
