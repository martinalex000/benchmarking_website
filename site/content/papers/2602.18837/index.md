---
title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
arxiv_id: '2602.18837'
authors: []
published_date: Feb 2026
abstract: Despite their theoretical advantages, spectral methods based on the graph
  Fourier transform (GFT) are seldom used in graph neural networks (GNNs) due to the
  cost of computing the eigenbasis and the lack of vertex-domain locality in spectral
  representations. As a result, most GNNs rely on local approximations such as polynomial
  Laplacian filters or message passing, which limit their ability to model long-range
  dependencies. In this paper, we introduce a novel factorization of the GFT into
  operators acting on subgraphs, which are then combined via a sequence of Cauchy
  matrices. We use this factorization to propose a new class of spectral GNNs, which
  we term L2G-Net (Local-to-Global Net). Unlike existing spectral methods, which are
  either fully global (when they use the GFT) or local (when they use polynomial filters),
  L2G-Net operates by processing the spectral representations of subgraphs and then
  combining them via structured matrices. Our algorithm avoids full eigendecompositions,
  exploiting graph topology to construct the factorization with quadratic complexity
  in the number of nodes, scaled by the subgraph interface size. Experiments on benchmarks
  stressing non-local dependencies show that L2G-Net outperforms existing spectral
  techniques and is competitive with the state-of-the-art with orders of magnitude
  fewer learnable parameters.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- Ours
mrr: 0.1299
results:
- &id003
  dataset: Amazon-ratings
  rows:
  - model: GENs
    value: 0.5592
    std: 0.0043
    metric: Accuracy
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
    global_rank: 1
    is_best: true
  - model: GraphSAGE
    value: 0.554
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: Polynormer
    value: 0.5481
    std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: NeuralWalker
    value: 0.5458
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: CO-GNN($\mu$, $\mu$)
    value: 0.5417
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GMN
    value: 0.5407
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: MP-SSM
    value: 0.5365
    std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: SAGE
    value: 0.5363
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: Exphormer
    value: 0.5351
    std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: GRAMA
    value: 0.5348
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: Ours
    value: 0.5341
    std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: Stable-ChebNet
    value: 0.5315
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GPS
    value: 0.531
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: FSGNN
    value: 0.5274
    std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: GAT-sep
    value: 0.5218
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: CO-GNN($\Sigma$, $\Sigma$)
    value: 0.5128
    std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: Nagphormer
    value: 0.5126
    std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: GT
    value: 0.5117
    std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: GAT
    value: 0.4909
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GCN
    value: 0.487
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 9
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: Gated + RWSE
    value: 0.4858
    std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 57
    is_best: false
  - model: GPSGCN+Performer (LapPE)
    value: 0.482
    std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GPS₃₂GCN+Performer (RWSE)
    value: 0.4808
    std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: R-GCN (RWSE)
    value: 0.464
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: GBK-GNN
    value: 0.4598
    std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 71
    is_best: false
  - model: GPS + Mamba
    value: 0.4513
    std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: GAT (LapPE)
    value: 0.449
    std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: GPR-GNN
    value: 0.4488
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GOAT
    value: 0.4461
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GCN+LapPE
    value: 0.4435
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 9
    source_ref: this paper
    global_rank: 77
    is_best: false
  - model: FAGCN
    value: 0.4412
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 78
    is_best: false
  - model: JacobiConv
    value: 0.4355
    std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 80
    is_best: false
  - model: GatedGCN
    value: 0.43
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 9
    source_ref: this paper
    global_rank: 61
    is_best: false
  - model: CPGNN
    value: 0.3979
    std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 87
    is_best: false
  - model: GLoGNN
    value: 0.3689
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 89
    is_best: false
  - model: H2GCN
    value: 0.3647
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 90
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Minesweeper
  rows:
  - model: CSNN
    value: 0.9906999999999999
    std: 0.0025
    metric: ROC-AUC
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
    global_rank: 1
    is_best: true
  - model: BuNN
    value: 0.9899
    std: 0.0016
    metric: ROC-AUC
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
    global_rank: 2
    is_best: true
  - model: Tango\textsubscript{GPS}
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: Ours
    value: 0.975
    std: 0.0026
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: Polynormer
    value: 0.9746
    std: 0.0036
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: CO-GNN($\mu$, $\mu$)
    value: 0.9731
    std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: Stable-ChebNet
    value: 0.9571
    std: 0.0226
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: MP-SSM
    value: 0.9533
    std: 0.0072
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: GRAMA$_{GCN}$
    value: 0.9527
    std: 0.0071
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: CO-GNN($\Sigma$, $\Sigma$)
    value: 0.9509
    std: 0.0118
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GCN+LapPE
    value: 0.9426
    std: 0.0049
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 9
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: GPSGCN+Performer (LapPE)
    value: 0.9385
    std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: R-GCN (RWSE)
    value: 0.9384
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: SAGE
    value: 0.9351
    std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 39
    is_best: false
  - model: GAT (LapPE)
    value: 0.935
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: GPS₃₂GCN+Performer (RWSE)
    value: 0.9288
    std: 0.005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: Gated + RWSE
    value: 0.9253
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: GAT-sep
    value: 0.9229
    std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: GAT
    value: 0.9201
    std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GT
    value: 0.9185
    std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GPSGCN+Transformer (LapPE)
    value: 0.9182
    std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: GPSGCN+Transformer (RWSE)
    value: 0.9117
    std: 0.0051
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 59
    is_best: false
  - model: GMN
    value: 0.9101
    std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: GBK-GNN
    value: 0.9085
    std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: Exphormer
    value: 0.9074
    std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GPS
    value: 0.9063
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 68
    is_best: false
  - model: FSGNN
    value: 0.9008
    std: 0.007
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: GPS + Mamba
    value: 0.8993
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GCN
    value: 0.8975
    std: 0.0052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 9
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: H2GCN
    value: 0.8971
    std: 0.0031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 77
    is_best: false
  - model: JacobiConv
    value: 0.8966
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 79
    is_best: false
  - model: FAGCN
    value: 0.8817
    std: 0.0073
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 82
    is_best: false
  - model: GatedGCN
    value: 0.8754
    std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 9
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: GPR-GNN
    value: 0.8624
    std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 84
    is_best: false
  - model: Nagphormer
    value: 0.8419
    std: 0.0066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: GOAT
    value: 0.8109
    std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 88
    is_best: false
  - model: CPGNN
    value: 0.5203
    std: 0.0546
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 92
    is_best: false
  - model: GLoGNN
    value: 0.5108
    std: 0.0123
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 93
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id001
  dataset: Roman-empire
  rows:
  - model: NeuralWalker
    value: 0.9292
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with , Rewiring, and Attention'
    date: Jul 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: CSNN
    value: 0.9262999999999999
    std: 0.005
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
    global_rank: 3
    is_best: true
  - model: Polynormer
    value: 0.9255
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GENs
    value: 0.9251999999999999
    std: 0.005
    metric: Accuracy
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
    global_rank: 4
    is_best: true
  - model: Ours
    value: 0.9212
    std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 5
    is_best: true
  - model: Stable-ChebNet
    value: 0.9203
    std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 7
    is_best: true
  - model: CO-GNN($\Sigma$, $\Sigma$)
    value: 0.9157
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: CO-GNN($\mu$, $\mu$)
    value: 0.9137
    std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: MP-SSM
    value: 0.9091
    std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: Exphormer
    value: 0.8903
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: GRAMA
    value: 0.8861
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 31
    is_best: false
  - model: GMN
    value: 0.8769
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: GAT-sep
    value: 0.8732
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 30
    is_best: false
  - model: Gated + RWSE
    value: 0.8662
    std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: GT
    value: 0.8651
    std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: SAGE
    value: 0.8574
    std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: R-GCN (RWSE)
    value: 0.8484
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GAT (LapPE)
    value: 0.848
    std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 50
    is_best: false
  - model: GPS₃₂GCN+Performer (RWSE)
    value: 0.8472
    std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 51
    is_best: false
  - model: GPSGCN+Performer (LapPE)
    value: 0.8396
    std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: GCN+LapPE
    value: 0.8337
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 9
    source_ref: this paper
    global_rank: 59
    is_best: false
  - model: GPS + Mamba
    value: 0.831
    std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 61
    is_best: false
  - model: GPS
    value: 0.82
    std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: GAT
    value: 0.8087
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: FSGNN
    value: 0.7992
    std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 71
    is_best: false
  - model: GBK-GNN
    value: 0.7457
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GatedGCN
    value: 0.7446
    std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 9
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: Nagphormer
    value: 0.7434
    std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: GCN
    value: 0.7369
    std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 9
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: GOAT
    value: 0.7159
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 78
    is_best: false
  - model: JacobiConv
    value: 0.7114
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 79
    is_best: false
  - model: FAGCN
    value: 0.6522
    std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 83
    is_best: false
  - model: GPR-GNN
    value: 0.6485
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 84
    is_best: false
  - model: CPGNN
    value: 0.6396
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 85
    is_best: false
  - model: H2GCN
    value: 0.6011
    std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 86
    is_best: false
  - model: GLoGNN
    value: 0.5963
    std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 90
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Tolokers
  rows:
  - model: GRAMA$_{GCN}$
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GRAMA
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
  - model: Polynormer
    value: 0.8591
    std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: IM-CO-GNN(μ,μ)
    value: 0.8577
    std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: Tango\textsubscript{GPS}
    value: 0.8565999999999999
    std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: true
  - model: Ours
    value: 0.8557
    std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 6
    is_best: true
  - model: Stable-ChebNet
    value: 0.8555
    std: 0.0335
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 8
    is_best: true
  - model: MP-SSM
    value: 0.8526
    std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 12
    is_best: true
  - model: R-GCN (RWSE)
    value: 0.8511
    std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 17
    is_best: true
  - model: Gated + RWSE
    value: 0.8502
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 20
    is_best: true
  - model: GAT (LapPE)
    value: 0.8499
    std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 21
    is_best: true
  - model: GCN+LapPE
    value: 0.8495
    std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501066
    table_ref: Table 9
    source_ref: this paper
    global_rank: 22
    is_best: true
  - model: GPS₃₂GCN+Performer (RWSE)
    value: 0.8481
    std: 0.0086
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 25
    is_best: true
  - model: GPSGCN+Performer (LapPE)
    value: 0.8472
    std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 29
    is_best: true
  - model: GMN
    value: 0.8452
    std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: CO-GNN($\mu$, $\mu$)
    value: 0.8445
    std: 0.0117
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 35
    is_best: true
  - model: Exphormer
    value: 0.8377
    std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: GPS
    value: 0.8371
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: GAT
    value: 0.837
    std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 45
    is_best: false
  - model: GPS + Mamba
    value: 0.837
    std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GCN
    value: 0.8364
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 9
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GPSGCN+Transformer (RWSE)
    value: 0.8353
    std: 0.0106
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: GPSGCN+Transformer (LapPE)
    value: 0.8351
    std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: CO-GNN($\Sigma$, $\Sigma$)
    value: 0.8336
    std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 50
    is_best: false
  - model: GT
    value: 0.8323
    std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GOAT
    value: 0.8311
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: FSGNN
    value: 0.8276
    std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 55
    is_best: false
  - model: GAT-sep
    value: 0.8252
    std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: SAGE
    value: 0.8243
    std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: GBK-GNN
    value: 0.8101
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: Nagphormer
    value: 0.7832
    std: 0.0095
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: FAGCN
    value: 0.7775
    std: 0.0105
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 66
    is_best: false
  - model: GatedGCN
    value: 0.7731
    std: 0.0114
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 9
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: GLoGNN
    value: 0.7339
    std: 0.0117
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: CPGNN
    value: 0.7336
    std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 71
    is_best: false
  - model: H2GCN
    value: 0.7335
    std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: GPR-GNN
    value: 0.7294
    std: 0.0097
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: JacobiConv
    value: 0.6866
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 9
    source_ref: this paper
    global_rank: 75
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
single_proposed_model: Ours
main_figure: /figures/2602.18837/main_figure.png
---

