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
result_count: 42
best_model:
  model: ExpC-s
  value: 0.3318
  metric: F1
  arxiv_id: '2012.07219'
  paper_title: Breaking the Expressive Bottlenecks of Graph Neural Networks
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
  - Hits@10
  rows:
  - model: ExpC-s
    model_plain: ExpC-s
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.3318
    - null
    metric_stds:
    - 0.0017
    - null
  - model: CombC
    model_plain: CombC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3276
    - null
    metric_stds:
    - 0.0015
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3163
    - null
    metric_stds:
    - 0.0018
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3163
    - null
    metric_stds:
    - 0.002
    - null
  - model: multi-head GAT
    model_plain: multi-head GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: Dec 2020
    date_iso: 2020-12
    date_display: Dec 2020
    codebase_url: https://github.com/qslim/epcb-gnns
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.311
    - null
    metric_stds:
    - null
    - null
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2911
    - null
    metric_stds:
    - 0.0044
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2737
    - null
    metric_stds:
    - 0.0016
    - null
  - model: TargetInGraph
    model_plain: TargetInGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2708
    - null
    metric_stds:
    - 0.0
    - null
  - model: SD-VAE
    model_plain: SD-VAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2708
    - null
    metric_stds:
    - 0.0039
    - null
  - model: ASAP
    model_plain: ASAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2506
    - null
    metric_stds:
    - 0.0037
    - null
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2445
    - null
    metric_stds:
    - 0.0077
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2444
    - null
    metric_stds:
    - 0.0025
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2439
    - null
    metric_stds:
    - 0.004
    - null
  - model: GG-NN
    model_plain: GG-NN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2315
    - null
    metric_stds:
    - 0.0049
    - null
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
    is_best: false
    metric_values:
    - 0.2222
    - null
    metric_stds:
    - 0.001
    - null
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
    - null
    metric_stds:
    - 0.002
    - null
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
    - null
    metric_stds:
    - 0.0012
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2149
    - null
    metric_stds:
    - 0.0061
    - null
  - model: GIN-VN
    model_plain: GIN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.211
    - null
    metric_stds:
    - 0.0061
    - null
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
    - null
    metric_stds:
    - 0.0007
    - null
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
    - null
    metric_stds:
    - 0.0024
    - null
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
    - null
    metric_stds:
    - 0.0033
    - null
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
    - null
    metric_stds:
    - 0.0049
    - null
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
    - null
    metric_stds:
    - 0.0015
    - null
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
    - null
    metric_stds:
    - 0.0015
    - null
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
    - null
    metric_stds:
    - 0.0018
    - null
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
    - null
    metric_stds:
    - 0.0026
    - null
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
    - null
    metric_stds:
    - 0.0032
    - null
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
    - null
    metric_stds:
    - 0.0018
    - null
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
    - null
    metric_stds:
    - 0.0015
    - null
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
    - null
    metric_stds:
    - 0.0023
    - null
  - model: Node2Token
    model_plain: Node2Token
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2101.07965'
    title: Directed Acyclic Graph Neural Networks
    date: Jan 2021
    date_iso: 2021-01
    date_display: Jan 2021
    codebase_url: https://github.com/vthost/DAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1304
    - null
    metric_stds:
    - 0.0
    - null
  - model: TransE
    model_plain: TransE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.317
    metric_stds:
    - null
    - null
  - model: ComplEx
    model_plain: ComplEx
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.4
    metric_stds:
    - null
    - null
  - model: ConvE
    model_plain: ConvE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.42
    metric_stds:
    - null
    - null
  - model: TuckER
    model_plain: TuckER
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.43
    metric_stds:
    - null
    - null
  - model: DistMult
    model_plain: DistMult
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.427
    metric_stds:
    - null
    - null
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.142
    metric_stds:
    - null
    - null
  - model: SACN
    model_plain: SACN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.443
    metric_stds:
    - null
    - null
  - model: CompGCN
    model_plain: CompGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.428
    metric_stds:
    - null
    - null
  - model: SimRGCN
    model_plain: SimRGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.432
    metric_stds:
    - null
    - null
  - model: SimQGNN
    model_plain: SimQGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2008.05089'
    title: Quaternion Graph Neural Networks
    date: Aug 2020
    date_iso: 2020-08
    date_display: Aug 2020
    codebase_url: https://github.com/daiquocnguyen/QGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.437
    metric_stds:
    - null
    - null
  milestones:
  - value: 0.1581
    std: 0.0026
    model: GCN+virtual node
    arxiv_id: '2005.00687'
    title: 'Open Graph Benchmark: Datasets for Machine Learning on Graphs'
    date: 2020-05
  - value: 0.3318
    std: 0.0017
    model: ExpC-s
    arxiv_id: '2012.07219'
    title: Breaking the Expressive Bottlenecks of Graph Neural Networks
    date: 2020-12
---

