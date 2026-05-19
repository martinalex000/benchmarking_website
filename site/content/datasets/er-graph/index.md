---
title: ER graph
slug: er-graph
benchmark: GraphBench
task_type: graph_classification
description: Node classification on Erdős–Rényi random graphs (GraphBench algorithmic
  reasoning).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 4
best_model:
  model: DeepSets
  value: 0.756
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
  rows:
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
    is_best: true
    metric_values:
    - 0.756
    metric_stds:
    - 0.711
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
    is_best: true
    metric_values:
    - 0.751
    metric_stds:
    - 0.767
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
    - 0.234
    metric_stds:
    - 0.191
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
    - 0.06486
    metric_stds:
    - 0.08101000000000001
  milestones:
  - value: 0.756
    std: 0.711
    model: DeepSets
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

