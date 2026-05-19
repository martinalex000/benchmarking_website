---
title: BlueSky
slug: bluesky
benchmark: GraphBench
task_type: node_classification
description: 'Dynamic directed graphs of Bluesky social network user interactions.
  Node-level task: predict future engagement from past interactions and text embeddings.

  '
primary_metric: MAE
higher_is_better: false
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 3
best_model:
  model: GNN
  value: 0.768
  metric: MAE
variants:
- slug: standard-split
  name: Standard split
  notes: 3 graphs, 286K–580K nodes, 3M–17M edges. Node-level regression.
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  rows:
  - model: GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.768
    metric_stds:
    - 0.002
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    metric_stds:
    - 0.001
  - model: DeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    metric_stds:
    - 0.005
  milestones:
  - value: 0.768
    std: 0.002
    model: GNN
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

