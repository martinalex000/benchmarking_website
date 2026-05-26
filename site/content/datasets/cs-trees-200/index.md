---
title: CS-Trees-200
slug: cs-trees-200
benchmark: CosmoBench
task_type: graph_classification
description: CS-Trees classification variant with 200-node graphs (Accuracy metric).
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 200
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 10
best_model:
  model: GNN (a)
  value: 0.7
  metric: Accuracy
  arxiv_id: '2507.03707'
  paper_title: CosmoBench
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: GNN (a)
    model_plain: GNN (a)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7
    metric_stds:
    - 0.005
  - model: GNN (M,c,v_max,a)
    model_plain: GNN (M,c,v_max,a)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.69
    metric_stds:
    - 0.005
  - model: GNN (M)
    model_plain: GNN (M)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.63
    metric_stds:
    - 0.004
  - model: DeepSet (M,c,v_max,a)
    model_plain: DeepSet (M,c,v_max,a)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.62
    metric_stds:
    - 0.006
  - model: DeepSet (M)
    model_plain: DeepSet (M)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    metric_stds:
    - 0.005
  - model: CO-GNN
    model_plain: CO-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    metric_stds:
    - 0.005
  - model: GNN (v_max)
    model_plain: GNN (v_max)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.61
    metric_stds:
    - 0.005
  - model: DeepSet (v_max)
    model_plain: DeepSet (v_max)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.59
    metric_stds:
    - 0.005
  - model: EPS
    model_plain: EPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.53
    metric_stds:
    - 0.073
  - model: DeepSet (c)
    model_plain: DeepSet (c)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.53
    metric_stds:
    - 0.005
  milestones:
  - value: 0.7
    std: 0.005
    model: GNN (a)
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: 2025-07
---

