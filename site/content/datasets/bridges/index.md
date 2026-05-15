---
title: Bridges
slug: bridges
benchmark: GraphBench
task_type: graph_classification
description: Bridge edge detection (GraphBench / CLRS-style algorithmic reasoning).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 5
best_model:
  model: GDT (RRWP)
  value: 0.9921
  metric: F1
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
  - model: GDT (RRWP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9921
    metric_stds:
    - 0.0009
  - model: GDT (LPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9176000000000001
    metric_stds:
    - 0.0766
  - model: GDT (RWSE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8734000000000001
    metric_stds:
    - 0.0397
  - model: GT (no PE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5536
    metric_stds:
    - 0.2494
  - model: GDT (SPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
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
    model: GDT (RRWP)
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: 2025-11
- slug: easy
  name: Easy
  notes: Small graph instances.
  is_standard: false
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
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
    - 0.9831
    metric_stds:
    - 0.0184
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
    is_best: false
    metric_values:
    - 0.9269
    metric_stds:
    - 0.0103
  milestones:
  - value: 0.9831
    std: 0.0184
    model: GIN
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
  - model: GDT (RRWP)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9921
    metric_stds:
    - 0.0009
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
    - 0.968
    metric_stds:
    - 0.0178
  - model: GDT (LPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9176000000000001
    metric_stds:
    - 0.0766
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
    is_best: false
    metric_values:
    - 0.8897
    metric_stds:
    - 0.0304
  - model: GDT (RWSE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8734000000000001
    metric_stds:
    - 0.0397
  - model: GT (no PE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5536
    metric_stds:
    - 0.2494
  - model: GDT (SPE)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_iso: 2025-11
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
    model: GDT (RRWP)
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: 2025-11
- slug: medium
  name: Medium
  notes: Medium-scale graph instances.
  is_standard: false
  primary_metric: F1
  higher_is_better: true
  metrics:
  - F1
  rows:
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
    - 0.9622
    metric_stds:
    - 0.0077
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
    is_best: false
    metric_values:
    - 0.8762
    metric_stds:
    - 0.0258
  milestones:
  - value: 0.9622
    std: 0.0077
    model: GIN
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

