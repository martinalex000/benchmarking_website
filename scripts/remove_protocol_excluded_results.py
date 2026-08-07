"""Remove database rows excluded by ``config/protocol_exclusions.yaml``.

Usage::

    uv run python scripts/remove_protocol_excluded_results.py --dry-run
    uv run python scripts/remove_protocol_excluded_results.py --yes
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.config import cfg
from backend.db import init_db, session_scope
from backend.models import Dataset, DatasetVariant, Paper, Result


def _load_rules() -> (
    tuple[dict[str, str], dict[str, set[str]], dict[str, set[str]], dict[str, dict[str, dict]]]
):
    path = cfg.config_dir / "protocol_exclusions.yaml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    exclude_all = {
        str(arxiv_id): str(reason)
        for arxiv_id, reason in (payload.get("exclude_all_results") or {}).items()
    }
    allowed_tasks = {
        str(arxiv_id): {str(task) for task in tasks}
        for arxiv_id, tasks in (payload.get("allowed_dataset_tasks") or {}).items()
    }
    excluded_datasets = {
        str(arxiv_id): {str(dataset).strip().casefold() for dataset in datasets}
        for arxiv_id, datasets in (payload.get("exclude_datasets") or {}).items()
    }
    exclude_results = {
        str(arxiv_id): {
            str(dataset).strip().casefold(): rule
            for dataset, rule in (rules or {}).items()
            if isinstance(rule, dict)
        }
        for arxiv_id, rules in (payload.get("exclude_results") or {}).items()
    }
    return exclude_all, allowed_tasks, excluded_datasets, exclude_results


def _matching_results() -> list[tuple[int, str, str, str]]:
    exclude_all, allowed_tasks, excluded_datasets, exclude_results = _load_rules()
    with session_scope() as session:
        rows = (
            session.query(Result)
            .join(Paper, Result.paper_id == Paper.id)
            .join(DatasetVariant, Result.dataset_variant_id == DatasetVariant.id)
            .join(Dataset, DatasetVariant.dataset_id == Dataset.id)
            .all()
        )
        return [
            (
                row.id,
                row.paper.arxiv_id,
                row.dataset_variant.dataset.name,
                row.metric_name,
            )
            for row in rows
            if row.paper.arxiv_id in exclude_all
            or row.dataset_variant.dataset.name.strip().casefold()
            in excluded_datasets.get(row.paper.arxiv_id, set())
            or (
                row.paper.arxiv_id in allowed_tasks
                and row.dataset_variant.dataset.task_type not in allowed_tasks[row.paper.arxiv_id]
            )
            or _matches_row_rule(row, exclude_results)
        ]


def _matches_row_rule(row: Result, exclude_results: dict[str, dict[str, dict]]) -> bool:
    dataset_rules = exclude_results.get(row.paper.arxiv_id, {}).get(
        row.dataset_variant.dataset.name.strip().casefold()
    )
    if not dataset_rules:
        return False
    model_names = {str(name).strip().casefold() for name in (dataset_rules.get("models") or [])}
    metric_names = {str(name).strip().casefold() for name in (dataset_rules.get("metrics") or [])}
    return (bool(model_names) and row.model.name.strip().casefold() in model_names) or (
        bool(metric_names) and row.metric_name.strip().casefold() in metric_names
    )


def clear(*, dry_run: bool) -> int:
    init_db()
    rows = _matching_results()
    if dry_run:
        for result_id, arxiv_id, dataset, metric in rows:
            print(
                f"would delete result={result_id} paper={arxiv_id} "
                f"dataset={dataset} metric={metric}"
            )
        print(f"Would delete {len(rows)} result row(s).")
        return len(rows)

    ids = [result_id for result_id, _arxiv_id, _dataset, _metric in rows]
    if ids:
        with session_scope() as session:
            session.query(Result).filter(Result.id.in_(ids)).delete(synchronize_session=False)
    print(f"Deleted {len(ids)} protocol-mismatched result row(s).")
    return len(ids)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--yes", action="store_true", help="Apply deletions")
    parser.add_argument("--dry-run", action="store_true", help="Show deletions without applying")
    args = parser.parse_args(argv)
    clear(dry_run=args.dry_run or not args.yes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
