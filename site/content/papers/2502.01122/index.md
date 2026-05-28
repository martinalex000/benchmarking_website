---
title: Learning Efficient Positional Encodings with Graph Neural Networks
arxiv_id: '2502.01122'
source_url: ''
authors: []
published_date: Feb 2025
published_date_iso: 2025-02
abstract: 'Positional encodings (PEs) are essential for effective graph representation
  learning because they provide position awareness in inherently position-agnostic
  transformer architectures and increase the expressive capacity of Graph Neural Networks
  (GNNs). However, designing powerful and efficient PEs for graphs poses significant
  challenges due to the absence of canonical node ordering and the scale of the graph.
  In this work, we identify four key properties that graph PEs should satisfy: stability,
  expressive power, scalability, and genericness. We find that existing eigenvector-based
  PE methods often fall short of jointly satisfying these criteria. To address this
  gap, we introduce, a novel framework of learnable PEs for graphs. Our primary insight
  is that message-passing GNNs function as nonlinear mappings of eigenvectors, enabling
  the design of GNN architectures for generating powerful and efficient PEs. A crucial
  challenge lies in initializing node attributes in a manner that is both expressive
  and permutation equivariant. We tackle this by initializing GNNs with random node
  inputs or standard basis vectors, thereby unlocking the expressive power of message-passing
  operations, while employing statistical pooling functions to maintain permutation
  equivariance. Our analysis demonstrates that approximates equivariant functions
  of eigenvectors with linear complexity, while rigorously establishing its stability
  and high expressive power. Experimental evaluations show that outperforms lightweight
  versions of eigenvector-based PEs and achieves comparable performance to full eigenvector-based
  PEs, but with one or two orders of magnitude lower complexity. Our code is available
  at https://github.com/ehejin/Pearl-PE.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- SignNet
- R-method
- B-method
mrr: 0.6698
adjusted_mrr: 0.6698
mrr_dataset_count: 3
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- GNNBenchmark
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id007
  dataset: CSL
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: ''
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 1
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: Apr 4, 2024
    date_display: Apr 2024
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: Transformer+RWSE
    model_key: transformer+rwse
    model_plain: Transformer+RWSE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: Apr 4, 2024
    date_display: Apr 2024
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: A_2+LapPE
    model_key: a_2+lappe
    model_plain: A_2+LapPE
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.03380'
    title: On the Theoretical Expressive Power and the Design Space of Higher-Order
      Graph Transformers
    date: Apr 4, 2024
    date_display: Apr 2024
    date_iso: '2024-04-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: Message-passing GNNs with WL-related PEs
    model_key: message-passing gnns with wl-related pes
    model_plain: Message-passing GNNs with WL-related PEs
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: ''
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 37
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: D&D
  is_multi_metric: true
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    metric_values:
    - 0.989
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.989
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    metric_values:
    - 0.981
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.981
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    metric_values:
    - 0.976
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.976
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: SPE
    model_key: spe
    model_plain: SPE
    metric_values:
    - null
    - 0.9294
    metric_stds:
    - null
    - 0.0015
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9294
    sort_std: 0.0015
    true_value: null
    true_std: null
    paper_value: 0.9294
    paper_std: 0.0015
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: R-method
    model_key: r-method
    model_plain: R-method
    metric_values:
    - null
    - 0.9292
    metric_stds:
    - null
    - 0.0012
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9292
    sort_std: 0.0012
    true_value: null
    true_std: null
    paper_value: 0.9292
    paper_std: 0.0012
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SPE-8S
    model_key: spe-8s
    model_plain: SPE-8S
    metric_values:
    - null
    - 0.9262
    metric_stds:
    - null
    - 0.001
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9262
    sort_std: 0.001
    true_value: null
    true_std: null
    paper_value: 0.9262
    paper_std: 0.001
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: PEG
    model_key: peg
    model_plain: PEG
    metric_values:
    - null
    - 0.9257
    metric_stds:
    - null
    - 0.0022
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9257
    sort_std: 0.0022
    true_value: null
    true_std: null
    paper_value: 0.9257
    paper_std: 0.0022
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: B-method
    model_key: b-method
    model_plain: B-method
    metric_values:
    - null
    - 0.9081
    metric_stds:
    - null
    - 0.0079
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.9081
    sort_std: 0.0079
    true_value: null
    true_std: null
    paper_value: 0.9081
    paper_std: 0.0079
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: BasisNet
    model_key: basisnet
    model_plain: BasisNet
    metric_values:
    - null
    - 0.8942
    metric_stds:
    - null
    - 0.0118
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.8942
    sort_std: 0.0118
    true_value: null
    true_std: null
    paper_value: 0.8942
    paper_std: 0.0118
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SignNet
    model_key: signnet
    model_plain: SignNet
    metric_values:
    - 0.1086
    - 0.9243
    metric_stds:
    - null
    - 0.0027
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.1086
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.1086
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    metric_values:
    - 0.1086
    - null
    metric_stds:
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.1086
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.1086
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    metric_values:
    - 0.1073
    - 0.9289
    metric_stds:
    - null
    - 0.0014
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.1073
    sort_std: null
    true_value: null
    true_std: null
    paper_value: 0.1073
    paper_std: null
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  metrics:
  - MAP
  - ROC-AUC
  primary_metric: Accuracy
  higher_is_better: true
- &id003
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
    value: 0.2421
    std: 0.0016
    metric: MAE
    higher_is_better: false
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
    global_rank: 3
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.245
    std: 0.002
    paper_value: 0.245
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
    value_note: global 0.2449 within std
    paper_rank: 33
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.247
    std: 0.001
    paper_value: 0.247
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 72
    true_value: 0.247
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.247
    sort_std: 0.001
    is_best: false
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 0.248
    std: 0.001
    paper_value: 0.248
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 100
    true_value: 0.248
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.248
    sort_std: 0.001
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.25
    std: 0.001
    paper_value: 0.25
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: frasca_2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 131
    true_value: 0.2498
    true_std: 0.0008
    value_gap_source_arxiv: '2311.04653'
    value_gap_source_title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00020000000000000573
    value_note: global 0.2498 within std
    paper_rank: 134
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.2498
    sort_std: 0.0008
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.252
    std: 0.001
    paper_value: 0.252
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0020000000000000018
    value_note: ''
    paper_rank: 158
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.255
    std: 0.001
    paper_value: 0.255
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kruezer_2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 188
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005000000000000004
    value_note: global 0.2545 within std
    paper_rank: 190
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.268
    std: 0.004
    paper_value: 0.268
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kruezer_2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 242
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.274
    std: 0.0
    paper_value: 0.274
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2022from
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 250
    true_value: 0.274
    true_std: 0.0
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 250
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.274
    sort_std: 0.0
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: REDDIT-BINARY
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.945
    std: 0.004
    paper_value: 0.945
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 1
    true_value: 0.945
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.9199
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9199
    sort_std: 0.0159
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.918
    std: 0.01
    paper_value: 0.918
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.918
    true_std: 0.01
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.01
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.918
    std: 0.016
    paper_value: 0.918
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.918
    true_std: 0.016
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.918
    sort_std: 0.016
    is_best: false
  - model: GSN with cliques
    model_key: gsn with cliques
    model_plain: GSN with cliques
    value: 0.911
    std: 0.018
    paper_value: 0.911
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 5
    true_value: 0.911
    true_std: 0.018
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.911
    sort_std: 0.018
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.904
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.904
    sort_std: 0.008
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.89
    std: 0.052
    paper_value: 0.89
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.89
    true_std: 0.052
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.89
    sort_std: 0.052
    is_best: true
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8801
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 2.26
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.8801
    sort_std: 0.0019
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5
    std: 0.0
    paper_value: 0.5
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 36
    true_value: 0.5
    true_std: 0.0
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: REDDIT-MULTI-5K
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.606
    std: 0.003
    paper_value: 0.606
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 1
    true_value: 0.606
    true_std: 0.003
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.003
    is_best: true
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.57
    std: 0.021
    paper_value: 0.57
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 0.57
    true_std: 0.021
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.569
    std: 0.02
    paper_value: 0.569
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.569
    true_std: 0.02
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.569
    sort_std: 0.02
    is_best: false
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.5673
    std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.5673
    sort_std: 0.0196
    is_best: false
  - model: LaGraph
    model_key: lagraph
    model_plain: LaGraph
    value: 0.564
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.564
    sort_std: 0.004
    is_best: false
  - model: GSN with cliques
    model_key: gsn with cliques
    model_plain: GSN with cliques
    value: 0.562
    std: 0.018
    paper_value: 0.562
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 6
    true_value: 0.562
    true_std: 0.018
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.562
    sort_std: 0.018
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.552
    std: 0.029
    paper_value: 0.552
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.552
    true_std: 0.029
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.552
    sort_std: 0.029
    is_best: false
  - model: AD-GCL-OPT
    model_key: ad-gcl-opt
    model_plain: AD-GCL-OPT
    value: 0.5493
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.5493
    sort_std: 0.0043
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2
    std: 0.0
    paper_value: 0.2
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 33
    true_value: 0.2
    true_std: 0.0
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2
    sort_std: 0.0
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: true
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: true
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.606
    std: 0.003
    paper_value: 0.606
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.606
    sort_std: 0.003
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.57
    std: 0.021
    paper_value: 0.57
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.57
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.569
    std: 0.02
    paper_value: 0.569
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.569
    sort_std: 0.02
    is_best: false
  - model: GSN with cliques
    model_key: gsn with cliques
    model_plain: GSN with cliques
    value: 0.562
    std: 0.018
    paper_value: 0.562
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.562
    sort_std: 0.018
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.552
    std: 0.029
    paper_value: 0.552
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.552
    sort_std: 0.029
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2
    std: 0.0
    paper_value: 0.2
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:RGNN-REDDIT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: null
    sort_value: 0.2
    sort_std: 0.0
    is_best: false
  metric: F1
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
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
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
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
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
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
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: SignNet
    model_key: signnet
    model_plain: SignNet
    value: 0.0853
    std: 0.0026
    paper_value: 0.0853
    paper_std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0613
    value_note: ''
    paper_rank: 164
    rank_delta: 149
    rank_delta_abs: 149
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 0.0644
    std: 0.001
    paper_value: 0.0644
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 74
    true_value: 0.0644
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0644
    sort_std: 0.001
    is_best: false
  - model: B-method
    model_key: b-method
    model_plain: B-method
    value: 0.0644
    std: 0.001
    paper_value: 0.0644
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:stability_expressiveness}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 74
    true_value: 0.0644
    true_std: 0.001
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0644
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.209
    std: 0.018
    paper_value: 0.209
    paper_std: 0.018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.144
    value_note: ''
    paper_rank: 261
    rank_delta: 186
    rank_delta_abs: 186
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.0693
    std: 0.004
    paper_value: 0.0693
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 106
    true_value: 0.0693
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0693
    sort_std: 0.004
    is_best: false
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.0699
    std: 0.002
    paper_value: 0.0699
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 107
    true_value: 0.0699
    true_std: 0.002
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0699
    sort_std: 0.002
    is_best: false
  - model: SPE-8S
    model_key: spe-8s
    model_plain: SPE-8S
    value: 0.0736
    std: 0.0007
    paper_value: 0.0736
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 123
    true_value: 0.0736
    true_std: 0.0007
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0736
    sort_std: 0.0007
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.469
    std: 0.002
    paper_value: 0.469
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.39299999999999996
    value_note: ''
    paper_rank: 293
    rank_delta: 162
    rank_delta_abs: 162
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: SignNet-8S
    model_key: signnet-8s
    model_plain: SignNet-8S
    value: 0.1034
    std: 0.0056
    paper_value: 0.1034
    paper_std: 0.0056
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 191
    true_value: 0.1034
    true_std: 0.0056
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 191
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1034
    sort_std: 0.0056
    is_best: false
  - model: GSN with cycles
    model_key: gsn with cycles
    model_plain: GSN with cycles
    value: 0.115
    std: 0.012
    paper_value: 0.115
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 201
    true_value: 0.115
    true_std: 0.012
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.115
    sort_std: 0.012
    is_best: false
  - model: BasisNet-8S
    model_key: basisnet-8s
    model_plain: BasisNet-8S
    value: 0.1554
    std: 0.0048
    paper_value: 0.1554
    paper_std: 0.0048
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 240
    true_value: 0.1554
    true_std: 0.0048
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 240
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1554
    sort_std: 0.0048
    is_best: false
  - model: BasisNet
    model_key: basisnet
    model_plain: BasisNet
    value: 0.1555
    std: 0.0124
    paper_value: 0.1555
    paper_std: 0.0124
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 241
    true_value: 0.1555
    true_std: 0.0124
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 241
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1555
    sort_std: 0.0124
    is_best: false
  - model: NoPE
    model_key: nope
    model_plain: NoPE
    value: 0.1772
    std: 0.004
    paper_value: 0.1772
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 248
    true_value: 0.1772
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 248
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1772
    sort_std: 0.004
    is_best: false
  - model: GIN + rand id
    model_key: gin + rand id
    model_plain: GIN + rand id
    value: 0.279
    std: 0.023
    paper_value: 0.279
    paper_std: 0.023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 270
    true_value: 0.279
    true_std: 0.023
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 270
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.279
    sort_std: 0.023
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: GNNBenchmark
  datasets:
  - *id007
main_figure: /figures/2502.01122/main_figure.png
---

