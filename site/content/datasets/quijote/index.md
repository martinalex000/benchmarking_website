---
title: Quijote
slug: quijote
benchmark: CosmoBench
task_type: graph_regression
description: Cosmological parameter inference on Quijote N-body simulation data (graph
  regression, R² metric).
primary_metric: R^2
higher_is_better: true
pyg_url: ''
stats: null
result_count: 6
best_model:
  model: 2PCF
  value: 0.85
  metric: R^2
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: R^2
  higher_is_better: true
  metrics:
  - R^2
  rows:
  - model: 2PCF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.011
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.85
    metric_stds:
    - 0.004
  - model: LLS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.049
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.83
    metric_stds:
    - 0.004
  - model: GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.26
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.004
  - model: GNN (w/o edgeMP)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.128
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.004
  - model: LLS (1<=P<=4)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.435
    metric_stds:
    - null
  - model: Linear theory oracle
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.001
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.3769
    metric_stds:
    - null
  milestones:
  - value: 0.85
    std: 0.004
    model: 2PCF
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: 2025-07
---

