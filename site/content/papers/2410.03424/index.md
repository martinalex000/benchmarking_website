---
title: Cayley Graph Propagation
arxiv_id: '2410.03424'
source_url: ''
authors: []
published_date: Oct 2024
published_date_iso: 2024-10
abstract: In spite of the plethora of success stories with graph neural networks (GNNs)
  on modelling graph-structured data, they are notoriously vulnerable to over-squashing,
  whereby tasks necessitate the mixing of information between distance pairs of nodes.
  To address this problem, prior work suggests rewiring the graph structure to improve
  information flow. Alternatively, a significant body of research has dedicated itself
  to discovering and precomputing bottleneck-free graph structures to ameliorate over-squashing.
  One well regarded family of bottleneck-free graphs within the mathematical community
  are expander graphs, with prior work—Expander Graph Propagation (EGP)—proposing
  the use of a well-known expander graph family—the Cayley graphs of the $SL(2,Z_n)$
  special linear group—as a computational template for GNNs. However, in EGP the computational
  graphs used are truncated to align with a given input graph. In this work, we show
  that truncation is detrimental to the coveted expansion properties. Instead, we
  propose CGP, a method to propagate information over a complete Cayley graph structure,
  thereby ensuring it is bottleneck-free to better alleviate over-squashing. Our empirical
  evidence across several real-world datasets not only shows that CGP recovers significant
  improvements as compared to EGP, but it is also akin to or outperforms computationally
  complex graph rewiring techniques.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN + CGP
- GIN + CGP
- CGP
mrr: 0.0085
adjusted_mrr: 0.0028
mrr_dataset_count: 1
benchmark_categories:
- TU Dortmund
- OGB
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id005
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7049
    std: 0.01628
    paper_value: 0.7049
    paper_std: 0.01628
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.827
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12209999999999999
    value_note: ''
    paper_rank: 77
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7149
    std: 0.00746
    paper_value: 0.7149
    paper_std: 0.00746
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 14
    true_value: 0.8059
    true_std: 0.0027
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09099999999999997
    value_note: ''
    paper_rank: 73
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.8059
    sort_std: 0.0027
    is_best: false
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.7335
    std: 0.00788
    paper_value: 0.7335
    paper_std: 0.00788
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 48
    true_value: 0.7335
    true_std: 0.00788
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7335
    sort_std: 0.00788
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.7332
    std: 0.00814
    paper_value: 0.7332
    paper_std: 0.00814
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 49
    true_value: 0.7332
    true_std: 0.00814
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7332
    sort_std: 0.00814
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.72958
    std: 0.00419
    paper_value: 0.72958
    paper_std: 0.00419
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 54
    true_value: 0.72958
    true_std: 0.00419
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72958
    sort_std: 0.00419
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.7274
    std: 0.00786
    paper_value: 0.7274
    paper_std: 0.00786
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 55
    true_value: 0.7274
    true_std: 0.00786
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7274
    sort_std: 0.00786
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.726
    std: 0.01025
    paper_value: 0.726
    paper_std: 0.01025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 58
    true_value: 0.726
    true_std: 0.01025
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.01025
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.7233
    std: 0.00954
    paper_value: 0.7233
    paper_std: 0.00954
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 59
    true_value: 0.7233
    true_std: 0.00954
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7233
    sort_std: 0.00954
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.72039
    std: 0.00771
    paper_value: 0.72039
    paper_std: 0.00771
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 63
    true_value: 0.72039
    true_std: 0.00771
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72039
    sort_std: 0.00771
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.71849
    std: 0.0071
    paper_value: 0.71849
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 70
    true_value: 0.71849
    true_std: 0.0071
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71849
    sort_std: 0.0071
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.7172
    std: 0.00892
    paper_value: 0.7172
    paper_std: 0.00892
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 72
    true_value: 0.7172
    true_std: 0.00892
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7172
    sort_std: 0.00892
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.7133
    std: 0.00807
    paper_value: 0.7133
    paper_std: 0.00807
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 75
    true_value: 0.7133
    true_std: 0.00807
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7133
    sort_std: 0.00807
    is_best: false
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.6963
    std: 0.0073
    paper_value: 0.6963
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 82
    true_value: 0.6963
    true_std: 0.0073
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6963
    sort_std: 0.0073
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.6947
    std: 0.0097
    paper_value: 0.6947
    paper_std: 0.0097
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 83
    true_value: 0.6947
    true_std: 0.0097
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6947
    sort_std: 0.0097
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.6722
    std: 0.01367
    paper_value: 0.6722
    paper_std: 0.01367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 92
    true_value: 0.6722
    true_std: 0.01367
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6722
    sort_std: 0.01367
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.5762
    std: 0.0101
    paper_value: 0.5762
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 93
    true_value: 0.5762
    true_std: 0.0101
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5762
    sort_std: 0.0101
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
    date: '2023-06-09'
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
    date: '2023-06-09'
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
    date: '2023-06-09'
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.35667
    std: 0.02803
    paper_value: 0.35667
    paper_std: 0.02803
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 13
    true_value: 0.606
    true_std: 0.034
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.24933
    value_note: ''
    paper_rank: 61
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.606
    sort_std: 0.034
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.34167
    std: 0.00029
    paper_value: 0.34167
    paper_std: 0.00029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Nguyen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 15
    true_value: 0.584
    true_std: 0.021
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.24233
    value_note: ''
    paper_rank: 67
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.584
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.29083
    std: 0.02363
    paper_value: 0.29083
    paper_std: 0.02363
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.563
    true_std: 0.036
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27216999999999997
    value_note: ''
    paper_rank: 99
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.563
    sort_std: 0.036
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.26667
    std: 0.02
    paper_value: 0.26667
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23632999999999998
    value_note: ''
    paper_rank: 117
    rank_delta: 95
    rank_delta_abs: 95
    rank_delta_direction: worse
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.37167
    std: 0.02709
    paper_value: 0.37167
    paper_std: 0.02709
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 23
    true_value: 0.503
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13133
    value_note: ''
    paper_rank: 58
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.503
    sort_std: 0.026000000000000002
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.40667
    std: 0.03095
    paper_value: 0.40667
    paper_std: 0.03095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Choi & Panda
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 24
    true_value: 0.502
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09533000000000003
    value_note: ''
    paper_rank: 46
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.502
    sort_std: 0.027000000000000003
    is_best: false
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.50083
    std: 0.02242
    paper_value: 0.50083
    paper_std: 0.02242
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.50083
    true_std: 0.02242
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.50083
    sort_std: 0.02242
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.47833
    std: 0.02529
    paper_value: 0.47833
    paper_std: 0.02529
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 29
    true_value: 0.47833
    true_std: 0.02529
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.47833
    sort_std: 0.02529
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.42167
    std: 0.02286
    paper_value: 0.42167
    paper_std: 0.02286
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Choi & Panda
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 36
    true_value: 0.462
    true_std: 0.0141
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04033000000000003
    value_note: ''
    paper_rank: 41
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.462
    sort_std: 0.0141
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.415
    std: 0.03063
    paper_value: 0.415
    paper_std: 0.03063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Topping 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 44
    true_value: 0.415
    true_std: 0.03063
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.415
    sort_std: 0.03063
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.3175
    std: 0.02466
    paper_value: 0.3175
    paper_std: 0.02466
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Black 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 79
    true_value: 0.3175
    true_std: 0.02466
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3175
    sort_std: 0.02466
    is_best: false
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.31
    std: 0.02397
    paper_value: 0.31
    paper_std: 0.02397
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 88
    true_value: 0.31
    true_std: 0.02397
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31
    sort_std: 0.02397
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.28083
    std: 0.02301
    paper_value: 0.28083
    paper_std: 0.02301
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 99
    true_value: 0.292
    true_std: 0.013600000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011169999999999958
    value_note: global 0.2920 within std
    paper_rank: 112
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.292
    sort_std: 0.013600000000000001
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.28667
    std: 0.03693
    paper_value: 0.28667
    paper_std: 0.03693
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 103
    true_value: 0.28667
    true_std: 0.03693
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.28667
    sort_std: 0.03693
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.27583
    std: 0.03262
    paper_value: 0.27583
    paper_std: 0.03262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Choi & Panda
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 115
    true_value: 0.27583
    true_std: 0.03262
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.27583
    sort_std: 0.03262
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.25333
    std: 0.02931
    paper_value: 0.25333
    paper_std: 0.02931
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Black 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 116
    true_value: 0.2752
    true_std: 0.009899999999999999
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02187
    value_note: global 0.2752 within std
    paper_rank: 122
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.2752
    sort_std: 0.009899999999999999
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.24167
    std: 0.03005
    paper_value: 0.24167
    paper_std: 0.03005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 123
    true_value: 0.25067
    true_std: 0.00994
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009000000000000008
    value_note: global 0.2507 within std
    paper_rank: 124
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.25067
    sort_std: 0.00994
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.7995
    std: 0.0246
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
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.605
    std: 0.02729
    paper_value: 0.605
    paper_std: 0.02729
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 12
    true_value: 0.769
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16400000000000003
    value_note: ''
    paper_rank: 134
    rank_delta: 122
    rank_delta_abs: 122
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7125
    std: 0.01509
    paper_value: 0.7125
    paper_std: 0.01509
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03849999999999998
    value_note: global 0.7510 within std
    paper_rank: 79
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.699
    std: 0.02332
    paper_value: 0.699
    paper_std: 0.02332
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 68
    true_value: 0.7183
    true_std: 0.0193
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.019300000000000095
    value_note: global 0.7183 within std
    paper_rank: 99
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.7183
    sort_std: 0.0193
    is_best: false
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.7165
    std: 0.01532
    paper_value: 0.7165
    paper_std: 0.01532
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 72
    true_value: 0.7165
    true_std: 0.01532
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7165
    sort_std: 0.01532
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.707
    std: 0.00018
    paper_value: 0.707
    paper_std: 0.00018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 78
    true_value: 0.713
    true_std: 0.015
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006000000000000005
    value_note: global 0.7130 within std
    paper_rank: 90
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.713
    sort_std: 0.015
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.6955
    std: 0.01473
    paper_value: 0.6955
    paper_std: 0.01473
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 79
    true_value: 0.7128
    true_std: 0.0086
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017299999999999982
    value_note: ''
    paper_rank: 104
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.7128
    sort_std: 0.0086
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.6925
    std: 0.0181
    paper_value: 0.6925
    paper_std: 0.0181
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 80
    true_value: 0.7121
    true_std: 0.00919
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01959999999999995
    value_note: ''
    paper_rank: 105
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.7121
    sort_std: 0.00919
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.6955
    std: 0.02381
    paper_value: 0.6955
    paper_std: 0.02381
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 104
    true_value: 0.6972
    true_std: 0.01152
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0017000000000000348
    value_note: global 0.6972 within std
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6972
    sort_std: 0.01152
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.6835
    std: 0.02346
    paper_value: 0.6835
    paper_std: 0.02346
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 107
    true_value: 0.6835
    true_std: 0.02346
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6835
    sort_std: 0.02346
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.6825
    std: 0.01121
    paper_value: 0.6825
    paper_std: 0.01121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 109
    true_value: 0.6825
    true_std: 0.01121
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6825
    sort_std: 0.01121
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.5265
    std: 0.0215
    paper_value: 0.5265
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 123
    true_value: 0.6439
    true_std: 0.00907
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11740000000000006
    value_note: ''
    paper_rank: 145
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.6439
    sort_std: 0.00907
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.607
    std: 0.02079
    paper_value: 0.607
    paper_std: 0.02079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 134
    true_value: 0.607
    true_std: 0.02079
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 134
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.607
    sort_std: 0.02079
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.5975
    std: 0.02357
    paper_value: 0.5975
    paper_std: 0.02357
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 137
    true_value: 0.5975
    true_std: 0.02357
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5975
    sort_std: 0.02357
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.597
    std: 0.02371
    paper_value: 0.597
    paper_std: 0.02371
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 138
    true_value: 0.597
    true_std: 0.02371
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.597
    sort_std: 0.02371
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.59
    std: 0.02254
    paper_value: 0.59
    paper_std: 0.02254
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 140
    true_value: 0.59
    true_std: 0.02254
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 140
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.59
    sort_std: 0.02254
    is_best: false
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.562
    std: 0.01825
    paper_value: 0.562
    paper_std: 0.01825
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 142
    true_value: 0.562
    true_std: 0.01825
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.562
    sort_std: 0.01825
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4895
    std: 0.01652
    paper_value: 0.4895
    paper_std: 0.01652
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 158
    true_value: 0.4895
    true_std: 0.01652
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4895
    sort_std: 0.01652
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.815
    std: 0.04696
    paper_value: 0.815
    paper_std: 0.04696
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 9
    true_value: 0.9109999999999999
    true_std: 0.013999999999999999
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09599999999999997
    value_note: ''
    paper_rank: 91
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.9109999999999999
    sort_std: 0.013999999999999999
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.8025
    std: 0.05314
    paper_value: 0.8025
    paper_std: 0.05314
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 15
    true_value: 0.9041
    true_std: 0.0461
    value_gap_source_arxiv: '2309.16014'
    value_gap_source_title: Graph-level Representation Learning with Joint-Embedding
      Predictive Architectures
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10160000000000002
    value_note: ''
    paper_rank: 102
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.9041
    sort_std: 0.0461
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7475
    std: 0.0403
    paper_value: 0.7475
    paper_std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 22
    true_value: 0.901
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15349999999999997
    value_note: ''
    paper_rank: 136
    rank_delta: 114
    rank_delta_abs: 114
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.74
    std: 0.03462
    paper_value: 0.74
    paper_std: 0.03462
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 26
    true_value: 0.895
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15500000000000003
    value_note: ''
    paper_rank: 139
    rank_delta: 113
    rank_delta_abs: 113
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.805
    std: 0.04177
    paper_value: 0.805
    paper_std: 0.04177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 27
    true_value: 0.895
    true_std: 0.026000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08999999999999997
    value_note: ''
    paper_rank: 97
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.895
    sort_std: 0.026000000000000002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.805
    std: 0.05143
    paper_value: 0.805
    paper_std: 0.05143
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08899999999999997
    value_note: ''
    paper_rank: 97
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.8325
    std: 0.03262
    paper_value: 0.8325
    paper_std: 0.03262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Choi & Panda
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 36
    true_value: 0.8875
    true_std: 0.015700000000000002
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05499999999999994
    value_note: ''
    paper_rank: 75
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.8875
    sort_std: 0.015700000000000002
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.7925
    std: 0.00038
    paper_value: 0.7925
    paper_std: 0.00038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Nguyen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 42
    true_value: 0.8809999999999999
    true_std: 0.027000000000000003
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08849999999999991
    value_note: ''
    paper_rank: 110
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.027000000000000003
    is_best: false
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.8525
    std: 0.032
    paper_value: 0.8525
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 63
    true_value: 0.8525
    true_std: 0.032
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8525
    sort_std: 0.032
    is_best: false
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.8375
    std: 0.03597
    paper_value: 0.8375
    paper_std: 0.03597
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 73
    true_value: 0.8375
    true_std: 0.03597
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8375
    sort_std: 0.03597
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.805
    std: 0.04738
    paper_value: 0.805
    paper_std: 0.04738
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 98
    true_value: 0.805
    true_std: 0.04738
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.805
    sort_std: 0.04738
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.7525
    std: 0.05722
    paper_value: 0.7525
    paper_std: 0.05722
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 104
    true_value: 0.8
    true_std: 0.015700000000000002
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0475000000000001
    value_note: global 0.8000 within std
    paper_rank: 135
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.8
    sort_std: 0.015700000000000002
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.785
    std: 0.04189
    paper_value: 0.785
    paper_std: 0.04189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Topping 2022
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 106
    true_value: 0.797
    true_std: 0.0215
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01200000000000001
    value_note: global 0.7970 within std
    paper_rank: 118
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.797
    sort_std: 0.0215
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.765
    std: 0.04189
    paper_value: 0.765
    paper_std: 0.04189
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Black 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 113
    true_value: 0.7909999999999999
    true_std: 0.018600000000000002
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.025999999999999912
    value_note: global 0.7910 within std
    paper_rank: 128
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.7909999999999999
    sort_std: 0.018600000000000002
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.79
    std: 0.03847
    paper_value: 0.79
    paper_std: 0.03847
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Black 2023
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 114
    true_value: 0.79
    true_std: 0.03847
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79
    sort_std: 0.03847
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.705
    std: 0.04738
    paper_value: 0.705
    paper_std: 0.04738
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 159
    true_value: 0.705
    true_std: 0.04738
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.04738
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7025
    std: 0.04608
    paper_value: 0.7025
    paper_std: 0.04608
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2019
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 160
    true_value: 0.7025
    true_std: 0.04608
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7025
    sort_std: 0.04608
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.70312
    std: 0.01749
    paper_value: 0.70312
    paper_std: 0.01749
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05888000000000004
    value_note: ''
    paper_rank: 175
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.66652
    std: 0.01933
    paper_value: 0.66652
    paper_std: 0.01933
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09348000000000001
    value_note: ''
    paper_rank: 191
    rank_delta: 153
    rank_delta_abs: 153
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: GCN + PANDA
    model_key: gcn + panda
    model_plain: GCN + PANDA
    value: 0.72321
    std: 0.01786
    paper_value: 0.72321
    paper_std: 0.01786
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 37
    true_value: 0.76
    true_std: 0.00774
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03678999999999999
    value_note: ''
    paper_rank: 137
    rank_delta: 100
    rank_delta_abs: 100
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.00774
    is_best: false
  - model: GIN-FOSR-R
    model_key: gin-fosr-r
    model_plain: GIN-FOSR-R
    value: 0.71518
    std: 0.01767
    paper_value: 0.71518
    paper_std: 0.01767
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 63
    true_value: 0.75107
    true_std: 0.00817
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03588999999999998
    value_note: ''
    paper_rank: 155
    rank_delta: 92
    rank_delta_abs: 92
    rank_delta_direction: worse
    sort_value: 0.75107
    sort_std: 0.00817
    is_best: false
  - model: GCN + BORF
    model_key: gcn + borf
    model_plain: GCN + BORF
    value: 0.70625
    std: 0.00017
    paper_value: 0.70625
    paper_std: 0.00017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 83
    true_value: 0.742
    true_std: 0.008
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03574999999999995
    value_note: ''
    paper_rank: 171
    rank_delta: 88
    rank_delta_abs: 88
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.008
    is_best: false
  - model: GCN + FoSR
    model_key: gcn + fosr
    model_plain: GCN + FoSR
    value: 0.70848
    std: 0.01618
    paper_value: 0.70848
    paper_std: 0.01618
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 105
    true_value: 0.7342
    true_std: 0.008100000000000001
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025719999999999965
    value_note: ''
    paper_rank: 168
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.7342
    sort_std: 0.008100000000000001
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.73304
    std: 0.02516
    paper_value: 0.73304
    paper_std: 0.02516
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 110
    true_value: 0.73304
    true_std: 0.02516
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73304
    sort_std: 0.02516
    is_best: false
  - model: GIN + GTR
    model_key: gin + gtr
    model_plain: GIN + GTR
    value: 0.72054
    std: 0.0151
    paper_value: 0.72054
    paper_std: 0.0151
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 113
    true_value: 0.7313
    true_std: 0.0069
    value_gap_source_arxiv: '2509.06777'
    value_gap_source_title: Asynchronous Message Passing for Addressing Oversquashing
      in Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010759999999999992
    value_note: global 0.7313 within std
    paper_rank: 144
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.7313
    sort_std: 0.0069
    is_best: false
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.7308
    std: 0.01396
    paper_value: 0.7308
    paper_std: 0.01396
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 116
    true_value: 0.7308
    true_std: 0.01396
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7308
    sort_std: 0.01396
    is_best: false
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.73036
    std: 0.01291
    paper_value: 0.73036
    paper_std: 0.01291
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 117
    true_value: 0.73036
    true_std: 0.01291
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73036
    sort_std: 0.01291
    is_best: false
  - model: GCN + GTR
    model_key: gcn + gtr
    model_plain: GCN + GTR
    value: 0.72991
    std: 0.01956
    paper_value: 0.72991
    paper_std: 0.01956
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 122
    true_value: 0.72991
    true_std: 0.01956
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72991
    sort_std: 0.01956
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.72902
    std: 0.01419
    paper_value: 0.72902
    paper_std: 0.01419
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 123
    true_value: 0.72902
    true_std: 0.01419
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72902
    sort_std: 0.01419
    is_best: false
  - model: GCN + SDRF
    model_key: gcn + sdrf
    model_plain: GCN + SDRF
    value: 0.67277
    std: 0.0217
    paper_value: 0.67277
    paper_std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 124
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05623000000000011
    value_note: ''
    paper_rank: 189
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: GIN-SDRF-R
    model_key: gin-sdrf-r
    model_plain: GIN-SDRF-R
    value: 0.69509
    std: 0.01709
    paper_value: 0.69509
    paper_std: 0.01709
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 125
    true_value: 0.7290000000000001
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03391000000000011
    value_note: ''
    paper_rank: 182
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.7290000000000001
    sort_std: 0.018000000000000002
    is_best: false
  - model: GCN + DIGL
    model_key: gcn + digl
    model_plain: GCN + DIGL
    value: 0.72321
    std: 0.0144
    paper_value: 0.72321
    paper_std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 138
    true_value: 0.72321
    true_std: 0.0144
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72321
    sort_std: 0.0144
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.71071
    std: 0.01506
    paper_value: 0.71071
    paper_std: 0.01506
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 163
    true_value: 0.71071
    true_std: 0.01506
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71071
    sort_std: 0.01506
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.70848
    std: 0.01568
    paper_value: 0.70848
    paper_std: 0.01568
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 169
    true_value: 0.70848
    true_std: 0.01568
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.70848
    sort_std: 0.01568
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
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
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7566
    std: 0.0104
    paper_value: 0.7566
    paper_std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2114999999999999
    value_note: ''
    paper_rank: 169
    rank_delta: 166
    rank_delta_abs: 166
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7678
    std: 0.0183
    paper_value: 0.7678
    paper_std: 0.0183
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20019999999999993
    value_note: ''
    paper_rank: 144
    rank_delta: 140
    rank_delta_abs: 140
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.7899
    std: 0.009
    paper_value: 0.7899
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 69
    true_value: 0.7899
    true_std: 0.009
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7899
    sort_std: 0.009
    is_best: false
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.7794
    std: 0.0122
    paper_value: 0.7794
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 117
    true_value: 0.7794
    true_std: 0.0122
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7794
    sort_std: 0.0122
    is_best: false
  - model: CGP
    model_key: cgp
    model_plain: CGP
    value: 0.7794
    std: 0.0122
    paper_value: 0.7794
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 118
    true_value: 0.7794
    true_std: 0.0122
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7794
    sort_std: 0.0122
    is_best: false
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.7731
    std: 0.0081
    paper_value: 0.7731
    paper_std: 0.0081
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 128
    true_value: 0.7731
    true_std: 0.0081
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7731
    sort_std: 0.0081
    is_best: false
  - model: GIN + FA
    model_key: gin + fa
    model_plain: GIN + FA
    value: 0.7718
    std: 0.0147
    paper_value: 0.7718
    paper_std: 0.0147
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 133
    true_value: 0.7718
    true_std: 0.0147
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 133
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7718
    sort_std: 0.0147
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7628
    std: 0.0191
    paper_value: 0.7628
    paper_std: 0.0191
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 158
    true_value: 0.7628
    true_std: 0.0191
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7628
    sort_std: 0.0191
    is_best: false
  - model: GCN + Master Node
    model_key: gcn + master node
    model_plain: GCN + Master Node
    value: 0.7608
    std: 0.0134
    paper_value: 0.7608
    paper_std: 0.0134
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 161
    true_value: 0.7608
    true_std: 0.0134
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7608
    sort_std: 0.0134
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.7537
    std: 0.0076
    paper_value: 0.7537
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 176
    true_value: 0.7537
    true_std: 0.0076
    value_gap_source_arxiv: '2410.03424'
    value_gap_source_title: Cayley Graph Propagation
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7537
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
  dataset: ogbg-molpcba
  rows:
  - model: EGP (GCN)
    model_key: egp (gcn)
    model_plain: EGP (GCN)
    value: 0.6821
    std: 0.0045
    paper_value: 0.6821
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.6821
    sort_std: 0.0045
    is_best: true
  - model: GCN + CGP
    model_key: gcn + cgp
    model_plain: GCN + CGP
    value: 0.6782
    std: 0.0066
    paper_value: 0.6782
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.6782
    sort_std: 0.0066
    is_best: true
  - model: GIN + CGP
    model_key: gin + cgp
    model_plain: GIN + CGP
    value: 0.6562
    std: 0.0147
    paper_value: 0.6562
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.6562
    sort_std: 0.0147
    is_best: false
  - model: EGP (GIN)
    model_key: egp (gin)
    model_plain: EGP (GIN)
    value: 0.6533
    std: 0.119
    paper_value: 0.6533
    paper_std: 0.119
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.6533
    sort_std: 0.119
    is_best: true
  - model: GCN + Master Node
    model_key: gcn + master node
    model_plain: GCN + Master Node
    value: 0.6069
    std: 0.0062
    paper_value: 0.6069
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: null
    sort_value: 0.6069
    sort_std: 0.0062
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5888
    std: 0.0441
    paper_value: 0.5888
    paper_std: 0.0441
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 41
    sort_value: 0.5888
    sort_std: 0.0441
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5483
    std: 0.0209
    paper_value: 0.5483
    paper_std: 0.0209
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table OGB
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbg-molpcba (score=86)'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 40
    sort_value: 0.5483
    sort_std: 0.0209
    is_best: false
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
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
    global_rank: 2
    sort_value: 0.3086
    sort_std: 0.0031
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: OGB
  datasets:
  - *id006
  - *id007
main_figure: /figures/2410.03424/main_figure.png
---

