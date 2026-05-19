---
title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
arxiv_id: '2308.11129'
authors: []
published_date: Aug 2023
abstract: Graph transformers need strong inductive biases to derive meaningful attention
  scores. Yet, current methods often fall short in capturing longer ranges, hierarchical
  structures, or community structures, which are common in various graphs such as
  molecules, social networks, and citation networks. This paper presents a Hierarchical
  Distance Structural Encoding (HDSE) method to model node distances in a graph, focusing
  on its multi-level, hierarchical nature. We introduce a novel framework to seamlessly
  integrate HDSE into the attention mechanism of existing graph transformers, allowing
  for simultaneous application with other positional encodings. To apply graph transformers
  with HDSE to large-scale graphs, we further propose a high-level HDSE that effectively
  biases the linear transformers towards graph hierarchies. We theoretically prove
  the superiority of HDSE over shortest path distances in terms of expressivity and
  generalization. Empirically, we demonstrate that graph transformers with HDSE excel
  in graph classification, regression on 7 graph-level datasets, and node classification
  on 11 large-scale graphs, including those with up to a billion nodes. Our implementation
  is available at https://github.com/LUOyk1999/HDSE.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GT + HDSE
- SAT + HDSE
- GraphGPS + HDSE
- GraphGPS + HDSE (K=0)
- GOAT + HDSE (K=1)
- ANS-GT + HDSE
mrr: 0.0895
results:
- &id002
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
  - model: GT + HDSE
    value: 0.38
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: SGFormer
    value: 0.379
    std: 0.011
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
  - model: CoBFormer
    value: 0.374
    std: 0.01
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
  - model: NodeFormer
    value: 0.369
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: SIGN
    value: 0.365
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: GOAT
    value: 0.321
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: GCN
    value: 0.301
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GAT
    value: 0.298
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: SGC
    value: 0.27
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 72
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: CIFAR10
  rows:
  - model: GRASS
    value: 0.8375
    std: 0.00141
    metric: Accuracy
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
    value: 0.80027
    std: 0.00185
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
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: Ours
    value: 0.79067
    std: 0.00269
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.02758'
    title: Differential Encoding for Improved Representation Learning over Graphs
    date: Jul 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GT + HDSE
    value: 0.76473
    std: 0.00429
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GRIT
    value: 0.76468
    std: 0.00881
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
  - model: GraphGPS + HDSE
    value: 0.7618
    std: 0.00277
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: Exphormer
    value: 0.74696
    std: 0.00125
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
  - model: Graph MLP-Mixer
    value: 0.73961
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 35
    is_best: false
  - model: GraphGPS
    value: 0.72298
    std: 0.00356
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
  - model: GIN-AK+
    value: 0.7219
    std: 0.0013
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
  - model: EGT
    value: 0.68702
    std: 0.00409
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
  - model: GatedGCN
    value: 0.67312
    std: 0.00311
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: GT
    value: 0.59753
    std: 0.00293
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 102
    is_best: false
  - model: GCN
    value: 0.5571
    std: 0.00381
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 86
    is_best: false
  - model: GIN
    value: 0.55255
    std: 0.01527
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 88
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: CLUSTER
  rows:
  - model: Tango_GPS
    value: 0.80113
    std: 0.0013800000000000002
    metric: Accuracy
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
    global_rank: 1
    is_best: true
  - model: PPGT
    value: 0.80027
    std: 0.00114
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GRIT
    value: 0.80026
    std: 0.00277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: GT + HDSE
    value: 0.79965
    std: 0.00203
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GRIT-GCCM
    value: 0.79816
    std: 0.0013700000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05689'
    title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive Consistency
      Model'
    date: May 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: EGT
    value: 0.79232
    std: 0.00348
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: SAT + HDSE
    value: 0.78513
    std: 0.00097
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GraphGPS + HDSE
    value: 0.78498
    std: 0.00121
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: Exphormer
    value: 0.78071
    std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: GraphGPS
    value: 0.78016
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: SAT
    value: 0.77856
    std: 0.00104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: SAN
    value: 0.76691
    std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GatedGCN
    value: 0.7384
    std: 0.00326
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 2
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GT
    value: 0.73169
    std: 0.00622
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 57
    is_best: false
  - model: SGFormer
    value: 0.69972
    std: 0.00634
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 59
    is_best: false
  - model: GCN
    value: 0.68498
    std: 0.00976
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: GIN
    value: 0.64716
    std: 0.01553
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 56
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
  - model: GT + HDSE
    value: 0.46
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 104
    is_best: false
  - model: SGFormer
    value: 0.449
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: GOAT
    value: 0.433
    std: 0.043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 110
    is_best: false
  - model: Graphormer
    value: 0.419
    std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 84
    is_best: false
  - model: SIGN
    value: 0.417
    std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 114
    is_best: false
  - model: GCN
    value: 0.413
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: GAT
    value: 0.392
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 45
    is_best: false
  - model: SGC
    value: 0.39
    std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 118
    is_best: false
  - model: GraphGPS
    value: 0.362
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 103
    is_best: false
  - model: NodeFormer
    value: 0.347
    std: 0.041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 78
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: ANS-GT + HDSE
    value: 0.8967
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: Coarformer
    value: 0.8869
    std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: GPRGNN
    value: 0.8827
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: H2GCN
    value: 0.8792
    std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: Gophormer
    value: 0.8765
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 55
    is_best: false
  - model: SGFormer
    value: 0.845
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 39
    is_best: false
  - model: GT + HDSE
    value: 0.839
    std: 0.007
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
  - model: HSGT
    value: 0.836
    std: 0.018
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
  - model: Gapformer
    value: 0.835
    std: 0.004
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
  - model: APPNP
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
    global_rank: 41
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
  - model: NodeFormer
    value: 0.822
    std: 0.009
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
  - model: SIGN
    value: 0.821
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 85
    is_best: false
  - model: GOAT
    value: 0.821
    std: 0.009
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
  - model: HC-GNN
    value: 0.819
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 140
    is_best: false
  - model: JKNet
    value: 0.818
    std: 0.005
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
  - model: AGT
    value: 0.817
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 142
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
  - model: SGC
    value: 0.801
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 80
    is_best: false
  - model: ANS-GT
    value: 0.794
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 154
    is_best: false
  - model: GraphGPS
    value: 0.765
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 115
    is_best: false
  - model: Graphormer
    value: 0.758
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 183
    is_best: false
  - model: SAN
    value: 0.7402
    std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 139
    is_best: false
  - model: SAT
    value: 0.724
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 214
    is_best: false
  - model: GT
    value: 0.7184
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 218
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: MNIST
  rows:
  - model: GRASS
    value: 0.98932
    std: 0.00076
    metric: Accuracy
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
  - model: GSM++ (MoT)
    value: 0.9884
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: NeuralWalker
    value: 0.9876
    std: 0.00079
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
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: Exphormer
    value: 0.9855
    std: 0.00039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GT + HDSE
    value: 0.98424
    std: 0.00124
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GraphGPS + HDSE
    value: 0.98367
    std: 0.00106
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: EGT
    value: 0.98173
    std: 0.00087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: GRIT
    value: 0.98108
    std: 0.00111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: GraphGPS
    value: 0.98051
    std: 0.00126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: PNA
    value: 0.9794
    std: 0.0012
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
  - model: Graph MLP-Mixer
    value: 0.97422
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: GatedGCN
    value: 0.9734
    std: 0.00143
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 2
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GIN
    value: 0.96485
    std: 0.00252
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: GT
    value: 0.90831
    std: 0.00161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 89
    is_best: false
  - model: GCN
    value: 0.90705
    std: 0.00218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 22
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: PATTERN
  rows:
  - model: GRIT (our run)
    value: 0.90405
    std: 0.00232
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GRIT 2-QiQRW
    value: 0.90165
    std: 0.00446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with - Quantum Computed Encodings
    date: Oct 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: PPGT
    value: 0.89752
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GT + HDSE
    value: 0.87281
    std: 0.00064
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GRIT
    value: 0.87196
    std: 0.00076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: SAT + HDSE
    value: 0.86933
    std: 0.00039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 30
    is_best: false
  - model: GIN-AK+
    value: 0.8685
    std: 0.00057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 35
    is_best: false
  - model: SAT
    value: 0.86848
    std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: EGT
    value: 0.86821
    std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 40
    is_best: false
  - model: Exphormer
    value: 0.86742
    std: 0.00015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GraphGPS + HDSE
    value: 0.86737
    std: 0.00055
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GraphGPS
    value: 0.86685
    std: 0.00059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 55
    is_best: false
  - model: SAN
    value: 0.86581
    std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 64
    is_best: false
  - model: GatedGCN
    value: 0.85568
    std: 0.00088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 2
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: GIN
    value: 0.85387
    std: 0.00136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 38
    is_best: false
  - model: SGFormer
    value: 0.85287
    std: 0.00097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GT
    value: 0.84808
    std: 0.00068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 75
    is_best: false
  - model: GCN
    value: 0.71892
    std: 0.00334
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 24
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: GraphGPS + HDSE
    value: 0.7156
    std: 0.0058
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: DRew
    value: 0.715
    std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Gutteridge 2023
    global_rank: 20
    is_best: false
  - model: GRIT
    value: 0.6988
    std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Ma 2023
    global_rank: 51
    is_best: false
  - model: Graph MLP-Mixer
    value: 0.697
    std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: He 2023
    global_rank: 61
    is_best: false
  - model: MGT+WavePE
    value: 0.6817
    std: 0.0064
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Ngo 2023
    global_rank: 102
    is_best: false
  - model: GraphGPS
    value: 0.6535
    std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Rampavsek 2022
    global_rank: 157
    is_best: false
  - model: Exphormer
    value: 0.6527
    std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Shirzad 2023
    global_rank: 168
    is_best: false
  - model: SAN+RWSE
    value: 0.6439
    std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 3
    source_ref: Kreuzer 2021
    global_rank: 187
    is_best: false
  - model: GT
    value: 0.6326
    std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Dwivedi 2020
    global_rank: 204
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 3
    source_ref: Dwivedi 2021
    global_rank: 130
    is_best: false
  - model: GCN
    value: 0.593
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: Kipf 2017
    global_rank: 9
    is_best: false
  - model: GatedGCN
    value: 0.5864
    std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 3
    source_ref: Bresson 2017
    global_rank: 47
    is_best: false
  - model: GINE
    value: 0.5498
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 3
    source_ref: Xu 2018
    global_rank: 138
    is_best: false
  metric: AP
  higher_is_better: true
- &id007
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
  - model: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: MGT+WavePE
    value: 0.2453
    std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Ngo 2023
    global_rank: 35
    is_best: true
  - model: GraphGPS + HDSE
    value: 0.2457
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 43
    is_best: false
  - model: GRIT
    value: 0.246
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Ma 2023
    global_rank: 51
    is_best: false
  - model: Graph MLP-Mixer
    value: 0.2475
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: He 2023
    global_rank: 27
    is_best: false
  - model: Exphormer
    value: 0.2481
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Shirzad 2023
    global_rank: 92
    is_best: false
  - model: GraphGPS
    value: 0.25
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Rampásek 2022
    global_rank: 120
    is_best: false
  - model: GT
    value: 0.2529
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Dwivedi 2020
    global_rank: 149
    is_best: false
  - model: DRew
    value: 0.2536
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Gutteridge 2023
    global_rank: 153
    is_best: false
  - model: SAN+RWSE
    value: 0.2545
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 3
    source_ref: Kreuzer 2021
    global_rank: 163
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 3
    source_ref: Dwivedi 2021
    global_rank: 146
    is_best: false
  - model: GatedGCN
    value: 0.342
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 3
    source_ref: Bresson 2017
    global_rank: 10
    is_best: false
  - model: GCN
    value: 0.3496
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: Kipf 2017
    global_rank: 2
    is_best: false
  - model: GINE
    value: 0.3547
    std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 3
    source_ref: Xu 2019
    global_rank: 71
    is_best: false
  metric: MAE
  higher_is_better: false
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
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GOAT + HDSE (K=1)
    value: 0.438
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 7
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: GT + HDSE
    value: 0.432
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: SGFormer
    value: 0.418
    std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: GOAT
    value: 0.411
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: Graphormer
    value: 0.409
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: SIGN
    value: 0.407
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: SGC
    value: 0.393
    std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 74
    is_best: false
  - model: GCN
    value: 0.386
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: NodeFormer
    value: 0.385
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GAT
    value: 0.356
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 45
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
  - model: GRIT
    value: 0.059
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Ma 2023
    global_rank: 9
    is_best: false
  - model: GT + HDSE
    value: 0.059
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: GraphGPS + HDSE
    value: 0.062
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: GraphGPS + HDSE (K=0)
    value: 0.064
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 6
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: SpecFormer
    value: 0.066
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Bo 2023
    global_rank: 70
    is_best: false
  - model: GraphGPS
    value: 0.07
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Rampásek 2022
    global_rank: 89
    is_best: false
  - model: Graph MLP-Mixer
    value: 0.073
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: He 2023
    global_rank: 107
    is_best: false
  - model: CIN
    value: 0.079
    std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Bodnar 2021
    global_rank: 7
    is_best: false
  - model: GIN-AK+
    value: 0.08
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Zhao 2021
    global_rank: 129
    is_best: false
  - model: Graphormer-GD
    value: 0.081
    std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Zhang 2023
    global_rank: 16
    is_best: false
  - model: SAT + HDSE
    value: 0.084
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 136
    is_best: false
  - model: SAT
    value: 0.094
    std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Chen 2022
    global_rank: 28
    is_best: false
  - model: EGT
    value: 0.108
    std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hussain 2022
    global_rank: 169
    is_best: false
  - model: SAN
    value: 0.139
    std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Kreuzer 2021
    global_rank: 194
    is_best: false
  - model: PNA
    value: 0.188
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Corso 2020
    global_rank: 40
    is_best: false
  - model: GT
    value: 0.226
    std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Dwivedi 2020
    global_rank: 232
    is_best: false
  - model: GatedGCN
    value: 0.282
    std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 2
    source_ref: Bresson 2017
    global_rank: 116
    is_best: false
  - model: SGFormer
    value: 0.306
    std: 0.023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wu 2023
    global_rank: 240
    is_best: false
  - model: GCN
    value: 0.367
    std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Kipf 2017
    global_rank: 115
    is_best: false
  - model: GIN
    value: 0.526
    std: 0.051
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Xu 2018
    global_rank: 67
    is_best: false
  metric: MAE
  higher_is_better: false
- &id012
  dataset: ogbn-arxiv
  rows:
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
    global_rank: 1
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
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GOAT + HDSE (K=1)
    value: 0.7336
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 7
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: GT + HDSE
    value: 0.7326
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: CoBFormer
    value: 0.7317
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: HC-GNN
    value: 0.7279
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: SGFormer
    value: 0.7263
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: HSGT
    value: 0.7258
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: Exphormer
    value: 0.7244
    std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: GOAT
    value: 0.7241
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: ANS-GT
    value: 0.7234
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 35
    is_best: false
  - model: AGT
    value: 0.7228
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 39
    is_best: false
  - model: GAT
    value: 0.7195
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: SIGN
    value: 0.7195
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: Gapformer
    value: 0.719
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GCN
    value: 0.7174
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GraphGPS
    value: 0.7097
    std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 62
    is_best: false
  - model: Nagphormer
    value: 0.7013
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: SGC
    value: 0.6779
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 79
    is_best: false
  - model: LINKX
    value: 0.6618
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 83
    is_best: false
  - model: NodeFormer
    value: 0.599
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 80
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: ogbn-papers100M
  rows:
  - model: GT + HDSE
    value: 0.6604
    std: 0.0015
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
  - model: SGFormer
    value: 0.6601
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 2
    is_best: true
  - model: SIGN
    value: 0.6511
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GOAT
    value: 0.6505
    std: 0.0013
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
  - model: LargeGT
    value: 0.6473
    std: 0.0005
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
  - model: LargeGT-full
    value: 0.6473
    std: 0.0005
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
  - model: GAT
    value: 0.6347
    std: 0.0039
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
  - model: SGC
    value: 0.6329
    std: 0.0019
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
  - model: GCN
    value: 0.6204
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GOAT-full-δ
    value: 0.6112
    std: 0.001
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
    global_rank: 10
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: ogbn-proteins
  rows:
  - model: GraphSAGE
    value: 0.8221
    std: 0.0032
    metric: ROC-AUC
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
    global_rank: 2
    is_best: true
  - model: GT + HDSE
    value: 0.803
    std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: nsqure~
    value: 0.7955
    std: 0.0079
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: SGFormer
    value: 0.7953
    std: 0.0038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: Polynormer
    value: 0.7953
    std: 0.0067
    metric: ROC-AUC
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
    global_rank: 6
    is_best: false
  - model: w/o HDSE
    value: 0.794
    std: 0.003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5 (Ablation)
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GOAT
    value: 0.7837
    std: 0.0026
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: w/o coarsening
    value: 0.783
    std: 0.004
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5 (Ablation)
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: HSGT
    value: 0.7813
    std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: NodeFormer
    value: 0.7745
    std: 0.0115
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: ANS-GT
    value: 0.7467
    std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: GCN
    value: 0.7251
    std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GAT
    value: 0.7202
    std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 1
    is_best: false
  - model: SIGN
    value: 0.7124
    std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: SGC
    value: 0.7031
    std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    global_rank: 23
    is_best: false
  metric: ROC-AUC
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
- benchmark: LRGB
  datasets:
  - *id006
  - *id007
- benchmark: GNNBenchmark
  datasets:
  - *id008
  - *id009
  - *id010
  - *id011
- benchmark: OGB
  datasets:
  - *id012
  - *id013
  - *id014
main_figure: /figures/2308.11129/main_figure.png
---

