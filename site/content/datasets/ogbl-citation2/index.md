---
title: ogbl-citation2
slug: ogbl-citation2
benchmark: OGB
task_type: link_prediction
description: Citation link prediction on arXiv/PubMed papers (directed).
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBLinkPropPredDataset.html
stats: null
result_count: 4
best_model:
  model: QGAT
  value: 0.822
  metric: MRR
variants:
- slug: standard-split
  name: Standard split
  notes: 'Time-based split. Metric: MRR.'
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  metrics:
  - MRR
  - Accuracy
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
    - 0.822
    - null
    metric_stds:
    - 0.0127
    - null
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
    is_best: false
    metric_values:
    - 0.8014
    - null
    metric_stds:
    - 0.0071
    - null
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
    is_best: false
    metric_values:
    - 0.7595
    - null
    metric_stds:
    - 0.0131
    - null
  - model: HOPE-WavePE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via - High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9912
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.822
    std: 0.0127
    model: QGAT
    arxiv_id: '2508.17630'
    title: 'Quantum Graph Attention Network: A Novel Quantum Multi-Head Attention
      Mechanism for Graph Learning'
    date: 2025-08
---

