---
title: Edge-Wise Graph-Instructed Neural Networks
arxiv_id: '2409.08023'
source_url: ''
authors: []
published_date: Sep 2024
published_date_iso: 2024-09
abstract: The problem of multi-task regression over graph nodes has been recently
  approached through Graph-Instructed Neural Network (GINN), which is a promising
  architecture belonging to the subset of message-passing graph neural networks. In
  this work, we discuss the limitations of the Graph-Instructed (GI) layer, and we
  formalize a novel edge-wise GI (EWGI) layer. We discuss the advantages of the EWGI
  layer and we provide numerical evidence that EWGINNs perform better than GINNs over
  with chaotic connectivity, like the ones inferred from the Erdos-R\'enyi graph.
codebase_url: https://github.com/Fra0013To/GINN
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- RoGN
mrr: 0.2222
adjusted_mrr: 0.1481
mrr_dataset_count: 2
benchmark_categories:
- GraphBench
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: BA graph
  rows:
  - model: DyGFormer
    model_key: dygformer
    model_plain: DyGFormer
    value: 1.0
    std: 0.0
    metric: Accuracy
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
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: DyRep
    model_key: dyrep
    model_plain: DyRep
    value: 1.0
    std: 0.0
    metric: Accuracy
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
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: GraphMixer
    model_key: graphmixer
    model_plain: GraphMixer
    value: 1.0
    std: 0.0
    metric: Accuracy
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
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.955
    std: 0.001
    paper_value: 0.955
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 8
    true_value: 0.98
    true_std: 0.005
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025000000000000022
    value_note: ''
    paper_rank: 11
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.98
    sort_std: 0.005
    is_best: false
  - model: RoGN
    model_key: rogn
    model_plain: RoGN
    value: 0.968
    std: 0.001
    paper_value: 0.968
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 9
    true_value: 0.968
    true_std: 0.001
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.968
    sort_std: 0.001
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.948
    std: 0.001
    paper_value: 0.948
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 10
    true_value: 0.96
    true_std: 0.01
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01200000000000001
    value_note: ''
    paper_rank: 13
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.96
    sort_std: 0.01
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.942
    std: 0.002
    paper_value: 0.942
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 12
    true_value: 0.95
    true_std: 0.01
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.9500 within std
    paper_rank: 13
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.95
    sort_std: 0.01
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.935
    std: 0.002
    paper_value: 0.935
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 14
    true_value: 0.94
    true_std: 0.01
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.004999999999999893
    value_note: global 0.9400 within std
    paper_rank: 15
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.94
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.921
    std: 0.003
    paper_value: 0.921
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 16
    true_value: 0.93
    true_std: 0.01
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009000000000000008
    value_note: global 0.9300 within std
    paper_rank: 17
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.93
    sort_std: 0.01
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.912
    std: 0.004
    paper_value: 0.912
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 18
    true_value: 0.92
    true_std: 0.01
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.9200 within std
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.92
    sort_std: 0.01
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.888
    std: 0.006
    paper_value: 0.888
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 19
    true_value: 0.91
    true_std: 0.01
    value_gap_source_arxiv: '1710.10321'
    value_gap_source_title: arXiv:1710.10321
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02200000000000002
    value_note: ''
    paper_rank: 21
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.91
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.895
    std: 0.005
    paper_value: 0.895
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 21
    true_value: 0.895
    true_std: 0.005
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.895
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: ER graph
  rows:
  - model: 1-WL_F
    model_key: 1-wl_f
    model_plain: 1-WL_F
    value: 1.0
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 1.0
    sort_std: 0.0
    is_best: true
  - model: 1-WLOA_F
    model_key: 1-wloa_f
    model_plain: 1-WLOA_F
    value: 0.986
    std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.07568'
    title: '--Leman at the margin: When more expressivity matters'
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://www.github.com/chrsmrrs/wl
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.986
    sort_std: 0.0
    is_best: false
  - model: RoGN
    model_key: rogn
    model_plain: RoGN
    value: 0.935
    std: 0.006
    paper_value: 0.935
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 3
    true_value: 0.935
    true_std: 0.006
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.935
    sort_std: 0.006
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.921
    std: 0.008
    paper_value: 0.921
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 4
    true_value: 0.921
    true_std: 0.008
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.921
    sort_std: 0.008
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.915
    std: 0.009
    paper_value: 0.915
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 5
    true_value: 0.915
    true_std: 0.009
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.915
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.91
    std: 0.01
    paper_value: 0.91
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 6
    true_value: 0.91
    true_std: 0.01
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.91
    sort_std: 0.01
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.905
    std: 0.012
    paper_value: 0.905
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 7
    true_value: 0.905
    true_std: 0.012
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.905
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.892
    std: 0.015
    paper_value: 0.892
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 8
    true_value: 0.892
    true_std: 0.015
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.892
    sort_std: 0.015
    is_best: false
  - model: MGNN
    model_key: mgnn
    model_plain: MGNN
    value: 0.891
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15646'
    title: Expressive Power of Invariant and Equivariant Graph Neural Networks
    date: Jun 2020
    date_display: Jun 2020
    date_iso: 2020-06
    codebase_url: https://github.com/mlelarge/graph_neural_net
    uses_external_data: false
    is_global_top: true
    global_rank: 9
    sort_value: 0.891
    sort_std: 0.009
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.885
    std: 0.018
    paper_value: 0.885
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
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    global_rank: 11
    true_value: 0.885
    true_std: 0.018
    value_gap_source_arxiv: '2409.08023'
    value_gap_source_title: Edge-Wise Graph-Instructed Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.885
    sort_std: 0.018
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GraphBench
  datasets:
  - *id001
  - *id002
single_proposed_model: RoGN
main_figure: /figures/2409.08023/main_figure.png
---

