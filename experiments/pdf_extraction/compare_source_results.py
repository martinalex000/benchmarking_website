#!/usr/bin/env python3
"""Compare downstream extraction rows from PDF Markdown with a LaTeX reference."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.extraction_validation import (  # noqa: E402
    normalized_result_key,
    normalized_result_value,
)
from backend.llm_extractor import ExtractionOutput  # noqa: E402


@dataclass(frozen=True)
class SourceResultStats:
    reference_rows: int
    candidate_rows: int
    matching_keys: int
    matching_values: int
    value_mismatches: int
    missing_keys: int
    extra_keys: int
    relaxed_value_matches: int

    @property
    def strict_recall(self) -> float:
        return self.matching_values / self.reference_rows if self.reference_rows else 1.0

    @property
    def strict_precision(self) -> float:
        return self.matching_values / self.candidate_rows if self.candidate_rows else 1.0

    @property
    def relaxed_recall(self) -> float:
        return self.relaxed_value_matches / self.reference_rows if self.reference_rows else 1.0


def _load_output(path: Path) -> ExtractionOutput:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return ExtractionOutput.model_validate(payload["results"])


def _entry_map(output: ExtractionOutput) -> dict[tuple[str, str, str], Decimal]:
    return {normalized_result_key(row): normalized_result_value(row) for row in output.results}


def _relaxed_fingerprints(output: ExtractionOutput) -> set[tuple[str, str, Decimal]]:
    return {
        (
            normalized_result_key(row)[1],
            normalized_result_key(row)[2],
            normalized_result_value(row),
        )
        for row in output.results
    }


def compare_outputs(reference: ExtractionOutput, candidate: ExtractionOutput) -> SourceResultStats:
    reference_entries = _entry_map(reference)
    candidate_entries = _entry_map(candidate)
    shared_keys = reference_entries.keys() & candidate_entries.keys()
    matching_values = sum(
        reference_entries[key] == candidate_entries[key] for key in shared_keys
    )
    relaxed_matches = _relaxed_fingerprints(reference) & _relaxed_fingerprints(candidate)
    return SourceResultStats(
        reference_rows=len(reference_entries),
        candidate_rows=len(candidate_entries),
        matching_keys=len(shared_keys),
        matching_values=matching_values,
        value_mismatches=len(shared_keys) - matching_values,
        missing_keys=len(reference_entries.keys() - candidate_entries.keys()),
        extra_keys=len(candidate_entries.keys() - reference_entries.keys()),
        relaxed_value_matches=len(relaxed_matches),
    )


def _as_dict(stats: SourceResultStats) -> dict[str, Any]:
    return {
        **stats.__dict__,
        "strict_recall": stats.strict_recall,
        "strict_precision": stats.strict_precision,
        "relaxed_recall": stats.relaxed_recall,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("candidates", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    reference = _load_output(args.reference)
    rows = []
    for candidate_path in args.candidates:
        stats = compare_outputs(reference, _load_output(candidate_path))
        row = {"candidate": str(candidate_path), **_as_dict(stats)}
        rows.append(row)
        if not args.as_json:
            print(
                f"{candidate_path}: strict recall={stats.strict_recall:.1%} "
                f"precision={stats.strict_precision:.1%}; "
                f"relaxed recall={stats.relaxed_recall:.1%}; "
                f"value mismatches={stats.value_mismatches}"
            )
    if args.as_json:
        print(json.dumps(rows, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
