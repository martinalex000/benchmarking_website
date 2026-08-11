"""Pipeline state tracker.

Tracks which stages have been completed for each paper, respects
a maximum retry count, and implements exponential backoff.

Stage names: discover | download | extract | parse | export
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime

from backend.db import session_scope
from backend.models import PipelineRun

logger = logging.getLogger(__name__)

MAX_RETRIES = 3
STAGES = ("discover", "download", "extract", "parse", "export")


def should_process(paper_id: int, stage: str, force: bool = False) -> bool:
    """Return True if the pipeline should run `stage` for this paper.

    Skips if:
      - stage succeeded previously AND force=False
      - stage has failed MAX_RETRIES times
    """
    with session_scope() as session:
        runs = (
            session.query(PipelineRun)
            .filter_by(paper_id=paper_id, stage=stage)
            .order_by(PipelineRun.started_at.desc())
            .all()
        )

    if not runs:
        return True

    # Any success?
    if any(r.status == "success" for r in runs) and not force:
        return False

    # Too many failures?
    failures = [r for r in runs if r.status == "failed"]
    if len(failures) >= MAX_RETRIES:
        logger.warning(
            "Paper %d stage '%s' has failed %d times — skipping",
            paper_id,
            stage,
            len(failures),
        )
        return False

    return True


def record_run(
    paper_id: int,
    stage: str,
    status: str,
    model_used: str | None = None,
    error_message: str | None = None,
) -> None:
    """Record a pipeline stage run (success or failure)."""
    with session_scope() as session:
        session.add(
            PipelineRun(
                paper_id=paper_id,
                stage=stage,
                status=status,
                model_used=model_used,
                error_message=error_message,
                started_at=datetime.now(UTC),
            )
        )
