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
result_count: 27
best_model:
  model: IDGL
  value: 0.836
  metric: Accuracy
  arxiv_id: '2006.13009'
  paper_title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and
    Robust Node Embeddings'
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
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.836
    metric_stds:
    - 0.004
  - model: IDGL-Anch
    model_plain: IDGL-Anch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.829
    metric_stds:
    - 0.003
  - model: GCN_kNN
    model_plain: GCN_kNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.813
    metric_stds:
    - 0.006
  - model: UniGCN
    model_plain: UniGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8024
    metric_stds:
    - 0.004
  - model: TriCL-N
    model_plain: TriCL-N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8018
    metric_stds:
    - 0.002
  - model: DHGNN
    model_plain: DHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8015
    metric_stds:
    - 0.003
  - model: TriCL
    model_plain: TriCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8014
    metric_stds:
    - 0.002
  - model: BiLSTM
    model_plain: BiLSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/hugochan/IDGL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.004
  - model: AllSet
    model_plain: AllSet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    metric_stds:
    - 0.004
  - model: HyperConv
    model_plain: HyperConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7983
    metric_stds:
    - 0.004
  - model: S2-HHGR
    model_plain: S2-HHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7975
    metric_stds:
    - 0.003
  - model: HNHN
    model_plain: HNHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7951
    metric_stds:
    - 0.004
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7919
    metric_stds:
    - 0.005
  - model: HyperGCN
    model_plain: HyperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7731
    metric_stds:
    - 0.06
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
    is_best: false
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
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.04739'
    title: 'I''m Me, We''re Us, and I''m Us: Tri-directional Contrastive Learning
      on Hypergraphs'
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/wooner49/TriCL
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6335
    metric_stds:
    - 0.017
  milestones:
  - value: 0.6851
    std: null
    model: Multinomial Naive Bayes
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: 2016-06
  - value: 0.836
    std: 0.004
    model: IDGL
    arxiv_id: '2006.13009'
    title: 'Iterative Deep Graph Learning for Graph Neural Networks: Better and Robust
      Node Embeddings'
    date: 2020-06
---

