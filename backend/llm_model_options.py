"""Shared model-specific request options for LLM calls."""

from __future__ import annotations

_DEFAULT_CONTEXT_TEXT_CHARS = 10_000
_DEFAULT_CONTEXT_TABLE_CHARS = 10_000
# openai-gpt-oss-120b returns valid structured output with empty results above ~8k input.
_GPT_OSS_CONTEXT_TEXT_CHARS = 6_000
_GPT_OSS_CONTEXT_TABLE_CHARS = 6_000

_DEFAULT_EXTRACT_MAX_TOKENS = 8192
_GPT_OSS_EXTRACT_MAX_TOKENS = 16_384

# Mapping from internal API alias → human-readable display name stored in the DB.
# Keys are lowercased for case-insensitive matching.
_DISPLAY_NAMES: dict[str, str] = {
    "alias-huge-no-thinking": "Kimi-K2.6",
    "bubble": "Kimi-K2.6",
}


def is_gpt_oss_model(model_name: str | None) -> bool:
    """Return True for OpenAI gpt-oss family models."""
    model = (model_name or "").lower()
    return "gpt-oss" in model or "gptoss" in model.replace("-", "")


def context_limits_for_model(model_name: str | None) -> tuple[int, int]:
    """Return (max_text_chars, max_table_chars) for per-dataset RAG context."""
    if is_gpt_oss_model(model_name):
        return (_GPT_OSS_CONTEXT_TEXT_CHARS, _GPT_OSS_CONTEXT_TABLE_CHARS)
    return (_DEFAULT_CONTEXT_TEXT_CHARS, _DEFAULT_CONTEXT_TABLE_CHARS)


def extraction_max_tokens_for_model(model_name: str | None) -> int:
    """Return the completion budget for dataset result extraction calls."""
    if is_gpt_oss_model(model_name):
        return _GPT_OSS_EXTRACT_MAX_TOKENS
    return _DEFAULT_EXTRACT_MAX_TOKENS


def display_name_for_model(model_name: str | None) -> str:
    """Return the human-readable display name for a model alias.

    Falls back to the original model name if no mapping is defined.
    """
    if not model_name:
        return model_name or ""
    return _DISPLAY_NAMES.get(model_name.lower(), model_name)


def extra_body_for_model(model_name: str | None) -> dict | None:
    """Return provider-specific extra_body options for a model.

    Several model families expose a reasoning/thinking mode that can consume
    completion budget before emitting the final answer. Disable it when
    supported for deterministic structured outputs.
    """
    model = (model_name or "").lower()

    # Qwen3 via compatible gateways.
    if "qwen3" in model:
        return {"chat_template_kwargs": {"enable_thinking": False}}

    # MiniMax and Kimi/Moonshot families.
    if "minimax" in model:
        return {"thinking": {"type": "disabled"}}

    if "kimi" in model or "alias-huge-no-thinking" in model or "bubble" in model:
        return {"chat_template_kwargs": {"thinking": "false"}}

    return None
