---
title: ECHO-Synth
slug: echo-synth
benchmark: ECHO Benchmark
task_type: graph_regression
description: ECHO synthetic propagation task — node-level regression on synthetic
  long-range graphs.
primary_metric: MAE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 10080
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 10
best_model:
  model: GRIT
  value: 1.014
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
  - model: GRIT
    model_plain: GRIT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: Dec 2025
    date_iso: 2025-12
    date_display: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.014
    metric_stds:
    - 0.046
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
    uses_external_data: false
    is_best: true
    metric_values:
    - 1.121
    metric_stds:
    - 0.07
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.151
    metric_stds:
    - 0.038
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.243
    metric_stds:
    - 0.047
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.627
    metric_stds:
    - 0.398
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.63
    metric_stds:
    - 0.161
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.005
    metric_stds:
    - 0.093
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.16
    metric_stds:
    - 0.098
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 2.969
    metric_stds:
    - 0.189
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 3.832
    metric_stds:
    - 0.262
  milestones:
  - value: 1.014
    std: 0.046
    model: GRIT
    arxiv_id: '2512.17762'
    title: ECHO Benchmark
    date: 2025-12
---

