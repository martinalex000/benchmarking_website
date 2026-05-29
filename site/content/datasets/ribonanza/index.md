---
title: Ribonanza
slug: ribonanza
benchmark: DualEquiNet RNA Benchmarks
task_type: graph_regression
description: RNA reactivity prediction on the Ribonanza benchmark (DMS/2A3 chemical
  probing).
primary_metric: RMSE
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: 2260
  avg_nodes: null
  avg_edges: null
  num_classes: null
result_count: 7
best_model:
  model: EU
  value: 0.558
  metric: RMSE
  arxiv_id: '2506.19862'
  paper_title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large
    Biomolecules'
variants:
- slug: standard-split
  name: Standard split
  notes: From Kaggle Ribonanza competition.
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
  - model: EU
    model_plain: EU
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
    - 0.558
    metric_stds:
    - 0.012
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
    - 0.839
    metric_stds:
    - 0.02
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
    - 0.857
    metric_stds:
    - 0.013
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
    - 0.932
    metric_stds:
    - 0.01
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
    - 0.934
    metric_stds:
    - 0.01
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
    - 0.937
    metric_stds:
    - 0.012
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
    - 0.939
    metric_stds:
    - 0.012
  milestones:
  - value: 0.558
    std: 0.012
    model: EU
    arxiv_id: '2506.19862'
    title: 'DualEquiNet: A Dual-Space Hierarchical Equivariant Network for Large Biomolecules'
    date: 2025-06
---

