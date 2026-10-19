import pytest

from experiments.table_provenance_experiment.run_single_background import thinking_options


def test_minimax_thinking_overrides_both_gateway_and_template_defaults():
    assert thinking_options("MiniMaxAI/MiniMax-M3", "enabled") == {
        "thinking": {"type": "enabled"},
        "chat_template_kwargs": {"thinking_mode": "enabled"},
    }


def test_llama_is_not_claimed_to_support_native_thinking():
    with pytest.raises(ValueError, match="only verified for MiniMax"):
        thinking_options("meta-llama/Llama-3.3-70B-Instruct", "enabled")


def test_provider_defaults_stay_unchanged():
    assert thinking_options("MiniMaxAI/MiniMax-M3", "provider-default") is None
