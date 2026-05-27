---
title: Tc-Ribo
slug: tc-ribo
benchmark: DualEquiNet RNA Benchmarks
task_type: graph_regression
description: Thermostable ribosome structure prediction (graph regression, RMSE metric).
primary_metric: RMSE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 355
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 11
best_model:
  model: DualEquiNet
  value: 0.636
  metric: RMSE
  arxiv_id: '2506.19862'
  paper_title: DualEquiNet RNA Benchmarks
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: RMSE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - RMSE
  rows:
  - model: DualEquiNet
    model_plain: DualEquiNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.636
    metric_stds:
    - 0.049
  - model: w/o CSIP
    model_plain: w/o CSIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.682
    metric_stds:
    - 0.026
  - model: TFN
    model_plain: TFN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.694
    metric_stds:
    - 0.008
  - model: w/o CSIP/Cross
    model_plain: w/o CSIP/Cross
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.698
    metric_stds:
    - 0.01
  - model: w/o CSIP/Cross/Dual
    model_plain: w/o CSIP/Cross/Dual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.699
    metric_stds:
    - 0.01
  - model: GotenNet
    model_plain: GotenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.718
    metric_stds:
    - 0.002
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.72
    metric_stds:
    - 0.022
  - model: HGNN
    model_plain: HGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.729
    metric_stds:
    - 0.007
  - model: FastEGNN
    model_plain: FastEGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.731
    metric_stds:
    - 0.006
  - model: GVPGNN
    model_plain: GVPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.736
    metric_stds:
    - 0.003
  - model: SchNet
    model_plain: SchNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.737
    metric_stds:
    - 0.002
  milestones:
  - value: 0.636
    std: 0.049
    model: DualEquiNet
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: 2025-06
---

