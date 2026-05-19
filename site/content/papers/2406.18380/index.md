---
title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
arxiv_id: '2406.18380'
authors: []
published_date: Jun 2024
abstract: In recent years, Graph Neural Networks (GNNs) have become the de facto tool
  for learning node and graph representations. Most GNNs typically consist of a sequence
  of neighborhood aggregation (a.k.a., message-passing) layers, within which the representation
  of each node is updated based on those of its neighbors. The most expressive message-passing
  GNNs can be obtained through the use of the sum aggregator and of MLPs for feature
  transformation, thanks to their universal approximation capabilities. However, the
  limitations of MLPs recently motivated the introduction of another family of universal
  approximators, called Kolmogorov-Arnold Networks (KANs) which rely on a different
  representation theorem. In this work, we compare the performance of KANs against
  that of MLPs on graph learning tasks. We implement three new KAN-based GNN layers,
  inspired respectively by the GCN, GAT and GIN layers. We evaluate two different
  implementations of KANs using two distinct base families of functions, namely B-splines
  and radial basis functions. We perform extensive experiments on node classification,
  link prediction, graph classification and graph regression datasets. Our results
  indicate that KANs are on-par with or better than MLPs on all tasks studied in this
  paper. We also show that the size and training speed of RBF-based KANs is only marginally
  higher than for MLPs, making them viable alternatives. Code available at https://github.com/RomanBresson/KAGNN.
codebase_url: https://github.com/RomanBresson/KAGNN
extraction_model: ''
has_results: true
proposed_models:
- BS-KAGCN
- RBF-KAGCN
- BS-KAGAT
- RBF-KAGAT
mrr: 0.021
results:
- &id004
  dataset: Actor
  rows:
  - model: GrokFormer
    value: 0.4298
    std: 0.0148
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
    global_rank: 1
    is_best: true
  - model: GrokFilter
    value: 0.4215
    std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: SpecFormer
    value: 0.4193
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
  - model: RBF-KAGCN
    value: 0.34369999999999995
    std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: BS-KAGCN
    value: 0.34259999999999996
    std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: RBF-KAGAT
    value: 0.3404
    std: 0.009399999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GIN
    value: 0.3346
    std: 0.0138
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
  - model: GCN
    value: 0.3281
    std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GAT
    value: 0.3251
    std: 0.011699999999999999
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
  - model: BS-KAGAT
    value: 0.3166
    std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 65
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GCN
    value: 0.716
    std: 0.004
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
  - model: GAT
    value: 0.6091
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: BS-KAGAT
    value: 0.5687
    std: 0.0167
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 203
    is_best: false
  - model: BS-KAGCN
    value: 0.5577000000000001
    std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 204
    is_best: false
  - model: RBF-KAGAT
    value: 0.4865
    std: 0.0239
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 209
    is_best: false
  - model: GIN
    value: 0.47979999999999995
    std: 0.0091
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: RBF-KAGCN
    value: 0.46869999999999995
    std: 0.019299999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 212
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: GCN
    value: 0.816
    std: 0.004
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
  - model: BS-KAGAT
    value: 0.7828
    std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 173
    is_best: false
  - model: GAT
    value: 0.7651
    std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: RBF-KAGCN
    value: 0.7277
    std: 0.013500000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 213
    is_best: false
  - model: RBF-KAGAT
    value: 0.7262000000000001
    std: 0.016399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 220
    is_best: false
  - model: GIN
    value: 0.7084999999999999
    std: 0.0175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 130
    is_best: false
  - model: BS-KAGCN
    value: 0.6578
    std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 267
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
  - model: BS-KAGCN
    value: 0.6964
    std: 0.07400000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: GIN
    value: 0.691
    std: 0.048499999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: BS-KAGAT
    value: 0.6766
    std: 0.0694
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: RBF-KAGCN
    value: 0.6729999999999999
    std: 0.0644
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: GAT
    value: 0.6685
    std: 0.0559
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
  - model: GCN
    value: 0.6613
    std: 0.060899999999999996
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
  - model: RBF-KAGAT
    value: 0.6414
    std: 0.061399999999999996
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
- &id013
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
  - model: GIN
    value: 0.5472
    std: 0.0655
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: BS-KAGAT
    value: 0.5133
    std: 0.129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: RBF-KAGAT
    value: 0.4978
    std: 0.0765
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
  - model: RBF-KAGCN
    value: 0.44780000000000003
    std: 0.0958
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
  - model: BS-KAGCN
    value: 0.445
    std: 0.08529999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: GCN
    value: 0.20559999999999998
    std: 0.037000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GAT
    value: 0.18170000000000003
    std: 0.0134
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
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    value: 0.8267
    std: 0.0047
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: RUM
    value: 0.811
    std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: nsqure~
    value: 0.7995
    std: 0.0246
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
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.7337
    std: 0.028999999999999998
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
  - model: BS-KAGCN
    value: 0.7313
    std: 0.0446
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: BS-KAGAT
    value: 0.72
    std: 0.038
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
  - model: RBF-KAGAT
    value: 0.71
    std: 0.0504
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 76
    is_best: false
  - model: RBF-KAGCN
    value: 0.6993
    std: 0.0384
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
  - model: GCN
    value: 0.684
    std: 0.0401
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
  - model: GAT
    value: 0.6737000000000001
    std: 0.0383
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
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    value: 0.63
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: DMON
    value: 0.62
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: SEP
    value: 0.61
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.5036
    std: 0.040999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: BS-KAGCN
    value: 0.5033
    std: 0.0387
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: BS-KAGAT
    value: 0.5009
    std: 0.0434
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
  - model: RBF-KAGCN
    value: 0.49219999999999997
    std: 0.0441
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
  - model: GCN
    value: 0.48560000000000003
    std: 0.0371
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: GAT
    value: 0.4824
    std: 0.050199999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: RBF-KAGAT
    value: 0.4813
    std: 0.0415
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 51
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
  - model: GIN
    value: 0.8615999999999999
    std: 0.0596
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: BS-KAGCN
    value: 0.8579000000000001
    std: 0.0806
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 50
    is_best: false
  - model: RBF-KAGCN
    value: 0.851
    std: 0.055999999999999994
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
  - model: BS-KAGAT
    value: 0.8266
    std: 0.0478
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
  - model: RBF-KAGAT
    value: 0.7587999999999999
    std: 0.121
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
  - model: GCN
    value: 0.5995
    std: 0.0898
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: GAT
    value: 0.5751
    std: 0.12300000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 104
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: NCI1
  rows:
  - model: Kern. WL
    value: 0.86
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via - High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: CoCN expanded
    value: 0.8583
    std: 0.0086
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
    global_rank: 2
    is_best: true
  - model: PR-MPNN (10-fold CV)
    value: 0.846
    std: 0.012
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
  - model: BS-KAGCN
    value: 0.8034
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GIN
    value: 0.7931999999999999
    std: 0.0163
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
  - model: RBF-KAGCN
    value: 0.7918999999999999
    std: 0.0181
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: BS-KAGAT
    value: 0.7646
    std: 0.0366
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
  - model: RBF-KAGAT
    value: 0.7263
    std: 0.04650000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 68
    is_best: false
  - model: GAT
    value: 0.6042000000000001
    std: 0.0821
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
  - model: GCN
    value: 0.601
    std: 0.0463
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
- &id010
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
  - model: RBF-KAGCN
    value: 0.7433
    std: 0.0352
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 81
    is_best: false
  - model: BS-KAGCN
    value: 0.7337
    std: 0.0281
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 105
    is_best: false
  - model: BS-KAGAT
    value: 0.7275
    std: 0.0218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 127
    is_best: false
  - model: RBF-KAGAT
    value: 0.7193
    std: 0.042300000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 146
    is_best: false
  - model: GIN
    value: 0.7066
    std: 0.036000000000000004
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
  - model: GCN
    value: 0.631
    std: 0.0375
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
  - model: GAT
    value: 0.5978
    std: 0.0087
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
  metric: Accuracy
  higher_is_better: true
- &id009
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
  - model: BS-KAGCN
    value: 0.5871
    std: 0.0102
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 260
    is_best: false
  - model: RBF-KAGCN
    value: 0.5768
    std: 0.020499999999999997
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 266
    is_best: false
  - model: GIN
    value: 0.5501
    std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 39
    is_best: false
  metric: AP
  higher_is_better: true
- &id017
  dataset: QM9
  rows:
  - model: Mace
    value: 0.02
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: DropGIN
    value: 0.02578744427174226
    std: 0.000867405321348238
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
  - model: ESA
    value: 0.02578744427174226
    std: 0.000867405321348238
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
    global_rank: 3
    is_best: false
  - model: BS-KAGCN
    value: 0.0618
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: RBF-KAGCN
    value: 0.0778
    std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GIN
    value: 0.0969
    std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
    is_best: false
  metric: MAE
  higher_is_better: false
- &id008
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
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: BS-KAGAT
    value: 0.7827
    std: 0.023700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: BS-KAGCN
    value: 0.7606
    std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: RBF-KAGCN
    value: 0.7592
    std: 0.0349
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GIN
    value: 0.7478
    std: 0.0382
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: RBF-KAGAT
    value: 0.7342
    std: 0.047599999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GAT
    value: 0.7192000000000001
    std: 0.0588
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN
    value: 0.6587000000000001
    std: 0.0633
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: F1
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
  - model: BS-KAGAT
    value: 0.7378
    std: 0.0639
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 96
    is_best: false
  - model: RBF-KAGCN
    value: 0.736
    std: 0.050499999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 97
    is_best: false
  - model: GIN
    value: 0.7351000000000001
    std: 0.0587
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 98
    is_best: false
  - model: BS-KAGCN
    value: 0.7297
    std: 0.056299999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 101
    is_best: false
  - model: GCN
    value: 0.7234
    std: 0.0592
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
  - model: RBF-KAGAT
    value: 0.7171
    std: 0.0649
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 107
    is_best: false
  - model: GAT
    value: 0.6901
    std: 0.061399999999999996
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
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GCN
    value: 0.7863
    std: 0.054299999999999994
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
  - model: BS-KAGCN
    value: 0.7863
    std: 0.0516
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: BS-KAGAT
    value: 0.7843000000000001
    std: 0.0547
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
  - model: GIN
    value: 0.7824
    std: 0.047599999999999996
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
  - model: GAT
    value: 0.7817000000000001
    std: 0.057
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
  - model: RBF-KAGCN
    value: 0.7673000000000001
    std: 0.048799999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: RBF-KAGAT
    value: 0.7634000000000001
    std: 0.0434
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 73
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: BS-KAGCN
    value: 0.3
    std: 0.0332
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 244
    is_best: false
  - model: RBF-KAGCN
    value: 0.3026
    std: 0.0663
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 245
    is_best: false
  - model: GIN
    value: 0.4131
    std: 0.0215
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  metric: MAE
  higher_is_better: false
- &id016
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
  - model: BS-KAGAT
    value: 0.5517
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 101
    is_best: false
  - model: RBF-KAGAT
    value: 0.5424
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 103
    is_best: false
  - model: GAT
    value: 0.5367999999999999
    std: 0.0012
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
  - model: GIN
    value: 0.5357999999999999
    std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 96
    is_best: false
  - model: RBF-KAGCN
    value: 0.5356000000000001
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 104
    is_best: false
  - model: GCN
    value: 0.5321
    std: 0.0013
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
  - model: BS-KAGCN
    value: 0.5305
    std: 0.0055000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 105
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: Classic
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
- benchmark: LRGB
  datasets:
  - *id009
- benchmark: TU Dortmund
  datasets:
  - *id010
  - *id011
  - *id012
  - *id013
  - *id014
  - *id015
- benchmark: OGB
  datasets:
  - *id016
- benchmark: Quantum Chemistry
  datasets:
  - *id017
---

