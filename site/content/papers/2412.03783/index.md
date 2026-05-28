---
title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
  An Information-Flow Centric Review'
arxiv_id: '2412.03783'
source_url: ''
authors: []
published_date: Dec 2024
published_date_iso: 2024-12
abstract: Graphs are ubiquitous in real-world applications, ranging from social networks
  to biological systems, and have inspired the development of Graph Neural Networks
  (GNNs) for learning expressive representations. While most research has centered
  on static graphs, many real-world scenarios involve dynamic, temporally evolving
  graphs, motivating the need for Continuous-Time Dynamic Graph (CTDG) models. This
  paper provides a comprehensive review of Graph Representation Learning (GRL) on
  CTDGs with a focus on Self-Supervised Representation Learning (SSRL). We introduce
  a novel theoretical framework that analyzes the expressivity of CTDG models through
  an Information-Flow (IF) lens, quantifying their ability to propagate and encode
  temporal and structural information. Leveraging this framework, we categorize existing
  CTDG methods based on their suitability for different graph types and application
  scenarios. Within the same scope, we examine the design of SSRL methods tailored
  to CTDGs, such as predictive and contrastive approaches, highlighting their potential
  to mitigate the reliance on labeled data. Empirical evaluations on synthetic and
  real-world datasets validate our theoretical insights, demonstrating the strengths
  and limitations of various methods across long-range, bi-partite and community-based
  graphs. This work offers both a theoretical foundation and practical guidance for
  selecting and developing CTDG models, advancing the understanding of GRL in dynamic
  settings.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- CTAN
mrr: 0.1667
adjusted_mrr: 0.0556
mrr_dataset_count: 1
benchmark_categories:
- OGB
task_categories:
- link_prediction
experiment_scopes:
- edge-level
results:
- &id001
  dataset: ogbl-wikikg2
  rows:
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 0.7983
    std: 0.0042
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7983
    sort_std: 0.0042
    is_best: true
  - model: TCL
    model_key: tcl
    model_plain: TCL
    value: 0.7811
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.9
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7811
    sort_std: 0.002
    is_best: false
  - model: CAWN
    model_key: cawn
    model_plain: CAWN
    value: 0.7304
    std: 0.006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 4.0
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7304
    sort_std: 0.006
    is_best: false
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 0.577
    std: 0.015
    paper_value: 0.577
    paper_std: 0.015
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 5
    true_value: 0.6893
    true_std: 0.0053
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 19
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6893
    sort_std: 0.0053
    is_best: false
  - model: CTAN
    model_key: ctan
    model_plain: CTAN
    value: 0.611
    std: 0.011
    paper_value: 0.611
    paper_std: 0.011
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 6
    true_value: 0.6676
    true_std: 0.0074
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056599999999999984
    value_note: ''
    paper_rank: 13
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.6676
    sort_std: 0.0074
    is_best: false
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 0.261
    std: 0.123
    paper_value: 0.261
    paper_std: 0.123
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 13
    true_value: 0.6305
    true_std: 0.0169
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36949999999999994
    value_note: ''
    paper_rank: 27
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6305
    sort_std: 0.0169
    is_best: false
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 0.282
    std: 0.022
    paper_value: 0.282
    paper_std: 0.022
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 18
    true_value: 0.5994
    true_std: 0.0163
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.31740000000000007
    value_note: ''
    paper_rank: 27
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.5994
    sort_std: 0.0163
    is_best: false
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 0.263
    std: 0.005
    paper_value: 0.263
    paper_std: 0.005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 21
    true_value: 0.5191
    true_std: 0.0195
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2561
    value_note: ''
    paper_rank: 27
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.5191
    sort_std: 0.0195
    is_best: false
  metric: MRR
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
single_proposed_model: CTAN
main_figure: /figures/2412.03783/main_figure.png
---

