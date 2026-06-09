"""Best-effort recovery for truncated or slightly malformed LLM JSON payloads."""

from __future__ import annotations

import json
import re
from typing import Any


def _try_load(text: str) -> Any | None:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def _strip_incomplete_json_suffix(text: str) -> str:
    """Drop a trailing partial key/value so bracket closure can succeed."""
    trimmed = text.rstrip()
    patterns = [
        r',\s*"[^"\\]*(?:\\.[^"\\]*)*"\s*:\s*"[^"\\]*(?:\\.[^"\\]*)*$',
        r',\s*"[^"\\]*(?:\\.[^"\\]*)*"\s*:\s*[^,}\]]*$',
        r',\s*"[^"\\]*(?:\\.[^"\\]*)*$',
        r':\s*"[^"\\]*(?:\\.[^"\\]*)*$',
        r":\s*[^,}\]]*$",
    ]
    for pattern in patterns:
        candidate = re.sub(pattern, "", trimmed)
        if candidate != trimmed:
            return candidate.rstrip()
    return trimmed


def _close_truncated_json(text: str) -> str:
    """Append closing brackets/braces for likely-truncated JSON."""
    base = _strip_incomplete_json_suffix(text)
    stack: list[str] = []
    in_string = False
    escape = False
    for ch in base:
        if in_string:
            if escape:
                escape = False
                continue
            if ch == "\\":
                escape = True
                continue
            if ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
            continue
        if ch in "{[":
            stack.append("}" if ch == "{" else "]")
        elif ch in "}]" and stack and stack[-1] == ch:
            stack.pop()
    suffix = "".join(reversed(stack))
    if in_string:
        suffix = '"' + suffix
    return base + suffix


def _salvage_object_array(text: str, array_key: str) -> dict[str, Any] | None:
    """Pull complete objects out of a truncated payload keyed by array_key."""
    match = re.search(rf'"{re.escape(array_key)}"\s*:\s*\[', text)
    if not match:
        return None

    start = match.end()
    objects: list[Any] = []
    idx = start
    length = len(text)
    while idx < length:
        while idx < length and text[idx] in " \t\r\n,":
            idx += 1
        if idx >= length or text[idx] == "]":
            break
        if text[idx] != "{":
            break
        depth = 0
        in_string = False
        escape = False
        end = idx
        for pos in range(idx, length):
            ch = text[pos]
            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    in_string = False
                continue
            if ch == '"':
                in_string = True
                continue
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end = pos + 1
                    break
        if depth != 0:
            break
        fragment = text[idx:end]
        parsed = _try_load(fragment)
        if isinstance(parsed, dict):
            objects.append(parsed)
        idx = end

    if not objects:
        return None

    return {array_key: objects}


def _salvage_results_array(text: str) -> dict[str, Any] | None:
    """Pull complete objects out of a truncated extraction payload."""
    salvaged = _salvage_object_array(text, "results")
    if salvaged is None:
        return None
    return {
        "proposed_model": None,
        "baseline_models": [],
        "results": salvaged["results"],
        "extraction_confidence": "LOW",
        "extraction_notes": "Recovered from truncated JSON via partial results salvage.",
    }


def _salvage_datasets_array(text: str) -> dict[str, Any] | None:
    """Pull complete dataset-statistics objects from a truncated payload."""
    salvaged = _salvage_object_array(text, "datasets")
    if salvaged is None:
        return None
    return {
        "datasets": salvaged["datasets"],
        "notes": "Recovered from truncated JSON via partial datasets salvage.",
    }


def parse_json_lenient(text: str) -> Any | None:
    """Parse JSON, attempting bracket closure and results-array salvage."""
    clean = text.strip()
    if not clean:
        return None

    direct = _try_load(clean)
    if direct is not None:
        return direct

    closed = _try_load(_close_truncated_json(clean))
    if closed is not None:
        return closed

    for pattern in [r"\{[\s\S]*", r"\[[\s\S]*"]:
        match = re.search(pattern, clean)
        if not match:
            continue
        fragment = match.group(0)
        parsed = _try_load(_close_truncated_json(fragment))
        if parsed is not None:
            return parsed

    salvaged = _salvage_results_array(clean)
    if salvaged is not None:
        return salvaged

    salvaged = _salvage_datasets_array(clean)
    if salvaged is not None:
        return salvaged

    return None
