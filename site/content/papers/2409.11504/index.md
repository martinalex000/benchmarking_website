---
title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
  Graph
arxiv_id: '2409.11504'
authors: []
published_date: Sep 2024
abstract: The ability of message-passing neural networks (MPNNs) to fit complex functions
  over graphs is limited as most graph convolutions amplify the same signal across
  all feature channels, a phenomenon known as rank collapse, and over-smoothing as
  a special case. Most approaches to mitigate over-smoothing extend common message-passing
  schemes, e.g., the graph convolutional network, by utilizing residual connections,
  gating mechanisms, normalization, or regularization techniques. Our work contrarily
  proposes to directly tackle the cause of this issue by modifying the message-passing
  scheme and exchanging different types of messages using multi-relational graphs.
  We identify a sufficient condition to ensure linearly independent node representations.
  As one instantion, we show that operating on multiple directed acyclic graphs always
  satisfies our condition and propose to obtain these by defining a strict partial
  ordering of the nodes. We conduct comprehensive experiments that confirm the benefits
  of operating on multi-relational graphs to achieve more informative node representations.
codebase_url: ''
extraction_model: Kimi-K2.6
has_results: true
proposed_models:
- MRS-GCN_DA (random)
- MRS-GCN_DA (Features)
- MRS-GCN_DA (PPR)
- MRS-GCN_DA (Degree)
- MRS-GCN_DA
- MRS-SAGE_DA
- MRS-GAT_DA
- MRS-GatedGCN_DA
- MRS-Dir-GCN_DA
mrr: 0.006
results:
- &id002
  dataset: Chameleon
  rows:
  - model: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: Dir-GNN
    value: 0.7971
    std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 4
    is_best: true
  - model: Sp$^2$GCL
    value: 0.7888
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    is_best: true
  - model: FSGNN
    value: 0.7827
    std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 6
    is_best: true
  - model: ACMGCN
    value: 0.7476
    std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 10
    is_best: false
  - model: Grad. Gating
    value: 0.714
    std: 0.0238
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 19
    is_best: false
  - model: GLoGNN
    value: 0.7121
    std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 20
    is_best: false
  - model: LINKX
    value: 0.6842
    std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 25
    is_best: false
  - model: GCN
    value: 0.6482
    std: 0.0224
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 43
    is_best: false
  - model: GPR-GNN
    value: 0.6285
    std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 48
    is_best: false
  - model: H_2GCN
    value: 0.5939
    std: 0.0198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 67
    is_best: false
  - model: MagNet
    value: 0.5822
    std: 0.0287
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 73
    is_best: false
  - model: DiGCN
    value: 0.5224
    std: 0.0365
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 89
    is_best: false
  - model: MLP
    value: 0.4621
    std: 0.0299
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi 2023
    global_rank: 102
    is_best: false
  metric: Accuracy
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
  - model: Polynormer
    value: 0.9266
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
  - model: MRS-Dir-GCN_DA
    value: 0.9187
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: Dir-GNN
    value: 0.9123
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 20
    is_best: false
  - model: MagNet
    value: 0.8807
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 33
    is_best: false
  - model: Grad. Gating
    value: 0.8216
    std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 63
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 71
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 18
    is_best: false
  - model: ACMGCN
    value: 0.6966
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 80
    is_best: false
  - model: MLP
    value: 0.6494
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 81
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 84
    is_best: false
  - model: H_2GCN
    value: 0.6011
    std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 88
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
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 90
    is_best: false
  - model: DiGCN
    value: 0.5271
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 92
    is_best: false
  - model: LINKX
    value: 0.3755
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 100
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Squirrel
  rows:
  - model: MRS-Dir-GCN_DA
    value: 0.7601
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: Dir-GNN
    value: 0.7531
    std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: FSGNN
    value: 0.741
    std: 0.0189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: GraphMAE
    value: 0.7205
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: Supervised
    value: 0.7191
    std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: ACMII-GCN
    value: 0.6998
    std: 0.0153
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
    global_rank: 6
    is_best: false
  - model: ACMGCN
    value: 0.674
    std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: Grad. Gating
    value: 0.6426
    std: 0.0238
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: LINKX
    value: 0.6181
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GLoGNN
    value: 0.5788
    std: 0.0176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GPR-GNN
    value: 0.5435
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: GCN
    value: 0.5343
    std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: MagNet
    value: 0.3901
    std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 75
    is_best: false
  - model: H_2GCN
    value: 0.379
    std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 82
    is_best: false
  - model: DiGCN
    value: 0.3774
    std: 0.0154
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 86
    is_best: false
  - model: MLP
    value: 0.2877
    std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table~\ref{tab:hetero}
    source_ref: this paper
    global_rank: 88
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: ZINC
  rows:
  - model: ESA
    value: 0.010894100678479495
    std: 0.00022839903839981288
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: MRS-GatedGCN_DA
    value: 0.088
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 147
    is_best: false
  - model: GatedGCN
    value: 0.099
    std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 116
    is_best: false
  - model: MRS-GCN_DA
    value: 0.106
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 166
    is_best: false
  - model: MRS-SAGE_DA
    value: 0.106
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 167
    is_best: false
  - model: GIN
    value: 0.123
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: SAGE
    value: 0.123
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 186
    is_best: false
  - model: MRS-GAT_DA
    value: 0.128
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 190
    is_best: false
  - model: GAT
    value: 0.149
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:zinc_full
    source_ref: this paper
    global_rank: 124
    is_best: false
  - model: GCN
    value: 0.155
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 115
    is_best: false
  - model: MRS-GCN_DA (Degree)
    value: 0.318
    std: 0.031
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 247
    is_best: false
  - model: MRS-GCN_DA (PPR)
    value: 0.358
    std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 253
    is_best: false
  - model: MRS-GCN_DA (Features)
    value: 0.39
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 259
    is_best: false
  - model: MRS-GCN_DA (random)
    value: 0.623
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 271
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: snap-patents
  rows:
  - model: MRS-Dir-GCN_DA
    value: 0.7472
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: Dir-GNN
    value: 0.7395
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Rossi et al. 2023
    global_rank: 2
    is_best: false
  - model: LargeGT-full
    value: 0.7021
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: Grad. Gating
    value: 0.695
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: LargeGT-local
    value: 0.6819
    std: 0.0311
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: FSGNN
    value: 0.6507
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GLoGNN
    value: 0.6209
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: LINKX
    value: 0.6195
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: Nagphormer
    value: 0.6011
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.11109'
    title: Graph Transformers for Large Graphs
    date: Dec 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    is_best: false
  - model: ACMGCN
    value: 0.5514
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCN
    value: 0.5102
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: GPR-GNN
    value: 0.4019
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: MLP
    value: 0.3134
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 22
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
- benchmark: LINKX Benchmarks
  datasets:
  - *id005
main_figure: /figures/2409.11504/main_figure.png
---

