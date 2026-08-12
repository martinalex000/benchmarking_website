"""Minimal OpenReview API v2 client for venue paper discovery."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from typing import Any

import requests

from backend.config import cfg
from backend.paper_matching import extract_arxiv_id_from_text

logger = logging.getLogger(__name__)

_API_BASE = "https://api2.openreview.net"
_LEGACY_API_BASE = "https://api.openreview.net"
_ARXIV_RE = re.compile(r"\b(\d{4}\.\d{4,5})(?:v\d+)?\b")


@dataclass(frozen=True)
class OpenReviewPaper:
    note_id: str
    forum_id: str
    title: str
    authors: list[str]
    arxiv_id: str
    venue: str
    venueid: str
    pdf_url: str
    invitation: str
    abstract: str = ""


class OpenReviewError(RuntimeError):
    pass


class OpenReviewClient:
    def __init__(
        self,
        *,
        username: str | None = None,
        password: str | None = None,
        token: str | None = None,
        baseurl: str = _API_BASE,
        timeout: int = 60,
    ) -> None:
        self.baseurl = baseurl.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.token = (token or "").strip() or None
        if self.token:
            self.session.headers["Authorization"] = f"Bearer {self.token}"
        elif username and password:
            self.login(username, password)

    @classmethod
    def from_config(cls) -> OpenReviewClient:
        token = cfg.openreview_token
        if token:
            return cls(token=token)
        username = cfg.openreview_username
        password = cfg.openreview_password
        if username and password:
            return cls(username=username, password=password)
        raise OpenReviewError(
            "OpenReview credentials missing. Set OPENREVIEW_TOKEN in .env "
            "(recommended), or OPENREVIEW_USERNAME and OPENREVIEW_PASSWORD. "
            "Obtain a token with: uv run python scripts/openreview_login.py"
        )

    def login(self, username: str, password: str, *, expires_in: int | None = None) -> str:
        payload: dict[str, object] = {"id": username, "password": password}
        if expires_in is not None:
            payload["expiresIn"] = expires_in
        response = self.session.post(
            f"{self.baseurl}/login",
            json=payload,
            timeout=self.timeout,
        )
        _raise_for_status(response)
        body = response.json()
        token = str(body.get("token") or "").strip()
        if not token:
            raise OpenReviewError("OpenReview login succeeded but returned no token")
        self.token = token
        self.session.headers["Authorization"] = f"Bearer {token}"
        return token

    @classmethod
    def login_for_token(
        cls,
        username: str,
        password: str,
        *,
        expires_in: int = 604_800,
        baseurl: str = _API_BASE,
    ) -> str:
        """Log in once and return a bearer token (no password stored)."""
        client = cls(baseurl=baseurl)
        return client.login(username, password, expires_in=expires_in)

    def get_group(self, group_id: str) -> dict[str, Any]:
        response = self.session.get(
            f"{self.baseurl}/groups",
            params={"id": group_id},
            timeout=self.timeout,
        )
        _raise_for_status(response)
        groups = response.json().get("groups") or []
        if not groups:
            raise OpenReviewError(f"OpenReview group not found: {group_id}")
        return groups[0]

    def submission_invitation_for_venue(self, venue_group_id: str) -> str:
        group = self.get_group(venue_group_id)
        content = group.get("content") or {}
        submission_id = _content_value(content, "submission_id")
        if submission_id:
            return submission_id
        submission_name = _content_value(content, "submission_name") or "Submission"
        return f"{venue_group_id}/-/{submission_name}"

    def iter_notes(
        self,
        *,
        invitation: str | None = None,
        content: dict[str, Any] | None = None,
        limit: int = 1000,
        baseurl: str | None = None,
    ) -> list[dict[str, Any]]:
        notes: list[dict[str, Any]] = []
        offset = 0
        notes_baseurl = (baseurl or self.baseurl).rstrip("/")
        while True:
            params: dict[str, Any] = {"limit": limit, "offset": offset}
            if invitation:
                params["invitation"] = invitation
            if content:
                params["content"] = json.dumps(content)
            response = self.session.get(
                f"{notes_baseurl}/notes",
                params=params,
                timeout=self.timeout,
            )
            _raise_for_status(response)
            batch = response.json().get("notes") or []
            if not batch:
                break
            notes.extend(batch)
            if len(batch) < limit:
                break
            offset += len(batch)
        return notes

    def fetch_venue_submissions(self, venue_group_id: str) -> list[OpenReviewPaper]:
        invitation = self.submission_invitation_for_venue(venue_group_id)
        notes = self.iter_notes(invitation=invitation)
        if not notes and invitation == f"{venue_group_id}/-/Submission":
            # Older venues such as ICLR 2022 expose submissions only through
            # API v1 and the Blind_Submission invitation.
            notes = self.iter_notes(
                invitation=f"{venue_group_id}/-/Blind_Submission",
                baseurl=_LEGACY_API_BASE,
            )
        papers: list[OpenReviewPaper] = []
        for note in notes:
            parsed = parse_openreview_note(note)
            if parsed.title:
                papers.append(parsed)
        return papers

    def search_submissions_by_title(self, venue_group_id: str, title: str) -> list[OpenReviewPaper]:
        invitation = self.submission_invitation_for_venue(venue_group_id)
        notes = self.iter_notes(invitation=invitation, content={"title": title})
        return [
            parse_openreview_note(note)
            for note in notes
            if _content_value(note.get("content"), "title")
        ]


def _content_value(content: object, key: str) -> str:
    if not isinstance(content, dict):
        return ""
    raw = content.get(key)
    if isinstance(raw, dict):
        return str(raw.get("value") or "").strip()
    return str(raw or "").strip()


def _content_list(content: object, key: str) -> list[str]:
    if not isinstance(content, dict):
        return []
    raw = content.get(key)
    values: list[object] = raw.get("value") or [] if isinstance(raw, dict) else raw or []
    if isinstance(values, str):
        return [values.strip()] if values.strip() else []
    if not isinstance(values, list):
        return []
    return [str(item).strip() for item in values if str(item).strip()]


def parse_openreview_note(note: dict[str, Any]) -> OpenReviewPaper:
    content = note.get("content") or {}
    title = _content_value(content, "title")
    authors = _content_list(content, "authors")
    pdf_url = _content_value(content, "pdf")
    venue = _content_value(content, "venue")
    venueid = _content_value(content, "venueid")
    arxiv_id = extract_arxiv_id_from_text(
        pdf_url,
        _content_value(content, "TLDR"),
        _content_value(content, "abstract"),
        json.dumps(content, ensure_ascii=False),
    )
    if not arxiv_id:
        for key, value in content.items():
            if "arxiv" in key.lower():
                arxiv_id = extract_arxiv_id_from_text(value)
                if arxiv_id:
                    break
    return OpenReviewPaper(
        note_id=str(note.get("id") or ""),
        forum_id=str(note.get("forum") or note.get("id") or ""),
        title=title,
        authors=authors,
        arxiv_id=arxiv_id,
        venue=venue,
        venueid=venueid,
        pdf_url=pdf_url,
        invitation=str(note.get("invitation") or ""),
        abstract=_content_value(content, "abstract"),
    )


def _raise_for_status(response: requests.Response) -> None:
    if response.status_code < 400:
        return
    try:
        payload = response.json()
        message = str(payload.get("message") or payload)
    except ValueError:
        message = response.text or response.reason
    raise OpenReviewError(message)
