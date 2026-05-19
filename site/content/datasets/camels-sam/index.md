---
title: CAMELS-SAM
slug: camels-sam
benchmark: CosmoBench
task_type: graph_regression
description: Galaxy property regression on CAMELS Semi-Analytic Model simulation (R²
  metric).
primary_metric: R^2
higher_is_better: true
pyg_url: ''
stats: null
result_count: 7
best_model:
  model: 2PCF
  value: 0.84
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
    - 0.84
    metric_stds:
    - 0.02
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
    is_best: true
    metric_values:
    - 0.8
    metric_stds:
    - 0.02
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
    - 0.78
    metric_stds:
    - 0.03
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
    - 0.78
    metric_stds:
    - 0.03
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
    - 0.297
    metric_stds:
    - null
  - model: LLS w/ modification
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
    - 0.2185
    metric_stds:
    - null
  - model: Linear theory oracle w/ modification
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.0732
    metric_stds:
    - null
  milestones:
  - value: 0.84
    std: 0.02
    model: 2PCF
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: 2025-07
---

