#!/usr/bin/env python3
"""Download one preflight-approved OpenReview PDF into isolated staging."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from backend.config import cfg  # noqa: E402
from backend.openreview_pdf import stage_openreview_pdf  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--note-id", required=True)
    parser.add_argument("--venue-id", required=True)
    parser.add_argument("--pdf-url", required=True)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(".cache/openreview_pdf_staging"),
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)

    staged = stage_openreview_pdf(
        note_id=args.note_id,
        venue_id=args.venue_id,
        pdf_url=args.pdf_url,
        output_dir=args.output_dir,
        force=args.force,
        token=cfg.openreview_token,
    )
    print(json.dumps(asdict(staged), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
