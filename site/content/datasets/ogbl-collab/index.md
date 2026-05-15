---
title: ogbl-collab
slug: ogbl-collab
benchmark: OGB
task_type: link_prediction
description: Link prediction on academic collaboration network (author co-authorship).
primary_metric: Hits@50
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBLinkPropPredDataset.html
stats: null
result_count: 15
best_model:
  model: QGAT
  value: 0.512
  metric: Hits@50
variants:
- slug: standard-split
  name: Standard split
  notes: 'Time-based split. Metric: Hits@50.'
  is_standard: true
  primary_metric: Hits@50
  higher_is_better: true
  metrics:
  - Hits@50
  rows:
  - model: QGAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.512
    metric_stds:
    - 0.0192
  - model: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.497
    metric_stds:
    - 0.0059
  - model: Graph transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.497
    metric_stds:
    - 0.0059
  - model: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.497
    metric_stds:
    - 0.0308
  - model: GPM w/o PE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.4959
    metric_stds:
    - 0.0065
  - model: LLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.491
    metric_stds:
    - 0.0057
  - model: GPM w/o AP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.4843
    metric_stds:
    - 0.0097
  - model: GPM w/o PE & AP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4824
    metric_stds:
    - 0.0097
  - model: RUM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4819
    metric_stds:
    - 0.0094
  - model: GPM GRU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4812
    metric_stds:
    - 0.0055
  - model: GPM Mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4783
    metric_stds:
    - 0.01
  - model: Nagphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4756
    metric_stds:
    - 0.0052
  - model: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.4663
    metric_stds:
    - 0.028
  - model: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4656
    metric_stds:
    - 0.0062
  - model: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4475
    metric_stds:
    - 0.0107
  milestones:
  - value: 0.497
    std: 0.0059
    model: GPM
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
  - value: 0.512
    std: 0.0192
    model: QGAT
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: 2025-08
---

