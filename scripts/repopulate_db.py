#!/usr/bin/env python3
"""repopulate_db.py — Reset extraction state and prime the todo queue for bulk re-runs.

Identifies papers that already have benchmark results in the database, optionally
wipes the DB and deletes their LLM artifacts, then marks those papers as manually
important in ``todo_papers`` so parallel workers can re-process them.

Typical use-case: after a major update to the extraction pipeline you want to
refresh all results without re-downloading anything.

Usage::
    # Full clean slate — wipe DB, delete LLM outputs for papers with results,
    # re-seed, and queue those papers as manually important
    uv run python scripts/repopulate_db.py --clean

    # Same but limit to specific papers (still requires existing DB results)
    uv run python scripts/repopulate_db.py --clean --paper 2206.08164 2309.00367

    # Preview what would happen without doing anything
    uv run python scripts/repopulate_db.py --clean --dry-run

    # Re-parse existing llm_output artifacts without new LLM calls
    uv run python scripts/repopulate_db.py --skip-extract

    # Also delete outdated llm_output artifacts for every paper directory
    uv run python scripts/repopulate_db.py --clean --delete-all-llm-outputs

After priming the queue, run the dashboard::

    uv run python scripts/process_papers.py dashboard --workers 10
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import NamedTuple

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.table import Table
from sqlalchemy import func

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Paper, Result
from backend.todo_queue import add_todo_paper

console = Console()
logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)

_QUEUE_REASON = "repopulate_db.py"
_QUEUE_ADDED_BY = "repopulate_db.py"
_MAX_SAMPLE_ROWS = 20
_DELETION_EXAMPLE_COUNT = 3


class LlmOutputDeletionSummary(NamedTuple):
    file_count: int
    paper_count: int


class QueuePrimeSummary(NamedTuple):
    queued: int
    skipped_no_download: int
    skipped_ids: list[str]
    messages: list[str]


def _empty_queue_prime_summary(*, queued: int = 0) -> QueuePrimeSummary:
    return QueuePrimeSummary(queued=queued, skipped_no_download=0, skipped_ids=[], messages=[])


def _collect_llm_output_paths(arxiv_ids: list[str]) -> tuple[LlmOutputDeletionSummary, list[str]]:
    from backend.paper_storage import PaperStorage

    file_count = 0
    paper_count = 0
    examples: list[str] = []
    for arxiv_id in arxiv_ids:
        storage = PaperStorage(arxiv_id)
        paths = sorted(
            list(storage.extracted_dir.glob("llm_output*.yaml"))
            + list(storage.extracted_dir.glob("llm_output*.json"))
        )
        if not paths:
            continue
        paper_count += 1
        for path in paths:
            file_count += 1
            if len(examples) < _DELETION_EXAMPLE_COUNT:
                examples.append(str(path.relative_to(cfg.project_root)))
    return LlmOutputDeletionSummary(file_count=file_count, paper_count=paper_count), examples


def _summarize_llm_output_deletions(arxiv_ids: list[str]) -> tuple[LlmOutputDeletionSummary, list[str]]:
    return _collect_llm_output_paths(arxiv_ids)


def _papers_with_results(only: list[str] | None = None) -> list[tuple[str, str]]:
    """Return (arxiv_id, title) for papers that have at least one stored result."""
    if not cfg.db_path.exists():
        return []

    init_db()
    with session_scope() as session:
        query = (
            session.query(Paper.arxiv_id, Paper.title)
            .join(Result, Result.paper_id == Paper.id)
            .group_by(Paper.id)
            .having(func.count(Result.id) > 0)
        )
        if only:
            query = query.filter(Paper.arxiv_id.in_(only))
        rows = query.order_by(Paper.arxiv_id).all()

    return [(arxiv_id, title or "") for arxiv_id, title in rows]


def _has_download(arxiv_id: str) -> bool:
    from backend.paper_storage import PaperStorage

    storage = PaperStorage(arxiv_id)
    return storage.pdf_path.exists() or storage.html_index_path.exists()


def _paper_title(arxiv_id: str, fallback: str = "") -> str:
    from backend.paper_storage import PaperStorage

    metadata = PaperStorage(arxiv_id).read_metadata()
    return str(metadata.get("title") or fallback or "")


def _discover_all_paper_ids() -> list[str]:
    """Return every arXiv ID directory under papers/."""
    papers_dir = cfg.papers_dir
    if not papers_dir.exists():
        return []

    ids: list[str] = []
    for directory in sorted(papers_dir.iterdir()):
        if not directory.is_dir():
            continue
        arxiv_id = directory.name
        if not arxiv_id or arxiv_id.startswith("."):
            continue
        ids.append(arxiv_id)
    return ids


def _delete_database() -> None:
    for suffix in ("", "-wal", "-shm"):
        path = Path(f"{cfg.db_path}{suffix}")
        if path.exists():
            path.unlink()
            console.print(f"  Deleted [dim]{path}[/dim]")


def _delete_llm_outputs(arxiv_ids: list[str]) -> tuple[LlmOutputDeletionSummary, list[str]]:
    from backend.paper_storage import PaperStorage

    file_count = 0
    paper_count = 0
    examples: list[str] = []
    for arxiv_id in arxiv_ids:
        storage = PaperStorage(arxiv_id)
        paths = sorted(
            list(storage.extracted_dir.glob("llm_output*.yaml"))
            + list(storage.extracted_dir.glob("llm_output*.json"))
        )
        if not paths:
            continue
        paper_count += 1
        for path in paths:
            if len(examples) < _DELETION_EXAMPLE_COUNT:
                examples.append(str(path.relative_to(cfg.project_root)))
            path.unlink()
            file_count += 1
    return LlmOutputDeletionSummary(file_count=file_count, paper_count=paper_count), examples


def _print_llm_output_deletion_summary(
    summary: LlmOutputDeletionSummary,
    *,
    prefix: str,
    scope: str,
    examples: list[str] | None = None,
) -> None:
    if examples:
        for example in examples:
            console.print(f"    [dim]• {example}[/dim]")
        remaining_files = summary.file_count - len(examples)
        if remaining_files > 0:
            console.print(f"    [dim]… and {remaining_files} more file(s)[/dim]")
    console.print(
        f"  {prefix} [bold]{summary.file_count}[/bold] llm_output file(s) "
        f"across [bold]{summary.paper_count}[/bold] paper "
        f"director{'ies' if summary.paper_count != 1 else 'y'} ({scope})"
    )


def _prime_repopulation_queue(papers: list[tuple[str, str]]) -> QueuePrimeSummary:
    """Mark papers as manually important and requeue finished rows when needed."""
    queued = 0
    skipped_no_download = 0
    skipped_ids: list[str] = []
    messages: list[str] = []

    for arxiv_id, title in papers:
        if not _has_download(arxiv_id):
            skipped_no_download += 1
            skipped_ids.append(arxiv_id)
            continue

        created, message = add_todo_paper(
            arxiv_id,
            title=title or _paper_title(arxiv_id),
            reason=_QUEUE_REASON,
            added_by=_QUEUE_ADDED_BY,
            is_manually_important=True,
            requeue=True,
        )
        queued += 1
        messages.append(message if created else f"[existing] {message}")

    return QueuePrimeSummary(
        queued=queued,
        skipped_no_download=skipped_no_download,
        skipped_ids=skipped_ids,
        messages=messages,
    )


def _print_queue_prime_summary(summary: QueuePrimeSummary) -> None:
    console.print(
        f"  [green]{summary.queued} queued as manually important[/green]  "
        f"[dim]{summary.skipped_no_download} skipped (no download)[/dim]"
    )
    if summary.skipped_ids:
        console.print("  [yellow]Skipped (no download):[/yellow]")
        for arxiv_id in summary.skipped_ids[:_MAX_SAMPLE_ROWS]:
            console.print(f"    [dim]{arxiv_id}[/dim]")
        remaining = len(summary.skipped_ids) - _MAX_SAMPLE_ROWS
        if remaining > 0:
            console.print(f"    [dim]… and {remaining} more[/dim]")


def _render_queue_plan_table(
    papers: list[tuple[str, str]],
    *,
    skip_extract: bool,
) -> None:
    queued = skipped = 0
    rows: list[tuple[str, str, str, str]] = []

    for arxiv_id, _title in papers:
        has_dl = "yes" if _has_download(arxiv_id) else "no"
        if skip_extract:
            action = "re-parse llm_output" if has_dl == "yes" else "skip — no download"
            if has_dl == "yes":
                queued += 1
            else:
                skipped += 1
        elif has_dl == "no":
            action = "skip queue — no download"
            skipped += 1
        else:
            action = "mark important + requeue"
            queued += 1
        rows.append((arxiv_id, "yes", has_dl, action))

    console.print(
        "[bold]Queue plan[/bold] — papers with benchmark results in the current database "
        "(read before any --clean wipe):"
    )
    console.print(
        f"  [green]{queued}[/green] will be processed  "
        f"[dim]{skipped} skipped (no download)[/dim]  "
        f"[dim]{len(papers)} total with stored results[/dim]"
    )

    if not rows:
        return

    sample = rows[:_MAX_SAMPLE_ROWS]
    table = Table(show_header=True, header_style="bold", title="Sample papers")
    table.add_column("arXiv ID")
    table.add_column("Had results")
    table.add_column("Downloaded")
    table.add_column("Planned action")
    for arxiv_id, had_results, downloaded, action in sample:
        table.add_row(arxiv_id, had_results, downloaded, action)
    console.print(table)

    remaining = len(rows) - len(sample)
    if remaining > 0:
        console.print(f"[dim]… and {remaining} more papers with the same planned actions.[/dim]")


def _run_skip_extract_parse(only: list[str] | None) -> int:
    from backend.paper_storage import PaperStorage
    from backend.results_parser import parse_and_store

    papers = _papers_with_results(only=only)
    if not papers:
        console.print("[yellow]No papers with stored results found in the database.[/yellow]")
        return 0

    ok_count = fail_count = skip_count = 0
    for arxiv_id, _title in papers:
        storage = PaperStorage(arxiv_id)
        if not storage.llm_output_path.exists():
            console.print(f"  [yellow]Skip parse[/yellow] {arxiv_id} — no llm_output artifact")
            skip_count += 1
            continue
        try:
            count = parse_and_store(arxiv_id)
            console.print(f"  [green]{arxiv_id}: {count} result(s) stored[/green]")
            ok_count += 1
        except Exception as exc:
            console.print(f"  [red]{arxiv_id}: parse failed: {exc}[/red]")
            fail_count += 1

    console.print(
        f"\n  [green]{ok_count} ok[/green]  "
        f"[red]{fail_count} failed[/red]  "
        f"[dim]{skip_count} skipped[/dim]"
    )
    return 1 if fail_count else 0


def _print_worker_instructions(model_tier: str) -> None:
    console.print("\n[bold]Next step — process the queue with the dashboard:[/bold]")
    cmd = "uv run python scripts/process_papers.py dashboard --workers 10"
    if model_tier != "primary":
        cmd += f" --model {model_tier}"
    console.print(f"  {cmd}")
    console.print(
        "\n[dim]Manually important papers are claimed first. After workers finish, export "
        "the site with `uv run python -m backend.export_to_hugo`.[/dim]"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Reset extraction state and prime the todo queue for bulk re-runs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--paper",
        nargs="+",
        metavar="ARXIV_ID",
        help="Limit to specific arXiv IDs (must already have stored results)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default="primary",
        help="Model tier workers should use (default: primary)",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help=(
            "Start from a clean slate: delete the database and LLM outputs, then re-seed from "
            "config/seed_data.yaml. By default only papers with stored results have LLM outputs "
            "removed; use --delete-all-llm-outputs to purge every papers/<id>/extracted/ artifact. "
            "Downloads are kept."
        ),
    )
    parser.add_argument(
        "--delete-all-llm-outputs",
        action="store_true",
        help=(
            "Delete llm_output*.yaml/json under every papers/<id>/extracted/ directory, "
            "not only for papers with stored results"
        ),
    )
    parser.add_argument(
        "--skip-extract",
        action="store_true",
        help="Skip queue priming; only re-parse existing llm_output artifacts into the DB",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without actually running anything",
    )
    args = parser.parse_args()

    if args.clean and args.skip_extract:
        console.print("[red]--clean and --skip-extract cannot be used together.[/red]")
        sys.exit(2)

    model_name = cfg.model_for_tier(args.model)
    papers_with_results = _papers_with_results(only=args.paper)

    console.rule("[bold]Repopulate DB[/bold]")
    console.print(f"  Papers w/ results : {len(papers_with_results)}")
    console.print(f"  Worker model      : [cyan]{model_name}[/cyan]  (tier={args.model})")
    console.print(
        f"  Clean             : {'[bold red]YES — wipe DB + LLM outputs[/bold red]' if args.clean else '[dim]no[/dim]'}"
    )
    console.print(
        f"  Delete LLM outs  : "
        f"{'[bold red]all papers/[/bold red]' if args.delete_all_llm_outputs else '[dim]papers with results only[/dim]'}"
    )
    console.print(
        f"  Mode              : {'[green]re-parse only[/green]' if args.skip_extract else '[green]prime important queue[/green]'}"
    )
    console.print(
        f"  Dry-run           : {'[yellow]YES — nothing will be changed[/yellow]' if args.dry_run else 'no'}"
    )
    console.print()

    if not papers_with_results:
        console.print(
            "[yellow]No papers with stored benchmark results found"
            + (" for the requested filter." if args.paper else ".")
            + "[/yellow]"
        )
        sys.exit(0)

    if args.dry_run:
        if args.clean:
            console.print("[bold yellow]Would delete database:[/bold yellow]")
            console.print(f"  • {cfg.db_path}")
            console.print(f"  • {cfg.db_path}-wal")
            console.print(f"  • {cfg.db_path}-shm")
            console.print()
            console.print(
                "[bold yellow]Would re-seed database from config/seed_data.yaml "
                "before priming the queue.[/bold yellow]\n"
            )

        if not args.skip_extract:
            delete_ids = (
                _discover_all_paper_ids()
                if args.delete_all_llm_outputs
                else [arxiv_id for arxiv_id, _title in papers_with_results]
            )
            scope = "all papers/" if args.delete_all_llm_outputs else "papers with stored results"
            deletion_summary, deletion_examples = _summarize_llm_output_deletions(delete_ids)
            console.print("[bold yellow]Would delete LLM outputs:[/bold yellow]")
            _print_llm_output_deletion_summary(
                deletion_summary,
                prefix="Delete",
                scope=scope,
                examples=deletion_examples,
            )
            console.print()

        _render_queue_plan_table(papers_with_results, skip_extract=args.skip_extract)
        if not args.skip_extract:
            _print_worker_instructions(args.model)
        return

    if args.skip_extract:
        init_db()
        sys.exit(_run_skip_extract_parse(only=args.paper))

    target_ids = [arxiv_id for arxiv_id, _title in papers_with_results]
    delete_ids = _discover_all_paper_ids() if args.delete_all_llm_outputs else target_ids

    if args.clean:
        console.print("[bold red]Step 1/3 — Wiping database…[/bold red]")
        _delete_database()
        console.print()

        scope = "all papers/" if args.delete_all_llm_outputs else "papers with stored results"
        console.print(f"[bold red]Step 2/3 — Deleting LLM outputs ({scope})…[/bold red]")
        deletion_summary, deletion_examples = _delete_llm_outputs(delete_ids)
        _print_llm_output_deletion_summary(
            deletion_summary,
            prefix="Deleted",
            scope=scope,
            examples=deletion_examples,
        )
        console.print()

        console.print("[bold red]Step 3/3 — Re-seeding database from config/seed_data.yaml…[/bold red]")
        from backend.seed_db import seed

        init_db()
        seed()
        console.print("  [green]Database re-seeded.[/green]\n")
    else:
        init_db()
        scope = "all papers/" if args.delete_all_llm_outputs else "papers with stored results"
        console.print(f"[bold]Deleting LLM outputs ({scope})…[/bold]")
        deletion_summary, deletion_examples = _delete_llm_outputs(delete_ids)
        _print_llm_output_deletion_summary(
            deletion_summary,
            prefix="Deleted",
            scope=scope,
            examples=deletion_examples,
        )
        console.print()

    console.print("[bold]Priming todo queue with manually important papers…[/bold]")
    queue_summary = _prime_repopulation_queue(papers_with_results)
    _print_queue_prime_summary(queue_summary)

    console.rule("[bold]Done[/bold]")
    if args.clean:
        console.print("  [dim]Order: wipe DB → delete LLM outputs → re-seed → prime queue[/dim]")
    _print_worker_instructions(args.model)


if __name__ == "__main__":
    main()
