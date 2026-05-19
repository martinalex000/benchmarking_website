---
title: Cayley Graph Propagation
arxiv_id: '2410.03424'
authors: []
published_date: Oct 2024
abstract: In spite of the plethora of success stories with graph neural networks (GNNs)
  on modelling graph-structured data, they are notoriously vulnerable to over-squashing,
  whereby tasks necessitate the mixing of information between distance pairs of nodes.
  To address this problem, prior work suggests rewiring the graph structure to improve
  information flow. Alternatively, a significant body of research has dedicated itself
  to discovering and precomputing bottleneck-free graph structures to ameliorate over-squashing.
  One well regarded family of bottleneck-free graphs within the mathematical community
  are expander graphs, with prior work—Expander Graph Propagation (EGP)—proposing
  the use of a well-known expander graph family—the Cayley graphs of the $SL(2,Z_n)$
  special linear group—as a computational template for GNNs. However, in EGP the computational
  graphs used are truncated to align with a given input graph. In this work, we show
  that truncation is detrimental to the coveted expansion properties. Instead, we
  propose CGP, a method to propagate information over a complete Cayley graph structure,
  thereby ensuring it is bottleneck-free to better alleviate over-squashing. Our empirical
  evidence across several real-world datasets not only shows that CGP recovers significant
  improvements as compared to EGP, but it is also akin to or outperforms computationally
  complex graph rewiring techniques.
codebase_url: ''
extraction_model: Kimi-K2.6
has_results: true
proposed_models:
- GCN + CGP
- GIN + CGP
mrr: 0.0105
results:
- &id002
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    value: 0.8722
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: nsqure~
    value: 0.8672
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: CoCN
    value: 0.8615
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GIN + CGP
    value: 0.7335
    std: 0.00788
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: GCN + PANDA
    value: 0.7332
    std: 0.00814
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: GIN-SDRF-R
    value: 0.72958
    std: 0.00419
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
  - model: GIN + FA
    value: 0.7274
    std: 0.00786
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: GCN + GTR
    value: 0.726
    std: 0.01025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 57
    is_best: false
  - model: EGP (GIN)
    value: 0.7233
    std: 0.00954
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
  - model: FAGCN
    value: 0.72039
    std: 0.00771
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
  - model: GIN + GTR
    value: 0.71849
    std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: GIN-FOSR-R
    value: 0.7172
    std: 0.00892
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 71
    is_best: false
  - model: GIN
    value: 0.7149
    std: 0.00746
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
  - model: GCN + SDRF
    value: 0.7133
    std: 0.00807
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GCN
    value: 0.7049
    std: 0.01628
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
  - model: GCN + CGP
    value: 0.6963
    std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 81
    is_best: false
  - model: EGP (GCN)
    value: 0.6947
    std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 82
    is_best: false
  - model: GCN + FoSR
    value: 0.6722
    std: 0.01367
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
  - model: GCN + DIGL
    value: 0.5762
    std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 92
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    value: 0.854
    std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: PR-MPNN
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Networks
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: EGP (GCN)
    value: 0.73304
    std: 0.02516
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 108
    is_best: false
  - model: GIN + CGP
    value: 0.7308
    std: 0.01396
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 115
    is_best: false
  - model: GCN + CGP
    value: 0.73036
    std: 0.01291
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 116
    is_best: false
  - model: GCN + GTR
    value: 0.72991
    std: 0.01956
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 121
    is_best: false
  - model: GIN + FA
    value: 0.72902
    std: 0.01419
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 122
    is_best: false
  - model: GCN + DIGL
    value: 0.72321
    std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 137
    is_best: false
  - model: GCN + PANDA
    value: 0.72321
    std: 0.01786
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
  - model: GIN + GTR
    value: 0.72054
    std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 111
    is_best: false
  - model: GIN-FOSR-R
    value: 0.71518
    std: 0.01767
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 114
    is_best: false
  - model: FAGCN
    value: 0.71071
    std: 0.01506
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 162
    is_best: false
  - model: EGP (GIN)
    value: 0.70848
    std: 0.01568
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 168
    is_best: false
  - model: GCN + FoSR
    value: 0.70848
    std: 0.01618
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
  - model: GCN + BORF
    value: 0.70625
    std: 0.00017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 82
    is_best: false
  - model: GIN
    value: 0.70312
    std: 0.01749
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
  - model: GIN-SDRF-R
    value: 0.69509
    std: 0.01709
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 124
    is_best: false
  - model: GCN + SDRF
    value: 0.67277
    std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 123
    is_best: false
  - model: GCN
    value: 0.66652
    std: 0.01933
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 37
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: GIN + CGP
    value: 0.7899
    std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: GCN + CGP
    value: 0.7794
    std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 96
    is_best: false
  - model: EGP (GCN)
    value: 0.7731
    std: 0.0081
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 106
    is_best: false
  - model: GIN + FA
    value: 0.7718
    std: 0.0147
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 111
    is_best: false
  - model: GIN
    value: 0.7678
    std: 0.0183
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: FAGCN
    value: 0.7628
    std: 0.0191
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 135
    is_best: false
  - model: GCN + Master Node
    value: 0.7608
    std: 0.0134
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 137
    is_best: false
  - model: GCN
    value: 0.7566
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: EGP (GIN)
    value: 0.7537
    std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 148
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
  dataset: ogbg-molpcba
  rows:
  - model: EGP (GCN)
    value: 0.6821
    std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: GCN + CGP
    value: 0.6782
    std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: GIN + CGP
    value: 0.6562
    std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: EGP (GIN)
    value: 0.6533
    std: 0.119
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: GCN + Master Node
    value: 0.6069
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GIN
    value: 0.5888
    std: 0.0441
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: GCN
    value: 0.5483
    std: 0.0209
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table OGB
    source_ref: this paper
    global_rank: 39
    is_best: false
  - model: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
  - model: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
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
    global_rank: 2
    is_best: false
  - model: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
- benchmark: OGB
  datasets:
  - *id003
  - *id004
main_figure: /figures/2410.03424/main_figure.png
---

