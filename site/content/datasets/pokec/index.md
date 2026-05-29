---
title: Pokec
slug: pokec
benchmark: LINKX Benchmarks
task_type: node_classification
description: Slovak social network Pokec node classification (binary gender, 1.6M
  nodes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.LINKXDataset.html
stats:
  num_graphs: 1
  avg_nodes: 662143.0
  avg_edges: 13806079.0
  num_classes: 2
result_count: 36
best_model:
  model: GloGNN
  value: 1.0
  metric: Accuracy
  arxiv_id: '2205.07308'
  paper_title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
variants:
- slug: standard-split
  name: Standard split
  notes: ''
  is_standard: true
  primary_metric: Accuracy
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - Accuracy
  - ACC
  rows:
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 1.0
    - null
    metric_stds:
    - null
    - null
  - model: MLP for adjacency matrix only
    model_plain: MLP for adjacency matrix only
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: May 15, 2022
    date_iso: '2022-05-15'
    date_display: May 2022
    codebase_url: ''
    uses_external_data: null
    is_best: true
    metric_values:
    - 1.0
    - null
    metric_stds:
    - null
    - null
  - model: GTs
    model_plain: GTs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7911
    - null
    metric_stds:
    - 0.0006
    - null
  - model: Polynormer
    model_plain: Polynormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7727
    - null
    metric_stds:
    - 0.0023
    - null
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7376
    - null
    metric_stds:
    - 0.0024
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: Feb 8, 2022
    date_iso: '2022-02-08'
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7309
    - null
    metric_stds:
    - 0.0028
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: Feb 8, 2022
    date_iso: '2022-02-08'
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7248
    - null
    metric_stds:
    - 0.0026
    - null
  - model: FMP
    model_plain: FMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: Feb 8, 2022
    date_iso: '2022-02-08'
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7216
    - null
    metric_stds:
    - 0.0033
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: Feb 8, 2022
    date_iso: '2022-02-08'
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7146
    - null
    metric_stds:
    - 0.0041
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: Feb 8, 2022
    date_iso: '2022-02-08'
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    - null
    metric_stds:
    - 0.0048
    - null
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7032
    - null
    metric_stds:
    - 0.0045
    - null
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: Feb 8, 2022
    date_iso: '2022-02-08'
    date_display: Feb 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.698
    - null
    metric_stds:
    - 0.0089
    - null
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6924
    - null
    metric_stds:
    - 0.0076
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.14863'
    title: 'Exploring the Global-to-Local Attention Scheme in Graph Transformers:
      An Empirical Study'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6847
    - null
    metric_stds:
    - 0.0142
    - null
  - model: SIGN
    model_plain: SIGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6801
    - null
    metric_stds:
    - 0.0025
    - null
  - model: GCN-NSampler
    model_plain: GCN-NSampler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6375
    - null
    metric_stds:
    - 0.0077
    - null
  - model: GAT-NSampler
    model_plain: GAT-NSampler
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6232
    - null
    metric_stds:
    - 0.0065
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6231
    - null
    metric_stds:
    - 0.0113
    - null
  - model: NIFTY
    model_plain: NIFTY
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14383'
    title: Interpreting Unfairness in Graph Neural Networks via Training Node Attribution
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yushundong/BIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.611
    - null
    metric_stds:
    - 0.003
    - null
  - model: FairGNN
    model_plain: FairGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14383'
    title: Interpreting Unfairness in Graph Neural Networks via Training Node Attribution
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yushundong/BIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.603
    - null
    metric_stds:
    - 0.005
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6015
    - null
    metric_stds:
    - 0.0003
    - null
  - model: BIND 1%
    model_plain: BIND 1%
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14383'
    title: Interpreting Unfairness in Graph Neural Networks via Training Node Attribution
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yushundong/BIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.588
    - null
    metric_stds:
    - 0.018
    - null
  - model: GCN-VN
    model_plain: GCN-VN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14383'
    title: Interpreting Unfairness in Graph Neural Networks via Training Node Attribution
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yushundong/BIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.585
    - null
    metric_stds:
    - 0.008
    - null
  - model: EDITS
    model_plain: EDITS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.14383'
    title: Interpreting Unfairness in Graph Neural Networks via Training Node Attribution
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: https://github.com/yushundong/BIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.568
    - null
    metric_stds:
    - 0.009
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/qitianwu/SGFormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5203
    - null
    metric_stds:
    - 0.0084
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6841
    metric_stds:
    - null
    - 0.003
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6541
    metric_stds:
    - null
    - 0.0074
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6581
    metric_stds:
    - null
    - 0.0043
  - model: FairGNN
    model_plain: FairGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.682
    metric_stds:
    - null
    - 0.0087
  - model: EDITS
    model_plain: EDITS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6682
    metric_stds:
    - null
    - 0.0098
  - model: FairDrop
    model_plain: FairDrop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6745
    metric_stds:
    - null
    - 0.008
  - model: NIFTY
    model_plain: NIFTY
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6691
    metric_stds:
    - null
    - 0.0138
  - model: FMP
    model_plain: FMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6762
    metric_stds:
    - null
    - 0.0127
  - model: BeMap (row)
    model_plain: BeMap (row)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6839
    metric_stds:
    - null
    - 0.0052
  - model: BeMap (sym)
    model_plain: BeMap (sym)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6912
    metric_stds:
    - null
    - 0.0076
  - model: BeMap (gat)
    model_plain: BeMap (gat)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04107'
    title: 'BeMap: Balanced Message Passing for Fair Graph Neural Network'
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: https://github.com/xiaolin-cs/BeMap
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.6547
    metric_stds:
    - null
    - 0.0097
  milestones:
  - value: 0.7309
    std: 0.0028
    model: GCN
    arxiv_id: '2202.04187'
    title: 'FMP: Toward Fair Graph Message Passing against Topology Bias'
    date: '2022-02-08'
  - value: 1.0
    std: null
    model: GloGNN
    arxiv_id: '2205.07308'
    title: Finding Global Homophily in Graph Neural Networks When Meeting Heterophily
    date: '2022-05-15'
---

