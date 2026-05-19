---
title: Unitary convolutions for learning on graphs and groups
arxiv_id: '2410.05499'
authors: []
published_date: '2024-10-07'
abstract: Data with geometric structure is ubiquitous in machine learning often arising
  from fundamental symmetries in a domain, such as permutation-invariance in graphs
  and translation-invariance in images. Group-convolutional architectures, which encode
  symmetries as inductive bias, have shown great success in applications, but can
  suffer from instabilities as their depth increases and often struggle to learn long
  range dependencies in data. For instance, graph neural networks experience instability
  due to the convergence of node representations (over-smoothing), which can occur
  after only a few iterations of message-passing, reducing their effectiveness in
  downstream tasks. Here, we propose and study unitary group convolutions, which allow
  for deeper networks that are more stable during training. The main focus of the
  paper are graph neural networks, where we show that unitary graph convolutions provably
  avoid over-smoothing. Our experimental results confirm that unitary graph convolutional
  networks achieve competitive performance on benchmark datasets compared to state-of-the-art
  graph neural networks. We complement our analysis of the graph domain with the study
  of general unitary convolutions and analyze their role in enhancing stability in
  general group convolutional architectures.
codebase_url: ''
extraction_model: Kimi-K2.6
has_results: true
proposed_models:
- UniGCN
- Lie UniGCN
- Unitary GCN
- Lie Unitary GCN
- Wide Unitary GCN
mrr: 0.0432
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
  - model: Unitary GCN
    value: 0.5534
    std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: Polynormer
    value: 0.5496
    std: 0.0222
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
    global_rank: 4
    is_best: true
  - model: SAGE
    value: 0.5363
    std: 0.0039
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 20
    is_best: false
  - model: Lie Unitary GCN
    value: 0.5235
    std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GT
    value: 0.5117
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 43
    is_best: false
  - model: GAT
    value: 0.4909
    std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 2
    is_best: false
  - model: GCN
    value: 0.487
    std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 17
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
  - model: Wide Unitary GCN
    value: 0.421
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: Unitary GCN
    value: 0.415
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 38
    is_best: false
  - model: GIN
    value: 0.313
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GAT
    value: 0.268
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 22
    is_best: false
  - model: GCN
    value: 0.255
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 13
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GIN
    value: 0.69
    std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Wide Unitary GCN
    value: 0.624
    std: 0.013
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Unitary GCN
    value: 0.612
    std: 0.014
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GCN
    value: 0.493
    std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GAT
    value: 0.47
    std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
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
  - model: Wide Unitary GCN
    value: 0.871
    std: 0.035
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: Unitary GCN
    value: 0.868
    std: 0.033
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: GIN
    value: 0.757
    std: 0.036
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: GCN
    value: 0.688
    std: 0.024
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 19
    is_best: false
  - model: GAT
    value: 0.685
    std: 0.028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 104
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
  - model: Lie Unitary GCN
    value: 0.9611
    std: 0.001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: Unitary GCN
    value: 0.9427
    std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 28
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
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 39
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
    table_ref: Table 2
    source_ref: Platonov 2023
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
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 52
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
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 5
    is_best: false
  metric: ROC-AUC
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
  - model: Wide Unitary GCN
    value: 0.756
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: Unitary GCN
    value: 0.751
    std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 64
    is_best: false
  - model: GAT
    value: 0.726
    std: 0.008
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
  - model: GCN
    value: 0.706
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    global_rank: 37
    is_best: false
  - model: GIN
    value: 0.697
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    global_rank: 31
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: CRaWl
    value: 0.4588
    std: 0.0079
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GPS
    value: 0.444
    std: 0.0065
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    global_rank: 9
    is_best: false
  - model: Lie UniGCN
    value: 0.4005
    std: 0.0067
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 30
    is_best: false
  - model: Exphormer
    value: 0.396
    std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 32
    is_best: false
  - model: GatedGCN
    value: 0.388
    std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: Tonshoff 2023
    global_rank: 16
    is_best: false
  - model: UniGCN
    value: 0.3516
    std: 0.007
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: DRew
    value: 0.3314
    std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: GINE
    value: 0.2718
    std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: Tonshoff 2023
    global_rank: 77
    is_best: false
  - model: GCN
    value: 0.2078
    std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: Tonshoff 2023
    global_rank: 43
    is_best: false
  metric: F1
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
  - model: Lie Unitary GCN
    value: 0.8001
    std: 0.0043
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 5
    is_best: true
  - model: Unitary GCN
    value: 0.7921
    std: 0.0079
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 9
    is_best: true
  - model: GT
    value: 0.7795
    std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 21
    is_best: false
  - model: GAT
    value: 0.7743
    std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 20
    is_best: false
  - model: SAGE
    value: 0.7644
    std: 0.0062
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 41
    is_best: false
  - model: GCN
    value: 0.7609
    std: 0.0127
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 10
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
  - model: Unitary GCN
    value: 0.8721
    std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: this paper
    global_rank: 35
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
    table_ref: tab:platonov
    source_ref: Platonov 2023
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
    table_ref: tab:platonov
    source_ref: Platonov 2023
    global_rank: 44
    is_best: false
  - model: Lie Unitary GCN
    value: 0.855
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: tab:platonov
    source_ref: this paper
    global_rank: 47
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
    table_ref: tab:platonov
    source_ref: Platonov 2023
    global_rank: 24
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
    table_ref: tab:platonov
    source_ref: Platonov 2023
    global_rank: 18
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
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
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
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: Lie Unitary GCN
    value: 0.8518
    std: 0.0043
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 15
    is_best: true
  - model: Unitary GCN
    value: 0.8483
    std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 24
    is_best: true
  - model: GAT
    value: 0.837
    std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 45
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
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 41
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
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 52
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
    table_ref: Table 2
    source_ref: Platonov 2023
    global_rank: 58
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
- benchmark: LRGB
  datasets:
  - *id006
- benchmark: TU Dortmund
  datasets:
  - *id007
  - *id008
  - *id009
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id010
main_figure: /figures/2410.05499/main_figure.png
---

