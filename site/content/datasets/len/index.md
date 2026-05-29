---
title: LEN
slug: len
benchmark: Hypergraph Benchmarks
task_type: node_classification
description: 'Labeled Entity Network — large-scale coordinated campaign detection
  graph for online social media analysis (node classification, 2 classes).

  '
primary_metric: Accuracy
higher_is_better: false
pyg_url: ''
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 2
result_count: 6
best_model:
  model: sRGCNN_Cayley
  value: 0.922
  metric: RMSE
  arxiv_id: '1705.07664'
  paper_title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
    Spectral Filters'
variants:
- slug: standard-split
  name: Standard split
  notes: Introduced in arXiv:2506.13912.
  is_standard: true
  primary_metric: RMSE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - RMSE
  rows:
  - model: sRGCNN_Cayley
    model_plain: sRGCNN_Cayley
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.922
    metric_stds:
    - null
  - model: sRGCNN_Cheby_r=4
    model_plain: sRGCNN_Cheby_r=4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    metric_stds:
    - null
  - model: GRALS
    model_plain: GRALS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.945
    metric_stds:
    - null
  - model: MC
    model_plain: MC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.973
    metric_stds:
    - null
  - model: GMC
    model_plain: GMC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.996
    metric_stds:
    - null
  - model: IMC
    model_plain: IMC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 2017
    date_iso: 2017-05
    date_display: May 2017
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.653
    metric_stds:
    - null
  milestones:
  - value: 0.922
    std: null
    model: sRGCNN_Cayley
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: 2017-05
---

