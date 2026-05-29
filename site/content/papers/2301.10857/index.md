---
title: arXiv:2301.10857
arxiv_id: '2301.10857'
source_url: ''
authors: []
published_date: Jan 2023
published_date_iso: 2023-01
abstract: Deep graph generative modeling has proven capable of learning the distribution
  of complex, multi-scale structures characterizing real-world graphs. However, one
  of the main limitations of existing methods is their large output space, which limits
  generation scalability and hinders accurate modeling of the underlying distribution.
  To overcome these limitations, we propose a novel approach that significantly reduces
  the output space of existing graph generative models. Specifically, starting from
  the observation that many real-world graphs have low graph bandwidth, we restrict
  graph bandwidth during training and generation. Our strategy improves both generation
  scalability and quality without increasing architectural complexity or reducing
  expressiveness. Our approach is compatible with existing graph generative methods,
  and we describe its application to both autoregressive and one-shot models. We extensively
  validate our strategy on synthetic and real datasets, including molecular graphs.
  Our experiments show that, in addition to improving generation efficiency, our approach
  consistently improves generation quality and reconstruction accuracy. The implementation
  is made available.
codebase_url: https://github.com/Genentech/bandwidth-graph-generation
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- C-M
mrr: 0.5051
adjusted_mrr: 0.3367
mrr_dataset_count: 2
benchmark_categories:
- Classic
- TU Dortmund
- LRGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
  dataset: ENZYMES
  rows:
  - model: C-M
    model_key: c-m
    model_plain: C-M
    value: 0.802
    std: 0.009
    paper_value: 0.802
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 1
    true_value: 0.802
    true_std: 0.009
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.794
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.794
    sort_std: 0.008
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.785
    std: 0.01
    paper_value: 0.785
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
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 3
    true_value: 0.785
    true_std: 0.01
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.785
    sort_std: 0.01
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.78
    std: 0.0489
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2012.08734'
    title: Hierarchical Graph Capsule Network
    date: Dec 2020
    date_display: Dec 2020
    date_iso: 2020-12
    codebase_url: https://github.com/uta-smile/HGCN
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.78
    sort_std: 0.0489
    is_best: true
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.779
    std: 0.011
    paper_value: 0.779
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 5
    true_value: 0.779
    true_std: 0.011
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.779
    sort_std: 0.011
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.778
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.17589'
    title: Graph Inductive Biases in Transformers without Message Passing
    date: May 27, 2023
    date_display: May 2023
    date_iso: '2023-05-27'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.778
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.771
    std: 0.012
    paper_value: 0.771
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
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 7
    true_value: 0.771
    true_std: 0.012
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.771
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.762
    std: 0.015
    paper_value: 0.762
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 9
    true_value: 0.762
    true_std: 0.015
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.015
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.758
    std: 0.018
    paper_value: 0.758
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
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 11
    true_value: 0.758
    true_std: 0.018
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.018
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.745
    std: 0.021
    paper_value: 0.745
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
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 12
    true_value: 0.745
    true_std: 0.021
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Peptides-func
  rows:
  - model: S2GCN +PE
    model_key: s2gcn +pe
    model_plain: S2GCN +PE
    value: 0.7311
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7311
    sort_std: 0.0066
    is_best: true
  - model: S2GCN
    model_key: s2gcn
    model_plain: S2GCN
    value: 0.7275
    std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.07624'
    title: 'Return of ChebNet: Understanding and Improving an Overlooked GNN on Long-Range
      Tasks'
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7275
    sort_std: 0.0066
    is_best: true
  - model: gLSTM
    model_key: glstm
    model_plain: gLSTM
    value: 0.725
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.0023
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.385
    std: 0.012
    paper_value: 0.385
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
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 33
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.30100000000000005
    value_note: ''
    paper_rank: 105
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.415
    std: 0.009
    paper_value: 0.415
    paper_std: 0.009
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 97
    true_value: 0.5498
    true_std: 0.0079
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13479999999999998
    value_note: ''
    paper_rank: 102
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.5498
    sort_std: 0.0079
    is_best: false
  - model: C-M
    model_key: c-m
    model_plain: C-M
    value: 0.462
    std: 0.006
    paper_value: 0.462
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 98
    true_value: 0.462
    true_std: 0.006
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.462
    sort_std: 0.006
    is_best: false
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.451
    std: 0.007
    paper_value: 0.451
    paper_std: 0.007
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 99
    true_value: 0.451
    true_std: 0.007
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.451
    sort_std: 0.007
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.448
    std: 0.009
    paper_value: 0.448
    paper_std: 0.009
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 100
    true_value: 0.448
    true_std: 0.009
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.448
    sort_std: 0.009
    is_best: false
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.445
    std: 0.008
    paper_value: 0.445
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
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 101
    true_value: 0.445
    true_std: 0.008
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.445
    sort_std: 0.008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.432
    std: 0.01
    paper_value: 0.432
    paper_std: 0.01
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 102
    true_value: 0.432
    true_std: 0.01
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.432
    sort_std: 0.01
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.401
    std: 0.015
    paper_value: 0.401
    paper_std: 0.015
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 103
    true_value: 0.401
    true_std: 0.015
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.401
    sort_std: 0.015
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.392
    std: 0.011
    paper_value: 0.392
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 105
    true_value: 0.392
    true_std: 0.011
    value_gap_source_arxiv: '2301.10857'
    value_gap_source_title: arXiv:2301.10857
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.392
    sort_std: 0.011
    is_best: false
  metric: AP
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: C-M
    model_key: c-m
    model_plain: C-M
    value: 0.001
    std: 0.0001
    paper_value: 0.001
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: null
    sort_value: 0.001
    sort_std: 0.0001
    is_best: true
  - model: PaiNN
    model_key: painn
    model_plain: PaiNN
    value: 0.0011
    std: 0.0001
    paper_value: 0.0011
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 98
    sort_value: 0.0011
    sort_std: 0.0001
    is_best: true
  - model: DimeNet++
    model_key: dimenet++
    model_plain: DimeNet++
    value: 0.0012
    std: 0.0001
    paper_value: 0.0012
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 107
    sort_value: 0.0012
    sort_std: 0.0001
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.0013
    std: 0.0001
    paper_value: 0.0013
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 50
    sort_value: 0.0013
    sort_std: 0.0001
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.0014
    std: 0.0001
    paper_value: 0.0014
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 131
    sort_value: 0.0014
    sort_std: 0.0001
    is_best: false
  - model: GCN (RWSE)
    model_key: gcn (rwse)
    model_plain: GCN (RWSE)
    value: 0.0015
    std: 0.0001
    paper_value: 0.0015
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: null
    sort_value: 0.0015
    sort_std: 0.0001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.0016
    std: 0.0001
    paper_value: 0.0016
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 3
    sort_value: 0.0016
    sort_std: 0.0001
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.0017
    std: 0.0001
    paper_value: 0.0017
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 42
    sort_value: 0.0017
    sort_std: 0.0001
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.0018
    std: 0.0001
    paper_value: 0.0018
    paper_std: 0.0001
    metric: MMD
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 250k (score=94)'
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    global_rank: 2
    sort_value: 0.0018
    sort_std: 0.0001
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    arxiv_id: '2402.08450'
    title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph
      Products'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    codebase_url: https://github.com/BarSGuy/Subgraphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.021
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.021
    sort_std: 0.002
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
- benchmark: LRGB
  datasets:
  - *id003
single_proposed_model: C-M
main_figure: /figures/2301.10857/main_figure.png
---

