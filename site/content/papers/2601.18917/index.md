---
title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse Problems'
arxiv_id: '2601.18917'
source_url: ''
authors: []
published_date: Jan 2026
published_date_iso: 2026-01
abstract: A wide range of graph learning tasks, such as structure discovery, temporal
  graph analysis, and combinatorial optimization, focus on inferring graph structures
  from data, rather than making predictions on given graphs. However, the respective
  methods to solve such problems are often developed in an isolated, task-specific
  manner and thus lack a unifying theoretical foundation. Here, we provide a stepping
  stone towards the formation of such a foundation and further development by introducing
  the Neural Graph Inverse Problem (GraIP) conceptual framework, which formalizes
  and reframes a broad class of graph learning tasks as inverse problems. Unlike discriminative
  approaches that directly predict target variables from given graph inputs, the GraIP
  paradigm addresses inverse problems, i.e., it relies on observational data and aims
  to recover the underlying graph structure by reversing the forward process, such
  as message passing or network dynamics, that produced the observed outputs. We demonstrate
  the versatility of GraIP across various graph learning tasks, including rewiring,
  causal discovery, and neural relational inference. We also propose benchmark datasets
  and metrics for each GraIP domain considered, and characterize and empirically evaluate
  existing baseline methods used to solve them. Overall, our unifying perspective
  bridges seemingly disparate applications and provides a principled approach to structural
  learning in constrained and combinatorial settings while encouraging cross-pollination
  of existing methods across graph inverse problems.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- NRI + STE
- I-MLE
- SIMPLE
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
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
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
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
    global_rank: 2
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
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
    global_rank: 3
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
    value: 0.659
    std: 0.04
    paper_value: 0.659
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 84
    true_value: 0.659
    true_std: 0.04
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.04
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.595
    std: 0.051
    paper_value: 0.595
    paper_std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 99
    true_value: 0.595
    true_std: 0.051
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: 0.051
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.574
    std: 0.006
    paper_value: 0.574
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 107
    true_value: 0.574
    true_std: 0.006
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.574
    sort_std: 0.006
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.541
    std: 0.038
    paper_value: 0.541
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 114
    true_value: 0.541
    true_std: 0.038
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.541
    sort_std: 0.038
    is_best: false
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.51
    std: 0.057
    paper_value: 0.51
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 125
    true_value: 0.51
    true_std: 0.057
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.51
    sort_std: 0.057
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: D&D
  rows:
  - model: NRI + STE (non-blind)
    model_key: nri + ste (non-blind)
    model_plain: NRI + STE (non-blind)
    value: 0.00018
    std: 0.0
    paper_value: 0.00018
    paper_std: 0.0
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: null
    sort_value: 0.00018
    sort_std: 0.0
    is_best: true
  - model: NRI + STE
    model_key: nri + ste
    model_plain: NRI + STE
    value: 0.0021
    std: 0.0
    paper_value: 0.0021
    paper_std: 0.0
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: null
    sort_value: 0.0021
    sort_std: 0.0
    is_best: false
  - model: NRI + SIMPLE
    model_key: nri + simple
    model_plain: NRI + SIMPLE
    value: 0.0028
    std: 0.0
    paper_value: 0.0028
    paper_std: 0.0
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: null
    sort_value: 0.0028
    sort_std: 0.0
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.05
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.05
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.093
    std: null
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.093
    sort_std: null
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: false
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
    date: '2025-01-29'
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
    date: '2025-01-29'
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
    date: '2025-01-29'
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
    value: 0.683
    std: 0.009
    paper_value: 0.683
    paper_std: 0.009
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 96
    true_value: 0.683
    true_std: 0.009
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.683
    sort_std: 0.009
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.659
    std: 0.012
    paper_value: 0.659
    paper_std: 0.012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 157
    true_value: 0.659
    true_std: 0.012
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 157
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.659
    sort_std: 0.012
    is_best: false
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.651
    std: 0.003
    paper_value: 0.651
    paper_std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 180
    true_value: 0.651
    true_std: 0.003
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.651
    sort_std: 0.003
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.573
    std: 0.012
    paper_value: 0.573
    paper_std: 0.012
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 278
    true_value: 0.573
    true_std: 0.012
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 278
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.573
    sort_std: 0.012
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.55
    std: 0.008
    paper_value: 0.55
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 286
    true_value: 0.55
    true_std: 0.008
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 286
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.55
    sort_std: 0.008
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
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 100
    true_value: 0.248
    true_std: 0.001
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
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
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.251
    std: 0.001
    paper_value: 0.251
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 151
    true_value: 0.251
    true_std: 0.001
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.251
    sort_std: 0.001
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.251
    std: 0.003
    paper_value: 0.251
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 152
    true_value: 0.251
    true_std: 0.003
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 152
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.251
    sort_std: 0.003
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.252
    std: 0.003
    paper_value: 0.252
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 158
    true_value: 0.252
    true_std: 0.003
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.252
    sort_std: 0.003
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.355
    std: 0.005
    paper_value: 0.355
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 308
    true_value: 0.355
    true_std: 0.005
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 308
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.355
    sort_std: 0.005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
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
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
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
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
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
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
    value: 0.827
    std: 0.032
    paper_value: 0.827
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 47
    true_value: 0.827
    true_std: 0.032
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.032
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.789
    std: 0.067
    paper_value: 0.789
    paper_std: 0.067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 64
    true_value: 0.789
    true_std: 0.067
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.789
    sort_std: 0.067
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.784
    std: 0.033
    paper_value: 0.784
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 65
    true_value: 0.784
    true_std: 0.033
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.784
    sort_std: 0.033
    is_best: false
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.738
    std: 0.012
    paper_value: 0.738
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 95
    true_value: 0.738
    true_std: 0.012
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.012
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.674
    std: 0.01
    paper_value: 0.674
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
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 116
    true_value: 0.674
    true_std: 0.01
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.674
    sort_std: 0.01
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
    value: 0.75
    std: 0.015
    paper_value: 0.75
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 79
    true_value: 0.75
    true_std: 0.015
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.015
    is_best: false
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.731
    std: 0.005
    paper_value: 0.731
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 92
    true_value: 0.731
    true_std: 0.005
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.005
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.706
    std: 0.037
    paper_value: 0.706
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 95
    true_value: 0.706
    true_std: 0.037
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.706
    sort_std: 0.037
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.697
    std: 0.013
    paper_value: 0.697
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 98
    true_value: 0.697
    true_std: 0.013
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.013
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.694
    std: 0.022
    paper_value: 0.694
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 102
    true_value: 0.694
    true_std: 0.022
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.694
    sort_std: 0.022
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
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.148
    std: 0.008
    paper_value: 0.148
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 218
    true_value: 0.148
    true_std: 0.008
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.148
    sort_std: 0.008
    is_best: false
  - model: I-MLE
    model_key: i-mle
    model_plain: I-MLE
    value: 0.148
    std: 0.008
    paper_value: 0.148
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 218
    true_value: 0.148
    true_std: 0.008
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.148
    sort_std: 0.008
    is_best: false
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
    value: 0.151
    std: 0.001
    paper_value: 0.151
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 220
    true_value: 0.151
    true_std: 0.001
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 220
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.151
    sort_std: 0.001
    is_best: false
  - model: SIMPLE
    model_key: simple
    model_plain: SIMPLE
    value: 0.151
    std: 0.001
    paper_value: 0.151
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 220
    true_value: 0.151
    true_std: 0.001
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 220
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.151
    sort_std: 0.001
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.16
    std: 0.006
    paper_value: 0.16
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 230
    true_value: 0.16
    true_std: 0.006
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 230
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.16
    sort_std: 0.006
    is_best: false
  - model: Gumbel
    model_key: gumbel
    model_plain: Gumbel
    value: 0.16
    std: 0.006
    paper_value: 0.16
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 230
    true_value: 0.16
    true_std: 0.006
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 230
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.16
    sort_std: 0.006
    is_best: false
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.19
    std: 0.007
    paper_value: 0.19
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 240
    true_value: 0.19
    true_std: 0.007
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 240
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.19
    sort_std: 0.007
    is_best: false
  - model: Random rewire
    model_key: random rewire
    model_plain: Random rewire
    value: 0.19
    std: 0.007
    paper_value: 0.19
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 240
    true_value: 0.19
    true_std: 0.007
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 240
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.19
    sort_std: 0.007
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.209
    std: 0.005
    paper_value: 0.209
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 249
    true_value: 0.209
    true_std: 0.005
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.209
    sort_std: 0.005
    is_best: false
  - model: Baseline (GINE)
    model_key: baseline (gine)
    model_plain: Baseline (GINE)
    value: 0.209
    std: 0.005
    paper_value: 0.209
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2026
    date_display: Jan 2026
    date_iso: 2026-01
    global_rank: 249
    true_value: 0.209
    true_std: 0.005
    value_gap_source_arxiv: '2601.18917'
    value_gap_source_title: 'GraIP: A Benchmarking Framework For Neural Graph Inverse
      Problems'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.209
    sort_std: 0.005
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Heterophilic Graphs
  datasets:
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
main_figure: /figures/2601.18917/main_figure.png
---

