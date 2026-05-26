---
title: Case 1
slug: case-1
benchmark: Power Flow Benchmarks
task_type: graph_regression
description: Power flow analysis on IEEE test case 1 (small power grid, node-level
  regression).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1000000
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 4
best_model:
  model: RMGL
  value: 0.9987
  metric: Accuracy
  arxiv_id: '2601.01387'
  paper_title: Power Flow Benchmarks
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: RMGL
    model_plain: RMGL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.9987
    metric_stds:
    - null
  - model: MGL
    model_plain: MGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9964
    metric_stds:
    - null
  - model: GLR
    model_plain: GLR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9963
    metric_stds:
    - null
  - model: GLP
    model_plain: GLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.9954000000000001
    metric_stds:
    - null
  milestones:
  - value: 0.9987
    std: null
    model: RMGL
    arxiv_id: '2601.01387'
    title: Power Flow Benchmarks
    date: 2026-01
---

