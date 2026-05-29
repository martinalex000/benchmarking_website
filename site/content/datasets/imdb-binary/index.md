---
title: IMDB-BINARY
slug: imdb-binary
benchmark: TU Dortmund
task_type: graph_classification
description: Binary graph classification of movie collaboration networks (action vs.
  romance).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.TUDataset.html
stats:
  num_graphs: 1000
  avg_nodes: 19.8
  avg_edges: 96.5
  num_classes: 2
result_count: 70
best_model:
  model: GPM
  value: 0.8267
  metric: Accuracy
  arxiv_id: '2501.18739'
  paper_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
variants:
- slug: 10-fold-cv
  name: 10-fold CV
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
  rows:
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
    - 0.8267
    metric_stds:
    - 0.0047
  - model: RUM
    model_plain: RUM
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
    is_best: true
    metric_values:
    - 0.811
    metric_stds:
    - 0.045
  - model: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.7995
    metric_stds:
    - 0.0246
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
    - 0.785
    metric_stds:
    - 0.006
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
    - 0.7829
    metric_stds:
    - 0.0126
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
    - 0.7805
    metric_stds:
    - 0.01
  - model: GPS
    model_plain: GPS
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
    - 0.7776
    metric_stds:
    - 0.0098
  - model: CoCN
    model_plain: CoCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7726
    metric_stds:
    - 0.0027
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.771
    metric_stds:
    - 0.007
  - model: PG
    model_plain: PG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.768
    metric_stds:
    - 0.026
  - model: Full B8C1
    model_plain: Full B8C1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.762
    metric_stds:
    - 0.0518
  - model: DGN
    model_plain: DGN
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
    - 0.762
    metric_stds:
    - 0.008
  - model: SAN
    model_plain: SAN
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
    - 0.76
    metric_stds:
    - 0.019
  - model: MPNN
    model_plain: MPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.76
    metric_stds:
    - 0.027
  - model: SE2P-C3
    model_plain: SE2P-C3
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.759
    metric_stds:
    - 0.034
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
    - 0.7588
    metric_stds:
    - 0.036
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
    - 0.758
    metric_stds:
    - 0.009
  - model: SE2P-C4
    model_plain: SE2P-C4
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.757
    metric_stds:
    - 0.048
  - model: PDF
    model_plain: PDF
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
    - 0.756
    metric_stds:
    - 0.0269
  - model: 0-MPNNs
    model_plain: 0-MPNNs
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.754
    metric_stds:
    - 0.02
  - model: DropGCN
    model_plain: DropGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.753
    metric_stds:
    - 0.033
  - model: DropGIN
    model_plain: DropGIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    metric_stds:
    - 0.031
  - model: SE2P-C2
    model_plain: SE2P-C2
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.752
    metric_stds:
    - 0.029
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    metric_stds:
    - 0.051
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
    - 0.75
    metric_stds:
    - 0.042
  - model: SE2P-C1
    model_plain: SE2P-C1
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.746
    metric_stds:
    - 0.037
  - model: Full B12C1
    model_plain: Full B12C1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    metric_stds:
    - 0.0331
  - model: AWL
    model_plain: AWL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.745
    metric_stds:
    - 0.059
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
    - 0.7445
    metric_stds:
    - 0.0583
  - model: GCNJK
    model_plain: GCNJK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.0376
  - model: Repeat B12C3
    model_plain: Repeat B12C3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.0541
  - model: Diverse B12C3
    model_plain: Diverse B12C3
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.742
    metric_stds:
    - 0.0335
  - model: SEP
    model_plain: SEP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7412
    metric_stds:
    - 0.0056
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
    - 0.741
    metric_stds:
    - 0.011
  - model: GraphTrans
    model_plain: GraphTrans
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.74
    metric_stds:
    - 0.0574
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.0513
  - model: WL
    model_plain: WL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.039
  - model: WL subtree
    model_plain: WL subtree
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.738
    metric_stds:
    - 0.039
  - model: ResGCN
    model_plain: ResGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.737
    metric_stds:
    - 0.057
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
    - 0.7369
    metric_stds:
    - 0.0205
  - model: GCNFA
    model_plain: GCNFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.736
    metric_stds:
    - 0.0562
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
    - 0.735
    metric_stds:
    - 0.012
  - model: GMT
    model_plain: GMT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7348
    metric_stds:
    - 0.0076
  - model: SAGPool
    model_plain: SAGPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.734
    metric_stds:
    - 0.0302
  - model: TwoHop
    model_plain: TwoHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.724
    metric_stds:
    - 0.0561
  - model: DiffPool
    model_plain: DiffPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7227
    metric_stds:
    - 0.0447
  - model: StructPool
    model_plain: StructPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7206
    metric_stds:
    - 0.0064
  - model: IGN
    model_plain: IGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.72
    metric_stds:
    - 0.055
  - model: R-GIN + FoSR
    model_plain: R-GIN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7196
    metric_stds:
    - 0.0069
  - model: TopKPool
    model_plain: TopKPool
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7158
    metric_stds:
    - 0.0095
  - model: GCNVIR
    model_plain: GCNVIR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: https://github.com/LARS-research/LRGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.715
    metric_stds:
    - 0.049
  - model: GIN + GTR
    model_plain: GIN + GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7149
    metric_stds:
    - 0.0093
  - model: R-GIN + Every FA
    model_plain: R-GIN + Every FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7148
    metric_stds:
    - 0.0088
  - model: PS
    model_plain: PS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    metric_stds:
    - 0.022
  - model: PATCHY-SAN
    model_plain: PATCHY-SAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_iso: 2024-06
    date_display: Jun 2024
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    metric_stds:
    - 0.023
  - model: R-GIN + SDRF
    model_plain: R-GIN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7021
    metric_stds:
    - 0.0081
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
    - 0.70025
    metric_stds:
    - 0.05147
  - model: DGCNN
    model_plain: DGCNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: Dec 2019
    date_iso: 2019-12
    date_display: Dec 2019
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - null
  - model: R-GIN + Last FA
    model_plain: R-GIN + Last FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6971
    metric_stds:
    - 0.0103
  - model: R-GIN + None
    model_plain: R-GIN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6889
    metric_stds:
    - 0.0087
  - model: DGK
    model_plain: DGK
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
    - 0.6696
    metric_stds:
    - 0.0056
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
    - 0.6605
    metric_stds:
    - 0.06631
  - model: GCN + GTR
    model_plain: GCN + GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6509
    metric_stds:
    - 0.0093
  - model: GCN + DIGL
    model_plain: GCN + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6439
    metric_stds:
    - 0.0091
  - model: R-GIN + DIGL
    model_plain: R-GIN + DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6393
    metric_stds:
    - 0.0095
  - model: GCN + None
    model_plain: GCN + None
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4977
    metric_stds:
    - 0.0082
  - model: GCN + FoSR
    model_plain: GCN + FoSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4966
    metric_stds:
    - 0.0086
  - model: GCN + SDRF
    model_plain: GCN + SDRF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.494
    metric_stds:
    - 0.009
  - model: GCN + Last FA
    model_plain: GCN + Last FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4898
    metric_stds:
    - 0.0095
  - model: GCN + Every FA
    model_plain: GCN + Every FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.06835'
    title: Understanding Oversquashing in GNNs through the Lens of Effective Resistance
    date: Feb 14, 2023
    date_iso: '2023-02-14'
    date_display: Feb 2023
    codebase_url: https://github.com/blackmit/gtr_rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4817
    metric_stds:
    - 0.008
  milestones:
  - value: 0.76
    std: 0.027
    model: MPNN
    arxiv_id: '1912.06058'
    title: Coloring graph neural networks for node disambiguation
    date: 2019-12
  - value: 0.762
    std: 0.0518
    model: Full B8C1
    arxiv_id: '2302.08671'
    title: Search to Capture Long-range Dependency with Stacking GNNs for Graph Classification
    date: 2023-02
  - value: 0.785
    std: 0.006
    model: ILLS
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: '2023-05-27'
  - value: 0.7995
    std: 0.0246
    model: novel dynamic message-passing mechanism
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: 2024-10
  - value: 0.8267
    std: 0.0047
    model: GPM
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
---

