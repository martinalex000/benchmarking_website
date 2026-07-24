#!/usr/bin/env python3
"""Print vLLM throughput, active requests, and KV-cache usage."""

from __future__ import annotations

import argparse
import time
from urllib.request import urlopen

DEFAULT_ENDPOINT = "http://127.0.0.1:8773/metrics"


def metric_sum(metrics: str, metric: str, required_label: str | None = None) -> float:
    """Sum a Prometheus metric across vLLM's engine labels."""
    return sum(metric_values(metrics, metric, required_label))


def metric_average(metrics: str, metric: str, required_label: str | None = None) -> float:
    """Average a per-engine Prometheus gauge."""
    values = metric_values(metrics, metric, required_label)
    return sum(values) / len(values) if values else 0.0


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


def fetch_snapshot(endpoint: str) -> dict[str, float]:
    with urlopen(
        endpoint, timeout=5
    ) as response:  # noqa: S310 - endpoint is an explicit CLI option
        metrics = response.read().decode()
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT, help="Prometheus metrics URL")
    parser.add_argument("--interval", type=float, default=2.0, help="Refresh interval in seconds")
    args = parser.parse_args()

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


if __name__ == "__main__":
    main()
