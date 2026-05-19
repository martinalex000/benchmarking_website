---
title: TorsionAngle
slug: torsionangle
benchmark: DualEquiNet RNA Benchmarks
task_type: graph_regression
description: RNA backbone torsion angle prediction (circular regression task, Circular
  MAE metric).
primary_metric: Circular MAE
higher_is_better: false
pyg_url: ''
stats: null
result_count: 8
best_model:
  model: DualEquiNet
  value: 15.87
  metric: Circular MAE
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Circular MAE
  higher_is_better: false
  metrics:
  - Circular MAE
  rows:
  - model: DualEquiNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 15.87
    metric_stds:
    - 2.03
  - model: GotenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 16.27
    metric_stds:
    - 1.19
  - model: GVPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 17.56
    metric_stds:
    - 0.21
  - model: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 17.79
    metric_stds:
    - 0.61
  - model: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 18.41
    metric_stds:
    - 0.22
  - model: SchNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 18.54
    metric_stds:
    - 0.86
  - model: FastEGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 18.89
    metric_stds:
    - 0.22
  - model: TFN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 21.97
    metric_stds:
    - 0.45
  milestones:
  - value: 15.87
    std: 2.03
    model: DualEquiNet
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: 2025-06
---

