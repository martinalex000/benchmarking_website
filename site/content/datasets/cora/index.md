---
title: Cora
slug: cora
benchmark: Classic
task_type: node_classification
description: Citation network node classification (7 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Planetoid.html
stats: null
result_count: 22
best_model:
  model: NID_GCN (End-to-End Learning)
  value: 87.88
  metric: Accuracy
variants:
- slug: random-10-fold
  name: Random 10-fold
  notes: 10-fold cross-validation; results not directly comparable to Planetoid.
  is_standard: false
  primary_metric: Accuracy
  higher_is_better: true
  metrics:
  - Accuracy
  - Efficiency
  - GED
  - RSE
  - Usage rate
  - Voltage
  rows:
  - model: NID_GCN (End-to-End Learning)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: true
    metric_values:
    - 87.88
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.69
    - null
    - null
    - null
    - null
    - null
  - model: NID_GCN (Post-hoc RVQ)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 86.17
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.33
    - null
    - null
    - null
    - null
    - null
  - model: NID_GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 85.63
    - null
    - 6.15
    - null
    - 84.7
    - null
    metric_stds:
    - 0.31
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 84.0
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.4
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 83.5
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.4
    - null
    - null
    - null
    - null
    - null
  - model: InfoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 83.5
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.3
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 82.3
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.6
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 81.83
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.26
    - null
    - null
    - null
    - null
    - null
  - model: NID_SAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 76.78
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.59
    - null
    - null
    - null
    - null
    - null
  - model: VQGraph without reconstruction loss
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 76.17
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.47
    - null
    - null
    - null
    - null
    - null
  - model: VQGraph
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 76.08
    - null
    - 6.85
    - null
    - 1.3
    - null
    metric_stds:
    - 0.55
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 71.5
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.4
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 70.52
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.14
    - null
    - null
    - null
    - null
    - null
  - model: DGCluster
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 69.8
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VQGraph tokens
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 63.39
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 1.15
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - 57.8
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.5
    - null
    - null
    - null
    - null
    - null
  - model: GT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: 'GraphBench: Next-generation graph learning benchmarking'
    date: Dec 2025
    date_iso: '2025-12-04'
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.29
    - null
    - 0.29
    - null
    - 0.39
    metric_stds:
    - null
    - 0.03
    - null
    - 0.03
    - null
    - 0.05
  - model: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: 'GraphBench: Next-generation graph learning benchmarking'
    date: Dec 2025
    date_iso: '2025-12-04'
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.44
    - null
    - 0.44
    - null
    - 0.54
    metric_stds:
    - null
    - 0.13
    - null
    - 0.13
    - null
    - 0.12
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04475'
    title: 'GraphBench: Next-generation graph learning benchmarking'
    date: Dec 2025
    date_iso: '2025-12-04'
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.38
    - null
    - 0.38
    - null
    - 0.48
    metric_stds:
    - null
    - 0.05
    - null
    - 0.05
    - null
    - 0.02
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2512.04475'
    title: 'GraphBench: Next-generation graph learning benchmarking'
    date: Dec 2025
    date_iso: '2025-12-04'
    codebase_url: https://github.com/graphbench/package
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.53
    - null
    - 0.53
    - null
    - 0.61
    metric_stds:
    - null
    - 0.06
    - null
    - 0.06
    - null
    - 0.07
  - model: NID_GCN(M=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 83.3
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: May 2024
    date_iso: '2024-05-26'
    codebase_url: https://github.com/LUOyk1999/NodeID
    uses_external_data: null
    is_best: false
    metric_values:
    - null
    - null
    - 7.21
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 87.88
    std: 0.69
    model: NID_GCN (End-to-End Learning)
    arxiv_id: '2405.16435'
    title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph
      Learning'
    date: '2024-05-26'
---

