---
title: 'ReHub: Linear Complexity Graph Transformers with Adaptive Hub-Spoke Reassignment'
arxiv_id: '2412.01519'
source_url: ''
authors: []
published_date: Dec 2024
published_date_iso: 2024-12
abstract: We present, a novel graph transformer architecture that achieves linear
  complexity through an efficient reassignment technique between nodes and virtual
  nodes. Graph transformers have become increasingly important in graph learning for
  their ability to utilize long-range node communication explicitly, addressing limitations
  such as oversmoothing and oversquashing found in message-passing graph networks.
  However, their dense attention mechanism scales quadratically with the number of
  nodes, limiting their applicability to large-scale graphs. draws inspiration from
  the airline industry's hub-and-spoke model, where flights are assigned to optimize
  operational efficiency. In our approach, graph nodes (spokes) are dynamically reassigned
  to a fixed number of virtual nodes (hubs) at each model layer. Recent work, Neural
  Atoms li2024neural, has demonstrated impressive and consistent improvements over
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
paper_type: method
proposed_models:
- + ReHub-FC
- + ReHub
mrr: 0.0304
adjusted_mrr: 0.0304
mrr_dataset_count: 4
benchmark_categories:
- LRGB
task_categories:
- graph_classification
- graph_regression
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id004
  dataset: PCQM-Contact
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
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
    date_display: Jan 2026
    date_iso: 2026-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.6143
    sort_std: null
    is_best: true
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
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
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.5341
    sort_std: null
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4707
    std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs via Random Walks
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4707
    sort_std: 0.0007
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3218
    std: 0.0011
    paper_value: 0.3218
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 5
    true_value: 0.467
    true_std: 0.0004
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14520000000000005
    value_note: ''
    paper_rank: 61
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.467
    sort_std: 0.0004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2329
    std: 0.0009
    paper_value: 0.2329
    paper_std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 7
    true_value: 0.4526
    true_std: 0.0006
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2197
    value_note: ''
    paper_rank: 70
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.4526
    sort_std: 0.0006
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3637
    std: 0.002
    paper_value: 0.3637
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 10
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: + ReHub
    model_key: + rehub
    model_plain: + ReHub
    value: 0.3534
    std: 0.0014
    paper_value: 0.3534
    paper_std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 12
    true_value: 0.3534
    true_std: 0.0014
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3534
    sort_std: 0.0014
    is_best: false
  - model: + ReHub-FC
    model_key: + rehub-fc
    model_plain: + ReHub-FC
    value: 0.3526
    std: 0.0014
    paper_value: 0.3526
    paper_std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 13
    true_value: 0.3526
    true_std: 0.0014
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3526
    sort_std: 0.0014
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.318
    std: 0.0027
    paper_value: 0.318
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 17
    true_value: 0.3509
    true_std: 0.0006
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.032899999999999985
    value_note: ''
    paper_rank: 61
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.3509
    sort_std: 0.0006
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.335
    std: 0.0003
    paper_value: 0.335
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 45
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3337
    std: 0.0006
    paper_value: 0.3337
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 49
    true_value: 0.3337
    true_std: 0.0006
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3337
    sort_std: 0.0006
    is_best: false
  - model: + NeuralAtoms
    model_key: + neuralatoms
    model_plain: + NeuralAtoms
    value: 0.3262
    std: 0.001
    paper_value: 0.3262
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 56
    true_value: 0.3262
    true_std: 0.001
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3262
    sort_std: 0.001
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3242
    std: 0.0008
    paper_value: 0.3242
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 60
    true_value: 0.3242
    true_std: 0.0008
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3242
    sort_std: 0.0008
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.3174
    std: 0.002
    paper_value: 0.3174
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 62
    true_value: 0.3174
    true_std: 0.002
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3174
    sort_std: 0.002
    is_best: false
  - model: GCN2
    model_key: gcn2
    model_plain: GCN2
    value: 0.3161
    std: 0.0004
    paper_value: 0.3161
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 65
    true_value: 0.3161
    true_std: 0.0004
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3161
    sort_std: 0.0004
    is_best: false
  metric: MRR
  higher_is_better: true
- &id003
  dataset: PascalVOC-SP
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.567
    std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.567
    sort_std: 0.0049
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4912
    std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.05649'
    title: 'Greener GRASS: Enhancing GNNs with Encoding, Rewiring, and Attention'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4912
    sort_std: 0.0042
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4653
    std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2401.01233'
    title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph
      Modeling'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3975
    std: 0.0037
    paper_value: 0.3975
    paper_std: 0.0037
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: + ReHub
    model_key: + rehub
    model_plain: + ReHub
    value: 0.386
    std: 0.0172
    paper_value: 0.386
    paper_std: 0.0172
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 44
    true_value: 0.386
    true_std: 0.0172
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.386
    sort_std: 0.0172
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3748
    std: 0.0109
    paper_value: 0.3748
    paper_std: 0.0109
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 48
    true_value: 0.3748
    true_std: 0.0109
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3748
    sort_std: 0.0109
    is_best: false
  - model: + ReHub-FC
    model_key: + rehub-fc
    model_plain: + ReHub-FC
    value: 0.3526
    std: 0.0045
    paper_value: 0.3526
    paper_std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 56
    true_value: 0.3526
    true_std: 0.0045
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3526
    sort_std: 0.0045
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.323
    std: 0.0039
    paper_value: 0.323
    paper_std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 61
    true_value: 0.323
    true_std: 0.0039
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.323
    sort_std: 0.0039
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2694
    std: 0.0098
    paper_value: 0.2694
    paper_std: 0.0098
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 81
    true_value: 0.2694
    true_std: 0.0098
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2694
    sort_std: 0.0098
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 261
    rank_delta: 252
    rank_delta_abs: 252
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 273
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: + ReHub-FC
    model_key: + rehub-fc
    model_plain: + ReHub-FC
    value: 0.6732
    std: 0.0107
    paper_value: 0.6732
    paper_std: 0.0107
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 122
    true_value: 0.6732
    true_std: 0.0107
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6732
    sort_std: 0.0107
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    paper_value: 0.6069
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 133
    true_value: 0.6685
    true_std: 0.0062
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06159999999999999
    value_note: ''
    paper_rank: 239
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.6685
    sort_std: 0.0062
    is_best: false
  - model: + ReHub
    model_key: + rehub
    model_plain: + ReHub
    value: 0.6685
    std: 0.0074
    paper_value: 0.6685
    paper_std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 134
    true_value: 0.6685
    true_std: 0.0074
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6685
    sort_std: 0.0074
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.5498
    std: 0.0079
    paper_value: 0.5498
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 288
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: + NeuralAtoms
    model_key: + neuralatoms
    model_plain: + NeuralAtoms
    value: 0.6591
    std: 0.005
    paper_value: 0.6591
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: li2024neural
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 157
    true_value: 0.6591
    true_std: 0.005
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6591
    sort_std: 0.005
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 166
    true_value: 0.655
    true_std: 0.004
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015000000000000568
    value_note: global 0.6550 within std
    paper_rank: 168
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.655
    sort_std: 0.004
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6527
    std: 0.0043
    paper_value: 0.6527
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 212
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    paper_value: 0.6326
    paper_std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 217
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GCN2
    model_key: gcn2
    model_plain: GCN2
    value: 0.5543
    std: 0.0078
    paper_value: 0.5543
    paper_std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 286
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 286
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: 0.0013
    paper_value: 0.342
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2481
    std: 0.0007
    paper_value: 0.2481
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: + ReHub
    model_key: + rehub
    model_plain: + ReHub
    value: 0.2488
    std: 0.0017
    paper_value: 0.2488
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 121
    true_value: 0.2488
    true_std: 0.0017
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2488
    sort_std: 0.0017
    is_best: false
  - model: + ReHub-FC
    model_key: + rehub-fc
    model_plain: + ReHub-FC
    value: 0.2489
    std: 0.0011
    paper_value: 0.2489
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 125
    true_value: 0.2489
    true_std: 0.0011
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2489
    sort_std: 0.0011
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 136
    true_value: 0.25
    true_std: 0.0012
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0012
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 168
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    paper_value: 0.3357
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 167
    true_value: 0.2529
    true_std: 0.0009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08279999999999998
    value_note: ''
    paper_rank: 289
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.2529
    sort_std: 0.0009
    is_best: false
  - model: + NeuralAtoms
    model_key: + neuralatoms
    model_plain: + NeuralAtoms
    value: 0.2553
    std: 0.0005
    paper_value: 0.2553
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 194
    true_value: 0.2553
    true_std: 0.0005
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2553
    sort_std: 0.0005
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0043
    paper_value: 0.2683
    paper_std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:lrgb-baseline
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 242
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2680 within std
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GCN2
    model_key: gcn2
    model_plain: GCN2
    value: 0.3471
    std: 0.001
    paper_value: 0.3471
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table lrgb-vs-na
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 301
    true_value: 0.3471
    true_std: 0.001
    value_gap_source_arxiv: '2412.01519'
    value_gap_source_title: 'ReHub: Linear Complexity Graph Transformers with Adaptive
      Hub-Spoke Reassignment'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 301
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3471
    sort_std: 0.001
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

