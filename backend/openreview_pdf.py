"""Validated, atomic downloader for staging OpenReview PDFs."""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

MAX_PDF_DOWNLOAD_BYTES = 200 * 1024 * 1024
OPENREVIEW_BASE_URL = "https://openreview.net"
_ALLOWED_HOSTS = frozenset({"openreview.net", "www.openreview.net"})
_SAFE_ID_RE = re.compile(r"[^A-Za-z0-9._-]+")


@dataclass(frozen=True)
class StagedPdf:
    note_id: str
    venue_id: str
    source_url: str
    final_url: str
    pdf_path: str
    size_bytes: int
    downloaded_at: str
    reused: bool = False


def normalize_openreview_pdf_url(pdf_url: str) -> str:
    """Return a safe absolute OpenReview URL or raise for an unexpected host."""
    url = urljoin(f"{OPENREVIEW_BASE_URL}/", str(pdf_url or "").strip())
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in _ALLOWED_HOSTS:
        raise ValueError(f"unsupported OpenReview PDF URL: {pdf_url!r}")
    return url


def safe_note_id(note_id: str) -> str:
    value = _SAFE_ID_RE.sub("_", str(note_id or "").strip()).strip("._")
    if not value:
        raise ValueError("OpenReview note ID is empty or unsafe")
    return value


def is_valid_pdf(path: Path) -> bool:
    if not path.is_file() or path.stat().st_size < 5:
        return False
    with path.open("rb") as handle:
        return handle.read(5) == b"%PDF-"


def _write_metadata(path: Path, staged: StagedPdf) -> None:
    temporary = path.with_suffix(path.suffix + ".part")
    try:
        temporary.write_text(
            json.dumps(asdict(staged), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def stage_openreview_pdf(
    *,
    note_id: str,
    venue_id: str,
    pdf_url: str,
    output_dir: Path,
    force: bool = False,
    timeout: int = 60,
    token: str | None = None,
) -> StagedPdf:
    """Download one OpenReview PDF into a staging directory without DB writes."""
    safe_id = safe_note_id(note_id)
    source_url = normalize_openreview_pdf_url(pdf_url)
    venue_dir = output_dir / _SAFE_ID_RE.sub("_", venue_id).strip("._")
    venue_dir.mkdir(parents=True, exist_ok=True)
    destination = venue_dir / f"{safe_id}.pdf"
    metadata_path = venue_dir / f"{safe_id}.json"

    if not force and is_valid_pdf(destination):
        staged = StagedPdf(
            note_id=note_id,
            venue_id=venue_id,
            source_url=source_url,
            final_url=source_url,
            pdf_path=str(destination),
            size_bytes=destination.stat().st_size,
            downloaded_at=datetime.fromtimestamp(destination.stat().st_mtime, UTC).isoformat(),
            reused=True,
        )
        _write_metadata(metadata_path, staged)
        return staged

    temporary = destination.with_suffix(".pdf.part")
    temporary.unlink(missing_ok=True)
    downloaded = 0
    try:
        headers = {"User-Agent": "GraphBenchBot/1.0"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        response = requests.get(
            source_url,
            stream=True,
            timeout=timeout,
            allow_redirects=True,
            headers=headers,
        )
        response.raise_for_status()
        final_url = normalize_openreview_pdf_url(response.url)
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_PDF_DOWNLOAD_BYTES:
            raise ValueError("OpenReview PDF exceeds 200 MB download limit")

        with temporary.open("wb") as handle:
            for chunk in response.iter_content(chunk_size=64 * 1024):
                if not chunk:
                    continue
                downloaded += len(chunk)
                if downloaded > MAX_PDF_DOWNLOAD_BYTES:
                    raise ValueError("OpenReview PDF exceeds 200 MB download limit")
                handle.write(chunk)
            handle.flush()
            os.fsync(handle.fileno())
        if not is_valid_pdf(temporary):
            raise ValueError("OpenReview response is not a valid PDF")
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)

    staged = StagedPdf(
        note_id=note_id,
        venue_id=venue_id,
        source_url=source_url,
        final_url=final_url,
        pdf_path=str(destination),
        size_bytes=downloaded,
        downloaded_at=datetime.now(UTC).isoformat(),
    )
    _write_metadata(metadata_path, staged)
    return staged
