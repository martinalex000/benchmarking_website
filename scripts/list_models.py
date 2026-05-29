"""List available models at the configured LLM endpoint and verify configured models.

Optionally pings each model to see if it responds and whether reasoning mode
was successfully deactivated.

Usage::
    uv run python -m scripts.list_models
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
from backend.llm_model_options import extra_body_for_model

console = Console()


def fetch_model_ids(endpoint: str, api_key: str) -> list[str]:
    client = OpenAI(
        base_url=endpoint,
        api_key=api_key or "none",
        timeout=30,
    )
    return sorted(m.id for m in client.models.list().data)


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
        max_tokens=16,
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


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="List available models at the LLM endpoint and verify configured ones"
    )
    p.add_argument(
        "--endpoint",
        default=cfg.llm_endpoint,
        help="LLM base URL (default: LLM_ENDPOINT from .env)",
    )
    p.add_argument(
        "--api-key",
        default=cfg.llm_api_key,
        help="API key (default: LLM_API_KEY from .env)",
    )
    p.add_argument(
        "--ping",
        action="store_true",
        help="Send a probe request to every configured model and report reasoning-mode status",
    )
    args = p.parse_args(argv)

    if not args.endpoint:
        console.print(
            "[red]No endpoint configured.[/red] "
            "Set [bold]LLM_ENDPOINT[/bold] in [cyan].env[/cyan] or pass [bold]--endpoint[/bold]."
        )
        return 1

    console.print(f"[bold]LLM endpoint:[/bold] [cyan]{args.endpoint}[/cyan]")
    console.print("Fetching available models…\n")

    try:
        model_ids = fetch_model_ids(args.endpoint, args.api_key)
    except Exception as exc:
        console.print(f"[red]Failed to fetch models:[/red] {exc}")
        return 1

    # ── Print all available models ────────────────────────────────────────────
    table = Table(title=f"Available models ({len(model_ids)})", show_header=False, highlight=True)
    table.add_column("Model ID", style="cyan")
    for mid in model_ids:
        table.add_row(mid)
    console.print(table)

    # ── Check configured model tiers ─────────────────────────────────────────
    console.print("\n[bold]Configured model tiers:[/bold]")
    configured = {
        "primary  (LLM_MODEL_PRIMARY)": cfg.model_primary,
        "fallback (LLM_MODEL_FALLBACK)": cfg.model_fallback,
        "small    (LLM_MODEL_SMALL)": cfg.model_small,
    }
    all_ok = True
    for label, name in configured.items():
        if name in model_ids:
            console.print(f"  [green]✓[/green]  {label} = [cyan]{name}[/cyan]")
        else:
            console.print(
                f"  [red]✗[/red]  {label} = [yellow]{name}[/yellow]  "
                f"[red dim](not found at this endpoint)[/red dim]"
            )
            all_ok = False

    if not all_ok:
        console.print(
            "\n[yellow]Some configured models are not available at this endpoint.[/yellow]\n"
            "Update [bold]LLM_MODEL_PRIMARY[/bold] / [bold]LLM_MODEL_FALLBACK[/bold] / "
            "[bold]LLM_MODEL_SMALL[/bold] in [cyan].env[/cyan] or "
            "[cyan]config/llm_config.yaml[/cyan]."
        )
        return 1

    # ── Optional ping + reasoning-mode check ──────────────────────────────────
    if args.ping:
        console.print("\n[bold]Model ping + reasoning-mode check:[/bold]")
        ping_table = Table(show_header=True, highlight=True)
        ping_table.add_column("Model", style="cyan")
        ping_table.add_column("Response")
        ping_table.add_column("Reasoning", justify="center")
        ping_table.add_column("Status", justify="center")

        for _label, name in configured.items():
            try:
                result = ping_model(args.endpoint, args.api_key, name, timeout=cfg.llm_timeout)
            except RateLimitError:
                ping_table.add_row(name, "rate limited", "–", "[yellow]⚠[/yellow]")
                continue
            except APIStatusError as exc:
                ping_table.add_row(name, f"HTTP {exc.status_code}", "–", "[red]✗[/red]")
                continue
            except Exception as exc:
                ping_table.add_row(name, str(exc)[:40], "–", "[red]✗[/red]")
                continue

            ok_text = "[green]✓[/green]" if result["ok"] else "[red]✗[/red]"
            if result["reasoning_present"]:
                reason_text = (
                    "[red]ACTIVE[/red]\n" f"[dim]extra_body={result['extra_body_sent']}[/dim]"
                )
            else:
                reason_text = "[green]OFF[/green]"
            ping_table.add_row(
                name,
                result["content"] or "(empty)",
                reason_text,
                ok_text,
            )
        console.print(ping_table)

    console.print("\n[green]All configured models are available.[/green]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
