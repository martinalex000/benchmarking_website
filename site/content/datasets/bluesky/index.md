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
stats:
  num_graphs: 3
  avg_nodes: 433000.0
  avg_edges: 10000000.0
  num_classes: null
result_count: 3
best_model:
  model: GNN
  value: 0.768
  metric: MAE
  arxiv_id: '2512.04475'
  paper_title: GraphBench
variants:
- slug: standard-split
  name: Standard split
  notes: 3 graphs, 286K–580K nodes, 3M–17M edges. Node-level regression.
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
  - model: GNN
    model_plain: GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.768
    metric_stds:
    - 0.002
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    metric_stds:
    - 0.001
  - model: DeepSets
    model_plain: DeepSets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: GraphBench
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
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

