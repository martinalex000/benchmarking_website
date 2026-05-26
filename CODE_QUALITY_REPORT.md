# Code Quality Report

## Scope

This report covers the code-quality work completed in the recent cleanup sequence, including the earlier extractor/export splits and the follow-up implementation slices completed in this pass.

Relevant recent commits:

- `c807a83` Split extraction runner orchestration
- `c61390a` Split Hugo development exports
- `4330fb1` Add repopulate_db API regression test
- `f57ed66` Add export helper regression tests
- `2a4f614` Unify todo queue status handling
- `e42b45c` Add pipeline integration coverage
- `8c264dd` Add todo queue DB indexes
- `8cb0ff5` Document extractor heuristic thresholds

## What Changed

### 1. Extraction and export boundaries were made more explicit

- `backend/extraction_runner.py` now holds the orchestration layer that had previously been mixed into `backend/llm_extractor.py`.
- `backend/hugo_dev_exports.py` now holds the development/admin Hugo export logic that had previously lived inside `backend/export_to_hugo.py`.
- `backend/export_to_hugo.py` still acts as the compatibility surface, but the development-page responsibilities are no longer embedded directly in the main export flow.

### 2. Critical helper behavior is now regression-tested

- Added `tests/unit/test_export_to_hugo.py`.
- Added focused coverage for title sanitization, model sanitization, value-gap logic, and ranking behavior.
- While adding those tests, two real bugs in `backend/export_to_hugo.py` were fixed:
  - title sanitization now strips LaTeX commands before collapsing backslashes
  - model subscript/superscript rendering now substitutes the captured text correctly instead of emitting literal `\1`

### 3. Todo queue status handling is now internally consistent

- Added shared status definitions and exit-code mapping in `backend/models.py`.
- Updated `scripts/process_todo_list.py` and `scripts/find_todo_papers.py` to use the same queue-status vocabulary.
- Added `tests/unit/test_todo_queue_statuses.py` to pin down the `rejected` path and parser acceptance of that status.

### 4. The main processing path now has a real integration-style guardrail

- Added `tests/integration/test_pipeline_extract_parse_export.py`.
- This test uses a real temp database, real parser, and real export code, while faking extraction output at the pipeline boundary.
- The test covers the `extract -> parse -> export` path and verifies both DB state and generated site output.

### 5. The parser now has an explicit summary contract behind the legacy API

- `backend/results_parser.py` now exposes `ParseStoreSummary` and `parse_and_store_with_summary()`.
- Existing callers continue to use `parse_and_store()` and still receive the original integer return value.
- The new summary reports side effects that were previously hidden, including:
  - created stub paper
  - created models
  - metadata changes
  - updated results
  - skipped unknown datasets
  - skipped invalid values
  - overrides applied
- Added `tests/unit/test_results_parser_summary.py` for this behavior.

### 6. DB bootstrap hygiene improved for the todo queue

- `backend/db.py` now uses explicit `sqlalchemy.text` imports rather than the previous `__import__("sqlalchemy")` pattern.
- Added explicit runtime index creation for `todo_papers.created_at` and `todo_papers.seen_count`.
- Added matching ORM indexes in `backend/models.py`.
- Updated `config/schema.sql` so the canonical schema matches the runtime behavior.
- Added `tests/unit/test_db_indexes.py` to check index creation and idempotent bootstrap.

### 7. Extraction heuristics are less magical locally

- `backend/llm_extractor.py` now names and centralizes several heuristic constants:
  - top dataset hint limit
  - ripgrep dataset match limit
  - dataset context window
  - benchmark-context markers
- Added local rationale to `_title_looks_corrupted()` and replaced in-function literals with named constants.
- Extended `tests/unit/test_llm_extractor.py` with title-corruption coverage.

## Where the Major Problems Were

### 1. Hidden behavior in large helper modules

The worst concentration of maintainability risk was in `backend/export_to_hugo.py` and `backend/results_parser.py`.

- `backend/export_to_hugo.py` mixed formatting, ranking, export orchestration, and diagnostics logic.
- `backend/results_parser.py` hid multiple meaningful side effects behind a single integer return value.
- In both modules, small helper bugs could survive for a long time because the behavior had little or no direct test coverage.

### 2. Semantic drift between scripts that should agree

The todo-queue scripts were not just duplicated. They disagreed on what statuses existed and what certain command outcomes meant.

- `scripts/process_todo_list.py` treated exit code `2` as `rejected`
- `scripts/find_todo_papers.py` did not expose that same status cleanly

That kind of drift is especially dangerous because it creates user-visible inconsistency without necessarily causing a crash.

### 3. Missing integration coverage on the operational pipeline

Before this pass, `tests/integration/` was effectively empty. That left the highest-value path in the repo under-protected:

- stage orchestration
- artifact persistence
- DB storage
- export generation

The new integration test does not solve all coverage gaps, but it establishes the missing seam.

### 4. Local heuristics were hard to reason about

Several extraction and parsing decisions relied on undocumented thresholds or in-function constants.

- fuzzy model matching threshold
- ZINC MAE threshold behavior
- dataset precheck limits and context windows
- title corruption checks

The code mostly worked, but it was carrying local knowledge that was not visible enough to maintain confidently.

### 5. DB bootstrap was more ad hoc than it should be

`backend/db.py` still uses a lightweight runtime migration style rather than a versioned migration framework. The cleanup here improved the surface, but the deeper problem remains: schema evolution is still only partially formalized.

## What Is Still Open

### High priority

1. Finish decomposing `backend/export_to_hugo.py`.
   The development export split helped, but the main export module is still the largest mixed-responsibility file in the repo.

2. Consolidate todo queue ownership into one supported operational surface.
   Statuses are now aligned, but the repo still has overlapping queue-management scripts with partially duplicated behavior.

3. Expand integration coverage beyond the current happy-path test.
   Missing cases still include malformed extraction output, fallback/extraction failure behavior, and export behavior under partial data.

4. Replace the ad hoc runtime migration model in `backend/db.py` with a tracked versioned migration system.
   The repo is in better shape now, but this is still the biggest infrastructure-quality item left open.

### Medium priority

1. Continue parser boundary cleanup.
   `parse_and_store_with_summary()` is a step forward, but the parser module still owns too many responsibilities.

2. Centralize shared sanitization logic across parser and export.
   Some of the normalization behavior is still duplicated or parallel rather than fully shared.

3. Introduce more explicit status typing across other state-heavy tables.
   Todo queue status handling improved, but other status columns still rely on free-form strings.

4. Audit and narrow broad `except Exception` blocks in extraction and export paths.
   Several degraded states are still intentionally quiet, which makes debugging harder than it should be.

### Lower priority

1. Add more explicit architecture/maintainer documentation.
2. Add snapshot-style tests for generated markdown where stable enough.
3. Revisit pipeline-stage helper boundaries in `backend/pipeline.py` so more of the stage logic can be tested without `argparse.Namespace` scaffolding.

## General Comments on Conciseness and Simplicity

### What is already reasonably good

- The repo has a pragmatic shape: extraction, parsing, storage, and export are conceptually distinct, and most modules are named honestly.
- The code generally prefers straightforward control flow over abstract frameworks.
- Operational scripts are simple to run and easy to inspect.

### What still hurts simplicity

- A few core modules still carry too many responsibilities, so local simplicity is worse than the top-level architecture suggests.
- Several behaviors depend on implicit conventions rather than explicit contracts.
- The codebase is concise in many places, but not always simple. Some files are short and direct, while a few critical modules accumulate special cases, fallback logic, and formatting rules until they become difficult to reason about.

### Overall assessment

The codebase is in a better state than before this cleanup pass. The main improvements are not cosmetic: several previously unguarded or internally inconsistent behaviors are now tested and explicitly modeled. The biggest remaining quality problem is not style. It is the concentration of too much behavior in a few high-value modules, especially export and schema evolution paths.

The code is reasonably pragmatic, but not yet uniformly simple. The direction is good. The next meaningful gains will come from continuing to reduce hidden side effects, shrinking the remaining large modules, and replacing informal operational conventions with explicit contracts and versioned infrastructure.

## Validation Summary

The following broader regression suite passed after the changes in this pass:

- `pytest tests/unit/test_export_to_hugo.py`
- `pytest tests/unit/test_todo_queue_statuses.py`
- `pytest tests/unit/test_results_parser.py`
- `pytest tests/unit/test_results_parser_summary.py`
- `pytest tests/unit/test_db_indexes.py`
- `pytest tests/unit/test_llm_extractor.py`
- `pytest tests/integration/test_pipeline_extract_parse_export.py`

Combined run result: `37 passed`.