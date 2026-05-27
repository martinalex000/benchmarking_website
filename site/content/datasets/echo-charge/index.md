---
title: ECHO-Charge
slug: echo-charge
benchmark: ECHO Benchmark
task_type: graph_regression
description: ECHO charge propagation task — predicting charge distribution on physical
  graphs.
primary_metric: MAE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 170000
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 11
best_model:
  model: SWAN
  value: 6.109
  metric: MAE
  arxiv_id: '2512.17762'
  paper_title: ECHO Benchmark
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
  - model: SWAN
    model_plain: SWAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 6.109
    metric_stds:
    - 0.103
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 6.182
    metric_stds:
    - 0.219
  - model: A-DGN
    model_plain: A-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 6.543
    metric_stds:
    - 0.146
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 7.134
    metric_stds:
    - 6.09
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 7.176
    metric_stds:
    - 0.371
  - model: PH-DGN
    model_plain: PH-DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 7.915
    metric_stds:
    - 0.269
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 8.421
    metric_stds:
    - 0.512
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 8.829
    metric_stds:
    - 0.021
  - model: DRew
    model_plain: DRew
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 9.086
    metric_stds:
    - 0.473
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 10.784
    metric_stds:
    - 0.059
  - model: GraphCON
    model_plain: GraphCON
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 19.629
    metric_stds:
    - 0.195
  milestones:
  - value: 6.109
    std: 0.103
    model: SWAN
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: 2025-12
---

