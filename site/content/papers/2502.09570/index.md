---
title: Enhancing the Utility of Higher-Order Information in Relational Learning
arxiv_id: '2502.09570'
source_url: ''
authors: []
published_date: Feb 2025
published_date_iso: 2025-02
abstract: Higher-order information is crucial for relational learning in many domains
  where relationships extend beyond pairwise interactions. Hypergraphs provide a natural
  framework for modeling such relationships, which has motivated recent extensions
  of graph neural network architectures to hypergraphs. However, comparisons between
  hypergraph architectures and standard graph-level models remain limited. In this
  work, we systematically evaluate a selection of hypergraph-level and graph-level
  architectures, to determine their effectiveness in leveraging higher-order information
  in relational learning. Our results show that graph-level architectures applied
  to hypergraph expansions often outperform hypergraph-level ones, even on inputs
  that are naturally parametrized as hypergraphs. As an alternative approach for leveraging
  higher-order information, we propose hypergraph-level encodings based on classical
  hypergraph characteristics. While these encodings do not significantly improve hypergraph
  architectures, they yield substantial performance gains when combined with graph-level
  models. Our theoretical analysis shows that hypergraph-level encodings provably
  increase the representational power of message-passing graph neural networks beyond
  that of their graph-level counterparts.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- UniGAT (HCP-FRC)
- UniGAT (LDP)
- UniGAT (Hodge H-20-LAPE)
- UniGAT (Norm. H-20-LAPE)
- UniGAT (H-19-RWPEE EE)
- UniGAT (H-19-RWPEE WE)
- UniGAT (no encodings nlayer2)
- UniGCN (HCP-FRC)
- UniGCN (LDP)
- UniGCN (H-19-RWPEE EN)
- UniGCN (no encodings)
- UniSAGE (HCP-FRC)
- UniSAGE (LDP)
- UniSAGE (no encodings)
- UniGCNII (HCP-FRC depth 2)
- UniGCNII (LDP depth 2)
- UniGCNII (Hodge H-20-LAPE depth 2)
- UniGCNII (Norm. H-20-LAPE depth 2)
- UniGCNII (H-19-RWPEE EE depth 2)
- UniGCNII (no encodings depth 2)
- UniGCNII (H-19-RWPEE WE depth 8)
- GCN (LCP-FRC)
- GCN (LCP-ORC)
- GCN (19-RWPE)
- GCN (20-LAPE)
- GCN (EE H-19-RWPE)
- GCN (Hodge H-20-LAPE)
- GCN (Norm. H-20-LAPE)
- GPS (LCP-FRC)
- GPS (LCP-ORC)
- GPS (19-RWPE)
- GPS (20-LAPE)
- GPS (EN H-19-RWPE)
mrr: 0.0051
adjusted_mrr: 0.0051
mrr_dataset_count: 3
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- Hypergraph Benchmarks
- Heterogeneous Graph Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id010
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
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
    global_rank: 1
    sort_value: 0.8722
    sort_std: 0.0013
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.8672
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.8615
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.7592
    std: 0.0133
    paper_value: 0.7592
    paper_std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 32
    true_value: 0.7592
    true_std: 0.0133
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7592
    sort_std: 0.0133
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.7474
    std: 0.0123
    paper_value: 0.7474
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 38
    true_value: 0.7474
    true_std: 0.0123
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7474
    sort_std: 0.0123
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.7429
    std: 0.0142
    paper_value: 0.7429
    paper_std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 41
    true_value: 0.7429
    true_std: 0.0142
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7429
    sort_std: 0.0142
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.7418
    std: 0.0122
    paper_value: 0.7418
    paper_std: 0.0122
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 42
    true_value: 0.7418
    true_std: 0.0122
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7418
    sort_std: 0.0122
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.7417
    std: 0.0133
    paper_value: 0.7417
    paper_std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 43
    true_value: 0.7417
    true_std: 0.0133
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7417
    sort_std: 0.0133
    is_best: false
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.7337
    std: 0.0159
    paper_value: 0.7337
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 47
    true_value: 0.7337
    true_std: 0.0159
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7337
    sort_std: 0.0159
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.726
    std: 0.0128
    paper_value: 0.726
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 56
    true_value: 0.726
    true_std: 0.0128
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.0128
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.7232
    std: 0.0142
    paper_value: 0.7232
    paper_std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 60
    true_value: 0.7232
    true_std: 0.0142
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7232
    sort_std: 0.0142
    is_best: false
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.7218
    std: 0.0137
    paper_value: 0.7218
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 61
    true_value: 0.7218
    true_std: 0.0137
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7218
    sort_std: 0.0137
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.7216
    std: 0.0139
    paper_value: 0.7216
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 62
    true_value: 0.7216
    true_std: 0.0139
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7216
    sort_std: 0.0139
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.7196
    std: 0.013
    paper_value: 0.7196
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 68
    true_value: 0.7196
    true_std: 0.013
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7196
    sort_std: 0.013
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.7195
    std: 0.0135
    paper_value: 0.7195
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 69
    true_value: 0.7195
    true_std: 0.0135
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7195
    sort_std: 0.0135
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.7176
    std: 0.0134
    paper_value: 0.7176
    paper_std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 71
    true_value: 0.7176
    true_std: 0.0134
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7176
    sort_std: 0.0134
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.7152
    std: 0.0126
    paper_value: 0.7152
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 73
    true_value: 0.7152
    true_std: 0.0126
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7152
    sort_std: 0.0126
    is_best: false
  - model: GIN (HCP-FRC)
    model_key: gin (hcp-frc)
    model_plain: GIN (HCP-FRC)
    value: 0.7144
    std: 0.0146
    paper_value: 0.7144
    paper_std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 74
    true_value: 0.7144
    true_std: 0.0146
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7144
    sort_std: 0.0146
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.6744
    std: 0.0113
    paper_value: 0.6744
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 91
    true_value: 0.6744
    true_std: 0.0113
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6744
    sort_std: 0.0113
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
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
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
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
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
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
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    model_key: unigcnii (hodge h-20-lape depth 2)
    model_plain: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.6538
    std: 0.0153
    paper_value: 0.6538
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 164
    true_value: 0.6538
    true_std: 0.0153
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6538
    sort_std: 0.0153
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    model_key: unigcnii (h-19-rwpee ee depth 2)
    model_plain: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.6538
    std: 0.0156
    paper_value: 0.6538
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 165
    true_value: 0.6538
    true_std: 0.0156
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6538
    sort_std: 0.0156
    is_best: false
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    model_key: unigcnii (norm. h-20-lape depth 2)
    model_plain: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.6525
    std: 0.016
    paper_value: 0.6525
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 166
    true_value: 0.6525
    true_std: 0.016
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6525
    sort_std: 0.016
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    model_key: unigcnii (no encodings depth 2)
    model_plain: UniGCNII (no encodings depth 2)
    value: 0.6524
    std: 0.0167
    paper_value: 0.6524
    paper_std: 0.0167
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 167
    true_value: 0.6524
    true_std: 0.0167
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6524
    sort_std: 0.0167
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    model_key: unigcnii (h-19-rwpee we depth 8)
    model_plain: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.652
    std: 0.0152
    paper_value: 0.652
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 168
    true_value: 0.652
    true_std: 0.0152
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.652
    sort_std: 0.0152
    is_best: false
  - model: UniGCNII (LDP depth 2)
    model_key: unigcnii (ldp depth 2)
    model_plain: UniGCNII (LDP depth 2)
    value: 0.636
    std: 0.0161
    paper_value: 0.636
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 177
    true_value: 0.636
    true_std: 0.0161
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 177
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.636
    sort_std: 0.0161
    is_best: false
  - model: UniGAT (no encodings nlayer2)
    model_key: unigat (no encodings nlayer2)
    model_plain: UniGAT (no encodings nlayer2)
    value: 0.6325
    std: 0.0148
    paper_value: 0.6325
    paper_std: 0.0148
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
    global_rank: 178
    true_value: 0.6325
    true_std: 0.0148
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6325
    sort_std: 0.0148
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    model_key: unigcnii (hcp-frc depth 2)
    model_plain: UniGCNII (HCP-FRC depth 2)
    value: 0.6293
    std: 0.0145
    paper_value: 0.6293
    paper_std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 180
    true_value: 0.6293
    true_std: 0.0145
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6293
    sort_std: 0.0145
    is_best: false
  - model: UniGAT (LDP)
    model_key: unigat (ldp)
    model_plain: UniGAT (LDP)
    value: 0.6207
    std: 0.0168
    paper_value: 0.6207
    paper_std: 0.0168
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
    global_rank: 185
    true_value: 0.6207
    true_std: 0.0168
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 185
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6207
    sort_std: 0.0168
    is_best: false
  - model: UniGAT (HCP-FRC)
    model_key: unigat (hcp-frc)
    model_plain: UniGAT (HCP-FRC)
    value: 0.6108
    std: 0.0185
    paper_value: 0.6108
    paper_std: 0.0185
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
    global_rank: 190
    true_value: 0.6108
    true_std: 0.0185
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6108
    sort_std: 0.0185
    is_best: false
  - model: UniGCN (no encodings)
    model_key: unigcn (no encodings)
    model_plain: UniGCN (no encodings)
    value: 0.6056
    std: 0.0231
    paper_value: 0.6056
    paper_std: 0.0231
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 192
    true_value: 0.6056
    true_std: 0.0231
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 192
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6056
    sort_std: 0.0231
    is_best: false
  - model: UniSAGE (no encodings)
    model_key: unisage (no encodings)
    model_plain: UniSAGE (no encodings)
    value: 0.6056
    std: 0.021
    paper_value: 0.6056
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 193
    true_value: 0.6056
    true_std: 0.021
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 193
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6056
    sort_std: 0.021
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    model_key: unigat (hodge h-20-lape)
    model_plain: UniGAT (Hodge H-20-LAPE)
    value: 0.6055
    std: 0.0202
    paper_value: 0.6055
    paper_std: 0.0202
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
    global_rank: 194
    true_value: 0.6055
    true_std: 0.0202
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6055
    sort_std: 0.0202
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    model_key: unigat (norm. h-20-lape)
    model_plain: UniGAT (Norm. H-20-LAPE)
    value: 0.6054
    std: 0.0219
    paper_value: 0.6054
    paper_std: 0.0219
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
    global_rank: 195
    true_value: 0.6054
    true_std: 0.0219
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6054
    sort_std: 0.0219
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    model_key: unigcn (h-19-rwpee en)
    model_plain: UniGCN (H-19-RWPEE EN)
    value: 0.603
    std: 0.0233
    paper_value: 0.603
    paper_std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 197
    true_value: 0.603
    true_std: 0.0233
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.603
    sort_std: 0.0233
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    model_key: unigat (h-19-rwpee ee)
    model_plain: UniGAT (H-19-RWPEE EE)
    value: 0.6029
    std: 0.0217
    paper_value: 0.6029
    paper_std: 0.0217
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
    global_rank: 198
    true_value: 0.6029
    true_std: 0.0217
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 198
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6029
    sort_std: 0.0217
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    model_key: unigat (h-19-rwpee we)
    model_plain: UniGAT (H-19-RWPEE WE)
    value: 0.6022
    std: 0.0222
    paper_value: 0.6022
    paper_std: 0.0222
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
    global_rank: 199
    true_value: 0.6022
    true_std: 0.0222
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 199
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6022
    sort_std: 0.0222
    is_best: false
  - model: UniSAGE (LDP)
    model_key: unisage (ldp)
    model_plain: UniSAGE (LDP)
    value: 0.5997
    std: 0.0227
    paper_value: 0.5997
    paper_std: 0.0227
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 200
    true_value: 0.5997
    true_std: 0.0227
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 200
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5997
    sort_std: 0.0227
    is_best: false
  - model: UniGCN (LDP)
    model_key: unigcn (ldp)
    model_plain: UniGCN (LDP)
    value: 0.5988
    std: 0.0237
    paper_value: 0.5988
    paper_std: 0.0237
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 203
    true_value: 0.5988
    true_std: 0.0237
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 203
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5988
    sort_std: 0.0237
    is_best: false
  - model: UniGCN (HCP-FRC)
    model_key: unigcn (hcp-frc)
    model_plain: UniGCN (HCP-FRC)
    value: 0.591
    std: 0.0184
    paper_value: 0.591
    paper_std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 204
    true_value: 0.591
    true_std: 0.0184
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 204
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.591
    sort_std: 0.0184
    is_best: false
  - model: UniSAGE (HCP-FRC)
    model_key: unisage (hcp-frc)
    model_plain: UniSAGE (HCP-FRC)
    value: 0.591
    std: 0.0229
    paper_value: 0.591
    paper_std: 0.0229
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 205
    true_value: 0.591
    true_std: 0.0229
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 205
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.591
    sort_std: 0.0229
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    model_key: unigcnii (norm. h-20-lape depth 2)
    model_plain: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.7268
    std: 0.0136
    paper_value: 0.7268
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 218
    true_value: 0.7268
    true_std: 0.0136
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7268
    sort_std: 0.0136
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    model_key: unigcnii (h-19-rwpee we depth 8)
    model_plain: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.7265
    std: 0.0127
    paper_value: 0.7265
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 219
    true_value: 0.7265
    true_std: 0.0127
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 219
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7265
    sort_std: 0.0127
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    model_key: unigcnii (no encodings depth 2)
    model_plain: UniGCNII (no encodings depth 2)
    value: 0.7264
    std: 0.0106
    paper_value: 0.7264
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 221
    true_value: 0.7264
    true_std: 0.0106
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 221
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7264
    sort_std: 0.0106
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    model_key: unigcnii (h-19-rwpee ee depth 2)
    model_plain: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7259
    std: 0.0125
    paper_value: 0.7259
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 223
    true_value: 0.7259
    true_std: 0.0125
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7259
    sort_std: 0.0125
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    model_key: unigcnii (hodge h-20-lape depth 2)
    model_plain: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7252
    std: 0.0138
    paper_value: 0.7252
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 224
    true_value: 0.7252
    true_std: 0.0138
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 224
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7252
    sort_std: 0.0138
    is_best: false
  - model: UniGAT (no encodings nlayer2)
    model_key: unigat (no encodings nlayer2)
    model_plain: UniGAT (no encodings nlayer2)
    value: 0.7116
    std: 0.0155
    paper_value: 0.7116
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 237
    true_value: 0.7116
    true_std: 0.0155
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 237
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7116
    sort_std: 0.0155
    is_best: false
  - model: UniGCNII (LDP depth 2)
    model_key: unigcnii (ldp depth 2)
    model_plain: UniGCNII (LDP depth 2)
    value: 0.6985
    std: 0.0165
    paper_value: 0.6985
    paper_std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 243
    true_value: 0.6985
    true_std: 0.0165
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 243
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6985
    sort_std: 0.0165
    is_best: false
  - model: UniGAT (LDP)
    model_key: unigat (ldp)
    model_plain: UniGAT (LDP)
    value: 0.6931
    std: 0.0223
    paper_value: 0.6931
    paper_std: 0.0223
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 249
    true_value: 0.6931
    true_std: 0.0223
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6931
    sort_std: 0.0223
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    model_key: unigat (norm. h-20-lape)
    model_plain: UniGAT (Norm. H-20-LAPE)
    value: 0.6789
    std: 0.0237
    paper_value: 0.6789
    paper_std: 0.0237
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 256
    true_value: 0.6789
    true_std: 0.0237
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 256
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6789
    sort_std: 0.0237
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    model_key: unigcn (h-19-rwpee en)
    model_plain: UniGCN (H-19-RWPEE EN)
    value: 0.6786
    std: 0.0215
    paper_value: 0.6786
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 257
    true_value: 0.6786
    true_std: 0.0215
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 257
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6786
    sort_std: 0.0215
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    model_key: unigat (h-19-rwpee we)
    model_plain: UniGAT (H-19-RWPEE WE)
    value: 0.6782
    std: 0.0218
    paper_value: 0.6782
    paper_std: 0.0218
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 259
    true_value: 0.6782
    true_std: 0.0218
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 259
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6782
    sort_std: 0.0218
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    model_key: unigat (hodge h-20-lape)
    model_plain: UniGAT (Hodge H-20-LAPE)
    value: 0.678
    std: 0.0227
    paper_value: 0.678
    paper_std: 0.0227
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 260
    true_value: 0.678
    true_std: 0.0227
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 260
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.678
    sort_std: 0.0227
    is_best: false
  - model: UniSAGE (no encodings)
    model_key: unisage (no encodings)
    model_plain: UniSAGE (no encodings)
    value: 0.678
    std: 0.0233
    paper_value: 0.678
    paper_std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 261
    true_value: 0.678
    true_std: 0.0233
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 261
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.678
    sort_std: 0.0233
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    model_key: unigat (h-19-rwpee ee)
    model_plain: UniGAT (H-19-RWPEE EE)
    value: 0.6776
    std: 0.0191
    paper_value: 0.6776
    paper_std: 0.0191
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 262
    true_value: 0.6776
    true_std: 0.0191
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 262
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6776
    sort_std: 0.0191
    is_best: false
  - model: UniGCN (no encodings)
    model_key: unigcn (no encodings)
    model_plain: UniGCN (no encodings)
    value: 0.677
    std: 0.0233
    paper_value: 0.677
    paper_std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 263
    true_value: 0.677
    true_std: 0.0233
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 263
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.677
    sort_std: 0.0233
    is_best: false
  - model: UniGAT (HCP-FRC)
    model_key: unigat (hcp-frc)
    model_plain: UniGAT (HCP-FRC)
    value: 0.6595
    std: 0.0324
    paper_value: 0.6595
    paper_std: 0.0324
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 271
    true_value: 0.6595
    true_std: 0.0324
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 271
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6595
    sort_std: 0.0324
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    model_key: unigcnii (hcp-frc depth 2)
    model_plain: UniGCNII (HCP-FRC depth 2)
    value: 0.6554
    std: 0.0193
    paper_value: 0.6554
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 273
    true_value: 0.6554
    true_std: 0.0193
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 273
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6554
    sort_std: 0.0193
    is_best: false
  - model: UniSAGE (LDP)
    model_key: unisage (ldp)
    model_plain: UniSAGE (LDP)
    value: 0.6308
    std: 0.0268
    paper_value: 0.6308
    paper_std: 0.0268
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 277
    true_value: 0.6308
    true_std: 0.0268
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 277
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6308
    sort_std: 0.0268
    is_best: false
  - model: UniGCN (LDP)
    model_key: unigcn (ldp)
    model_plain: UniGCN (LDP)
    value: 0.6296
    std: 0.0289
    paper_value: 0.6296
    paper_std: 0.0289
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 278
    true_value: 0.6296
    true_std: 0.0289
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 278
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6296
    sort_std: 0.0289
    is_best: false
  - model: UniGCN (HCP-FRC)
    model_key: unigcn (hcp-frc)
    model_plain: UniGCN (HCP-FRC)
    value: 0.5777
    std: 0.031
    paper_value: 0.5777
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 289
    true_value: 0.5777
    true_std: 0.031
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 289
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5777
    sort_std: 0.031
    is_best: false
  - model: UniSAGE (HCP-FRC)
    model_key: unisage (hcp-frc)
    model_plain: UniSAGE (HCP-FRC)
    value: 0.5735
    std: 0.0315
    paper_value: 0.5735
    paper_std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 292
    true_value: 0.5735
    true_std: 0.0315
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 292
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5735
    sort_std: 0.0315
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: Cora-CA
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.8478
    std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8478
    sort_std: 0.015700000000000002
    is_best: true
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.7864
    std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2603.00599'
    title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    codebase_url: https://github.com/Mingzhang21/HealHGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7864
    sort_std: 0.0165
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    model_key: unigcnii (hodge h-20-lape depth 2)
    model_plain: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7635
    std: 0.0108
    paper_value: 0.7635
    paper_std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.7635
    true_std: 0.0108
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7635
    sort_std: 0.0108
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    model_key: unigcnii (no encodings depth 2)
    model_plain: UniGCNII (no encodings depth 2)
    value: 0.7634
    std: 0.0112
    paper_value: 0.7634
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.7634
    true_std: 0.0112
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7634
    sort_std: 0.0112
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    model_key: unigcnii (h-19-rwpee ee depth 2)
    model_plain: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7631
    std: 0.0115
    paper_value: 0.7631
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 5
    true_value: 0.7631
    true_std: 0.0115
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7631
    sort_std: 0.0115
    is_best: false
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    model_key: unigcnii (norm. h-20-lape depth 2)
    model_plain: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.7624
    std: 0.0116
    paper_value: 0.7624
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 6
    true_value: 0.7624
    true_std: 0.0116
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7624
    sort_std: 0.0116
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    model_key: unigcnii (h-19-rwpee we depth 8)
    model_plain: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.7616
    std: 0.012
    paper_value: 0.7616
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.7616
    true_std: 0.012
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7616
    sort_std: 0.012
    is_best: false
  - model: UniGCNII (LDP depth 2)
    model_key: unigcnii (ldp depth 2)
    model_plain: UniGCNII (LDP depth 2)
    value: 0.7589
    std: 0.0141
    paper_value: 0.7589
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 8
    true_value: 0.7589
    true_std: 0.0141
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7589
    sort_std: 0.0141
    is_best: false
  - model: UniGAT (no encodings nlayer2)
    model_key: unigat (no encodings nlayer2)
    model_plain: UniGAT (no encodings nlayer2)
    value: 0.7568
    std: 0.0145
    paper_value: 0.7568
    paper_std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.7568
    true_std: 0.0145
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7568
    sort_std: 0.0145
    is_best: false
  - model: UniGAT (LDP)
    model_key: unigat (ldp)
    model_plain: UniGAT (LDP)
    value: 0.7547
    std: 0.0147
    paper_value: 0.7547
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 10
    true_value: 0.7547
    true_std: 0.0147
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7547
    sort_std: 0.0147
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    model_key: unigcnii (hcp-frc depth 2)
    model_plain: UniGCNII (HCP-FRC depth 2)
    value: 0.7501
    std: 0.014
    paper_value: 0.7501
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCNII
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 11
    true_value: 0.7501
    true_std: 0.014
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7501
    sort_std: 0.014
    is_best: false
  - model: UniGAT (HCP-FRC)
    model_key: unigat (hcp-frc)
    model_plain: UniGAT (HCP-FRC)
    value: 0.7485
    std: 0.0166
    paper_value: 0.7485
    paper_std: 0.0166
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.7485
    true_std: 0.0166
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7485
    sort_std: 0.0166
    is_best: false
  - model: UniSAGE (no encodings)
    model_key: unisage (no encodings)
    model_plain: UniSAGE (no encodings)
    value: 0.7416
    std: 0.015
    paper_value: 0.7416
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 13
    true_value: 0.7416
    true_std: 0.015
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7416
    sort_std: 0.015
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    model_key: unigat (hodge h-20-lape)
    model_plain: UniGAT (Hodge H-20-LAPE)
    value: 0.7413
    std: 0.0157
    paper_value: 0.7413
    paper_std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 14
    true_value: 0.7413
    true_std: 0.0157
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7413
    sort_std: 0.0157
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    model_key: unigat (norm. h-20-lape)
    model_plain: UniGAT (Norm. H-20-LAPE)
    value: 0.741
    std: 0.0152
    paper_value: 0.741
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.741
    true_std: 0.0152
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.0152
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    model_key: unigcn (h-19-rwpee en)
    model_plain: UniGCN (H-19-RWPEE EN)
    value: 0.74
    std: 0.0157
    paper_value: 0.74
    paper_std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 16
    true_value: 0.74
    true_std: 0.0157
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74
    sort_std: 0.0157
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    model_key: unigat (h-19-rwpee ee)
    model_plain: UniGAT (H-19-RWPEE EE)
    value: 0.7399
    std: 0.0159
    paper_value: 0.7399
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 17
    true_value: 0.7399
    true_std: 0.0159
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7399
    sort_std: 0.0159
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    model_key: unigat (h-19-rwpee we)
    model_plain: UniGAT (H-19-RWPEE WE)
    value: 0.7397
    std: 0.0135
    paper_value: 0.7397
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGAT
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 18
    true_value: 0.7397
    true_std: 0.0135
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7397
    sort_std: 0.0135
    is_best: false
  - model: UniGCN (no encodings)
    model_key: unigcn (no encodings)
    model_plain: UniGCN (no encodings)
    value: 0.7397
    std: 0.0156
    paper_value: 0.7397
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 19
    true_value: 0.7397
    true_std: 0.0156
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7397
    sort_std: 0.0156
    is_best: false
  - model: UniSAGE (LDP)
    model_key: unisage (ldp)
    model_plain: UniSAGE (LDP)
    value: 0.7388
    std: 0.0171
    paper_value: 0.7388
    paper_std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.7388
    true_std: 0.0171
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7388
    sort_std: 0.0171
    is_best: false
  - model: UniGCN (LDP)
    model_key: unigcn (ldp)
    model_plain: UniGCN (LDP)
    value: 0.7383
    std: 0.0159
    paper_value: 0.7383
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 21
    true_value: 0.7383
    true_std: 0.0159
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7383
    sort_std: 0.0159
    is_best: false
  - model: UniGCN (HCP-FRC)
    model_key: unigcn (hcp-frc)
    model_plain: UniGCN (HCP-FRC)
    value: 0.7291
    std: 0.0188
    paper_value: 0.7291
    paper_std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniGCN
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 22
    true_value: 0.7291
    true_std: 0.0188
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7291
    sort_std: 0.0188
    is_best: false
  - model: UniSAGE (HCP-FRC)
    model_key: unisage (hcp-frc)
    model_plain: UniSAGE (HCP-FRC)
    value: 0.7257
    std: 0.0196
    paper_value: 0.7257
    paper_std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table tab:hg_node_classification_UniSAGE
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 23
    true_value: 0.7257
    true_std: 0.0196
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7257
    sort_std: 0.0196
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
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
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.5128
    std: 0.0112
    paper_value: 0.5128
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.5128
    true_std: 0.0112
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5128
    sort_std: 0.0112
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.5109
    std: 0.0164
    paper_value: 0.5109
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 21
    true_value: 0.5109
    true_std: 0.0164
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5109
    sort_std: 0.0164
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.4819
    std: 0.0131
    paper_value: 0.4819
    paper_std: 0.0131
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 28
    true_value: 0.4819
    true_std: 0.0131
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4819
    sort_std: 0.0131
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.4778
    std: 0.0098
    paper_value: 0.4778
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 30
    true_value: 0.4778
    true_std: 0.0098
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4778
    sort_std: 0.0098
    is_best: false
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.4766
    std: 0.0092
    paper_value: 0.4766
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 31
    true_value: 0.4766
    true_std: 0.0092
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4766
    sort_std: 0.0092
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.4744
    std: 0.0116
    paper_value: 0.4744
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 32
    true_value: 0.4744
    true_std: 0.0116
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4744
    sort_std: 0.0116
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.4683
    std: 0.0114
    paper_value: 0.4683
    paper_std: 0.0114
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 33
    true_value: 0.4683
    true_std: 0.0114
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4683
    sort_std: 0.0114
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.429
    std: 0.0135
    paper_value: 0.429
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 40
    true_value: 0.429
    true_std: 0.0135
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.429
    sort_std: 0.0135
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.3283
    std: 0.0136
    paper_value: 0.3283
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 75
    true_value: 0.3283
    true_std: 0.0136
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3283
    sort_std: 0.0136
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.3093
    std: 0.0127
    paper_value: 0.3093
    paper_std: 0.0127
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 89
    true_value: 0.3093
    true_std: 0.0127
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3093
    sort_std: 0.0127
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.3087
    std: 0.0138
    paper_value: 0.3087
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 90
    true_value: 0.3087
    true_std: 0.0138
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3087
    sort_std: 0.0138
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.3066
    std: 0.0178
    paper_value: 0.3066
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 91
    true_value: 0.3066
    true_std: 0.0178
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3066
    sort_std: 0.0178
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.2852
    std: 0.0116
    paper_value: 0.2852
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 108
    true_value: 0.2852
    true_std: 0.0116
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2852
    sort_std: 0.0116
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.2803
    std: 0.0115
    paper_value: 0.2803
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 113
    true_value: 0.2803
    true_std: 0.0115
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2803
    sort_std: 0.0115
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: IMDB
  rows:
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.7308
    std: 0.0124
    paper_value: 0.7308
    paper_std: 0.0124
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 1
    true_value: 0.7308
    true_std: 0.0124
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7308
    sort_std: 0.0124
    is_best: true
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.7205
    std: 0.0115
    paper_value: 0.7205
    paper_std: 0.0115
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 0.7205
    true_std: 0.0115
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7205
    sort_std: 0.0115
    is_best: true
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.7148
    std: 0.0103
    paper_value: 0.7148
    paper_std: 0.0103
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.7148
    true_std: 0.0103
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7148
    sort_std: 0.0103
    is_best: true
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.7093
    std: 0.0121
    paper_value: 0.7093
    paper_std: 0.0121
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.7093
    true_std: 0.0121
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7093
    sort_std: 0.0121
    is_best: true
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.7067
    std: 0.0118
    paper_value: 0.7067
    paper_std: 0.0118
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 5
    true_value: 0.7067
    true_std: 0.0118
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7067
    sort_std: 0.0118
    is_best: true
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.7064
    std: 0.0132
    paper_value: 0.7064
    paper_std: 0.0132
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 6
    true_value: 0.7064
    true_std: 0.0132
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7064
    sort_std: 0.0132
    is_best: true
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.7053
    std: 0.018
    paper_value: 0.7053
    paper_std: 0.018
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.7053
    true_std: 0.018
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7053
    sort_std: 0.018
    is_best: true
  - model: GIN (HCP-FRC)
    model_key: gin (hcp-frc)
    model_plain: GIN (HCP-FRC)
    value: 0.704
    std: 0.0152
    paper_value: 0.704
    paper_std: 0.0152
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 8
    true_value: 0.704
    true_std: 0.0152
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.704
    sort_std: 0.0152
    is_best: true
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.7018
    std: 0.0144
    paper_value: 0.7018
    paper_std: 0.0144
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.7018
    true_std: 0.0144
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7018
    sort_std: 0.0144
    is_best: false
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.6992
    std: 0.015
    paper_value: 0.6992
    paper_std: 0.015
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 10
    true_value: 0.6992
    true_std: 0.015
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6992
    sort_std: 0.015
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.6948
    std: 0.0171
    paper_value: 0.6948
    paper_std: 0.0171
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 11
    true_value: 0.6948
    true_std: 0.0171
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6948
    sort_std: 0.0171
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.6937
    std: 0.0165
    paper_value: 0.6937
    paper_std: 0.0165
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.6937
    true_std: 0.0165
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6937
    sort_std: 0.0165
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.6935
    std: 0.0224
    paper_value: 0.6935
    paper_std: 0.0224
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 13
    true_value: 0.6935
    true_std: 0.0224
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6935
    sort_std: 0.0224
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.6816
    std: 0.0283
    paper_value: 0.6816
    paper_std: 0.0283
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 14
    true_value: 0.6816
    true_std: 0.0283
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6816
    sort_std: 0.0283
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.6712
    std: 0.0136
    paper_value: 0.6712
    paper_std: 0.0136
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.6712
    true_std: 0.0136
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6712
    sort_std: 0.0136
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.664
    std: 0.0153
    paper_value: 0.664
    paper_std: 0.0153
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 16
    true_value: 0.664
    true_std: 0.0153
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.664
    sort_std: 0.0153
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id008
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
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.8936
    std: 0.0168
    paper_value: 0.8936
    paper_std: 0.0168
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 31
    true_value: 0.8936
    true_std: 0.0168
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8936
    sort_std: 0.0168
    is_best: false
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8849
    std: 0.0212
    paper_value: 0.8849
    paper_std: 0.0212
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 38
    true_value: 0.8849
    true_std: 0.0212
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8849
    sort_std: 0.0212
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.869
    std: 0.0181
    paper_value: 0.869
    paper_std: 0.0181
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 52
    true_value: 0.869
    true_std: 0.0181
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.869
    sort_std: 0.0181
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.8672
    std: 0.0196
    paper_value: 0.8672
    paper_std: 0.0196
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 54
    true_value: 0.8672
    true_std: 0.0196
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8672
    sort_std: 0.0196
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.8493
    std: 0.0182
    paper_value: 0.8493
    paper_std: 0.0182
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 66
    true_value: 0.8493
    true_std: 0.0182
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8493
    sort_std: 0.0182
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8309
    std: 0.0171
    paper_value: 0.8309
    paper_std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 76
    true_value: 0.8309
    true_std: 0.0171
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8309
    sort_std: 0.0171
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.8234
    std: 0.0268
    paper_value: 0.8234
    paper_std: 0.0268
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 84
    true_value: 0.8234
    true_std: 0.0268
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8234
    sort_std: 0.0268
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.8227
    std: 0.0157
    paper_value: 0.8227
    paper_std: 0.0157
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 85
    true_value: 0.8227
    true_std: 0.0157
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8227
    sort_std: 0.0157
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.8085
    std: 0.0177
    paper_value: 0.8085
    paper_std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 97
    true_value: 0.8085
    true_std: 0.0177
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8085
    sort_std: 0.0177
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.804
    std: 0.0153
    paper_value: 0.804
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 102
    true_value: 0.804
    true_std: 0.0153
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.804
    sort_std: 0.0153
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.8013
    std: 0.0165
    paper_value: 0.8013
    paper_std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 103
    true_value: 0.8013
    true_std: 0.0165
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8013
    sort_std: 0.0165
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.733
    std: 0.0195
    paper_value: 0.733
    paper_std: 0.0195
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 146
    true_value: 0.733
    true_std: 0.0195
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: 0.0195
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.7175
    std: 0.0208
    paper_value: 0.7175
    paper_std: 0.0208
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 152
    true_value: 0.7175
    true_std: 0.0208
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7175
    sort_std: 0.0208
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.6596
    std: 0.0176
    paper_value: 0.6596
    paper_std: 0.0176
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:mutag}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 168
    true_value: 0.6596
    true_std: 0.0176
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6596
    sort_std: 0.0176
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.7482
    std: 0.0111
    paper_value: 0.7482
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 77
    true_value: 0.7482
    true_std: 0.0111
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7482
    sort_std: 0.0111
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.7452
    std: 0.012
    paper_value: 0.7452
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 79
    true_value: 0.7452
    true_std: 0.012
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7452
    sort_std: 0.012
    is_best: false
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.745
    std: 0.0113
    paper_value: 0.745
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 80
    true_value: 0.745
    true_std: 0.0113
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.0113
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.741
    std: 0.0098
    paper_value: 0.741
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 90
    true_value: 0.741
    true_std: 0.0098
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.741
    sort_std: 0.0098
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.7405
    std: 0.0113
    paper_value: 0.7405
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 94
    true_value: 0.7405
    true_std: 0.0113
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7405
    sort_std: 0.0113
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.7403
    std: 0.011
    paper_value: 0.7403
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 95
    true_value: 0.7403
    true_std: 0.011
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7403
    sort_std: 0.011
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.7395
    std: 0.0108
    paper_value: 0.7395
    paper_std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 98
    true_value: 0.7395
    true_std: 0.0108
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7395
    sort_std: 0.0108
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.7378
    std: 0.0125
    paper_value: 0.7378
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 101
    true_value: 0.7378
    true_std: 0.0125
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7378
    sort_std: 0.0125
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.7194
    std: 0.0158
    paper_value: 0.7194
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 146
    true_value: 0.7194
    true_std: 0.0158
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7194
    sort_std: 0.0158
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.7192
    std: 0.0118
    paper_value: 0.7192
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 148
    true_value: 0.7192
    true_std: 0.0118
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7192
    sort_std: 0.0118
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.7148
    std: 0.009
    paper_value: 0.7148
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 157
    true_value: 0.7148
    true_std: 0.009
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7148
    sort_std: 0.009
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.7146
    std: 0.0152
    paper_value: 0.7146
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 158
    true_value: 0.7146
    true_std: 0.0152
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7146
    sort_std: 0.0152
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.7146
    std: 0.0125
    paper_value: 0.7146
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 159
    true_value: 0.7146
    true_std: 0.0125
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7146
    sort_std: 0.0125
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.7127
    std: 0.012
    paper_value: 0.7127
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 162
    true_value: 0.7127
    true_std: 0.012
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7127
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.617
    std: 0.01
    paper_value: 0.617
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 235
    true_value: 0.617
    true_std: 0.01
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 235
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.617
    sort_std: 0.01
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.609
    std: 0.01
    paper_value: 0.609
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 239
    true_value: 0.609
    true_std: 0.01
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 239
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.609
    sort_std: 0.01
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.604
    std: 0.01
    paper_value: 0.604
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 242
    true_value: 0.604
    true_std: 0.01
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.604
    sort_std: 0.01
    is_best: false
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.604
    std: 0.01
    paper_value: 0.604
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 243
    true_value: 0.604
    true_std: 0.01
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 243
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.604
    sort_std: 0.01
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.602
    std: 0.01
    paper_value: 0.602
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 247
    true_value: 0.602
    true_std: 0.01
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 247
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.602
    sort_std: 0.01
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.599
    std: 0.011
    paper_value: 0.599
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 252
    true_value: 0.599
    true_std: 0.011
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 252
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.599
    sort_std: 0.011
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.594
    std: 0.011
    paper_value: 0.594
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 261
    true_value: 0.594
    true_std: 0.011
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 261
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.594
    sort_std: 0.011
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.593
    std: 0.009
    paper_value: 0.593
    paper_std: 0.009
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 263
    true_value: 0.593
    true_std: 0.009
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 263
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.593
    sort_std: 0.009
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.559
    std: 0.004
    paper_value: 0.559
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 283
    true_value: 0.559
    true_std: 0.004
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 283
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.559
    sort_std: 0.004
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.559
    std: 0.004
    paper_value: 0.559
    paper_std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 284
    true_value: 0.559
    true_std: 0.004
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 284
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.559
    sort_std: 0.004
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.549
    std: 0.005
    paper_value: 0.549
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 290
    true_value: 0.549
    true_std: 0.005
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 290
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.549
    sort_std: 0.005
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.538
    std: 0.007
    paper_value: 0.538
    paper_std: 0.007
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 292
    true_value: 0.538
    true_std: 0.007
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 292
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.007
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.534
    std: 0.006
    paper_value: 0.534
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 294
    true_value: 0.534
    true_std: 0.006
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 294
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.534
    sort_std: 0.006
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.532
    std: 0.005
    paper_value: 0.532
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 295
    true_value: 0.532
    true_std: 0.005
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 295
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.532
    sort_std: 0.005
    is_best: false
  metric: AP
  higher_is_better: true
- &id006
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
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.252
    std: 0.003
    paper_value: 0.252
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 159
    true_value: 0.252
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.252
    sort_std: 0.003
    is_best: false
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.252
    std: 0.003
    paper_value: 0.252
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 160
    true_value: 0.252
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.252
    sort_std: 0.003
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.253
    std: 0.003
    paper_value: 0.253
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 173
    true_value: 0.253
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 173
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.253
    sort_std: 0.003
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.254
    std: 0.002
    paper_value: 0.254
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 182
    true_value: 0.254
    true_std: 0.002
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 182
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.002
    is_best: false
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.254
    std: 0.003
    paper_value: 0.254
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 183
    true_value: 0.254
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.003
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.254
    std: 0.004
    paper_value: 0.254
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 184
    true_value: 0.254
    true_std: 0.004
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 184
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.004
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.255
    std: 0.004
    paper_value: 0.255
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 191
    true_value: 0.255
    true_std: 0.004
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 191
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.255
    sort_std: 0.004
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.257
    std: 0.003
    paper_value: 0.257
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 205
    true_value: 0.257
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 205
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.257
    sort_std: 0.003
    is_best: false
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.258
    std: 0.003
    paper_value: 0.258
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 208
    true_value: 0.258
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.258
    sort_std: 0.003
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.258
    std: 0.003
    paper_value: 0.258
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 209
    true_value: 0.258
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 209
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.258
    sort_std: 0.003
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.262
    std: 0.003
    paper_value: 0.262
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 220
    true_value: 0.262
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 220
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.262
    sort_std: 0.003
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.263
    std: 0.003
    paper_value: 0.263
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 225
    true_value: 0.263
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 225
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.263
    sort_std: 0.003
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.265
    std: 0.003
    paper_value: 0.265
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 234
    true_value: 0.265
    true_std: 0.003
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 234
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.265
    sort_std: 0.003
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.266
    std: 0.002
    paper_value: 0.266
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 237
    true_value: 0.266
    true_std: 0.002
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 237
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.266
    sort_std: 0.002
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: UniGAT (no encodings nlayer2)
    model_key: unigat (no encodings nlayer2)
    model_plain: UniGAT (no encodings nlayer2)
    value: 0.7562
    std: 0.0109
    paper_value: 0.7562
    paper_std: 0.0109
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
    global_rank: 131
    true_value: 0.7562
    true_std: 0.0109
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7562
    sort_std: 0.0109
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    model_key: unigcnii (hodge h-20-lape depth 2)
    model_plain: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7551
    std: 0.0113
    paper_value: 0.7551
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 132
    true_value: 0.7551
    true_std: 0.0113
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7551
    sort_std: 0.0113
    is_best: false
  - model: UniGCNII (Norm. H-20-LAPE depth 2)
    model_key: unigcnii (norm. h-20-lape depth 2)
    model_plain: UniGCNII (Norm. H-20-LAPE depth 2)
    value: 0.7544
    std: 0.0109
    paper_value: 0.7544
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 133
    true_value: 0.7544
    true_std: 0.0109
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7544
    sort_std: 0.0109
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    model_key: unigcnii (no encodings depth 2)
    model_plain: UniGCNII (no encodings depth 2)
    value: 0.754
    std: 0.0118
    paper_value: 0.754
    paper_std: 0.0118
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 134
    true_value: 0.754
    true_std: 0.0118
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: 0.0118
    is_best: false
  - model: UniGAT (Norm. H-20-LAPE)
    model_key: unigat (norm. h-20-lape)
    model_plain: UniGAT (Norm. H-20-LAPE)
    value: 0.7507
    std: 0.0144
    paper_value: 0.7507
    paper_std: 0.0144
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
    global_rank: 136
    true_value: 0.7507
    true_std: 0.0144
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7507
    sort_std: 0.0144
    is_best: false
  - model: UniGAT (Hodge H-20-LAPE)
    model_key: unigat (hodge h-20-lape)
    model_plain: UniGAT (Hodge H-20-LAPE)
    value: 0.7503
    std: 0.0142
    paper_value: 0.7503
    paper_std: 0.0142
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
    global_rank: 137
    true_value: 0.7503
    true_std: 0.0142
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7503
    sort_std: 0.0142
    is_best: false
  - model: UniGCNII (H-19-RWPEE WE depth 8)
    model_key: unigcnii (h-19-rwpee we depth 8)
    model_plain: UniGCNII (H-19-RWPEE WE depth 8)
    value: 0.7503
    std: 0.0096
    paper_value: 0.7503
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 138
    true_value: 0.7503
    true_std: 0.0096
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7503
    sort_std: 0.0096
    is_best: false
  - model: UniGCN (no encodings)
    model_key: unigcn (no encodings)
    model_plain: UniGCN (no encodings)
    value: 0.7502
    std: 0.0139
    paper_value: 0.7502
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 139
    true_value: 0.7502
    true_std: 0.0139
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 139
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7502
    sort_std: 0.0139
    is_best: false
  - model: UniSAGE (no encodings)
    model_key: unisage (no encodings)
    model_plain: UniSAGE (no encodings)
    value: 0.7502
    std: 0.0144
    paper_value: 0.7502
    paper_std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 140
    true_value: 0.7502
    true_std: 0.0144
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7502
    sort_std: 0.0144
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    model_key: unigcnii (h-19-rwpee ee depth 2)
    model_plain: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7501
    std: 0.0098
    paper_value: 0.7501
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 141
    true_value: 0.7501
    true_std: 0.0098
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7501
    sort_std: 0.0098
    is_best: false
  - model: UniGAT (H-19-RWPEE EE)
    model_key: unigat (h-19-rwpee ee)
    model_plain: UniGAT (H-19-RWPEE EE)
    value: 0.7441
    std: 0.0143
    paper_value: 0.7441
    paper_std: 0.0143
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
    global_rank: 144
    true_value: 0.7441
    true_std: 0.0143
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7441
    sort_std: 0.0143
    is_best: false
  - model: UniGAT (H-19-RWPEE WE)
    model_key: unigat (h-19-rwpee we)
    model_plain: UniGAT (H-19-RWPEE WE)
    value: 0.7437
    std: 0.0133
    paper_value: 0.7437
    paper_std: 0.0133
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
    global_rank: 145
    true_value: 0.7437
    true_std: 0.0133
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 145
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7437
    sort_std: 0.0133
    is_best: false
  - model: UniGCN (H-19-RWPEE EN)
    model_key: unigcn (h-19-rwpee en)
    model_plain: UniGCN (H-19-RWPEE EN)
    value: 0.7429
    std: 0.0136
    paper_value: 0.7429
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 147
    true_value: 0.7429
    true_std: 0.0136
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7429
    sort_std: 0.0136
    is_best: false
  - model: UniGAT (LDP)
    model_key: unigat (ldp)
    model_plain: UniGAT (LDP)
    value: 0.6841
    std: 0.0179
    paper_value: 0.6841
    paper_std: 0.0179
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
    global_rank: 156
    true_value: 0.6841
    true_std: 0.0179
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6841
    sort_std: 0.0179
    is_best: false
  - model: UniSAGE (LDP)
    model_key: unisage (ldp)
    model_plain: UniSAGE (LDP)
    value: 0.6753
    std: 0.0309
    paper_value: 0.6753
    paper_std: 0.0309
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 157
    true_value: 0.6753
    true_std: 0.0309
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6753
    sort_std: 0.0309
    is_best: false
  - model: UniGCN (LDP)
    model_key: unigcn (ldp)
    model_plain: UniGCN (LDP)
    value: 0.6741
    std: 0.0316
    paper_value: 0.6741
    paper_std: 0.0316
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 158
    true_value: 0.6741
    true_std: 0.0316
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6741
    sort_std: 0.0316
    is_best: false
  - model: UniGCNII (LDP depth 2)
    model_key: unigcnii (ldp depth 2)
    model_plain: UniGCNII (LDP depth 2)
    value: 0.674
    std: 0.0193
    paper_value: 0.674
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 159
    true_value: 0.674
    true_std: 0.0193
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.674
    sort_std: 0.0193
    is_best: false
  - model: UniGAT (HCP-FRC)
    model_key: unigat (hcp-frc)
    model_plain: UniGAT (HCP-FRC)
    value: 0.6634
    std: 0.0179
    paper_value: 0.6634
    paper_std: 0.0179
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
    global_rank: 160
    true_value: 0.6634
    true_std: 0.0179
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6634
    sort_std: 0.0179
    is_best: false
  - model: UniSAGE (HCP-FRC)
    model_key: unisage (hcp-frc)
    model_plain: UniSAGE (HCP-FRC)
    value: 0.6571
    std: 0.0258
    paper_value: 0.6571
    paper_std: 0.0258
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 161
    true_value: 0.6571
    true_std: 0.0258
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6571
    sort_std: 0.0258
    is_best: false
  - model: UniGCN (HCP-FRC)
    model_key: unigcn (hcp-frc)
    model_plain: UniGCN (HCP-FRC)
    value: 0.6555
    std: 0.024
    paper_value: 0.6555
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 162
    true_value: 0.6555
    true_std: 0.024
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6555
    sort_std: 0.024
    is_best: false
  - model: UniGCNII (HCP-FRC depth 2)
    model_key: unigcnii (hcp-frc depth 2)
    model_plain: UniGCNII (HCP-FRC depth 2)
    value: 0.65
    std: 0.0218
    paper_value: 0.65
    paper_std: 0.0218
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 163
    true_value: 0.65
    true_std: 0.0218
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.0218
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Reddit
  rows:
  - model: GCN (LCP-ORC)
    model_key: gcn (lcp-orc)
    model_plain: GCN (LCP-ORC)
    value: 0.8719
    std: 0.0156
    paper_value: 0.8719
    paper_std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 1
    true_value: 0.8719
    true_std: 0.0156
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8719
    sort_std: 0.0156
    is_best: true
  - model: GIN (HCP-ORC)
    model_key: gin (hcp-orc)
    model_plain: GIN (HCP-ORC)
    value: 0.8482
    std: 0.0162
    paper_value: 0.8482
    paper_std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 0.8482
    true_std: 0.0162
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8482
    sort_std: 0.0162
    is_best: true
  - model: GPS (EN H-19-RWPE)
    model_key: gps (en h-19-rwpe)
    model_plain: GPS (EN H-19-RWPE)
    value: 0.8425
    std: 0.0113
    paper_value: 0.8425
    paper_std: 0.0113
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.8425
    true_std: 0.0113
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8425
    sort_std: 0.0113
    is_best: false
  - model: GPS (LCP-ORC)
    model_key: gps (lcp-orc)
    model_plain: GPS (LCP-ORC)
    value: 0.8307
    std: 0.0124
    paper_value: 0.8307
    paper_std: 0.0124
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.8307
    true_std: 0.0124
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8307
    sort_std: 0.0124
    is_best: false
  - model: GPS (20-LAPE)
    model_key: gps (20-lape)
    model_plain: GPS (20-LAPE)
    value: 0.8205
    std: 0.0129
    paper_value: 0.8205
    paper_std: 0.0129
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 5
    true_value: 0.8205
    true_std: 0.0129
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8205
    sort_std: 0.0129
    is_best: false
  - model: GPS (19-RWPE)
    model_key: gps (19-rwpe)
    model_plain: GPS (19-RWPE)
    value: 0.8192
    std: 0.0131
    paper_value: 0.8192
    paper_std: 0.0131
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 6
    true_value: 0.8192
    true_std: 0.0131
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8192
    sort_std: 0.0131
    is_best: false
  - model: GPS (LCP-FRC)
    model_key: gps (lcp-frc)
    model_plain: GPS (LCP-FRC)
    value: 0.8168
    std: 0.0116
    paper_value: 0.8168
    paper_std: 0.0116
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.8168
    true_std: 0.0116
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8168
    sort_std: 0.0116
    is_best: false
  - model: GPS (No Encoding)
    model_key: gps (no encoding)
    model_plain: GPS (No Encoding)
    value: 0.8094
    std: 0.0142
    paper_value: 0.8094
    paper_std: 0.0142
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gps}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 8
    true_value: 0.8094
    true_std: 0.0142
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8094
    sort_std: 0.0142
    is_best: false
  - model: GCN (Hodge H-20-LAPE)
    model_key: gcn (hodge h-20-lape)
    model_plain: GCN (Hodge H-20-LAPE)
    value: 0.7994
    std: 0.0181
    paper_value: 0.7994
    paper_std: 0.0181
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.7994
    true_std: 0.0181
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7994
    sort_std: 0.0181
    is_best: false
  - model: GCN (Norm. H-20-LAPE)
    model_key: gcn (norm. h-20-lape)
    model_plain: GCN (Norm. H-20-LAPE)
    value: 0.7915
    std: 0.0154
    paper_value: 0.7915
    paper_std: 0.0154
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 10
    true_value: 0.7915
    true_std: 0.0154
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7915
    sort_std: 0.0154
    is_best: false
  - model: GCN (EE H-19-RWPE)
    model_key: gcn (ee h-19-rwpe)
    model_plain: GCN (EE H-19-RWPE)
    value: 0.7746
    std: 0.0153
    paper_value: 0.7746
    paper_std: 0.0153
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 11
    true_value: 0.7746
    true_std: 0.0153
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7746
    sort_std: 0.0153
    is_best: false
  - model: GCN (20-LAPE)
    model_key: gcn (20-lape)
    model_plain: GCN (20-LAPE)
    value: 0.7584
    std: 0.0165
    paper_value: 0.7584
    paper_std: 0.0165
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.7584
    true_std: 0.0165
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7584
    sort_std: 0.0165
    is_best: false
  - model: GCN (No Encoding)
    model_key: gcn (no encoding)
    model_plain: GCN (No Encoding)
    value: 0.7538
    std: 0.0127
    paper_value: 0.7538
    paper_std: 0.0127
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 13
    true_value: 0.7538
    true_std: 0.0127
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7538
    sort_std: 0.0127
    is_best: false
  - model: GCN (19-RWPE)
    model_key: gcn (19-rwpe)
    model_plain: GCN (19-RWPE)
    value: 0.744
    std: 0.0168
    paper_value: 0.744
    paper_std: 0.0168
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 14
    true_value: 0.744
    true_std: 0.0168
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.744
    sort_std: 0.0168
    is_best: false
  - model: GIN (HCP-FRC)
    model_key: gin (hcp-frc)
    model_plain: GIN (HCP-FRC)
    value: 0.7053
    std: 0.0148
    paper_value: 0.7053
    paper_std: 0.0148
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gin_selected}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.7053
    true_std: 0.0148
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7053
    sort_std: 0.0148
    is_best: false
  - model: GCN (LCP-FRC)
    model_key: gcn (lcp-frc)
    model_plain: GCN (LCP-FRC)
    value: 0.6966
    std: 0.0162
    paper_value: 0.6966
    paper_std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: "Table \ref{tab:gcn}"
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 16
    true_value: 0.6966
    true_std: 0.0162
    value_gap_source_arxiv: '2502.09570'
    value_gap_source_title: Enhancing the Utility of Higher-Order Information in Relational
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6966
    sort_std: 0.0162
    is_best: false
  metric: F1
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
- benchmark: TU Dortmund
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id011
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id012
main_figure: /figures/2502.09570/main_figure.png
---

