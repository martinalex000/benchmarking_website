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
stats: null
result_count: 23
best_model:
  model: DualEquiNet
  value: 0.353
  metric: RMSE
variants:
- slug: standard-split
  name: Standard split
  notes: RMSE on reactivity prediction (lower is better).
  is_standard: true
  primary_metric: RMSE
  higher_is_better: false
  metrics:
  - RMSE
  - MSE
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
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.353
    - null
    metric_stds:
    - 0.006
    - null
  - model: w/o CSIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    date_iso: 2025-06
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
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

