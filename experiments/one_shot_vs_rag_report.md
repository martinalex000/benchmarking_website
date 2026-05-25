# Extraction Quality Report

Date: 2026-05-25
State: merged to `main`, then extended with a larger validation sweep

## TL;DR

- Keep `two-step` RAG as the default extraction path.
- Make YAML the default structured format. It is materially more robust than JSON on long, high-cardinality benchmark papers.
- qwen is now the safest default for hard benchmark papers. The fast OpenAI model is competitive on some papers, but it is much less consistent on the hardest ones.
- GLM is still useful as a comparison point, but it is not reliable enough to be treated as ground truth by itself.
- Whole-paper one-shot remains experimental. The compact full-mode rescue helps, but it is still far less complete than two-step RAG.

## Pipeline State After This Pass

The extraction pipeline now includes:

1. YAML as the default `result_output_format`.
2. A ripgrep-based dataset-name precheck before dataset discovery, using canonical names from `config/seed_data.yaml` and feeding those candidates into the discovery prompt.
3. Compact full-paper prompts plus payload-expansion rescue for the `full` strategy.
4. Stronger ablation exclusion in dataset discovery, table selection, extraction prompts, and result post-processing.
5. Proposed-model stabilization that avoids inventing a single proposed model for benchmarking/reassessment papers.
6. Per-artifact usage reporting: total extraction calls, token totals, and a post-run quota snapshot.

## Final Hard-Paper Set

I screened eight new hard papers and kept the five where qwen was clearly stronger than the fast OpenAI model in two-step YAML mode.

| arXiv ID | Paper | qwen rows / datasets | fast rows / datasets | qwen parse failures | fast parse failures |
|---|---|---:|---:|---:|---:|
| `2310.05174` | GSLB: The Graph Structure Learning Benchmark | `256 / 17` | `124 / 6` | `0` | `2` |
| `2502.09263` | Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures Meet Excellence | `184 / 11` | `111 / 10` | `2` | `0` |
| `2410.05697` | Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter Tuning | `74 / 8` | `26 / 4` | `6` | `0` |
| `2407.18480` | Scalable Graph Compressed Convolutions | `219 / 15` | `114 / 10` | `1` | `0` |
| `2310.02156` | Probabilistically Rewired Message-Passing Neural Networks | `177 / 14` | `55 / 9` | `2` | `1` |

Aggregate over this final five-paper set:

- qwen: `910` extracted rows, `65` dataset appearances, `726,887` tokens, `11` parse failures.
- fast OpenAI: `430` extracted rows, `39` dataset appearances, `696,431` tokens, `3` parse failures.

Interpretation:

- On the hardest benchmark-heavy papers, qwen wins mostly by coverage.
- The fast model is not failing by arithmetic transcription alone; it often drops whole datasets or large parts of the main benchmark tables.
- Lower parse-failure counts for the fast model do not imply better extraction quality. Several fast runs were simply shorter and less complete.

## Refreshed GLM-Backed Analysis

I refreshed GLM runs on a five-paper batch and combined that with the already-valid `2406.08993` GLM-backed paper to get a six-paper comparison set:

- `2406.08993` — Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification
- `2310.05174` — GSLB: The Graph Structure Learning Benchmark
- `2506.04765` — OpenGT: A Comprehensive Benchmark For Graph Transformers
- `2502.09263` — Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures Meet Excellence
- `2406.09639` — TGB 2.0: A Benchmark for Learning on Temporal Knowledge Graphs and Heterogeneous Graphs
- `2309.00367` — Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark

Aggregate against the refreshed GLM references:

| Model | Baseline rows | Hits | Value errors | Misses | Hallucinations | Recall | Precision |
|---|---:|---:|---:|---:|---:|---:|---:|
| qwen | `963` | `764` | `0` | `199` | `209` | `0.793` | `0.785` |
| fast OpenAI | `963` | `624` | `4` | `335` | `217` | `0.648` | `0.738` |

Per-paper headline result:

- qwen clearly beats fast on `2310.05174` and `2502.09263`.
- qwen slightly beats fast on `2406.09639`.
- fast beats qwen on `2406.08993`, `2506.04765`, and `2309.00367` when scored against GLM.

Important caveat: these GLM-based scores are useful for coarse ranking, but they are not absolute truth.

## GPT-5.4 Verification

I asked a GPT-5.4 subagent to inspect the LaTeX and extracted artifacts directly for three representative papers:

### 2310.05174

- Verdict: qwen best, GLM runner-up, fast clearly weakest.
- Main issue in fast: major coverage loss across heterogeneous and graph-level benchmark tables.

### 2502.09263

- Verdict: GLM best, qwen runner-up, fast clearly weaker.
- Main issue in fast: it drops large parts of the LRGB and OGB benchmark tables.

### 2506.04765

- Verdict: qwen best, fast runner-up, GLM weakest.
- Main issue in GLM: wrong-table contamination and at least one invented numeric row from an OOM/missing entry.

What this means:

- The quantitative metrics are directionally useful.
- Coverage is the main error mode.
- GLM should not be treated as unquestionable ground truth on dense benchmark papers.
- When a paper mixes main tables with nearby positional-encoding variants, appendix tables, or OOM cells, paper-level verification is still necessary.

## Whole-Paper One-Shot

This remains a secondary path only.

What improved:

- qwen full-mode extraction no longer immediately dies on schema validation for `2406.08993`.
- The compact prompt plus payload-expansion rescue makes whole-paper full mode at least testable.

What did not change:

- Two-step RAG is still far more complete and stable.
- Full-mode one-shot still loses too much benchmark coverage to be the default.

## Usage Limits

The endpoint exposes request-limit headers. A representative live snapshot during this pass showed:

- `2` requests per second
- `10` requests per minute
- `600` requests per hour
- `1200` requests per day
- `10000` requests per month

The extractor now writes a short `Usage` section into each saved artifact with:

- extraction-call count
- prompt/completion/total token usage
- end-of-run quota snapshot

This is a request-budget snapshot, not a billing report.

## Recommendations

1. Keep `two-step` RAG as the production default.
2. Keep YAML as the default output format.
3. Use qwen as the default model for hard benchmark papers with many datasets or wide tables.
4. Keep the fast OpenAI model available as a second option, but verify it on hard papers before trusting it.
5. Treat GLM as a comparison baseline, not as definitive truth.
6. Keep whole-paper one-shot behind an experimental flag only.

## Relevant Artifacts

Direct hard-paper comparison set:

- `papers/2310.05174/extracted/experiments/qwen-two-step-yaml-expanded/`
- `papers/2502.09263/extracted/experiments/qwen-two-step-yaml-expanded/`
- `papers/2410.05697/extracted/experiments/qwen-two-step-yaml-expanded-b/`
- `papers/2407.18480/extracted/experiments/qwen-two-step-yaml-expanded-c/`
- `papers/2310.02156/extracted/experiments/qwen-two-step-yaml-expanded-c/`

Refreshed GLM-backed comparison set:

- `papers/2406.08993/extracted/`
- `papers/2310.05174/extracted/experiments/glm-two-step-yaml-expanded/`
- `papers/2506.04765/extracted/experiments/glm-two-step-yaml-expanded/`
- `papers/2502.09263/extracted/experiments/glm-two-step-yaml-expanded/`
- `papers/2406.09639/extracted/experiments/glm-two-step-yaml-expanded/`
- `papers/2309.00367/extracted/experiments/glm-two-step-yaml-expanded/`