---
title: IMDB
slug: imdb
benchmark: Heterogeneous Graph Benchmarks
task_type: node_classification
description: Heterogeneous IMDB graph — classify movie nodes (3 genres).
primary_metric: Micro-F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.IMDB.html
stats: null
result_count: 25
best_model:
  model: GPS (EN H-19-RWPE)
  value: 0.7308
  metric: Micro-F1
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Micro-F1
  higher_is_better: true
  metrics:
  - Micro-F1
  - AP
  - Accuracy
  rows:
  - model: GPS (EN H-19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7308
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
  - model: GPS (LCP-ORC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7205
    - null
    - null
    metric_stds:
    - 0.0115
    - null
    - null
  - model: GPS (LCP-FRC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7148
    - null
    - null
    metric_stds:
    - 0.0103
    - null
    - null
  - model: GPS (No Encoding)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7093
    - null
    - null
    metric_stds:
    - 0.0121
    - null
    - null
  - model: GPS (20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7067
    - null
    - null
    metric_stds:
    - 0.0118
    - null
    - null
  - model: GCN (LCP-ORC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7064
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
  - model: GCN (EE H-19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7053
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: GIN (HCP-FRC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.704
    - null
    - null
    metric_stds:
    - 0.0152
    - null
    - null
  - model: GCN (LCP-FRC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7018
    - null
    - null
    metric_stds:
    - 0.0144
    - null
    - null
  - model: GIN (HCP-ORC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6992
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GCN (Norm. H-20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6948
    - null
    - null
    metric_stds:
    - 0.0171
    - null
    - null
  - model: GCN (Hodge H-20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6937
    - null
    - null
    metric_stds:
    - 0.0165
    - null
    - null
  - model: GCN (19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6935
    - null
    - null
    metric_stds:
    - 0.0224
    - null
    - null
  - model: GCN (20-LAPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6816
    - null
    - null
    metric_stds:
    - 0.0283
    - null
    - null
  - model: GCN (No Encoding)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6712
    - null
    - null
    metric_stds:
    - 0.0136
    - null
    - null
  - model: GPS (19-RWPE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.664
    - null
    - null
    metric_stds:
    - 0.0153
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.493
    - null
    metric_stds:
    - null
    - 0.008
    - null
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.69
    - null
    metric_stds:
    - null
    - 0.01
    - null
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.47
    - null
    metric_stds:
    - null
    - 0.011
    - null
  - model: Unitary GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.612
    - null
    metric_stds:
    - null
    - 0.014
    - null
  - model: Wide Unitary GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05499'
    title: Unitary convolutions for learning on graphs and groups
    date: '2024-10-07'
    date_iso: '2024-10-07'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.624
    - null
    metric_stds:
    - null
    - 0.013
    - null
  - model: GCN with AFR-3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.689
    metric_stds:
    - null
    - null
    - 0.011
  - model: GCN with BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.677
    metric_stds:
    - null
    - null
    - 0.015
  - model: GIN with AFR-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.678
    metric_stds:
    - null
    - null
    - 0.012
  - model: GCN with NONE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.476
    metric_stds:
    - null
    - null
    - 0.011
  milestones:
  - value: 0.7308
    std: 0.0124
    model: GPS (EN H-19-RWPE)
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: 2025-02
---

