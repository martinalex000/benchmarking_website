---
title: Enhancing the Utility of Higher-Order Information Relational Learning
arxiv_id: '2502.09570'
authors: []
published_date: Feb 2025
abstract: Higher-order information is crucial for relational learning in many domains
  where relationships extend beyond pairwise interactions. Hypergraphs provide a natural
  framework for modeling such relationships, which has motivated recent extensions
  of graph neural network architectures to hypergraphs. However, comparisons between
  hypergraph architectures and standard graph-level models remain limited. In this
  work, we systematically evaluate a selection of hypergraph-level and graph-level
  architectures, to determine their effectiveness in leveraging higher-order information
  in relational learning. Our results show that graph-level architectures applied
  to hypergraph expansions often outperform hypergraph-level ones, even on inputs
  that are naturally parametrized as hypergraphs. As an alternative approach for leveraging
  higher-order information, we propose hypergraph-level encodings based on classical
  hypergraph characteristics. While these encodings do not significantly improve hypergraph
  architectures, they yield substantial performance gains when combined with graph-level
  models. Our theoretical analysis shows that hypergraph-level encodings provably
  increase the representational power of message-passing graph neural networks beyond
  that of their graph-level counterparts.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- UniGAT (HCP-FRC)
- UniGAT (LDP)
- UniGAT (Hodge H-20-LAPE)
- UniGAT (Norm. H-20-LAPE)
- UniGAT (H-19-RWPEE EE)
- UniGAT (H-19-RWPEE WE)
- UniGAT (no encodings nlayer2)
- UniGCN (HCP-FRC)
- UniGCN (LDP)
- UniGCN (H-19-RWPEE EN)
- UniGCN (no encodings)
- UniSAGE (HCP-FRC)
- UniSAGE (LDP)
- UniSAGE (no encodings)
- UniGCNII (HCP-FRC depth 2)
- UniGCNII (LDP depth 2)
- UniGCNII (Hodge H-20-LAPE depth 2)
- UniGCNII (Norm. H-20-LAPE depth 2)
- UniGCNII (H-19-RWPEE EE depth 2)
- UniGCNII (no encodings depth 2)
- UniGCNII (H-19-RWPEE WE depth 8)
- GCN (LCP-FRC)
- GCN (LCP-ORC)
- GCN (19-RWPE)
- GCN (20-LAPE)
- GCN (EE H-19-RWPE)
- GCN (Hodge H-20-LAPE)
- GCN (Norm. H-20-LAPE)
- GPS (LCP-FRC)
- GPS (LCP-ORC)
- GPS (19-RWPE)
- GPS (20-LAPE)
- GPS (EN H-19-RWPE)
mrr: 0.0052
results:
- &id010
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
  - model: GPS (EN H-19-RWPE)
    value: 0.7592
    std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.7474
    std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.7429
    std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.7418
    std: 0.0122
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GPS (No Encoding)
    value: 0.7417
    std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: GPS (LCP-FRC)
    value: 0.7337
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GCN (LCP-ORC)
    value: 0.726
    std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 55
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.7232
    std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 59
    is_best: false
  - model: GIN (HCP-ORC)
    value: 0.7218
    std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.7216
    std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 61
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.7196
    std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.7195
    std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 68
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.7176
    std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.7152
    std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: GIN (HCP-FRC)
    value: 0.7144
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: GCN (No Encoding)
    value: 0.6744
    std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 89
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.6538
    std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 161
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.6538
    std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 162
    is_best: false
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.6525
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 163
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    value: 0.6524
    std: 0.0167
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 164
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.652
    std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 165
    is_best: false
  - model: UniGCNII (LDP depth 2)
    value: 0.636
    std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 174
    is_best: false
  - model: UniGAT (no encodings nlayer2)
    value: 0.6325
    std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 175
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    value: 0.6293
    std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 177
    is_best: false
  - model: UniGAT (LDP)
    value: 0.6207
    std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 181
    is_best: false
  - model: UniGAT (HCP-FRC)
    value: 0.6108
    std: 0.0185
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 185
    is_best: false
  - model: UniGCN (no encodings)
    value: 0.6056
    std: 0.0231
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 187
    is_best: false
  - model: UniSAGE (no encodings)
    value: 0.6056
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 188
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    value: 0.6055
    std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 189
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    value: 0.6054
    std: 0.0219
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 190
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    value: 0.603
    std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 192
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    value: 0.6029
    std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 193
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    value: 0.6022
    std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 194
    is_best: false
  - model: UniSAGE (LDP)
    value: 0.5997
    std: 0.0227
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 195
    is_best: false
  - model: UniGCN (LDP)
    value: 0.5988
    std: 0.0237
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 198
    is_best: false
  - model: UniGCN (HCP-FRC)
    value: 0.591
    std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 199
    is_best: false
  - model: UniSAGE (HCP-FRC)
    value: 0.591
    std: 0.0229
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 200
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.7268
    std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 216
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.7265
    std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 217
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    value: 0.7264
    std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 219
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7259
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 221
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7252
    std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 222
    is_best: false
  - model: UniGAT (no encodings nlayer2)
    value: 0.7116
    std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 233
    is_best: false
  - model: UniGCNII (LDP depth 2)
    value: 0.6985
    std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 238
    is_best: false
  - model: UniGAT (LDP)
    value: 0.6931
    std: 0.0223
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 244
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    value: 0.6789
    std: 0.0237
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 251
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    value: 0.6786
    std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 252
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    value: 0.6782
    std: 0.0218
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 254
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    value: 0.678
    std: 0.0227
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 255
    is_best: false
  - model: UniSAGE (no encodings)
    value: 0.678
    std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    global_rank: 256
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    value: 0.6776
    std: 0.0191
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 257
    is_best: false
  - model: UniGCN (no encodings)
    value: 0.677
    std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 258
    is_best: false
  - model: UniGAT (HCP-FRC)
    value: 0.6595
    std: 0.0324
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 266
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    value: 0.6554
    std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 268
    is_best: false
  - model: UniSAGE (LDP)
    value: 0.6308
    std: 0.0268
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    global_rank: 272
    is_best: false
  - model: UniGCN (LDP)
    value: 0.6296
    std: 0.0289
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 273
    is_best: false
  - model: UniGCN (HCP-FRC)
    value: 0.5777
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 285
    is_best: false
  - model: UniSAGE (HCP-FRC)
    value: 0.5735
    std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    global_rank: 288
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: Cora-CA
  rows:
  - model: HealHGNN
    value: 0.8478
    std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HGNN
    value: 0.7864
    std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7635
    std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    value: 0.7634
    std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7631
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.7624
    std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.7616
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: UniGCNII (LDP depth 2)
    value: 0.7589
    std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: UniGAT (no encodings nlayer2)
    value: 0.7568
    std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: UniGAT (LDP)
    value: 0.7547
    std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    value: 0.7501
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: UniGAT (HCP-FRC)
    value: 0.7485
    std: 0.0166
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: UniSAGE (no encodings)
    value: 0.7416
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    value: 0.7413
    std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    value: 0.741
    std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    value: 0.74
    std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    value: 0.7399
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    value: 0.7397
    std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: UniGCN (no encodings)
    value: 0.7397
    std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: UniSAGE (LDP)
    value: 0.7388
    std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: UniGCN (LDP)
    value: 0.7383
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: UniGCN (HCP-FRC)
    value: 0.7291
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: UniSAGE (HCP-FRC)
    value: 0.7257
    std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    global_rank: 23
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: PathNN-SP (K=2)
    value: 0.704
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: SPN(k=5)
    value: 0.694
    std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.01267'
    title: Cooperative Graph Neural Networks
    date: '2023-10-02'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GPS (EN H-19-RWPE)
    value: 0.5128
    std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.5109
    std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.4819
    std: 0.0131
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.4778
    std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: GPS (LCP-FRC)
    value: 0.4766
    std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.4744
    std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GPS (No Encoding)
    value: 0.4683
    std: 0.0114
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.429
    std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: GCN (LCP-ORC)
    value: 0.3283
    std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.3093
    std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 81
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.3087
    std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 82
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.3066
    std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 83
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.2852
    std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 101
    is_best: false
  - model: GCN (No Encoding)
    value: 0.2803
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 106
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: IMDB
  rows:
  - model: GPS (EN H-19-RWPE)
    value: 0.7308
    std: 0.0124
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GPS (LCP-ORC)
    value: 0.7205
    std: 0.0115
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GPS (LCP-FRC)
    value: 0.7148
    std: 0.0103
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: GPS (No Encoding)
    value: 0.7093
    std: 0.0121
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GPS (20-LAPE)
    value: 0.7067
    std: 0.0118
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 5
    is_best: true
  - model: GCN (LCP-ORC)
    value: 0.7064
    std: 0.0132
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 6
    is_best: true
  - model: GCN (EE H-19-RWPE)
    value: 0.7053
    std: 0.018
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 7
    is_best: true
  - model: GIN (HCP-FRC)
    value: 0.704
    std: 0.0152
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    global_rank: 8
    is_best: true
  - model: GCN (LCP-FRC)
    value: 0.7018
    std: 0.0144
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GIN (HCP-ORC)
    value: 0.6992
    std: 0.015
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.6948
    std: 0.0171
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.6937
    std: 0.0165
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.6935
    std: 0.0224
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.6816
    std: 0.0283
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GCN (No Encoding)
    value: 0.6712
    std: 0.0136
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.664
    std: 0.0153
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 16
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id008
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    value: 0.984
    std: 0.024
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
    global_rank: 1
    is_best: true
  - model: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
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
    global_rank: 2
    is_best: true
  - model: IPR-MPNN
    value: 0.98
    std: 0.034
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
    global_rank: 3
    is_best: true
  - model: GPS (LCP-FRC)
    value: 0.8936
    std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: GPS (EN H-19-RWPE)
    value: 0.8849
    std: 0.0212
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.869
    std: 0.0181
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.8672
    std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 45
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.8493
    std: 0.0182
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: GCN (LCP-ORC)
    value: 0.8309
    std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.8234
    std: 0.0268
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.8227
    std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.8085
    std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 86
    is_best: false
  - model: GPS (No Encoding)
    value: 0.804
    std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 90
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.8013
    std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 91
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.733
    std: 0.0195
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 134
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.7175
    std: 0.0208
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 140
    is_best: false
  - model: GCN (No Encoding)
    value: 0.6596
    std: 0.0176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    global_rank: 154
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GPS (EN H-19-RWPE)
    value: 0.7482
    std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.7452
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 78
    is_best: false
  - model: GPS (LCP-FRC)
    value: 0.745
    std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 79
    is_best: false
  - model: GPS (No Encoding)
    value: 0.741
    std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 89
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.7405
    std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 93
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.7403
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 94
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.7395
    std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 97
    is_best: false
  - model: GCN (LCP-ORC)
    value: 0.7378
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 100
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.7194
    std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 145
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.7192
    std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 147
    is_best: false
  - model: GCN (No Encoding)
    value: 0.7148
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 156
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.7146
    std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 157
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.7146
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 158
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.7127
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 161
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GPS (EN H-19-RWPE)
    value: 0.617
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 227
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.609
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 231
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.604
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 233
    is_best: false
  - model: GPS (LCP-FRC)
    value: 0.604
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 234
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.602
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 238
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.599
    std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 243
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.594
    std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 252
    is_best: false
  - model: GPS (No Encoding)
    value: 0.593
    std: 0.009
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 254
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.559
    std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 271
    is_best: false
  - model: GCN (LCP-ORC)
    value: 0.559
    std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 272
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.549
    std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 278
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.538
    std: 0.007
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 280
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.534
    std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 282
    is_best: false
  - model: GCN (No Encoding)
    value: 0.532
    std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 283
    is_best: false
  metric: AP
  higher_is_better: true
- &id006
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
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
  - model: GCN (Hodge H-20-LAPE)
    value: 0.252
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 139
    is_best: false
  - model: GPS (EN H-19-RWPE)
    value: 0.252
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 140
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.253
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 152
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.254
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 159
    is_best: false
  - model: GPS (LCP-FRC)
    value: 0.254
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 160
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.254
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 161
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.255
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 167
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.257
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 179
    is_best: false
  - model: GCN (LCP-ORC)
    value: 0.258
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 182
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.258
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 183
    is_best: false
  - model: GPS (No Encoding)
    value: 0.262
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 193
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.263
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 198
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.265
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 206
    is_best: false
  - model: GCN (No Encoding)
    value: 0.266
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 209
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
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
  - model: MLP
    value: 0.9476
    std: 0.001
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
    global_rank: 3
    is_best: true
  - model: UniGAT (no encodings nlayer2)
    value: 0.7562
    std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 129
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7551
    std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 130
    is_best: false
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.7544
    std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 131
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    value: 0.754
    std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 132
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    value: 0.7507
    std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 134
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    value: 0.7503
    std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 135
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.7503
    std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 136
    is_best: false
  - model: UniGCN (no encodings)
    value: 0.7502
    std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 137
    is_best: false
  - model: UniSAGE (no encodings)
    value: 0.7502
    std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 138
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7501
    std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 139
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    value: 0.7441
    std: 0.0143
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
  - model: UniGAT (H-19-RWPEE WE)
    value: 0.7437
    std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 143
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    value: 0.7429
    std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 145
    is_best: false
  - model: UniGAT (LDP)
    value: 0.6841
    std: 0.0179
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 152
    is_best: false
  - model: UniSAGE (LDP)
    value: 0.6753
    std: 0.0309
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 153
    is_best: false
  - model: UniGCN (LDP)
    value: 0.6741
    std: 0.0316
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 154
    is_best: false
  - model: UniGCNII (LDP depth 2)
    value: 0.674
    std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 155
    is_best: false
  - model: UniGAT (HCP-FRC)
    value: 0.6634
    std: 0.0179
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 156
    is_best: false
  - model: UniSAGE (HCP-FRC)
    value: 0.6571
    std: 0.0258
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 157
    is_best: false
  - model: UniGCN (HCP-FRC)
    value: 0.6555
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 158
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    value: 0.65
    std: 0.0218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 159
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GPS (LCP-ORC)
    value: 0.8307
    std: 0.0124
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GPS (20-LAPE)
    value: 0.8205
    std: 0.0129
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GPS (19-RWPE)
    value: 0.8192
    std: 0.0131
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GPS (LCP-FRC)
    value: 0.8168
    std: 0.0116
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GPS (No Encoding)
    value: 0.8094
    std: 0.0142
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    value: 0.7994
    std: 0.0181
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    value: 0.7915
    std: 0.0154
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCN (EE H-19-RWPE)
    value: 0.7746
    std: 0.0153
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: GCN (20-LAPE)
    value: 0.7584
    std: 0.0165
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GCN (No Encoding)
    value: 0.7538
    std: 0.0127
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GCN (19-RWPE)
    value: 0.744
    std: 0.0168
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GIN (HCP-FRC)
    value: 0.7053
    std: 0.0148
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GCN (LCP-FRC)
    value: 0.6966
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    global_rank: 16
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
- benchmark: TU Dortmund
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id011
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id012
main_figure: /figures/2502.09570/main_figure.png
---

