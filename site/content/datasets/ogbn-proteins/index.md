---
title: ogbn-proteins
slug: ogbn-proteins
benchmark: OGB
task_type: node_classification
description: Multi-label binary node classification on protein association network
  (112 tasks).
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBNodePropPredDataset.html
stats:
  num_graphs: 132534
  avg_nodes: 39561252.0
  avg_edges: null
  num_classes: 112
result_count: 21
best_model:
  model: RevGNN-Wide
  value: 0.8824
  metric: ROC-AUC
  arxiv_id: '2106.07476'
  paper_title: Training Graph Neural Networks with 1000 Layers
variants:
- slug: standard-split
  name: Standard split
  notes: 'Species-based split. Metric: ROC-AUC.'
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
  - model: RevGNN-Wide
    model_plain: RevGNN-Wide
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_iso: '2021-06-14'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8824
    metric_stds:
    - 0.0015
  - model: RevGNN-Deep
    model_plain: RevGNN-Deep
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_iso: '2021-06-14'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8774
    metric_stds:
    - 0.0013
  - model: UniMP+CEF
    model_plain: UniMP+CEF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 1.96
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_iso: '2021-06-14'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8691
    metric_stds:
    - 0.0018
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.48
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_iso: '2021-06-14'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8682
    metric_stds:
    - 0.0021
  - model: UniMP
    model_plain: UniMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.475605
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8642
    metric_stds:
    - 0.0008
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.37
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: Jun 14, 2021
    date_iso: '2021-06-14'
    date_display: Jun 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8616
    metric_stds:
    - 0.0016
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.253743
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.858
    metric_stds:
    - 0.0017
  - model: MWE-DGCN
    model_plain: MWE-DGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.538544
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8436
    metric_stds:
    - 0.0065
  - model: ILSS
    model_plain: ILSS
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
    - 0.841
    metric_stds:
    - 0.002
  - model: Graphormer
    model_plain: Graphormer
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
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.835
    metric_stds:
    - 0.001
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
    - 0.832
    metric_stds:
    - 0.002
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
    - 0.824
    metric_stds:
    - 0.003
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
    - 0.821
    metric_stds:
    - 0.002
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
    - 0.818
    metric_stds:
    - 0.004
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
    - 0.815
    metric_stds:
    - 0.003
  - model: GeniePath-BS
    model_plain: GeniePath-BS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.316754
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7825
    metric_stds:
    - 0.0035
  - model: GaAN
    model_plain: GaAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_iso: 2020-09
    date_display: Sep 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7803
    metric_stds:
    - 0.0073
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7768
    metric_stds:
    - 0.002
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7251
    metric_stds:
    - 0.0035
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7204
    metric_stds:
    - 0.0048
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: May 2020
    date_iso: 2020-05
    date_display: May 2020
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6881
    metric_stds:
    - 0.0065
  milestones:
  - value: 0.7768
    std: 0.002
    model: GraphSAGE
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: 2020-05
  - value: 0.8642
    std: 0.0008
    model: UniMP
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: 2020-09
  - value: 0.8824
    std: 0.0015
    model: RevGNN-Wide
    arxiv_id: '2106.07476'
    title: Training Graph Neural Networks with 1000 Layers
    date: '2021-06-14'
---

