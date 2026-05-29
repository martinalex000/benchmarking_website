---
title: Bridges
slug: bridges
benchmark: GraphBench
task_type: graph_classification
description: Bridge edge detection (GraphBench / CLRS-style algorithmic reasoning).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats:
  num_graphs: 21000000
  avg_nodes: 264.0
  avg_edges: 3667.0
  num_classes: null
result_count: 5
best_model:
  model: RRWP
  value: 0.9921
  metric: F1
  arxiv_id: '2511.08028'
  paper_title: Generalizable Insights for Graph Transformers in Theory and Practice
variants:
- slug: hard
  name: Hard
  notes: Large graph instances.
  is_standard: false
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  rows:
  - model: RRWP
    model_plain: RRWP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9921
    metric_stds:
    - 0.0009
  - model: LPE
    model_plain: LPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9176
    metric_stds:
    - 0.0766
  - model: RWSE
    model_plain: RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8734
    metric_stds:
    - 0.0397
  - model: NoPE
    model_plain: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5536
    metric_stds:
    - 0.2494
  - model: SPE
    model_plain: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    date_display: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5481
    metric_stds:
    - 0.212
  milestones:
  - value: 0.9921
    std: 0.0009
    model: RRWP
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: 2025-11
---

