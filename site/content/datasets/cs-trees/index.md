---
title: CS-Trees
slug: cs-trees
benchmark: CosmoBench
task_type: graph_regression
description: Cosmic structure tree regression task from CosmoBench (R² metric).
primary_metric: R2
higher_is_better: true
pyg_url: ''
stats: null
result_count: 14
best_model:
  model: GNN (M,c,v_max,a)
  value: 0.996
  metric: R2
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: R2
  higher_is_better: true
  metrics:
  - R2
  - MAE
  rows:
  - model: GNN (M,c,v_max,a)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.996
    - null
    metric_stds:
    - 0.001
    - null
  - model: DeepSet (M,c,v_max,a)
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
    - 0.993
    - null
    metric_stds:
    - 0.001
    - null
  - model: CO-GNN
    is_baseline: false
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
    - 0.84
    - null
    metric_stds:
    - 0.004
    - null
  - model: GNN (v_max)
    is_baseline: false
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
    - 0.69
    - null
    metric_stds:
    - 0.008
    - null
  - model: 1NN
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
    - 0.64
    - null
    metric_stds:
    - 0.063
    - null
  - model: DeepSet (v_max)
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
    - 0.57
    - null
    metric_stds:
    - 0.01
    - null
  - model: EPS
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
    - 0.53
    - null
    metric_stds:
    - 0.073
    - null
  - model: GNN (a)
    is_baseline: false
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
    - 0.33
    - null
    metric_stds:
    - 0.011
    - null
  - model: DeepSet (c)
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
    - 0.23
    - null
    metric_stds:
    - 0.012
    - null
  - model: GNN (M)
    is_baseline: false
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
    - 0.16
    - null
    metric_stds:
    - 0.01
    - null
  - model: DeepSet (M)
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
    - 0.12
    - null
    metric_stds:
    - 0.009
    - null
  - model: DirGCN (Trees, undir, no PE, no Spec)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 1.2887
    metric_stds:
    - null
    - 0.1195
  - model: DirGCN (Trees, direc, no PE, no Spec)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.8166
    metric_stds:
    - null
    - 0.5012
  - model: S²GNN s (Trees, direc, PE, Spec)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.7767
    metric_stds:
    - null
    - 0.3306
  milestones:
  - value: 0.996
    std: 0.001
    model: GNN (M,c,v_max,a)
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: 2025-07
---

