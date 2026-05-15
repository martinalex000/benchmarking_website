---
title: Case 2
slug: case-2
benchmark: Power Flow Benchmarks
task_type: graph_regression
description: Power flow analysis on IEEE test case 2 (medium power grid, node-level
  regression).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats: null
result_count: 6
best_model:
  model: RMGL
  value: 0.9928
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - Perplexity
  rows:
  - model: RMGL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.9928
    - null
    metric_stds:
    - null
    - null
  - model: MGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9606999999999999
    - null
    metric_stds:
    - null
    - null
  - model: GLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.5072
    - null
    metric_stds:
    - null
    - null
  - model: GLR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.47090000000000004
    - null
    metric_stds:
    - null
    - null
  - model: GPT2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 117.0
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 20.966
    metric_stds:
    - null
    - null
  - model: GPT2 + GFSA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - null
    - 20.923
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.9928
    std: null
    model: RMGL
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: 2026-01
---

