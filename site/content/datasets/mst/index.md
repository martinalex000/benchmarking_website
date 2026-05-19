---
title: MST
slug: mst
benchmark: GraphBench
task_type: graph_classification
description: Minimum Spanning Tree edge prediction (GraphBench / CLRS-style algorithmic
  reasoning).
primary_metric: F1
higher_is_better: true
pyg_url: https://graphbench.github.io/website/datasets.html
stats: null
result_count: 5
best_model:
  model: GDT (RRWP)
  value: 0.9604
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
    - 0.9604
    metric_stds:
    - 0.0091
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
    - 0.9329000000000001
    metric_stds:
    - 0.0088
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
    - 0.9326000000000001
    metric_stds:
    - 0.0045000000000000005
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
    - 0.9251999999999999
    metric_stds:
    - 0.0012
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
    is_best: false
    metric_values:
    - 0.9107999999999999
    metric_stds:
    - 0.0095
  milestones:
  - value: 0.9604
    std: 0.0091
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
    - 0.8566
    metric_stds:
    - 0.0068
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
    - 0.6906
    metric_stds:
    - 0.1655
  milestones:
  - value: 0.8566
    std: 0.0068
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
    - 0.9604
    metric_stds:
    - 0.0091
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
    - 0.9329000000000001
    metric_stds:
    - 0.0088
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
    - 0.9326000000000001
    metric_stds:
    - 0.0045000000000000005
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
    - 0.9251999999999999
    metric_stds:
    - 0.0012
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
    is_best: false
    metric_values:
    - 0.9107999999999999
    metric_stds:
    - 0.0095
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
    - 0.8421
    metric_stds:
    - 0.0115
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
    - 0.6107
    metric_stds:
    - 0.2015
  milestones:
  - value: 0.9604
    std: 0.0091
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
    - 0.8504
    metric_stds:
    - 0.0148
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
    - 0.7288
    metric_stds:
    - 0.0894
  milestones:
  - value: 0.8504
    std: 0.0148
    model: GT
    arxiv_id: '2512.04475'
    title: GraphBench
    date: 2025-12
---

