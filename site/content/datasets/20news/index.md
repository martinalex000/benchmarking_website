---
title: 20News
slug: 20news
benchmark: Other Graph Benchmarks
task_type: graph_classification
description: '20 Newsgroups text classification represented as a graph (nodes = documents,
  edges = TF-IDF similarity). 20 classes.

  '
primary_metric: Accuracy
higher_is_better: true
pyg_url: ''
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 20
result_count: 12
best_model:
  model: Multinomial Naive Bayes
  value: 0.6851
  metric: Accuracy
  arxiv_id: '1606.09375'
  paper_title: Convolutional Neural Networks on Graphs with Fast Localized Spectral
    Filtering
variants:
- slug: standard-split
  name: Standard split
  notes: Used as a heterophilic benchmark in several GNN papers.
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
  - model: Multinomial Naive Bayes
    model_plain: Multinomial Naive Bayes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.6851
    metric_stds:
    - null
  - model: GC32
    model_plain: GC32
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6826
    metric_stds:
    - null
  - model: Softmax
    model_plain: Softmax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6628
    metric_stds:
    - null
  - model: LDS
    model_plain: LDS
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.6615
    metric_stds:
    - 0.0036
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.6601
    metric_stds:
    - 0.0118
  - model: GCN
    model_plain: GCN
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.6598
    metric_stds:
    - 0.0068
  - model: Linear SVM
    model_plain: Linear SVM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.659
    metric_stds:
    - null
  - model: FC2500-FC500
    model_plain: FC2500-FC500
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6576
    metric_stds:
    - null
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.6509
    metric_stds:
    - 0.0123
  - model: FC2500
    model_plain: FC2500
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 2016
    date_iso: 2016-06
    date_display: Jun 2016
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6464
    metric_stds:
    - null
  - model: DropEdge
    model_plain: DropEdge
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.6446
    metric_stds:
    - 0.0043
  - model: GAT
    model_plain: GAT
    is_baseline: true
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
    is_best: false
    metric_values:
    - 0.6406
    metric_stds:
    - 0.0044
  milestones:
  - value: 0.6851
    std: null
    model: Multinomial Naive Bayes
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: 2016-06
---

