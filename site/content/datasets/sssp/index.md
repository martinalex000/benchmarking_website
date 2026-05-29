---
title: SSSP
slug: sssp
benchmark: Algorithmic Graph Tasks
task_type: graph_regression
description: Single Source Shortest Path prediction on synthetic graphs (node-level
  distances).
primary_metric: MSE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 7040
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 9
best_model:
  model: A-DGN
  value: 4.0e-07
  metric: MSE
  arxiv_id: '2510.08450'
  paper_title: ': Mitigating by Increasing Storage Capacity'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: MSE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MSE
  rows:
  - model: A-DGN
    model_plain: A-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: true
    metric_values:
    - 4.0e-07
    metric_stds:
    - 3.0e-07
  - model: gLSTM
    model_plain: gLSTM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.5e-06
    metric_stds:
    - 9.0e-06
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: false
    metric_values:
    - 7.4e-06
    metric_stds:
    - 1.0e-07
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.00029
    metric_stds:
    - 0.0026
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.002
    metric_stds:
    - 0.0071
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0062
    metric_stds:
    - 0.00015
  - model: DGC
    model_plain: DGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0071
    metric_stds:
    - 5.0e-05
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.008
    metric_stds:
    - 0.0046
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0089
    metric_stds:
    - 0.0
  milestones:
  - value: 4.0e-07
    std: 3.0e-07
    model: A-DGN
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: 2025-10
---

