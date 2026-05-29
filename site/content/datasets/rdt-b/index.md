---
title: RDT-B
slug: rdt-b
benchmark: TU Dortmund
task_type: graph_classification
description: Alias for REDDIT-BINARY in some papers.
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 2000
  avg_nodes: 429.63
  avg_edges: 497.75
  num_classes: 2
result_count: 1
best_model:
  model: PDF
  value: 0.934
  metric: Accuracy
  arxiv_id: '2305.06102'
  paper_title: Towards Better Graph Representation Learning with Parameterized Decomposition
    & Filtering
variants:
- slug: 10-fold-cv
  name: 10-fold CV
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  rows:
  - model: PDF
    model_plain: PDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.934
    metric_stds:
    - 0.013
  milestones:
  - value: 0.934
    std: 0.013
    model: PDF
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: '2023-05-10'
---

