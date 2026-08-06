"""Check reachable LLMs, model behavior, rate limits, and local metrics.

Usage::
    uv run python scripts/test_llms.py
    uv run python scripts/test_llms.py ping
    uv run python scripts/test_llms.py ping MODEL_NAME
    uv run python scripts/test_llms.py --rate-limits
    uv run python scripts/test_llms.py metrics
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

# Allow running from the project root without installing the package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests
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


def _format_rate_limits(headers: dict[str, str]) -> str:
    """Format available endpoint rate-limit headers for human-readable output."""
    windows: list[str] = []
    for window in ("second", "minute", "hour", "day", "month"):
        limit = headers.get(f"x-ratelimit-limit-{window}")
        remaining = headers.get(f"x-ratelimit-remaining-{window}")
        reset = headers.get(f"x-ratelimit-reset-{window}")
        if limit or remaining or reset:
            detail = f"{window}: {remaining or '?'}/{limit or '?'}"
            if reset:
                detail += f" reset={reset}"
            windows.append(detail)

    burst_limit = headers.get("ratelimit-limit")
    burst_remaining = headers.get("ratelimit-remaining")
    burst_reset = headers.get("ratelimit-reset") or headers.get("retry-after")
    if burst_limit or burst_remaining or burst_reset:
        detail = f"burst: {burst_remaining or '?'}/{burst_limit or '?'}"
        if burst_reset:
            detail += f" reset={burst_reset}"
        windows.append(detail)
    return "; ".join(windows) if windows else "not reported"


def _ping_routes(
    routes: dict[str, ModelRoute],
    model_ids: list[str] | None = None,
    *,
    show_rate_limits: bool = False,
) -> tuple[Table, bool]:
    ping_table = Table(show_header=True, highlight=True)
    ping_table.add_column("Model", style="cyan")
    ping_table.add_column("Backend")
    ping_table.add_column("Response")
    ping_table.add_column("Reasoning", justify="center")
    ping_table.add_column("Status", justify="center")
    if show_rate_limits:
        ping_table.add_column("Rate limits")

    reasoning_ok = True
    candidates = model_ids if model_ids is not None else routes
    models_to_check = sorted(model_id for model_id in candidates if model_id in routes)
    models_to_check = [
        model_id for model_id in models_to_check if is_chat_model_for_reasoning_check(model_id)
    ]

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
            row = [model_id, backend.label, "rate limited", "–", "[yellow]⚠[/yellow]"]
            if show_rate_limits:
                row.append("rate limited")
            ping_table.add_row(*row)
            continue
        except APIStatusError as exc:
            row = [model_id, backend.label, f"HTTP {exc.status_code}", "–", "[red]✗[/red]"]
            if show_rate_limits:
                row.append("not available")
            ping_table.add_row(*row)
            continue
        except Exception as exc:
            row = [model_id, backend.label, str(exc)[:40], "–", "[red]✗[/red]"]
            if show_rate_limits:
                row.append("not available")
            ping_table.add_row(*row)
            continue

        ok_text = "[green]✓[/green]" if result["ok"] else "[red]✗[/red]"
        if result["reasoning_present"]:
            if strict_no_reasoning_required(model_id) or extra_body_for_model(model_id) is None:
                reasoning_ok = False
                reason_text = (
                    "[red]ACTIVE[/red]\n" f"[dim]extra_body={result['extra_body_sent']}[/dim]"
                )
            else:
                reason_text = (
                    "[yellow]PARTIAL[/yellow]\n"
                    f"[dim]extra_body={result['extra_body_sent']}[/dim]"
                )
        else:
            reason_text = "[green]OFF[/green]"
        row = [model_id, backend.label, result["content"] or "(empty)", reason_text, ok_text]
        if show_rate_limits:
            row.append(_format_rate_limits(result["headers"]))
        ping_table.add_row(*row)

    return ping_table, reasoning_ok


def _print_rate_limit_routes(routes: dict[str, ModelRoute]) -> None:
    """Probe one suitable chat model per backend and print rate-limit headers."""
    selected: dict[str, str] = {}
    preferred = [cfg.model_primary, cfg.model_fallback, cfg.model_small]
    for model_id in [*preferred, *sorted(routes)]:
        route = routes.get(model_id)
        if route is None or not is_chat_model_for_reasoning_check(model_id):
            continue
        selected.setdefault(route.backend.label, model_id)

    table = Table(title="Current endpoint rate limits", show_header=True, highlight=True)
    table.add_column("Backend")
    table.add_column("Endpoint")
    table.add_column("Probe model", style="cyan")
    table.add_column("Limits")
    for backend_label, model_id in sorted(selected.items()):
        route = routes[model_id]
        try:
            result = ping_model(
                route.backend.endpoint,
                route.backend.api_key,
                model_id,
                timeout=cfg.llm_timeout,
            )
            limits = _format_rate_limits(result["headers"])
        except Exception as exc:
            limits = f"probe failed: {str(exc)[:80]}"
        table.add_row(backend_label, route.backend.endpoint, model_id, limits)
    console.print(table)


def _run_check(
    *,
    endpoint: str | None,
    api_key: str | None,
    ping: bool,
    model_ids: list[str] | None,
    rate_limits: bool,
) -> int:
    if endpoint:
        console.print(f"[bold]LLM endpoint:[/bold] [cyan]{endpoint}[/cyan]")
        console.print("Fetching available models…\n")
        try:
            available_model_ids = fetch_model_ids(endpoint, api_key or cfg.llm_api_key)
        except Exception as exc:
            console.print(f"[red]Failed to fetch models:[/red] {exc}")
            return 1
        routes = {
            model_name: ModelRoute(
                model_id=model_name,
                backend=LlmBackend(
                    label="override",
                    endpoint=endpoint,
                    api_key=api_key or cfg.llm_api_key or "none",
                ),
            )
            for model_name in available_model_ids
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
            status = (
                "[green]reachable[/green]" if probe.reachable else "[yellow]unreachable[/yellow]"
            )
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
        if not ping and not rate_limits:
            return 1

    if ping:
        unknown_models = [model_id for model_id in (model_ids or []) if model_id not in routes]
        if unknown_models:
            console.print(f"[red]Model(s) not reachable:[/red] {', '.join(unknown_models)}")
            return 1
        console.print("\n[bold]Model ping + reasoning-mode check:[/bold]")
        ping_table, reasoning_ok = _ping_routes(
            routes,
            model_ids,
            show_rate_limits=rate_limits,
        )
        console.print(ping_table)
        if not reasoning_ok:
            console.print(
                "\n[red]Reasoning/thinking is still active for one or more reachable chat "
                "models.[/red] Check [cyan]backend/llm_model_options.py[/cyan]."
            )
            return 1
    elif rate_limits:
        _print_rate_limit_routes(routes)

    if tiers_ok:
        console.print("\n[green]All configured models are reachable on this node.[/green]")
    else:
        console.print(
            "\n[yellow]Reasoning check passed, but some configured tiers are missing.[/yellow]"
        )
    return 0 if tiers_ok or ping else 1


def _endpoint_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--endpoint",
        default=None,
        help="Single LLM base URL override (default: all configured backends on this node)",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="API key for --endpoint override (default: LLM_API_KEY from .env)",
    )
    parser.add_argument(
        "--rate-limits",
        action="store_true",
        help="Perform a small probe and print current endpoint rate-limit headers",
    )


DEFAULT_METRICS_ENDPOINT = "http://127.0.0.1:8773/metrics"


def metric_values(metrics: str, metric: str, required_label: str | None = None) -> list[float]:
    """Return matching Prometheus samples across vLLM's engine labels."""
    values = []
    for line in metrics.splitlines():
        if not (line.startswith(f"{metric}{{") or line.startswith(f"{metric} ")):
            continue
        if required_label and required_label not in line:
            continue
        values.append(float(line.rsplit(" ", maxsplit=1)[1]))
    return values


def metric_sum(metrics: str, metric: str, required_label: str | None = None) -> float:
    """Sum a Prometheus metric across vLLM's engine labels."""
    return sum(metric_values(metrics, metric, required_label))


def metric_average(metrics: str, metric: str, required_label: str | None = None) -> float:
    """Average a per-engine Prometheus gauge."""
    values = metric_values(metrics, metric, required_label)
    return sum(values) / len(values) if values else 0.0


def fetch_snapshot(endpoint: str) -> dict[str, float]:
    parsed = urlparse(endpoint)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("metrics endpoint must be an HTTP(S) URL")
    response = requests.get(endpoint, timeout=5)
    response.raise_for_status()
    metrics = response.text
    return {
        "input": metric_sum(metrics, "vllm:prompt_tokens_total"),
        "input_computed": metric_sum(
            metrics,
            "vllm:prompt_tokens_by_source_total",
            'source="local_compute"',
        ),
        "output": metric_sum(metrics, "vllm:generation_tokens_total"),
        "processing": metric_sum(metrics, "vllm:num_requests_running"),
        "kv_cache_usage": metric_average(metrics, "vllm:kv_cache_usage_perc"),
    }


def metrics_main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Watch vLLM throughput and cache metrics.")
    parser.add_argument(
        "--endpoint", default=DEFAULT_METRICS_ENDPOINT, help="Prometheus metrics URL"
    )
    parser.add_argument("--interval", type=float, default=2.0, help="Refresh interval in seconds")
    args = parser.parse_args(argv)

    if args.interval <= 0:
        parser.error("--interval must be greater than zero")

    previous = fetch_snapshot(args.endpoint)
    previous_time = time.monotonic()
    print(f"Watching {args.endpoint}; press Ctrl-C to stop.")

    try:
        while True:
            time.sleep(args.interval)
            current = fetch_snapshot(args.endpoint)
            now = time.monotonic()
            elapsed = now - previous_time
            print(
                f"input: {(current['input'] - previous['input']) / elapsed:8.1f} tok/s | "
                f"prefill (uncached): "
                f"{(current['input_computed'] - previous['input_computed']) / elapsed:8.1f} tok/s | "
                f"output: {(current['output'] - previous['output']) / elapsed:8.1f} tok/s | "
                f"processing: {current['processing']:3.0f} | "
                f"KV cache: {current['kv_cache_usage']:.1%}"
            )
            previous, previous_time = current, now
    except KeyboardInterrupt:
        print()
    return 0


def main(argv: list[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    if arguments and arguments[0] == "metrics":
        return metrics_main(arguments[1:])

    if arguments and arguments[0] == "ping":
        parser = argparse.ArgumentParser(description="Probe reachable chat models.")
        parser.add_argument("models", nargs="*", metavar="MODEL")
        _endpoint_arguments(parser)
        args = parser.parse_args(arguments[1:])
        return _run_check(
            endpoint=args.endpoint,
            api_key=args.api_key,
            ping=True,
            model_ids=args.models or None,
            rate_limits=args.rate_limits,
        )

    parser = argparse.ArgumentParser(
        description="List models reachable from this node and verify configured tiers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Commands:
  ping [MODEL ...]   Probe chat models and reasoning behavior
  metrics            Watch local vLLM Prometheus metrics""",
    )
    _endpoint_arguments(parser)
    args = parser.parse_args(arguments)
    return _run_check(
        endpoint=args.endpoint,
        api_key=args.api_key,
        ping=False,
        model_ids=None,
        rate_limits=args.rate_limits,
    )


if __name__ == "__main__":
    sys.exit(main())
