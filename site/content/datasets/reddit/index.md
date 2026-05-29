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
result_count: 38
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
  - AUC
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
    metric_stds:
    - 0.0
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
    metric_stds:
    - 0.001
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
    metric_stds:
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
    metric_stds:
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
    metric_stds:
    - 0.001
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
    metric_stds:
    - 0.0003
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
    metric_stds:
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
    metric_stds:
    - 0.0007
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
    metric_stds:
    - 0.0008
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
    metric_stds:
    - 0.001
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
    metric_stds:
    - 0.0003
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
    metric_stds:
    - 0.0007
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
    metric_stds:
    - 0.0003
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
    metric_stds:
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
    metric_stds:
    - 0.001
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
    metric_stds:
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
    metric_stds:
    - 0.001
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
    metric_stds:
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
    metric_stds:
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
    metric_stds:
    - 0.0
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
    metric_stds:
    - 0.001
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
    metric_stds:
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
    metric_stds:
    - 0.001
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
    metric_stds:
    - 0.001
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
    metric_stds:
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
    metric_stds:
    - 0.001
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
    metric_stds:
    - 0.001
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
    metric_stds:
    - 0.002
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
    metric_stds:
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
    metric_stds:
    - 0.0
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
    metric_stds:
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
    metric_stds:
    - 0.001
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
    metric_stds:
    - 0.0009
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
    - 0.9751
    metric_stds:
    - null
    - 0.001
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
    - 0.9634
    metric_stds:
    - null
    - 0.0083
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
    - 0.9818
    metric_stds:
    - null
    - 0.0005
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
    - 0.9823
    metric_stds:
    - null
    - 0.001
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
    - 0.9861
    metric_stds:
    - null
    - 0.0004
  milestones:
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

