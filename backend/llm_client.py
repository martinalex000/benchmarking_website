"""LLM transport and structured-response handling."""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import UTC, datetime
from typing import Any

import yaml
from openai import APIStatusError, RateLimitError
from tenacity import retry, stop_after_attempt, wait_exponential

from backend.config import cfg
from backend.json_repair import parse_json_lenient
from backend.llm_metadata import _headers_to_dict
from backend.llm_model_options import extra_body_for_model
from backend.llm_types import CallRecord

logger = logging.getLogger(__name__)


def _estimated_tokens(text: str) -> int:
    """Conservative token estimate used to keep requests below the global budget."""
    return max(1, (len(text) + 2) // 3)


class LLMClientMixin:
    """Internal transport methods shared by the extraction task class."""

    def _extra_body(self) -> dict | None:
        """Return model-specific extra_body parameters for chat.completions.create().

        Uses the shared helper so behavior is consistent across scripts.
        """
        return extra_body_for_model(self.model_name)

    def _probe_usage_limits(self) -> dict[str, Any]:
        """Fetch a compact snapshot of endpoint request-limit headers."""
        try:
            raw = self._client.chat.completions.with_raw_response.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant. Respond briefly."},
                    {"role": "user", "content": "Say 'OK' and nothing else."},
                ],
                max_tokens=8,
                temperature=0.0,
                extra_body=self._extra_body(),
            )
            headers = _headers_to_dict(getattr(raw, "headers", None))
        except Exception as exc:
            logger.debug("Usage limit probe failed for %s: %s", self.model_name, exc)
            return {
                "checked_at": datetime.now(UTC).isoformat(),
                "model": self.model_name,
                "note": f"Usage limit probe failed: {exc}",
            }

        windows: dict[str, dict[str, str]] = {}
        for window in ("second", "minute", "hour", "day", "month"):
            limit = headers.get(f"x-ratelimit-limit-{window}")
            remaining = headers.get(f"x-ratelimit-remaining-{window}")
            if limit or remaining:
                windows[window] = {
                    "limit": limit or "?",
                    "remaining": remaining or "?",
                }

        snapshot: dict[str, Any] = {
            "checked_at": datetime.now(UTC).isoformat(),
            "model": self.model_name,
            "windows": windows,
        }
        burst_limit = headers.get("ratelimit-limit")
        burst_remaining = headers.get("ratelimit-remaining")
        if burst_limit or burst_remaining:
            snapshot["burst"] = {
                "limit": burst_limit or "?",
                "remaining": burst_remaining or "?",
                "reset": headers.get("ratelimit-reset") or headers.get("retry-after"),
            }
        if not windows and "burst" not in snapshot:
            snapshot["note"] = (
                "Endpoint did not return explicit rate-limit headers on the probe request."
            )
        return snapshot

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2, min=5, max=60),
        reraise=True,
    )
    def _call(
        self,
        system_prompt: str,
        user_content: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
    ) -> str:
        requested_max_tokens = max_tokens or cfg.llm_max_tokens
        estimated_prompt_tokens = _estimated_tokens(system_prompt) + _estimated_tokens(user_content)
        completion_budget = min(
            requested_max_tokens,
            cfg.llm_max_total_tokens - estimated_prompt_tokens,
        )
        if completion_budget < 1:
            raise ValueError(
                "LLM prompt exceeds the configured total token budget "
                f"({cfg.llm_max_total_tokens:,} estimated tokens)."
            )

        request_start = time.perf_counter()
        first_token_time: float | None = None
        chunks: list[str] = []
        prompt_tokens: int | None = None
        completion_tokens: int | None = None
        extra_body = self._extra_body()
        try:
            if self.streaming:
                # Streaming path: captures TTFT and tokens/sec
                stream = self._client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content},
                    ],
                    max_tokens=completion_budget,
                    temperature=cfg.llm_temperature,
                    stream=True,
                    stream_options={"include_usage": True},
                    extra_body=extra_body,
                )
                for chunk in stream:
                    if getattr(chunk, "usage", None) is not None:
                        prompt_tokens = chunk.usage.prompt_tokens
                        completion_tokens = chunk.usage.completion_tokens
                    if not chunk.choices:
                        continue
                    delta = chunk.choices[0].delta.content
                    if delta:
                        if first_token_time is None:
                            first_token_time = time.perf_counter()
                        chunks.append(delta)
                content = "".join(chunks).strip()
            else:
                # Non-streaming path (production default)
                response = self._client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_content},
                    ],
                    max_tokens=completion_budget,
                    temperature=cfg.llm_temperature,
                    extra_body=extra_body,
                )
                choice = response.choices[0]
                content = (choice.message.content or "").strip()
                if response.usage:
                    prompt_tokens = response.usage.prompt_tokens
                    completion_tokens = response.usage.completion_tokens

        except Exception as exc:
            elapsed = time.perf_counter() - request_start
            # Better error classification for debugging
            exc_type = type(exc).__name__
            if isinstance(exc, RateLimitError):
                logger.warning(
                    "LLM request to %r rate limited (429): %s — will retry with backoff",
                    self.model_name,
                    exc,
                )
            elif isinstance(exc, APIStatusError):
                status = exc.status_code
                if status >= 500:
                    logger.warning(
                        "LLM endpoint error (HTTP %d) for %r: %s — will retry",
                        status,
                        self.model_name,
                        exc,
                    )
                else:
                    logger.warning(
                        "LLM API error (HTTP %d) for %r: %s — will retry",
                        status,
                        self.model_name,
                        exc,
                    )
            else:
                logger.warning(
                    "LLM request to %r failed in %.2f s (%s): %s — will retry",
                    self.model_name,
                    elapsed,
                    exc_type,
                    exc,
                )
            raise

        end_time = time.perf_counter()
        total_s = end_time - request_start
        ttft_s = (first_token_time - request_start) if first_token_time else None
        gen_s = (end_time - first_token_time) if first_token_time else total_s

        # Tokens per second: prefer API-reported completion_tokens
        if completion_tokens and gen_s > 0:
            tps: float | None = completion_tokens / gen_s
        elif content and gen_s > 0:
            tps = (len(content) / 4.0) / gen_s  # rough estimate: ~4 chars/token
        else:
            tps = None

        record = CallRecord(
            call_type=call_type,
            system_prompt=system_prompt,
            user_content=user_content,
            raw_response=content,
            input_chars=len(system_prompt) + len(user_content),
            output_chars=len(content),
            duration_s=total_s,
            ttft_s=ttft_s,
            tokens_per_sec=tps,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            success=bool(content),
            extra=call_extra or {},
        )
        self._call_log.append(record)

        if not content:
            # Some endpoints return HTTP 200 with an empty body when
            # rate-limiting or encountering a transient error.  Raising here
            # allows the @retry decorator on _call() to back off and retry.
            logger.warning(
                "Model %r returned empty content "
                "(input_chars=%d, duration=%.2f s) — likely rate limit or quota issue, will retry",
                self.model_name,
                record.input_chars,
                total_s,
            )
            raise RuntimeError(
                f"Model {self.model_name!r} returned empty content "
                f"(input_chars={record.input_chars}, duration={total_s:.2f}s) — "
                f"likely rate limit or quota exceeded — treating as transient error"
            )
        else:
            logger.debug(
                "Model %r [%s]: %d in → %d out chars | %.2f s total%s",
                self.model_name,
                call_type,
                record.input_chars,
                record.output_chars,
                total_s,
                f" | TTFT {ttft_s:.2f}s | {tps:.0f} tok/s" if ttft_s else "",
            )
        return content

    def _call_json(
        self,
        system_prompt: str,
        user_content: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
    ) -> Any:
        """Call LLM, parse JSON from the response.

        Handles:
        - Markdown code fences (```json ... ```)
        - Thinking-model blocks (<think>...</think>, common in DeepSeek/Qwen3)
        - Regex fallback: extracts first JSON object/array if direct parse fails
        """
        raw = self._call(
            system_prompt,
            user_content,
            max_tokens,
            call_type=call_type,
            call_extra=call_extra,
        )
        if not raw:
            raise ValueError(
                f"Model {self.model_name!r} returned an empty response. "
                "The input may be too long — check the model's context-window limit."
            )

        # 1. Strip thinking-model tags (<think>…</think>)
        clean = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        # 2. Strip markdown code fences: ```json ... ``` or ``` ... ```
        clean = re.sub(r"^```(?:json)?\s*", "", clean, flags=re.MULTILINE)
        clean = re.sub(r"\s*```$", "", clean, flags=re.MULTILINE).strip()

        parse_method = "direct"
        try:
            result = json.loads(clean)
        except json.JSONDecodeError:
            # 3. Regex fallback: find first {...} or [...]
            result = None
            for pattern in [r"\{[\s\S]*\}", r"\[[\s\S]*\]"]:
                m = re.search(pattern, clean)
                if m:
                    try:
                        result = json.loads(m.group(0))
                        parse_method = "regex"
                        break
                    except json.JSONDecodeError:
                        pass
            if result is None:
                result = parse_json_lenient(clean)
                if result is not None:
                    parse_method = "lenient_repair"
            if result is None:
                logger.debug("Raw LLM response (first 500 chars): %s", raw[:500])
                logger.error("JSON parse error from %r", self.model_name)
                if self._call_log:
                    self._call_log[-1].parse_error = (
                        f"JSON parse failed — raw (first 200 chars): {raw[:200]}"
                    )
                raise ValueError(  # noqa: B904
                    f"JSON parse error from {self.model_name!r}: could not extract valid JSON"
                )

        if self._call_log:
            self._call_log[-1].parsed_result = result
            if parse_method != "direct":
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "json_parse_method": parse_method,
                }
        return result

    @staticmethod
    def _read_prompt(filename: str) -> str:
        path = cfg.prompts_dir / filename
        if not path.exists():
            raise FileNotFoundError(f"Prompt not found: {path}")
        return path.read_text(encoding="utf-8").strip()

    def _read_result_prompt(self, full_mode: bool = False) -> str:
        if self.result_output_format == "yaml":
            yaml_name = (
                "full_result_extraction_yaml.txt" if full_mode else "result_extraction_yaml.txt"
            )
            yaml_path = cfg.prompts_dir / yaml_name
            if yaml_path.exists():
                return yaml_path.read_text(encoding="utf-8").strip()
        return self._read_prompt(
            "full_result_extraction.txt" if full_mode else "result_extraction.txt"
        )

    def _parse_structured_response(self, raw: str, output_format: str) -> Any:
        if not raw:
            raise ValueError(
                f"Model {self.model_name!r} returned an empty response. "
                "The input may be too long — check the model's context-window limit."
            )

        clean = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        clean = re.sub(r"^```(?:json|yaml|yml)?\s*", "", clean, flags=re.MULTILINE)
        clean = re.sub(r"\s*```$", "", clean, flags=re.MULTILINE).strip()

        fmt = output_format.lower()
        parse_errors: list[str] = []
        parsers: list[tuple[str, Any]] = []
        if fmt == "yaml":
            parsers = [("yaml", yaml.safe_load), ("json", json.loads)]
        else:
            parsers = [("json", json.loads), ("yaml", yaml.safe_load)]

        for parser_name, parser in parsers:
            try:
                result = parser(clean)
                if self._call_log:
                    self._call_log[-1].parsed_result = result
                    if parser_name != fmt:
                        self._call_log[-1].extra = {
                            **self._call_log[-1].extra,
                            "structured_parse_method": parser_name,
                        }
                return result
            except Exception as exc:
                parse_errors.append(f"{parser_name}: {exc}")

        repaired = parse_json_lenient(clean)
        if repaired is not None:
            if self._call_log:
                self._call_log[-1].parsed_result = repaired
                self._call_log[-1].extra = {
                    **self._call_log[-1].extra,
                    "structured_parse_method": "lenient_repair",
                }
            return repaired

        # Regex fallback for JSON-shaped content embedded in extra prose.
        for pattern in [r"\{[\s\S]*\}", r"\[[\s\S]*\]"]:
            m = re.search(pattern, clean)
            if not m:
                continue
            try:
                result = json.loads(m.group(0))
                if self._call_log:
                    self._call_log[-1].parsed_result = result
                    self._call_log[-1].extra = {
                        **self._call_log[-1].extra,
                        "structured_parse_method": "json_regex",
                    }
                return result
            except Exception as exc:
                parse_errors.append(f"json_regex: {exc}")

        logger.debug("Raw LLM response (first 500 chars): %s", raw[:500])
        if self._call_log:
            self._call_log[-1].parse_error = "; ".join(parse_errors)[:500]
        raise ValueError(
            f"Structured parse error from {self.model_name!r}: could not parse as {output_format}"
        )

    def _call_structured(
        self,
        system_prompt: str,
        user_content: str,
        max_tokens: int | None = None,
        call_type: str = "llm",
        call_extra: dict | None = None,
        output_format: str = "json",
    ) -> Any:
        raw = self._call(
            system_prompt,
            user_content,
            max_tokens,
            call_type=call_type,
            call_extra={**(call_extra or {}), "requested_output_format": output_format},
        )
        return self._parse_structured_response(raw, output_format)
