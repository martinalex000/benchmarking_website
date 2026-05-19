---
title: Max Clique
slug: max-clique
benchmark: GraphBench
task_type: graph_classification
description: Maximum clique node prediction (GraphBench algorithmic task).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 2
best_model:
  model: GT
  value: 0.5407
  metric: F1
variants:
- slug: easy
  name: Easy
  notes: Small graph instances.
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
  - model: GT
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
    is_best: true
    metric_values:
    - 0.5407
    metric_stds:
    - 0.0088
  - model: GIN
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
    - 0.4584
    metric_stds:
    - 0.0101
  milestones:
  - value: 0.5407
    std: 0.0088
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: hard
  name: Hard
  notes: Large graph instances.
  is_standard: false
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
  - model: GT
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
    is_best: true
    metric_values:
    - 0.4868
    metric_stds:
    - 0.0013
  - model: GIN
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
    is_best: true
    metric_values:
    - 0.4102
    metric_stds:
    - 0.082
  milestones:
  - value: 0.4868
    std: 0.0013
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
- slug: medium
  name: Medium
  notes: Medium-scale graph instances.
  is_standard: false
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
  - model: GT
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
    is_best: true
    metric_values:
    - 0.4859
    metric_stds:
    - 0.0017
  - model: GIN
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
    is_best: true
    metric_values:
    - 0.3996
    metric_stds:
    - 0.0852
  milestones:
  - value: 0.4859
    std: 0.0017
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

