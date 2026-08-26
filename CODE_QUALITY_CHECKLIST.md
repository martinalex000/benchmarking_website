# Code Quality Checklist

This checklist preserves the actionable findings from the former
`DEEP_ANALYSIS_REPORT.md`. That report was archival; this file tracks items that
remain relevant in the current codebase.

## Open follow-ups

- [ ] **Consolidate metadata enrichment.** The extraction path has a local
  metadata cascade in `backend/extraction_runner.py:84-159`, including
  `_fetch_best_metadata()`, HTML/LaTeX fallback, and Semantic Scholar/arXiv
  lookup. The parsing path independently performs a broader cascade in
  `backend/results_parser.py:1011-1254`, inside `_enrich_paper_metadata()`;
  this also handles repository verification, author recovery, and GitHub
  heuristics. Define one shared policy/helper so the two paths cannot produce
  divergent paper metadata.
- [ ] **Replace todo-queue timestamp string comparison.**
  `backend/todo_queue.py` still relies on ISO timestamp ordering; migrate to a
  typed timestamp or an explicit parsed datetime when the schema permits.
- [ ] **Decompose high-complexity functions.** Prioritize `run_extraction()`
  in `backend/extraction_runner.py`, `parse_and_store_with_summary()` in
  `backend/results_parser.py`, `main()` in `scripts/run_manual.py`, and the
  extraction/export functions called out in the historical report.
- [ ] **Review transaction boundaries.** `run_extraction()` uses several
  independent database sessions. This is currently an intentional non-atomic
  design, but its partial-commit behavior should remain explicit in operator
  documentation and tests.
- [ ] **Narrow broad exception handlers.** Audit the remaining broad
  `except Exception` handlers in extraction, parsing, queue, and dashboard
  paths so expected failures are handled explicitly and unexpected failures
  remain visible.
- [ ] **Standardize HTTP client behavior.** Review the remaining
  `urllib.request.urlopen` calls in `backend/llm_metadata.py:404-406` and
  `backend/latex_source.py:242-244`; use the project HTTP client or an
  equivalently explicit TLS/redirect policy.
- [ ] **Make queue subprocess failures explicit.**
  `backend/todo_queue.py:431-436` captures a child process return code but does
  not use `check=True`; verify that every caller handles non-zero results
  immediately and records the failure consistently.
- [ ] **Reduce ORM typing debt.** Evaluate migrating classic SQLAlchemy
  `Column[...]` declarations to SQLAlchemy 2-style `Mapped[...]` annotations.
- [ ] **Remove confirmed dead code.** Re-run the configured lint/static
  analysis and remove unused imports, variables, and obsolete helpers rather
  than relying on the historical inventory.

## Resolved items retained for regression awareness

The previous reports recorded fixes for arXiv ID validation, path traversal and
SSRF defenses, bounded downloads, atomic file writes, extraction error
handling, stale override cleanup, scientific-notation parsing, export cleanup,
pipeline exit codes, SQL migration identifier validation, XML parser hardening,
development lint tooling, and proposed-model abbreviation extraction. Preserve
their regression tests when refactoring.

The former bug report also documented an empty-extraction parse-status issue;
the current integration test now covers the intended behavior of skipping a
paper page when no results are available. Re-check this contract if parse
status handling changes.
