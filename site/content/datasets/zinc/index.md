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
result_count: 166
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
  - '% N.U.V.'
  - Accuracy
  - FCD
  - Hit Ratio
  - MMD
  - NSPDK
  - RMSE
  - Unique
  - Vina Score
  - idity
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
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
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
  - model: GRIT
    model_plain: GRIT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.023
    - null
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
    - 0.0017
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FragNet
    model_plain: FragNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0237
    - null
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
  - model: Graphormer-GD
    model_plain: Graphormer-GD
    is_baseline: false
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
    - 0.025
    - null
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
    - 0.0026
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.0025
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: CIN
    model_plain: CIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.027
    - null
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: URPE
    model_plain: URPE
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
  - model: Graphormer-URPE
    model_plain: Graphormer-URPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: NGNN
    model_plain: NGNN
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
    - 0.029
    - null
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
  - model: AUTOBAHN
    model_plain: AUTOBAHN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.029
    - null
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
    - 0.0031
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
    - 0.007
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
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
  - model: HIMP
    model_plain: HIMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: GC
    model_plain: GC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: Oct 2016
    date_iso: 2016-10
    date_display: Oct 2016
    codebase_url: https://github.com/aspuru-guzik-group/chemical_vae
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.05
    - null
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
  - model: Graphormer
    model_plain: Graphormer
    is_baseline: false
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
    - 0.052
    - null
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
  - model: GRIT-SPSE
    model_plain: GRIT-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: GIN
    model_plain: GIN
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
    - 0.088
    - null
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
  - model: MoNet
    model_plain: MoNet
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
  - model: GAT
    model_plain: GAT
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
    - 0.111
    - null
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
  - model: GCN
    model_plain: GCN
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
    - 0.113
    - null
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
    - 0.0017
    - null
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
  - model: Encoder
    model_plain: Encoder
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: Oct 2016
    date_iso: 2016-10
    date_display: Oct 2016
    codebase_url: https://github.com/aspuru-guzik-group/chemical_vae
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.13
    - null
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
  - model: VAE
    model_plain: VAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: Oct 2016
    date_iso: 2016-10
    date_display: Oct 2016
    codebase_url: https://github.com/aspuru-guzik-group/chemical_vae
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.15
    - null
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
    - 0.0079
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: 1-hot SMILES
    model_plain: 1-hot SMILES
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: Oct 2016
    date_iso: 2016-10
    date_display: Oct 2016
    codebase_url: https://github.com/aspuru-guzik-group/chemical_vae
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.16
    - null
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
  - model: ECFP
    model_plain: ECFP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: Oct 2016
    date_iso: 2016-10
    date_display: Oct 2016
    codebase_url: https://github.com/aspuru-guzik-group/chemical_vae
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.38
    - null
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
  - model: MEAN
    model_plain: MEAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: Oct 2016
    date_iso: 2016-10
    date_display: Oct 2016
    codebase_url: https://github.com/aspuru-guzik-group/chemical_vae
    uses_external_data: false
    is_best: false
    metric_values:
    - 1.14
    - null
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
    - null
    - 0.9919
    - null
    - null
    - null
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
    - null
    - 0.9933
    - null
    - null
    - null
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
    - null
    - 0.9914
    - null
    - null
    - null
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
    - null
    - 0.9344
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0059
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
    - null
    - 0.9337
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
    - null
    - 0.9414
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0065
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
    - null
    - 0.9415
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
    - null
    - 0.9448
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
    - null
    - 0.9453
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0048
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
    - 0.761
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.024
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
    - 0.736
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.048
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
    - 0.723
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.033
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
    - 0.713
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.054
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
    - 0.752
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
  - model: GATED-GCN-4
    model_plain: GATED-GCN-4
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
    - 0.764
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.029
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
    - 0.731
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.005
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
    - 0.735
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
  - model: JT-VAE
    model_plain: JT-VAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 1.0
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
  - model: GCPN
    model_plain: GCPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9997
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
  - model: MRNN
    model_plain: MRNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9989
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
  - model: GraphMVP
    model_plain: GraphMVP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.4038
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
  - model: GRF
    model_plain: GRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.3942
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
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.991
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
  - model: MoFlow
    model_plain: MoFlow
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.10137'
    title: 'MoFlow: An Invertible Flow Model for Generating Molecular Graphs'
    date: Jun 2020
    date_iso: 2020-06
    date_display: Jun 2020
    codebase_url: https://github.com/calvin-zcx/moflow
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.9999
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
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 16.023
    - null
    - null
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
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 33.546
    - null
    - null
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
  - model: GraphArm
    model_plain: GraphArm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 16.26
    - null
    - null
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
  - model: MiCaM
    model_plain: MiCaM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 31.495
    - null
    - null
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
  - model: SPECTRE
    model_plain: SPECTRE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 18.44
    - null
    - null
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
  - model: GSDM
    model_plain: GSDM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 12.956
    - null
    - null
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
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 16.737
    - null
    - null
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
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 14.656
    - null
    - null
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
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 23.06
    - null
    - null
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
  - model: MoFlow
    model_plain: MoFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 20.931
    - null
    - null
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
  - model: CatFlow
    model_plain: CatFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 13.211
    - null
    - null
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
  - model: DeFoG
    model_plain: DeFoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 2.03
    - null
    - null
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
  - model: HOG-Diff
    model_plain: HOG-Diff
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.04308'
    title: 'HOG-Diff: Higher-Order Guided Diffusion for Graph Generation'
    date: Feb 2025
    date_iso: 2025-02
    date_display: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 1.633
    - null
    - null
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
  - model: JT-VAE
    model_plain: JT-VAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.263
    - null
    - null
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
  - model: GCPN
    model_plain: GCPN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.023
    - null
    - null
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
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: GA
    model_plain: GA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: MARS
    model_plain: MARS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.271
    - null
    - null
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
  - model: HierVAE
    model_plain: HierVAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
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
  - model: H-VAE*
    model_plain: H-VAE*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.037
    - null
    - null
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
  - model: F-VAE*
    model_plain: F-VAE*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.085
    - null
    - null
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
  - model: PS-VAE
    model_plain: PS-VAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2106.15098'
    title: Molecule Generation by Principal Subgraph Mining and Assembling
    date: Jun 2021
    date_iso: 2021-06
    date_display: Jun 2021
    codebase_url: https://github.com/THUNLP-MT/PS-VAE
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 0.318
    - null
    - null
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
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
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
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0001
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
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0016
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
    - 0.0001
    - null
    - null
    - null
    - null
    - null
  - model: GCN (RWSE)
    model_plain: GCN (RWSE)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0015
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
    - 0.0001
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
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
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
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0013
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
    - 0.0001
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
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0017
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
    - 0.0001
    - null
    - null
    - null
    - null
    - null
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - null
    - 0.0012
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
    - 0.0001
    - null
    - null
    - null
    - null
    - null
  - model: PaiNN
    model_plain: PaiNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
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
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
  - model: C-M
    model_plain: C-M
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_iso: 2023-01
    date_display: Jan 2023
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_best: false
    metric_values:
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
    metric_stds:
    - null
    - null
    - null
    - null
    - null
    - 0.0001
    - null
    - null
    - null
    - null
    - null
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: GraphAF+FC
    model_plain: GraphAF+FC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: MoFlow
    model_plain: MoFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: GraphEmb
    model_plain: GraphEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: SDE
    model_plain: SDE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.08892'
    title: Fast Graph Generation via Spectral Diffusion
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
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
    - 1.0
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
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8001
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0123
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
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.5465
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0122
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
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.5515
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0131
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.6834
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0136
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7012
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0124
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
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7361
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0132
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7613
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0114
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.7875
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0134
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.6635
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0116
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: G^2
    model_plain: G^2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.8036
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0118
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: dir-gcn
    model_plain: dir-gcn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9275
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0075
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9338
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9279
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0059
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: NDDGNN
    model_plain: NDDGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.9417
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
    - null
    - null
    - 0.0058
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
  - model: DHGNN
    model_plain: DHGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 0.946
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    - null
    metric_stds:
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
  - model: SBDD
    model_plain: SBDD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.06050'
    title: arXiv:2408.06050
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: https://github.com/rafalkarczewski/SimpleSBDD
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
    - -7.82
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
    - 1.47
    - null
  - model: MoFlow
    model_plain: MoFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 20.931
    - null
    - null
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
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 16.737
    - null
    - null
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
  - model: GraphEmb
    model_plain: GraphEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 35.471
    - null
    - null
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
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 14.656
    - null
    - null
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
  - model: Flow Matching
    model_plain: Flow Matching
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 18.764
    - null
    - null
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
  - model: Dirichlet FM
    model_plain: Dirichlet FM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 14.222
    - null
    - null
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
  - model: CatFlow
    model_plain: CatFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.04843'
    title: Variational Flow Matching for Graph Generation
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 13.211
    - null
    - null
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
  - model: M3GNet
    model_plain: M3GNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.02450'
    title: A Universal Graph Deep Learning Interatomic Potential for the Periodic
      Table
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/materialsvirtuallab/m3gnet
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
    - 0.0009
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
  - model: M3GNet-all
    model_plain: M3GNet-all
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.02450'
    title: A Universal Graph Deep Learning Interatomic Potential for the Periodic
      Table
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/materialsvirtuallab/m3gnet
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
    - 0.0019
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
  - model: EAM
    model_plain: EAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.02450'
    title: A Universal Graph Deep Learning Interatomic Potential for the Periodic
      Table
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/materialsvirtuallab/m3gnet
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
    - 0.0085
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
  - model: MEAM
    model_plain: MEAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.02450'
    title: A Universal Graph Deep Learning Interatomic Potential for the Periodic
      Table
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/materialsvirtuallab/m3gnet
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
    - 0.023
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
  - model: NNP
    model_plain: NNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.02450'
    title: A Universal Graph Deep Learning Interatomic Potential for the Periodic
      Table
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/materialsvirtuallab/m3gnet
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
    - 0.0023
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
  - model: MTP
    model_plain: MTP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.02450'
    title: A Universal Graph Deep Learning Interatomic Potential for the Periodic
      Table
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/materialsvirtuallab/m3gnet
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
    - 0.0008
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
  - model: System
    model_plain: System
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 1.51
    - null
    - null
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
  - model: MoFlow
    model_plain: MoFlow
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 20.93
    - null
    - null
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
  - model: GraphAF
    model_plain: GraphAF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 16.02
    - null
    - null
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
  - model: GraphDF
    model_plain: GraphDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 33.55
    - null
    - null
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
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 16.74
    - null
    - null
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
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 14.66
    - null
    - null
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
  - model: GruM
    model_plain: GruM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 2.26
    - null
    - null
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
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 3.48
    - null
    - null
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
  - model: GraphArm
    model_plain: GraphArm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 16.26
    - null
    - null
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
  - model: MDM w/ cosine
    model_plain: MDM w/ cosine
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 25.41
    - null
    - null
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
  - model: MDM w/ polynomial
    model_plain: MDM w/ polynomial
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 26.43
    - null
    - null
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
  - model: MDM w/ power-law
    model_plain: MDM w/ power-law
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.16790'
    title: Learning Flexible Forward Trajectories for Masked Molecular Diffusion
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
    - 26.09
    - null
    - null
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
  - model: Saturn
    model_plain: Saturn
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17066'
    title: 'Saturn: Sample-efficient Generative Molecular Design using Memory Manipulation'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/schwallergroup/saturn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.57981
    - null
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
    - 0.18537
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Saturn-GA
    model_plain: Saturn-GA
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17066'
    title: 'Saturn: Sample-efficient Generative Molecular Design using Memory Manipulation'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/schwallergroup/saturn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.55597
    - null
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
    - 0.05617
    - null
    - null
    - null
    - null
    - null
    - null
  - model: GEAM
    model_plain: GEAM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17066'
    title: 'Saturn: Sample-efficient Generative Molecular Design using Memory Manipulation'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/schwallergroup/saturn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.45158
    - null
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
    - 0.02408
    - null
    - null
    - null
    - null
    - null
    - null
  - model: Augmented Memory
    model_plain: Augmented Memory
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17066'
    title: 'Saturn: Sample-efficient Generative Molecular Design using Memory Manipulation'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/schwallergroup/saturn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.16966
    - null
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
    - 0.03224
    - null
    - null
    - null
    - null
    - null
    - null
  - model: ZINC 250k
    model_plain: ZINC 250k
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17066'
    title: 'Saturn: Sample-efficient Generative Molecular Design using Memory Manipulation'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/schwallergroup/saturn
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - null
    - 0.03993
    - null
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
    - 0.00355
    - null
    - null
    - null
    - null
    - null
    - null
  - model: EDP-GNN
    model_plain: EDP-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 16.737
    - null
    - null
    - 0.0485
    - null
    - 0.9979
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
  - model: GDSS
    model_plain: GDSS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 14.656
    - null
    - null
    - 0.0195
    - null
    - 0.9964
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
  - model: DiGress
    model_plain: DiGress
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 3.482
    - null
    - null
    - 0.0021
    - null
    - 0.9997
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
  - model: GruM
    model_plain: GruM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 2.257
    - null
    - null
    - 0.0015
    - null
    - 0.9997
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
  - model: DeFoG
    model_plain: DeFoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 1.425
    - null
    - null
    - 0.0008
    - null
    - 0.9999
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
  - model: SID
    model_plain: SID
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 2.01
    - null
    - null
    - 0.0021
    - null
    - 0.9984
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
  - model: TopBF
    model_plain: TopBF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 1.392
    - null
    - null
    - 0.0008
    - null
    - 1.0
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
  - model: MGG
    model_plain: MGG
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.10211'
    title: Transport-Coupled Bayesian Flows for Molecular Graph Generation
    date: Oct 2025
    date_iso: 2025-10
    date_display: Oct 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - null
    - 1.392
    - null
    - null
    - 0.0008
    - null
    - 1.0
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
  milestones:
  - value: 0.05
    std: null
    model: GC
    arxiv_id: '1610.02415'
    title: Automatic Chemical Design Using a Data-Driven Continuous Representation
      of Molecules
    date: 2016-10
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
  - MSE
  - RMSE
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: CSA-SPSE
    model_plain: CSA-SPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.061
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: Subgraphormer
    model_plain: Subgraphormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.293
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: MFN (GCN)
    model_plain: MFN (GCN)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10434'
    title: Equivariant Matrix Function Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.063
    - null
    - null
    metric_stds:
    - 0.002
    - null
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
    uses_external_data: null
    is_best: true
    metric_values:
    - 0.064
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: GRIT-RWSE
    model_plain: GRIT-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.065
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GSO
    model_plain: GSO
    is_baseline: false
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
    - 0.066
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: PDF
    model_plain: PDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10434'
    title: Equivariant Matrix Function Neural Networks
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.066
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GPS + GPSE
    model_plain: GPS + GPSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.068
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0004
    - null
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
    - 0.0681
    - null
    - null
    metric_stds:
    - 0.0013
    - null
    - null
  - model: CSA-RWSE
    model_plain: CSA-RWSE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09365'
    title: Simple Path Structural Encoding for Graph Transformers
    date: Feb 13, 2025
    date_iso: '2025-02-13'
    date_display: Feb 2025
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.069
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: Spec-GN
    model_plain: Spec-GN
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
    - 0.0698
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
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
    - 0.07
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GraphGPS
    model_plain: GraphGPS
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
    - 0.07
    - null
    - null
    metric_stds:
    - 0.004
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
    - 0.071
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
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
    - 0.073
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0007
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: GRED
    model_plain: GRED
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: MP (dual readout, VN)
    model_plain: MP (dual readout, VN)
    is_baseline: false
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
    - 0.077
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: FragNet
    model_plain: FragNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08210'
    title: arXiv:2406.08210
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.0775
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: CIN
    model_plain: CIN
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
    - 0.079
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GIN-AK+
    model_plain: GIN-AK+
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
    - 0.08
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: Graphormer-GD
    model_plain: Graphormer-GD
    is_baseline: false
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
    - 0.081
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: SUN
    model_plain: SUN
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
    - 0.083
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: MP (dual readout, slim)
    model_plain: MP (dual readout, slim)
    is_baseline: false
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
    - 0.084
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: SignNet
    model_plain: SignNet
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
    - 0.0853
    - null
    - null
    metric_stds:
    - 0.0026
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: URPE
    model_plain: URPE
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
    - 0.086
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: GNN-AK
    model_plain: GNN-AK
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
    - 0.091
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: KP-GIN
    model_plain: KP-GIN
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
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.008
    - null
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
    - 0.094
    - null
    - null
    metric_stds:
    - 0.005
    - null
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
    - 0.094
    - null
    - null
    metric_stds:
    - 0.008
    - null
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
    - 0.094
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: MP
    model_plain: MP
    is_baseline: false
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: AUTOBAHN
    model_plain: AUTOBAHN
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
    - 0.106
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: NGNN
    model_plain: NGNN
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
    - 0.111
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
  - model: Graphormer-SPIS
    model_plain: Graphormer-SPIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.115
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: novel probabilistic model
    model_plain: novel probabilistic model
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.121
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
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
    - 0.1241
    - null
    - null
    metric_stds:
    - 0.0056
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: NequIP
    model_plain: NequIP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.128
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0194
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: EGNN
    model_plain: EGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.132
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: SAT
    model_plain: SAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.135
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PaiNN
    model_plain: PaiNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.135
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SphereNet
    model_plain: SphereNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.138
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.139
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    codebase_url: https://github.com/LouisBearing/Graph-SPSE-Encoding
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.139
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: HES-GNN (2,2)
    model_plain: HES-GNN (2,2)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.14
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: F-HES-GNN (1,3)
    model_plain: F-HES-GNN (1,3)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.14
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PNA
    model_plain: PNA
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
    - 0.141
    - null
    - null
    metric_stds:
    - 0.004
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
    - 0.142
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
  - model: Ours(100K)
    model_plain: Ours(100K)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.011
    - null
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
    - 0.144
    - null
    - null
    metric_stds:
    - 0.016
    - null
    - null
  - model: MPNN
    model_plain: MPNN
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
    - 0.145
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: MPNN (sum)
    model_plain: MPNN (sum)
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
    - 0.145
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: DimeNet++
    model_plain: DimeNet++
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.145
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: MPNN-JT
    model_plain: MPNN-JT
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
    - 0.151
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: HIMP
    model_plain: HIMP
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
    - 0.151
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.152
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GNN-FA
    model_plain: GNN-FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.154
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0048
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0124
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: DGN
    model_plain: DGN
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
    - 0.168
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.168
    - null
    - null
    metric_stds:
    - 0.006
    - null
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
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: May 2018
    date_iso: 2018-05
    date_display: May 2018
    codebase_url: https://github.com/microsoft/constrained-graph-variational-autoencoder
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.176
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0071
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: PNA(100K)
    model_plain: PNA(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: HES-GNN (1,1)
    model_plain: HES-GNN (1,1)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.188
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0276
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.001
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GNN+T
    model_plain: GNN+T
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.199
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SoGCN-GRU
    model_plain: SoGCN-GRU
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.201
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.207
    - null
    - null
    metric_stds:
    - null
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
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
    - 0.214
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GatedGCN-PE/E(500K)
    model_plain: GatedGCN-PE/E(500K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.216
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: GT
    model_plain: GT
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
    - 0.226
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
  - model: GNN+random ID
    model_plain: GNN+random ID
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.13911'
    title: Logical Expressiveness of Graph Neural Networks with Hierarchical Node
      Individualization
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: https://github.com/ariesoeteman/HEGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.226
    - null
    - null
    metric_stds:
    - null
    - null
    - null
  - model: SoGCN
    model_plain: SoGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.238
    - null
    - null
    metric_stds:
    - 0.017
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.245
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - null
    - null
    metric_stds:
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
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
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.278
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.023
    - null
    - null
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
    - null
    - null
    metric_stds:
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
    - 0.285
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.292
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: Vanilla GCN + GRU
    model_plain: Vanilla GCN + GRU
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.295
    - null
    - null
    metric_stds:
    - 0.005
    - null
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
    - 0.296
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: 3WLGNN
    model_plain: 3WLGNN
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
    - 0.303
    - null
    - null
    metric_stds:
    - 0.068
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.031
    - null
    - null
  - model: ANA
    model_plain: ANA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.325
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: GatedGCN(100K)
    model_plain: GatedGCN(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
  - model: GNA
    model_plain: GNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.337
    - null
    - null
    metric_stds:
    - 0.021
    - null
    - null
  - model: RingGNN
    model_plain: RingGNN
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
    - 0.353
    - null
    - null
    metric_stds:
    - 0.019
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.366
    - null
    - null
    metric_stds:
    - 0.014
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.367
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
  - model: GCN + Vanilla
    model_plain: GCN + Vanilla
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.367
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
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
    - 0.3768
    - null
    - null
    metric_stds:
    - 0.0041
    - null
    - null
  - model: GAT
    model_plain: GAT
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
    - 0.384
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: MoNet
    model_plain: MoNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.386
    - null
    - null
    metric_stds:
    - 0.009
    - null
    - null
  - model: GIN(100K)
    model_plain: GIN(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.015
    - null
    - null
  - model: MoNet(100K)
    model_plain: MoNet(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - 0.398
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: 3WLGNN
    model_plain: 3WLGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.07141'
    title: 'SoGCN: Second-Order Graph Convolutional Networks'
    date: Oct 14, 2021
    date_iso: '2021-10-14'
    date_display: Oct 2021
    codebase_url: https://github.com/yuehaowang/SoGCN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.407
    - null
    - null
    metric_stds:
    - 0.028
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.407
    - null
    - null
    metric_stds:
    - 0.018
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.408
    - null
    - null
    metric_stds:
    - 0.008
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2109.12872'
    title: 'Meta-Aggregator: Learning to Aggregate for 1-bit Graph Neural Networks'
    date: Sep 2021
    date_iso: 2021-09
    date_display: Sep 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.426
    - null
    - null
    metric_stds:
    - 0.012
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
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
    - 0.4625
    - null
    - null
    metric_stds:
    - 0.0222
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GraphSage(100K)
    model_plain: GraphSage(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2201.12674'
    title: Rewiring with Positional Encodings for Graph Neural Networks
    date: Jan 2022
    date_iso: 2022-01
    date_display: Jan 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.468
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: GAT(100K)
    model_plain: GAT(100K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.007
    - null
    - null
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.479
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.503
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GINE
    model_plain: GINE
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
    - 0.526
    - null
    - null
    metric_stds:
    - 0.051
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.526
    - null
    - null
    metric_stds:
    - 0.051
    - null
    - null
  - model: Graphormer-Neighbor
    model_plain: Graphormer-Neighbor
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.531
    - null
    - null
    metric_stds:
    - 0.004
    - null
    - null
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.538
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GraphTransformer(500K)
    model_plain: GraphTransformer(500K)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
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
    - null
    - null
    metric_stds:
    - 0.049
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0151
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0155
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0096
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0294
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0067
    - null
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.05421'
    title: Factorizable Graph Convolutional Networks
    date: Oct 2020
    date_iso: 2020-10
    date_display: Oct 2020
    codebase_url: https://github.com/ihollywhy/FactorGCN.PyTorch
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.667
    - null
    - null
    metric_stds:
    - 0.002
    - null
    - null
  - model: Graphormer-id
    model_plain: Graphormer-id
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.13987'
    title: On Structural Expressive Power of Graph Transformers
    date: May 2023
    date_iso: 2023-05
    date_display: May 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.668
    - null
    - null
    metric_stds:
    - 0.003
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.0033
    - null
    - null
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
    - null
    - null
    metric_stds:
    - 0.005
    - null
    - null
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.613
    - null
    metric_stds:
    - null
    - 0.023
    - null
  - model: GINE
    model_plain: GINE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.546
    - null
    metric_stds:
    - null
    - 0.048
    - null
  - model: GatedGCN
    model_plain: GatedGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.251
    - null
    metric_stds:
    - null
    - 0.009
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.202
    - null
    metric_stds:
    - null
    - 0.006
    - null
  - model: GatedGCN + SignNet
    model_plain: GatedGCN + SignNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.121
    - null
    metric_stds:
    - null
    - 0.005
    - null
  - model: GatedGCN + MAP
    model_plain: GatedGCN + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.118
    - null
    metric_stds:
    - null
    - 0.0006
    - null
  - model: GatedGCN + OAP + LSPE
    model_plain: GatedGCN + OAP + LSPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.098
    - null
    metric_stds:
    - null
    - 0.0009
    - null
  - model: PNA
    model_plain: PNA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.141
    - null
    metric_stds:
    - null
    - 0.004
    - null
  - model: PNA + LapPE + RS
    model_plain: PNA + LapPE + RS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.132
    - null
    metric_stds:
    - null
    - 0.01
    - null
  - model: PNA + SignNet
    model_plain: PNA + SignNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.105
    - null
    metric_stds:
    - null
    - 0.007
    - null
  - model: PNA + MAP
    model_plain: PNA + MAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.101
    - null
    metric_stds:
    - null
    - 0.005
    - null
  - model: PNA + OAP
    model_plain: PNA + OAP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.098
    - null
    metric_stds:
    - null
    - 0.0008
    - null
  - model: PNA + OAP + LSPE
    model_plain: PNA + OAP + LSPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18378'
    title: A Canonicalization Perspective on Invariant and Equivariant Learning
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: https://github.com/PKU-ML/canonicalization
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - 0.095
    - null
    metric_stds:
    - null
    - 0.004
    - null
  - model: SD-VAE
    model_plain: SD-VAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08786'
    title: Syntax-Directed Variational Autoencoder for Structured Data
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: https://github.com/Hanjun-Dai/sdvae
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 1.366
    metric_stds:
    - null
    - null
    - 0.023
  - model: GVAE
    model_plain: GVAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08786'
    title: Syntax-Directed Variational Autoencoder for Structured Data
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: https://github.com/Hanjun-Dai/sdvae
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 1.404
    metric_stds:
    - null
    - null
    - 0.006
  - model: CVAE
    model_plain: CVAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1802.08786'
    title: Syntax-Directed Variational Autoencoder for Structured Data
    date: Feb 2018
    date_iso: 2018-02
    date_display: Feb 2018
    codebase_url: https://github.com/Hanjun-Dai/sdvae
    uses_external_data: false
    is_best: false
    metric_values:
    - null
    - null
    - 1.504
    metric_stds:
    - null
    - null
    - 0.006
  milestones:
  - value: 0.121
    std: 0.002
    model: novel probabilistic model
    arxiv_id: '1805.09076'
    title: Constrained Graph Variational Autoencoders for Molecule Design
    date: 2018-05
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
  - value: 0.063
    std: 0.002
    model: MFN (GCN)
    arxiv_id: '2310.10434'
    title: Equivariant Matrix Function Neural Networks
    date: 2023-10
  - value: 0.059
    std: 0.002
    model: GRIT
    arxiv_id: '2312.01538'
    title: Recurrent Distance Filtering for Graph Representation Learning
    date: '2023-12-03'
---

