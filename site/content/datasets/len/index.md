---
title: LEN
slug: len
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: 'Labeled Entity Network — large-scale coordinated campaign detection
  graph for online social media analysis (node classification, 2 classes).

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats: null
result_count: 26
best_model:
  model: SAGE (RWW, Degree, 0.5)
  value: 0.852
  metric: Accuracy
variants:
- slug: standard-split
  name: Standard split
  notes: Introduced in arXiv:2506.13912.
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - RMSE E
  - RMSE F
  rows:
  - model: SAGE (RWW, Degree, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.852
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: SAGE (RWW, Truss, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: GAT (RWW, Core, mid)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: GCN (NF+RWW, Truss, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
  - model: GCN (RWW, Truss, median)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
  - model: GAT (RWW, Degree, median)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.022
    - null
    - null
  - model: GAT (NF+RWW, Truss, median)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.03
    - null
    - null
  - model: GIN (NF+RWW, Core, mid)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: SAGE (NF+RWW, Core, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.79
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: GCN (RWW, Core, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.787
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GAT (NF+RWW, Core, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.785
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GCN (RWW, Degree, mid)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GIN (NF+RWW, Truss, mid)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.782
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
  - model: SAGE (RWW, Core, mid)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    - null
    - null
    metric_stds:
    - 0.025
    - null
    - null
  - model: GIN (RWW, Truss, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GCN (NF+RWW, Core, median)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.766
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: SAGE (NF+RWW, Degree, median)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.758
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GIN (RWW, Degree, 0.5)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GAT (NF)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: SAGE (NF)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.729
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GCN (NF)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: GIN (NF)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.633
    - null
    - null
    metric_stds:
    - 0.065
    - null
    - null
  - model: Lorem
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.020999
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 3.309
    - 50.084
    metric_stds:
    - null
    - null
    - null
  - model: Cace-Les
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 17.803
    - 147.616
    metric_stds:
    - null
    - null
    - null
  - model: Mace
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 12.592
    - 104.318
    metric_stds:
    - null
    - null
    - null
  - model: Pet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.19382'
    title: Learning Long-Range Representations with Equivariant Messages
    date: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 3.205
    - 46.905
    metric_stds:
    - null
    - null
    - null
  milestones:
  - value: 0.852
    std: 0.01
    model: SAGE (RWW, Degree, 0.5)
    arxiv_id: '2506.13912'
    title: Density-aware Walks for Coordinated Campaign Detection
    date: 2025-06
---

