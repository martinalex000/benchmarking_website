"""Save-only, resumable repetition assessments for all papers with stored results."""

from __future__ import annotations

import fcntl
import hashlib
import json
import logging
import os
import shutil
import sqlite3
import time
from collections import Counter, deque
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import UTC, datetime
from pathlib import Path

from backend.config import cfg
from backend.repetition_batch import RequestGate, write_json
from backend.repetition_extractor import DEFAULT_MODEL, extract_repetition_metadata
from backend.repetition_metadata import RepetitionFacts, Verification, validate_repetitions

ROOT = cfg.papers_dir / "repetition_backfill_all_stored_results"
PRIOR_ROOTS = (
    cfg.papers_dir / "repetition_backfill",
    cfg.papers_dir / "repetition_backfill_large_budget_retry",
)
MAX_TOTAL = 1_000_000
MAX_COMPLETION = 128_000
TIMEOUT = 1_800
LOG = logging.getLogger(__name__)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def readonly_connection() -> sqlite3.Connection:
    return sqlite3.connect(f"file:{cfg.db_path}?mode=ro", uri=True)


def select_external_glm_only() -> None:
    """Skip broad model discovery and bind the extractor to the authorized route."""
    import backend.llm_tasks as llm_tasks
    from backend.llm_backends import LlmBackend, ModelRoute

    endpoint = (cfg.llm_endpoint or "").strip()
    if not endpoint:
        raise RuntimeError("No external LLM endpoint is configured")
    backend = LlmBackend("external", endpoint, cfg.llm_api_key or "none")
    route = ModelRoute(DEFAULT_MODEL, backend)

    def params(model_name: str, routes=None):
        if model_name != DEFAULT_MODEL:
            raise ValueError(f"Only {DEFAULT_MODEL} is authorized for this backfill")
        return endpoint, backend.api_key, route

    # LLMExtractor imports this resolver at module load; replace only that binding.
    llm_tasks.client_params_for_model = params


def stored_result_cohort() -> list[dict]:
    """Include every identified paper with at least one result, independent of venue."""
    with readonly_connection() as connection:
        papers = connection.execute(
            """SELECT p.id, p.arxiv_id, p.title, p.venue, p.published_date
               FROM papers p WHERE p.arxiv_id IS NOT NULL
               AND EXISTS (SELECT 1 FROM results r WHERE r.paper_id = p.id)
               ORDER BY p.arxiv_id"""
        ).fetchall()
        result = []
        for paper_id, arxiv_id, title, venue, published_date in papers:
            hints = [
                row[0]
                for row in connection.execute(
                    """SELECT COALESCE(NULLIF(r.model_name_override, ''), m.name)
                       FROM results r JOIN models m ON m.id = r.model_id
                       WHERE r.paper_id = ? ORDER BY 1""",
                    (paper_id,),
                )
            ]
            result.append(
                {
                    "paper_id": arxiv_id,
                    "title": title,
                    "venue": venue,
                    "published_date": published_date,
                    "hints": sorted(set(hints)),
                }
            )
    return result


def freeze_prompts() -> Path:
    folder = ROOT / "prompts"
    folder.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).parents[2] / "backend" / "prompts"
    for name in ("repetition_metadata.txt", "repetition_verification.txt"):
        original = (source / name).read_bytes()
        target = folder / name
        if target.exists() and target.read_bytes() != original:
            raise ValueError("Frozen prompts differ; use a new output directory")
        if not target.exists():
            target.write_bytes(original)
    return folder


def prompt_hashes(prompts: Path) -> dict:
    return {
        "facts": sha256((prompts / "repetition_metadata.txt").read_text()),
        "verification": sha256((prompts / "repetition_verification.txt").read_text()),
    }


def classify(analysis: dict, source: str) -> str:
    """Mirror the guarded paper-level labels without applying anything to stored rows."""
    if analysis.get("error"):
        return "failed"
    validated = analysis["validated"]
    coverage = validated.get("coverage", {})
    if any(coverage.values()):
        return "table_dependent"
    outcomes = validated["table_outcomes"]
    benchmarks = [table for table in outcomes if table["outcome"] != "excluded"]
    if not benchmarks or all(table["outcome"] == "unknown" for table in benchmarks):
        return "unknown"
    if any(table["outcome"] != "count" for table in benchmarks):
        return "table_dependent"
    protocols = {
        (item["repetitions"], item["cv_folds"], item["design"])
        for item in validated.get("accepted", [])
    }
    if len(protocols) != 1:
        return "table_dependent"
    count = next(iter(protocols))[0]
    if any(
        item.get("candidate_repetitions") is not None and item.get("candidate_repetitions") != count
        for item in validated.get("withheld", [])
        if item["origin"] == "self_evaluated"
        and "ablation_variant_not_eligible" not in item["flags"]
    ):
        return "table_dependent"
    return "uniform"


def revalidate(analysis: dict, source: str) -> dict:
    """Re-run deterministic source checks before any assessment is counted as successful."""
    if analysis.get("error"):
        return analysis
    if analysis["provenance"].get("model") != DEFAULT_MODEL:
        raise ValueError("Assessment model is not the required GLM-5.3-Flash")
    facts = RepetitionFacts.model_validate(analysis["facts"])
    verification = Verification.model_validate(analysis["verification"])
    analysis["validated"] = validate_repetitions(facts, verification, source)
    return analysis


def compatible_analysis(
    candidate: Path, source: str, hashes: dict, expected_id: str
) -> dict | None:
    analysis_path = candidate / "analysis.json"
    source_path = candidate / "source.tex"
    if not analysis_path.exists() or not source_path.exists():
        return None
    try:
        saved_source = source_path.read_text()
        analysis = json.loads(analysis_path.read_text())
        provenance = analysis["provenance"]
        if (
            saved_source != source
            or provenance.get("source_sha256") != sha256(source)
            or provenance.get("prompt_sha256") != hashes
            or provenance.get("model") != DEFAULT_MODEL
            or provenance.get("paper_id") != expected_id
            or analysis.get("error")
            or not (candidate / "call_1.json").exists()
            or not (candidate / "call_2.json").exists()
        ):
            return None
        return revalidate(analysis, source)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError):
        return None


def persist_attempt(folder: Path, attempt_name: str, analysis: dict) -> Path:
    attempt = folder / attempt_name
    attempt.mkdir(parents=True, exist_ok=True)
    calls = analysis.pop("calls", [])
    for index, call in enumerate(calls, 1):
        write_json(attempt / f"call_{index}.json", call)
    write_json(attempt / "analysis.json", analysis)
    return attempt / "analysis.json"


def analyze(paper: dict, prompts: Path, hashes: dict, gate: RequestGate) -> dict:
    pid = paper["paper_id"]
    source_path = cfg.papers_dir / pid / "latex" / "expanded.tex"
    folder = ROOT / "papers" / pid
    folder.mkdir(parents=True, exist_ok=True)
    if not source_path.exists():
        error = "Missing expanded LaTeX source"
        evidence = folder / "analysis.json"
        write_json(evidence, {"paper_id": pid, "error": error, "validated": {"accepted": []}})
        return {"paper_id": pid, "status": "failed", "error": error, "analysis": str(evidence)}
    source = source_path.read_text()
    (folder / "source.tex").write_text(source)
    for old_root in PRIOR_ROOTS:
        candidate = old_root / "papers" / pid
        analysis = compatible_analysis(candidate, source, hashes, pid)
        if analysis is not None:
            if folder.exists():
                shutil.rmtree(folder)
            shutil.copytree(candidate, folder)
            copied = json.loads((folder / "analysis.json").read_text())
            copied = revalidate(copied, source)
            write_json(folder / "analysis.json", copied)
            return {
                "paper_id": pid,
                "status": classify(copied, source),
                "analysis": str(folder / "analysis.json"),
                "reused_from": str(candidate),
                "cached": True,
                "table_outcomes": len(copied["validated"].get("table_outcomes", [])),
            }
    analysis_path = folder / "analysis.json"
    if analysis_path.exists():
        existing = compatible_analysis(folder, source, hashes, pid)
        if existing is not None:
            return {
                "paper_id": pid,
                "status": classify(existing, source),
                "analysis": str(analysis_path),
                "cached": True,
                "table_outcomes": len(existing["validated"].get("table_outcomes", [])),
            }
        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%f")
        archive = ROOT / "attempt_history" / pid / stamp
        archive.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            folder,
            archive,
            ignore=shutil.ignore_patterns("history"),
            copy_function=os.link,
        )
    attempts = []
    for thinking in (True, False):
        analysis = extract_repetition_metadata(
            source,
            paper_id=pid,
            hints=paper["hints"],
            model=DEFAULT_MODEL,
            enable_reasoning=thinking,
            max_tokens=MAX_COMPLETION,
            max_total_tokens=MAX_TOTAL,
            request_timeout_seconds=TIMEOUT,
            prompt_directory=prompts,
            request_gate=gate,
        )
        attempt_name = "thinking_attempt" if thinking else "no_thinking_attempt"
        analysis_path = persist_attempt(folder, attempt_name, analysis)
        attempts.append(analysis_path)
        attempt_data = json.loads(analysis_path.read_text())
        if not (thinking and "Reasoning exhausted" in attempt_data.get("error", "")):
            analysis = attempt_data
            break
    # Publish the final attempt at the stable path while retaining every raw attempt.
    analysis_path = folder / "analysis.json"
    write_json(analysis_path, analysis)
    for attempt_path in attempts[-1].parent.glob("call_*.json"):
        # Per-attempt calls remain authoritative; stable copies ease legacy inspection.
        target = folder / attempt_path.name
        if attempt_path != target:
            shutil.copy2(attempt_path, target)
    result = {"paper_id": pid, "analysis": str(analysis_path), "cached": False}
    if analysis.get("error"):
        result.update(status="failed", error=analysis["error"])
    else:
        analysis = revalidate(analysis, source)
        write_json(analysis_path, analysis)
        result.update(
            status=classify(analysis, source),
            table_outcomes=len(analysis["validated"].get("table_outcomes", [])),
        )
    return result


def table_summary(results: dict) -> dict:
    counts: Counter = Counter()
    for item in results.values():
        if item.get("status") == "failed" or not item.get("analysis"):
            continue
        path = Path(item["analysis"])
        try:
            analysis = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        # Inspect saved error fields before considering any assessment successful.
        if analysis.get("error"):
            continue
        for table in analysis.get("validated", {}).get("table_outcomes", []):
            counts[table.get("outcome", "special")] += 1
    return dict(counts)


def save_progress(state: dict, gate: RequestGate) -> None:
    statuses = Counter(item["status"] for item in state["results"].values())
    with gate.condition:
        active = gate.active
        limit = gate.limit
        cooldown = max(0, round(gate.cooldown_until - time.monotonic()))
        rate_limits = gate.rate_limits
    state.update(
        updated_at=datetime.now(UTC).isoformat(),
        completed=len(state["results"]),
        categories=dict(statuses),
        table_outcomes=table_summary(state["results"]),
        active_requests=active,
        request_limit=limit,
        rate_limits=rate_limits,
        cooldown_seconds=cooldown,
    )
    write_json(ROOT / "status.json", state)
    report = [
        "# Paper-level repetition backfill: all stored-result papers",
        "",
        f"Updated {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')}; state: {state['state']}.",
        f"Cohort: {state['total']} papers with stored results, irrespective of exported conference label.",
        f"Completed {state['completed']}/{state['total']}; classifications: {dict(statuses)}.",
        f"Table outcomes (coverage, separate from fact acceptance): {state['table_outcomes']}.",
        f"Active local request streams: {active}/{limit}; 429s: {rate_limits}; cooldown remaining: {cooldown}s.",
        "Model: zai-org/GLM-5.3-Flash; unchanged frozen prompts; 1,000,000 total tokens; 128,000 completion tokens per call; 1,800-second timeout.",
        "Schedule: one request 08:00–23:00 and up to 20 requests 23:00–08:00 Europe/Berlin; shared local 429 retry-after cooldown.",
        "Save-only: no database writes, run-count assignments, result changes or statistics.",
        "",
        "## Paper evidence",
        "",
    ]
    for pid in sorted(state["results"]):
        item = state["results"][pid]
        report.append(
            f"- [{pid}](papers/{pid}/analysis.json): {item['status']}; error: {item.get('error') or 'none'}"
        )
    (ROOT / "report.md").write_text("\n".join(report) + "\n")


def run() -> dict:
    ROOT.mkdir(parents=True, exist_ok=True)
    with (ROOT / "batch.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        select_external_glm_only()
        prompts = freeze_prompts()
        hashes = prompt_hashes(prompts)
        papers = stored_result_cohort()
        manifest_path = ROOT / "manifest.json"
        manifest = {
            "cohort_definition": "all papers with at least one stored result; no venue/conference filter",
            "model": DEFAULT_MODEL,
            "papers": papers,
            "prior_sources": [str(path) for path in PRIOR_ROOTS],
            "reused_only_when": "source, paper id, model, frozen prompt hashes match; saved error field empty",
            "prompt_sha256": hashes,
            "schedule_timezone": "Europe/Berlin",
            "day_request_limit": 1,
            "night_request_limit": 20,
            "max_total_tokens": MAX_TOTAL,
            "max_completion_tokens": MAX_COMPLETION,
            "request_timeout_seconds": TIMEOUT,
            "database_writes": False,
        }
        if manifest_path.exists() and json.loads(manifest_path.read_text()) != manifest:
            raise ValueError(
                "Cohort or provenance changed; preserve this run and use a fresh directory"
            )
        write_json(manifest_path, manifest)
        prior_state_path = ROOT / "status.json"
        state = (
            json.loads(prior_state_path.read_text())
            if prior_state_path.exists()
            else {
                "state": "running",
                "total": len(papers),
                "active": 0,
                "results": {},
                "started_at": datetime.now(UTC).isoformat(),
            }
        )
        if state.get("total") != len(papers):
            raise ValueError("Saved cohort total changed; use a fresh output directory")
        # Rebuild reusable results from checked per-paper evidence, not status labels alone.
        results = state.get("results", {})
        for paper in papers:
            pid = paper["paper_id"]
            source_path = cfg.papers_dir / pid / "latex" / "expanded.tex"
            if not source_path.exists():
                folder = ROOT / "papers" / pid
                folder.mkdir(parents=True, exist_ok=True)
                evidence = folder / "analysis.json"
                error = "Missing expanded LaTeX source"
                write_json(
                    evidence, {"paper_id": pid, "error": error, "validated": {"accepted": []}}
                )
                results[pid] = {
                    "paper_id": pid,
                    "status": "failed",
                    "error": error,
                    "analysis": str(evidence),
                }
                continue
            source = source_path.read_text()
            analysis_path = ROOT / "papers" / pid / "analysis.json"
            if analysis_path.exists():
                verified = compatible_analysis(analysis_path.parent, source, hashes, pid)
                if verified:
                    results[pid] = {
                        "paper_id": pid,
                        "status": classify(verified, source),
                        "analysis": str(analysis_path),
                        "cached": True,
                    }
                else:
                    results.pop(pid, None)
        pending = [paper for paper in papers if paper["paper_id"] not in results]
        state.update(state="running", pid=os.getpid(), total=len(papers), results=results)
        gate = RequestGate(maximum=20)
        save_progress(state, gate)
        queue = deque(pending)
        futures = {}
        with ThreadPoolExecutor(max_workers=20) as pool:
            while queue or futures:
                while queue and len(futures) < 20:
                    paper = queue.popleft()
                    futures[pool.submit(analyze, paper, prompts, hashes, gate)] = paper
                state["active"] = len(futures)
                save_progress(state, gate)
                completed, _ = wait(futures, timeout=5, return_when=FIRST_COMPLETED)
                for future in completed:
                    paper = futures.pop(future)
                    pid = paper["paper_id"]
                    try:
                        result = future.result()
                    except Exception as exc:
                        LOG.exception("Save-only repetition assessment failed for %s", pid)
                        folder = ROOT / "papers" / pid
                        folder.mkdir(parents=True, exist_ok=True)
                        evidence = folder / "analysis.json"
                        failure = {"paper_id": pid, "error": f"{type(exc).__name__}: {exc}"}
                        write_json(evidence, failure)
                        result = {
                            "paper_id": pid,
                            "status": "failed",
                            "error": failure["error"],
                            "analysis": str(evidence),
                        }
                    results[pid] = result
                    state["results"] = results
                    save_progress(state, gate)
        state.update(state="finished", active=0)
        save_progress(state, gate)
        return state


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    run()
