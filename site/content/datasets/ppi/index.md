---
title: PPI
slug: ppi
benchmark: Classic
task_type: node_classification
description: Protein-protein interaction node classification (121 GO labels, multi-label).
primary_metric: F1
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.PPI.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 121
result_count: 31
best_model:
  model: GaAN
  value: 0.9871
  metric: F1
  arxiv_id: '1803.07294'
  paper_title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
    Graphs'
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
  - ROC-AUC
  rows:
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
    is_best: true
    metric_values:
    - 0.9871
    - null
    metric_stds:
    - 0.0002
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
    - 0.9846
    - null
    metric_stds:
    - 0.0009
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
    - 0.9839
    - null
    metric_stds:
    - 0.0005
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
    - 0.9839
    - null
    metric_stds:
    - 0.0005
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
    - 0.9832
    - null
    metric_stds:
    - 0.0018
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
    - 0.981
    - null
    metric_stds:
    - 0.004
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.973
    - null
    metric_stds:
    - 0.002
    - null
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
    is_best: false
    metric_values:
    - 0.97
    - null
    metric_stds:
    - 0.003
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
    - 0.9685
    - null
    metric_stds:
    - 0.0019
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
    - 0.963
    - null
    metric_stds:
    - 0.01
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
    - 0.942
    - null
    metric_stds:
    - 0.001
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
    - 0.935
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
    - 0.933
    - null
    metric_stds:
    - 0.002
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
    - 0.931
    - null
    metric_stds:
    - 0.003
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
    - 0.929
    - null
    metric_stds:
    - 0.002
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
    - 0.928
    - null
    metric_stds:
    - 0.001
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.926
    - null
    metric_stds:
    - 0.002
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
    - 0.892
    - null
    metric_stds:
    - 0.015
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
    - 0.875
    - null
    metric_stds:
    - 0.004
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
    - 0.687
    - null
    metric_stds:
    - 0.012
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
    - 0.637
    - null
    metric_stds:
    - 0.006
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
    - 0.612
    - null
    metric_stds:
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
    - 0.5407
    - null
    metric_stds:
    - 0.0006
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
    - 0.515
    - null
    metric_stds:
    - 0.006
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
    - 0.513
    - null
    metric_stds:
    - 0.032
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.769
    metric_stds:
    - null
    - 0.002
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.803
    metric_stds:
    - null
    - 0.005
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.783
    metric_stds:
    - null
    - 0.004
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.782
    metric_stds:
    - null
    - 0.01
  - model: P-GNN-F-1L
    model_plain: P-GNN-F-1L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.775
    metric_stds:
    - null
    - 0.029
  - model: P-GNN-E-2L
    model_plain: P-GNN-E-2L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1906.04817'
    title: Position-aware Graph Neural Networks
    date: Jun 11, 2019
    date_iso: '2019-06-11'
    date_display: Jun 2019
    codebase_url: https://github.com/JiaxuanYou/P-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.808
    metric_stds:
    - null
    - 0.003
  milestones:
  - value: 0.9871
    std: 0.0002
    model: GaAN
    arxiv_id: '1803.07294'
    title: 'GaAN: Gated Attention Networks for Learning on Large and Spatiotemporal
      Graphs'
    date: 2018-03
---

