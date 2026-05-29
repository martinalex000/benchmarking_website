---
title: ogbl-citation2
slug: ogbl-citation2
benchmark: OGB
task_type: link_prediction
description: Citation link prediction on arXiv/PubMed papers (directed).
primary_metric: MRR
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.OGBLinkPropPredDataset.html
stats:
  num_graphs: 2927963
  avg_nodes: 30561187.0
  avg_edges: null
  num_classes: null
result_count: 19
best_model:
  model: GCN
  value: 0.8474
  metric: MRR
  arxiv_id: '2005.00687'
  paper_title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
variants:
- slug: standard-split
  name: Standard split
  notes: 'Time-based split. Metric: MRR.'
  is_standard: true
  primary_metric: MRR
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MRR
  - Hits@100
  rows:
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
    is_best: true
    metric_values:
    - 0.8474
    - 0.1867
    metric_stds:
    - 0.0021
    - 0.0132
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
    - 0.826
    - 0.1655
    metric_stds:
    - 0.0036
    - 0.024
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
    - 0.812
    - null
    metric_stds:
    - 0.001
    - null
  - model: OpenGNN
    model_plain: OpenGNN
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
    - 0.805
    - null
    metric_stds:
    - 0.001
    - null
  - model: Neighbor Sampling (NS)
    model_plain: Neighbor Sampling (NS)
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
    - 0.8044
    - null
    metric_stds:
    - 0.001
    - null
  - model: GraphGPS
    model_plain: GraphGPS
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
    - 0.801
    - null
    metric_stds:
    - 0.002
    - null
  - model: Cluster-GCN
    model_plain: Cluster-GCN
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
    - 0.8004
    - null
    metric_stds:
    - 0.0025
    - null
  - model: GraphSAINT
    model_plain: GraphSAINT
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
    - 0.7985
    - null
    metric_stds:
    - 0.004
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.795
    - null
    metric_stds:
    - 0.002
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
    - 0.792
    - null
    metric_stds:
    - 0.003
    - null
  - model: GINE
    model_plain: GINE
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
    - 0.788
    - null
    metric_stds:
    - 0.002
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
    - 0.785
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
    - 0.772
    - null
    metric_stds:
    - 0.004
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
    - 0.77
    - null
    metric_stds:
    - 0.003
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
    - 0.768
    - null
    metric_stds:
    - 0.002
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
    - 0.765
    - null
    metric_stds:
    - 0.003
    - null
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
    - 0.6141
    - 0.2226
    metric_stds:
    - 0.0011
    - 0.0083
  - model: MatrixFactorization
    model_plain: MatrixFactorization
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
    - 0.5186
    - 0.3229
    metric_stds:
    - 0.0443
    - 0.0094
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
    - 0.2895
    - 0.46
    metric_stds:
    - 0.0014
    - 0.0
  milestones:
  - value: 0.8474
    std: 0.0021
    model: GCN
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: 2020-05
---

