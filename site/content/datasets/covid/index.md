---
title: COVID
slug: covid
benchmark: DualEquiNet RNA Benchmarks
task_type: graph_regression
description: RNA structure prediction on the COVID-19 dataset from the EternaFold/Kaggle
  Ribonanza challenge (RMSE metric, lower is better).
primary_metric: RMSE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 4082
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 7
best_model:
  model: DualEquiNet
  value: 0.353
  metric: RMSE
  arxiv_id: '2506.19862'
  paper_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large
    Biomolecules'
variants:
- slug: standard-split
  name: Standard split
  notes: RMSE on reactivity prediction (lower is better).
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
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.353
    metric_stds:
    - 0.006
  - model: GotenNet
    model_plain: GotenNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.475
    metric_stds:
    - 0.009
  - model: FastEGNN
    model_plain: FastEGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.478
    metric_stds:
    - 0.031
  - model: GVPGNN
    model_plain: GVPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.531
    metric_stds:
    - 0.011
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.533
    metric_stds:
    - 0.011
  - model: SchNet
    model_plain: SchNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.534
    metric_stds:
    - 0.011
  - model: TFN
    model_plain: TFN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.535
    metric_stds:
    - 0.011
  milestones:
  - value: 0.353
    std: 0.006
    model: DualEquiNet
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: 2025-06
---

