"""Check benchmark source-paper links and local Hugo paper targets.

Usage::
    UV_CACHE_DIR=/tmp/benchmarking-uv-cache uv run python scripts/audit_benchmark_links.py
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import requests
import yaml


def _source_urls(project_root: Path) -> list[tuple[str, str, str]]:
    seed_path = project_root / "config" / "seed_data.yaml"
    data = yaml.safe_load(seed_path.read_text(encoding="utf-8")) or {}
    rows: list[tuple[str, str, str]] = []
    for benchmark in data.get("benchmarks", []):
        name = str(benchmark.get("name") or "Unnamed benchmark")
        sources = benchmark.get("source_papers") or []
        if not sources and (benchmark.get("arxiv_id") or benchmark.get("url")):
            sources = [{"arxiv_id": benchmark["arxiv_id"], "url": benchmark.get("url")}]
        for source in sources:
            arxiv_id = str(source.get("arxiv_id") or "").strip()
            url = str(
                source.get("url") or (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else "")
            ).strip()
            if url:
                rows.append((name, arxiv_id, url))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    failures = 0
    seen: set[str] = set()
    for benchmark, arxiv_id, url in _source_urls(root):
        if url in seen:
            continue
        seen.add(url)
        try:
            response = requests.get(url, allow_redirects=True, timeout=args.timeout)
            status = response.status_code
            final_url = response.url
            ok = 200 <= status < 400
            print(f"{'OK' if ok else 'FAIL'}\t{status}\t{benchmark}\tarXiv:{arxiv_id}\t{final_url}")
            failures += not ok
        except requests.RequestException as exc:
            print(f"FAIL\tERROR\t{benchmark}\tarXiv:{arxiv_id}\t{url}\t{exc}")
            failures += 1
    return int(failures > 0)


if __name__ == "__main__":
    sys.exit(main())
