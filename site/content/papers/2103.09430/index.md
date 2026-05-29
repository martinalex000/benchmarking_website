---
title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning on Graphs'
arxiv_id: '2103.09430'
source_url: ''
authors: []
published_date: Mar 2021
published_date_iso: 2021-03
abstract: Enabling effective and efficient machine learning (ML) over large-scale
  graph data (, graphs with billions of edges) can have a great impact on both industrial
  and scientific applications. However, existing efforts to advance large-scale graph
  ML have been largely limited by the lack of a suitable public benchmark. Here we
  present OGB Large-Scale Challenge (OGB-LSC), a collection of three real-world datasets
  for facilitating the advancements in large-scale graph ML. The OGB-LSC datasets
  are orders of magnitude larger than existing ones, covering three core graph learning
  tasks---link prediction, graph regression, and node classification. Furthermore,
  we provide dedicated baseline experiments, scaling up expressive graph ML models
  to the massive datasets. We show that expressive models significantly outperform
  simple scalable baselines, indicating an opportunity for dedicated efforts to further
  improve graph ML at scale. Moreover, OGB-LSC datasets were deployed at ACM KDD Cup
  2021 and attracted more than 500 team registrations globally, during which significant
  performance improvements were made by a variety of innovative techniques. We summarize
  the common techniques used by the winning solutions and highlight the current best
  practices in large-scale graph ML. Finally, we describe how we have updated the
  datasets after the KDD Cup to further facilitate research advances. The OGB-LSC
  datasets, baseline code, and all the information about the KDD Cup are available
  at.
codebase_url: https://github.com/snap-stanford/ogb
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- ML
mrr: 0.1416
adjusted_mrr: 0.1416
mrr_dataset_count: 3
benchmark_categories:
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
  dataset: ogbg-molpcba
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
    value: 0.339
    std: 0.0073
    metric: AP
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.339
    sort_std: 0.0073
    is_best: true
  - model: unified method + FLAG
    model_key: unified method + flag
    model_plain: unified method + FLAG
    value: 0.3174
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2207.08806'
    title: Unified 2D and 3D Pre-Training of Molecular Representations
    date: Jul 2022
    date_display: Jul 2022
    date_iso: 2022-07
    codebase_url: https://github.com/teslacool/UnifiedMolPretrain
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3174
    sort_std: null
    is_best: false
  - model: TGT-Ag+TGT-At-DP
    model_key: tgt-ag+tgt-at-dp
    model_plain: TGT-Ag+TGT-At-DP
    value: 0.3167
    std: 0.0031
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04538'
    title: 'Triplet Interaction Improves Graph Transformers: Accurate Molecular Graph
      Learning with Triplet Graph Transformers'
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: https://github.com/shamim-hussain/tgt
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.3167
    sort_std: 0.0031
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.233
    std: 0.001
    paper_value: 0.233
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 5
    true_value: 0.314
    true_std: null
    value_gap_source_arxiv: '2207.08806'
    value_gap_source_title: Unified 2D and 3D Pre-Training of Molecular Representations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08099999999999999
    value_note: ''
    paper_rank: 52
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.314
    sort_std: null
    is_best: false
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.232
    std: 0.001
    paper_value: 0.232
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 22
    true_value: 0.2885
    true_std: 0.003
    value_gap_source_arxiv: '2110.07875'
    value_gap_source_title: Graph Neural Networks with Learnable Structural and Positional
      Representations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05649999999999997
    value_note: ''
    paper_rank: 53
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.2885
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.231
    std: 0.001
    paper_value: 0.231
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 27
    true_value: 0.2838
    true_std: 0.0035
    value_gap_source_arxiv: '2110.07875'
    value_gap_source_title: Graph Neural Networks with Learnable Structural and Positional
      Representations
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.052799999999999986
    value_note: ''
    paper_rank: 53
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.2838
    sort_std: 0.0035
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.229
    std: 0.001
    paper_value: 0.229
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 35
    true_value: 0.2703
    true_std: 0.0023
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.041299999999999976
    value_note: ''
    paper_rank: 55
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.2703
    sort_std: 0.0023
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.226
    std: 0.001
    paper_value: 0.226
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 46
    true_value: 0.2424
    true_std: 0.0034
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016399999999999998
    value_note: ''
    paper_rank: 58
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.2424
    sort_std: 0.0034
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.235
    std: 0.001
    paper_value: 0.235
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 50
    true_value: 0.235
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.235
    sort_std: 0.001
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.23
    std: 0.001
    paper_value: 0.23
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 54
    true_value: 0.23
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.23
    sort_std: 0.001
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.228
    std: 0.001
    paper_value: 0.228
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 56
    true_value: 0.228
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.228
    sort_std: 0.001
    is_best: false
  - model: Jumping Knowledge
    model_key: jumping knowledge
    model_plain: Jumping Knowledge
    value: 0.228
    std: 0.001
    paper_value: 0.228
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 57
    true_value: 0.228
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.228
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.227
    std: 0.001
    paper_value: 0.227
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 58
    true_value: 0.227
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.227
    sort_std: 0.001
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.225
    std: 0.001
    paper_value: 0.225
    paper_std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 59
    true_value: 0.225
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.225
    sort_std: 0.001
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
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
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
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
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7811
    sort_std: 0.002
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.746
    std: 0.001
    paper_value: 0.746
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 3
    true_value: 0.746
    true_std: 0.001
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.746
    sort_std: 0.001
    is_best: false
  - model: RotatE + GCN
    model_key: rotate + gcn
    model_plain: RotatE + GCN
    value: 0.738
    std: 0.002
    paper_value: 0.738
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 4
    true_value: 0.738
    true_std: 0.002
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.738
    sort_std: 0.002
    is_best: false
  - model: ComplEx + GCN
    model_key: complex + gcn
    model_plain: ComplEx + GCN
    value: 0.735
    std: 0.002
    paper_value: 0.735
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 5
    true_value: 0.735
    true_std: 0.002
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.735
    sort_std: 0.002
    is_best: false
  - model: DistMult + GCN
    model_key: distmult + gcn
    model_plain: DistMult + GCN
    value: 0.732
    std: 0.002
    paper_value: 0.732
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 6
    true_value: 0.732
    true_std: 0.002
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
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
    codebase_url: https://github.com/gravins/non-dissipative-propagation-CTDGs
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.7304
    sort_std: 0.006
    is_best: false
  - model: RotatE
    model_key: rotate
    model_plain: RotatE
    value: 0.728
    std: 0.003
    paper_value: 0.728
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 8
    true_value: 0.728
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.003
    is_best: false
  - model: ComplEx
    model_key: complex
    model_plain: ComplEx
    value: 0.725
    std: 0.003
    paper_value: 0.725
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 9
    true_value: 0.725
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.003
    is_best: false
  - model: DistMult
    model_key: distmult
    model_plain: DistMult
    value: 0.721
    std: 0.003
    paper_value: 0.721
    paper_std: 0.003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 10
    true_value: 0.721
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.003
    is_best: false
  - model: TransE
    model_key: transe
    model_plain: TransE
    value: 0.685
    std: 0.004
    paper_value: 0.685
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 12
    true_value: 0.685
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.685
    sort_std: 0.004
    is_best: false
  - model: R-GCN
    model_key: r-gcn
    model_plain: R-GCN
    value: 0.678
    std: 0.004
    paper_value: 0.678
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 13
    true_value: 0.678
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.678
    sort_std: 0.004
    is_best: false
  - model: CompGCN
    model_key: compgcn
    model_plain: CompGCN
    value: 0.675
    std: 0.004
    paper_value: 0.675
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 14
    true_value: 0.675
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.675
    sort_std: 0.004
    is_best: false
  - model: TuckER
    model_key: tucker
    model_plain: TuckER
    value: 0.672
    std: 0.004
    paper_value: 0.672
    paper_std: 0.004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 15
    true_value: 0.672
    true_std: 0.004
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.672
    sort_std: 0.004
    is_best: false
  - model: Holographic Embeddings
    model_key: holographic embeddings
    model_plain: Holographic Embeddings
    value: 0.665
    std: 0.005
    paper_value: 0.665
    paper_std: 0.005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 17
    true_value: 0.665
    true_std: 0.005
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.665
    sort_std: 0.005
    is_best: false
  - model: HolE
    model_key: hole
    model_plain: HolE
    value: 0.662
    std: 0.005
    paper_value: 0.662
    paper_std: 0.005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 18
    true_value: 0.662
    true_std: 0.005
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.662
    sort_std: 0.005
    is_best: false
  - model: ProjE
    model_key: proje
    model_plain: ProjE
    value: 0.658
    std: 0.005
    paper_value: 0.658
    paper_std: 0.005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 20
    true_value: 0.658
    true_std: 0.005
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.658
    sort_std: 0.005
    is_best: false
  - model: ConvE
    model_key: conve
    model_plain: ConvE
    value: 0.655
    std: 0.005
    paper_value: 0.655
    paper_std: 0.005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 21
    true_value: 0.655
    true_std: 0.005
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.655
    sort_std: 0.005
    is_best: false
  metric: MRR
  higher_is_better: true
- &id003
  dataset: ogbn-mag
  rows:
  - model: CoE
    model_key: coe
    model_plain: CoE
    value: 0.7837
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.20853'
    title: arXiv:2505.20853
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: https://github.com/strangeAlan/CoE
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7837
    sort_std: 0.0016
    is_best: true
  - model: ILSS
    model_key: ilss
    model_plain: ILSS
    value: 0.781
    std: 0.003
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
    global_rank: 2
    sort_value: 0.781
    sort_std: 0.003
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.775
    std: 0.002
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
    global_rank: 3
    sort_value: 0.775
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.708
    std: 0.004
    paper_value: 0.708
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 9
    true_value: 0.768
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06000000000000005
    value_note: ''
    paper_rank: 20
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.768
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.701
    std: 0.002
    paper_value: 0.701
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 10
    true_value: 0.761
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06000000000000005
    value_note: ''
    paper_rank: 20
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.761
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.695
    std: 0.003
    paper_value: 0.695
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 12
    true_value: 0.753
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05800000000000005
    value_note: ''
    paper_rank: 20
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.753
    sort_std: 0.002
    is_best: false
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.742
    std: 0.002
    paper_value: 0.742
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 14
    true_value: 0.742
    true_std: 0.002
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: AP-GNN
    model_key: ap-gnn
    model_plain: AP-GNN
    value: 0.731
    std: 0.002
    paper_value: 0.731
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 15
    true_value: 0.731
    true_std: 0.002
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.002
    is_best: false
  - model: HGT
    model_key: hgt
    model_plain: HGT
    value: 0.725
    std: 0.002
    paper_value: 0.725
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 17
    true_value: 0.725
    true_std: 0.002
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.002
    is_best: false
  - model: HAN
    model_key: han
    model_plain: HAN
    value: 0.718
    std: 0.003
    paper_value: 0.718
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 18
    true_value: 0.718
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.003
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.712
    std: 0.003
    paper_value: 0.712
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
    date: Mar 2021
    date_display: Mar 2021
    date_iso: 2021-03
    global_rank: 20
    true_value: 0.712
    true_std: 0.003
    value_gap_source_arxiv: '2103.09430'
    value_gap_source_title: 'OGB-LSC: A Large-Scale Challenge for Machine Learning
      on Graphs'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.712
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
  - *id003
single_proposed_model: ML
---

