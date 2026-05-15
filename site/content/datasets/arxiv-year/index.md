---
title: arxiv-year
slug: arxiv-year
benchmark: LINKX Benchmarks
task_type: node_classification
description: OGB-arXiv node classification by publication year (5 classes, heterophilic
  variant).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats: null
result_count: 22
best_model:
  model: S² DirGCN
  value: 0.6495
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  rows:
  - model: S² DirGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6495
    metric_stds:
    - 0.0033
  - model: FaberNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6462
    metric_stds:
    - 0.0101
  - model: DirGCN (tuned)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6444
    metric_stds:
    - 0.0027
  - model: DiGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
    date_iso: '2024-05-29'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6408
    metric_stds:
    - 0.0026
  - model: nsqure~
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5869
    metric_stds:
    - 0.0042
  - model: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.56
    metric_stds:
    - 0.0134
  - model: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4909
    metric_stds:
    - 0.001
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4605
    metric_stds:
    - 0.0051
  - model: Supervised
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4602
    metric_stds:
    - 0.0026
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4602
    metric_stds:
    - 0.0026
  - model: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4434
    metric_stds:
    - 0.0007
  - model: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4185
    metric_stds:
    - 0.0004
  - model: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4143
    metric_stds:
    - 0.0004
  - model: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4078
    metric_stds:
    - 0.0001
  - model: MaskGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4059
    metric_stds:
    - 0.0004
  - model: S2GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4032
    metric_stds:
    - 0.0012
  - model: Sp$^2$GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3909
    metric_stds:
    - 0.0002
  - model: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3815
    metric_stds:
    - 0.0026
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3768
    metric_stds:
    - 0.003
  - model: AUG-MAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.371
    metric_stds:
    - 0.0013
  - model: VGAER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3639
    metric_stds:
    - 0.0021
  - model: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3283
    metric_stds:
    - 0.0013
  milestones:
  - value: 0.6495
    std: 0.0033
    model: S² DirGCN
    arxiv_id: '2405.19121'
    title: Spatio-Spectral Graph Neural Networks
    date: '2024-05-29'
---

