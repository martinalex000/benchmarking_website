"""Re-apply all overrides.yaml files to the database WITHOUT re-running LLM extraction.

Use this after editing an overrides.yaml file to update the DB immediately.

Usage::
    python -m backend.reapply_overrides                   # all papers
    python -m backend.reapply_overrides --paper 2206.08164
    python -m backend.reapply_overrides --paper 2206.08164 2512.04475
"""
from __future__ import annotations

import argparse
import logging

from rich.console import Console
from rich.table import Table

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper
from backend.override_handler import apply_overrides_to_db

logger = logging.getLogger(__name__)
console = Console()


def reapply_all(arxiv_ids: list[str] | None = None) -> dict[str, int]:
    """Re-apply overrides for the given papers (or all papers if arxiv_ids is None).

    Returns a dict of {arxiv_id: rows_affected}.
    """
    init_db()

    if arxiv_ids:
        ids_to_process = arxiv_ids
    else:
        # Find all papers that have an overrides.yaml with actual content
        ids_to_process = []
        papers_root = cfg.papers_dir
        if papers_root.exists():
            for override_file in sorted(papers_root.glob("*/overrides.yaml")):
                arxiv_id = override_file.parent.name
                # Only process if file has non-template content (i.e. has real keys)
                import yaml
                try:
                    data = yaml.safe_load(override_file.read_text(encoding="utf-8")) or {}
                    has_content = any(
                        data.get(k)
                        for k in ("problematic_results", "result_overrides", "metadata_overrides")
                    )
                    if has_content:
                        ids_to_process.append(arxiv_id)
                except Exception:
                    pass

    results: dict[str, int] = {}
    for arxiv_id in ids_to_process:
        try:
            affected = apply_overrides_to_db(arxiv_id)
            results[arxiv_id] = affected
        except Exception as exc:
            logger.error("Failed to apply overrides for %s: %s", arxiv_id, exc)
            results[arxiv_id] = -1

    return results


def main(argv: list[str] | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Re-apply overrides.yaml files to the database")
    parser.add_argument(
        "--paper", "-p",
        nargs="+",
        metavar="ARXIV_ID",
        help="Specific paper arXiv IDs to process (default: all papers with overrides)",
    )
    args = parser.parse_args(argv)

    results = reapply_all(arxiv_ids=args.paper)

    if not results:
        console.print("[yellow]No override files with content found.[/yellow]")
        return

    table = Table(title="Override Application Results")
    table.add_column("arXiv ID", style="cyan")
    table.add_column("Rows Affected", justify="right")
    table.add_column("Status")

    for arxiv_id, count in sorted(results.items()):
        if count >= 0:
            table.add_row(arxiv_id, str(count), "[green]OK[/green]")
        else:
            table.add_row(arxiv_id, "—", "[red]Error[/red]")

    console.print(table)
    total = sum(v for v in results.values() if v >= 0)
    console.print(f"\nTotal rows updated: [bold]{total}[/bold]")


if __name__ == "__main__":
    main()
