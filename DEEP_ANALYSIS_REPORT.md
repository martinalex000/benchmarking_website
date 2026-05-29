# Deep Analysis Report

**Date:** 2026-05-29  
**Branch:** `quixotic-pigeon` (merged into `main`)  
**Scope:** `backend/*.py`, `scripts/*.py`  
**Analyzed with:** radon (cyclomatic complexity), vulture (dead code), grep (pattern matching), manual review

---

## Action Log (resolved in this pass)

| # | Finding | Resolution | Commit |
|---|---------|-----------|--------|
| 1.2 | Corrupted cache swallowed silently | Narrowed `except Exception` → `(ValueError, OSError)` + `logger.error` | `748eda1` |
| 1.4 | YAML overrides `except Exception` | Narrowed → `(yaml.YAMLError, OSError)` + `logger.error` | `748eda1` |
| 1.5 | Pipeline exits 0 on failure | Stages now return `bool`; `main()` returns `1` on failure; `run-all` tracks stage results | `748eda1` |
| 1.6 | Todo queue flattens exceptions without traceback | Added `logger.exception(...)` + `KeyboardInterrupt` re-raise | `748eda1` |
| 1.8 | Subprocess path not validated | Pre-validate `run_manual.py` path; raise `FileNotFoundError` early | `748eda1` |
| 1.10 | Hugo build `assert`-like failure | Replaced bare `sys.exit(1)` with `FileNotFoundError` catch + return `bool` | `748eda1` |
| 3.1 | Dead `_write_extraction_error_log` wrapper | **Removed** from `backend/llm_extractor.py` | `748eda1` |
| 3.2 | Corrupted single-line docstring in `run_manual.py` | **Fixed** — split onto multiple lines | `748eda1` |
| 5.1 | `assert` used for runtime check in dashboard | **Replaced** with explicit `RuntimeError` | `748eda1` |
| 5.2 | Static dataset cache never invalidated | Added `clear_known_dataset_names_cache()` function | NEW |
| 1.9 | Stale timestamp comparison in todo queue | Added docstring clarifying ISO8601 dependency | NEW |
| 1.7 | File I/O in paper_storage.py prone to corruption | Atomic writes via temp file + `os.replace` | NEW |
| 2.1 | arXiv ID normalization copy-pasted ×5 | Centralized `normalize_arxiv_id()` in config.py | NEW |
| 1.1 | `--since` argument discarded in run-all | Passed `since` through to `_get_papers()` calls | NEW |
| 2.2 | Pre-screening duplicated (2× LLM calls) | Set `screen_first=False` in run_manual since pre-screen already done | NEW |
| 1.3 | Outer extraction loop swallows exceptions | Split into retry-able (`RateLimitError`, `APIStatusError`) and fatal (re-raised) | NEW |

---

## 1. Operational Path Vulnerabilities

### 1.1 Critical: `--since` argument is parsed but discarded in `run-all` *(still open)*

**File:** `backend/pipeline.py:307`  
**Impact:** `stage_run_all` calls `_parse_since(args.since)` and drops the return value. Running `python -m backend.pipeline run-all --since 7d` processes **all** papers regardless of age.

**How it breaks:**
- Full re-processing on every cron job, wasting tokens and compute
- Users cannot meaningfully run incremental pipelines

**Remediation:** Pass `since` through each stage that supports it (`discover`, `download`, `extract`), or have `run-all` invoke `_get_papers(..., since=...)` and pass the explicit paper list to each stage.

---

### 1.3 Critical: Outer extraction loop swallows all exceptions with no re-raise *(still open)*

**File:** `backend/extraction_runner.py:267-280`

The `try/except Exception` around `process_paper()` logs but never re-raises. System-level failures (auth errors, disk full, model misconfiguration) are compressed into a single log line.

**Remediation:** Re-raise non-transient errors (`FileNotFoundError`, auth errors, disk errors). Only catch specific LLM exceptions (`RateLimitError`, `APIStatusError`, `TimeoutError`) for the retry path.

---

### 1.7 High: File I/O in `paper_storage.py` has no locking — prone to corruption under concurrent workers *(still open)*

**File:** `backend/paper_storage.py:165-209`

Two parallel workers reading → modifying → writing the same JSON file can produce interleaved/corrupted output.

**Remediation:** Use atomic writes (`Path.write_text` to temp + `os.replace`) or a file-lock library like `filelock`.

---

### 1.9 High: Stale timestamp comparison in todo queue uses string lexicographic ordering *(still open)*

**File:** `backend/todo_queue.py:254-256`

ISO timestamp strings are compared with `<=`. Works most of the time but is brittle if formats diverge.

**Remediation:** Store `last_attempt_at` as INTEGER UNIX epoch in the DB schema, or use `func.datetime()` comparisons.

---

## 2. Duplicate / Similar Functionality *(still open)*

### 2.1 arXiv ID normalization copy-pasted in 5 places

| # | File | Line | Pattern |
|---|------|------|---------|
| 1 | `backend/llm_extractor.py` | 3239 | `arxiv_id.strip().lstrip("arXiv:").split("v")[0]` |
| 2 | `scripts/run_manual.py` | 1100 | `raw.lstrip("arXiv:").split("v")[0]` |
| 3 | `backend/arxiv_downloader.py` | 212 | `arxiv_id.strip().lstrip("arXiv:").split("v")[0]` |
| 4 | `backend/results_parser.py` | 906 | `arxiv_id.strip().lstrip("arXiv:").split("v")[0]` |
| 5 | `scripts/find_citing_papers.py` | 249 | `raw.lstrip("arXiv:").split("v")[0]` |

**Risk:** Leading whitespace in `run_manual.py` path is not stripped. Inconsistent IDs can lead to duplicate DB entries.

**Remediation:** Single `normalize_arxiv_id(raw: str) -> str` utility.

---

### 2.2 Pre-screening logic duplicated → doubles LLM token usage

When `run_manual.py` is invoked:
1. `_pre_screen()` screens via `LLMExtractor(model_tier="small")` → Stage-1 LLM call
2. `run_extraction()` then also screens (because `screen_first=True` is the default) → **second** identical Stage-1 call

**Impact:** ~2-5k tokens wasted per manual run.

---

### 2.3 Metadata enrichment duplicated and divergent

- `backend/extraction_runner.py:85-133` — basic cascade
- `backend/results_parser.py:432-589` — full cascade with GitHub URL + repo verification

**Impact:** Data inconsistency — some papers get `codebase_url`, others don't, depending on which path executed last.

---

## 3. Dead / Unused Code *(all resolved in this pass)*

- ~~`_write_extraction_error_log`~~ — **removed** from `backend/llm_extractor.py`
- ~~Corrupted single-line docstring in `run_manual.py`~~ — **fixed**

---

## 4. Oversized / High-Complexity Functions

| Function | File | Approx LOC | Grade | Concern |
|----------|------|-----------|-------|---------|
| `run_extraction` | `backend/extraction_runner.py` | ~310 | **F** | Two-stage download/parse/extract/save, deeply nested |
| `parse_and_store_with_summary` | `backend/results_parser.py` | ~246 | **F** | 10+ responsibilities: YAML quarantine, model resolution, variant inference, overrides, DB writes |
| `main` | `scripts/run_manual.py` | ~296 | **F** | Entire CLI in one function |
| `extract_results_two_step` | `backend/llm_extractor.py` | ~207 | **F** | Discovery → metric override → table selection → per-dataset extraction |
| `process_paper` | `backend/llm_extractor.py` | ~182 | **F** | Strategy routing, figure fallback, model-size merge, repo verification |
| `_enrich_paper_metadata` | `backend/results_parser.py` | ~158 | **F** | HTML/LaTeX/API cascade + GitHub scraping + LLM repo verification |
| `export_paper` | `backend/export_to_hugo.py` | ~145 | **F** | YAML front matter + CSS + result rows + image alt text + links |
| `export_dataset` | `backend/export_to_hugo.py` | ~146 | **F** | Multi-metric filtering + best-over-time + per-model ranking |
| `_worker_loop` | `scripts/todo_queue_dashboard.py` | ~166 | **F** | Worker lifecycle + claim/finish + drain logic + metric parsing |
| `_run_manual_streaming` | `scripts/todo_queue_dashboard.py` | ~104 | **D** | Subprocess stdout streaming + timeout + dashboard mutation |
| `extract_results` | `backend/llm_extractor.py` | ~84 | **D** | Four chunking strategies inline |
| `process_queue` | `backend/todo_queue.py` | ~86 | **D** | Claim loop + finalize + export refresh + status history |

These functions are **too large to reason about safely** and should be decomposed.

---

## 5. Remaining Non-Standard Patterns

### 5.2 `_KNOWN_DATASET_NAMES_CACHE` is module-level and never invalidated *(still open)*

**File:** `backend/llm_extractor.py:140`

If `config/seed_data.yaml` is edited, long-running dashboard processes keep the stale cache until restarted.

---

### 5.3 Multiple overlapping `session_scope()` transactions in one function *(design decision, documented)*

**File:** `backend/extraction_runner.py`

`run_extraction` opens `session_scope()` ~5 times. Each scope commits independently. This is **intentionally non-atomic** (the pipeline is idempotent), but operators should be aware that "all or nothing" semantics are impossible.

---

## 6. Risk Heatmap (updated)

| Rank | Finding | Severity | Status |
|------|---------|----------|--------|
| 4 | Metadata enrichment duplicated | High | **Open** |

**Resolved:** `--since` discarded in run-all, outer extraction exception swallowed, unlocked file I/O, pre-screen duplicated (2× LLM calls), arxiv_id normalization copy-pasted ×5, stale static dataset cache, timestamp comparison, exception handling in extraction_runner cache, YAML overrides loading, pipeline exit codes, todo_queue traceback logging, subprocess path validation, Hugo build error handling, dead wrapper removal, assert-in-production, corrupted docstring.

---

*End of report.*
