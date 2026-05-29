---
title: Amazon2M
slug: amazon2m
benchmark: Other Graph Benchmarks
task_type: node_classification
description: 'Large-scale Amazon co-purchase graph with ~2M nodes. Node classification
  (product category). Used to benchmark scalable GNNs and graph transformers.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: 1
  avg_nodes: 2000000.0
  avg_edges: 61000000.0
  num_classes: null
result_count: 2
best_model:
  model: Cluster-GCN (2-layer)
  value: 0.9041
  metric: F1
  arxiv_id: '1905.07953'
  paper_title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
    Convolutional Networks'
variants:
- slug: standard-split
  name: Standard split
  notes: ~2M nodes, ~61M edges.
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  rows:
  - model: Cluster-GCN (2-layer)
    model_plain: Cluster-GCN (2-layer)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/google-research/google-research
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.9041
    metric_stds:
    - null
  - model: VRGCN (2-layer)
    model_plain: VRGCN (2-layer)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/google-research/google-research
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9021
    metric_stds:
    - null
  milestones:
  - value: 0.9041
    std: null
    model: Cluster-GCN (2-layer)
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: 2019-05
---

