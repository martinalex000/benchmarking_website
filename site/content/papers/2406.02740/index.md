---
title: Long Range Propagation on Continuous-Time Dynamic Graphs
arxiv_id: '2406.02740'
source_url: ''
authors: []
published_date: Jun 4, 2024
published_date_iso: '2024-06-04'
abstract: Learning Continuous-Time Dynamic Graphs (C-TDGs) requires accurately modeling
  spatio-temporal information on streams of irregularly sampled events. While many
  methods have been proposed recently, we find that most message passing-, recurrent-
  or self-attention-based methods perform poorly on long-range tasks. These tasks
  require correlating information that occurred "far" away from the current event,
  either spatially (higher-order node information) or along the time dimension (events
  occurred in the past). To address long-range dependencies, we introduce Continuous-Time
  Graph Anti-Symmetric Network (CTAN). Grounded within the ordinary differential equations
  framework, our method is designed for efficient propagation of information. In this
  paper, we show how CTAN's (i) long-range modeling capabilities are substantiated
  by theoretical findings and how (ii) its empirical performance on synthetic long-range
  benchmarks and real-world benchmarks is superior to other methods. Our results motivate
  CTAN's ability to propagate long-range information in C-TDGs as well as the inclusion
  of long-range tasks as part of temporal graph models evaluation.
codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- DGNs
mrr: 0.0233
adjusted_mrr: 0.0078
mrr_dataset_count: 1
benchmark_categories:
- Classic
- TU Dortmund
- LRGB
- OGB
- GraphBench
task_categories:
- graph_classification
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id006
  dataset: BA graph
  rows:
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 1
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
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
    sort_std: 0.0
    is_best: true
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 2
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
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
    sort_std: 0.0
    is_best: true
  - model: GraphMixer
    model_key: graphmixer
    model_plain: GraphMixer
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 3
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 4
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 5
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 6
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: DGNs
    model_key: dgns
    model_plain: DGNs
    value: 1.0
    std: 0.0
    paper_value: 1.0
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ba graph (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 7
    true_value: 1.0
    true_std: 0.0
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: RoGN
    model_key: rogn
    model_plain: RoGN
    value: 0.968
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.968
    sort_std: 0.001
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.955
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.955
    sort_std: 0.001
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.948
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.08023'
    title: Edge-Wise Graph-Instructed Neural Networks
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: https://github.com/Fra0013To/GINN
    uses_external_data: false
    is_global_top: true
    global_rank: 10
    sort_value: 0.948
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9285
    std: 0.0054
    metric: Accuracy
    higher_is_better: true
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9285
    sort_std: 0.0054
    is_best: true
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
    value: 0.9171
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9171
    sort_std: 0.0029
    is_best: false
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
    codebase_url: https://github.com/Hugo-Attali/TRIGON-CIKM-2025
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: false
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 0.0845
    std: 0.0013
    paper_value: 0.0845
    paper_std: 0.0013
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0845
    sort_std: 0.0013
    is_best: false
  - model: DGNs
    model_key: dgns
    model_plain: DGNs
    value: 0.0789
    std: 0.0033
    paper_value: 0.0789
    paper_std: 0.0033
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0789
    sort_std: 0.0033
    is_best: false
  - model: GraphMixer
    model_key: graphmixer
    model_plain: GraphMixer
    value: 0.066
    std: 0.0011
    paper_value: 0.066
    paper_std: 0.0011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.066
    sort_std: 0.0011
    is_best: false
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 0.0633
    std: 0.0041
    paper_value: 0.0633
    paper_std: 0.0041
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0633
    sort_std: 0.0041
    is_best: false
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 0.0604
    std: 0.0027
    paper_value: 0.0604
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0604
    sort_std: 0.0027
    is_best: false
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 0.0539
    std: 0.0019
    paper_value: 0.0539
    paper_std: 0.0019
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0539
    sort_std: 0.0019
    is_best: false
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 0.0529
    std: 0.0047
    paper_value: 0.0529
    paper_std: 0.0047
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to random 10-fold (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0529
    sort_std: 0.0047
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: D&D
  rows:
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.20406'
    title: Short-Range Oversquashing
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/YakovM93/Short-Range-Oversquashing
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: DGNs
    model_key: dgns
    model_plain: DGNs
    value: 0.9755
    std: 0.0009
    paper_value: 0.9755
    paper_std: 0.0009
    metric: AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9755
    sort_std: 0.0009
    is_best: false
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 0.956
    std: 0.0018
    paper_value: 0.956
    paper_std: 0.0018
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.956
    sort_std: 0.0018
    is_best: false
  - model: VRN Ensemble
    model_key: vrn ensemble
    model_plain: VRN Ensemble
    value: 0.9554
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9554
    sort_std: null
    is_best: false
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 0.9491
    std: 0.0025
    paper_value: 0.9491
    paper_std: 0.0025
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9491
    sort_std: 0.0025
    is_best: false
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 0.9468
    std: 0.0105
    paper_value: 0.9468
    paper_std: 0.0105
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9468
    sort_std: 0.0105
    is_best: false
  - model: MVCNN
    model_key: mvcnn
    model_plain: MVCNN
    value: 0.901
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1703.06114'
    title: Deep Sets
    date: Mar 2017
    date_display: Mar 2017
    date_iso: 2017-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 0.8864
    std: 0.0015
    paper_value: 0.8864
    paper_std: 0.0015
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.8864
    sort_std: 0.0015
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: PascalVOC-SP
  rows:
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.4561
    std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4561
    sort_std: 0.0039
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.4352
    std: 0.003
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4352
    sort_std: 0.003
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.4191
    std: 0.0126
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.00282'
    title: 'GraphMinNet: Learning Dependencies in Graphs with Light Complexity Minimal
      Architecture'
    date: Feb 1, 2025
    date_display: Feb 2025
    date_iso: '2025-02-01'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4191
    sort_std: 0.0126
    is_best: false
  - model: DGNs
    model_key: dgns
    model_plain: DGNs
    value: 0.0998
    std: 0.0033
    paper_value: 0.0998
    paper_std: 0.0033
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 43
    true_value: 0.0998
    true_std: 0.0033
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0998
    sort_std: 0.0033
    is_best: false
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 0.0807
    std: 0.0027
    paper_value: 0.0807
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 44
    true_value: 0.0807
    true_std: 0.0027
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0807
    sort_std: 0.0027
    is_best: false
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 0.0604
    std: 0.0026
    paper_value: 0.0604
    paper_std: 0.0026
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 45
    true_value: 0.0604
    true_std: 0.0026
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0604
    sort_std: 0.0026
    is_best: false
  - model: GraphMixer
    model_key: graphmixer
    model_plain: GraphMixer
    value: 0.0588
    std: 0.0008
    paper_value: 0.0588
    paper_std: 0.0008
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 46
    true_value: 0.0588
    true_std: 0.0008
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0588
    sort_std: 0.0008
    is_best: false
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 0.0576
    std: 0.0035
    paper_value: 0.0576
    paper_std: 0.0035
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 47
    true_value: 0.0576
    true_std: 0.0035
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0576
    sort_std: 0.0035
    is_best: false
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 0.0559
    std: 0.0024
    paper_value: 0.0559
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 48
    true_value: 0.0559
    true_std: 0.0024
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0559
    sort_std: 0.0024
    is_best: false
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 0.0523
    std: 0.0011
    paper_value: 0.0523
    paper_std: 0.0011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to pascalvoc-sp (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 49
    true_value: 0.0523
    true_std: 0.0011
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0523
    sort_std: 0.0011
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
  dataset: Reddit
  rows:
  - model: DGNs
    model_key: dgns
    model_plain: DGNs
    value: 0.9861
    std: 0.0004
    paper_value: 0.9861
    paper_std: 0.0004
    metric: AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9861
    sort_std: 0.0004
    is_best: true
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 0.9823
    std: 0.001
    paper_value: 0.9823
    paper_std: 0.001
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9823
    sort_std: 0.001
    is_best: false
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 0.9818
    std: 0.0005
    paper_value: 0.9818
    paper_std: 0.0005
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9818
    sort_std: 0.0005
    is_best: false
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 0.9751
    std: 0.001
    paper_value: 0.9751
    paper_std: 0.001
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9751
    sort_std: 0.001
    is_best: false
  - model: SIGN
    model_key: sign
    model_plain: SIGN
    value: 0.968
    std: 0.0
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.968
    sort_std: 0.0
    is_best: false
  - model: Cluster-GCN
    model_key: cluster-gcn
    model_plain: Cluster-GCN
    value: 0.966
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1905.07953'
    title: 'Cluster-GCN: An Efficient Algorithm for Training Deep and Large Graph
      Convolutional Networks'
    date: May 2019
    date_display: May 2019
    date_iso: 2019-05
    codebase_url: https://github.com/google-research/google-research
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.966
    sort_std: null
    is_best: false
  - model: GraphSAINT
    model_key: graphsaint
    model_plain: GraphSAINT
    value: 0.966
    std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2004.11198'
    title: 'SIGN: Scalable Inception Graph Neural Networks'
    date: Apr 2020
    date_display: Apr 2020
    date_iso: 2020-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.966
    sort_std: 0.001
    is_best: false
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 0.9634
    std: 0.0083
    paper_value: 0.9634
    paper_std: 0.0083
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9634
    sort_std: 0.0083
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: ogbl-wikikg2
  rows:
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 0.7983
    std: 0.0042
    paper_value: 0.7983
    paper_std: 0.0042
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 1
    true_value: 0.7983
    true_std: 0.0042
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7983
    sort_std: 0.0042
    is_best: true
  - model: TCL
    model_key: tcl
    model_plain: TCL
    value: 0.7811
    std: 0.002
    paper_value: 0.7811
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.9
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 2
    true_value: 0.7811
    true_std: 0.002
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7811
    sort_std: 0.002
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.746
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.746
    sort_std: 0.001
    is_best: false
  - model: RotatE + GCN
    model_key: rotate + gcn
    model_plain: RotatE + GCN
    value: 0.738
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.738
    sort_std: 0.002
    is_best: false
  - model: ComplEx + GCN
    model_key: complex + gcn
    model_plain: ComplEx + GCN
    value: 0.735
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2103.09430'
    title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    codebase_url: https://github.com/snap-stanford/ogb
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.735
    sort_std: 0.002
    is_best: false
  - model: CAWN
    model_key: cawn
    model_plain: CAWN
    value: 0.7304
    std: 0.006
    paper_value: 0.7304
    paper_std: 0.006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 4.0
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 7
    true_value: 0.7304
    true_std: 0.006
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7304
    sort_std: 0.006
    is_best: false
  - model: TGN
    model_key: tgn
    model_plain: TGN
    value: 0.6893
    std: 0.0053
    paper_value: 0.6893
    paper_std: 0.0053
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 11
    true_value: 0.6893
    true_std: 0.0053
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6893
    sort_std: 0.0053
    is_best: false
  - model: CTAN
    model_key: ctan
    model_plain: CTAN
    value: 0.6676
    std: 0.0074
    paper_value: 0.6676
    paper_std: 0.0074
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 16
    true_value: 0.6676
    true_std: 0.0074
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6676
    sort_std: 0.0074
    is_best: false
  - model: EdgeBank_re
    model_key: edgebank_re
    model_plain: EdgeBank_re
    value: 0.6588
    std: null
    paper_value: 0.6588
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 19
    true_value: 0.6588
    true_std: null
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6588
    sort_std: null
    is_best: false
  - model: EdgeBank_tw-ts
    model_key: edgebank_tw-ts
    model_plain: EdgeBank_tw-ts
    value: 0.6325
    std: null
    paper_value: 0.6325
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 22
    true_value: 0.6325
    true_std: null
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6325
    sort_std: null
    is_best: false
  - model: JODIE
    model_key: jodie
    model_plain: JODIE
    value: 0.6305
    std: 0.0169
    paper_value: 0.6305
    paper_std: 0.0169
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 23
    true_value: 0.6305
    true_std: 0.0169
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6305
    sort_std: 0.0169
    is_best: false
  - model: TGAT
    model_key: tgat
    model_plain: TGAT
    value: 0.5994
    std: 0.0163
    paper_value: 0.5994
    paper_std: 0.0163
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 24
    true_value: 0.5994
    true_std: 0.0163
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5994
    sort_std: 0.0163
    is_best: false
  - model: GraphMixer
    model_key: graphmixer
    model_plain: GraphMixer
    value: 0.5975
    std: 0.0039
    paper_value: 0.5975
    paper_std: 0.0039
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 25
    true_value: 0.5975
    true_std: 0.0039
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5975
    sort_std: 0.0039
    is_best: false
  - model: EdgeBank_th
    model_key: edgebank_th
    model_plain: EdgeBank_th
    value: 0.5281
    std: null
    paper_value: 0.5281
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 27
    true_value: 0.5281
    true_std: null
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5281
    sort_std: null
    is_best: false
  - model: EdgeBank_inf
    model_key: edgebank_inf
    model_plain: EdgeBank_inf
    value: 0.525
    std: null
    paper_value: 0.525
    paper_std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 28
    true_value: 0.525
    true_std: null
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.525
    sort_std: null
    is_best: false
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 0.5191
    std: 0.0195
    paper_value: 0.5191
    paper_std: 0.0195
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: huang2023empirical
    variant_inference_reason: 'dataset: fuzzy match to ogbl-wikikg2 (score=75)'
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 30
    true_value: 0.5191
    true_std: 0.0195
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5191
    sort_std: 0.0195
    is_best: false
  metric: MRR
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
- benchmark: TU Dortmund
  datasets:
  - *id003
- benchmark: LRGB
  datasets:
  - *id004
- benchmark: OGB
  datasets:
  - *id005
- benchmark: GraphBench
  datasets:
  - *id006
single_proposed_model: DGNs
main_figure: /figures/2406.02740/main_figure.png
---

