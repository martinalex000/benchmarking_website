# AGENTS.md

## Project goal

This repository builds a self-hosted benchmarking website that helps researchers browse the
state of the art, find relevant baselines, and compare benchmarks across papers. The pipeline
discovers papers, extracts benchmark results, applies manual overrides where needed, and exports
the curated data to the site.

## How to work in this repo

- Use `uv` for package and environment management.
- Install dependencies with `uv sync --group dev`.
- Run commands with `uv run ...` instead of calling local Python tooling directly.
- In this sandbox, prefix `uv` commands with `UV_CACHE_DIR=/tmp/benchmarking-uv-cache` so uv does not try to write its cache under the read-only home directory.
- Prefer small, focused, regular git commits over large batches of unrelated work.
- Keep changes clean and reviewable; do not leave the tree in a half-finished state.

## Code quality expectations

- Write clear, legible code.
- Keep functions maintainable in size; extract helpers when a function starts doing too much.
- Comment only where there is an interesting twist, non-obvious decision, or subtle constraint.
- Follow existing patterns in the codebase before introducing new abstractions.
- Preserve or improve testability; add tests when behavior changes.

## Tooling and hooks

The repository uses these pre-commit hooks:

- `checkpoint-benchmarks-db` (merge WAL into `data/benchmarks.db`; block `-wal`/`-shm` commits)
- `isort`
- `black`
- `ruff` / `ruff-format`
- `bandit` (medium+ severity only)

Respect the configured formatting and linting rules:

- Python target: 3.12
- Line length: 100

For simply watching and summarizing terminal outputs: spin up simple models such as gpt-5.4-mini (in case you are gpt-5.4 or 5.5). 

## Repository layout

- `backend/` — core extraction, parsing, storage, and export logic
- `scripts/` — CLI entry points and maintenance utilities
- `site/` — Hugo/static site content and generated data
- `tests/` — unit and integration tests
- `papers/` — local workspace for downloads, extracted artifacts, and overrides; treat as untracked

## Practical guardrails

- Never commit secrets or `.env` values.
- Avoid committing generated artifacts unless a file is meant to be versioned.
- Prefer existing scripts and tests when validating changes.
- Keep the researcher workflow in mind: the end result should make it easier to browse SOTA and find
  strong baselines and benchmarks.
- Perform regular git commits with concise messages spanning (typically) at most two lines.
