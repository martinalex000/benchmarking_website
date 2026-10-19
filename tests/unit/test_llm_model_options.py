"""Unit tests for backend.llm_model_options."""

from backend.llm_model_options import extra_body_for_model, strict_no_reasoning_required


def test_extra_body_for_kimi_uses_boolean_thinking_flag():
    extra = extra_body_for_model("moonshotai/Kimi-K2.6")
    assert extra == {
        "thinking": {"type": "disabled"},
        "chat_template_kwargs": {"thinking": False},
    }


def test_extra_body_for_kimi_aliases():
    for model in ("alias-huge-no-thinking", "alias-huge", "bubble"):
        extra = extra_body_for_model(model)
        assert extra["chat_template_kwargs"]["thinking"] is False
        assert extra["thinking"] == {"type": "disabled"}


def test_extra_body_for_qwen3_disables_thinking():
    extra = extra_body_for_model("Qwen/Qwen3-Coder-30B-A3B-Instruct")
    assert extra == {"chat_template_kwargs": {"enable_thinking": False}}


def test_extra_body_for_minimax_disables_thinking():
    extra = extra_body_for_model("MiniMaxAI/MiniMax-M2.7")
    assert extra == {
        "thinking": {"type": "disabled"},
        "chat_template_kwargs": {"thinking": False},
    }


def test_extra_body_for_gpt_oss_disables_reasoning():
    extra = extra_body_for_model("openai/gpt-oss-120b")
    assert extra == {"reasoning_effort": "none"}


def test_extra_body_for_plain_model_is_none():
    assert extra_body_for_model("google/gemma-4-31B-it") is None


def test_strict_no_reasoning_required_for_kimi_and_qwen3():
    assert strict_no_reasoning_required("moonshotai/Kimi-K2.6")
    assert strict_no_reasoning_required("alias-huge")
    assert strict_no_reasoning_required("Qwen/Qwen3-VL-8B-Instruct")
    assert strict_no_reasoning_required("MiniMaxAI/MiniMax-M2.7")
    assert strict_no_reasoning_required("openai/gpt-oss-120b")


def test_deepseek_thinking_mode_is_explicitly_selectable():
    model = "deepseek-ai/DeepSeek-V4.1-Flash"
    assert extra_body_for_model(model) is None
    assert extra_body_for_model(model, enable_reasoning=False) == {
        "thinking": {"type": "disabled"},
        "reasoning_effort": "none",
    }
    assert extra_body_for_model(model, enable_reasoning=True) is None
