# Bug & Regression Report

**Repository:** benchmarking-website  
**Branch:** `quixotic-pigeon`  
**Date:** 2026-05-29  
**Scope:** Full repository scan (backend, scripts, tests, site)

---

## Executive Summary

A systematic static-analysis pass and targeted manual review uncovered **two confirmed regressions (failing tests)**, **several latent runtime bugs**, **multiple medium-severity security issues**, and **widespread type-safety violations** (800+). The codebase also carries a high volume of `except Exception` swallow patterns that mask real failures and make debugging the pipeline unnecessarily difficult.

### Missing Static-Analysis Tooling in the Current UV Venv

The project’s `pyproject.toml` only lists `pytest`, `pytest-mock`, `black` and `pre-commit` in the `dev` dependency group. The following tools were **not present** and had to be installed ad-hoc for this review:

| Tool | Version Installed | What it caught here |
|------|------------------|---------------------|
| **ruff** | 0.15.15 | 55 style / import / unused-variable issues |
| **mypy** | 2.1.0 | 223 strict typing errors (mostly `Column[T]` vs bare `T`) |
| **pyright** | 1.1.409 | 338 type errors (same family, stricter in some areas) |
| **bandit** | 1.9.4 | 3 Medium-severity security findings |
| **pylint** | 4.0.5 | Architectural smells (too-many-locals, import-outside-toplevel, etc.) |
| **flake8** | 7.3.0 | 200+ style issues (line length, import ordering, W503) |

*Recommendation:* Add at least `ruff`, `mypy` and `bandit` to the `dev` dependency group so CI can gate on them.

---

## 1. Confirmed Regressions (Failing Tests)

### 1.1 Parse stage mis-records failure for empty-extraction papers

**Test:** `tests/integration/test_pipeline_extract_parse_export.py::test_pipeline_parse_failure_still_exports_paper_page`

**Symptom:** The test asserts that `("parse", "failed")` should appear in `pipeline_runs`, but the DB only contains `("parse", "success")`.

**Root cause:** `backend/results_parser.py::parse_and_store_with_summary` returns early when `result_entries` is empty (line 652-654):

```python
if not result_entries:
    logger.warning("No result entries in LLM output for arXiv:%s", arxiv_id)
    return summary
```

Because it returns before the caller (`pipeline.py::stage_parse`) reaches the `except Exception` block, `record_run(p.id, "parse", "success")` is executed even though no actual results were stored. The test expects the **semantic** failure (no results == parse failure), but the code treats it as success.

**Impact:** Operational dashboards and downstream consumers (e.g. the Hugo export logic that gates on `has_results: false`) receive an inconsistent signal. This makes it impossible to distinguish “genuinely parsed but no results” from “parse logic failed”.

---

### 1.2 `_extract_proposed_model_hint` prefers long model name over short abbreviation

**Test:** `tests/unit/test_llm_extractor.py::test_extract_proposed_model_hint_prefers_short_abbreviation_from_intro`

**Symptom:** Given title `Curve Your Attention: Mixed-Curvature Transformers ...` and abstract `... Fully Product-Stereographic Transformer (FPS-T) ...`, the function returns `"Mixed-Curvature Transformers"` instead of the expected `"FPS-T"`.

**Root cause:** The heuristic in `backend/llm_extractor.py` (~line 660+) extracts the title prefix before the colon and does not give priority to short capitalised abbreviations found inside parentheses in the abstract/intro text.

**Impact:** The "proposed model" hint stored in the DB is wrong, which propagates to the results parser (proposed rows not matched, missing model identity) and to the exported Hugo pages.

---

## 2. Latent Runtime Bugs

### 2.1 SQL Injection in schema migration helpers

**File:** `backend/db.py`

```python
def _add_column_if_missing(engine, table, column, col_type):
    ...
    conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} {col_type}"))
```

All three arguments are concatenated directly into an SQL string. While the callers today use hard-coded values, this is a **privilege-escalation vector** if any future code path accepts user input (e.g. from a config file or CLI argument).

**Severity:** Medium (currently latent, but violates defence-in-depth).  
**Fix:** Use SQLAlchemy text parameters or the DDL layer (`sa.Column`, `op.add_column` via Alembic).

---

### 2.2 `subprocess.run` without `check=True` ignores pipeline failures

**File:** `backend/todo_queue.py:221`

```python
subprocess.run([sys.executable, "scripts/process_todo_list.py", "--paper", arxiv_id])
```

No `check=True`, no `capture_output`, and no return-code inspection. If the subprocess crashes, the parent script silently continues and later marks the paper as `failed` or `done` based on stale state.

**Impact:** Silent data loss / false-positive queue completions.

---

### 2.3 `ET.fromstring` on untrusted XML (XXE / billion-laughs)

**File:** `backend/llm_extractor.py:343`

```python
root = ET.fromstring(xml_bytes)
```

`xml.etree.ElementTree` is vulnerable to XML entity expansion attacks unless `defusedxml` is used.

**Impact:** A malicious arXiv metadata response (or a compromised mirror) could trigger a denial-of-service via billion-laughs.

---

### 2.4 `urllib.request.urlopen` without SSL context validation hardening

**Files:** `backend/latex_source.py:235`, `backend/llm_extractor.py:341`

Bandit flags both uses because `urllib.request.urlopen` on Python ≤3.11 does not verify TLS hostnames as strictly as `requests`. The project already depends on `requests`, which should be used instead for consistent certificate validation.

---

### 2.5 Overly broad exception swallowing across the codebase

There are **98 occurrences** of `except Exception` (and blanket `except:`) in the repo. Key danger zones:

| File | Lines | Risk |
|------|-------|------|
| `backend/llm_extractor.py` | 16 catches | Silent extraction failures; missing data not retried |
| `backend/results_parser.py` | 4 catches | Metadata enrichment, HTML fallback, and YAML parse errors silently ignored |
| `backend/extraction_runner.py` | 8 catches | Paper download / parsing / figure extraction failures masked |
| `backend/pipeline.py` | 3 catches | Whole pipeline stages may fail without halting execution |
| `scripts/run_manual.py` | 7 catches | Manual-run script may report "success" when nothing happened |
| `scripts/compare_models.py` | 5 catches | Model comparison silently drops broken model entries |
| `scripts/todo_queue_dashboard.py` | 3 catches | Dashboard UI crashes suppressed; user sees stale data |

**Impact:** Operational issues are extremely hard to debug. CI may pass while production silently drops papers.

---

## 3. Code-Quality & Type-Safety Debt

### 3.1 SQLAlchemy ORM type confusion (800+ typing errors)

Both mypy and pyright report hundreds of errors of the form:

```
Cannot assign to attribute "title" for class "Paper"
  Expression of type "str" cannot be assigned to attribute "title" of class "Paper"
  "str" is not assignable to "Column[str]"
```

**Root cause:** The project uses the classic SQLAlchemy 1.x ORM pattern (`Column(String)`) without `Mapped[str]` type annotations. SQLAlchemy 2.0 strict typing requires `Mapped[...]` wrappers.

**Impact:** IDE autocomplete is unreliable, refactoring is error-prone, and many real type mismatches (e.g. assigning `None` to non-nullable columns) are hidden in the noise.

---

### 3.2 Dead / unused code

| File | Item | Risk |
|------|------|------|
| `backend/export_to_hugo.py` | `get_baseline_summary`, `build_dataset_variant_lookup`, `resolve_dataset_variant_quiet`, `_truncate_words`, `PendingDataset`, `TodoPaper`, `PaperCandidate`, `PipelineRun`, `sqlalchemy.func` | Import bloat, slower start-up, false cycles in import graph |
| `backend/alternative_downloader.py` | `Path` (unused import) | Minor |
| `backend/arxiv_downloader.py` | `Path` (unused import) | Minor |
| `backend/baseline_aggregator.py` | `DatasetVariant`, `ModelAlias` | Minor |
| `backend/llm_extractor.py` | `init_db`, `PipelineRun`, `parse_method`, `use_two_step`, `matched_family`, `unique_proposed_keys` | Reduces readability, hides logic that may have been intended to run |
| `scripts/compare_models.py` | `Panel`, `Rule` (unused rich imports) | Minor |
| `scripts/run_manual.py` | `fetch_arxiv_metadata` (unused import) | Minor |
| `scripts/find_todo_semanticscholar.py` | `sys` (unused import) | Minor |
| `scripts/test_model_ping.py` | `test_model` treated as a pytest fixture (parameter name collision) | **Runtime error in test collection** |

---

### 3.3 `f-string without placeholders`

Multiple locations use `f"..."` when no interpolation occurs. While harmless, it is a minor performance regression and lint noise.

---

## 4. Test-Suite Health

| Metric | Value |
|--------|-------|
| Total tests collected | 93 |
| Passed | 90 |
| Failed | 2 (see §1) |
| Error | 1 (`scripts/test_model_ping.py::test_model` – fixture collision) |

The single **ERROR** is caused by `test_model` being interpreted as a pytest fixture because of its signature `def test_model(model_name: str) -> bool:`. Pytest tries to inject a `model_name` fixture which does not exist. This file is obviously meant to be a CLI script, but because it contains a top-level function named `test_model`, pytest collects it as a test module.

**Impact:** CI noise; the script cannot be safely imported by pytest without renaming the function or adding `pytest.skip` guards.

---

## 5. Recommended Fixes (Prioritised)

| Priority | Fix | Effort | File(s) |
|----------|-----|--------|---------|
| **P0** | Record pipeline run status when `parse_and_store_with_summary` returns an empty-results summary | Small | `backend/pipeline.py` or `backend/results_parser.py` |
| **P0** | Correct `_extract_proposed_model_hint` to prefer short abbreviations in parentheses | Small | `backend/llm_extractor.py` |
| **P0** | Prevent `scripts/test_model_ping.py` from being collected by pytest | Tiny | Rename `test_model` → `check_model` or add `__test__ = False` |
| **P1** | Harden `_add_column_if_missing` against SQL injection | Small | `backend/db.py` |
| **P1** | Add `check=True` (or inspect `returncode`) to `subprocess.run` in todo queue | Small | `backend/todo_queue.py`, `backend/pipeline.py` |
| **P1** | Replace `ET.fromstring` with `defusedxml.ElementTree.fromstring` | Small | `backend/llm_extractor.py` |
| **P1** | Replace `urllib.request` calls with `requests` for consistent TLS validation | Small | `backend/latex_source.py`, `backend/llm_extractor.py` |
| **P1** | Add `ruff`, `mypy`, `bandit` to the `dev` dependency group | Tiny | `pyproject.toml` |
| **P2** | Migrate SQLAlchemy model declarations to `Mapped[...]` annotations | Medium | `backend/models.py` and all assign sites |
| **P2** | Audit and narrow the 98 broad `except Exception` blocks | Medium | Repository-wide |
| **P3** | Remove dead imports / unused variables identified by ruff | Tiny | Repository-wide |

---

## 6. Missing Tooling Summary

| Tool | Present? | Suggested Action |
|------|----------|------------------|
| ruff | No | Add to `dev` dependencies |
| mypy | No | Add to `dev` dependencies |
| pyright | No | Optional (can be run via `basedpyright` or Pylance) |
| bandit | No | Add to `dev` dependencies |
| pylint | No | Optional (ruff covers most rules now) |
| flake8 | No | Optional (ruff is a drop-in replacement) |
| semgrep | No | Consider for security-focused CI gates |
| safety / pip-audit | No | Consider for dependency vulnerability scanning |
| pre-commit hooks for any of the above | No | Configure `.pre-commit-config.yaml` with the new tools |

The existing `.pre-commit-config.yaml` was not reviewed in depth, but the repository currently has **no automated lint or security checks** configured in `pyproject.toml` or CI.

---

*End of report*
