---
title: When Graph Neural Networks Meet Dynamic Mode Decomposition
arxiv_id: '2410.05593'
authors: []
published_date: Oct 2024
abstract: Graph Neural Networks (GNNs) have emerged as fundamental tools for a wide
  range of prediction tasks on graph-structured data. Recent studies have drawn analogies
  between GNN feature propagation and diffusion processes, which can be interpreted
  as dynamical systems. In this paper, we delve deeper into this perspective by connecting
  the dynamics in GNNs to modern Koopman theory and its numerical method, Dynamic
  Mode Decomposition (DMD). We illustrate how DMD can estimate a low-rank, finite-dimensional
  linear operator based on multiple states of the system, effectively approximating
  potential nonlinear interactions between nodes in the graph. This approach allows
  us to capture complex dynamics within the graph accurately and efficiently. We theoretically
  establish a connection between the DMD-estimated operator and the original dynamic
  operator between system states. Building upon this foundation, we introduce a family
  of DMD-GNN models that effectively leverage the low-rank eigenfunctions provided
  by the DMD algorithm. We further discuss the potential of enhancing our approach
  by incorporating domain-specific constraints such as symmetry into the DMD computation,
  allowing the corresponding GNN models to respect known physical properties of the
  underlying system. Our work paves the path for applying advanced dynamical system
  analysis tools via GNNs. We validate our approach through extensive experiments
  on various learning tasks, including directed graphs, large-scale graphs, long-range
  interactions, and spatial-temporal graphs. We also empirically verify that our proposed
  models can serve as powerful encoders for link prediction tasks. The results demonstrate
  that our DMD-enhanced GNNs achieve state-of-the-art performance, highlighting the
  effectiveness of integrating DMD into GNN frameworks.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- DMD-GCN
- DMD-SGC
- DMD++
- DMD-ACMP
mrr: 0.0232
results:
- &id008
  dataset: COCO-SP
  rows:
  - model: FloydNet
    value: 0.4901
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GRASS
    value: 0.4752
    std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: DMD++
    value: 0.091
    std: 0.009
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: DMD-SGC
    value: 0.083
    std: 0.012
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 75
    is_best: false
  - model: DMD-GCN
    value: 0.081
    std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GCN
    value: 0.079
    std: 0.025
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: SGC
    value: 0.056
    std: 0.011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 78
    is_best: false
  - model: GPRGNN
    value: 0.044
    std: 0.015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 79
    is_best: false
  - model: MLP
    value: 0.031
    std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb
    source_ref: this paper
    global_rank: 82
    is_best: false
  metric: F1
  higher_is_better: true
- &id010
  dataset: COVID
  rows:
  - model: DualEquiNet
    value: 0.353
    std: 0.006
    metric: RMSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: w/o CSIP
    value: 0.356
    std: 0.002
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: w/o CSIP/Cross
    value: 0.356
    std: 0.013
    metric: RMSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.19862'
    title: DualEquiNet RNA Benchmarks
    date: Jun 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DMD-GCN
    value: 0.76
    std: 0.025
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMD++
    value: 0.784
    std: 0.013
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMD-SGC
    value: 0.805
    std: 0.067
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DMD-ACMP
    value: 0.809
    std: 0.011
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GAT-kNN
    value: 0.861
    std: 0.045
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Framelets
    value: 0.938
    std: 0.081
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN
    value: 0.956
    std: 0.029
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: MLP
    value: 0.956
    std: 0.034
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: ChebNet
    value: 0.991
    std: 0.078
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GAT
    value: 1.052
    std: 0.081
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GRAND
    value: 1.271
    std: 0.073
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN-kNN
    value: 1.475
    std: 0.028
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table stg_main_results
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: RMSE
  higher_is_better: false
- &id005
  dataset: CiteSeer
  rows:
  - model: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: APPNP
    value: 0.759
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: GPRGNN
    value: 0.759
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: DMD++
    value: 0.732
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 110
    is_best: false
  - model: H2GCN
    value: 0.731
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: DMD-ACMP
    value: 0.73
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 112
    is_best: false
  - model: DMD-SGC
    value: 0.726
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 114
    is_best: false
  - model: GAT
    value: 0.72
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: DMD-GCN
    value: 0.714
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 125
    is_best: false
  - model: Framelets
    value: 0.71
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 129
    is_best: false
  - model: GCN
    value: 0.709
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GRAND
    value: 0.708
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 130
    is_best: false
  - model: SAGE
    value: 0.672
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 134
    is_best: false
  - model: MLP
    value: 0.591
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 31
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Cora
  rows:
  - model: GPM
    value: 0.9285
    std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: TRIGON
    value: 0.9170999999999999
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: DR
    value: 0.9139
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.19071'
    title: Dynamic Triangulation-Based Graph Rewiring for Graph Neural Networks
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: DMD-SGC
    value: 0.841
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 113
    is_best: false
  - model: GPRGNN
    value: 0.838
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: APPNP
    value: 0.835
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: H2GCN
    value: 0.834
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: Framelets
    value: 0.833
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 125
    is_best: false
  - model: GAT
    value: 0.83
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: GRAND
    value: 0.829
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 132
    is_best: false
  - model: DMD-ACMP
    value: 0.829
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 133
    is_best: false
  - model: DMD-GCN
    value: 0.826
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 136
    is_best: false
  - model: DMD++
    value: 0.823
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 142
    is_best: false
  - model: GCN
    value: 0.815
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 50
    is_best: false
  - model: SAGE
    value: 0.745
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 119
    is_best: false
  - model: MLP
    value: 0.551
    std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ACMGCN
    value: 0.9393
    std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: ACM-SGC-1
    value: 0.9377
    std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DMD++
    value: 0.914
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: MLP
    value: 0.913
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: APPNP
    value: 0.898
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: DMD-ACMP
    value: 0.881
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: H2GCN
    value: 0.851
    std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: GPRGNN
    value: 0.85
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: DMD-GCN
    value: 0.836
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: DMD-SGC
    value: 0.8
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: GAT
    value: 0.76
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: GRAND
    value: 0.756
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 38
    is_best: false
  - model: Framelets
    value: 0.726
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: SAGE
    value: 0.714
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: GCN
    value: 0.665
    std: 0.138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 27
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: PascalVOC-SP
  rows:
  - model: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: DMD-GCN
    value: 0.243
    std: 0.014
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 87
    is_best: false
  - model: DMD++
    value: 0.241
    std: 0.017
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 88
    is_best: false
  - model: GCN
    value: 0.238
    std: 0.016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: DMD-SGC
    value: 0.217
    std: 0.036
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 90
    is_best: false
  - model: SGC
    value: 0.216
    std: 0.039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 91
    is_best: false
  - model: GPRGNN
    value: 0.152
    std: 0.024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 101
    is_best: false
  - model: MLP
    value: 0.114
    std: 0.023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 108
    is_best: false
  metric: F1
  higher_is_better: true
- &id006
  dataset: PubMed
  rows:
  - model: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: ND
    value: 0.9256
    std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: DMD-ACMP
    value: 0.812
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 114
    is_best: false
  - model: DMD++
    value: 0.799
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 117
    is_best: false
  - model: GPRGNN
    value: 0.798
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: Framelets
    value: 0.794
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 118
    is_best: false
  - model: DMD-SGC
    value: 0.794
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 119
    is_best: false
  - model: DMD-GCN
    value: 0.793
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 120
    is_best: false
  - model: H2GCN
    value: 0.792
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: GRAND
    value: 0.792
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 55
    is_best: false
  - model: GCN
    value: 0.79
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: APPNP
    value: 0.79
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: GAT
    value: 0.785
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: SAGE
    value: 0.768
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 126
    is_best: false
  - model: MLP
    value: 0.714
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Texas
  rows:
  - model: ACMGCN
    value: 0.9656
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DMD++
    value: 0.926
    std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 12
    is_best: true
  - model: MLP
    value: 0.923
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: DMD-ACMP
    value: 0.894
    std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: H2GCN
    value: 0.859
    std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: DMD-GCN
    value: 0.842
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: APPNP
    value: 0.839
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: Framelets
    value: 0.823
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 50
    is_best: false
  - model: GRAND
    value: 0.814
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: DMD-SGC
    value: 0.812
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: SAGE
    value: 0.793
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 62
    is_best: false
  - model: GAT
    value: 0.788
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: GPRGNN
    value: 0.759
    std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: GCN
    value: 0.757
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 44
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Wisconsin
  rows:
  - model: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: CSNN
    value: 0.9
    std: 0.028300000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: GPRGNN
    value: 0.899
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: true
  - model: O(d)-NSD
    value: 0.8941
    std: 0.047400000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    is_best: true
  - model: DMD-ACMP
    value: 0.894
    std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: true
  - model: Gen-NSD
    value: 0.8920999999999999
    std: 0.0384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    is_best: true
  - model: Framelets
    value: 0.889
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: true
  - model: GRAND
    value: 0.886
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: true
  - model: H2GCN
    value: 0.879
    std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: true
  - model: DMD-GCN
    value: 0.852
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: DMD-SGC
    value: 0.83
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GAT
    value: 0.71
    std: 0.046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GCN
    value: 0.667
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: SAGE
    value: 0.648
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 75
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: DMD-ACMP
    value: 0.755
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: DMD++
    value: 0.744
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: true
  - model: GRAND
    value: 0.741
    std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: true
  - model: DMD-SGC
    value: 0.741
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: DMD-GCN
    value: 0.739
    std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: true
  - model: H2GCN
    value: 0.728
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: GCN
    value: 0.727
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GAT
    value: 0.72
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: Framelets
    value: 0.719
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 59
    is_best: false
  - model: SAGE
    value: 0.706
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GPRGNN
    value: 0.704
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 75
    is_best: false
  - model: APPNP
    value: 0.703
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: MLP
    value: 0.55
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 91
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Classic
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
- benchmark: OGB
  datasets:
  - *id009
- benchmark: DualEquiNet RNA Benchmarks
  datasets:
  - *id010
main_figure: /figures/2410.05593/main_figure.png
---

