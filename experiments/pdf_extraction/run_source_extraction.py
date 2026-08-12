#!/usr/bin/env python3
"""Run the same restricted result extraction against LaTeX or PDF Markdown."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.config import cfg  # noqa: E402
from backend.db import session_scope  # noqa: E402
from backend.latex_source import _parse_expanded  # noqa: E402
from backend.llm_extractor import DatasetInfo, LLMExtractor  # noqa: E402
from backend.models import Paper  # noqa: E402


def _paper_title(arxiv_id: str) -> str:
    with session_scope() as session:
        paper = session.query(Paper).filter_by(arxiv_id=arxiv_id).first()
        return paper.title if paper is not None else f"arXiv:{arxiv_id}"


def _load_source(
    arxiv_id: str, *, markdown_path: Path | None, papers_dir: Path
) -> tuple[str, object | None, str]:
    if markdown_path is not None:
        return (
            markdown_path.read_text(encoding="utf-8", errors="replace"),
            None,
            str(markdown_path),
        )

    expanded_path = papers_dir / arxiv_id / "latex" / "expanded.tex"
    text = expanded_path.read_text(encoding="utf-8", errors="replace")
    return text, _parse_expanded(arxiv_id, text), str(expanded_path)


def run_source_extraction(
    *,
    arxiv_id: str,
    datasets: list[str],
    model_tier: str,
    markdown_path: Path | None,
    papers_dir: Path,
) -> dict:
    paper_text, latex_paper, source = _load_source(
        arxiv_id,
        markdown_path=markdown_path,
        papers_dir=papers_dir,
    )
    extractor = LLMExtractor(
        model_tier=model_tier,
        result_output_format="yaml",
        streaming=True,
    )
    output = extractor.extract_results_two_step(
        paper_text,
        [],
        latex_paper=latex_paper,
        paper_title=_paper_title(arxiv_id),
        target_datasets=set(datasets),
        known_datasets=[DatasetInfo(name=name) for name in datasets],
        arxiv_id=arxiv_id,
        single_pass=True,
    )
    return {
        "arxiv_id": arxiv_id,
        "source": source,
        "source_kind": "pdf_markdown" if markdown_path is not None else "latex",
        "datasets": datasets,
        "model": cfg.model_for_tier(model_tier),
        "extracted_at": datetime.now(UTC).isoformat(),
        "results": output.model_dump(),
        "calls": [
            {
                "call_type": record.call_type,
                "input_chars": record.input_chars,
                "output_chars": record.output_chars,
                "duration_s": record.duration_s,
                "prompt_tokens": record.prompt_tokens,
                "completion_tokens": record.completion_tokens,
                "success": record.success,
                "parse_error": record.parse_error,
                "extra": record.extra,
            }
            for record in extractor._call_log
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("arxiv_id")
    parser.add_argument("--datasets", nargs="+", required=True)
    parser.add_argument("--model-tier", default="primary")
    parser.add_argument("--papers-dir", type=Path, default=Path("papers"))
    parser.add_argument("--markdown", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = run_source_extraction(
        arxiv_id=args.arxiv_id,
        datasets=args.datasets,
        model_tier=args.model_tier,
        markdown_path=args.markdown,
        papers_dir=args.papers_dir,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved {len(payload['results']['results'])} result rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
