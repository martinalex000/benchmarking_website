---
title: Topological Sorting
slug: topological-sorting
benchmark: GraphBench
task_type: node_classification
description: Topological ordering node rank regression on DAGs (GraphBench algorithmic
  task).
primary_metric: MAE
higher_is_better: false
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 2
best_model:
  model: GIN
  value: 0.1001
  metric: MAE
  arxiv_id: '2512.04475'
  paper_title: GraphBench
variants:
- slug: easy
  name: Easy
  notes: Small DAGs.
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
    - 0.1001
    metric_stds:
    - 0.0089
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
    is_best: false
    metric_values:
    - 0.116
    metric_stds:
    - 0.0058
  milestones:
  - value: 0.1001
    std: 0.0089
    model: GIN
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: hard
  name: Hard
  notes: Large DAGs.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
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
    - 0.1301
    metric_stds:
    - 0.0046
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
    - 0.1532
    metric_stds:
    - 0.0214
  milestones:
  - value: 0.1301
    std: 0.0046
    model: GIN
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: medium
  name: Medium
  notes: Medium-scale DAGs.
  is_standard: false
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
    - 0.1305
    metric_stds:
    - 0.0094
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
    is_best: false
    metric_values:
    - 0.1537
    metric_stds:
    - 0.0031
  milestones:
  - value: 0.1305
    std: 0.0094
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

