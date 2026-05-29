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
stats:
  num_graphs: 1018
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 7
best_model:
  model: DualEquiNet
  value: 15.87
  metric: Circular MAE
  arxiv_id: '2506.19862'
  paper_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large
    Biomolecules'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Circular MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Circular MAE
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
    - 15.87
    metric_stds:
    - 2.03
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
    is_best: true
    metric_values:
    - 16.27
    metric_stds:
    - 1.19
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
    is_best: true
    metric_values:
    - 17.56
    metric_stds:
    - 0.21
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
    - 18.41
    metric_stds:
    - 0.22
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
    is_best: true
    metric_values:
    - 18.54
    metric_stds:
    - 0.86
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
    - 18.89
    metric_stds:
    - 0.22
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
    - 21.97
    metric_stds:
    - 0.45
  milestones:
  - value: 15.87
    std: 2.03
    model: DualEquiNet
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: 2025-06
---

