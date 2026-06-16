"""List models reachable from this node and verify configured tiers.

Optionally pings each reachable chat model to confirm reasoning/thinking mode
was successfully deactivated via ``extra_body_for_model``.

Usage::
    uv run python -m scripts.list_models
    uv run python -m scripts.list_models --ping
    uv run python -m scripts.list_models --endpoint https://api.example.com/v1
    uv run python -m scripts.list_models --endpoint https://api.example.com/v1 --ping
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Allow running from the project root without installing the package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai import APIStatusError, OpenAI, RateLimitError
from rich.console import Console
from rich.table import Table

from backend.config import cfg
from backend.llm_backends import (
    LlmBackend,
    ModelRoute,
    configured_backends,
    fetch_model_routes,
    probe_backends,
)
from backend.llm_model_options import extra_body_for_model, strict_no_reasoning_required

console = Console()

_NON_CHAT_PREFIXES = (
    "BAAI/",
    "Qwen/Qwen3-Embedding",
    "openai/whisper",
    "stabilityai/",
    "black-forest-labs/",
)
_NON_CHAT_EXACT = frozenset(
    {
        "tts-1-hd",
        "Kokoro-82M",
        "alias-image-generation",
    }
)
# Models that intentionally expose reasoning; skip the no-thinking probe for them.
_REASONING_ALLOWED = frozenset({"alias-reasoning"})


def fetch_model_ids(endpoint: str, api_key: str) -> list[str]:
    client = OpenAI(
        base_url=endpoint,
        api_key=api_key or "none",
        timeout=30,
    )
    return sorted(m.id for m in client.models.list().data)


def is_chat_model_for_reasoning_check(model_id: str) -> bool:
    """Return True for chat models that should have thinking disabled."""
    if model_id in _NON_CHAT_EXACT or model_id in _REASONING_ALLOWED:
        return False
    return not any(model_id.startswith(prefix) for prefix in _NON_CHAT_PREFIXES)


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


def _has_reasoning_trace(body_text: str) -> bool:
    """Peek into the raw JSON to see if the model emitted a reasoning block."""
    try:
        parsed = json.loads(body_text)
        m = (parsed.get("choices") or [{}])[0].get("message") or {}
        if m.get("reasoning_content") or m.get("reasoning"):
            return True
        provider = m.get("provider_specific_fields") or {}
        if provider.get("reasoning_content") or provider.get("reasoning"):
            return True
    except Exception:
        pass
    return False


def ping_model(endpoint: str, api_key: str, model_name: str, timeout: int = 30) -> dict:
    """Send a minimal probe to *model_name* and report diagnostics."""
    client = OpenAI(
        api_key=api_key,
        base_url=endpoint,
        timeout=timeout,
    )
    extra = extra_body_for_model(model_name)

    raw = client.chat.completions.with_raw_response.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Respond briefly."},
            {"role": "user", "content": "Say 'OK' and nothing else."},
        ],
        max_tokens=64,
        temperature=0.1,
        extra_body=extra,
    )
    headers = _headers_to_dict(getattr(raw, "headers", None))
    status_code = getattr(raw, "status_code", None)
    response = raw.parse()
    content = (response.choices[0].message.content or "").strip()
    reasoning_present = _has_reasoning_trace(raw.text)
    return {
        "ok": bool(content),
        "status_code": status_code,
        "content": content,
        "reasoning_present": reasoning_present,
        "extra_body_sent": extra,
        "headers": headers,
    }


def _configured_tiers() -> dict[str, str]:
    return {
        "primary  (LLM_MODEL_PRIMARY)": cfg.model_primary,
        "fallback (LLM_MODEL_FALLBACK)": cfg.model_fallback,
        "small    (LLM_MODEL_SMALL)": cfg.model_small,
    }


def _print_model_inventory(routes: dict[str, ModelRoute]) -> None:
    table = Table(
        title=f"Reachable models ({len(routes)})",
        show_header=True,
        highlight=True,
    )
    table.add_column("Model ID", style="cyan")
    table.add_column("Backend")
    for model_id in sorted(routes):
        route = routes[model_id]
        table.add_row(model_id, route.backend.label)
    console.print(table)


def _print_tier_status(routes: dict[str, ModelRoute]) -> bool:
    console.print("\n[bold]Configured model tiers:[/bold]")
    all_ok = True
    for label, name in _configured_tiers().items():
        route = routes.get(name)
        if route is not None:
            console.print(
                f"  [green]✓[/green]  {label} = [cyan]{name}[/cyan] "
                f"[dim]({route.backend.label})[/dim]"
            )
        else:
            console.print(
                f"  [red]✗[/red]  {label} = [yellow]{name}[/yellow]  "
                f"[red dim](not reachable from this node)[/red dim]"
            )
            all_ok = False
    return all_ok


def _ping_routes(routes: dict[str, ModelRoute]) -> tuple[Table, bool]:
    ping_table = Table(show_header=True, highlight=True)
    ping_table.add_column("Model", style="cyan")
    ping_table.add_column("Backend")
    ping_table.add_column("Response")
    ping_table.add_column("Reasoning", justify="center")
    ping_table.add_column("Status", justify="center")

    reasoning_ok = True
    models_to_check = sorted(
        model_id for model_id in routes if is_chat_model_for_reasoning_check(model_id)
    )

    for model_id in models_to_check:
        route = routes[model_id]
        backend = route.backend
        try:
            result = ping_model(
                backend.endpoint,
                backend.api_key,
                model_id,
                timeout=cfg.llm_timeout,
            )
        except RateLimitError:
            ping_table.add_row(model_id, backend.label, "rate limited", "–", "[yellow]⚠[/yellow]")
            continue
        except APIStatusError as exc:
            ping_table.add_row(
                model_id,
                backend.label,
                f"HTTP {exc.status_code}",
                "–",
                "[red]✗[/red]",
            )
            continue
        except Exception as exc:
            ping_table.add_row(model_id, backend.label, str(exc)[:40], "–", "[red]✗[/red]")
            continue

        ok_text = "[green]✓[/green]" if result["ok"] else "[red]✗[/red]"
        if result["reasoning_present"]:
            if strict_no_reasoning_required(model_id) or extra_body_for_model(model_id) is None:
                reasoning_ok = False
                reason_text = (
                    "[red]ACTIVE[/red]\n"
                    f"[dim]extra_body={result['extra_body_sent']}[/dim]"
                )
            else:
                reason_text = (
                    "[yellow]PARTIAL[/yellow]\n"
                    f"[dim]extra_body={result['extra_body_sent']}[/dim]"
                )
        else:
            reason_text = "[green]OFF[/green]"
        ping_table.add_row(
            model_id,
            backend.label,
            result["content"] or "(empty)",
            reason_text,
            ok_text,
        )

    return ping_table, reasoning_ok


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="List models reachable from this node and verify configured tiers"
    )
    p.add_argument(
        "--endpoint",
        default=None,
        help="Single LLM base URL override (default: all configured backends on this node)",
    )
    p.add_argument(
        "--api-key",
        default=None,
        help="API key for --endpoint override (default: LLM_API_KEY from .env)",
    )
    p.add_argument(
        "--ping",
        action="store_true",
        help=(
            "Probe every reachable chat model and report whether reasoning/thinking "
            "was successfully deactivated"
        ),
    )
    args = p.parse_args(argv)

    if args.endpoint:
        console.print(f"[bold]LLM endpoint:[/bold] [cyan]{args.endpoint}[/cyan]")
        console.print("Fetching available models…\n")
        try:
            model_ids = fetch_model_ids(args.endpoint, args.api_key or cfg.llm_api_key)
        except Exception as exc:
            console.print(f"[red]Failed to fetch models:[/red] {exc}")
            return 1
        routes = {
            model_id: ModelRoute(
                model_id=model_id,
                backend=LlmBackend(
                    label="override",
                    endpoint=args.endpoint,
                    api_key=args.api_key or cfg.llm_api_key or "none",
                ),
            )
            for model_id in model_ids
        }
    else:
        backends = configured_backends()
        if not backends:
            console.print(
                "[red]No LLM backend configured.[/red] "
                "Set [bold]LLM_ENDPOINT[/bold] and/or [bold]LLM_LOCAL_ENDPOINT[/bold] in "
                "[cyan].env[/cyan]."
            )
            return 1

        console.print("[bold]LLM backends on this node:[/bold]")
        probes = probe_backends(backends)
        reachable_backends = [probe.backend for probe in probes if probe.reachable]
        for probe in probes:
            status = "[green]reachable[/green]" if probe.reachable else "[yellow]unreachable[/yellow]"
            console.print(
                f"  {probe.backend.label}: {status} at [cyan]{probe.backend.endpoint}[/cyan]"
            )
            if not probe.reachable and probe.error:
                console.print(f"    [dim]{probe.error}[/dim]")

        if not reachable_backends:
            console.print("\n[red]No reachable LLM backends on this node.[/red]")
            return 1

        console.print("\nFetching available models…\n")
        routes = fetch_model_routes(reachable_backends)
        if not routes:
            console.print("[red]Reachable backends returned no models.[/red]")
            return 1

    _print_model_inventory(routes)
    tiers_ok = _print_tier_status(routes)
    if not tiers_ok:
        console.print(
            "\n[yellow]Some configured models are not reachable from this node.[/yellow]\n"
            "Update [bold]LLM_MODEL_PRIMARY[/bold] / [bold]LLM_MODEL_FALLBACK[/bold] / "
            "[bold]LLM_MODEL_SMALL[/bold] in [cyan].env[/cyan]."
        )
        if not args.ping:
            return 1

    if args.ping:
        console.print("\n[bold]Model ping + reasoning-mode check:[/bold]")
        ping_table, reasoning_ok = _ping_routes(routes)
        console.print(ping_table)
        if not reasoning_ok:
            console.print(
                "\n[red]Reasoning/thinking is still active for one or more reachable chat "
                "models.[/red] Check [cyan]backend/llm_model_options.py[/cyan]."
            )
            return 1

    if tiers_ok:
        console.print("\n[green]All configured models are reachable on this node.[/green]")
    else:
        console.print(
            "\n[yellow]Reasoning check passed, but some configured tiers are missing.[/yellow]"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
