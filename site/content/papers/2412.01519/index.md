---
title: ': Linear Complexity Graph Transformers Adaptive Hub-Spoke Reassignment'
arxiv_id: '2412.01519'
authors: []
published_date: Dec 2024
abstract: We present , a novel graph transformer architecture that achieves linear
  complexity through an efficient reassignment technique between nodes and virtual
  nodes. Graph transformers have become increasingly important in graph learning for
  their ability to utilize long-range node communication explicitly, addressing limitations
  such as oversmoothing and oversquashing found in message-passing graph networks.
  However, their dense attention mechanism scales quadratically with the number of
  nodes, limiting their applicability to large-scale graphs. draws inspiration from
  the airline industry's hub-and-spoke model, where flights are assigned to optimize
  operational efficiency. In our approach, graph nodes (spokes) are dynamically reassigned
  to a fixed number of virtual nodes (hubs) at each model layer. Recent work, Neural
  Atoms~li2024neural, has demonstrated impressive and consistent improvements over
  GNN baselines by utilizing such virtual nodes; their findings suggest that the number
  of hubs strongly influences performance. However, increasing the number of hubs
  typically raises complexity, requiring a trade-off to maintain linear complexity.
  Our key insight is that each node only needs to interact with a small subset of
  hubs to achieve linear complexity, even when the total number of hubs is large.
  To leverage all hubs without incurring additional computational costs, we propose
  a simple yet effective adaptive reassignment technique based on hub-hub similarity
  scores, eliminating the need for expensive node-hub computations. Our experiments
  on long-range graph benchmarks indicate a consistent improvement in results over
  the base method, Neural Atoms, while maintaining a linear complexity instead of
  $O(n^3/2)$. Remarkably, our sparse model achieves performance on par with its non-sparse
  counterpart. Furthermore, outperforms competitive baselines and consistently ranks
  among the top performers across various benchmarks. Code is available on our project
  webpagehttps://tomerborreda.github.io/rehub/.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- + ReHub-FC
- + ReHub
mrr: 0.0312
results:
- &id004
  dataset: PCQM-Contact
  rows:
  - model: FloydNet
    value: 0.6143
    std: null
    metric: MRR
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
  - model: ViT-PS
    value: 0.5341
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: NeuralWalker
    value: 0.4707
    std: 0.0007
    metric: MRR
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
    global_rank: 3
    is_best: false
  - model: Exphormer
    value: 0.3637
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: + ReHub
    value: 0.3534
    std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: + ReHub-FC
    value: 0.3526
    std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: SAN+LapPE
    value: 0.335
    std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: GraphGPS
    value: 0.3337
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: + NeuralAtoms
    value: 0.3262
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.3242
    std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: GatedGCN
    value: 0.3218
    std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GINE
    value: 0.318
    std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: Transformer+LapPE
    value: 0.3174
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 60
    is_best: false
  - model: GCN2
    value: 0.3161
    std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: GCN
    value: 0.2329
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 7
    is_best: false
  metric: MRR
  higher_is_better: true
- &id003
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
  - model: Exphormer
    value: 0.3975
    std: 0.0037
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shirzad2023exphormer
    global_rank: 32
    is_best: false
  - model: + ReHub
    value: 0.386
    std: 0.0172
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GraphGPS
    value: 0.3748
    std: 0.0109
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampavsek2022recipe
    global_rank: 45
    is_best: false
  - model: + ReHub-FC
    value: 0.3526
    std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 53
    is_best: false
  - model: SAN+LapPE
    value: 0.323
    std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 58
    is_best: false
  - model: Transformer+LapPE
    value: 0.2694
    std: 0.0098
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 1
    source_ref: this paper
    global_rank: 78
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
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
  - model: + ReHub-FC
    value: 0.6732
    std: 0.0107
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 120
    is_best: false
  - model: + ReHub
    value: 0.6685
    std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 132
    is_best: false
  - model: + NeuralAtoms
    value: 0.6591
    std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: li2024neural
    global_rank: 154
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
    table_ref: Table tab:lrgb-baseline
    source_ref: rampavsek2022recipe
    global_rank: 162
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
    table_ref: Table tab:lrgb-baseline
    source_ref: shirzad2023exphormer
    global_rank: 174
    is_best: false
  - model: SAN+LapPE
    value: 0.6384
    std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 204
    is_best: false
  - model: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 209
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 131
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GatedGCN
    value: 0.5864
    std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: GCN2
    value: 0.5543
    std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 274
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 140
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
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
  - model: Exphormer
    value: 0.2481
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 92
    is_best: false
  - model: + ReHub
    value: 0.2488
    std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 107
    is_best: false
  - model: + ReHub-FC
    value: 0.2489
    std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 110
    is_best: false
  - model: GraphGPS
    value: 0.25
    std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 120
    is_best: false
  - model: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 147
    is_best: false
  - model: + NeuralAtoms
    value: 0.2553
    std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 170
    is_best: false
  - model: SAN+LapPE
    value: 0.2683
    std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    global_rank: 213
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCN2
    value: 0.3471
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 268
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
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
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    global_rank: 71
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
main_figure: /figures/2412.01519/main_figure.png
---

