---
title: Electronic Circuits
slug: electronic-circuits
benchmark: GraphBench
task_type: graph_classification
description: 'Analog circuit topology design. Graph-level task: predict 2 continuous
  performance metrics from graph structure across 3 circuit-size datasets.

  '
primary_metric: MAE
higher_is_better: false
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 93000
  avg_nodes: 18.5
  avg_edges: 43.0
  num_classes: null
result_count: 4
best_model:
  model: GT
  value: 0.07
  metric: MAE
  arxiv_id: '2512.04475'
  paper_title: GraphBench
variants:
- slug: standard-split
  name: Standard split
  notes: 93,000 graphs, 13–24 nodes, 30–56 edges. Graph-level regression.
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
  - model: GT
    model_plain: GT
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
    is_best: true
    metric_values:
    - 0.07
    metric_stds:
    - 0.03
  - model: GIN
    model_plain: GIN
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
    is_best: true
    metric_values:
    - 0.09
    metric_stds:
    - 0.06
  - model: GAT
    model_plain: GAT
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
    is_best: true
    metric_values:
    - 0.11
    metric_stds:
    - 0.05
  - model: GCN
    model_plain: GCN
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
    is_best: true
    metric_values:
    - 0.13
    metric_stds:
    - 0.07
  milestones:
  - value: 0.07
    std: 0.03
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

