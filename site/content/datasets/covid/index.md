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
result_count: 23
best_model:
  model: DualEquiNet
  value: 0.353
  metric: RMSE
  arxiv_id: '2506.19862'
  paper_title: DualEquiNet RNA Benchmarks
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
  - MSE
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
    - 0.353
    - null
    metric_stds:
    - 0.006
    - null
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
    - 0.356
    - null
    metric_stds:
    - 0.002
    - null
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
    is_best: true
    metric_values:
    - 0.356
    - null
    metric_stds:
    - 0.013
    - null
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
    is_best: true
    metric_values:
    - 0.362
    - null
    metric_stds:
    - 0.01
    - null
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
    - 0.475
    - null
    metric_stds:
    - 0.009
    - null
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
    - 0.478
    - null
    metric_stds:
    - 0.031
    - null
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
    - 0.531
    - null
    metric_stds:
    - 0.011
    - null
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
    - 0.533
    - null
    metric_stds:
    - 0.011
    - null
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
    - 0.534
    - null
    metric_stds:
    - 0.011
    - null
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
    - 0.535
    - null
    metric_stds:
    - 0.011
    - null
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
    - 0.535
    - null
    metric_stds:
    - 0.011
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.956
    metric_stds:
    - null
    - 0.034
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.956
    metric_stds:
    - null
    - 0.029
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.052
    metric_stds:
    - null
    - 0.081
  - model: GAT-kNN
    model_plain: GAT-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.861
    metric_stds:
    - null
    - 0.045
  - model: GCN-kNN
    model_plain: GCN-kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.475
    metric_stds:
    - null
    - 0.028
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.991
    metric_stds:
    - null
    - 0.078
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 1.271
    metric_stds:
    - null
    - 0.073
  - model: Framelets
    model_plain: Framelets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.938
    metric_stds:
    - null
    - 0.081
  - model: DMD-GCN
    model_plain: DMD-GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.76
    metric_stds:
    - null
    - 0.025
  - model: DMD-SGC
    model_plain: DMD-SGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.805
    metric_stds:
    - null
    - 0.067
  - model: DMD-ACMP
    model_plain: DMD-ACMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.809
    metric_stds:
    - null
    - 0.011
  - model: DMD++
    model_plain: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - 0.784
    metric_stds:
    - null
    - 0.013
  milestones:
  - value: 0.353
    std: 0.006
    model: DualEquiNet
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: 2025-06
---

