"""Shared model-specific request options for LLM calls."""

from __future__ import annotations

# Mapping from internal API alias → human-readable display name stored in the DB.
# Keys are lowercased for case-insensitive matching.
_DISPLAY_NAMES: dict[str, str] = {
    "alias-huge-no-thinking": "Kimi-K2.6",
    "bubble": "Kimi-K2.6",
}


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
