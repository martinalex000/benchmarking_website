---
title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
arxiv_id: '2406.08993'
authors: []
published_date: Jun 2024
abstract: Graph Transformers (GTs) have recently emerged as popular alternatives to
  traditional message-passing Graph Neural Networks (GNNs), due to their theoretically
  superior expressiveness and impressive performance reported on standard node classification
  benchmarks, often significantly outperforming GNNs. In this paper, we conduct a
  thorough empirical analysis to reevaluate the performance of three classic GNN models
  (GCN, GAT, and GraphSAGE) against GTs. Our findings suggest that the previously
  reported superiority of GTs may have been overstated due to suboptimal hyperparameter
  configurations in GNNs. Remarkably, with slight hyperparameter tuning, these classic
  GNN models achieve state-of-the-art performance, matching or even exceeding that
  of recent GTs across 17 out of the 18 diverse datasets examined. Additionally, we
  conduct detailed ablation studies to investigate the influence of various GNN configurations—such
  as normalization, dropout, residual connections, and network depth—on node classification
  performance. Our study aims to promote a higher standard of empirical rigor in the
  field of graph machine learning, encouraging more accurate comparisons and evaluations
  of model capabilities. Our implementation is available at https://github.com/LUOyk1999/tunedGNN.
codebase_url: ''
extraction_model: glm-4.7
has_results: true
proposed_models:
- GCN* (-) Normalization
- GCN* (-) Dropout
- GraphSAGE* (-) Normalization
- GraphSAGE* (-) Dropout
- GCN* (-) Residual Connections
- GraphSAGE* (-) Residual Connections
- GAT* (-) Dropout
mrr: 0.0977
results:
- &id011
  dataset: Amazon-Computers
  rows:
  - model: GAT
    value: 0.9409
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.9399
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 2
    is_best: true
  - model: Polynormer
    value: 0.9378
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 3
    is_best: true
  - model: GCN* (-) Dropout
    value: 0.9378
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 4
    is_best: true
  - model: GraphSAGE
    value: 0.9325
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 5
    is_best: false
  - model: GraphSAGE* (-) Normalization
    value: 0.9277
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GCN* (-) Normalization
    value: 0.926
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: SGFormer
    value: 0.9242
    std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 8
    is_best: false
  - model: GOAT
    value: 0.9229
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 9
    is_best: false
  - model: GraphSAGE* (-) Dropout
    value: 0.9202
    std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: Exphormer
    value: 0.918
    std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 11
    is_best: false
  - model: GraphGPS
    value: 0.9179
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 12
    is_best: false
  - model: Nagphormer
    value: 0.9169
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 13
    is_best: false
  - model: ParaFormer (a)
    value: 0.8936
    std: 0.0014000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 14
    is_best: false
  - model: NodeFormer
    value: 0.8729
    std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer
    global_rank: 15
    is_best: false
  - model: GAT-NSampler
    value: 0.8517
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 16
    is_best: false
  - model: GCN-Nsampler
    value: 0.8384
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 17
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: Amazon-Photo
  rows:
  - model: GENs
    value: 0.9712000000000001
    std: 0.0024
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
    value: 0.9678
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 2
    is_best: true
  - model: GAT
    value: 0.966
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 3
    is_best: true
  - model: Polynormer
    value: 0.9657
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 4
    is_best: false
  - model: Nagphormer
    value: 0.9614
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 5
    is_best: false
  - model: GCN
    value: 0.961
    std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 6
    is_best: false
  - model: Exphormer
    value: 0.9569
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 7
    is_best: false
  - model: SGFormer
    value: 0.9558
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 8
    is_best: false
  - model: GraphGPS
    value: 0.9489
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 9
    is_best: false
  - model: GOAT
    value: 0.9433
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 10
    is_best: false
  - model: NodeFormer
    value: 0.9343
    std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 11
    is_best: false
  - model: CaCoSE
    value: 0.9298000000000001
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    is_best: false
  - model: GOKU
    value: 0.9251
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 13
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: GAT
    value: 0.5554
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 2
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 3
    is_best: true
  - model: Polynormer
    value: 0.5496
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer
    global_rank: 4
    is_best: false
  - model: IM-CO-GNN(μ,μ)
    value: 0.5443
    std: 0.0041
    metric: Accuracy
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
    global_rank: 5
    is_best: false
  - model: CO-GNN
    value: 0.542
    std: 0.0034000000000000002
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
    is_best: false
  - model: SGFormer
    value: 0.5414
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 9
    is_best: false
  - model: GCN
    value: 0.538
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 14
    is_best: false
  - model: GraphGPS
    value: 0.5327
    std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 18
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 22
    is_best: false
  - model: GPRGNN
    value: 0.4488
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 55
    is_best: false
  - model: NodeFormer
    value: 0.4379
    std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 59
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 62
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 63
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 64
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
    global_rank: 2
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
    global_rank: 3
    is_best: true
  - model: GCN
    value: 0.4629
    std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 28
    is_best: false
  - model: SGFormer
    value: 0.4521
    std: 0.0372
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 56
    is_best: false
  - model: GraphSAGE
    value: 0.4481
    std: 0.0474
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 36
    is_best: false
  - model: GAT
    value: 0.4413
    std: 0.0417
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 29
    is_best: false
  - model: Polynormer
    value: 0.4197
    std: 0.0318
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 74
    is_best: false
  - model: GraphGPS
    value: 0.4155
    std: 0.0391
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 78
    is_best: false
  - model: FSGNN
    value: 0.4061
    std: 0.0297
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 80
    is_best: false
  - model: GPRGNN
    value: 0.3993
    std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 19
    is_best: false
  - model: NodeFormer
    value: 0.3638
    std: 0.0385
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 62
    is_best: false
  - model: CPGNN
    value: 0.33
    std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 79
    is_best: false
  - model: H2GCN
    value: 0.2675
    std: 0.0364
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 52
    is_best: false
  - model: GLoGNN
    value: 0.259
    std: 0.0358
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 81
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: GCNII
    value: 0.8183
    std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: ACMGCN
    value: 0.8183
    std: 0.0165
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
  - model: GCN
    value: 0.7314
    std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 8
    is_best: false
  - model: GraphGPS
    value: 0.7273
    std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 64
    is_best: false
  - model: SGFormer
    value: 0.7272
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 23
    is_best: false
  - model: NodeFormer
    value: 0.7237
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 38
    is_best: false
  - model: GraphSAGE
    value: 0.7226
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 19
    is_best: false
  - model: GAT
    value: 0.7222
    std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 29
    is_best: false
  - model: GOAT
    value: 0.7221
    std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 65
    is_best: false
  - model: Polynormer
    value: 0.7219
    std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 24
    is_best: false
  - model: Exphormer
    value: 0.7185
    std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 67
    is_best: false
  - model: Nagphormer
    value: 0.7059
    std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 13
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: Coauthor-CS
  rows:
  - model: GraphSAGE
    value: 0.9638
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 1
    is_best: true
  - model: GAT
    value: 0.9621
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 2
    is_best: true
  - model: GCN
    value: 0.9617
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 3
    is_best: false
  - model: Exphormer
    value: 0.9592
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 4
    is_best: false
  - model: Nagphormer
    value: 0.9585
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 5
    is_best: false
  - model: SGFormer
    value: 0.9571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 6
    is_best: false
  - model: NodeFormer
    value: 0.9569
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 7
    is_best: false
  - model: Polynormer
    value: 0.9542
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 8
    is_best: false
  - model: GraphGPS
    value: 0.9404
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 9
    is_best: false
  - model: GOAT
    value: 0.9381
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 10
    is_best: false
  - model: CaCoSE
    value: 0.9073
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    is_best: false
  - model: SDRF
    value: 0.9056000000000001
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    is_best: false
  - model: BORF
    value: 0.9052
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.27529'
    title: Cross-attentive Cohesive Subgraph Embedding to Mitigate Oversquashing in
      GNNs
    date: Mar 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 13
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: Coauthor-Physics
  rows:
  - model: GCN
    value: 0.9746
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 1
    is_best: true
  - model: Nagphormer
    value: 0.9735
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 2
    is_best: true
  - model: GAT
    value: 0.9725
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 3
    is_best: false
  - model: GraphSAGE
    value: 0.9719
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 4
    is_best: false
  - model: Polynormer
    value: 0.9718
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 5
    is_best: false
  - model: Exphormer
    value: 0.9706
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 6
    is_best: false
  - model: SGFormer
    value: 0.9675
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 7
    is_best: false
  - model: GraphGPS
    value: 0.9671
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 8
    is_best: false
  - model: NodeFormer
    value: 0.9648
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 9
    is_best: false
  - model: GOAT
    value: 0.9647
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 10
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Cora
  rows:
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
    global_rank: 1
    is_best: true
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
    global_rank: 2
    is_best: true
  - model: GAT+JK
    value: 0.8952
    std: 0.0043
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
    is_best: false
  - model: GCN
    value: 0.851
    std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 32
    is_best: false
  - model: SGFormer
    value: 0.8482
    std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 23
    is_best: false
  - model: GAT
    value: 0.8446
    std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 24
    is_best: false
  - model: GraphSAGE
    value: 0.8388
    std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 49
    is_best: false
  - model: GraphGPS
    value: 0.8387
    std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 71
    is_best: false
  - model: Polynormer
    value: 0.8343
    std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 29
    is_best: false
  - model: Exphormer
    value: 0.8329
    std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 73
    is_best: false
  - model: GOAT
    value: 0.8326
    std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 74
    is_best: false
  - model: NodeFormer
    value: 0.8273
    std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 13
    is_best: false
  - model: Nagphormer
    value: 0.8092
    std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 21
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: GCN
    value: 0.9786
    std: 0.0024
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 5
    is_best: false
  - model: GraphSAGE
    value: 0.9777
    std: 0.0062
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 6
    is_best: false
  - model: GAT
    value: 0.9773
    std: 0.0073
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 7
    is_best: false
  - model: Polynormer
    value: 0.9749
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 8
    is_best: false
  - model: SGFormer
    value: 0.9142
    std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 38
    is_best: false
  - model: GraphGPS
    value: 0.9075
    std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 42
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 47
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 48
    is_best: false
  - model: NodeFormer
    value: 0.8771
    std: 0.0069
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 53
    is_best: false
  - model: GPRGNN
    value: 0.8624
    std: 0.0061
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 55
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 58
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
    table_ref: Table 3
    source_ref: Deng et al. 2024
    global_rank: 59
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id009
  dataset: PubMed
  rows:
  - model: ACMII-Snowball-3
    value: 0.9131
    std: 0.006
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
    value: 0.9081
    std: 0.0052
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
  - model: ACMII-GCN
    value: 0.9063
    std: 0.0056
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
  - model: GCN
    value: 0.8112
    std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 27
    is_best: false
  - model: SGFormer
    value: 0.806
    std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 14
    is_best: false
  - model: GAT
    value: 0.8028
    std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 48
    is_best: false
  - model: Nagphormer
    value: 0.8014
    std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 15
    is_best: false
  - model: GOAT
    value: 0.8006
    std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 79
    is_best: false
  - model: GraphGPS
    value: 0.7994
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 80
    is_best: false
  - model: GraphSAGE
    value: 0.7972
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 35
    is_best: false
  - model: Exphormer
    value: 0.7967
    std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 81
    is_best: false
  - model: NodeFormer
    value: 0.7959
    std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 22
    is_best: false
  - model: Polynormer
    value: 0.7935
    std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 5
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Questions
  rows:
  - model: IM-CO-GNN(Σ,Σ)
    value: 0.8049
    std: 0.0092
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
    global_rank: 1
    is_best: true
  - model: Tango_GatedGCN
    value: 0.8039000000000001
    std: 0.0104
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
    global_rank: 2
    is_best: true
  - model: Tango_GPS
    value: 0.8031999999999999
    std: 0.010700000000000001
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
  - model: GCN
    value: 0.7902
    std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 8
    is_best: true
  - model: Polynormer
    value: 0.7894
    std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 9
    is_best: true
  - model: FSGNN
    value: 0.7886
    std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 11
    is_best: true
  - model: GAT
    value: 0.7795
    std: 0.0051
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 17
    is_best: false
  - model: GraphSAGE
    value: 0.7721
    std: 0.0128
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 25
    is_best: false
  - model: NodeFormer
    value: 0.7502
    std: 0.0161
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 39
    is_best: false
  - model: SGFormer
    value: 0.7381
    std: 0.0059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 44
    is_best: false
  - model: GraphGPS
    value: 0.7256
    std: 0.0133
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 45
    is_best: false
  - model: CPGNN
    value: 0.6596
    std: 0.0195
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 49
    is_best: false
  - model: GLoGNN
    value: 0.6574
    std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 50
    is_best: false
  - model: H2GCN
    value: 0.6359
    std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 51
    is_best: false
  - model: GPRGNN
    value: 0.5548
    std: 0.0091
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 53
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
  dataset: Roman-empire
  rows:
  - model: Polynormer
    value: 0.9266
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
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
    global_rank: 3
    is_best: true
  - model: IM-CO-GNN(Σ,Σ)
    value: 0.9208
    std: 0.0033
    metric: Accuracy
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
  - model: GCN
    value: 0.9127
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 12
    is_best: false
  - model: GraphSAGE
    value: 0.9106
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 13
    is_best: false
  - model: GAT
    value: 0.9063
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 15
    is_best: false
  - model: GraphGPS
    value: 0.8272
    std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 40
    is_best: false
  - model: SGFormer
    value: 0.8001
    std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 43
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 45
    is_best: false
  - model: NodeFormer
    value: 0.7483
    std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 46
    is_best: false
  - model: GPRGNN
    value: 0.6485
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 52
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 53
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 54
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
    table_ref: Table 3
    source_ref: deng2024polynormer,wu2023simplifying,platonov2023critical
    global_rank: 55
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Squirrel
  rows:
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
    global_rank: 1
    is_best: true
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
    global_rank: 2
    is_best: true
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
    global_rank: 3
    is_best: true
  - model: GCN
    value: 0.4501
    std: 0.0163
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: SGFormer
    value: 0.4265
    std: 0.0241
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: Polynormer
    value: 0.4197
    std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: deng2024polynormer
    global_rank: 40
    is_best: false
  - model: GAT
    value: 0.4173
    std: 0.0207
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 35
    is_best: false
  - model: GraphSAGE
    value: 0.4078
    std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GraphGPS
    value: 0.3981
    std: 0.0228
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GPRGNN
    value: 0.3895
    std: 0.0199
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
  - model: NodeFormer
    value: 0.3889
    std: 0.0267
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: FSGNN
    value: 0.3592
    std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 68
    is_best: false
  - model: GLoGNN
    value: 0.3511
    std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 64
    is_best: false
  - model: H2GCN
    value: 0.351
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: CPGNN
    value: 0.3004
    std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 53
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: WikiCS
  rows:
  - model: GENs
    value: 0.8148000000000001
    std: 0.0046
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
  - model: GAT
    value: 0.8107
    std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 2
    is_best: true
  - model: GraphSAGE
    value: 0.8069
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 3
    is_best: false
  - model: GCN
    value: 0.803
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 4
    is_best: false
  - model: Polynormer
    value: 0.8026
    std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 5
    is_best: true
  - model: SGFormer
    value: 0.8005
    std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 6
    is_best: false
  - model: Exphormer
    value: 0.7938
    std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 7
    is_best: false
  - model: GraphMAE
    value: 0.7932
    std: 0.0029
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
    global_rank: 8
    is_best: false
  - model: BGRL
    value: 0.7902
    std: 0.0013
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
    global_rank: 9
    is_best: false
  - model: GraphGPS
    value: 0.7866
    std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 11
    is_best: false
  - model: GOAT
    value: 0.7796
    std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 12
    is_best: false
  - model: Nagphormer
    value: 0.7792
    std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 13
    is_best: false
  - model: NodeFormer
    value: 0.7513
    std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Deng et al. 2024; Wu et al. 2023
    global_rank: 14
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: ogbn-arxiv
  rows:
  - model: GCN
    value: 0.7353
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 1
    is_best: true
  - model: Polynormer
    value: 0.734
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 2
    is_best: true
  - model: GAT
    value: 0.733
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 3
    is_best: true
  - model: GraphSAGE
    value: 0.73
    std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 4
    is_best: false
  - model: ParaFormer (a)
    value: 0.7287
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.14619'
    title: 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation
      Learning'
    date: Dec 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: SGFormer
    value: 0.7276
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 6
    is_best: false
  - model: GOAT
    value: 0.7276
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 8
    is_best: false
  - model: GENs
    value: 0.7276
    std: 0.0019
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
    global_rank: 7
    is_best: false
  - model: GCN* (-) Residual Connections
    value: 0.7247
    std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: PPGT
    value: 0.7246
    std: 0.0015
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
    global_rank: 10
    is_best: false
  - model: Exphormer
    value: 0.7232
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 11
    is_best: false
  - model: GraphSAGE* (-) Residual Connections
    value: 0.7222
    std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: GCN* (-) Dropout
    value: 0.7206
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GAT* (-) Dropout
    value: 0.7168
    std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: GCN* (-) Normalization
    value: 0.7133
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: GraphSAGE* (-) Dropout
    value: 0.713
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: GraphGPS
    value: 0.7123
    std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 21
    is_best: false
  - model: GraphSAGE* (-) Normalization
    value: 0.7113
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: Nagphormer
    value: 0.7088
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 18
    is_best: false
  - model: NodeFormer
    value: 0.6778
    std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 28
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id016
  dataset: ogbn-proteins
  rows:
  - model: GAT
    value: 0.8501
    std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 1
    is_best: true
  - model: GraphSAGE
    value: 0.8221
    std: 0.0032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 2
    is_best: false
  - model: SGFormer
    value: 0.7992
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 3
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
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 4
    is_best: false
  - model: GOAT
    value: 0.7931
    std: 0.0042
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 5
    is_best: false
  - model: NodeFormer
    value: 0.7786
    std: 0.0084
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 6
    is_best: false
  - model: Exphormer
    value: 0.7762
    std: 0.0033
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 7
    is_best: false
  - model: GCN
    value: 0.7729
    std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 8
    is_best: false
  - model: GraphGPS
    value: 0.7715
    std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 9
    is_best: false
  - model: GAT-NSampler
    value: 0.7463
    std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    is_best: false
  - model: GCN-Nsampler
    value: 0.7351
    std: 0.0131
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    is_best: false
  - model: Nagphormer
    value: 0.7217
    std: 0.0045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: deng2024polynormer,wu2023simplifying
    global_rank: 12
    is_best: false
  - model: MLP
    value: 0.7204
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.10759'
    title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
    date: Jun 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 13
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
  - *id005
  - *id006
- benchmark: Classic
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
  - *id011
  - *id012
  - *id013
  - *id014
- benchmark: OGB
  datasets:
  - *id015
  - *id016
main_figure: /figures/2406.08993/main_figure.png
---

