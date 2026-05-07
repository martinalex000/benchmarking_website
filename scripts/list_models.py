"""List available models at the configured LLM endpoint and verify configured models.

Usage::
    uv run python -m scripts.list_models
    uv run python -m scripts.list_models --endpoint https://api.example.com/v1
    uv run python -m scripts.list_models --endpoint https://api.example.com/v1 --api-key sk-xxx
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running from the project root without installing the package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai import OpenAI
from rich.console import Console
from rich.table import Table

from backend.config import cfg

console = Console()


def fetch_model_ids(endpoint: str, api_key: str) -> list[str]:
    client = OpenAI(
        base_url=endpoint,
        api_key=api_key or "none",
        timeout=30,
    )
    return sorted(m.id for m in client.models.list().data)


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

    console.print("\n[green]All configured models are available.[/green]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
