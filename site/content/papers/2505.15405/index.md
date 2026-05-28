---
title: 'HOPSE: Scalable Higher-Order Positional and Structural Encoder for Combinatorial
  Representations'
arxiv_id: '2505.15405'
source_url: ''
authors: []
published_date: May 2025
published_date_iso: 2025-05
abstract: While Graph Neural Networks (GNNs) have proven highly effective at modeling
  relational data, pairwise connections cannot fully capture multi-way relationships
  naturally present in complex real-world systems. In response to this, Topological
  Deep Learning (TDL) leverages more general combinatorial representations ---such
  as simplicial or cellular complexes--- to accommodate higher-order interactions.
  Existing TDL methods often extend GNNs through Higher-Order Message Passing (HOMP),
  but face critical scalability challenges due to (i) a combinatorial explosion of
  message-passing routes, and (ii) significant complexity overhead from the propagation
  mechanism.blueThis work presents HOPSE (Higher-Order Positional and Structural Encoder),
  an alternative method to solve tasks involving higher-order interactions without
  message passing. Instead, HOPSE breaks apart arbitrary higher-order domains into
  it's neighborhood relationships using a Hasse graph decompositions. This method
  shows that decoupling the representation learning of the topology of each neighborhood
  and the attributes results in a lower computational complexity, putting into question
  the need for HOMP.The experiments on molecular graph tasks and topological benchmarks
  show that HOPSE matches performance in traditional TDL datasets and outperforms
  HOMP methods in topological tasks, all while achieving up to $7 $ speedups over
  HOMP-based models, opening a new path for scalable TDL.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- HOPSE-M
- HOPSE-G
mrr: 0.0145
adjusted_mrr: 0.0145
mrr_dataset_count: 4
benchmark_categories:
- Classic
- TU Dortmund
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id003
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.984
    std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.984
    sort_std: 0.024
    is_best: true
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6979
    std: 0.068
    paper_value: 0.6979
    paper_std: 0.068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1, Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 22
    true_value: 0.901
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20310000000000006
    value_note: ''
    paper_rank: 160
    rank_delta: 138
    rank_delta_abs: 138
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: null
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7957
    std: 0.0613
    paper_value: 0.7957
    paper_std: 0.0613
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09830000000000005
    value_note: ''
    paper_rank: 106
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: HOPSE-M
    model_key: hopse-m
    model_plain: HOPSE-M
    value: 0.8638
    std: 0.0631
    paper_value: 0.8638
    paper_std: 0.0631
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1, Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 55
    true_value: 0.8638
    true_std: 0.0631
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8638
    sort_std: 0.0631
    is_best: false
  - model: GCCN
    model_key: gccn
    model_plain: GCCN
    value: 0.8596
    std: 0.0466
    paper_value: 0.8596
    paper_std: 0.0466
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1, Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 57
    true_value: 0.8596
    true_std: 0.0466
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8596
    sort_std: 0.0466
    is_best: false
  - model: HOPSE-G
    model_key: hopse-g
    model_plain: HOPSE-G
    value: 0.8553
    std: 0.0277
    paper_value: 0.8553
    paper_std: 0.0277
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1, Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 62
    true_value: 0.8553
    true_std: 0.0277
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8553
    sort_std: 0.0277
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.8426
    std: 0.0356
    paper_value: 0.8426
    paper_std: 0.0356
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 67
    true_value: 0.8426
    true_std: 0.0356
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8426
    sort_std: 0.0356
    is_best: false
  - model: CWN
    model_key: cwn
    model_plain: CWN
    value: 0.8043
    std: 0.0178
    paper_value: 0.8043
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 99
    true_value: 0.8043
    true_std: 0.0178
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8043
    sort_std: 0.0178
    is_best: false
  - model: GAT+PSEs
    model_key: gat+pses
    model_plain: GAT+PSEs
    value: 0.8043
    std: 0.0508
    paper_value: 0.8043
    paper_std: 0.0508
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 100
    true_value: 0.8043
    true_std: 0.0508
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8043
    sort_std: 0.0508
    is_best: false
  - model: SaNN
    model_key: sann
    model_plain: SaNN
    value: 0.7957
    std: 0.0356
    paper_value: 0.7957
    paper_std: 0.0356
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 107
    true_value: 0.7957
    true_std: 0.0356
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7957
    sort_std: 0.0356
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7277
    std: 0.0277
    paper_value: 0.7277
    paper_std: 0.0277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1, Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 117
    true_value: 0.7871
    true_std: 0.0751
    value_gap_source_arxiv: '2310.05174'
    value_gap_source_title: 'GSLB: The Graph Structure Learning Benchmark'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.05940000000000001
    value_note: global 0.7871 within std
    paper_rank: 148
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.7871
    sort_std: 0.0751
    is_best: false
  - model: CCCN
    model_key: cccn
    model_plain: CCCN
    value: 0.7702
    std: 0.0932
    paper_value: 0.7702
    paper_std: 0.0932
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 126
    true_value: 0.7702
    true_std: 0.0932
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7702
    sort_std: 0.0932
    is_best: false
  - model: SCCNN
    model_key: sccnn
    model_plain: SCCNN
    value: 0.7617
    std: 0.0663
    paper_value: 0.7617
    paper_std: 0.0663
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1, Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 130
    true_value: 0.7617
    true_std: 0.0663
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 130
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7617
    sort_std: 0.0663
    is_best: false
  - model: SCN
    model_key: scn
    model_plain: SCN
    value: 0.7362
    std: 0.0613
    paper_value: 0.7362
    paper_std: 0.0613
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 144
    true_value: 0.7362
    true_std: 0.0613
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7362
    sort_std: 0.0613
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: NCI1
  is_multi_metric: true
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    metric_values:
    - 0.865
    - null
    metric_stds:
    - 0.014
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.17311'
    title: Probabilistic Graph Rewiring via Virtual Nodes
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.865
    sort_std: 0.014
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    metric_values:
    - 0.86
    - null
    metric_stds:
    - 0.018
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
    sort_value: 0.86
    sort_std: 0.018
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    metric_values:
    - 0.8583
    - null
    metric_stds:
    - 0.0086
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
    sort_value: 0.8583
    sort_std: 0.0086
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.7426
    - 0.7442
    metric_stds:
    - 0.0096
    - 0.007
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.827
    sort_std: 0.017
    true_value: 0.827
    true_std: 0.017
    paper_value: 0.7426
    paper_std: 0.0096
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08439999999999992
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 18
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.7286
    - 0.722
    metric_stds:
    - 0.0069
    - 0.0122
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.802
    sort_std: 0.02
    true_value: 0.802
    true_std: 0.02
    paper_value: 0.7286
    paper_std: 0.0069
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07340000000000002
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 33
  - model: GAT+PSEs
    model_key: gat+pses
    model_plain: GAT+PSEs
    metric_values:
    - 0.7786
    - null
    metric_stds:
    - 0.0102
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7786
    sort_std: 0.0102
    true_value: 0.7786
    true_std: 0.0102
    paper_value: 0.7786
    paper_std: 0.0102
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 45
  - model: HOPSE-G
    model_key: hopse-g
    model_plain: HOPSE-G
    metric_values:
    - 0.777
    - 0.7636
    metric_stds:
    - 0.014
    - 0.0175
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.777
    sort_std: 0.014
    true_value: 0.777
    true_std: 0.014
    paper_value: 0.777
    paper_std: 0.014
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 46
  - model: HOPSE-M
    model_key: hopse-m
    model_plain: HOPSE-M
    metric_values:
    - 0.7735
    - 0.7634
    metric_stds:
    - 0.0081
    - 0.014
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7735
    sort_std: 0.0081
    true_value: 0.7735
    true_std: 0.0081
    paper_value: 0.7735
    paper_std: 0.0081
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 50
  - model: GAT
    model_key: gat
    model_plain: GAT
    metric_values:
    - 0.75
    - 0.738
    metric_stds:
    - 0.01
    - 0.0073
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.773
    sort_std: 0.025
    true_value: 0.773
    true_std: 0.025
    paper_value: 0.75
    paper_std: 0.01
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02300000000000002
    value_gap_source_arxiv: '2306.05955'
    value_gap_source_title: 'Path Neural Networks: Expressive and Accurate Graph Neural
      Networks'
    value_note: global 0.7730 within std
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 51
  - model: GCCN
    model_key: gccn
    model_plain: GCCN
    metric_values:
    - 0.7685
    - 0.7576
    metric_stds:
    - 0.015
    - 0.0128
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7685
    sort_std: 0.015
    true_value: 0.7685
    true_std: 0.015
    paper_value: 0.7685
    paper_std: 0.015
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 56
  - model: CCCN
    model_key: cccn
    model_plain: CCCN
    metric_values:
    - 0.7667
    - 0.7535
    metric_stds:
    - 0.0148
    - 0.015
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7667
    sort_std: 0.0148
    true_value: 0.7667
    true_std: 0.0148
    paper_value: 0.7667
    paper_std: 0.0148
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 57
  - model: SCCNN
    model_key: sccnn
    model_plain: SCCNN
    metric_values:
    - 0.766
    - 0.7712
    metric_stds:
    - 0.0175
    - 0.0107
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.766
    sort_std: 0.0175
    true_value: 0.766
    true_std: 0.0175
    paper_value: 0.766
    paper_std: 0.0175
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 58
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    metric_values:
    - 0.7488
    - null
    metric_stds:
    - 0.0054
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7488
    sort_std: 0.0054
    true_value: 0.7488
    true_std: 0.0054
    paper_value: 0.7488
    paper_std: 0.0054
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 68
  - model: SCN
    model_key: scn
    model_plain: SCN
    metric_values:
    - 0.7449
    - 0.757
    metric_stds:
    - 0.0103
    - 0.0104
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7449
    sort_std: 0.0103
    true_value: 0.7449
    true_std: 0.0103
    paper_value: 0.7449
    paper_std: 0.0103
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 69
  - model: CWN
    model_key: cwn
    model_plain: CWN
    metric_values:
    - 0.7393
    - 0.738
    metric_stds:
    - 0.0187
    - 0.0206
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7393
    sort_std: 0.0187
    true_value: 0.7393
    true_std: 0.0187
    paper_value: 0.7393
    paper_std: 0.0187
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 70
  - model: SaNN
    model_key: sann
    model_plain: SaNN
    metric_values:
    - 0.6875
    - null
    metric_stds:
    - 0.0164
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6875
    sort_std: 0.0164
    true_value: 0.6875
    true_std: 0.0164
    paper_value: 0.6875
    paper_std: 0.0164
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 80
  metrics:
  - Accuracy
  - ACC
  primary_metric: Accuracy
  higher_is_better: true
- &id002
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.854
    sort_std: 0.044
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.807
    std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02156'
    title: Probabilistically Rewired Message-Passing Neural Networks
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.807
    sort_std: 0.039
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7634
    std: 0.0166
    paper_value: 0.7634
    paper_std: 0.0166
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 28
    true_value: 0.7634
    true_std: 0.0166
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7634
    sort_std: 0.0166
    is_best: false
  - model: HOPSE-G
    model_key: hopse-g
    model_plain: HOPSE-G
    value: 0.7627
    std: 0.021
    paper_value: 0.7627
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 30
    true_value: 0.7627
    true_std: 0.021
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7627
    sort_std: 0.021
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.752
    std: 0.033
    paper_value: 0.752
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010000000000000009
    value_note: global 0.7620 within std
    paper_rank: 55
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: CWN
    model_key: cwn
    model_plain: CWN
    value: 0.7613
    std: 0.027
    paper_value: 0.7613
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 36
    true_value: 0.7613
    true_std: 0.027
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7613
    sort_std: 0.027
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.757
    std: 0.0214
    paper_value: 0.757
    paper_std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.7600 within std
    paper_rank: 45
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.7577
    std: 0.0298
    paper_value: 0.7577
    paper_std: 0.0298
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 45
    true_value: 0.7577
    true_std: 0.0298
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7577
    sort_std: 0.0298
    is_best: false
  - model: GAT+PSEs
    model_key: gat+pses
    model_plain: GAT+PSEs
    value: 0.7548
    std: 0.0344
    paper_value: 0.7548
    paper_std: 0.0344
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 51
    true_value: 0.7548
    true_std: 0.0344
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7548
    sort_std: 0.0344
    is_best: false
  - model: SCN
    model_key: scn
    model_plain: SCN
    value: 0.7527
    std: 0.0214
    paper_value: 0.7527
    paper_std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 55
    true_value: 0.7527
    true_std: 0.0214
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7527
    sort_std: 0.0214
    is_best: false
  - model: HOPSE-M
    model_key: hopse-m
    model_plain: HOPSE-M
    value: 0.7513
    std: 0.0366
    paper_value: 0.7513
    paper_std: 0.0366
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 61
    true_value: 0.7513
    true_std: 0.0366
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7513
    sort_std: 0.0366
    is_best: false
  - model: SaNN
    model_key: sann
    model_plain: SaNN
    value: 0.7505
    std: 0.0352
    paper_value: 0.7505
    paper_std: 0.0352
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 67
    true_value: 0.7505
    true_std: 0.0352
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7505
    sort_std: 0.0352
    is_best: false
  - model: GCCN
    model_key: gccn
    model_plain: GCCN
    value: 0.7491
    std: 0.0251
    paper_value: 0.7491
    paper_std: 0.0251
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 76
    true_value: 0.7491
    true_std: 0.0251
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7491
    sort_std: 0.0251
    is_best: false
  - model: SCCNN
    model_key: sccnn
    model_plain: SCCNN
    value: 0.7419
    std: 0.0286
    paper_value: 0.7419
    paper_std: 0.0286
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 87
    true_value: 0.7419
    true_std: 0.0286
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7419
    sort_std: 0.0286
    is_best: false
  - model: CCCN
    model_key: cccn
    model_plain: CCCN
    value: 0.7333
    std: 0.023
    paper_value: 0.7333
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 108
    true_value: 0.7333
    true_std: 0.023
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7333
    sort_std: 0.023
    is_best: false
  metric: Accuracy
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.57
    std: 0.04
    paper_value: 0.57
    paper_std: 0.04
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5049999999999999
    value_note: ''
    paper_rank: 296
    rank_delta: 221
    rank_delta_abs: 221
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.62
    std: 0.01
    paper_value: 0.62
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.544
    value_note: ''
    paper_rank: 299
    rank_delta: 168
    rank_delta_abs: 168
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.61
    std: 0.01
    paper_value: 0.61
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 142
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.5323645103769521
    value_note: ''
    paper_rank: 299
    rank_delta: 157
    rank_delta_abs: 157
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  - model: CCCN
    model_key: cccn
    model_plain: CCCN
    value: 0.34
    std: 0.02
    paper_value: 0.34
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 277
    true_value: 0.34
    true_std: 0.02
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 277
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34
    sort_std: 0.02
    is_best: false
  - model: CWN
    model_key: cwn
    model_plain: CWN
    value: 0.34
    std: 0.01
    paper_value: 0.34
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 278
    true_value: 0.34
    true_std: 0.01
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 278
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34
    sort_std: 0.01
    is_best: false
  - model: GCCN
    model_key: gccn
    model_plain: GCCN
    value: 0.35
    std: 0.01
    paper_value: 0.35
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 280
    true_value: 0.35
    true_std: 0.01
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 280
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35
    sort_std: 0.01
    is_best: false
  - model: SCCNN
    model_key: sccnn
    model_plain: SCCNN
    value: 0.36
    std: 0.02
    paper_value: 0.36
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 283
    true_value: 0.36
    true_std: 0.02
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 283
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.36
    sort_std: 0.02
    is_best: false
  - model: HOPSE-M
    model_key: hopse-m
    model_plain: HOPSE-M
    value: 0.39
    std: 0.02
    paper_value: 0.39
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 286
    true_value: 0.39
    true_std: 0.02
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 286
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.02
    is_best: false
  - model: HOPSE-M
    model_key: hopse-m
    model_plain: HOPSE-M
    value: 0.39
    std: 0.02
    paper_value: 0.39
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 286
    true_value: 0.39
    true_std: 0.02
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 286
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.02
    is_best: false
  - model: GAT+PSEs
    model_key: gat+pses
    model_plain: GAT+PSEs
    value: 0.39
    std: 0.02
    paper_value: 0.39
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 287
    true_value: 0.39
    true_std: 0.02
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 287
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.39
    sort_std: 0.02
    is_best: false
  - model: GPSE + GCN
    model_key: gpse + gcn
    model_plain: GPSE + GCN
    value: 0.43
    std: 0.03
    paper_value: 0.43
    paper_std: 0.03
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 292
    true_value: 0.43
    true_std: 0.03
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 292
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.43
    sort_std: 0.03
    is_best: false
  - model: HOPSE-G
    model_key: hopse-g
    model_plain: HOPSE-G
    value: 0.43
    std: 0.01
    paper_value: 0.43
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 291
    true_value: 0.43
    true_std: 0.01
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 291
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.43
    sort_std: 0.01
    is_best: false
  - model: HOPSE-G
    model_key: hopse-g
    model_plain: HOPSE-G
    value: 0.43
    std: 0.01
    paper_value: 0.43
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 291
    true_value: 0.43
    true_std: 0.01
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 291
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.43
    sort_std: 0.01
    is_best: false
  - model: SCN
    model_key: scn
    model_plain: SCN
    value: 0.53
    std: 0.04
    paper_value: 0.53
    paper_std: 0.04
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 294
    true_value: 0.53
    true_std: 0.04
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 294
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.53
    sort_std: 0.04
    is_best: false
  - model: SaNN
    model_key: sann
    model_plain: SaNN
    value: 0.55
    std: 0.01
    paper_value: 0.55
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    global_rank: 296
    true_value: 0.55
    true_std: 0.01
    value_gap_source_arxiv: '2505.15405'
    value_gap_source_title: 'HOPSE: Scalable Higher-Order Positional and Structural
      Encoder for Combinatorial Representations'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 296
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.55
    sort_std: 0.01
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
  - *id003
  - *id004
main_figure: /figures/2505.15405/main_figure.png
---

