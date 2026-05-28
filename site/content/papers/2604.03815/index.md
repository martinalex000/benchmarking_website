---
title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive
  Power of GraphGPS
arxiv_id: '2604.03815'
source_url: ''
authors: []
published_date: Apr 2026
published_date_iso: 2026-04
abstract: 'Abstract Graph transformers have shown promise in overcoming limitations
  of traditional graph neural networks, such as oversquashing and difficulties in
  modelling long-range dependencies. However, their application to large-scale graphs
  is hindered by the quadratic memory and computational complexity of the all-to-all
  attention mechanism. Although alternatives such as linearized attention and restricted
  attention patterns have been proposed, these often degrade performance or limit
  expressive power. To better balance efficiency and effectiveness, we introduce k-Maximum
  Inner Product (k-MIP) attention for graph transformers. k-MIP attention selects
  the most relevant key nodes per query via a top-k operation, yielding a sparse yet
  flexible attention pattern. Combined with an attention score computation based on
  symbolic matrices, this results in linear memory complexity and practical speedups
  of up to an order of magnitude compared to all-to-all attention, enabling the processing
  of graphs with over 500k nodes on a single A100 GPU. We provide a theoretical analysis
  of expressive power, showing that k-MIP attention does not compromise the expressiveness
  of graph transformers: specifically, we prove that k-MIP transformers can approximate
  any full-attention transformer to arbitrary precision. In addition, we analyze the
  expressive power of the GraphGPS framework, in which we integrate our attention
  mechanism, and establish an upper bound on its graph distinguishing capability in
  terms of the S-SEG-WL test. Finally, we validate our approach on the Long Range
  Graph Benchmark, the City-Networks benchmark, and two custom large-scale inductive
  point cloud datasets, consistently ranking among the top-performing scalable graph
  transformers.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GPS + k-MIP
- GPS + k-MIP (k=1)
- GraphGPS with k-MIP attention (k=1)
mrr: 0.0194
adjusted_mrr: 0.0194
mrr_dataset_count: 4
benchmark_categories:
- LRGB
- GNNBenchmark
- Other Graph Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id005
  dataset: CIFAR10
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.8375
    std: 0.00141
    metric: Accuracy
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
    sort_value: 0.8375
    sort_std: 0.00141
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.80027
    std: 0.00185
    metric: Accuracy
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
    sort_value: 0.80027
    sort_std: 0.00185
    is_best: false
  - model: RandAlign (4 layers)
    model_key: randalign (4 layers)
    model_plain: RandAlign (4 layers)
    value: 0.7942
    std: 0.00072
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_display: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7942
    sort_std: 0.00072
    is_best: false
  - model: GraphGPS with k-MIP attention (k=1)
    model_key: graphgps with k-mip attention (k=1)
    model_plain: GraphGPS with k-MIP attention (k=1)
    value: 0.7565000000000001
    std: 0.0044
    paper_value: 0.7565000000000001
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 33
    true_value: 0.7565000000000001
    true_std: 0.0044
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7565000000000001
    sort_std: 0.0044
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: COCO-SP
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.4901
    std: null
    metric: F1
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
    sort_value: 0.4901
    sort_std: null
    is_best: true
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.4752
    std: 0.0032
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
    global_rank: 2
    sort_value: 0.4752
    sort_std: 0.0032
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4483
    sort_std: 0.0070999999999999995
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.3884
    std: 0.0055000000000000005
    paper_value: 0.3884
    paper_std: 0.0055000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 15
    true_value: 0.3884
    true_std: 0.0055000000000000005
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3884
    sort_std: 0.0055000000000000005
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.3884
    std: 0.0055000000000000005
    paper_value: 0.3884
    paper_std: 0.0055000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 17
    true_value: 0.3884
    true_std: 0.0055000000000000005
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3884
    sort_std: 0.0055000000000000005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2922
    std: 0.0018
    paper_value: 0.2922
    paper_std: 0.0018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 21
    true_value: 0.3802
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08799999999999997
    value_note: ''
    paper_rank: 43
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.3802
    sort_std: 0.0015
    is_best: false
  - model: GPS + k-MIP
    model_key: gps + k-mip
    model_plain: GPS + k-MIP
    value: 0.3556
    std: 0.0045000000000000005
    paper_value: 0.3556
    paper_std: 0.0045000000000000005
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 26
    true_value: 0.3556
    true_std: 0.0045000000000000005
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3556
    sort_std: 0.0045000000000000005
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.3525
    std: 0.0027
    paper_value: 0.3525
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 27
    true_value: 0.3525
    true_std: 0.0027
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3525
    sort_std: 0.0027
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3455
    std: 0.0009
    paper_value: 0.3455
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 31
    true_value: 0.3455
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3455
    sort_std: 0.0009
    is_best: false
  - model: GPS + Performer
    model_key: gps + performer
    model_plain: GPS + Performer
    value: 0.27699999999999997
    std: 0.0027
    paper_value: 0.27699999999999997
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 44
    true_value: 0.27699999999999997
    true_std: 0.0027
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.27699999999999997
    sort_std: 0.0027
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1338
    std: 0.0007000000000000001
    paper_value: 0.1338
    paper_std: 0.0007000000000000001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 45
    true_value: 0.2733
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13949999999999999
    value_note: ''
    paper_rank: 68
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.2733
    sort_std: 0.0041
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.1886
    std: 0.0011
    paper_value: 0.1886
    paper_std: 0.0011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 46
    true_value: 0.2697
    true_std: 0.0011
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0811
    value_note: ''
    paper_rank: 64
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.2697
    sort_std: 0.0011
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2125
    std: 0.0009
    paper_value: 0.2125
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 64
    true_value: 0.2125
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2125
    sort_std: 0.0009
    is_best: false
  metric: F1
  higher_is_better: true
- &id006
  dataset: MalNet-Tiny
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.948
    std: 0.00424
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.948
    sort_std: 0.00424
    is_best: true
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.946
    std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.946
    sort_std: 0.0057
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9437
    std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9437
    sort_std: 0.0058
    is_best: true
  - model: GraphGPS with k-MIP attention (k=1)
    model_key: graphgps with k-mip attention (k=1)
    model_plain: GraphGPS with k-MIP attention (k=1)
    value: 0.934
    std: 0.005699999999999999
    paper_value: 0.934
    paper_std: 0.005699999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 14
    true_value: 0.934
    true_std: 0.005699999999999999
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.934
    sort_std: 0.005699999999999999
    is_best: false
  metric: Accuracy
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
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.444
    std: 0.006500000000000001
    paper_value: 0.444
    paper_std: 0.006500000000000001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 10
    true_value: 0.444
    true_std: 0.006500000000000001
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.444
    sort_std: 0.006500000000000001
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.444
    std: 0.006500000000000001
    paper_value: 0.444
    paper_std: 0.006500000000000001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 12
    true_value: 0.444
    true_std: 0.006500000000000001
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.444
    sort_std: 0.006500000000000001
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.38799999999999996
    std: 0.004
    paper_value: 0.38799999999999996
    paper_std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 19
    true_value: 0.4263
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.038300000000000056
    value_note: ''
    paper_rank: 42
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.4263
    sort_std: 0.0057
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
    source_ref: Shirzad 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
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
  - model: GPS + k-MIP
    model_key: gps + k-mip
    model_plain: GPS + k-MIP
    value: 0.3969
    std: 0.0092
    paper_value: 0.3969
    paper_std: 0.0092
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 37
    true_value: 0.3969
    true_std: 0.0092
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3969
    sort_std: 0.0092
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.3875
    std: 0.0064
    paper_value: 0.3875
    paper_std: 0.0064
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 43
    true_value: 0.3875
    true_std: 0.0064
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3875
    sort_std: 0.0064
    is_best: false
  - model: GPS + Performer
    model_key: gps + performer
    model_plain: GPS + Performer
    value: 0.37920000000000004
    std: 0.0113
    paper_value: 0.37920000000000004
    paper_std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 45
    true_value: 0.37920000000000004
    true_std: 0.0113
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37920000000000004
    sort_std: 0.0113
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2078
    std: 0.0031
    paper_value: 0.2078
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1682
    value_note: ''
    paper_rank: 95
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.27149999999999996
    std: 0.0049
    paper_value: 0.27149999999999996
    paper_std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 49
    true_value: 0.37
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09850000000000003
    value_note: ''
    paper_rank: 80
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.37
    sort_std: 0.001
    is_best: false
  - model: GraphGPS + k-MIP (k=1)
    model_key: graphgps + k-mip (k=1)
    model_plain: GraphGPS + k-MIP (k=1)
    value: 0.369
    std: 0.0033
    paper_value: 0.369
    paper_std: 0.0033
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 50
    true_value: 0.369
    true_std: 0.0033
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.369
    sort_std: 0.0033
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2718
    std: 0.0054
    paper_value: 0.2718
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 80
    true_value: 0.2718
    true_std: 0.0054
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2718
    sort_std: 0.0054
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
    value: 0.6859999999999999
    std: 0.005
    paper_value: 0.6859999999999999
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040100000000000025
    value_note: ''
    paper_rank: 89
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6765000000000001
    std: 0.004699999999999999
    paper_value: 0.6765000000000001
    paper_std: 0.004699999999999999
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0240999999999999
    value_note: ''
    paper_rank: 110
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6787000000000001
    std: 0.005600000000000001
    paper_value: 0.6787000000000001
    paper_std: 0.005600000000000001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 78
    true_value: 0.6924
    true_std: 0.0044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013699999999999934
    value_note: ''
    paper_rank: 110
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.6924
    sort_std: 0.0044
    is_best: false
  - model: GPS + k-MIP
    model_key: gps + k-mip
    model_plain: GPS + k-MIP
    value: 0.6627
    std: 0.0044
    paper_value: 0.6627
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 139
    true_value: 0.6627
    true_std: 0.0044
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6627
    sort_std: 0.0044
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.6620999999999999
    std: 0.0067
    paper_value: 0.6620999999999999
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS + Performer
    model_key: gps + performer
    model_plain: GPS + Performer
    value: 0.6606000000000001
    std: 0.0064
    paper_value: 0.6606000000000001
    paper_std: 0.0064
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 152
    true_value: 0.6606000000000001
    true_std: 0.0064
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6606000000000001
    sort_std: 0.0064
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.6534
    std: 0.0091
    paper_value: 0.6534
    paper_std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 171
    true_value: 0.6535
    true_std: 0.0041
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.6535 within std
    paper_rank: 172
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6535
    sort_std: 0.0041
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.6534
    std: 0.0091
    paper_value: 0.6534
    paper_std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 174
    true_value: 0.6534
    true_std: 0.0091
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6534
    sort_std: 0.0091
    is_best: false
  - model: GPS + k-MIP (k=1)
    model_key: gps + k-mip (k=1)
    model_plain: GPS + k-MIP (k=1)
    value: 0.6529
    std: 0.0034000000000000002
    paper_value: 0.6529
    paper_std: 0.0034000000000000002
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 176
    true_value: 0.6529
    true_std: 0.0034000000000000002
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6529
    sort_std: 0.0034000000000000002
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
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.6483
    std: 0.0073
    paper_value: 0.6483
    paper_std: 0.0073
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 187
    true_value: 0.6483
    true_std: 0.0073
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 187
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6483
    sort_std: 0.0073
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
    value: 0.246
    std: 0.0007
    paper_value: 0.246
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.003899999999999987
    value_note: ''
    paper_rank: 54
    rank_delta: 51
    rank_delta_abs: 51
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
    value: 0.2477
    std: 0.0009
    paper_value: 0.2477
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.004599999999999993
    value_note: ''
    paper_rank: 89
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2473
    std: 0.0017
    paper_value: 0.2473
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    table_ref: Table 1
    source_ref: Shirzad 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.2488
    std: 0.0018
    paper_value: 0.2488
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 120
    true_value: 0.2488
    true_std: 0.0018
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2488
    sort_std: 0.0018
    is_best: false
  - model: GPS w/ Transformer
    model_key: gps w/ transformer
    model_plain: GPS w/ Transformer
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 140
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 148
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: Graph transformer
    model_key: graph transformer
    model_plain: Graph transformer
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 150
    true_value: 0.2509
    true_std: 0.0014
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 150
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2509
    sort_std: 0.0014
    is_best: false
  - model: GPS + k-MIP
    model_key: gps + k-mip
    model_plain: GPS + k-MIP
    value: 0.2562
    std: 0.0037
    paper_value: 0.2562
    paper_std: 0.0037
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 197
    true_value: 0.2562
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2562
    sort_std: 0.0037
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.2566
    std: 0.0019
    paper_value: 0.2566
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 201
    true_value: 0.2566
    true_std: 0.0019
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2566
    sort_std: 0.0019
    is_best: false
  - model: GPS + Performer
    model_key: gps + performer
    model_plain: GPS + Performer
    value: 0.2643
    std: 0.0008
    paper_value: 0.2643
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 231
    true_value: 0.2643
    true_std: 0.0008
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 231
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2643
    sort_std: 0.0008
    is_best: false
  metric: MAE
  higher_is_better: false
- &id007
  dataset: ShapeNet-Part
  rows:
  - model: GPS + k-MIP
    model_key: gps + k-mip
    model_plain: GPS + k-MIP
    value: 0.8268000000000001
    std: 0.0064
    paper_value: 0.8268000000000001
    paper_std: 0.0064
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 1
    true_value: 0.8268000000000001
    true_std: 0.0064
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8268000000000001
    sort_std: 0.0064
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8262
    std: 0.0031
    paper_value: 0.8262
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 2
    true_value: 0.8262
    true_std: 0.0031
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8262
    sort_std: 0.0031
    is_best: true
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.7965000000000001
    std: 0.0098
    paper_value: 0.7965000000000001
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
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 3
    true_value: 0.7965000000000001
    true_std: 0.0098
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7965000000000001
    sort_std: 0.0098
    is_best: false
  - model: GPS + Performer
    model_key: gps + performer
    model_plain: GPS + Performer
    value: 0.7736
    std: 0.0123
    paper_value: 0.7736
    paper_std: 0.0123
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 4
    true_value: 0.7736
    true_std: 0.0123
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7736
    sort_std: 0.0123
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.762
    std: 0.0032
    paper_value: 0.762
    paper_std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 5
    true_value: 0.762
    true_std: 0.0032
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.0032
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.6456999999999999
    std: 0.0034999999999999996
    paper_value: 0.6456999999999999
    paper_std: 0.0034999999999999996
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 6
    true_value: 0.6456999999999999
    true_std: 0.0034999999999999996
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6456999999999999
    sort_std: 0.0034999999999999996
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6301
    std: 0.0017000000000000001
    paper_value: 0.6301
    paper_std: 0.0017000000000000001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 7
    true_value: 0.6301
    true_std: 0.0017000000000000001
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6301
    sort_std: 0.0017000000000000001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6018
    std: 0.0004
    paper_value: 0.6018
    paper_std: 0.0004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    global_rank: 8
    true_value: 0.6018
    true_std: 0.0004
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6018
    sort_std: 0.0004
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: GNNBenchmark
  datasets:
  - *id005
- benchmark: Other Graph Benchmarks
  datasets:
  - *id006
  - *id007
---

