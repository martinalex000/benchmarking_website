---
title: Cornell
slug: cornell
benchmark: Heterophilic Graphs
task_type: node_classification
description: WebKB node classification on Cornell university webpages (5 classes).
primary_metric: Accuracy
higher_is_better: true
pyg_url: https://pytorch-geometric.readthedocs.io/en/latest/generated/torch_geometric.datasets.WebKB.html
stats:
  num_graphs: null
  avg_nodes: null
  avg_edges: null
  num_classes: 5
result_count: 340
best_model:
  model: FMP ode
  value: 0.938
  metric: Accuracy
  arxiv_id: '2302.14806'
  paper_title: Framelet Message Passing
variants:
- slug: standard-split
  name: Standard split
  notes: Geom-GCN 10 fixed splits.
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
  - model: FMP ode
    model_plain: FMP ode
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.938
    metric_stds:
    - 0.015
  - model: DMD++
    model_plain: DMD++
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.914
    metric_stds:
    - 0.017
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.913
    metric_stds:
    - 0.007
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.898
    metric_stds:
    - 0.006
  - model: Our (GCN) vs. GCN
    model_plain: Our (GCN) vs. GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8919
    metric_stds:
    - null
  - model: Our (APPNP) vs. APPNP
    model_plain: Our (APPNP) vs. APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8919
    metric_stds:
    - null
  - model: DMD-ACMP
    model_plain: DMD-ACMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.881
    metric_stds:
    - 0.024
  - model: simple GNN model (3-hop)
    model_plain: simple GNN model (3-hop)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8784
    metric_stds:
    - 0.0619
  - model: FSGNN
    model_plain: FSGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.873
    metric_stds:
    - 0.0453
  - model: ASGAT
    model_plain: ASGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.869
    metric_stds:
    - 0.042
  - model: NewtonNet
    model_plain: NewtonNet
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8658
    metric_stds:
    - 0.053
  - model: Diag-NSD
    model_plain: Diag-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8649
    metric_stds:
    - 0.0735
  - model: Conn-NSD
    model_plain: Conn-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: true
    metric_values:
    - 0.8595
    metric_stds:
    - 0.077
  - model: Gen-NSD
    model_plain: Gen-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568
    metric_stds:
    - 0.0651
  - model: GGCN
    model_plain: GGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568
    metric_stds:
    - 0.066
  - model: GIND
    model_plain: GIND
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.14418'
    title: Optimization-Induced Graph Implicit Nonlinear Diffusion
    date: Jun 29, 2022
    date_iso: '2022-06-29'
    date_display: Jun 2022
    codebase_url: https://github.com/7qchen/GIND
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8568
    metric_stds:
    - 0.0383
  - model: GPNN
    model_plain: GPNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8514
    metric_stds:
    - 0.06
  - model: EGNN
    model_plain: EGNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8513
    metric_stds:
    - 0.0557
  - model: LLM-BP (appr.)
    model_plain: LLM-BP (appr.)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8492
    metric_stds:
    - null
  - model: O(d)-NSD
    model_plain: O(d)-NSD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8486
    metric_stds:
    - 0.0471
  - model: Planetoid-G/T
    model_plain: Planetoid-G/T
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.845
    metric_stds:
    - null
  - model: UDGNN_GCN
    model_plain: UDGNN_GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8432
    metric_stds:
    - 0.0729
  - model: DL
    model_plain: DL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.841
    metric_stds:
    - 0.001
  - model: DMD-GCN
    model_plain: DMD-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.836
    metric_stds:
    - 0.031
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8351
    metric_stds:
    - 0.0656
  - model: LLM-BP
    model_plain: LLM-BP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.8328
    metric_stds:
    - null
  - model: UDGNN*_SAGE
    model_plain: UDGNN*_SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8324
    metric_stds:
    - 0.0783
  - model: GraphSAGE + HR
    model_plain: GraphSAGE + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8288
    metric_stds:
    - 0.0556
  - model: UDGNN*_GAT
    model_plain: UDGNN*_GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8271
    metric_stds:
    - 0.0406
  - model: GPRGNN (GDC)
    model_plain: GPRGNN (GDC)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.824
    metric_stds:
    - 0.047
  - model: PPGN
    model_plain: PPGN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.824
    metric_stds:
    - 0.043
  - model: ESC-GNN
    model_plain: ESC-GNN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.822
    metric_stds:
    - 0.04
  - model: H2GCN-1
    model_plain: H2GCN-1
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8216
    metric_stds:
    - 0.048
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8216
    metric_stds:
    - 0.0745
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8216
    metric_stds:
    - 0.048
  - model: H2GCN-2
    model_plain: H2GCN-2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8216
    metric_stds:
    - 0.06
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.821
    metric_stds:
    - 0.049
  - model: H2GCN + HR
    model_plain: H2GCN + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8206
    metric_stds:
    - 0.0627
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.82
    metric_stds:
    - 0.035
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.819
    metric_stds:
    - 0.054
  - model: CSNN
    model_plain: CSNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8162
    metric_stds:
    - 0.0432
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.816
    metric_stds:
    - 0.054
  - model: ChebNet
    model_plain: ChebNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8158
    metric_stds:
    - 0.08
  - model: Text-Embedding-3-Large
    model_plain: Text-Embedding-3-Large
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.815
    metric_stds:
    - null
  - model: LLM2Vec
    model_plain: LLM2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.8126
    metric_stds:
    - null
  - model: CHEV(GDC)
    model_plain: CHEV(GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.811
    metric_stds:
    - 0.032
  - model: ARMA
    model_plain: ARMA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.811
    metric_stds:
    - 0.061
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8108
    metric_stds:
    - 0.0659
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.81
    metric_stds:
    - 0.039
  - model: CHEV
    model_plain: CHEV
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.808
    metric_stds:
    - 0.041
  - model: BernNet
    model_plain: BernNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.803
    metric_stds:
    - 0.054
  - model: DMD-SGC
    model_plain: DMD-SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.8
    metric_stds:
    - 0.019
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.799
    metric_stds:
    - 0.053
  - model: GFMate
    model_plain: GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7967
    metric_stds:
    - 0.0847
  - model: LP+FT +GFMate
    model_plain: LP+FT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7967
    metric_stds:
    - 0.0847
  - model: GraphEmb
    model_plain: GraphEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.795
    metric_stds:
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.794
    metric_stds:
    - 0.055
  - model: WRGAT
    model_plain: WRGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    metric_stds:
    - 0.035
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.792
    metric_stds:
    - 0.063
  - model: Logistic Reg.-X
    model_plain: Logistic Reg.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7868
    metric_stds:
    - 0.033
  - model: GLR
    model_plain: GLR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7866
    metric_stds:
    - 0.043
  - model: ARMA (GDC)
    model_plain: ARMA (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.784
    metric_stds:
    - 0.041
  - model: Ours-Log
    model_plain: Ours-Log
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7811
    metric_stds:
    - 0.039
  - model: SANE-hete
    model_plain: SANE-hete
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7784
    metric_stds:
    - 0.0551
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7784
    metric_stds:
    - 0.058
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    metric_stds:
    - null
  - model: APPNP (GDC)
    model_plain: APPNP (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.778
    metric_stds:
    - 0.035
  - model: Vicuna-7B
    model_plain: Vicuna-7B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7762
    metric_stds:
    - 0.029
  - model: AAGCN
    model_plain: AAGCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.776
    metric_stds:
    - 0.068
  - model: Ours-Expn
    model_plain: Ours-Expn
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7757
    metric_stds:
    - 0.0383
  - model: DisenGCN
    model_plain: DisenGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.774
    metric_stds:
    - 0.044
  - model: 7B-to-1B
    model_plain: 7B-to-1B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7738
    metric_stds:
    - 0.027
  - model: AAGCN-N_H
    model_plain: AAGCN-N_H
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.773
    metric_stds:
    - 0.044
  - model: SG-FBGNN_N
    model_plain: SG-FBGNN_N
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7684
    metric_stds:
    - 0.0089
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
    - 0.7657
    metric_stds:
    - 0.0412
  - model: GPRGNN + HR
    model_plain: GPRGNN + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7656
    metric_stds:
    - 0.0577
  - model: GCNII
    model_plain: GCNII
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7649
    metric_stds:
    - null
  - model: GraphSAGE
    model_plain: GraphSAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7595
    metric_stds:
    - 0.0501
  - model: Bloom 1B
    model_plain: Bloom 1B
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7571
    metric_stds:
    - 0.014
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.10064'
    title: arXiv:2310.10064
    date: Oct 2023
    date_iso: 2023-10
    date_display: Oct 2023
    codebase_url: https://github.com/junjie-xu/NewtonNet
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7556
    metric_stds:
    - 0.061
  - model: Bloom 560M
    model_plain: Bloom 560M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7548
    metric_stds:
    - 0.021
  - model: MDGPT +GFMate
    model_plain: MDGPT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7547
    metric_stds:
    - 0.1006
  - model: Diffusion-X
    model_plain: Diffusion-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7511
    metric_stds:
    - 0.054
  - model: FB-GCN-N_A
    model_plain: FB-GCN-N_A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.751
    metric_stds:
    - 0.043
  - model: DGI+FT +GFMate
    model_plain: DGI+FT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7506
    metric_stds:
    - 0.1037
  - model: 7B-to-560M
    model_plain: 7B-to-560M
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.75
    metric_stds:
    - 0.04
  - model: SpecFormer
    model_plain: SpecFormer
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
    - 0.7478
    metric_stds:
    - 0.0255
  - model: Cheby+JK
    model_plain: Cheby+JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7459
    metric_stds:
    - 0.0787
  - model: GRAND
    model_plain: GRAND
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7459
    metric_stds:
    - 0.0404
  - model: FB-GCN
    model_plain: FB-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.743
    metric_stds:
    - 0.044
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7421
    metric_stds:
    - 0.0142
  - model: GRED
    model_plain: GRED
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7378
    metric_stds:
    - 0.0453
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7351
    metric_stds:
    - 0.0634
  - model: DAGNN
    model_plain: DAGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7351
    metric_stds:
    - 0.0718
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7351
    metric_stds:
    - null
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.735
    metric_stds:
    - 0.043
  - model: GCL+FT +GFMate
    model_plain: GCL+FT +GFMate
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7329
    metric_stds:
    - 0.102
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
    - 0.7297
    metric_stds:
    - 0.0221
  - model: GCNII + HR
    model_plain: GCNII + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7297
    metric_stds:
    - 0.0673
  - model: CO-GNN
    model_plain: CO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_iso: 2025-07
    date_display: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.727
    metric_stds:
    - 0.0547
  - model: Framelets
    model_plain: Framelets
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_iso: 2024-10
    date_display: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.726
    metric_stds:
    - 0.003
  - model: Shift-MLP
    model_plain: Shift-MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.723
    metric_stds:
    - 0.035
  - model: S-GCN
    model_plain: S-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7211
    metric_stds:
    - 0.0146
  - model: SG-GCN_L
    model_plain: SG-GCN_L
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7211
    metric_stds:
    - 0.0125
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
    - 0.7207
    metric_stds:
    - 0.0127
  - model: OGNN
    model_plain: OGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7191
    metric_stds:
    - 0.018
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.714
    metric_stds:
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7132
    metric_stds:
    - 0.0143
  - model: N.S.-GCN
    model_plain: N.S.-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7132
    metric_stds:
    - 0.0139
  - model: ECL-GSR
    model_plain: ECL-GSR
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7127
    metric_stds:
    - 0.0206
  - model: Graphormer
    model_plain: Graphormer
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
    - 0.7117
    metric_stds:
    - 0.0127
  - model: CoBFormer
    model_plain: CoBFormer
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
    - 0.7117
    metric_stds:
    - 0.0337
  - model: GRAFF
    model_plain: GRAFF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7108
    metric_stds:
    - 0.0364
  - model: Transformer + CAR
    model_plain: Transformer + CAR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.71
    metric_stds:
    - 0.02
  - model: SpaM
    model_plain: SpaM
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.708
    metric_stds:
    - 0.0193
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7079
    metric_stds:
    - 0.0165
  - model: SUBLIME
    model_plain: SUBLIME
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7029
    metric_stds:
    - 0.0351
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.702
    metric_stds:
    - null
  - model: GAT + HR
    model_plain: GAT + HR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7009
    metric_stds:
    - 0.0677
  - model: GAT + CAR
    model_plain: GAT + CAR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.03
  - model: Transformer
    model_plain: Transformer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.7
    metric_stds:
    - 0.02
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6976
    metric_stds:
    - 0.03
  - model: TRIGON
    model_plain: TRIGON
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6911
    metric_stds:
    - 0.0153
  - model: DeepGCNs
    model_plain: DeepGCNs
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.15454'
    title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel Geometric Polynomials'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6838
    metric_stds:
    - 0.059
  - model: DeeperGCN
    model_plain: DeeperGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6838
    metric_stds:
    - 0.0585
  - model: GIN + TAGs (8b)
    model_plain: GIN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.682
    metric_stds:
    - 0.0148
  - model: APPNP + DHGR
    model_plain: APPNP + DHGR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6811
    metric_stds:
    - 0.0659
  - model: GATv2
    model_plain: GATv2
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.68
    metric_stds:
    - 0.04
  - model: UniMP + TAGs (8b)
    model_plain: UniMP + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.678
    metric_stds:
    - 0.0178
  - model: R-GCN
    model_plain: R-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6738
    metric_stds:
    - 0.0533
  - model: DR
    model_plain: DR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6722
    metric_stds:
    - 0.0148
  - model: Geom-GCN-I-g
    model_plain: Geom-GCN-I-g
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6702
    metric_stds:
    - null
  - model: SAN
    model_plain: SAN
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
    - 0.6667
    metric_stds:
    - 0.0337
  - model: SEGSL
    model_plain: SEGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6667
    metric_stds:
    - 0.041
  - model: CPGNN
    model_plain: CPGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6622
    metric_stds:
    - 0.0769
  - model: GBK-GNN
    model_plain: GBK-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6619
    metric_stds:
    - 0.028
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.66
    metric_stds:
    - null
  - model: NodeFormer
    model_plain: NodeFormer
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
    - 0.6577
    metric_stds:
    - 0.0459
  - model: GCN-LPA
    model_plain: GCN-LPA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.656
    metric_stds:
    - 0.073
  - model: SemiEmb
    model_plain: SemiEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.654
    metric_stds:
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
    - 0.6486
    metric_stds:
    - 0.0441
  - model: GRIT
    model_plain: GRIT
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
    - 0.6486
    metric_stds:
    - 0.0584
  - model: GraphVAT
    model_plain: GraphVAT
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08226'
    title: 'Graph Adversarial Training: Dynamically Regularizing Based on Graph Structure'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/fulifeng/GraphAT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.647
    metric_stds:
    - null
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.646
    metric_stds:
    - 0.063
  - model: SeHGNN + TAGs (8b)
    model_plain: SeHGNN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.646
    metric_stds:
    - 0.0212
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.646
    metric_stds:
    - 0.0208
  - model: GCN-JKNet
    model_plain: GCN-JKNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.15127'
    title: 'Universal Deep GNNs: Rethinking Residual Connection in GNNs from a Path
      Decomposition Perspective for Preventing the Over-smoothing'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/JC-202/UDGNNs
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6459
    metric_stds:
    - 0.0868
  - model: NeuralSparse
    model_plain: NeuralSparse
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.641
    metric_stds:
    - 0.055
  - model: SF
    model_plain: SF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.64
    metric_stds:
    - null
  - model: MO-SFL
    model_plain: MO-SFL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.639
    metric_stds:
    - null
  - model: RGCN + TAGs (8b)
    model_plain: RGCN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.638
    metric_stds:
    - 0.0186
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6378
    metric_stds:
    - 0.0543
  - model: Sbert
    model_plain: Sbert
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6366
    metric_stds:
    - null
  - model: ManiReg
    model_plain: ManiReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.634
    metric_stds:
    - null
  - model: UniMP
    model_plain: UniMP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.634
    metric_stds:
    - 0.0179
  - model: KNN w/ sp.-X
    model_plain: KNN w/ sp.-X
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6307
    metric_stds:
    - 0.066
  - model: HAN + TAGs (70b)
    model_plain: HAN + TAGs (70b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.628
    metric_stds:
    - 0.0186
  - model: Feat
    model_plain: Feat
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: Mar 29, 2016
    date_iso: '2016-03-29'
    date_display: Mar 2016
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.621
    metric_stds:
    - null
  - model: Planetoid*
    model_plain: Planetoid*
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.619
    metric_stds:
    - null
  - model: GCNII
    model_plain: GCNII
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.08264'
    title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring Approach'
    date: Sep 2022
    date_iso: 2022-09
    date_display: Sep 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.617
    metric_stds:
    - 0.0591
  - model: Roberta
    model_plain: Roberta
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6168
    metric_stds:
    - null
  - model: Incep(Drop)
    model_plain: Incep(Drop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6162
    metric_stds:
    - null
  - model: IGNN
    model_plain: IGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6135
    metric_stds:
    - 0.0484
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1902.08226'
    title: 'Graph Adversarial Training: Dynamically Regularizing Based on Graph Structure'
    date: Feb 2019
    date_iso: 2019-02
    date_display: Feb 2019
    codebase_url: https://github.com/fulifeng/GraphAT
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.612
    metric_stds:
    - null
  - model: JKNet(Drop)
    model_plain: JKNet(Drop)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6108
    metric_stds:
    - null
  - model: GCOPE
    model_plain: GCOPE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6098
    metric_stds:
    - 0.1466
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6081
    metric_stds:
    - null
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.608
    metric_stds:
    - null
  - model: MLP
    model_plain: MLP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.601
    metric_stds:
    - 0.012
  - model: HAN + TAGs (8b)
    model_plain: HAN + TAGs (8b)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.6
    metric_stds:
    - 0.0147
  - model: SeHGNN
    model_plain: SeHGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.6
    metric_stds:
    - 0.013
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.598
    metric_stds:
    - 0.037
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5946
    metric_stds:
    - null
  - model: SAMGPT
    model_plain: SAMGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5934
    metric_stds:
    - 0.0982
  - model: LINKX
    model_plain: LINKX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5916
    metric_stds:
    - null
  - model: DAGPrompt
    model_plain: DAGPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5911
    metric_stds:
    - 0.1004
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: May 2021
    date_iso: 2021-05
    date_display: May 2021
    codebase_url: https://github.com/sunilkmaurya/FSGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5892
    metric_stds:
    - 0.0332
  - model: PairNorm
    model_plain: PairNorm
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_iso: 2024-02
    date_display: Feb 2024
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5892
    metric_stds:
    - 0.0315
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.10720'
    title: 'EIGNN: Efficient Infinite-Depth Graph Neural Networks'
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/SwiftieH/IGNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5891
    metric_stds:
    - 0.0315
  - model: GAT (GDC)
    model_plain: GAT (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.589
    metric_stds:
    - 0.022
  - model: Node2Seq
    model_plain: Node2Seq
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2110.00973'
    title: Graph Pointer Neural Networks
    date: Oct 2021
    date_iso: 2021-10
    date_display: Oct 2021
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.587
    metric_stds:
    - 0.068
  - model: NWR-GAE full
    model_plain: NWR-GAE full
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5864
    metric_stds:
    - 0.0561
  - model: GCN (rand. splits)
    model_plain: GCN (rand. splits)
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.584
    metric_stds:
    - 0.017
  - model: Geom-GCN-IP
    model_plain: Geom-GCN-IP
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5838
    metric_stds:
    - null
  - model: GraphNAS
    model_plain: GraphNAS
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5811
    metric_stds:
    - 0.0387
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.581
    metric_stds:
    - null
  - model: Dir-GNN
    model_plain: Dir-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.579
    metric_stds:
    - 0.018
  - model: GCN+GDC
    model_plain: GCN+GDC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.576
    metric_stds:
    - 0.041
  - model: GAuG-O
    model_plain: GAuG-O
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.576
    metric_stds:
    - 0.038
  - model: RGCN
    model_plain: RGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.576
    metric_stds:
    - 0.0178
  - model: JDR
    model_plain: JDR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5731
    metric_stds:
    - 0.016
  - model: JK-Net
    model_plain: JK-Net
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.573
    metric_stds:
    - null
  - model: All-In-One
    model_plain: All-In-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5724
    metric_stds:
    - 0.127
  - model: SNAG
    model_plain: SNAG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5703
    metric_stds:
    - 0.0348
  - model: GEN
    model_plain: GEN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5702
    metric_stds:
    - 0.0719
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.568
    metric_stds:
    - 0.0122
  - model: MixHop
    model_plain: MixHop
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5676
    metric_stds:
    - null
  - model: Our (SGC) vs. SGC
    model_plain: Our (SGC) vs. SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5676
    metric_stds:
    - null
  - model: SANE
    model_plain: SANE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.12357'
    title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic Graphs'
    date: Feb 2023
    date_iso: 2023-02
    date_display: Feb 2023
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5676
    metric_stds:
    - 0.0651
  - model: SGC (GDC)
    model_plain: SGC (GDC)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2206.02386'
    title: Restructuring Graphs for Higher Homophily via Adaptive Spectral Clustering
    date: Jun 2022
    date_iso: 2022-06
    date_display: Jun 2022
    codebase_url: https://github.com/seanli3/graph_restructure
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.562
    metric_stds:
    - 0.038
  - model: HAN
    model_plain: HAN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.56
    metric_stds:
    - 0.0167
  - model: Geom-GCN
    model_plain: Geom-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2007.02133'
    title: arXiv:2007.02133
    date: Jul 2020
    date_iso: 2020-07
    date_display: Jul 2020
    codebase_url: https://github.com/chennnM/GCNII
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5568
    metric_stds:
    - null
  - model: ACMGCN
    model_plain: ACMGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.556
    metric_stds:
    - 0.033
  - model: Auto-HeG
    model_plain: Auto-HeG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.555
    metric_stds:
    - 0.035
  - model: JacobiConv
    model_plain: JacobiConv
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.553
    metric_stds:
    - 0.034
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5513
    metric_stds:
    - 0.1339
  - model: MagNet
    model_plain: MagNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.551
    metric_stds:
    - 0.0131
  - model: PCNet
    model_plain: PCNet
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.55
    metric_stds:
    - 0.031
  - model: GOAL
    model_plain: GOAL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.549
    metric_stds:
    - 0.066
  - model: TED-GCN
    model_plain: TED-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.546
    metric_stds:
    - 0.032
  - model: GRCN
    model_plain: GRCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5432
    metric_stds:
    - 0.0824
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5432
    metric_stds:
    - null
  - model: Geom-GCN-I-s
    model_plain: Geom-GCN-I-s
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5432
    metric_stds:
    - null
  - model: SBert + NA
    model_plain: SBert + NA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.5421
    metric_stds:
    - null
  - model: MDGPT
    model_plain: MDGPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5419
    metric_stds:
    - 0.1308
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
    - 0.5405
    metric_stds:
    - 0.0441
  - model: ProtGNN
    model_plain: ProtGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5405
    metric_stds:
    - 0.0616
  - model: Shift-GCN
    model_plain: Shift-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.54
    metric_stds:
    - 0.018
  - model: TFE-GNN
    model_plain: TFE-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.537
    metric_stds:
    - 0.0107
  - model: MVGRL
    model_plain: MVGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5351
    metric_stds:
    - 0.0326
  - model: Sparse PCA
    model_plain: Sparse PCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.535
    metric_stds:
    - null
  - model: DeGTA
    model_plain: DeGTA
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
    - 0.5315
    metric_stds:
    - 0.0459
  - model: GPR-GNN
    model_plain: GPR-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.531
    metric_stds:
    - 0.016
  - model: CL
    model_plain: CL
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5306
    metric_stds:
    - 0.0105
  - model: GCN
    model_plain: GCN
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2002.05287'
    title: 'Geom-GCN: Geometric Graph Convolutional Networks'
    date: Feb 2020
    date_iso: 2020-02
    date_display: Feb 2020
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.527
    metric_stds:
    - null
  - model: CoGSL
    model_plain: CoGSL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5216
    metric_stds:
    - 0.0321
  - model: GPF
    model_plain: GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5215
    metric_stds:
    - 0.1453
  - model: Shift-GAT
    model_plain: Shift-GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.521
    metric_stds:
    - 0.011
  - model: DisGNN
    model_plain: DisGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.52
    metric_stds:
    - 0.057
  - model: GREET
    model_plain: GREET
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.519
    metric_stds:
    - 0.0247
  - model: JK
    model_plain: JK
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5188
    metric_stds:
    - 0.056
  - model: L2DGCN
    model_plain: L2DGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.515
    metric_stds:
    - 0.0328
  - model: GPRGNN
    model_plain: GPRGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.514
    metric_stds:
    - 0.0136
  - model: CDC
    model_plain: CDC
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.514
    metric_stds:
    - null
  - model: Logistic Reg.-A
    model_plain: Logistic Reg.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5136
    metric_stds:
    - 0.031
  - model: SGC
    model_plain: SGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.512
    metric_stds:
    - 0.009
  - model: VEPM
    model_plain: VEPM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.512
    metric_stds:
    - 0.07
  - model: JOAO
    model_plain: JOAO
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5102
    metric_stds:
    - 0.0096
  - model: CAL CausalGAT
    model_plain: CAL CausalGAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.10946'
    title: Causally-guided Regularization of Graph Attention Improves Generalizability
    date: Oct 2022
    date_iso: 2022-10
    date_display: Oct 2022
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.51
    metric_stds:
    - null
  - model: FactorGCN
    model_plain: FactorGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.13700'
    title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily with Edge
      Splitting'
    date: May 2022
    date_iso: 2022-05
    date_display: May 2022
    codebase_url: https://github.com/jingweio/ES-GNN
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.506
    metric_stds:
    - 0.018
  - model: DisamGCL
    model_plain: DisamGCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.14134'
    title: Exploring the Potential of Large Language Models for Heterophilic Graphs
    date: Aug 2024
    date_iso: 2024-08
    date_display: Aug 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5048
    metric_stds:
    - 0.02
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5026
    metric_stds:
    - 0.0145
  - model: SUGRL
    model_plain: SUGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5007
    metric_stds:
    - 0.0033
  - model: IDGL
    model_plain: IDGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.5
    metric_stds:
    - 0.0898
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.498
    metric_stds:
    - 0.036
  - model: AD-GCL
    model_plain: AD-GCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4952
    metric_stds:
    - 0.0293
  - model: VGAE
    model_plain: VGAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4932
    metric_stds:
    - 0.0919
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.09384'
    title: Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci
      Curvature
    date: Sep 2023
    date_iso: 2023-09
    date_display: Sep 2023
    codebase_url: https://github.com/Weber-GeoML/AFRC_Rewiring
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.493
    metric_stds:
    - 0.011000000000000001
  - model: BRIDGE
    model_plain: BRIDGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4928
    metric_stds:
    - 0.1256
  - model: GloGNN
    model_plain: GloGNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.01207'
    title: Sparse Bayesian Message Passing under Structural Uncertainty
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.488
    metric_stds:
    - 0.0115
  - model: GRACEIS
    model_plain: GRACEIS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4857
    metric_stds:
    - 0.0195
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
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4838
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.18581'
    title: 'Unleashing the Potential of Text-attributed Graphs: Automatic Relation
      Decomposition via Large Language Models'
    date: May 2024
    date_iso: 2024-05
    date_display: May 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.482
    metric_stds:
    - 0.0218
  - model: LDS
    model_plain: LDS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4787
    metric_stds:
    - 0.0714
  - model: SRDF
    model_plain: SRDF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4773
    metric_stds:
    - 0.0151
  - model: AERO-GNN
    model_plain: AERO-GNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.477
    metric_stds:
    - 0.042
  - model: GTR
    model_plain: GTR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4757
    metric_stds:
    - 0.0152
  - model: GCA
    model_plain: GCA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4745
    metric_stds:
    - 0.0088
  - model: BORF
    model_plain: BORF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4681
    metric_stds:
    - 0.0156
  - model: SVD
    model_plain: SVD
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.467
    metric_stds:
    - null
  - model: FAGCN
    model_plain: FAGCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.465
    metric_stds:
    - 0.017
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4648
    metric_stds:
    - 0.0797
  - model: RiemannGFM
    model_plain: RiemannGFM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4635
    metric_stds:
    - 0.1192
  - model: Base (GAT)
    model_plain: Base (GAT)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4605
    metric_stds:
    - 0.0149
  - model: GraphWave
    model_plain: GraphWave
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4596
    metric_stds:
    - 0.022
  - model: GPT-3.5-turbo
    model_plain: GPT-3.5-turbo
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4554
    metric_stds:
    - null
  - model: GPT-4o
    model_plain: GPT-4o
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.4554
    metric_stds:
    - null
  - model: GAE
    model_plain: GAE
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.454
    metric_stds:
    - 0.0999
  - model: Ortho-GCN
    model_plain: Ortho-GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.454
    metric_stds:
    - 0.047
  - model: FA
    model_plain: FA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4533
    metric_stds:
    - 0.0155
  - model: FOSR
    model_plain: FOSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4511
    metric_stds:
    - 0.0147
  - model: GraphCL
    model_plain: GraphCL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4486
    metric_stds:
    - 0.0373
  - model: Base (GCN)
    model_plain: Base (GCN)
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4478
    metric_stds:
    - 0.0145
  - model: CGC
    model_plain: CGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.03670'
    title: 'CDC: A Simple Framework for Complex Data Clustering This work was supported
      by the National Natural Science Foundation of China Grant 62276053. Corresponding
      author: Erlin Pan Z. Kang, X. Xie, B. Li, E. Pan are with the School of Computer
      Science and Engineering, University of Electronic Science and Technology of
      China, Chengdu, China (e-mail: zkang@uestc.edu.cn; x624361380@outlook.com; bingheng86,
      wujisixsix6@gmail.com).'
    date: Mar 2024
    date_iso: 2024-03
    date_display: Mar 2024
    codebase_url: ''
    uses_external_data: null
    is_best: false
    metric_values:
    - 0.446
    metric_stds:
    - null
  - model: DIGL
    model_plain: DIGL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    date_iso: 2025-08
    date_display: Aug 2025
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4446
    metric_stds:
    - 0.0137
  - model: SGSR
    model_plain: SGSR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4432
    metric_stds:
    - 0.0216
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
    - 0.4414
    metric_stds:
    - 0.0127
  - model: STABLE
    model_plain: STABLE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4403
    metric_stds:
    - 0.0405
  - model: gfNN
    model_plain: gfNN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4342
    metric_stds:
    - 0.0122
  - model: KNN w/ sp.-A
    model_plain: KNN w/ sp.-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4318
    metric_stds:
    - 0.065
  - model: GIN
    model_plain: GIN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.429
    metric_stds:
    - 0.046
  - model: NodeFormer
    model_plain: NodeFormer
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.17856'
    title: Graph Structure Refinement with Energy-based Contrastive Learning
    date: Dec 2024
    date_iso: 2024-12
    date_display: Dec 2024
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.427
    metric_stds:
    - 0.0551
  - model: SSGC
    model_plain: SSGC
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08871'
    title: Adapting to Heterophilic Graph Data with Structure-Guided Neighbor Discovery
    date: Jun 2025
    date_iso: 2025-06
    date_display: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4237
    metric_stds:
    - 0.011
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.421
    metric_stds:
    - 0.031
  - model: DeepWalk
    model_plain: DeepWalk
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4121
    metric_stds:
    - 0.034
  - model: N-GCN_a
    model_plain: N-GCN_a
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08676'
    title: 'Redesigning graph filter-based GNNs to relax the homophily assumption
      This work was supported in part by the Spanish AEI Grants PID2022-136887NB-I00,
      PID2023-149457OB-I00, FPU20/05554, the Community of Madrid (Madrid ELLIS Unit),
      and the NSF under award CCF-2340481. Research was sponsored by the Army Research
      Office and was accomplished under Grant Number W911NF-17-S-0002. The views and
      conclusions contained in this document are those of the authors and should not
      be interpreted as representing the official policies, either expressed or implied,
      of the Army Research Office or the U.S. Army or the U.S. Government. The U.S.
      Government is authorized to reproduce and distribute reprints for Government
      purposes notwithstanding any copyright notation herein. Emails: samuel.rey.escudero@urjc.es,
      nav@rice.edu, victor.tenorio@urjc.es, segarra@rice.edu, antonio.garcia.marques@urjc.es'
    date: Sep 2024
    date_iso: 2024-09
    date_display: Sep 2024
    codebase_url: https://github.com/reysam93/adaptive_agg_gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.411
    metric_stds:
    - 0.051
  - model: GMI
    model_plain: GMI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4109
    metric_stds:
    - 0.0524
  - model: ARGVA
    model_plain: ARGVA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4108
    metric_stds:
    - 0.0485
  - model: MDGFM
    model_plain: MDGFM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4077
    metric_stds:
    - 0.0596
  - model: APPNP
    model_plain: APPNP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: Jul 2022
    date_iso: 2022-07
    date_display: Jul 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4054
    metric_stds:
    - null
  - model: Node2Vec
    model_plain: Node2Vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.4054
    metric_stds:
    - 0.0162
  - model: GOFA
    model_plain: GOFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.395
    metric_stds:
    - null
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2211.15081'
    title: Mitigating Overfitting in Graph Neural Networks via Feature and Hyperplane
      Perturbation
    date: Nov 2022
    date_iso: 2022-11
    date_display: Nov 2022
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.394
    metric_stds:
    - 0.043
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
    - 0.3874
    metric_stds:
    - 0.0127
  - model: ProNoG
    model_plain: ProNoG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3718
    metric_stds:
    - 0.1004
  - model: H2GCN
    model_plain: H2GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3558
    metric_stds:
    - 0.1502
  - model: BGRL
    model_plain: BGRL
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.19024'
    title: arXiv:2505.19024
    date: May 2025
    date_iso: 2025-05
    date_display: May 2025
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3515
    metric_stds:
    - 0.1043
  - model: SAGE
    model_plain: SAGE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3255
    metric_stds:
    - 0.1336
  - model: GPR
    model_plain: GPR
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.3077
    metric_stds:
    - 0.1342
  - model: OFA
    model_plain: OFA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2984
    metric_stds:
    - null
  - model: SemiEmb
    model_plain: SemiEmb
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.267
    metric_stds:
    - null
  - model: LP
    model_plain: LP
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.265
    metric_stds:
    - null
  - model: GraphPrompt
    model_plain: GraphPrompt
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2584
    metric_stds:
    - 0.0948
  - model: RolX
    model_plain: RolX
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2567
    metric_stds:
    - 0.1178
  - model: GraphMAE SpikingGPF
    model_plain: GraphMAE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2522
    metric_stds:
    - 0.0722
  - model: EdgePred All-in-One
    model_plain: EdgePred All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2509
    metric_stds:
    - 0.1196
  - model: GraphCL GPF-plus
    model_plain: GraphCL GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2497
    metric_stds:
    - 0.086
  - model: GraphCL SpikingGPF
    model_plain: GraphCL SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.246
    metric_stds:
    - 0.0777
  - model: EdgePred SpikingGPF
    model_plain: EdgePred SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2447
    metric_stds:
    - 0.0467
  - model: GraphMAE GPF
    model_plain: GraphMAE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2435
    metric_stds:
    - 0.0765
  - model: EdgePred GPF
    model_plain: EdgePred GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2422
    metric_stds:
    - 0.0575
  - model: EdgePred Fine-Tuning
    model_plain: EdgePred Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2398
    metric_stds:
    - 0.0663
  - model: LP+FT
    model_plain: LP+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2388
    metric_stds:
    - 0.1143
  - model: GraphMAE GPF-plus
    model_plain: GraphMAE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2385
    metric_stds:
    - 0.0783
  - model: GraphCL GPF
    model_plain: GraphCL GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2373
    metric_stds:
    - 0.0668
  - model: SimGRACE GPF-plus
    model_plain: SimGRACE GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2373
    metric_stds:
    - 0.0891
  - model: struc2vec
    model_plain: struc2vec
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.09025'
    title: Graph Auto-Encoder Via Neighborhood Wasserstein Reconstruction
    date: Feb 2022
    date_iso: 2022-02
    date_display: Feb 2022
    codebase_url: https://github.com/mtang724/NWR-GAE
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2372
    metric_stds:
    - 0.1369
  - model: SimGRACE Fine-Tuning
    model_plain: SimGRACE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2348
    metric_stds:
    - 0.0529
  - model: SimGRACE GPF
    model_plain: SimGRACE GPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2348
    metric_stds:
    - 0.0869
  - model: SimGRACE SpikingGPF
    model_plain: SimGRACE SpikingGPF
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2348
    metric_stds:
    - 0.0343
  - model: EdgePred GPF-plus
    model_plain: EdgePred GPF-plus
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2335
    metric_stds:
    - 0.0836
  - model: GraphMAE Fine-Tuning
    model_plain: GraphMAE Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2323
    metric_stds:
    - 0.0676
  - model: ICA
    model_plain: ICA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.231
    metric_stds:
    - null
  - model: GraphMAE
    model_plain: GraphMAE
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2304
    metric_stds:
    - null
  - model: UniGLM
    model_plain: UniGLM
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.2303
    metric_stds:
    - null
  - model: DGI+FT
    model_plain: DGI+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2289
    metric_stds:
    - 0.1132
  - model: ManiReg
    model_plain: ManiReg
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1609.02907'
    title: Semi-Supervised Classification with Graph Convolutional Networks
    date: Sep 2016
    date_iso: 2016-09
    date_display: Sep 2016
    codebase_url: https://github.com/tkipf/gcn
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.218
    metric_stds:
    - null
  - model: GraphCL All-in-One
    model_plain: GraphCL All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2174
    metric_stds:
    - 0.0777
  - model: GCN
    model_plain: GCN
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2137
    metric_stds:
    - 0.0624
  - model: SimGRACE All-in-One
    model_plain: SimGRACE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2137
    metric_stds:
    - 0.0407
  - model: GAT
    model_plain: GAT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2124
    metric_stds:
    - 0.0467
  - model: GraphCL Fine-Tuning
    model_plain: GraphCL Fine-Tuning
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2124
    metric_stds:
    - 0.045
  - model: GCL+FT
    model_plain: GCL+FT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.14809'
    title: arXiv:2605.14809
    date: May 2026
    date_iso: 2026-05
    date_display: May 2026
    codebase_url: https://github.com/YanJiangJerry/GFMate
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2056
    metric_stds:
    - 0.1336
  - model: GPPT
    model_plain: GPPT
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.2025
    metric_stds:
    - 0.0756
  - model: GraphMAE All-in-One
    model_plain: GraphMAE All-in-One
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.02662'
    title: 'When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph
      Prompt Learning'
    date: Jan 2026
    date_iso: 2026-01
    date_display: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1801
    metric_stds:
    - 0.0476
  - model: Diffusion-A
    model_plain: Diffusion-A
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.12330'
    title: 'Graph as a Feature: A Graph-Aware Non-Neural Model for Node Classification'
    date: Nov 2024
    date_iso: 2024-11
    date_display: Nov 2024
    codebase_url: https://github.com/graph-lr/graph-aware-logistic-regression
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1613
    metric_stds:
    - 0.027
  - model: DGI
    model_plain: DGI
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1466
    metric_stds:
    - null
  - model: LLaGA
    model_plain: LLaGA
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1257
    metric_stds:
    - null
  - model: ZeroG
    model_plain: ZeroG
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: true
    is_best: false
    metric_values:
    - 0.1047
    metric_stds:
    - null
  - model: GraphGPS
    model_plain: GraphGPS
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_iso: '2025-02-17'
    date_display: Feb 2025
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_best: false
    metric_values:
    - 0.1018
    metric_stds:
    - null
  milestones:
  - value: 0.845
    std: null
    model: Planetoid-G/T
    arxiv_id: '1603.08861'
    title: Revisiting Semi-Supervised Learning with Graph Embeddings
    date: '2016-03-29'
  - value: 0.8784
    std: 0.0619
    model: simple GNN model (3-hop)
    arxiv_id: '2105.07634'
    title: Improving Graph Neural Networks with Simple Architecture Design
    date: 2021-05
  - value: 0.8919
    std: null
    model: Our (GCN) vs. GCN
    arxiv_id: '2207.08629'
    title: Comprehensive Graph Gradual Pruning for Sparse Training in Graph Neural
      Networks
    date: 2022-07
  - value: 0.938
    std: 0.015
    model: FMP ode
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: 2023-02
---

