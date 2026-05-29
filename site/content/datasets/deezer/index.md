---
title: Deezer
slug: deezer
benchmark: Heterophilic Graphs
task_type: node_classification
description: Deezer Europe user friendship graph binary node classification (like/dislike)
  from the heterophilic benchmark.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.HeterophilousGraphDataset.html
stats:
  num_graphs: 1
  avg_nodes: 28281.0
  avg_edges: 1650703.0
  num_classes: 2
result_count: 1
best_model:
  model: novel all-pair message passing scheme
  value: 0.7124
  metric: ROC-AUC
  arxiv_id: '2306.08385'
  paper_title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure
    for Graph Neural Networks'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - ROC-AUC
  rows:
  - model: novel all-pair message passing scheme
    model_plain: novel all-pair message passing scheme
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.08385'
    title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for
      Graph Neural Networks'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/NodeFormer
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7124
    metric_stds:
    - 0.0032
  milestones:
  - value: 0.7124
    std: 0.0032
    model: novel all-pair message passing scheme
    arxiv_id: '2306.08385'
    title: 'Align All the Nodes: Scalable Learning of Flexible Latent Structure for
      Graph Neural Networks'
    date: 2023-06
---

