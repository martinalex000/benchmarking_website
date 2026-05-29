---
title: Reddit
slug: reddit
benchmark: Classic
task_type: node_classification
description: Reddit posts node classification (41 community labels) from the GraphSAGE
  paper.
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.Reddit.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 41
result_count: 404
best_model:
  model: SIGN
  value: 0.968
  metric: F1
  arxiv_id: '2004.11198'
  paper_title: 'SIGN: Scalable Inception Graph Neural Networks'
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  - AA
  - ACC
  - AP
  - ASR
  - AUC
  - AUC-ROC
  - Accuracy
  - CTA
  - F1-macro
  - F1-micro
  - Hit@10
  - MR
  - Macro-F1
  - Micro-F1
  - ROC-AUC
  rows:
  - model: SIGN
    model_plain: SIGN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.968
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Neighbor2Seq+Conv
    model_plain: Neighbor2Seq+Conv
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.967
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Neighbor2Seq+Attn
    model_plain: Neighbor2Seq+Attn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.967
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.966
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
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
    is_best: false
    metric_values:
    - 0.966
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT-EDGE
    model_plain: GraphSAINT-EDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.966
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT + RWSE
    model_plain: GraphSAINT + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.966
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GaAN
    model_plain: GaAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.964
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Stochastic-GCN
    model_plain: Stochastic-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.964
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.03341'
    title: 'Neighbor2Seq: Deep Learning on Massive Graphs by Transforming Neighbors
      to Sequences'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/divelab/Neighbor2Seq
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.964
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GaAN
    model_plain: GaAN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9636
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
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
    - 0.963
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Attention-only
    model_plain: Attention-only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9619
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Parallelized Graph Sampling
    model_plain: Parallelized Graph Sampling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.96
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pairwise+sigmoid
    model_plain: Pairwise+sigmoid
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9586
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AS-GCN
    model_plain: AS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.958
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Pairwise+tanh
    model_plain: Pairwise+tanh
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.958
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Avg. pooling
    model_plain: Avg. pooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9578
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.07161'
    title: arXiv:2206.07161
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.957
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphFM-IB + SAGE
    model_plain: GraphFM-IB + SAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.07161'
    title: arXiv:2206.07161
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.957
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Max pooling
    model_plain: Max pooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9562
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE-LSTM
    model_plain: SAGE-LSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.954
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGCN
    model_plain: DAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9539
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.953
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GSC
    model_plain: GSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.953
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SubG-Con
    model_plain: SubG-Con
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.952
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.951
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9504
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE-mean
    model_plain: SAGE-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.95
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.949
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1908.05081'
    title: 'AdaGCN: Adaboosting Graph Convolutional Networks into Deep Models'
    date: Aug 2019
    date_iso: 2019-08
    date_display: Aug 2019
    codebase_url: https://github.com/datake/AdaGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.9446
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ILLS
    model_plain: ILLS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.941
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.94
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.938
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphtransformer
    model_plain: Graphtransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.937
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.937
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.936
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ICG_u-NN
    model_plain: ICG_u-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.936
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.935
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_iso: '2023-05-27'
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.934
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random-Init DGI
    model_plain: Random-Init DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.933
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES
    model_plain: LADIES
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.932
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.931
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE-GCN
    model_plain: SAGE-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: Feb 19, 2019
    date_iso: '2019-02-19'
    date_display: Feb 2019
    codebase_url: https://github.com/Tiiiger/SGC
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.93
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES (512)
    model_plain: LADIES (512)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.928
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.925
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_iso: 2020-04
    date_display: Apr 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.924
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.923
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.921
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.92
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(GSAGE-mean, l=1)
    model_plain: GZoom(GSAGE-mean, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.919
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.918
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(GSAGE-GCN, l=1)
    model_plain: GZoom(GSAGE-GCN, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.917
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(GSAGE-LSTM, l=1)
    model_plain: GZoom(GSAGE-LSTM, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.917
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Full-Batch
    model_plain: Full-Batch
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.916
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.915
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: Oct 2017
    date_iso: 2017-10
    date_display: Oct 2017
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.912
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GZoom(GSAGE-pool, l=1)
    model_plain: GZoom(GSAGE-pool, l=1)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.912
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-GCN
    model_plain: GraphSAGE-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.908
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-LSTM
    model_plain: GraphSAGE-LSTM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.907
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DC-Graph
    model_plain: DC-Graph
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.905
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.901
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SFGC
    model_plain: SFGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.899
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-mean
    model_plain: GraphSAGE-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.897
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPT-GNN
    model_plain: GPT-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ICG-NN
    model_plain: ICG-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.896
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (8192)
    model_plain: FastGCN (8192)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.895
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1910.02370'
    title: 'GraphZoom: A Multi-level Spectral Approach for Accurate and Scalable Graph
      Embedding'
    date: Oct 2019
    date_iso: 2019-10
    date_display: Oct 2019
    codebase_url: https://github.com/cornell-zhang/GraphZoom
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.892
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AS-GCN
    model_plain: AS-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.89
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.013
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.885
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE (unsp.)
    model_plain: GraphSAGE (unsp.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.88
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph Infomax
    model_plain: Graph Infomax
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.877
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: No Pre-train
    model_plain: No Pre-train
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15437'
    title: 'GPT-GNN: Generative Pre-Training of Graph Neural Networks'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/acbull/GPT-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.873
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GC
    model_plain: GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.864
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LADIES (64)
    model_plain: LADIES (64)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.835
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN
    model_plain: FastGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.05872'
    title: 'Sampling methods for efficient training of graph convolutional networks:
      A survey'
    date: Mar 2021
    date_iso: 2021-03
    date_display: Mar 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Whole Dataset
    model_plain: Whole Dataset
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.825
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 2-Layer FNN
    model_plain: 2-Layer FNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: Mar 2018
    date_iso: 2018-03
    date_display: Mar 2018
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7358
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GDEM
    model_plain: GDEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCSR
    model_plain: GCSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN-HWN-full
    model_plain: CLN-HWN-full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.719
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN-HWN-mini
    model_plain: CLN-HWN-mini
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.712
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Herding
    model_plain: Herding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCDM
    model_plain: GCDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.709
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLN-FNN
    model_plain: CLN-FNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.705
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGC
    model_plain: SimGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SL-RF
    model_plain: SL-RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.688
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Kcenter
    model_plain: Kcenter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.683
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6718
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HWN-noRel
    model_plain: HWN-noRel
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.668
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.663
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6574
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SL-LR
    model_plain: SL-LR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.653
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MNCI
    model_plain: MNCI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6526
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6495
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT
    model_plain: GIANT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6464
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGC
    model_plain: DGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6287
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLDG_node
    model_plain: CLDG_node
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6287
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6249
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CLDG_graph
    model_plain: CLDG_graph
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6226
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6186
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6178
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphText
    model_plain: GraphText
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6146
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAdapter
    model_plain: GraphAdapter
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6113
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3GC + CMV-ND
    model_plain: S^3GC + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0134
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6095
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CO-EVOLVE
    model_plain: CO-EVOLVE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE
    model_plain: TAPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.605
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM-GNN
    model_plain: GLEM-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5941
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ENGINE
    model_plain: ENGINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5934
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TAPE
    model_plain: TAPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5918
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Coarsening
    model_plain: Coarsening
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17063'
    title: 'Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised
      Learning'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/XYGaoG/CTGCcode
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.591
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.04
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CCA-SSG
    model_plain: CCA-SSG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5869
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-Center
    model_plain: K-Center
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.585
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Raw features
    model_plain: Raw features
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.585
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5841
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5809
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5802
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DinkNet
    model_plain: DinkNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Patton
    model_plain: Patton
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5785
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAW
    model_plain: CAW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.578
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM-LM
    model_plain: GLEM-LM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5756
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PGD + HAO
    model_plain: PGD + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5699000000000001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AGIA + HAO
    model_plain: AGIA + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.569
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.14451'
    title: 'CLDG: Contrastive Learning on Dynamic Graphs'
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: https://github.com/yimingxu24/CLDG
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5681
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Patton
    model_plain: Patton
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5653
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: S^3GC
    model_plain: S^3GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5643
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0134
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: wvRN-RL
    model_plain: wvRN-RL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.558
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5578
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Sent-BERT
    model_plain: Sent-BERT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5577
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: wvRN-IC
    model_plain: wvRN-IC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/trangptm/Column
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.547
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TDGIA + HAO
    model_plain: TDGIA + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5432
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MetaGIA + HAO
    model_plain: MetaGIA + HAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08057'
    title: Understanding and Improving Graph Injection Attack by Promoting Unnoticeability
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/LFhase/GIA-HAO
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5414
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProGCL + CMV-ND
    model_plain: ProGCL + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5377
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InstructGLM
    model_plain: InstructGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.07457'
    title: 'GLBench: A Comprehensive Benchmark for Graph with Large Language Models'
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/NineAbyss/GLBench
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5317
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5246
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InstructGLM
    model_plain: InstructGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.19596'
    title: 'CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics
      for Heterophilous Learning'
    date: Mar 2026
    date_iso: 2026-03
    date_display: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5192
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProGCL
    model_plain: ProGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4773
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0184
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Coarsening
    model_plain: Coarsening
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.20724'
    title: on Large Graphs using Intersecting Communities
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/benfinkelshtein/ICGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.474
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.11996'
    title: Generative Subgraph Contrast for Self-Supervised Graph Representation Learning
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: https://github.com/yh-han/GSC.git
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.324
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (64)
    model_plain: FastGCN (64)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.278
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.126
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means + CMV-ND
    model_plain: K-means + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.268
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0241
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI + CMV-ND
    model_plain: DGI + CMV-ND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2355
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0243
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FastGCN (512)
    model_plain: FastGCN (512)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.07323'
    title: Layer-Dependent Importance Sampling for Training Deep and Large Graph Convolutional
      Networks
    date: Nov 2019
    date_iso: 2019-11
    date_display: Nov 2019
    codebase_url: https://github.com/acbull/LADIES
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.175
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.167
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1748
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Meta-GNN
    model_plain: Meta-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.09718'
    title: 'Meta-GNN: On Few-shot Node Classification in Graph Meta-learning'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/AI-DL-Conference/Meta-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1422
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Meta-SGC
    model_plain: Meta-SGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.09718'
    title: 'Meta-GNN: On Few-shot Node Classification in Graph Meta-learning'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/AI-DL-Conference/Meta-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1415
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.09718'
    title: 'Meta-GNN: On Few-shot Node Classification in Graph Meta-learning'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/AI-DL-Conference/Meta-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.09718'
    title: 'Meta-GNN: On Few-shot Node Classification in Graph Meta-learning'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/AI-DL-Conference/Meta-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.098
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-mean
    model_plain: GraphSAGE-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.09718'
    title: 'Meta-GNN: On Few-shot Node Classification in Graph Meta-learning'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/AI-DL-Conference/Meta-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0947
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE-pool
    model_plain: GraphSAGE-pool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.09718'
    title: 'Meta-GNN: On Few-shot Node Classification in Graph Meta-learning'
    date: May 2019
    date_iso: 2019-05
    date_display: May 2019
    codebase_url: https://github.com/AI-DL-Conference/Meta-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0931
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: K-means
    model_plain: K-means
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.13368'
    title: Scalable Attribute-Missing Graph Clustering via Neighborhood Differentiation
    date: Jul 9, 2025
    date_iso: '2025-07-09'
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.068
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - 0.0261
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.9751
    - null
    - null
    - null
    - null
    - null
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
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.9634
    - null
    - null
    - null
    - null
    - null
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
    - 0.0083
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.9818
    - null
    - null
    - null
    - null
    - null
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
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.9823
    - null
    - null
    - null
    - null
    - null
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
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGNs
    model_plain: DGNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_iso: '2024-06-04'
    date_display: Jun 2024
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.9861
    - null
    - null
    - null
    - null
    - null
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
    - 0.0004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VQ-GNN
    model_plain: VQ-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14363'
    title: 'VQ-GNN: A Universal Framework to Scale-up Graph Neural Networks using
      Vector Quantization'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9399
    - null
    - null
    - null
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
    - null
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NS-SAGE
    model_plain: NS-SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14363'
    title: 'VQ-GNN: A Universal Framework to Scale-up Graph Neural Networks using
      Vector Quantization'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9615
    - null
    - null
    - null
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
    - null
    - 0.0089
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14363'
    title: 'VQ-GNN: A Universal Framework to Scale-up Graph Neural Networks using
      Vector Quantization'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9264
    - null
    - null
    - null
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
    - null
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAINT + RWSE
    model_plain: GraphSAINT + RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.14363'
    title: 'VQ-GNN: A Universal Framework to Scale-up Graph Neural Networks using
      Vector Quantization'
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9225
    - null
    - null
    - null
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
    - null
    - 0.0057
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5839
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.005
  - model: VAGE
    model_plain: VAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5798
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.006
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6452
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.005
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6124
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.006
  - model: CTDNE
    model_plain: CTDNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5943
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.006
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6183
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.027
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6556
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.007
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6291
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.024
  - model: TGN-attn
    model_plain: TGN-attn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10637'
    title: Temporal Graph Networks for Deep Learning on Dynamic Graphs
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6706
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.009
  - model: GraphSAINT
    model_plain: GraphSAINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9235
    - null
    - null
    - null
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
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PPRGo
    model_plain: PPRGo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9038
    - null
    - null
    - null
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
    - null
    - 0.0011
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9281
    - null
    - null
    - null
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
    - null
    - 0.0003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8897
    - null
    - null
    - null
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
    - null
    - 0.0032
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8963
    - null
    - null
    - null
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
    - null
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ANS-GT
    model_plain: ANS-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9323
    - null
    - null
    - null
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
    - null
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NAGphormer
    model_plain: NAGphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9358
    - null
    - null
    - null
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
    - null
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VCR-Graphormer
    model_plain: VCR-Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9369
    - null
    - null
    - null
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
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAM-GT
    model_plain: DAM-GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.17660'
    title: 'DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer
      for Node Classification'
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9392
    - null
    - null
    - null
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
    - null
    - 0.0007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9733
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9765
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9711
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9798
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9812
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN-attn
    model_plain: TGN-attn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.987
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAW
    model_plain: CAW
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9839
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PINT
    model_plain: PINT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15059'
    title: Provably expressive temporal graph networks
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9903
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.924
    - null
    - null
    - null
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
    - null
    - 0.025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.921
    - null
    - null
    - null
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
    - null
    - 0.026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6882
    - null
    - null
    - null
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
    - null
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGK
    model_plain: DGK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7804
    - null
    - null
    - null
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
    - null
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: graph2vec
    model_plain: graph2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7578
    - null
    - null
    - null
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
    - null
    - 0.0103
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.825
    - null
    - null
    - null
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
    - null
    - 0.0142
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8953
    - null
    - null
    - null
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
    - null
    - 0.0084
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8529
    - null
    - null
    - null
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
    - null
    - 0.0135
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCC
    model_plain: GCC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.898
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.845
    - null
    - null
    - null
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
    - null
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7684
    - null
    - null
    - null
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
    - null
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: UGMAE
    model_plain: UGMAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08023'
    title: 'UGMAE: A Unified Framework for Graph Masked Autoencoders'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8954
    - null
    - null
    - null
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
    - null
    - 0.0021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.467
    - 0.624
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ARGE
    model_plain: ARGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.601
    - 0.645
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DSGC
    model_plain: DSGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.611
    - 0.693
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.418
    - 0.605
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIC
    model_plain: GIC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.433
    - 0.622
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.639
    - 0.752
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FeatWalk
    model_plain: FeatWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.503
    - 0.663
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAN
    model_plain: CAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.726
    - 0.82
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CONN
    model_plain: CONN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.11981'
    title: Collaborative Graph Neural Networks for Attributed Network Embedding
    date: Jul 2023
    date_iso: 2023-07
    date_display: Jul 2023
    codebase_url: https://github.com/Qiaoyut/CONN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.879
    - 0.913
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-4
    model_plain: GCN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.928
    - null
    - null
    - null
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
    - null
    - 0.017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-3-TOGL-1
    model_plain: GCN-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.561
    - null
    - null
    - null
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
    - null
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIN-4
    model_plain: GIN-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.817
    - null
    - null
    - null
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
    - null
    - 0.069
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-4
    model_plain: GAT-4
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.442
    - null
    - null
    - null
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
    - null
    - 0.066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT-3-TOGL-1
    model_plain: GAT-3-TOGL-1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.895
    - null
    - null
    - null
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
    - null
    - 0.087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.78
    - null
    - null
    - null
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
    - null
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL-OA
    model_plain: WL-OA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.876
    - null
    - null
    - null
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
    - null
    - 0.003
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GFL
    model_plain: GFL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.557
    - null
    - null
    - null
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
    - null
    - 0.021
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN-1-TOGL-1 (static)
    model_plain: GCN-1-TOGL-1 (static)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.555
    - null
    - null
    - null
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
    - null
    - 0.018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PersLay
    model_plain: PersLay
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.07835'
    title: Topological Graph Neural Networks
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/BorgwardtLab/TOGL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.556
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TPP
    model_plain: TPP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.12230'
    title: 'Continual Graph Learning: A Survey'
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.994
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (Ogb-feature)
    model_plain: GNN (Ogb-feature)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6191
    - null
    - null
    - null
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
    - null
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (RoBERTa)
    model_plain: GNN (RoBERTa)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6191
    - null
    - null
    - null
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
    - null
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (RoBERTa+Prop)
    model_plain: GNN (RoBERTa+Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6198
    - null
    - null
    - null
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
    - null
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT (BERT)
    model_plain: GIANT (BERT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6379
    - null
    - null
    - null
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
    - null
    - 0.0045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GIANT (BERT+Prop)
    model_plain: GIANT (BERT+Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6348
    - null
    - null
    - null
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
    - null
    - 0.0039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM (DeBERTa)
    model_plain: GLEM (DeBERTa)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6228
    - null
    - null
    - null
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
    - null
    - 0.006
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM (DeBERTa+Prop)
    model_plain: GLEM (DeBERTa+Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6221
    - null
    - null
    - null
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
    - null
    - 0.0052
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLPs (Llama 2 + Prop)
    model_plain: MLPs (Llama 2 + Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6123
    - null
    - null
    - null
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
    - null
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LoRA (Llama 2 + Prop)
    model_plain: LoRA (Llama 2 + Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.574
    - null
    - null
    - null
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
    - null
    - 0.0172
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (Llama 2)
    model_plain: GNN (Llama 2)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.632
    - null
    - null
    - null
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
    - null
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (Llama 2+Prop)
    model_plain: GNN (Llama 2+Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6324
    - null
    - null
    - null
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
    - null
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graph2Text (Llama 2 + Prop)
    model_plain: Graph2Text (Llama 2 + Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6053
    - null
    - null
    - null
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
    - null
    - 0.0033
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAdapter
    model_plain: GraphAdapter
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6461
    - null
    - null
    - null
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
    - null
    - 0.0019
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: BERT-GNN
    model_plain: BERT-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6061
    - null
    - null
    - null
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
    - null
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAdapter (BERT)
    model_plain: GraphAdapter (BERT)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6366
    - null
    - null
    - null
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
    - null
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLEM (RoBERTa)
    model_plain: GLEM (RoBERTa)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6228
    - null
    - null
    - null
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
    - null
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphAdapter (RoBERTa)
    model_plain: GraphAdapter (RoBERTa)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6379
    - null
    - null
    - null
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
    - null
    - 0.0061
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (PLM)
    model_plain: GNN (PLM)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6191
    - null
    - null
    - null
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
    - null
    - 0.0043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN (PLM+Prop)
    model_plain: GNN (PLM+Prop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6198
    - null
    - null
    - null
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
    - null
    - 0.0036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GNN w Pretraining
    model_plain: GNN w Pretraining
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.641
    - null
    - null
    - null
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
    - null
    - 0.0027
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Re-init All
    model_plain: Re-init All
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6369
    - null
    - null
    - null
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
    - null
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Re-init GNN
    model_plain: Re-init GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6364
    - null
    - null
    - null
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
    - null
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Re-init Fusion
    model_plain: Re-init Fusion
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6378
    - null
    - null
    - null
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
    - null
    - 0.0022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Only GNN (GAT*)
    model_plain: Only GNN (GAT*)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6495
    - null
    - null
    - null
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
    - null
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Only GNN (SAGE)
    model_plain: Only GNN (SAGE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.12984'
    title: Can GNN be Good Adapter for LLMs?
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/zjunet/GraphAdapter
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.632
    - null
    - null
    - null
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
    - null
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8965
    - null
    - null
    - null
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
    - null
    - 0.0014
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9008
    - null
    - null
    - null
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
    - null
    - 0.0044
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9144
    - null
    - null
    - null
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
    - null
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9168
    - null
    - null
    - null
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
    - null
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9171
    - null
    - null
    - null
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
    - null
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AM-GCN
    model_plain: AM-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.902
    - null
    - null
    - null
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
    - null
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DEMO-Net
    model_plain: DEMO-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8953
    - null
    - null
    - null
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
    - null
    - 0.0029
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.8987
    - null
    - null
    - null
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
    - null
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9037
    - null
    - null
    - null
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
    - null
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.923
    - null
    - null
    - null
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
    - null
    - 0.0155
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.92
    - null
    - null
    - null
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
    - null
    - 0.0024
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MGNN
    model_plain: MGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9198
    - null
    - null
    - null
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
    - null
    - 0.0042
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IGNN-Solver (AA)
    model_plain: IGNN-Solver (AA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9391
    - null
    - null
    - null
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
    - null
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IGNN-Solver (NN)
    model_plain: IGNN-Solver (NN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.08524'
    title: 'IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/landrarwolf/IGNN-Solver
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.9242
    - null
    - null
    - null
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
    - null
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ERM
    model_plain: ERM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.447
    - null
    - null
    - null
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
    - null
    - 0.0431
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Attention
    model_plain: Attention
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4381
    - null
    - null
    - null
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
    - null
    - 0.0478
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Top-K Pooling
    model_plain: Top-K Pooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3881
    - null
    - null
    - null
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
    - null
    - 0.0268
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGPooling
    model_plain: SAGPooling
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3706
    - null
    - null
    - null
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
    - null
    - 0.0899
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Virtual Node
    model_plain: Virtual Node
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.2881
    - null
    - null
    - null
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
    - null
    - 0.0097
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropoutEdge
    model_plain: DropoutEdge
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.2877
    - null
    - null
    - null
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
    - null
    - 0.0915
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DropoutNode
    model_plain: DropoutNode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.2759
    - null
    - null
    - null
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
    - null
    - 0.0859
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FLAG
    model_plain: FLAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3845
    - null
    - null
    - null
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
    - null
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MixUp
    model_plain: MixUp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4853
    - null
    - null
    - null
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
    - null
    - 0.0254
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Group DRO
    model_plain: Group DRO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3917
    - null
    - null
    - null
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
    - null
    - 0.0317
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IRM
    model_plain: IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3191
    - null
    - null
    - null
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
    - null
    - 0.0694
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: V-REx
    model_plain: V-REx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3458
    - null
    - null
    - null
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
    - null
    - 0.059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: IB-IRM
    model_plain: IB-IRM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3004
    - null
    - null
    - null
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
    - null
    - 0.0469
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAD
    model_plain: CAD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3799
    - null
    - null
    - null
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
    - null
    - 0.009
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3977
    - null
    - null
    - null
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
    - null
    - 0.0477
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OOD-GNN
    model_plain: OOD-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.2853
    - null
    - null
    - null
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
    - null
    - 0.0074
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SizeShiftReg
    model_plain: SizeShiftReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.3302
    - null
    - null
    - null
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
    - null
    - 0.0087
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: OOD-GMixup
    model_plain: OOD-GMixup
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.08344'
    title: Graph Out-of-Distribution Generalization with Controllable Data Augmentation
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5046
    - null
    - null
    - null
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
    - null
    - 0.0141
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: AutoGCL
    model_plain: AutoGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5675
    - null
    - null
    - null
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
    - null
    - 0.0018
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TopER
    model_plain: TopER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5651
    - null
    - null
    - null
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
    - null
    - 0.0222
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PH
    model_plain: PH
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01778'
    title: 'TopER: Topological Embeddings in Graph Representation Learning'
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/AstritTola/TopER
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.541
    - null
    - null
    - null
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
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DC-Graph
    model_plain: DC-Graph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 99.9
    - null
    - null
    - null
    - 85.38
    - null
    - null
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
    - 0.03
    - null
    - null
    - null
    - 0.42
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 99.84
    - null
    - null
    - null
    - 88.5
    - null
    - null
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
    - 0.14
    - null
    - null
    - null
    - 0.27
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCond-X
    model_plain: GCond-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 99.89
    - null
    - null
    - null
    - 87.47
    - null
    - null
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
    - 0.07
    - null
    - null
    - null
    - 0.21
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 99.99
    - null
    - null
    - null
    - 90.37
    - null
    - null
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
    - 0.01
    - null
    - null
    - null
    - 0.22
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 99.85
    - null
    - null
    - null
    - 88.33
    - null
    - null
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
    - 0.12
    - null
    - null
    - null
    - 0.92
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 99.99
    - null
    - null
    - null
    - 90.65
    - null
    - null
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
    - 0.0
    - null
    - null
    - null
    - 0.13
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 100.0
    - null
    - null
    - null
    - 42.75
    - null
    - null
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
    - 0.0
    - null
    - null
    - null
    - 0.95
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 100.0
    - null
    - null
    - null
    - 88.41
    - null
    - null
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
    - 0.0
    - null
    - null
    - null
    - 0.02
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Cheby
    model_plain: Cheby
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.11025'
    title: Backdoor Graph Condensation
    date: Jul 2024
    date_iso: 2024-07
    date_display: Jul 2024
    codebase_url: https://github.com/JiahaoWuGit/BGC
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 98.54
    - null
    - null
    - null
    - 72.78
    - null
    - null
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
    - 1.71
    - null
    - null
    - null
    - 1.21
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.476
    - null
    - null
    - null
    - null
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
    - 0.039
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5
    - null
    - null
    - null
    - null
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
    - 0.045
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ROLAND-GCN
    model_plain: ROLAND-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.455
    - null
    - null
    - null
    - null
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
    - 0.09
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ROLAND-GAT
    model_plain: ROLAND-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.468
    - null
    - null
    - null
    - null
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
    - 0.08
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TREND
    model_plain: TREND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.623
    - null
    - null
    - null
    - null
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
    - 0.067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DDGCL
    model_plain: DDGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.52
    - null
    - null
    - null
    - null
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
    - 0.064
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPDG
    model_plain: CPDG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.587
    - null
    - null
    - null
    - null
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
    - 0.047
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.575
    - null
    - null
    - null
    - null
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
    - 0.043
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProG
    model_plain: ProG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.658
    - null
    - null
    - null
    - null
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
    - 0.034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.66
    - null
    - null
    - null
    - null
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
    - 0.066
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SAMGPT
    model_plain: SAMGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.742
    - null
    - null
    - null
    - null
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
    - 0.022
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TIGPrompt
    model_plain: TIGPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.652
    - null
    - null
    - null
    - null
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
    - 0.059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGPrompt
    model_plain: DAGPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.13540'
    title: Decoupled and Divergence-Conditioned Prompt for Multi-domain Dynamic Graph
      Foundation Models
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/RingBDStack/DyGFM
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7
    - null
    - null
    - null
    - null
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
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9236
    - 0.9778
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.004
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9252
    - 0.9791
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.001
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9375
    - 0.9848
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.002
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9306
    - 0.9824
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT* + TGSL
    model_plain: TGAT* + TGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9431
    - 0.9867
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.001
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9027
    - 0.9669
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.002
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer + TGSL
    model_plain: GraphMixer + TGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.07699'
    title: Time-aware Graph Structure Learning via Sequence Prediction on Temporal
      Graphs
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/ViktorAxelsen/TGSL
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9068
    - 0.9697
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ROLAND-GCN
    model_plain: ROLAND-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4825
    - null
    - null
    - null
    - null
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
    - 0.0957
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ROLAND-GAT
    model_plain: ROLAND-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4795
    - null
    - null
    - null
    - null
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
    - 0.0842
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5364
    - null
    - null
    - null
    - null
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
    - 0.055
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4954
    - null
    - null
    - null
    - null
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
    - 0.0623
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TREND
    model_plain: TREND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6485
    - null
    - null
    - null
    - null
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
    - 0.0471
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6021
    - null
    - null
    - null
    - null
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
    - 0.0536
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DDGCL
    model_plain: DDGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5521
    - null
    - null
    - null
    - null
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
    - 0.0619
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CPDG
    model_plain: CPDG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6592
    - null
    - null
    - null
    - null
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
    - 0.0625
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6089
    - null
    - null
    - null
    - null
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
    - 0.0637
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ProG
    model_plain: ProG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.686
    - null
    - null
    - null
    - null
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
    - 0.0564
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT-TIGPrompt
    model_plain: TGAT-TIGPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6375
    - null
    - null
    - null
    - null
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
    - 0.056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT-DyGPrompt
    model_plain: TGAT-DyGPrompt
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.74
    - null
    - null
    - null
    - null
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
    - 0.031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep-DyGPrompt
    model_plain: DyRep-DyGPrompt
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5098
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE-DyGPrompt
    model_plain: JODIE-DyGPrompt
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6093
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Variant 1
    model_plain: Variant 1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7259
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DAGPrompt
    model_plain: DAGPrompt
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13937'
    title: Node-Time Conditional Prompt Learning in Dynamic Graphs
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.735
    - null
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9924
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.998
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9966
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.993
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: APAN
    model_plain: APAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9924
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DySAT
    model_plain: DySAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9852
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAWs-attn
    model_plain: CAWs-attn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9851
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAWs-mean
    model_plain: CAWs-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9843
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGSRec
    model_plain: TGSRec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.11636'
    title: Do We Really Need Complicated Model Architectures For Temporal Networks?
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/CongWeilin/GraphMixer
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9521
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAW-N-mean
    model_plain: CAW-N-mean
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9996
    - null
    - 0.9767
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAW-N-attn
    model_plain: CAW-N-attn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9999
    - null
    - 0.9771
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0008
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DynAERNN
    model_plain: DynAERNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.8558
    - null
    - 0.5751
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0212
    - null
    - 0.0254
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9114
    - null
    - 0.7249
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0038
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.6754
    - null
    - 0.6237
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0202
    - null
    - 0.0149
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: VGRNN
    model_plain: VGRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5087
    - null
    - 0.6193
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0081
    - null
    - 0.0072
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EvolveGCN-H
    model_plain: EvolveGCN-H
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.5449
    - null
    - 0.6331
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0073
    - null
    - 0.0053
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.05974'
    title: Inductive Representation Learning in Temporal Networks via Causal Anonymous
      Walks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/twitter-research/tgn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9838
    - null
    - 0.9496
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: HopeDGN
    model_plain: HopeDGN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9931
    - null
    - 0.9927
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyGFormer
    model_plain: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9922
    - null
    - 0.9915
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CAWN
    model_plain: CAWN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9911
    - null
    - 0.9902
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: PINT
    model_plain: PINT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9903
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9862
    - null
    - 0.9859
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0002
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9818
    - null
    - 0.9813
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0003
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9824
    - null
    - 0.982
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0005
    - null
    - 0.0005
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyRep
    model_plain: DyRep
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9807
    - null
    - 0.9802
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0013
    - null
    - 0.0015
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9689
    - null
    - 0.9677
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0
    - null
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TCL
    model_plain: TCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.01367'
    title: Towards Dynamic Graph Neural Networks with Provably High-Order Expressive
      Power
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.9697
    - null
    - 0.9688
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    - 0.0001
    - null
    - 0.0002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyGC
    model_plain: DyGC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.399
    - 0.399
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.01
    - 0.012
    - null
  - model: Random
    model_plain: Random
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.302
    - 0.327
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.01
    - 0.013
    - null
  - model: Herding
    model_plain: Herding
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.371
    - 0.371
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.013
    - 0.007
    - null
  - model: K-Center
    model_plain: K-Center
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.345
    - 0.369
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.008
    - 0.012
    - null
  - model: GCOND
    model_plain: GCOND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.177
    - 0.271
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.036
    - 0.017
    - null
  - model: GCDM
    model_plain: GCDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.235
    - 0.296
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.043
    - 0.022
    - null
  - model: SimGC
    model_plain: SimGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.274
    - 0.303
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.017
    - 0.012
    - null
  - model: CGC
    model_plain: CGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13099'
    title: Dynamic Graph Condensation
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.229
    - 0.284
    - null
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.033
    - 0.023
    - null
  - model: PDGNNs
    model_plain: PDGNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.13200'
    title: Topology-aware Embedding Memory for Continual Learning on Expanding Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.947
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.004
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SSM
    model_plain: SSM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.13200'
    title: Topology-aware Embedding Memory for Continual Learning on Expanding Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.944
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.0
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SEM-curvature
    model_plain: SEM-curvature
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.13200'
    title: Topology-aware Embedding Memory for Continual Learning on Expanding Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.963
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Joint
    model_plain: Joint
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.13200'
    title: Topology-aware Embedding Memory for Continual Learning on Expanding Networks
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.993
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - 0.002
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5863
    - 50.49
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
    - null
    - null
    - null
    - null
    - null
    - 0.0154
    - 1.14
    - null
    - null
    - null
  - model: CTDNE
    model_plain: CTDNE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5855
    - 51.3
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
    - null
    - null
    - null
    - null
    - null
    - 0.0108
    - 1.37
    - null
    - null
    - null
  - model: DynGEM
    model_plain: DynGEM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.4537
    - 52.43
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
    - null
    - null
    - null
    - null
    - null
    - 0.009
    - 1.75
    - null
    - null
    - null
  - model: DySAT
    model_plain: DySAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5615
    - 55.79
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
    - null
    - null
    - null
    - null
    - null
    - 0.0114
    - 1.78
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.5911
    - 56.13
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
    - null
    - null
    - null
    - null
    - null
    - 0.0194
    - 1.78
    - null
    - null
    - null
  - model: DeepCoevolve
    model_plain: DeepCoevolve
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6206
    - 49.7
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
    - null
    - null
    - null
    - null
    - null
    - 0.0102
    - 1.53
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6433
    - 45.11
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
    - null
    - null
    - null
    - null
    - null
    - 0.0266
    - 2.19
    - null
    - null
    - null
  - model: TGNs
    model_plain: TGNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.6161
    - 56.34
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
    - null
    - null
    - null
    - null
    - null
    - 0.0273
    - 2.04
    - null
    - null
    - null
  - model: TDIG-MPNN
    model_plain: TDIG-MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7146
    - 46.91
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
    - null
    - null
    - null
    - null
    - null
    - 0.0008
    - 0.49
    - null
    - null
    - null
  - model: The graph neural networks
    model_plain: The graph neural networks
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07944'
    title: 'TCL: Transformer-based Dynamic Graph Modelling via Contrastive Learning'
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.7595
    - 33.95
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
    - null
    - null
    - null
    - null
    - null
    - 0.0047
    - 1.27
    - null
    - null
    - null
  - model: DistGNN (cd-0)
    model_plain: DistGNN (cd-0)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2104.06700'
    title: 'DistGNN: Scalable Distributed Training for Large-Scale Graph Neural Networks'
    date: Apr 2021
    date_iso: 2021-04
    date_display: Apr 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.934
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE
    model_plain: JODIE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5522
    - null
    - null
    - null
    - null
    - null
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
    - 0.0103
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DySAT
    model_plain: DySAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.569
    - null
    - null
    - null
    - null
    - null
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
    - 0.0234
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT
    model_plain: TGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.61
    - null
    - null
    - null
    - null
    - null
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
    - 0.0088
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN
    model_plain: TGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5926
    - null
    - null
    - null
    - null
    - null
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
    - 0.0041
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer
    model_plain: GraphMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6298
    - null
    - null
    - null
    - null
    - null
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
    - 0.0147
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyGFormer
    model_plain: DyGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6371
    - null
    - null
    - null
    - null
    - null
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
    - 0.0067
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JODIE+RF
    model_plain: JODIE+RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.4872
    - null
    - null
    - null
    - null
    - null
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
    - 0.0056
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DySAT+RF
    model_plain: DySAT+RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5347
    - null
    - null
    - null
    - null
    - null
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
    - 0.0151
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGAT+RF
    model_plain: TGAT+RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5613
    - null
    - null
    - null
    - null
    - null
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
    - 0.0407
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: TGN+RF
    model_plain: TGN+RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5385
    - null
    - null
    - null
    - null
    - null
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
    - 0.0212
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphMixer+RF
    model_plain: GraphMixer+RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.5139
    - null
    - null
    - null
    - null
    - null
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
    - 0.0251
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DyGFormer+RF
    model_plain: DyGFormer+RF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.6406
    - null
    - null
    - null
    - null
    - null
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
    - 0.0034
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SPLASH
    model_plain: SPLASH
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.00328'
    title: Simple yet Effective Node Property Prediction on Edge Streams under Distribution
      Shifts
    date: Apr 2025
    date_iso: 2025-04
    date_display: Apr 2025
    codebase_url: https://github.com/jhsk777/SPLASH
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.7358
    - null
    - null
    - null
    - null
    - null
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
    - 0.0028
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Graphlet
    model_plain: Graphlet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.502
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: sp
    model_plain: sp
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.577
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.576
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: InfoGraph
    model_plain: InfoGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.508
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.519
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CuCo
    model_plain: CuCo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.51
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.52
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: RGCL
    model_plain: RGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.509
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: SimGRACE
    model_plain: SimGRACE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.513
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GLCC
    model_plain: GLCC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.11879'
    title: 'GLCC: A General Framework for Graph-Level Clustering'
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - 0.676
    - null
    - null
    - null
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
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  milestones:
  - value: 0.719
    std: null
    model: CLN-HWN-full
    arxiv_id: '1609.04508'
    title: Column Networks for Collective Classification
    date: 2016-09
  - value: 0.931
    std: 0.001
    model: GraphGPS
    arxiv_id: '1710.10321'
    title: arXiv:1710.10321
    date: 2017-10
  - value: 0.9636
    std: 0.0003
    model: GaAN
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: 2018-03
  - value: 0.964
    std: null
    model: GaAN
    arxiv_id: '1902.07153'
    title: Simplifying Graph Convolutional Networks
    date: '2019-02-19'
  - value: 0.966
    std: null
    model: Cluster-GCN
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: 2019-05
  - value: 0.968
    std: null
    model: SIGN
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: 2020-04
---

