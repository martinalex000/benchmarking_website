# One-Shot vs RAG Extraction Report

Date: 2026-05-22
Branch: `experiment/one-shot-vs-rag`

## Goal

Compare whole-paper one-shot extraction on expanded LaTeX (`paper.tex` / `main_tex`) against the current multi-shot RAG pipeline, and test whether YAML is a better structured output format than JSON for long result extraction runs.

## Pipeline Changes Made

1. Added explicit extraction strategy controls: `auto`, `two-step`, `full`.
2. Added labeled experiment artifact directories under `papers/<id>/extracted/experiments/<label>/`.
3. Added YAML result output mode plus structured parsing fallback.
4. Hardened result parsing so incomplete rows do not fail an entire dataset extraction.
5. Allowed labeled experiment runs even when the default paper output was produced by the fallback model.
6. Normalized model names (`$^*$` -> `*`, basic LaTeX cleanup) and stabilized `proposed_model.name` from extracted proposed rows.
7. Fixed `full` mode so it actually uses the full expanded LaTeX source instead of the intro slice.
8. Added dedicated compact full-paper prompts plus payload expansion rescue for `full` extraction.
9. Tightened dataset discovery, table selection, and result extraction prompts to exclude ablations and diagnostic tables.
10. Added post-processing heuristics so benchmarking/reassessment papers do not keep an invented single proposed model.

## Papers Tested

- `2210.07606` — Revisiting Heterophily For Graph Neural Networks
- `2406.08993` — Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification

## Experiment Matrix

### 2210.07606

Valid post-fix runs:

| Run | Model | Strategy | Format | Outcome |
|---|---|---|---|---|
| `qwen-two-step-json` | `qwen3.6-35b-a3b` | two-step RAG | JSON | Success |
| `smoke-2210-two-step-yaml` | `qwen3.6-35b-a3b` | two-step RAG | YAML | Success |
| `qwen-full-json` | `qwen3.6-35b-a3b` | full whole-paper | JSON | Failed after full-mode fix |
| `qwen-full-yaml` | `qwen3.6-35b-a3b` | full whole-paper | YAML | Failed after full-mode fix |

Key observations:

- Two-step RAG with qwen produced `296` results over `9` datasets in both JSON and YAML.
- Overlap against the existing default qwen extraction was `261 / 264` result keys.
- YAML brought no measurable gain on this paper.
- Whole-paper one-shot was not usable after the `main_tex` fix:
  - JSON failed with a top-level list response instead of the required object.
  - YAML failed to parse at all.
- The incomplete-row sanitizer mattered here: before it, a single `value: null` row caused the Wisconsin dataset call to fail entirely.

Conclusion for this paper:

- RAG is clearly better than one-shot.
- JSON is fine when the paper is relatively small and the RAG calls are bounded per dataset.

### 2406.08993

Valid post-fix runs:

| Run | Model | Strategy | Format | Results | Datasets | Parse Failures | Overlap vs GLM baseline |
|---|---|---|---|---:|---:|---:|---:|
| `qwen-two-step-json` | `qwen3.6-35b-a3b` | two-step RAG | JSON | 296 | 15 | 3 | 215 / 327 |
| `qwen-two-step-yaml` | `qwen3.6-35b-a3b` | two-step RAG | YAML | 363 | 18 | 0 | 254 / 327 |
| `fast-two-step-json` | `openai-gpt-oss-120b` | two-step RAG | JSON | 374 | 18 | 0 | 243 / 327 |
| `fast-two-step-yaml` | `openai-gpt-oss-120b` | two-step RAG | YAML | 374 | 17 | 1 | 303 / 327 |
| `qwen-full-json` | `qwen3.6-35b-a3b` | full whole-paper | JSON | failed | failed | n/a | n/a |
| `qwen-full-yaml` | `qwen3.6-35b-a3b` | full whole-paper | YAML | failed | failed | n/a | n/a |
| `fast-full-json` | `openai-gpt-oss-120b` | full whole-paper | JSON | failed | failed | n/a | n/a |

Reference baseline already in the repo:

- Default extraction: `glm-4.7`
- Result keys: `327`

Key observations:

- Whole-paper one-shot remained unstable even after fixing it to read the full `main_tex`.
- qwen + RAG + JSON lost three entire dataset calls due to JSON escaping failures:
  - `Minesweeper`
  - `ogbn-proteins`
  - `pokec`
- Switching only the output format from JSON to YAML fixed those qwen parse failures completely and improved dataset coverage from `15` to `18`.
- The fast model benefited strongly from RAG. Whole-paper full mode failed, but two-step RAG succeeded.
- For the fast model, YAML was materially better than JSON on this paper:
  - same total result count (`374`)
  - one parse failure (`Physics`)
  - much better overlap against the GLM baseline (`303` vs `243`)
  - fewer extra keys (`69` vs `131`)

Conclusion for this paper:

- RAG is necessary.
- YAML is better than JSON for long, high-cardinality per-dataset extraction, especially when the model emits long tables or source references that trigger JSON escape issues.

## Model Name Findings

What worked after the name cleanup pass:

- `GNN*` was corrected to `GCN*` in the qwen YAML RAG output for `2406.08993`.
- LaTeX star markup such as `GraphGPS$^*$` was normalized to `GraphGPS*`.
- `ACMII-GCN++` was preserved correctly for `2210.07606` in the two-step runs.
- After the benchmarking-title heuristic fix, `2406.08993` no longer persists a fake single proposed model in the final qwen two-step YAML artifact.

What still needs work:

- The fast model's dataset discovery sometimes prefers shorter aliases (`Computer`, `Photo`, `CS`) instead of the longer paper-local forms (`Amazon-Computers`, `Amazon-Photo`, `Coauthor-CS`). This did not block extraction, but it is less faithful.

## Follow-Up Update (2026-05-22)

The second pass focused on the two biggest weaknesses from the initial experiment: making whole-paper one-shot extraction at least testable, and preventing benchmarking papers from inventing a proposed model.

Validated updates on `2406.08993`:

- `qwen-two-step-yaml` now keeps only main benchmark-table results, excludes ablation-style rows, and finishes with `334` results across `17` datasets.
- The final saved `qwen-two-step-yaml` artifact now has `proposed_model: null` and no `is_proposed` rows, which matches the paper's benchmarking/reassessment framing.
- `qwen-full-json` no longer fails schema validation on the full-paper path. With the compact full prompt plus payload-expansion rescue, it saves a valid artifact with `16` results across `4` datasets from the main benchmark table and no proposed model.

What this changes in the original conclusion:

- Whole-paper one-shot is still much weaker than two-step RAG, but it is no longer completely unusable for qwen on this paper.
- Ablation exclusion has to happen twice: once in table selection and again in result post-processing.
- Proposed-model stabilization cannot rely only on the model output; benchmarking-title-aware cleanup is necessary.

## What Worked Well

- Explicit experiment labels made it practical to run repeated comparisons without overwriting the default artifacts.
- The incomplete-row sanitizer prevented single bad rows from invalidating a whole dataset call.
- YAML was a real improvement for long RAG calls, not just a parser convenience.
- Model-name normalization improved the saved artifacts enough that the proposed model is now readable and usable in the report.

## What Did Not Work Well

- Whole-paper one-shot extraction on full expanded LaTeX is not robust enough yet.
- The current full-mode prompt/schema adherence collapses on large smart-excerpt calls, in both JSON and YAML.
- RAG still produces some extra keys versus the strongest baseline, especially for the fast model.

## Recommendation

1. Keep the default extraction path as multi-shot RAG.
2. Prefer YAML over JSON for long papers with many datasets or long source references.
3. Use `openai-gpt-oss-120b` only with two-step RAG; do not use it for whole-paper one-shot extraction.
4. Treat whole-paper one-shot as an experimental path that now has a workable rescue layer, but is still materially less complete than two-step RAG.

## Relevant Artifacts

Representative successful outputs:

- `papers/2210.07606/extracted/experiments/qwen-two-step-json/`
- `papers/2210.07606/extracted/experiments/smoke-2210-two-step-yaml/`
- `papers/2406.08993/extracted/experiments/qwen-two-step-yaml/`
- `papers/2406.08993/extracted/experiments/fast-two-step-yaml/`

Representative failure logs for valid whole-paper post-fix runs:

- `papers/2210.07606/extracted/extraction_error_20260521_153825.md`
- `papers/2210.07606/extracted/extraction_error_20260521_154333.md`
- `papers/2406.08993/extracted/extraction_error_20260521_153935.md`
- `papers/2406.08993/extracted/extraction_error_20260521_154152.md`