---
title: Tox21
slug: tox21
benchmark: MoleculeNet
task_type: graph_classification
description: Multi-task toxicity prediction (12 tasks) on NCI Tox21 challenge compounds.
primary_metric: ROC-AUC
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.MoleculeNet.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 12
result_count: 39
best_model:
  model: GIN-VN
  value: 0.7757
  metric: ROC-AUC
  arxiv_id: '2110.07875'
  paper_title: Graph Neural Networks with Learnable Structural and Positional Representations
variants:
- slug: scaffold-split
  name: Scaffold split
  notes: ''
  is_standard: true
  primary_metric: ROC-AUC
  higher_is_better: true
  stats:
    num_graphs: null
    avg_nodes: null
    avg_edges: null
  metrics:
  - ROC-AUC
  - Accuracy
  - ROCAUC
  rows:
  - model: GIN-VN
    model_plain: GIN-VN
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
    is_best: true
    metric_values:
    - 0.7757
    - null
    - null
    metric_stds:
    - 0.0062
    - null
    - null
  - model: GCN-VN
    model_plain: GCN-VN
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
    is_best: true
    metric_values:
    - 0.7746
    - null
    - null
    metric_stds:
    - 0.0086
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
    is_best: true
    metric_values:
    - 0.7743
    - null
    - null
    metric_stds:
    - 0.0073
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.7529
    - null
    - null
    metric_stds:
    - 0.0069
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.7491
    - null
    - null
    metric_stds:
    - 0.0051
    - null
    - null
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
    - 0.741
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
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
    - 0.736
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
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
    - 0.735
    - null
    - null
    metric_stds:
    - 0.01
    - null
    - null
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
    - 0.729
    - null
    - null
    metric_stds:
    - 0.006
    - null
    - null
  - model: GIN
    model_plain: GIN
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
    - 0.727
    - null
    - null
    metric_stds:
    - 0.017
    - null
    - null
  - model: GCN
    model_plain: GCN
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
    - 0.722
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
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
    - 0.721
    - null
    - null
    metric_stds:
    - 0.011
    - null
    - null
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
    - 0.716
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
    - null
    - null
    - 0.772
    metric_stds:
    - null
    - null
    - 0.006
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
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
    - null
    - null
    - 0.774
    metric_stds:
    - null
    - null
    - 0.007
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
    - null
    - null
    - 0.784
    metric_stds:
    - null
    - null
    - 0.005
  - model: PNA
    model_plain: PNA
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
    - null
    - null
    - 0.755
    metric_stds:
    - null
    - null
    - 0.008
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
    - null
    - null
    - 0.761
    metric_stds:
    - null
    - null
    - 0.002
  - model: SAN
    model_plain: SAN
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
    - null
    - null
    - 0.744
    metric_stds:
    - null
    - null
    - 0.007
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
    - null
    - null
    - 0.766
    metric_stds:
    - null
    - null
    - 0.007
  - model: Graph-ViT
    model_plain: Graph-ViT
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
    - null
    - null
    - 0.743
    metric_stds:
    - null
    - null
    - 0.003
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
    - null
    - null
    - 0.769
    metric_stds:
    - null
    - null
    - 0.011
  - model: GAT
    model_plain: GAT
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
    - null
    - 0.9035
    - null
    metric_stds:
    - null
    - 0.0071
    - null
  - model: 3WLGNN
    model_plain: 3WLGNN
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
    - null
    - 0.9031
    - null
    metric_stds:
    - null
    - 0.0133
    - null
  - model: SGFormer
    model_plain: SGFormer
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
    - null
    - 0.8806
    - null
    metric_stds:
    - null
    - 0.005
    - null
  - model: MEWISPool
    model_plain: MEWISPool
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
    - null
    - 0.8813
    - null
    metric_stds:
    - null
    - 0.0005
    - null
  - model: CurvGN
    model_plain: CurvGN
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
    - null
    - 0.9087
    - null
    metric_stds:
    - null
    - 0.0038
    - null
  - model: NestedGIN
    model_plain: NestedGIN
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
    - null
    - 0.9142
    - null
    metric_stds:
    - null
    - 0.0118
    - null
  - model: DropGIN
    model_plain: DropGIN
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
    - null
    - 0.9166
    - null
    metric_stds:
    - null
    - 0.0092
    - null
  - model: GatedGCN+LapPE
    model_plain: GatedGCN+LapPE
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
    - null
    - 0.9171
    - null
    metric_stds:
    - null
    - 0.0071
    - null
  - model: GraphSNN
    model_plain: GraphSNN
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
    - null
    - 0.9224
    - null
    metric_stds:
    - null
    - 0.0059
    - null
  - model: GCN
    model_plain: GCN
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
    - null
    - 0.901
    - null
    metric_stds:
    - null
    - 0.0077
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
    - null
    - 0.9174
    - null
    metric_stds:
    - null
    - 0.0074
    - null
  - model: GatedGCN
    model_plain: GatedGCN
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
    - null
    - 0.9083
    - null
    metric_stds:
    - null
    - 0.0096
    - null
  - model: UnionGatedGCN
    model_plain: UnionGatedGCN
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
    - null
    - 0.9131
    - null
    metric_stds:
    - null
    - 0.0089
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
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
    - null
    - 0.8836
    - null
    metric_stds:
    - null
    - 0.0015
    - null
  - model: UnionGraphSAGE
    model_plain: UnionGraphSAGE
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
    - null
    - 0.8859
    - null
    metric_stds:
    - null
    - 0.0012
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
    - null
    - 0.9174
    - null
    metric_stds:
    - null
    - 0.0095
    - null
  - model: UnionSNN
    model_plain: UnionSNN
    is_baseline: false
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
    - null
    - 0.9176
    - null
    metric_stds:
    - null
    - 0.0085
    - null
  milestones:
  - value: 0.7757
    std: 0.0062
    model: GIN-VN
    arxiv_id: '2110.07875'
    title: Graph Neural Networks with Learnable Structural and Positional Representations
    date: 2021-10
---

