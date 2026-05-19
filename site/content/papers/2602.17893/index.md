---
title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs with Context Gating
  State Space Models'
arxiv_id: '2602.17893'
authors: []
published_date: Feb 2026
abstract: 'State space models (SSMs) have recently emerged for modeling long-range
  dependency in sequence data, with much simplified computational costs than modern
  alternatives, such as transformers. Advancing SMMs to graph structured data, especially
  for large graphs, is a significant challenge because SSMs are sequence models and
  the shear graph volumes make it very expensive to convert graphs as sequences for
  effective learning. In this paper, we propose COMBA to tackle large graph learning
  using state space models, with two key innovations: graph context gating and cross
  batch aggregation. Graph context refers to different hops of neighborhood for each
  node, and graph context gating allows COMBA to use such context to learn best control
  of neighbor aggregation. For each graph context, COMBA samples nodes as batches,
  and train a graph neural network (GNN), with information being aggregated cross
  batches, allowing COMBA to scale to large graphs. Our theoretical study asserts
  that cross-batch aggregation guarantees lower error than training GNN without aggregation.
  Experiments on benchmark networks demonstrate significant performance gains compared
  to baseline approaches. Code and benchmark datasets will be released for public
  access.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- COMBA
mrr: 0.0274
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
  - model: GAT
    value: 0.5554
    std: 0.0051
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
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: COMBA
    value: 0.507
    std: 0.0025
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
  - model: Nagphormer
    value: 0.504
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 42
    is_best: false
  - model: Graph Mamba-1
    value: 0.49
    std: 0.0036
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
  - model: GatedGCN
    value: 0.481
    std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 61
    is_best: false
  - model: Cluster-GCN
    value: 0.476
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 66
    is_best: false
  - model: GCN
    value: 0.462
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 17
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
  - model: COMBA
    value: 0.942
    std: 0.0039
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 30
    is_best: false
  - model: Graph Mamba-1
    value: 0.927
    std: 0.0021
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: GatedGCN
    value: 0.905
    std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 69
    is_best: false
  - model: Nagphormer
    value: 0.903
    std: 0.0006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: Cluster-GCN
    value: 0.886
    std: 0.0024
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 81
    is_best: false
  - model: GCN
    value: 0.884
    std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
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
  - model: COMBA
    value: 0.895
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: Graph Mamba-1
    value: 0.869
    std: 0.0092
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
  - model: GatedGCN
    value: 0.833
    std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: Cluster-GCN
    value: 0.815
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 64
    is_best: false
  - model: Nagphormer
    value: 0.8
    std: 0.0043
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
  - model: GCN
    value: 0.795
    std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
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
  - model: COMBA
    value: 0.845
    std: 0.0009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 33
    is_best: false
  - model: GCN
    value: 0.838
    std: 0.0034
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: Nagphormer
    value: 0.834
    std: 0.0045
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GatedGCN
    value: 0.832
    std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: Graph Mamba-1
    value: 0.803
    std: 0.0199
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: Cluster-GCN
    value: 0.758
    std: 0.0056
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id005
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
  - model: COMBA
    value: 0.716
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 66
    is_best: false
  - model: GatedGCN
    value: 0.701
    std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 78
    is_best: false
  - model: Nagphormer
    value: 0.696
    std: 0.0023
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
  - model: Graph Mamba-1
    value: 0.686
    std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: GCN
    value: 0.68
    std: 0.0044
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
  - model: Cluster-GCN
    value: 0.678
    std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 84
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
- benchmark: OGB
  datasets:
  - *id005
single_proposed_model: COMBA
main_figure: /figures/2602.17893/main_figure.png
---

