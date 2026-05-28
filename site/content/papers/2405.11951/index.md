---
title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
arxiv_id: '2405.11951'
source_url: ''
authors: []
published_date: May 2024
published_date_iso: 2024-05
abstract: 'Graph Transformers (GTs) such as SAN and GPS are graph processing models
  that combine Message-Passing GNNs (MPGNNs) with global Self-Attention. They were
  shown to be universal function approximators, with two reservations: 1. The initial
  node features must be augmented with certain positional encodings. 2. The approximation
  is non-uniform: Graphs of different sizes may require a different approximating
  network. We first clarify that this form of universality is not unique to GTs: Using
  the same positional encodings, also pure MPGNNs and even 2-layer MLPs are non-uniform
  universal approximators. We then consider uniform expressivity: The target function
  is to be approximated by a single network for graphs of all sizes. There, we compare
  GTs to the more efficient MPGNN + Virtual Node architecture. The essential difference
  between the two model definitions is in their global computation method -- Self-Attention
  Vs Virtual Node. We prove that none of the models is a uniform-universal approximator,
  before proving our main result: Neither model’s uniform expressivity subsumes the
  other’s. We demonstrate the theory with experiments on synthetic data. We further
  augment our study with real-world datasets, observing mixed results which indicate
  no clear ranking in practice as well.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GatedGCN + VN
mrr: 1.0
adjusted_mrr: 0.3333
mrr_dataset_count: 1
benchmark_categories:
- OGB
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    paper_value: 0.3141
    paper_std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 1
    true_value: 0.3141
    true_std: 0.0019
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3141
    sort_std: 0.0019
    is_best: true
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
    paper_value: 0.3066
    paper_std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 3
    true_value: 0.3066
    true_std: 0.0013
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3066
    sort_std: 0.0013
    is_best: false
  - model: LGI-GT
    model_key: lgi-gt
    model_plain: LGI-GT
    value: 0.304
    std: 0.0029
    paper_value: 0.304
    paper_std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LGI-GT
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 4
    true_value: 0.304
    true_std: 0.0029
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.304
    sort_std: 0.0029
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.2986
    std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.2986
    sort_std: 0.0025
    is_best: false
  - model: CRaWI
    model_key: crawi
    model_plain: CRaWI
    value: 0.2986
    std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: Jul 14, 2023
    date_display: Jul 2023
    date_iso: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.2986
    sort_std: 0.0025
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2907
    std: 0.0028
    paper_value: 0.2907
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek et al. 2022
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 21
    true_value: 0.2907
    true_std: 0.0028
    value_gap_source_arxiv: '2406.12059'
    value_gap_source_title: A Scalable and Effective Alternative to Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2907
    sort_std: 0.0028
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2765
    std: 0.0042
    paper_value: 0.2765
    paper_std: 0.0042
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 36
    true_value: 0.2765
    true_std: 0.0042
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2765
    sort_std: 0.0042
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2483
    std: 0.0037
    paper_value: 0.2483
    paper_std: 0.0037
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 40
    true_value: 0.2721
    true_std: 0.0046
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.023800000000000016
    value_note: ''
    paper_rank: 49
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.2721
    sort_std: 0.0046
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2703
    std: 0.0023
    paper_value: 0.2703
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 44
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
single_proposed_model: GatedGCN + VN
main_figure: /figures/2405.11951/main_figure.png
---

