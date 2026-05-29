---
title: ZINC
slug: zinc
benchmark: Classic
task_type: graph_regression
description: Molecular property regression (constrained solubility).
primary_metric: MAE
higher_is_better: false
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.ZINC.html
stats: null
result_count: 44
best_model:
  model: GatedGCN
  value: 0.004
  metric: MAE
  arxiv_id: '2306.03589'
  paper_title: How does over-squashing affect the power of GNNs?
variants:
- slug: full
  name: Full
  notes: 250,000 train molecules.
  is_standard: true
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  - Accuracy
  rows:
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.004
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
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.006
    - null
    metric_stds:
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.014
    - null
    metric_stds:
    - null
    - null
  - model: PPGN++(6)
    model_plain: PPGN++(6)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.02
    - null
    metric_stds:
    - 0.001
    - null
  - model: GPM
    model_plain: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.021
    - null
    metric_stds:
    - 0.002
    - null
  - model: GNN-SSWL
    model_plain: GNN-SSWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.274
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.022
    - null
    metric_stds:
    - 0.001
    - null
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.023
    - null
    metric_stds:
    - 0.001
    - null
  - model: UnionGPS
    model_plain: UnionGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0236
    - null
    metric_stds:
    - 0.0017
    - null
  - model: SUN
    model_plain: SUN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.526
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.024
    - null
    metric_stds:
    - 0.003
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 2023
    date_iso: 2023-06
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.024
    - null
    metric_stds:
    - null
    - null
  - model: Graphormer-GD
    model_plain: Graphormer-GD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.503
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.025
    - null
    metric_stds:
    - 0.004
    - null
  - model: Unionormer
    model_plain: Unionormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0252
    - null
    metric_stds:
    - 0.0026
    - null
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0262
    - null
    metric_stds:
    - 0.0025
    - null
  - model: URPE
    model_plain: URPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.028
    - null
    metric_stds:
    - 0.002
    - null
  - model: DS-GNN
    model_plain: DS-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.029
    - null
    metric_stds:
    - 0.003
    - null
  - model: NGNN
    model_plain: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.029
    - null
    metric_stds:
    - 0.001
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0309
    - null
    metric_stds:
    - 0.0031
    - null
  - model: GNN-AK
    model_plain: GNN-AK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.034
    - null
    metric_stds:
    - 0.007
    - null
  - model: Graph-ViT
    model_plain: Graph-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.035
    - null
    metric_stds:
    - 0.005
    - null
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.036
    - null
    metric_stds:
    - 0.005
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.036
    - null
    metric_stds:
    - 0.002
    - null
  - model: AgentNet
    model_plain: AgentNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.04
    - null
    metric_stds:
    - 0.006
    - null
  - model: CIN (small)
    model_plain: CIN (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.044
    - null
    metric_stds:
    - 0.003
    - null
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.489
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.052
    - null
    metric_stds:
    - 0.005
    - null
  - model: AWE
    model_plain: AWE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.059
    - null
    metric_stds:
    - 0.005
    - null
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.059
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
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.067
    - null
    metric_stds:
    - 0.009
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.51
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.088
    - null
    metric_stds:
    - 0.002
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.504
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.09
    - null
    metric_stds:
    - 0.002
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.111
    - null
    metric_stds:
    - 0.002
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.113
    - null
    metric_stds:
    - 0.002
    - null
  - model: UnionSAGE
    model_plain: UnionSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1146
    - null
    metric_stds:
    - 0.0017
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.126
    - null
    metric_stds:
    - 0.003
    - null
  - model: UnionGCN
    model_plain: UnionGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1334
    - null
    metric_stds:
    - 0.0013
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1552
    - null
    metric_stds:
    - 0.0079
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9919
    metric_stds:
    - null
    - null
  - model: LeNet5
    model_plain: LeNet5
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9933
    metric_stds:
    - null
    - null
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1611.08402'
    title: Geometric deep learning on graphs and manifolds using mixture model CNNs
    date: Nov 2016
    date_iso: 2016-11
    date_display: Nov 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9914
    metric_stds:
    - null
    - null
  - model: dir-gcn
    model_plain: dir-gcn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9344
    metric_stds:
    - null
    - 0.0059
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9337
    metric_stds:
    - null
    - 0.0022
  - model: dir-sage
    model_plain: dir-sage
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9414
    metric_stds:
    - null
    - 0.0065
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9415
    metric_stds:
    - null
    - 0.0061
  - model: dir-gat
    model_plain: dir-gat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9448
    metric_stds:
    - null
    - 0.0052
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.10498'
    title: Edge Directionality Improves Learning on Heterophilic Graphs
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/emalgorithm/directed-graph-neural-network
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9453
    metric_stds:
    - null
    - 0.0048
  milestones:
  - value: 0.025
    std: 0.004
    model: Graphormer-GD
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: 2023-01
  - value: 0.0236
    std: 0.0017
    model: UnionGPS
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: 2023-05
  - value: 0.004
    std: null
    model: GatedGCN
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: 2023-06
- slug: subset-12k
  name: Subset (12k)
  notes: 12,000 train molecules. Reported by many papers — most results in this leaderboard
    use this split.
  is_standard: false
  primary_metric: MAE
  higher_is_better: false
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - MAE
  rows:
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.059
    metric_stds:
    - 0.002
  - model: Tango_GPS
    model_plain: Tango_GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.062
    metric_stds:
    - 0.005
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.063
    metric_stds:
    - 0.001
  - model: LRDs
    model_plain: LRDs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.063
    metric_stds:
    - 0.001
  - model: GPM
    model_plain: GPM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.064
    metric_stds:
    - 0.004
  - model: GSSC
    model_plain: GSSC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.064
    metric_stds:
    - 0.002
  - model: B-PEs
    model_plain: B-PEs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0644
    metric_stds:
    - 0.001
  - model: GSO
    model_plain: GSO
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.066
    metric_stds:
    - 0.002
  - model: Graph-Mamba
    model_plain: Graph-Mamba
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.067
    metric_stds:
    - 0.002
  - model: GPS+RWSE
    model_plain: GPS+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0681
    metric_stds:
    - 0.0004
  - model: UnionGPS
    model_plain: UnionGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0681
    metric_stds:
    - 0.0013
  - model: SPE
    model_plain: SPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0693
    metric_stds:
    - 0.004
  - model: Spec-GN
    model_plain: Spec-GN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.503
    arxiv_id: '2302.08647'
    title: Multiresolution Graph Transformers and Wavelet Positional Encoding for
      Learning Hierarchical Structures
    date: Feb 17, 2023
    date_iso: '2023-02-17'
    date_display: Feb 2023
    codebase_url: https://github.com/HySonLab/Multires-Graph-Transformer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0698
    metric_stds:
    - 0.002
  - model: R-PEs
    model_plain: R-PEs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0699
    metric_stds:
    - 0.002
  - model: GPS
    model_plain: GPS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.07
    metric_stds:
    - 0.004
  - model: GNN-SSWL
    model_plain: GNN-SSWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.274
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.07
    metric_stds:
    - 0.005
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.07
    metric_stds:
    - 0.004
  - model: PPGN++(6)
    model_plain: PPGN++(6)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.071
    metric_stds:
    - 0.001
  - model: DeepGraph
    model_plain: DeepGraph
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.072
    metric_stds:
    - 0.004
  - model: Graph MLP-Mixer
    model_plain: Graph MLP-Mixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.073
    metric_stds:
    - 0.001
  - model: Graph-ViT
    model_plain: Graph-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.073
    metric_stds:
    - 0.001
  - model: SPE-8S
    model_plain: SPE-8S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0736
    metric_stds:
    - 0.0007
  - model: GM-Mix
    model_plain: GM-Mix
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.075
    metric_stds:
    - 0.001
  - model: GRED
    model_plain: GRED
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.077
    metric_stds:
    - 0.002
  - model: Eigenformer
    model_plain: Eigenformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.077
    metric_stds:
    - null
  - model: FragNet
    model_plain: FragNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.01254'
    title: 'What Expressivity Theory Misses: Message Passing Complexity for GNNs'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.078
    metric_stds:
    - null
  - model: CIN
    model_plain: CIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.079
    metric_stds:
    - 0.006
<<<<<<< Updated upstream
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0794978814609628
    metric_stds:
    - 0.003649727726331984
  - model: GNNAK+
    model_plain: GNNAK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.08
    metric_stds:
    - 0.001
  - model: GNN (a)
    model_plain: GNN (a)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: May 5, 2024
    date_iso: '2024-05-05'
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.08
    metric_stds:
    - 0.001
  - model: AS0:1^SN
    model_plain: AS0:1^SN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: Apr 4, 2024
    date_iso: '2024-04-04'
    date_display: Apr 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.08
    metric_stds:
    - 0.004
=======
>>>>>>> Stashed changes
  - model: GIN-AK+
    model_plain: GIN-AK+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.08
    metric_stds:
    - 0.001
  - model: Graphormer-GD
    model_plain: Graphormer-GD
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.503
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.081
    metric_stds:
    - 0.009
  - model: SUN
    model_plain: SUN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.526
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.083
    metric_stds:
    - 0.003
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.004
  - model: CRaW1
    model_plain: CRaW1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.004
<<<<<<< Updated upstream
  - model: GIN, with SignNet
    model_plain: GIN, with SignNet
=======
  - model: SignNet
    model_plain: SignNet
>>>>>>> Stashed changes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2410.09737'
    title: Towards Stable, Globally Expressive Graph Representations with Laplacian
      Eigenvectors
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.003
  - model: GINE-ViT
    model_plain: GINE-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.004
  - model: GPS-LGD
    model_plain: GPS-LGD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.001
  - model: CRaWl
    model_plain: CRaWl
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.085
    metric_stds:
    - 0.004
  - model: GINE + Hodge1Lap(project)
    model_plain: GINE + Hodge1Lap(project)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.086
    metric_stds:
    - 0.005
=======
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0853
    metric_stds:
    - 0.0026
>>>>>>> Stashed changes
  - model: Graphormer-URPE
    model_plain: Graphormer-URPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.086
    metric_stds:
    - 0.007
  - model: URPE
    model_plain: URPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.086
    metric_stds:
    - 0.007
  - model: Eigenformer (feat.)
    model_plain: Eigenformer (feat.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.17791'
    title: Graph Transformers without Positional Encodings
    date: Jan 2024
    date_iso: 2024-01
    date_display: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.089
    metric_stds:
    - null
  - model: PathNN
    model_plain: PathNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.09
    metric_stds:
    - 0.004
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.09
    metric_stds:
    - 0.001
  - model: GatedGCN-RWPE+LSPE+PosLoss
    model_plain: GatedGCN-RWPE+LSPE+PosLoss
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.09
    metric_stds:
    - 0.001
  - model: GNN-AK
    model_plain: GNN-AK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.091
    metric_stds:
<<<<<<< Updated upstream
    - 0.002
  - model: GIN+CSE
    model_plain: GIN+CSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.03113'
    title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based
      Centrality'
    date: Jan 2025
    date_iso: 2025-01
    date_display: Jan 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.092
    metric_stds:
    - 0.002
  - model: KP-GIN+
    model_plain: KP-GIN+
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_iso: '2023-06-09'
    date_display: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.093
    metric_stds:
    - 0.007
  - model: GRPE-FFGT
    model_plain: GRPE-FFGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.093
    metric_stds:
    - 0.004
  - model: CIN (small)
    model_plain: CIN (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.004
  - model: Ours(580k)
    model_plain: Ours(580k)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01704'
    title: Transformers are efficient hierarchical chemical graph learners
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.003
  - model: K-Subgraph SAT
    model_plain: K-Subgraph SAT
=======
    - 0.011
  - model: KP-GIN
    model_plain: KP-GIN
>>>>>>> Stashed changes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.093
    metric_stds:
    - 0.007
  - model: GatedGCN-RWPE+LSPE
    model_plain: GatedGCN-RWPE+LSPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.093
    metric_stds:
    - 0.003
  - model: K-Subgraph SAT
    model_plain: K-Subgraph SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.008
  - model: AWE
    model_plain: AWE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.005
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.008
  - model: CIN (small)
    model_plain: CIN (small)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
<<<<<<< Updated upstream
    - 0.003
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.008
  - model: GRPE
    model_plain: GRPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.101
    metric_stds:
    - 0.006
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.101
    metric_stds:
=======
>>>>>>> Stashed changes
    - 0.004
  - model: KS-SAT
    model_plain: KS-SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.094
    metric_stds:
    - 0.008
  - model: PNA-RWPE+LSPE
    model_plain: PNA-RWPE+LSPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.095
    metric_stds:
    - 0.002
  - model: DS-GNN
    model_plain: DS-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.097
    metric_stds:
    - 0.006
  - model: GSN
    model_plain: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.101
    metric_stds:
    - 0.01
  - model: PNA + MAP
    model_plain: PNA + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.101
    metric_stds:
    - 0.005
  - model: SignNet-8S
    model_plain: SignNet-8S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1034
    metric_stds:
    - 0.0056
  - model: SAN-RWPE+LSPE
    model_plain: SAN-RWPE+LSPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.104
    metric_stds:
    - 0.004
  - model: PNA + SignNet
    model_plain: PNA + SignNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.105
    metric_stds:
    - 0.007
  - model: GraphiT-RWPE+LSPE
    model_plain: GraphiT-RWPE+LSPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.106
    metric_stds:
    - 0.002
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/rampasek/GraphGPS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.108
    metric_stds:
    - 0.009
<<<<<<< Updated upstream
  - model: GSN
    model_plain: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.108
    metric_stds:
    - 0.018
  - model: CS-GNN
    model_plain: CS-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.09291'
    title: A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products
      and Graph Coarsening
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.109
    metric_stds:
    - 0.005
  - model: Nested-GNN
    model_plain: Nested-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.04941'
    title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle
      Counting Power
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.111
    metric_stds:
    - 0.003
  - model: NGNN
    model_plain: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.111
    metric_stds:
    - 0.003
=======
>>>>>>> Stashed changes
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_iso: '2025-02-01'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.111
    metric_stds:
    - 0.007
  - model: NGNN
    model_plain: NGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.111
    metric_stds:
<<<<<<< Updated upstream
    - 0.005
  - model: K-SG SAT
    model_plain: K-SG SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.115
    metric_stds:
    - 0.005
=======
    - 0.003
>>>>>>> Stashed changes
  - model: GSN with cycles
    model_plain: GSN with cycles
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.115
    metric_stds:
    - 0.012
  - model: GSN
    model_plain: GSN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.01254'
    title: 'What Expressivity Theory Misses: Message Passing Complexity for GNNs'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.12
    metric_stds:
    - null
  - model: GatedGCN + MAP
    model_plain: GatedGCN + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.12
    metric_stds:
    - 0.002
  - model: GatedGCN + SignNet
    model_plain: GatedGCN + SignNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.121
    metric_stds:
    - 0.005
  - model: Graphormer_SLIM
    model_plain: Graphormer_SLIM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.122
    metric_stds:
    - 0.006
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.122
    metric_stds:
    - 0.006
  - model: Unionormer
    model_plain: Unionormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1241
    metric_stds:
    - 0.0056
  - model: Tango_GatedGCN
    model_plain: Tango_GatedGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.128
    metric_stds:
    - 0.011
  - model: HopFormer
    model_plain: HopFormer
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1306
    metric_stds:
    - 0.0194
  - model: MGT + WavePE
    model_plain: MGT + WavePE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08647'
    title: Multiresolution Graph Transformers and Wavelet Positional Encoding for
      Learning Hierarchical Structures
    date: Feb 17, 2023
    date_iso: '2023-02-17'
    date_display: Feb 2023
    codebase_url: https://github.com/HySonLab/Multires-Graph-Transformer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.131
    metric_stds:
    - 0.003
  - model: PNA + LapPE + RS
    model_plain: PNA + LapPE + RS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.132
    metric_stds:
    - 0.01
  - model: SMP
    model_plain: SMP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.138
    metric_stds:
<<<<<<< Updated upstream
    - 0.005
  - model: SAN+LapPE
    model_plain: SAN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.139
    metric_stds:
    - 0.006
  - model: SAN+RWSE
    model_plain: SAN+RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.139
    metric_stds:
    - 0.006
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.139
    metric_stds:
    - 0.006
  - model: VANILLA-FFGT
    model_plain: VANILLA-FFGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_iso: 2023-11
    date_display: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.14
    metric_stds:
    - 0.005
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    - null
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.508577
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.139
    metric_stds:
    - 0.006
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
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.142
    metric_stds:
    - 0.001
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.387155
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.142
    metric_stds:
    - 0.01
  - model: Ours(100K)
    model_plain: Ours(100K)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.143
    metric_stds:
    - 0.006
  - model: EGT
    model_plain: EGT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.143
    metric_stds:
    - 0.011
  - model: AgentNet
    model_plain: AgentNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.144
    metric_stds:
    - 0.016
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.418
    arxiv_id: '2302.08647'
    title: Multiresolution Graph Transformers and Wavelet Positional Encoding for
      Learning Hierarchical Structures
    date: Feb 17, 2023
    date_iso: '2023-02-17'
    date_display: Feb 2023
    codebase_url: https://github.com/HySonLab/Multires-Graph-Transformer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.145
    metric_stds:
    - 0.007
  - model: MPNN (sum)
    model_plain: MPNN (sum)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.480805
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.145
    metric_stds:
<<<<<<< Updated upstream
    - 0.008
  - model: SIMPLE
    model_plain: SIMPLE
=======
    - 0.007
  - model: MPNN-JT
    model_plain: MPNN-JT
>>>>>>> Stashed changes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2601.18917'
    title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
=======
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
>>>>>>> Stashed changes
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.151
    metric_stds:
<<<<<<< Updated upstream
    - 0.001
  - model: HIMP
    model_plain: HIMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.151
    metric_stds:
    - 0.006
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1517617683115362
    metric_stds:
    - 0.02268571908117693
=======
    - null
>>>>>>> Stashed changes
  - model: OSAN
    model_plain: OSAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.154
    metric_stds:
    - 0.008
  - model: BasisNet-8S
    model_plain: BasisNet-8S
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1554
    metric_stds:
    - 0.0048
  - model: BasisNet
    model_plain: BasisNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1555
    metric_stds:
    - 0.0124
  - model: DimeNet++ (large)
    model_plain: DimeNet++ (large)
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.158
    metric_stds:
    - 0.002
  - model: GraphiT + MAP
    model_plain: GraphiT + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.16
    metric_stds:
    - 0.006
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_iso: '2024-02-13'
    date_display: Feb 2024
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.163
    metric_stds:
    - 0.004
  - model: PaiNN (large)
    model_plain: PaiNN (large)
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.165
    metric_stds:
    - 0.002
  - model: DGN
    model_plain: DGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.168
    metric_stds:
    - null
  - model: SAN + MAP
    model_plain: SAN + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.18716'
    title: 'Laplacian Canonization: A Minimalist Approach to Sign and Basis Invariant
      Spectral Embedding'
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/PKU-ML/LaplacianCanonization
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.17
    metric_stds:
    - 0.012
  - model: PaiNN
    model_plain: PaiNN
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.172
    metric_stds:
    - 0.002
  - model: NoPE
    model_plain: NoPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1772
    metric_stds:
    - 0.004
  - model: GPS+GE
    model_plain: GPS+GE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1789
    metric_stds:
    - 0.0071
  - model: SAN
    model_plain: SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.181
    metric_stds:
    - 0.004
  - model: Graph-ViT
    model_plain: Graph-ViT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.181
    metric_stds:
    - 0.006
  - model: SphereNet
    model_plain: SphereNet
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.185
    metric_stds:
    - 0.003
  - model: SE(3)-Transformer
    model_plain: SE(3)-Transformer
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.188
    metric_stds:
    - 0.003
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.188
    metric_stds:
    - null
  - model: PNA(100K)
    model_plain: PNA(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.188
    metric_stds:
    - 0.004
  - model: MPNN
    model_plain: MPNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.189
    metric_stds:
    - null
  - model: Exphormer
    model_plain: Exphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1905
    metric_stds:
    - 0.0276
  - model: GEANet
    model_plain: GEANet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_iso: '2025-01-30'
    date_display: Jan 2025
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.193
    metric_stds:
    - 0.001
  - model: EGNN
    model_plain: EGNN
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.195
    metric_stds:
    - 0.004
  - model: GPS
    model_plain: GPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1968
    metric_stds:
    - 0.012
  - model: DimeNet++
    model_plain: DimeNet++
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.198
    metric_stds:
    - 0.002
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.209
    metric_stds:
    - 0.018
  - model: EquiBind
    model_plain: EquiBind
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.21
    metric_stds:
    - 0.005
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.509
    arxiv_id: '2302.08647'
    title: Multiresolution Graph Transformers and Wavelet Positional Encoding for
      Learning Hierarchical Structures
    date: Feb 17, 2023
    date_iso: '2023-02-17'
    date_display: Feb 2023
    codebase_url: https://github.com/HySonLab/Multires-Graph-Transformer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.214
    metric_stds:
    - 0.006
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.214
    metric_stds:
    - 0.006
  - model: GatedGCN-PE/E(500K)
    model_plain: GatedGCN-PE/E(500K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.214
    metric_stds:
<<<<<<< Updated upstream
    - 0.005
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.214
    metric_stds:
=======
>>>>>>> Stashed changes
    - 0.006
  - model: GT
    model_plain: GT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.6
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.226
    metric_stds:
    - 0.014
<<<<<<< Updated upstream
  - model: 3WLGNN-E
    model_plain: 3WLGNN-E
=======
  - model: Graphtransformer
    model_plain: Graphtransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: May 10, 2023
    date_iso: '2023-05-10'
    date_display: May 2023
    codebase_url: https://github.com/qslim/PDF
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.226
    metric_stds:
    - 0.014
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.245
    metric_stds:
    - 0.003
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: https://github.com/vijaydwivedi75/gnn-lspe
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.251
    metric_stds:
    - 0.009
  - model: GIN
    model_plain: GIN
>>>>>>> Stashed changes
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.252
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: Dec 3, 2023
    date_iso: '2023-12-03'
    date_display: Dec 2023
    codebase_url: https://github.com/skeletondyh/GRED
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.278
    metric_stds:
    - 0.003
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.278
    metric_stds:
    - 0.006
  - model: GIN + rand id
    model_plain: GIN + rand id
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.279
    metric_stds:
    - 0.023
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.282
    metric_stds:
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
    - 0.285
    metric_stds:
    - 0.004
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.504
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.292
    metric_stds:
    - 0.006
<<<<<<< Updated upstream
  - model: BS-KAGCN
    model_plain: BS-KAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3
    metric_stds:
    - 0.0332
  - model: RBF-KAGCN
    model_plain: RBF-KAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.18380'
    title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/RomanBresson/KAGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3026
    metric_stds:
    - 0.0663
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.303
    metric_stds:
    - 0.068
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_iso: 2023-08
    date_display: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.306
    metric_stds:
    - 0.023
=======
>>>>>>> Stashed changes
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
    - 0.296
    metric_stds:
    - 0.005
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.508
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.303
    metric_stds:
    - 0.068
  - model: WL
    model_plain: WL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.317
    metric_stds:
    - 0.031
  - model: GatedGCN(100K)
    model_plain: GatedGCN(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.328
    metric_stds:
    - 0.003
  - model: RingGNN
    model_plain: RingGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.527
    arxiv_id: '2301.09505'
    title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/lsj2408/Graphormer-GD
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.353
    metric_stds:
    - 0.019
  - model: Graph-MLPMixer
    model_plain: Graph-MLPMixer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3617
    metric_stds:
    - 0.0222
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.363
    metric_stds:
    - 0.009
  - model: LRGA + GatedGCN
    model_plain: LRGA + GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.367
    metric_stds:
    - 0.008
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
<<<<<<< Updated upstream
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    params_millions: 2.0
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.367
    metric_stds:
    - 0.011
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.375
    metric_stds:
    - 0.003
  - model: UnionSAGE
    model_plain: UnionSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3768
    metric_stds:
    - 0.0041
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
<<<<<<< Updated upstream
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    params_millions: 0.531345
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.384
    metric_stds:
    - 0.007
  - model: GIN(100K)
    model_plain: GIN(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.387
    metric_stds:
    - 0.015
  - model: MoNet(100K)
    model_plain: MoNet(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.397
    metric_stds:
    - 0.01
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
<<<<<<< Updated upstream
    params_millions: null
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    params_millions: 0.505341
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.398
    metric_stds:
    - 0.002
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.01254'
    title: 'What Expressivity Theory Misses: Message Passing Complexity for GNNs'
    date: Sep 2025
    date_iso: 2025-09
    date_display: Sep 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4
    metric_stds:
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.407
    metric_stds:
    - 0.007
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
<<<<<<< Updated upstream
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: Feb 2021
    date_iso: 2021-02
    date_display: Feb 2021
    codebase_url: https://github.com/toenshoff/CRaWl
=======
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.408
    metric_stds:
    - 0.008
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.41
    metric_stds:
    - 0.005
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.459
    metric_stds:
    - 0.006
  - model: UnionGCN
    model_plain: UnionGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4625
    metric_stds:
    - 0.0222
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.463
    metric_stds:
    - 0.002
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.466
    metric_stds:
    - 0.006
  - model: GraphSage(100K)
    model_plain: GraphSage(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
>>>>>>> Stashed changes
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.468
    metric_stds:
    - 0.003
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.468
    metric_stds:
    - 0.003
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.469
    metric_stds:
    - 0.002
  - model: GAT(100K)
    model_plain: GAT(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.1
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.475
    metric_stds:
    - 0.007
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.03348'
    title: Global Self-Attention as a Replacement for Graph Convolution
    date: Aug 2021
    date_iso: 2021-08
    date_display: Aug 2021
    codebase_url: https://github.com/shamim-hussain/egt
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.475
    metric_stds:
    - 0.007
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.527
    arxiv_id: '2302.08647'
    title: Multiresolution Graph Transformers and Wavelet Positional Encoding for
      Learning Hierarchical Structures
    date: Feb 17, 2023
    date_iso: '2023-02-17'
    date_display: Feb 2023
    codebase_url: https://github.com/HySonLab/Multires-Graph-Transformer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.526
    metric_stds:
    - 0.051
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 3.8
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/microsoft/Graphormer
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.526
    metric_stds:
    - 0.051
  - model: GraphTransformer(500K)
    model_plain: GraphTransformer(500K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.598
    metric_stds:
    - 0.049
  - model: Graphtransformer
    model_plain: Graphtransformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6038
    metric_stds:
    - 0.0151
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.609
    metric_stds:
    - 0.0155
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6225
    metric_stds:
    - 0.0096
  - model: DIFFormer
    model_plain: DIFFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6602
    metric_stds:
    - 0.0294
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6619
    metric_stds:
    - 0.0067
  - model: SGFormer
    model_plain: SGFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.02268'
    title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control'
    date: Feb 2026
    date_iso: 2026-02
    date_display: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6703
    metric_stds:
    - 0.0033
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: https://github.com/leichen2018/GNN-Substructure-Counting
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.681
    metric_stds:
    - 0.005
  milestones:
  - value: 0.317
    std: 0.031
    model: WL
    arxiv_id: '2002.04025'
    title: Can Graph Neural Networks Count Substructures?
    date: 2020-02
  - value: 0.138
    std: null
    model: SMP
    arxiv_id: '2006.15107'
    title: Building powerful and equivariant graph neural networks with structural
      message-passing
    date: 2020-06
  - value: 0.122
    std: 0.006
<<<<<<< Updated upstream
    model: CIN
    arxiv_id: '2102.08786'
    title: 'Walking Out of the Weisfeiler Leman Hierarchy: Graph Learning Beyond Message
      Passing'
    date: 2021-02
  - value: 0.062
    std: 0.003
    model: GraphGPS + HDSE
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: 2023-08
  - value: 0.057
    std: 0.003
    model: GRIT + RRWP + Hodge1Lap(project)
    arxiv_id: '2310.19285'
    title: Facilitating Graph Neural Networks with Random Walk on Simplicial Complexes
    date: 2023-10
=======
    model: Graphormer_SLIM
    arxiv_id: '2106.05234'
    title: Do Transformers Really Perform Bad for Graph Representation?
    date: 2021-06
  - value: 0.09
    std: 0.001
    model: GatedGCN+LapPE
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: 2021-10
  - value: 0.07
    std: 0.004
    model: GPS
    arxiv_id: '2205.12454'
    title: Recipe for a General, Powerful, Scalable Graph Transformer
    date: 2022-05
  - value: 0.0698
    std: 0.002
    model: Spec-GN
    arxiv_id: '2302.08647'
    title: Multiresolution Graph Transformers and Wavelet Positional Encoding for
      Learning Hierarchical Structures
    date: '2023-02-17'
  - value: 0.066
    std: 0.002
    model: GSO
    arxiv_id: '2305.06102'
    title: Towards Better Graph Representation Learning with Parameterized Decomposition
      & Filtering
    date: '2023-05-10'
  - value: 0.059
    std: 0.002
    model: GRIT
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
>>>>>>> Stashed changes
---

