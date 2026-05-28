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
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CTAN
- Our
mrr: 0.0087
adjusted_mrr: 0.0029
mrr_dataset_count: 1
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- OGB
task_categories:
- graph_classification
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0845
    sort_std: 0.0013
    is_best: false
  - model: Our
    model_key: our
    model_plain: Our
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.0529
    sort_std: 0.0047
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: D&D
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.989
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
    global_rank: 1
    sort_value: 0.989
    sort_std: null
    is_best: true
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    value: 0.981
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
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    value: 0.976
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
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: Our
    model_key: our
    model_plain: Our
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.956
    sort_std: 0.0018
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9468
    sort_std: 0.0105
    is_best: false
  - model: EdgeBank (infinity)
    model_key: edgebank (infinity)
    model_plain: EdgeBank (infinity)
    value: 0.9182
    std: null
    paper_value: 0.9182
    paper_std: null
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9182
    sort_std: null
    is_best: false
  - model: EdgeBank (1% tr set)
    model_key: edgebank (1% tr set)
    model_plain: EdgeBank (1% tr set)
    value: 0.9152
    std: null
    paper_value: 0.9152
    paper_std: null
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9152
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.8864
    sort_std: 0.0015
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
  - model: Our
    model_key: our
    model_plain: Our
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 115
    true_value: 0.0998
    true_std: 0.0033
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 116
    true_value: 0.0807
    true_std: 0.0027
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 118
    true_value: 0.0604
    true_std: 0.0026
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 120
    true_value: 0.0588
    true_std: 0.0008
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 120
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 121
    true_value: 0.0576
    true_std: 0.0035
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 121
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 122
    true_value: 0.0559
    true_std: 0.0024
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 123
    true_value: 0.0523
    true_std: 0.0011
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
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
  - model: Our
    model_key: our
    model_plain: Our
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9751
    sort_std: 0.001
    is_best: false
  - model: EdgeBank
    model_key: edgebank
    model_plain: EdgeBank
    value: 0.9642
    std: null
    paper_value: 0.9642
    paper_std: null
    metric: AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9642
    sort_std: null
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
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: null
    sort_value: 0.9634
    sort_std: 0.0083
    is_best: false
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
    is_best: false
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
    is_best: false
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
    source_ref: yu2023towards
    variant_inference_reason: ''
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 3
    true_value: 0.7304
    true_std: 0.006
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
    sort_value: 0.7304
    sort_std: 0.006
    is_best: false
  - model: TNCN
    model_key: tncn
    model_plain: TNCN
    value: 0.711
    std: 0.007
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.711
    sort_std: 0.007
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 5
    true_value: 0.6893
    true_std: 0.0053
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 6
    true_value: 0.6676
    true_std: 0.0074
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
    sort_value: 0.6676
    sort_std: 0.0074
    is_best: false
  - model: TGTalker (nbr = 2)
    model_key: tgtalker (nbr = 2)
    model_plain: TGTalker (nbr = 2)
    value: 0.656
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 7
    sort_value: 0.656
    sort_std: null
    is_best: false
  - model: Qwen3-8B
    model_key: qwen3-8b
    model_plain: Qwen3-8B
    value: 0.651
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.05393'
    title: Are Large Language Models Good Temporal Graph Learners?
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 8
    sort_value: 0.651
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 13
    true_value: 0.6305
    true_std: 0.0169
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 18
    true_value: 0.5994
    true_std: 0.0163
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
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
    source_ref: cong2023we
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 19
    true_value: 0.5975
    true_std: 0.0039
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
    sort_value: 0.5975
    sort_std: 0.0039
    is_best: false
  - model: EdgeBank
    model_key: edgebank
    model_plain: EdgeBank
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 20
    true_value: 0.525
    true_std: null
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
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
    source_ref: huang2023temporal
    variant_inference_reason: ''
    date: Jun 4, 2024
    date_display: Jun 2024
    date_iso: '2024-06-04'
    global_rank: 21
    true_value: 0.5191
    true_std: 0.0195
    value_gap_source_arxiv: '2406.02740'
    value_gap_source_title: Long Range Propagation on Continuous-Time Dynamic Graphs
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
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
- benchmark: LRGB
  datasets:
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
- benchmark: OGB
  datasets:
  - *id005
main_figure: /figures/2406.02740/main_figure.png
---

