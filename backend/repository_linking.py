"""Helpers for extracting and verifying repository links from paper sources."""

from __future__ import annotations

import base64
import logging
import re
from typing import Any
from urllib.parse import urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

_URL_RE = re.compile(r"https?://[^\s<>'\"\]}\\)]+", re.IGNORECASE)
_GITHUB_URL_RE = re.compile(
    r"https?://(?:www\.)?github\.com/"
    r"(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)"
    r"(?:[/?#][^\s<>'\"\]}\\)]*)?",
    re.IGNORECASE,
)
_POSITIVE_CONTEXT_RE = re.compile(
    r"\b(?:code|source|implementation|repo|repository|github|gitlab|bitbucket|code|official|available|release|project)\b",
    re.IGNORECASE,
)
_NEGATIVE_CONTEXT_RE = re.compile(
    r"\b(?:baseline|library|framework|dependency|benchmark|dataset|borrowed|adapted|built on|uses|issue|issues|docs?)\b",
    re.IGNORECASE,
)
_STRONG_POSITIVE_CONTEXT_RE = re.compile(
    r"\b(?:our\s+code|code\s+(?:is|was)\s+available|implementation\s+(?:is|was)\s+available|"
    r"official\s+(?:code|implementation|repository)|source\s+code|open[- ]source|released\s+code|"
    r"project\s+page|we\s+(?:publicly\s+|openly\s+)?release|release\s+(?:data\s+and\s+)?code|"
    r"make\s+(?:code\s+)?(?:publicly\s+)?available|publicly\s+available)\b",
    re.IGNORECASE,
)
_CONTEXT_WINDOW = 220
_SCORING_WINDOW = 100
_MAX_README_CHARS = 12_000
_MAX_CANDIDATES = 6
_MIN_VERIFICATION_CONFIDENCE = 0.65
_GITHUB_API_HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Mozilla/5.0 (compatible; GraphBenchBot/1.0)",
}
_WEB_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; GraphBenchBot/1.0)"}
_KNOWN_REPO_HOSTS = frozenset(
    {
        "github.com",
        "www.github.com",
        "gitlab.com",
        "www.gitlab.com",
        "bitbucket.org",
        "www.bitbucket.org",
        "codeberg.org",
        "www.codeberg.org",
        "huggingface.co",
        "www.huggingface.co",
    }
)
_NON_REPO_HOSTS = frozenset(
    {
        "arxiv.org",
        "www.arxiv.org",
        "doi.org",
        "www.doi.org",
        "openreview.net",
        "www.openreview.net",
        "youtube.com",
        "www.youtube.com",
        "x.com",
        "twitter.com",
        "www.twitter.com",
    }
)
_GENERIC_PROJECT_PATH_RE = re.compile(
    r"/(?:code|codes?|source|sources?|repo|repos?|repository|implementation|project|software)\b",
    re.IGNORECASE,
)
_COMMON_TITLE_TOKENS = frozenset(
    {
        "graph",
        "graphs",
        "learning",
        "neural",
        "network",
        "networks",
        "transformer",
        "transformers",
        "benchmark",
        "benchmarks",
        "representation",
        "global",
        "generalizable",
        "insights",
        "theory",
        "practice",
        "model",
        "models",
        "message",
        "passing",
        "reasoning",
        "attention",
    }
)


def _clean_url(url: str) -> str:
    return url.strip().rstrip(").,;")


def _title_tokens(title: str) -> list[str]:
    return [token for token in re.findall(r"[A-Za-z0-9]+", title.lower()) if len(token) >= 4]


def _distinctive_title_tokens(title: str) -> list[str]:
    return [token for token in _title_tokens(title) if token not in _COMMON_TITLE_TOKENS]


def normalize_repository_url(url: str) -> str | None:
    """Collapse a candidate URL to a stable repository or project root when possible."""
    cleaned = _clean_url(url)
    parsed = urlparse(cleaned)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    host = parsed.netloc.lower()
    if host in _NON_REPO_HOSTS:
        return None

    path_parts = [part for part in parsed.path.split("/") if part]
    if host in _KNOWN_REPO_HOSTS:
        if len(path_parts) < 2:
            return None
        if host.endswith("huggingface.co") and path_parts[0] in {"spaces", "datasets"}:
            if len(path_parts) < 3:
                return None
            path = "/" + "/".join(path_parts[:3])
        else:
            path = "/" + "/".join(path_parts[:2])
        return urlunparse((parsed.scheme, parsed.netloc, path, "", "", ""))

    normalized = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))
    return normalized or cleaned


def normalize_github_repo_url(url: str) -> str | None:
    """Collapse a GitHub URL to its repository root."""
    match = _GITHUB_URL_RE.search(url.strip())
    if not match:
        return None
    owner = match.group("owner").strip().strip(".")
    repo = match.group("repo").strip().strip(".")
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo:
        return None
    return f"https://github.com/{owner}/{repo}"


def _context_score(context: str) -> int:
    score = 0
    if _POSITIVE_CONTEXT_RE.search(context):
        score += 3
    if _STRONG_POSITIVE_CONTEXT_RE.search(context):
        score += 3
    if re.search(r"\b(?:our|we|released?|open[- ]source)\b", context, re.IGNORECASE):
        score += 2
    if _NEGATIVE_CONTEXT_RE.search(context):
        score -= 2
    return score


def _candidate_host_priority(url: str) -> int:
    host = urlparse(url).netloc.lower()
    if host.endswith("github.com"):
        return 3
    if host in _KNOWN_REPO_HOSTS:
        return 2
    return 1


def _is_viable_candidate(url: str, context: str, score: int) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if host in _NON_REPO_HOSTS:
        return False
    if host in _KNOWN_REPO_HOSTS:
        return True
    return score >= 5 and bool(_GENERIC_PROJECT_PATH_RE.search(parsed.path))


def extract_repository_candidates(
    text: str, max_candidates: int = _MAX_CANDIDATES
) -> list[dict[str, Any]]:
    """Extract unique repository candidates plus nearby paper context."""
    if not text:
        return []

    candidates: dict[str, dict[str, Any]] = {}
    for match in _URL_RE.finditer(text):
        raw_url = match.group(0)
        normalized = normalize_repository_url(raw_url)
        if not normalized:
            continue
        start, end = match.span()
        raw_context = text[max(0, start - _CONTEXT_WINDOW) : min(len(text), end + _CONTEXT_WINDOW)]
        # Exclude the URL itself from scoring so path tokens (e.g. "Benchmark") don't skew scores.
        score_context = (
            text[max(0, start - _SCORING_WINDOW) : start]
            + " "
            + text[end : min(len(text), end + _SCORING_WINDOW)]
        )
        context = " ".join(raw_context.split())
        score = _context_score(score_context)
        if not _is_viable_candidate(normalized, context, score):
            continue
        existing = candidates.get(normalized)
        if existing is None:
            candidates[normalized] = {
                "url": normalized,
                "raw_url": _clean_url(raw_url),
                "paper_context": context[:800],
                "cue_score": score,
                "occurrences": 1,
                "first_pos": start,
            }
            continue
        existing["occurrences"] += 1
        if score > existing["cue_score"]:
            existing["paper_context"] = context[:800]
            existing["cue_score"] = score

    ordered = sorted(
        candidates.values(),
        key=lambda item: (
            -int(item["cue_score"]),
            -_candidate_host_priority(str(item["url"])),
            -int(item["occurrences"]),
            int(item["first_pos"]),
        ),
    )
    return [
        {
            "url": item["url"],
            "raw_url": item["raw_url"],
            "paper_context": item["paper_context"],
            "cue_score": item["cue_score"],
            "occurrences": item["occurrences"],
        }
        for item in ordered[:max_candidates]
    ]


def extract_github_repo_candidates(
    text: str, max_candidates: int = _MAX_CANDIDATES
) -> list[dict[str, Any]]:
    """Backward-compatible GitHub-only candidate extraction."""
    return [
        candidate
        for candidate in extract_repository_candidates(text, max_candidates=max_candidates * 2)
        if urlparse(candidate["url"]).netloc.lower().endswith("github.com")
    ][:max_candidates]


def repository_source_from_storage(
    storage: Any, fallback_text: str | None = None
) -> tuple[str, str]:
    """Return the preferred source text for repository extraction."""
    expanded_path = storage.latex_dir / "expanded.tex"
    if expanded_path.exists():
        try:
            return expanded_path.read_text(encoding="utf-8", errors="replace"), "latex"
        except OSError as exc:
            logger.debug("Could not read LaTeX source for repo extraction: %s", exc)
    if fallback_text and fallback_text.strip():
        return fallback_text, "paper_text"
    if storage.text_path.exists():
        try:
            return storage.text_path.read_text(encoding="utf-8", errors="replace"), "text_cache"
        except OSError as exc:
            logger.debug("Could not read cached text for repo extraction: %s", exc)
    return "", "none"


def _github_owner_repo(repo_url: str) -> tuple[str, str] | None:
    normalized = normalize_github_repo_url(repo_url)
    if not normalized:
        return None
    parts = normalized.removeprefix("https://github.com/").split("/")
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def fetch_github_repo_profile(repo_url: str) -> dict[str, str]:
    """Fetch basic repository metadata from the GitHub API."""
    owner_repo = _github_owner_repo(repo_url)
    if owner_repo is None:
        return {}
    owner, repo = owner_repo
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        resp = requests.get(api_url, headers=_GITHUB_API_HEADERS, timeout=20)
        if resp.status_code != 200:
            logger.info(
                "GitHub repo metadata unavailable for %s (status=%s)",
                repo_url,
                resp.status_code,
            )
            return {}
        raw = resp.json()
    except Exception as exc:
        logger.info("GitHub repo metadata request failed for %s: %s", repo_url, exc)
        return {}
    return {
        "normalized_url": str(raw.get("html_url") or repo_url).strip(),
        "description": str(raw.get("description") or "").strip(),
        "homepage": str(raw.get("homepage") or "").strip(),
        "default_branch": str(raw.get("default_branch") or "").strip(),
        "evidence_kind": "github_api",
    }


def fetch_github_readme(repo_url: str) -> dict[str, str]:
    """Fetch README text for a public GitHub repository."""
    owner_repo = _github_owner_repo(repo_url)
    if owner_repo is None:
        return {}
    owner, repo = owner_repo
    api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    try:
        resp = requests.get(api_url, headers=_GITHUB_API_HEADERS, timeout=20)
        if resp.status_code != 200:
            logger.info("GitHub README unavailable for %s (status=%s)", repo_url, resp.status_code)
            return {}
        raw = resp.json()
        content = base64.b64decode(raw.get("content", "")).decode("utf-8", errors="replace")
    except Exception as exc:
        logger.info("GitHub README request failed for %s: %s", repo_url, exc)
        return {}
    return {
        "path": str(raw.get("path") or raw.get("name") or "README"),
        "text": content[:_MAX_README_CHARS],
        "evidence_kind": "readme",
    }


def fetch_webpage_evidence(url: str) -> dict[str, str]:
    """Fetch visible text from a repository/project page for non-GitHub hosts."""
    try:
        resp = requests.get(url, headers=_WEB_HEADERS, timeout=20, allow_redirects=True)
        if resp.status_code != 200 or "html" not in resp.headers.get("Content-Type", "").lower():
            return {}
    except Exception as exc:
        logger.info("Repository page request failed for %s: %s", url, exc)
        return {}

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    body_text = " ".join(soup.get_text(" ", strip=True).split())
    meta_desc = ""
    meta = soup.find("meta", attrs={"name": "description"}) or soup.find(
        "meta", attrs={"property": "og:description"}
    )
    if meta and meta.get("content"):
        meta_desc = str(meta["content"]).strip()
    combined = "\n".join(part for part in [title, meta_desc, body_text[:_MAX_README_CHARS]] if part)
    return {
        "path": "page",
        "text": combined[:_MAX_README_CHARS],
        "evidence_kind": "page",
        "normalized_url": resp.url or url,
    }


def fetch_repository_profile(repo_url: str) -> dict[str, str]:
    """Fetch repository metadata/profile from the best available source."""
    host = urlparse(repo_url).netloc.lower()
    if host.endswith("github.com"):
        return fetch_github_repo_profile(repo_url)
    return {
        "normalized_url": repo_url,
        "description": "",
        "homepage": "",
        "default_branch": "",
        "evidence_kind": "url",
    }


def fetch_repository_evidence(repo_url: str) -> dict[str, str]:
    """Fetch README or page text for a repository candidate."""
    host = urlparse(repo_url).netloc.lower()
    if host.endswith("github.com"):
        readme = fetch_github_readme(repo_url)
        if readme.get("text"):
            return readme
    return fetch_webpage_evidence(repo_url)


def _heuristic_repository_verdict(
    *,
    arxiv_id: str,
    paper_title: str,
    candidate: dict[str, Any],
    repo_profile: dict[str, str],
    evidence: dict[str, str],
) -> dict[str, Any]:
    evidence_text = " ".join(
        part for part in [repo_profile.get("description", ""), evidence.get("text", "")] if part
    ).lower()
    title_tokens = _distinctive_title_tokens(paper_title) or _title_tokens(paper_title)
    matched_tokens = [token for token in title_tokens if token in evidence_text][:6]
    repo_name = (
        urlparse(candidate["url"]).path.rstrip("/").split("/")[-1] if candidate.get("url") else ""
    ).lower()
    score = float(candidate.get("cue_score") or 0)
    reasons: list[str] = []

    if arxiv_id and arxiv_id in evidence_text:
        score += 5
        reasons.append("repository page mentions the paper arXiv id")
    if paper_title and paper_title.lower() in evidence_text:
        score += 5
        reasons.append("repository page contains the exact paper title")
    if repo_name and any(
        token == repo_name or repo_name in token or token in repo_name for token in title_tokens
    ):
        score += 3
        reasons.append("repository name matches the paper's method/title")
    if len(matched_tokens) >= 3:
        score += 4
        reasons.append("repository page matches several paper-title tokens")
    elif len(matched_tokens) >= 2:
        score += 2
        reasons.append("repository page matches the paper title")
    if re.search(
        r"\b(?:official implementation|source code|code for|implementation of)\b", evidence_text
    ):
        score += 3
        reasons.append("repository page explicitly says it is code for the method/paper")
    if candidate.get("cue_score", 0) >= 5:
        reasons.append("paper text links it in strong code-availability context")
    if _NEGATIVE_CONTEXT_RE.search(evidence_text):
        score -= 3

    belongs = score >= 7 and (
        candidate.get("cue_score", 0) >= 5
        or (arxiv_id and arxiv_id in evidence_text)
        or any("repository name matches" in reason for reason in reasons)
        or paper_title.lower() in evidence_text
    )
    confidence = min(0.95, max(0.05, score / 10.0))
    reason = (
        "; ".join(reasons)
        if reasons
        else "No strong match between the repository page and the paper could be established."
    )
    return {
        "url": evidence.get("normalized_url")
        or repo_profile.get("normalized_url")
        or candidate["url"],
        "belongs_to_paper": belongs,
        "confidence": confidence if belongs else min(confidence, 0.49),
        "reason": reason,
        "evidence": reasons[:5],
        "paper_context": candidate.get("paper_context") or "",
        "repo_description": repo_profile.get("description") or "",
        "readme_path": evidence.get("path") or "",
        "evidence_kind": evidence.get("evidence_kind") or "heuristic",
    }


def verify_repository_candidate(
    *,
    llm_verifier: Any | None,
    arxiv_id: str,
    paper_title: str,
    paper_abstract: str,
    candidate: dict[str, Any],
    repo_profile: dict[str, str],
    readme: dict[str, str],
) -> dict[str, Any]:
    """Ask an LLM whether a candidate repository belongs to this paper."""
    if llm_verifier is None:
        return _heuristic_repository_verdict(
            arxiv_id=arxiv_id,
            paper_title=paper_title,
            candidate=candidate,
            repo_profile=repo_profile,
            evidence=readme,
        )
    prompt = llm_verifier._read_prompt("repository_verification.txt")
    user_content = "\n\n".join(
        [
            f"Paper arXiv ID: {arxiv_id or 'unknown'}",
            f"Paper title: {paper_title or 'unknown'}",
            f"Paper abstract:\n{paper_abstract or '(not available)'}",
            f"Candidate repository URL: {repo_profile.get('normalized_url') or candidate['url']}",
            f"Paper context around URL:\n{candidate.get('paper_context') or '(not available)'}",
            f"Repository description: {repo_profile.get('description') or '(empty)'}",
            f"Repository homepage: {repo_profile.get('homepage') or '(empty)'}",
            f"Repository evidence type: {readme.get('evidence_kind') or 'unknown'}",
            f"Repository evidence path: {readme.get('path') or '(unknown)'}",
            f"Repository evidence excerpt:\n{readme.get('text') or '(empty)'}",
        ]
    )
    try:
        raw = llm_verifier._call_json(
            prompt,
            user_content,
            max_tokens=512,
            call_type="verify_repository",
            call_extra={"repo_candidate": candidate["url"]},
        )
    except Exception:
        logger.warning(
            "LLM repository verification failed for %s; falling back to heuristics",
            candidate["url"],
        )
        return _heuristic_repository_verdict(
            arxiv_id=arxiv_id,
            paper_title=paper_title,
            candidate=candidate,
            repo_profile=repo_profile,
            evidence=readme,
        )
    belongs = bool(raw.get("belongs_to_paper"))
    try:
        confidence = float(raw.get("confidence") or 0.0)
    except (TypeError, ValueError):
        confidence = 0.0
    evidence_raw = raw.get("evidence") or []
    evidence = [str(item).strip() for item in evidence_raw if str(item).strip()]
    return {
        "url": repo_profile.get("normalized_url") or candidate["url"],
        "belongs_to_paper": belongs,
        "confidence": confidence,
        "reason": str(raw.get("reason") or "").strip(),
        "evidence": evidence[:5],
        "paper_context": candidate.get("paper_context") or "",
        "repo_description": repo_profile.get("description") or "",
        "readme_path": readme.get("path") or "",
        "evidence_kind": readme.get("evidence_kind") or "readme",
    }


def find_verified_repository_link(
    *,
    llm_verifier: Any | None,
    arxiv_id: str,
    paper_title: str,
    paper_abstract: str,
    source_text: str,
    source_kind: str,
    max_candidates: int = _MAX_CANDIDATES,
) -> dict[str, Any]:
    """Return the first verified repository linked in the paper."""
    candidates = extract_repository_candidates(source_text, max_candidates=max_candidates)
    result: dict[str, Any] = {
        "verified_url": None,
        "confidence": 0.0,
        "reason": "",
        "verification_model": str(getattr(llm_verifier, "model_name", "") or ""),
        "source_kind": source_kind,
        "candidate_urls": [candidate["url"] for candidate in candidates],
        "checked_candidates": [],
    }
    if not candidates:
        result["reason"] = "No repository links found in the available paper source."
        return result

    best_verified: dict[str, Any] | None = None
    for candidate in candidates:
        repo_profile = fetch_repository_profile(candidate["url"])
        evidence = fetch_repository_evidence(repo_profile.get("normalized_url") or candidate["url"])
        if not evidence.get("text") and int(candidate.get("cue_score") or 0) < 5:
            result["checked_candidates"].append(
                {
                    "url": repo_profile.get("normalized_url") or candidate["url"],
                    "belongs_to_paper": False,
                    "confidence": 0.0,
                    "reason": "Could not fetch repository evidence and paper context was not strong enough.",
                    "paper_context": candidate.get("paper_context") or "",
                    "repo_description": repo_profile.get("description") or "",
                    "readme_path": evidence.get("path") or "",
                    "evidence_kind": evidence.get("evidence_kind") or "",
                }
            )
            continue

        verdict = verify_repository_candidate(
            llm_verifier=llm_verifier,
            arxiv_id=arxiv_id,
            paper_title=paper_title,
            paper_abstract=paper_abstract,
            candidate=candidate,
            repo_profile=repo_profile,
            readme=evidence,
        )
        result["checked_candidates"].append(verdict)
        if verdict["belongs_to_paper"] and verdict["confidence"] >= _MIN_VERIFICATION_CONFIDENCE:
            if best_verified is None or float(verdict["confidence"]) > float(
                best_verified["confidence"]
            ):
                best_verified = verdict

    if best_verified is not None:
        result["verified_url"] = best_verified["url"]
        result["confidence"] = best_verified["confidence"]
        result["reason"] = best_verified["reason"]
        return result

    if result["checked_candidates"]:
        best = max(
            result["checked_candidates"], key=lambda item: float(item.get("confidence") or 0.0)
        )
        result["confidence"] = float(best.get("confidence") or 0.0)
        result["reason"] = str(best.get("reason") or "No candidate repository could be verified.")
    else:
        result["reason"] = "No repository candidates could be checked successfully."
    return result
