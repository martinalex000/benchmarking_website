#!/usr/bin/env python3
"""Quick test to verify if a model is responding.

Prints detailed HTTP diagnostics (status + headers), with special focus on
rate-limit related headers.
"""

import sys
import json
from pathlib import Path

# Allow running from project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai import OpenAI, APIStatusError, RateLimitError
from backend.config import cfg
from backend.llm_model_options import extra_body_for_model


_HEADER_KEYS_OF_INTEREST = [
    "date",
    "server",
    "content-type",
    "content-length",
    "retry-after",
    "x-request-id",
    "openai-processing-ms",
    "x-ratelimit-limit",
    "x-ratelimit-remaining",
    "x-ratelimit-reset",
    "x-ratelimit-limit-requests",
    "x-ratelimit-remaining-requests",
    "x-ratelimit-reset-requests",
    "x-ratelimit-limit-tokens",
    "x-ratelimit-remaining-tokens",
    "x-ratelimit-reset-tokens",
]


def _headers_to_dict(headers_obj) -> dict[str, str]:
    """Convert various header container types to a plain lowercase dict."""
    if headers_obj is None:
        return {}

    try:
        items = headers_obj.items()
    except Exception:
        try:
            return {str(k).lower(): str(v) for k, v in dict(headers_obj).items()}
        except Exception:
            return {}

    return {str(k).lower(): str(v) for k, v in items}


def _print_header_block(headers: dict[str, str]) -> None:
    """Print headers in a human-readable way, including rate-limit hints."""
    print("\nHTTP header diagnostics")
    print("-" * 70)

    if not headers:
        print("No response headers available.")
        return

    print("Important headers:")
    found_important = False
    for key in _HEADER_KEYS_OF_INTEREST:
        if key in headers:
            print(f"  - {key}: {headers[key]}")
            found_important = True
    if not found_important:
        print("  - (none of the common rate-limit/trace headers were present)")

    print("\nAll headers:")
    for key in sorted(headers):
        print(f"  - {key}: {headers[key]}")

    retry_after = headers.get("retry-after")
    remaining_req = headers.get("x-ratelimit-remaining") or headers.get(
        "x-ratelimit-remaining-requests"
    )
    remaining_tok = headers.get("x-ratelimit-remaining-tokens")

    print("\nInterpretation:")
    if retry_after:
        print(f"  - Server asks to retry after: {retry_after}")
    if remaining_req is not None:
        print(f"  - Remaining request budget: {remaining_req}")
    if remaining_tok is not None:
        print(f"  - Remaining token budget: {remaining_tok}")
    if retry_after is None and remaining_req is None and remaining_tok is None:
        print(
            "  - No explicit rate-limit headers; empty responses may still indicate upstream throttling."
        )


def test_model(model_name: str) -> bool:
    """Test if a model answers with a simple ping request."""
    print(f"\n{'='*70}")
    print(f"Testing model: {model_name}")
    print(f"{'='*70}")
    print(f"Endpoint: {cfg.llm_endpoint}")
    print(f"API Key: {'✓' if cfg.llm_api_key else '✗ NOT SET'}")
    print(f"Timeout: {cfg.llm_timeout}s")
    print()

    if not cfg.llm_api_key:
        print("❌ ERROR: LLM_API_KEY not configured")
        return False

    if not cfg.llm_endpoint:
        print("❌ ERROR: LLM_ENDPOINT not configured")
        return False

    client = OpenAI(
        api_key=cfg.llm_api_key,
        base_url=cfg.llm_endpoint,
        timeout=cfg.llm_timeout,
    )
    model_extra_body = extra_body_for_model(model_name)

    def _single_probe(
        max_tokens: int,
    ) -> tuple[
        bool,
        dict[str, str],
        int | None,
        str,
        str | None,
        str | None,
        str | None,
        int | None,
        int | None,
    ]:
        raw = client.chat.completions.with_raw_response.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Respond briefly."},
                {"role": "user", "content": "Say 'OK' and nothing else."},
            ],
            max_tokens=max_tokens,
            temperature=0.1,
            extra_body=model_extra_body,
        )
        headers = _headers_to_dict(getattr(raw, "headers", None))
        status_code = getattr(raw, "status_code", None)
        body_text = raw.text
        response = raw.parse()

        choice = response.choices[0]
        msg = choice.message
        content = (msg.content or "").strip()
        finish_reason = choice.finish_reason

        reasoning_content = None
        parsed_model_name = None
        try:
            parsed = json.loads(body_text)
            parsed_model_name = parsed.get("model")
            m = (parsed.get("choices") or [{}])[0].get("message") or {}
            reasoning_content = m.get("reasoning_content")
            if not reasoning_content:
                provider_fields = m.get("provider_specific_fields") or {}
                reasoning_content = provider_fields.get("reasoning_content") or provider_fields.get(
                    "reasoning"
                )
        except Exception:
            pass

        usage = response.usage
        prompt_tokens = usage.prompt_tokens if usage else None
        completion_tokens = usage.completion_tokens if usage else None

        ok = bool(content)
        return (
            ok,
            headers,
            status_code,
            content,
            finish_reason,
            reasoning_content,
            parsed_model_name,
            prompt_tokens,
            completion_tokens,
        )

    try:
        print("Sending probe request (max_tokens=16)...")
        ok1, headers1, status_code1, content1, finish1, reasoning1, model1, p1, c1 = _single_probe(
            16
        )

        print(f"✅ RESPONSE RECEIVED")
        if status_code1 is not None:
            print(f"   HTTP status: {status_code1}")
        print(f"   Routed model: {model1 or 'unknown'}")
        print(f"   Finish reason: {finish1}")
        print(f"   Response: {content1!r}")
        print(f"   Prompt tokens: {p1}")
        print(f"   Completion tokens: {c1}")
        if reasoning1:
            snippet = str(reasoning1)[:200].replace("\n", " ")
            print(f"   Reasoning trace present: yes ({snippet!r}...) ")
        else:
            print("   Reasoning trace present: no")
        # _print_header_block(headers1)

        ok_final = ok1

        # Secondary probe to distinguish true empty output vs reasoning-token truncation.
        if not ok1:
            print(
                "\nRunning secondary probe (max_tokens=128) to test reasoning-token truncation..."
            )
            ok2, _, status_code2, content2, finish2, reasoning2, model2, p2, c2 = _single_probe(128)
            print(f"   HTTP status: {status_code2}")
            print(f"   Routed model: {model2 or 'unknown'}")
            print(f"   Finish reason: {finish2}")
            print(f"   Response: {content2!r}")
            print(f"   Prompt tokens: {p2}")
            print(f"   Completion tokens: {c2}")

            if (finish1 == "length") and reasoning1 and ok2:
                print(
                    "\n✅ DIAGNOSIS: This is very likely reasoning-token exhaustion, not a hard outage."
                )
                print(
                    "   The first probe consumed tokens on reasoning and hit max_tokens before final answer."
                )
                print(
                    "   Increase max_tokens (or disable reasoning mode) for reliable non-empty content."
                )
                ok_final = True
            elif (finish1 == "length") and reasoning1 and (not ok2):
                print(
                    "\n⚠️ DIAGNOSIS: Reasoning token exhaustion persists even at higher token budget."
                )
                print(
                    "   This can be provider throttling, model routing mismatch, or gateway behavior."
                )
            else:
                print(
                    "\n⚠️ DIAGNOSIS: Empty response is not explained by simple reasoning truncation."
                )
                print(
                    "   Investigate gateway routing, provider quotas, or model-specific compatibility."
                )

        if not ok_final:
            print(f"\n⚠️  WARNING: Model returned empty content despite 200 response")
            print(f"   This could indicate: rate limiting, quota exceeded, or API issue")
            return False

        return True

    except RateLimitError as exc:
        print(f"❌ RATE LIMIT ERROR")
        print(f"   {exc}")
        print(f"   The API is being rate limited (too many requests)")
        # _print_header_block(_headers_to_dict(getattr(getattr(exc, "response", None), "headers", None)))
        return False

    except APIStatusError as exc:
        print(f"❌ API ERROR (HTTP {exc.status_code})")
        print(f"   {exc.message}")
        # _print_header_block(_headers_to_dict(getattr(getattr(exc, "response", None), "headers", None)))
        if exc.status_code == 429:
            print(f"   → Rate limit error")
        elif exc.status_code in (401, 403):
            print(f"   → Authentication/Authorization error — check API key")
        elif exc.status_code >= 500:
            print(f"   → Server error — the API service may be down")
        return False

    except TimeoutError:
        print(f"❌ TIMEOUT ERROR")
        print(f"   Request took longer than {cfg.llm_timeout}s")
        print(f"   The API endpoint may be slow or unresponsive")
        return False

    except Exception as exc:
        print(f"❌ UNEXPECTED ERROR: {type(exc).__name__}")
        print(f"   {exc}")
        return False


if __name__ == "__main__":
    model = sys.argv[1] if len(sys.argv) > 1 else "MiniMaxAI/MiniMax-M2.5"
    success = test_model(model)
    sys.exit(0 if success else 1)
