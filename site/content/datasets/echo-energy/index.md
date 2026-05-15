---
title: ECHO-Energy
slug: echo-energy
benchmark: ECHO Benchmark
task_type: graph_regression
description: ECHO energy propagation task — predicting energy distribution on physical
  graphs.
primary_metric: MAE
higher_is_better: false
pyg_url: ''
stats: null
result_count: 11
best_model:
  model: GPS
  value: 5.257
  metric: MAE
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  metrics:
  - MAE
  rows:
  - model: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 5.257
    metric_stds:
    - 0.842
  - model: DRew
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 11.325
    metric_stds:
    - 2.394
  - model: A-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 12.486
    metric_stds:
    - 1.621
  - model: SWAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 12.629
    metric_stds:
    - 1.157
  - model: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 13.235
    metric_stds:
    - 2.63
  - model: GraphCON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 14.295
    metric_stds:
    - 0.807
  - model: PH-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 16.08
    metric_stds:
    - 1.123
  - model: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 23.558
    metric_stds:
    - 7.568
  - model: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 25.508
    metric_stds:
    - 2.507
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 28.112
    metric_stds:
    - 1.239
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 47.851
    metric_stds:
    - 10.154
  milestones:
  - value: 5.257
    std: 0.842
    model: GPS
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: 2025-12
---

