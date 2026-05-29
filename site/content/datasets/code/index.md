---
title: Code
slug: code
benchmark: OGB
task_type: graph_classification
description: Code AST-level method name prediction (ogbg-code2). 143k Python snippets.
primary_metric: F1
higher_is_better: true
pyg_url: https://ogb.stanford.edu/docs/leader_graphprop/#ogbg-code2
stats:
  num_graphs: 452741
  avg_nodes: 125.2
  avg_edges: 124.2
  num_classes: 1
result_count: 15
best_model:
  model: AST (Data-flow, Magnetic Lap., w/ GNN)
  value: 0.2222
  metric: F1
  arxiv_id: '2302.00049'
  paper_title: Transformers Meet Directed Graphs
variants:
- slug: standard-split
  name: Standard split
  notes: Project-based split.
  is_standard: true
  primary_metric: F1
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - F1
  rows:
  - model: AST (Data-flow, Magnetic Lap., w/ GNN)
    model_plain: AST (Data-flow, Magnetic Lap., w/ GNN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.00049'
    title: Transformers Meet Directed Graphs
    date: Jan 31, 2023
    date_iso: '2023-01-31'
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.2222
    metric_stds:
    - 0.001
  - model: AST (Data-flow, Random walk, w/ GNN)
    model_plain: AST (Data-flow, Random walk, w/ GNN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.00049'
    title: Transformers Meet Directed Graphs
    date: Jan 31, 2023
    date_iso: '2023-01-31'
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2182
    metric_stds:
    - 0.002
  - model: AST (Data-flow, w/ GNN)
    model_plain: AST (Data-flow, w/ GNN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.00049'
    title: Transformers Meet Directed Graphs
    date: Jan 31, 2023
    date_iso: '2023-01-31'
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2161
    metric_stds:
    - 0.0012
  - model: Sequence-only AST (w/ GNN)
    model_plain: Sequence-only AST (w/ GNN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.00049'
    title: Transformers Meet Directed Graphs
    date: Jan 31, 2023
    date_iso: '2023-01-31'
    date_display: Jan 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2103
    metric_stds:
    - 0.0007
  - model: GraphTrans (GIN-Virtual)
    model_plain: GraphTrans (GIN-Virtual)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.183
    metric_stds:
    - 0.0024
  - model: GraphTrans (PNA)
    model_plain: GraphTrans (PNA)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1765
    metric_stds:
    - 0.0033
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1751
    metric_stds:
    - 0.0049
  - model: GraphTrans (GIN)
    model_plain: GraphTrans (GIN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1751
    metric_stds:
    - 0.0015
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.167
    metric_stds:
    - 0.0015
  - model: GCN-virtual
    model_plain: GCN-virtual
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1595
    metric_stds:
    - 0.0018
  - model: GCN+virtual node
    model_plain: GCN+virtual node
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
    - 0.1581
    metric_stds:
    - 0.0026
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: https://github.com/ucbrise/graphtrans
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.157
    metric_stds:
    - 0.0032
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
    - 0.1507
    metric_stds:
    - 0.0018
  - model: GIN + EGP
    model_plain: GIN + EGP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.02997'
    title: Expander Graph Propagation
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1497
    metric_stds:
    - 0.0015
  - model: GIN
    model_plain: GIN
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
    - 0.1495
    metric_stds:
    - 0.0023
  milestones:
  - value: 0.1581
    std: 0.0026
    model: GCN+virtual node
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: 2020-05
  - value: 0.183
    std: 0.0024
    model: GraphTrans (GIN-Virtual)
    arxiv_id: '2201.08821'
    title: Representing Long-Range Context for Graph Neural Networks with Global Attention
    date: 2022-01
  - value: 0.2222
    std: 0.001
    model: AST (Data-flow, Magnetic Lap., w/ GNN)
    arxiv_id: '2302.00049'
    title: Transformers Meet Directed Graphs
    date: '2023-01-31'
---

