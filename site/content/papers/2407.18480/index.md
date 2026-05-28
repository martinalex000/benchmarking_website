---
title: Scalable Graph Compressed Convolutions
arxiv_id: '2407.18480'
source_url: ''
authors: []
published_date: Jul 2024
published_date_iso: 2024-07
abstract: Designing effective graph neural networks (GNNs) with message passing has two fundamental challenges,
  i.e., determining optimal message-passing pathways and designing local aggregators. Previous methods
  of designing optimal pathways are limited with information loss on the input features. On the other
  hand, existing local aggregators generally fail to extract multi-scale features and approximate diverse
  operators under limited parameter scales. In contrast to these methods, Euclidean convolution has been
  proven as an expressive aggregator, making it a perfect candidate for GNN construction. However, the
  challenges of generalizing Euclidean convolution to graphs arise from the irregular structure of graphs.
  To bridge the gap between Euclidean space and graph topology, we propose a differentiable method that
  applies permutations to calibrate input graphs for Euclidean convolution. The permutations constrain
  all nodes in a row regardless of their input order and therefore enable the flexible generalization
  of Euclidean convolution to graphs. Based on the graph calibration, we propose the Compressed Convolution
  Network (CoCN) for hierarchical graph representation learning. CoCN follows local feature-learning and
  global parameter-sharing mechanisms of convolution neural networks. The whole model can be trained end-to-end,
  with compressed convolution applied to learn individual node features and their corresponding structure
  features. CoCN can further borrow successful practices from Euclidean convolution, including residual
  connection and inception mechanism. We validate CoCN on both node-level and graph-level benchmarks.
  CoCN achieves superior performance over competitive GNN baselines. Codes are available at https://github.com/sunjss/CoCN.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CoCN vanilla
- CoCN expanded
- CoCN exp.
- Sp. CoCN
- Seg. CoCN
mrr: 0.0942
adjusted_mrr: 0.0942
mrr_dataset_count: 12
benchmark_categories:
- Heterophilic Graphs
- LRGB
- TU Dortmund
task_categories:
- graph_classification
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id007
  dataset: Actor
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.4298
    std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4298
    sort_std: 0.0148
    is_best: true
  - model: GrokFilter
    model_key: grokfilter
    model_plain: GrokFilter
    value: 0.4215
    std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4215
    sort_std: 0.0129
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.4193
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: '2024-11-26'
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4193
    sort_std: 0.0104
    is_best: true
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3222
    std: 0.0234
    paper_value: 0.3222
    paper_std: 0.0234
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abu-El-Haija 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 17
    true_value: 0.3776
    true_std: 0.01
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055400000000000005
    value_note: ''
    paper_rank: 68
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.3776
    sort_std: 0.01
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.3411
    std: 0.0109
    paper_value: 0.3411
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 19
    true_value: 0.3761
    true_std: 0.0089
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.034999999999999976
    value_note: ''
    paper_rank: 56
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.3761
    sort_std: 0.0089
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.3754
    std: 0.0156
    paper_value: 0.3754
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yan 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 20
    true_value: 0.3754
    true_std: 0.0156
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3754
    sort_std: 0.0156
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3744
    std: 0.013
    paper_value: 0.3744
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 21
    true_value: 0.3744
    true_std: 0.013
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3744
    sort_std: 0.013
    is_best: false
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.3662
    std: 0.0085
    paper_value: 0.3662
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 31
    true_value: 0.3662
    true_std: 0.0085
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3662
    sort_std: 0.0085
    is_best: false
  - model: AERO-GNN
    model_key: aero-gnn
    model_plain: AERO-GNN
    value: 0.3657
    std: 0.011
    paper_value: 0.3657
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 32
    true_value: 0.3657
    true_std: 0.011
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3657
    sort_std: 0.011
    is_best: false
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.3643
    std: 0.012
    paper_value: 0.3643
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luan 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 34
    true_value: 0.3643
    true_std: 0.012
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3643
    sort_std: 0.012
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.3635
    std: 0.0012
    paper_value: 0.3635
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 35
    true_value: 0.3635
    true_std: 0.0012
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3635
    sort_std: 0.0012
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.361
    std: 0.0155
    paper_value: 0.361
    paper_std: 0.0155
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lim 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 37
    true_value: 0.361
    true_std: 0.0155
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.361
    sort_std: 0.0155
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.3002
    std: 0.0089
    paper_value: 0.3002
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 42
    true_value: 0.3532
    true_std: 0.0053
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05299999999999999
    value_note: ''
    paper_rank: 80
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.3532
    sort_std: 0.0053
    is_best: false
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.3516
    std: 0.009
    paper_value: 0.3516
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 43
    true_value: 0.3516
    true_std: 0.009
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3516
    sort_std: 0.009
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3507
    std: 0.0015
    paper_value: 0.3507
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 45
    true_value: 0.3507
    true_std: 0.0015
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3507
    sort_std: 0.0015
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.3482
    std: 0.0135
    paper_value: 0.3482
    paper_std: 0.0135
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bo 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 47
    true_value: 0.3482
    true_std: 0.0135
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3482
    sort_std: 0.0135
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3026
    std: 0.0079
    paper_value: 0.3026
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 66
    true_value: 0.3323
    true_std: 0.0116
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029700000000000004
    value_note: ''
    paper_rank: 78
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.3323
    sort_std: 0.0116
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.3159
    std: 0.0115
    paper_value: 0.3159
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 72
    true_value: 0.31629999999999997
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00039999999999995595
    value_note: global 0.3163 within std
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31629999999999997
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Amazon-ratings
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.5592
    std: 0.0043
    metric: Accuracy
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
    global_rank: 1
    sort_value: 0.5592
    sort_std: 0.0043
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4909
    std: 0.0063
    paper_value: 0.4909
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0645
    value_note: ''
    paper_rank: 53
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.5554
    sort_std: 0.0051
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.554
    sort_std: 0.0021
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.5496
    std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
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
    global_rank: 4
    sort_value: 0.5496
    sort_std: 0.0222
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.487
    std: 0.0063
    paper_value: 0.487
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 17
    true_value: 0.538
    true_std: 0.0
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.051000000000000045
    value_note: ''
    paper_rank: 58
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.538
    sort_std: 0.0
    is_best: false
  - model: Sp. CoCN
    model_key: sp. cocn
    model_plain: Sp. CoCN
    value: 0.5074
    std: 0.0015
    paper_value: 0.5074
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 47
    true_value: 0.5074
    true_std: 0.0015
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5074
    sort_std: 0.0015
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.5066
    std: 0.0048
    paper_value: 0.5066
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Wu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 49
    true_value: 0.5066
    true_std: 0.0048
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5066
    sort_std: 0.0048
    is_best: false
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.4488
    std: 0.0034
    paper_value: 0.4488
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Chien et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 78
    true_value: 0.4488
    true_std: 0.0034
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4488
    sort_std: 0.0034
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4412
    std: 0.003
    paper_value: 0.4412
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Bo et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 81
    true_value: 0.4412
    true_std: 0.003
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4412
    sort_std: 0.003
    is_best: false
  - model: Seg. CoCN
    model_key: seg. cocn
    model_plain: Seg. CoCN
    value: 0.4306
    std: 0.0021
    paper_value: 0.4306
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 84
    true_value: 0.4306
    true_std: 0.0021
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4306
    sort_std: 0.0021
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.3689
    std: 0.0014
    paper_value: 0.3689
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Li et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 93
    true_value: 0.3689
    true_std: 0.0014
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3689
    sort_std: 0.0014
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.3647
    std: 0.0023
    paper_value: 0.3647
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (left)
    source_ref: Zhu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 94
    true_value: 0.3647
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3647
    sort_std: 0.0023
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id014
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
    paper_value: 0.8722
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 1
    true_value: 0.8722
    true_std: 0.0013
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8615
    std: 0.001
    paper_value: 0.8615
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 4
    true_value: 0.8615
    true_std: 0.001
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8615
    sort_std: 0.001
    is_best: false
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
    value: 0.8059
    std: 0.0027
    paper_value: 0.8059
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 5
    true_value: 0.827
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021100000000000008
    value_note: ''
    paper_rank: 13
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.009
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.8213
    std: 0.0043
    paper_value: 0.8213
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 6
    true_value: 0.8213
    true_std: 0.0043
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8213
    sort_std: 0.0043
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.821
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.02379'
    title: 'No Metric to Rule Them All: Toward Principled Evaluations of Graph-Learning
      Datasets'
    date: '2025-02-04'
    date_display: Feb 2025
    date_iso: '2025-02-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.821
    sort_std: 0.009
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.8128
    std: 0.0015
    paper_value: 0.8128
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 9
    true_value: 0.8128
    true_std: 0.0015
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8128
    sort_std: 0.0015
    is_best: false
  - model: PG-GNN
    model_key: pg-gnn
    model_plain: PG-GNN
    value: 0.809
    std: 0.008
    paper_value: 0.809
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 11
    true_value: 0.809
    true_std: 0.008
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.809
    sort_std: 0.008
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.8074
    std: 0.0054
    paper_value: 0.8074
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 12
    true_value: 0.8074
    true_std: 0.0054
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8074
    sort_std: 0.0054
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7819
    std: 0.0063
    paper_value: 0.7819
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 14
    true_value: 0.8059
    true_std: 0.0027
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02399999999999991
    value_note: ''
    paper_rank: 20
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8059
    sort_std: 0.0027
    is_best: false
  - model: ASAP
    model_key: asap
    model_plain: ASAP
    value: 0.7864
    std: 0.005
    paper_value: 0.7864
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ranjan et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 18
    true_value: 0.7864
    true_std: 0.005
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7864
    sort_std: 0.005
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7803
    std: 0.0031
    paper_value: 0.7803
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 22
    true_value: 0.7803
    true_std: 0.0031
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7803
    sort_std: 0.0031
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7758
    std: 0.0085
    paper_value: 0.7758
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 24
    true_value: 0.7758
    true_std: 0.0085
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7758
    sort_std: 0.0085
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.739
    std: 0.017
    paper_value: 0.739
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 46
    true_value: 0.739
    true_std: 0.017
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.739
    sort_std: 0.017
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.726
    std: 0.0215
    paper_value: 0.726
    paper_std: 0.0215
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 57
    true_value: 0.726
    true_std: 0.0215
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.0215
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Chameleon
  rows:
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8051
    sort_std: 0.0125
    is_best: true
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8017
    sort_std: 0.0188
    is_best: true
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8002
    sort_std: 0.0087
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7935
    std: 0.0142
    paper_value: 0.7935
    paper_std: 0.0142
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 5
    true_value: 0.7935
    true_std: 0.0142
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7935
    sort_std: 0.0142
    is_best: true
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.7917
    std: 0.0017
    paper_value: 0.7917
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 6
    true_value: 0.7917
    true_std: 0.0017
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7917
    sort_std: 0.0017
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7785
    std: null
    paper_value: 0.7785
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 8
    true_value: 0.7827
    true_std: 0.0128
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0041999999999999815
    value_note: global 0.7827 within std
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7827
    sort_std: 0.0128
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.6846
    std: 0.017
    paper_value: 0.6846
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 9
    true_value: 0.7593
    true_std: 0.0171
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07469999999999999
    value_note: ''
    paper_rank: 29
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.7593
    sort_std: 0.0171
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.6833
    std: null
    paper_value: 0.6833
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 18
    true_value: 0.742
    true_std: 0.0103
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.058699999999999974
    value_note: ''
    paper_rank: 30
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.0103
    is_best: false
  - model: AERO-GNN
    model_key: aero-gnn
    model_plain: AERO-GNN
    value: 0.7158
    std: 0.024
    paper_value: 0.7158
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 21
    true_value: 0.7158
    true_std: 0.024
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7158
    sort_std: 0.024
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.7004
    std: null
    paper_value: 0.7004
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 23
    true_value: 0.7121
    true_std: 0.0184
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011699999999999933
    value_note: global 0.7121 within std
    paper_rank: 26
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7121
    sort_std: 0.0184
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.7114
    std: 0.0184
    paper_value: 0.7114
    paper_std: 0.0184
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 24
    true_value: 0.7114
    true_std: 0.0184
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7114
    sort_std: 0.0184
    is_best: false
  - model: ResNet+adj
    model_key: resnet+adj
    model_plain: ResNet+adj
    value: 0.7107
    std: null
    paper_value: 0.7107
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 25
    true_value: 0.7107
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7107
    sort_std: null
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.6842
    std: 0.0138
    paper_value: 0.6842
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 30
    true_value: 0.6842
    true_std: 0.0138
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6842
    sort_std: 0.0138
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.4726
    std: null
    paper_value: 0.4726
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 36
    true_value: 0.6748
    true_std: 0.004
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20219999999999994
    value_note: ''
    paper_rank: 106
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.6748
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5982
    std: 0.0258
    paper_value: 0.5982
    paper_std: 0.0258
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.050000000000000044
    value_note: ''
    paper_rank: 70
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4502
    std: null
    paper_value: 0.4502
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18880000000000002
    value_note: ''
    paper_rank: 117
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.6386
    std: 0.0304
    paper_value: 0.6386
    paper_std: 0.0304
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 51
    true_value: 0.6386
    true_std: 0.0304
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6386
    sort_std: 0.0304
    is_best: false
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.6259
    std: 0.0204
    paper_value: 0.6259
    paper_std: 0.0204
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 57
    true_value: 0.6259
    true_std: 0.0204
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6259
    sort_std: 0.0204
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4906
    std: 0.0188
    paper_value: 0.4906
    paper_std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 60
    true_value: 0.6215
    true_std: 0.0042
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13090000000000007
    value_note: ''
    paper_rank: 103
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.6215
    sort_std: 0.0042
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.4627
    std: null
    paper_value: 0.4627
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 64
    true_value: 0.612
    true_std: 0.0428
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1493
    value_note: ''
    paper_rank: 111
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.612
    sort_std: 0.0428
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6
    std: 0.0281
    paper_value: 0.6
    paper_std: 0.0281
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 65
    true_value: 0.609
    true_std: null
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009000000000000008
    value_note: global 0.6090 within std
    paper_rank: 70
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.609
    sort_std: null
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.605
    std: 0.0253
    paper_value: 0.605
    paper_std: 0.0253
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 67
    true_value: 0.605
    true_std: 0.0253
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.605
    sort_std: 0.0253
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.5524
    std: 0.0276
    paper_value: 0.5524
    paper_std: 0.0276
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 75
    true_value: 0.5928
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04039999999999999
    value_note: ''
    paper_rank: 85
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.5928
    sort_std: 0.0125
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.4044
    std: 0.0202
    paper_value: 0.4044
    paper_std: 0.0202
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 96
    true_value: 0.5191
    true_std: 0.0056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11470000000000002
    value_note: ''
    paper_rank: 124
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.5191
    sort_std: 0.0056
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.5136
    std: null
    paper_value: 0.5136
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 98
    true_value: 0.5136
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5136
    sort_std: null
    is_best: false
  - model: ResNet+SGC
    model_key: resnet+sgc
    model_plain: ResNet+SGC
    value: 0.4993
    std: null
    paper_value: 0.4993
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 100
    true_value: 0.4993
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4993
    sort_std: null
    is_best: false
  - model: ResNet
    model_key: resnet
    model_plain: ResNet
    value: 0.4952
    std: null
    paper_value: 0.4952
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 101
    true_value: 0.4952
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4952
    sort_std: null
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.4607
    std: 0.0211
    paper_value: 0.4607
    paper_std: 0.0211
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 102
    true_value: 0.4947
    true_std: 0.0284
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.033999999999999975
    value_note: ''
    paper_rank: 111
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.4947
    sort_std: 0.0284
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.8595
    std: 0.0564
    paper_value: 0.8595
    paper_std: 0.0564
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luan 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 6
    true_value: 0.9262
    true_std: 0.0257
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06669999999999998
    value_note: ''
    paper_rank: 19
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.9262
    sort_std: 0.0257
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.5676
    std: 0.0458
    paper_value: 0.5676
    paper_std: 0.0458
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2018
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 8
    true_value: 0.918
    true_std: 0.0063
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.35040000000000004
    value_note: ''
    paper_rank: 112
    rank_delta: 104
    rank_delta_abs: 104
    rank_delta_direction: worse
    sort_value: 0.918
    sort_std: 0.0063
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.7786
    std: 0.0379
    paper_value: 0.7786
    paper_std: 0.0379
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2020
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 13
    true_value: 0.9049
    true_std: 0.0445
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12630000000000008
    value_note: ''
    paper_rank: 32
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9049
    sort_std: 0.0445
    is_best: true
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7676
    std: 0.0587
    paper_value: 0.7676
    paper_std: 0.0587
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bo 2021
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 15
    true_value: 0.8803
    true_std: 0.056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11270000000000002
    value_note: ''
    paper_rank: 33
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.8803
    sort_std: 0.056
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8622
    std: 0.0049
    paper_value: 0.8622
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 19
    true_value: 0.8622
    true_std: 0.0049
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8622
    sort_std: 0.0049
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8568
    std: 0.0663
    paper_value: 0.8568
    paper_std: 0.0663
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yan 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 20
    true_value: 0.8568000000000001
    true_std: 0.0663
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8568000000000001
    sort_std: 0.0663
    is_best: false
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8339
    std: 0.0165
    paper_value: 0.8339
    paper_std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 25
    true_value: 0.8339
    true_std: 0.0165
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8339
    sort_std: 0.0165
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5703
    std: 0.0467
    paper_value: 0.5703
    paper_std: 0.0467
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25429999999999997
    value_note: ''
    paper_rank: 110
    rank_delta: 83
    rank_delta_abs: 83
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: AERO-GNN
    model_key: aero-gnn
    model_plain: AERO-GNN
    value: 0.8124
    std: 0.068
    paper_value: 0.8124
    paper_std: 0.068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee 2023
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 29
    true_value: 0.8124
    true_std: 0.068
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8124
    sort_std: 0.068
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8008
    std: 0.0296
    paper_value: 0.8008
    paper_std: 0.0296
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton 2017
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 30
    true_value: 0.8008
    true_std: 0.0296
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8008
    sort_std: 0.0296
    is_best: false
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.7811
    std: 0.0655
    paper_value: 0.7811
    paper_std: 0.0655
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 32
    true_value: 0.7811
    true_std: 0.0655
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7811
    sort_std: 0.0655
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.7784
    std: 0.0581
    paper_value: 0.7784
    paper_std: 0.0581
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lim 2021
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 33
    true_value: 0.7784
    true_std: 0.0581
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7784
    sort_std: 0.0581
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.743
    std: 0.0746
    paper_value: 0.743
    paper_std: 0.0746
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Defferrard 2016
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 43
    true_value: 0.743
    true_std: 0.0746
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.743
    sort_std: 0.0746
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7351
    std: 0.0634
    paper_value: 0.7351
    paper_std: 0.0634
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abu-El-Haija 2019
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 45
    true_value: 0.7351000000000001
    true_std: 0.0634
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7351000000000001
    sort_std: 0.0634
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6054
    std: 0.0367
    paper_value: 0.6054
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei 2020
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 99
    true_value: 0.6081
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0026999999999999247
    value_note: global 0.6081 within std
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6081
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
  - model: CoCN exp.
    model_key: cocn exp.
    model_plain: CoCN exp.
    value: 0.838
    std: null
    paper_value: 0.838
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 16
    true_value: 0.838
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.838
    sort_std: null
    is_best: false
  - model: k-GNN
    model_key: k-gnn
    model_plain: k-GNN
    value: 0.8213
    std: null
    paper_value: 0.8213
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: morris 2019
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 23
    true_value: 0.8213
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8213
    sort_std: null
    is_best: false
  - model: ResGCN
    model_key: resgcn
    model_plain: ResGCN
    value: 0.7833
    std: null
    paper_value: 0.7833
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: li 2019
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 31
    true_value: 0.7833
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7833
    sort_std: null
    is_best: false
  - model: CNN
    model_key: cnn
    model_plain: CNN
    value: 0.7639
    std: null
    paper_value: 0.7639
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: said 2023
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 34
    true_value: 0.7639
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7639
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.762
    std: null
    paper_value: 0.762
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: velickovic 2018
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 35
    true_value: 0.762
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7556
    std: null
    paper_value: 0.7556
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu 2019
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 38
    true_value: 0.7556
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7556
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7546
    std: null
    paper_value: 0.7546
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: kipf 2017
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 39
    true_value: 0.7546
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7546
    sort_std: null
    is_best: false
  - model: rf
    model_key: rf
    model_plain: rf
    value: 0.699
    std: null
    paper_value: 0.699
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: said 2023
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 44
    true_value: 0.699
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.699
    sort_std: null
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.5907
    std: null
    paper_value: 0.5907
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: defferrard 2016
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 64
    true_value: 0.5907
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5907
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
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
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7794
    std: 0.0033
    paper_value: 0.7794
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 6
    true_value: 0.7794
    true_std: 0.0033
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7794
    sort_std: 0.0033
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.7726
    std: 0.0027
    paper_value: 0.7726
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 11
    true_value: 0.7726
    true_std: 0.0027
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7726
    sort_std: 0.0027
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7326
    std: 0.0046
    paper_value: 0.7326
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 12
    true_value: 0.769
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03639999999999999
    value_note: ''
    paper_rank: 44
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: null
    is_best: false
  - model: PG-GNN
    model_key: pg-gnn
    model_plain: PG-GNN
    value: 0.768
    std: 0.026
    paper_value: 0.768
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 14
    true_value: 0.768
    true_std: 0.026
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.026
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7278
    std: 0.0086
    paper_value: 0.7278
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0232
    value_note: global 0.7510 within std
    paper_rank: 53
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7412
    std: 0.0056
    paper_value: 0.7412
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 31
    true_value: 0.7412
    true_std: 0.0056
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7412
    sort_std: 0.0056
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7348
    std: 0.0076
    paper_value: 0.7348
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 43
    true_value: 0.7348
    true_std: 0.0076
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7348
    sort_std: 0.0076
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7314
    std: 0.007
    paper_value: 0.7314
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 46
    true_value: 0.7314
    true_std: 0.007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7314
    sort_std: 0.007
    is_best: false
  - model: ASAP
    model_key: asap
    model_plain: ASAP
    value: 0.7281
    std: 0.005
    paper_value: 0.7281
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ranjan et al. 2020
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 53
    true_value: 0.7281
    true_std: 0.005
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7281
    sort_std: 0.005
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.726
    std: 0.033
    paper_value: 0.726
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 54
    true_value: 0.726
    true_std: 0.033
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.726
    sort_std: 0.033
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7255
    std: 0.0128
    paper_value: 0.7255
    paper_std: 0.0128
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al. 2019
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 57
    true_value: 0.7255
    true_std: 0.0128
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7255
    sort_std: 0.0128
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7158
    std: 0.0095
    paper_value: 0.7158
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al. 2019
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 74
    true_value: 0.7158
    true_std: 0.0095
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7158
    sort_std: 0.0095
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.71
    std: 0.0229
    paper_value: 0.71
    paper_std: 0.0229
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al. 2016
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 84
    true_value: 0.71
    true_std: 0.0229
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.0229
    is_best: false
  - model: PathNet
    model_key: pathnet
    model_plain: PathNet
    value: 0.704
    std: 0.038
    paper_value: 0.704
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Michel et al. 2023
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 94
    true_value: 0.704
    true_std: 0.038
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 94
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.704
    sort_std: 0.038
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.688
    std: 0.045
    paper_value: 0.688
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 106
    true_value: 0.688
    true_std: 0.045
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.688
    sort_std: 0.045
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: IMDB-MULTI
  rows:
  - model: KMIS
    model_key: kmis
    model_plain: KMIS
    value: 0.63
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.63
    sort_std: 0.02
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.62
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.62
    sort_std: 0.03
    is_best: true
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.5153
    std: 0.0065
    paper_value: 0.5153
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 3
    true_value: 0.61
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0947
    value_note: ''
    paper_rank: 24
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: Eigen
    model_key: eigen
    model_plain: Eigen
    value: 0.61
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.09821'
    title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    date: Jan 2025
    date_display: Jan 2025
    date_iso: 2025-01
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.5673
    std: 0.0036
    paper_value: 0.5673
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 7
    true_value: 0.5673
    true_std: 0.0036
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5673
    sort_std: 0.0036
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.5632
    std: 0.0018
    paper_value: 0.5632
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 9
    true_value: 0.5632
    true_std: 0.0018
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5632
    sort_std: 0.0018
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.5131
    std: 0.0072
    paper_value: 0.5131
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 10
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04690000000000005
    value_note: ''
    paper_rank: 24
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: PG-GNN
    model_key: pg-gnn
    model_plain: PG-GNN
    value: 0.532
    std: 0.036
    paper_value: 0.532
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 15
    true_value: 0.532
    true_std: 0.036
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.532
    sort_std: 0.036
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5039
    std: 0.0041
    paper_value: 0.5039
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 21
    true_value: 0.523
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019100000000000006
    value_note: ''
    paper_rank: 35
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.4813
    std: 0.0136
    paper_value: 0.4813
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 22
    true_value: 0.523
    true_std: 0.028
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.041700000000000015
    value_note: ''
    paper_rank: 63
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: 0.028
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.508
    std: 0.045
    paper_value: 0.508
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 29
    true_value: 0.508
    true_std: 0.045
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.508
    sort_std: 0.045
    is_best: false
  - model: ASAP
    model_key: asap
    model_plain: ASAP
    value: 0.5078
    std: 0.0075
    paper_value: 0.5078
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ranjan et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 31
    true_value: 0.5078
    true_std: 0.0075
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5078
    sort_std: 0.0075
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.5066
    std: 0.0082
    paper_value: 0.5066
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 34
    true_value: 0.5066
    true_std: 0.0082
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5066
    sort_std: 0.0082
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.5023
    std: 0.0044
    paper_value: 0.5023
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 37
    true_value: 0.5023
    true_std: 0.0044
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5023
    sort_std: 0.0044
    is_best: false
  - model: PathNet
    model_key: pathnet
    model_plain: PathNet
    value: 0.491
    std: 0.036
    paper_value: 0.491
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Michel et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 48
    true_value: 0.491
    true_std: 0.036
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.036
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.4859
    std: 0.0072
    paper_value: 0.4859
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 59
    true_value: 0.4859
    true_std: 0.0072
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4859
    sort_std: 0.0072
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.476
    std: 0.035
    paper_value: 0.476
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 67
    true_value: 0.476
    true_std: 0.035
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: 0.035
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.4523
    std: 0.0284
    paper_value: 0.4523
    paper_std: 0.0284
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 71
    true_value: 0.4523
    true_std: 0.0284
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4523
    sort_std: 0.0284
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.695
    std: 0.0178
    paper_value: 0.695
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 22
    true_value: 0.901
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20600000000000007
    value_note: ''
    paper_rank: 160
    rank_delta: 138
    rank_delta_abs: 138
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: null
    is_best: false
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8989
    std: 0.0039
    paper_value: 0.8989
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 24
    true_value: 0.8989
    true_std: 0.0039
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8989
    sort_std: 0.0039
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8139
    std: 0.0153
    paper_value: 0.8139
    paper_std: 0.0153
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08010000000000006
    value_note: ''
    paper_rank: 92
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.8895
    std: 0.0421
    paper_value: 0.8895
    paper_std: 0.0421
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 34
    true_value: 0.8895
    true_std: 0.0421
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8895
    sort_std: 0.0421
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.836
    std: 0.096
    paper_value: 0.836
    paper_std: 0.096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 35
    true_value: 0.889
    true_std: 0.015
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.05300000000000005
    value_note: global 0.8890 within std
    paper_rank: 73
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.889
    sort_std: 0.015
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8708
    std: 0.0017
    paper_value: 0.8708
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 48
    true_value: 0.8708
    true_std: 0.0017
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8708
    sort_std: 0.0017
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.8556
    std: 0.0109
    paper_value: 0.8556
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 61
    true_value: 0.8556
    true_std: 0.0109
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8556
    sort_std: 0.0109
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.8344
    std: 0.0133
    paper_value: 0.8344
    paper_std: 0.0133
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 74
    true_value: 0.8344
    true_std: 0.0133
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8344
    sort_std: 0.0133
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7922
    std: 0.0102
    paper_value: 0.7922
    paper_std: 0.0102
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 95
    true_value: 0.81
    true_std: 0.11
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.017800000000000038
    value_note: global 0.8100 within std
    paper_rank: 110
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.81
    sort_std: 0.11
    is_best: false
  - model: ASAP
    model_key: asap
    model_plain: ASAP
    value: 0.7783
    std: 0.0149
    paper_value: 0.7783
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ranjan et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 122
    true_value: 0.7783
    true_std: 0.0149
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7783
    sort_std: 0.0149
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7367
    std: 0.0428
    paper_value: 0.7367
    paper_std: 0.0428
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 143
    true_value: 0.7367
    true_std: 0.0428
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 143
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7367
    sort_std: 0.0428
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.6761
    std: 0.0336
    paper_value: 0.6761
    paper_std: 0.0336
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 165
    true_value: 0.6761
    true_std: 0.0336
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6761
    sort_std: 0.0336
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: NCI1
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.865
    std: 0.014
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
    sort_value: 0.865
    sort_std: 0.014
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.86
    std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.19117'
    title: 'Range-aware Positional Encoding via High-order Pretraining: Theory and
      Practice'
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.86
    sort_std: 0.018
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8583
    std: 0.0086
    paper_value: 0.8583
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 3
    true_value: 0.8583
    true_std: 0.0086
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8583
    sort_std: 0.0086
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.846
    std: 0.012
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
    global_rank: 4
    sort_value: 0.846
    sort_std: 0.012
    is_best: true
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8289
    std: 0.0019
    paper_value: 0.8289
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 14
    true_value: 0.8289
    true_std: 0.0019
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8289
    sort_std: 0.0019
    is_best: false
  - model: PG-GNN
    model_key: pg-gnn
    model_plain: PG-GNN
    value: 0.828
    std: 0.013
    paper_value: 0.828
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 16
    true_value: 0.828
    true_std: 0.013
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.828
    sort_std: 0.013
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8
    std: 0.014
    paper_value: 0.8
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 18
    true_value: 0.827
    true_std: 0.017
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026999999999999913
    value_note: ''
    paper_rank: 33
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.017
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.823
    std: 0.019
    paper_value: 0.823
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 21
    true_value: 0.823
    true_std: 0.019
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.823
    sort_std: 0.019
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7629
    std: 0.0179
    paper_value: 0.7629
    paper_std: 0.0179
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 33
    true_value: 0.802
    true_std: 0.02
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.039100000000000024
    value_note: ''
    paper_rank: 63
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.802
    sort_std: 0.02
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7935
    std: 0.0033
    paper_value: 0.7935
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 38
    true_value: 0.7935
    true_std: 0.0033
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7935
    sort_std: 0.0033
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.786
    std: 0.019
    paper_value: 0.786
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 41
    true_value: 0.786
    true_std: 0.019
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.786
    sort_std: 0.019
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.76
    std: 0.018
    paper_value: 0.76
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 47
    true_value: 0.777
    true_std: 0.015
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.017000000000000015
    value_note: global 0.7770 within std
    paper_rank: 65
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.777
    sort_std: 0.015
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.6232
    std: 0.019
    paper_value: 0.6232
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 55
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14580000000000004
    value_note: ''
    paper_rank: 87
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7635
    std: 0.0262
    paper_value: 0.7635
    paper_std: 0.0262
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 63
    true_value: 0.7635
    true_std: 0.0262
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7635
    sort_std: 0.0262
    is_best: false
  - model: ASAP
    model_key: asap
    model_plain: ASAP
    value: 0.7148
    std: 0.0042
    paper_value: 0.7148
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ranjan et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 77
    true_value: 0.7148
    true_std: 0.0042
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7148
    sort_std: 0.0042
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.6745
    std: 0.0111
    paper_value: 0.6745
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 82
    true_value: 0.6745
    true_std: 0.0111
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6745
    sort_std: 0.0111
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.6702
    std: 0.0225
    paper_value: 0.6702
    paper_std: 0.0225
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 83
    true_value: 0.6702
    true_std: 0.0225
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6702
    sort_std: 0.0225
    is_best: false
  - model: PathNet
    model_key: pathnet
    model_plain: PathNet
    value: 0.641
    std: 0.023
    paper_value: 0.641
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Michel et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 85
    true_value: 0.641
    true_std: 0.023
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.641
    sort_std: 0.023
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: PCQM-Contact
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.6143
    std: null
    metric: MRR
    higher_is_better: true
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
    sort_value: 0.6143
    sort_std: null
    is_best: true
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.5341
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.5341
    sort_std: null
    is_best: false
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.4707
    std: 0.0007
    metric: MRR
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
    global_rank: 3
    sort_value: 0.4707
    sort_std: 0.0007
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3218
    std: 0.0011
    paper_value: 0.3218
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 5
    true_value: 0.467
    true_std: 0.0004
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14520000000000005
    value_note: ''
    paper_rank: 61
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.467
    sort_std: 0.0004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3234
    std: 0.0006
    paper_value: 0.3234
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 7
    true_value: 0.4526
    true_std: 0.0006
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12919999999999998
    value_note: ''
    paper_rank: 60
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.4526
    sort_std: 0.0006
    is_best: false
  - model: CoCN exp.
    model_key: cocn exp.
    model_plain: CoCN exp.
    value: 0.3713
    std: 0.0037
    paper_value: 0.3713
    paper_std: 0.0037
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 8
    true_value: 0.3713
    true_std: 0.0037
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3713
    sort_std: 0.0037
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.318
    std: 0.0027
    paper_value: 0.318
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 17
    true_value: 0.3509
    true_std: 0.0006
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.032899999999999985
    value_note: ''
    paper_rank: 61
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.3509
    sort_std: 0.0006
    is_best: false
  - model: Cache-GNN+RWSE
    model_key: cache-gnn+rwse
    model_plain: Cache-GNN+RWSE
    value: 0.3488
    std: 0.0008
    paper_value: 0.3488
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ma et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 19
    true_value: 0.3488
    true_std: 0.0008
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3488
    sort_std: 0.0008
    is_best: false
  - model: Drew-GIN
    model_key: drew-gin
    model_plain: Drew-GIN
    value: 0.3444
    std: 0.0017
    paper_value: 0.3444
    paper_std: 0.0017
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gutteridge et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 25
    true_value: 0.3444
    true_std: 0.0017
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3444
    sort_std: 0.0017
    is_best: false
  - model: Graph Diffuser
    model_key: graph diffuser
    model_plain: Graph Diffuser
    value: 0.3388
    std: 0.0011
    paper_value: 0.3388
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Glickman et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 42
    true_value: 0.3388
    true_std: 0.0011
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3388
    sort_std: 0.0011
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3161
    std: 0.0004
    paper_value: 0.3161
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 64
    true_value: 0.3161
    true_std: 0.0004
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3161
    sort_std: 0.0004
    is_best: false
  metric: MRR
  higher_is_better: true
- &id009
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
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7948
    std: 0.0051
    paper_value: 0.7948
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 6
    true_value: 0.7948
    true_std: 0.0051
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7948
    sort_std: 0.0051
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.7686
    std: 0.0013
    paper_value: 0.7686
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 19
    true_value: 0.7686
    true_std: 0.0013
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7686
    sort_std: 0.0013
    is_best: false
  - model: PG-GNN
    model_key: pg-gnn
    model_plain: PG-GNN
    value: 0.768
    std: 0.038
    paper_value: 0.768
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 21
    true_value: 0.768
    true_std: 0.038
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.038
    is_best: false
  - model: SEP
    model_key: sep
    model_plain: SEP
    value: 0.7642
    std: 0.0039
    paper_value: 0.7642
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 25
    true_value: 0.7642
    true_std: 0.0039
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7642
    sort_std: 0.0039
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.7625
    std: 0.01
    paper_value: 0.7625
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 31
    true_value: 0.7625
    true_std: 0.01
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7625
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7146
    std: 0.0166
    paper_value: 0.7146
    paper_std: 0.0166
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0474
    value_note: ''
    paper_rank: 157
    rank_delta: 125
    rank_delta_abs: 125
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7324
    std: 0.0073
    paper_value: 0.7324
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 38
    true_value: 0.76
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.027599999999999958
    value_note: global 0.7600 within std
    paper_rank: 110
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.73
    std: 0.045
    paper_value: 0.73
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hamilton et al. 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 43
    true_value: 0.759
    true_std: 0.032
    value_gap_source_arxiv: '2406.06984'
    value_gap_source_title: On the Stability of Multiset and Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.029000000000000026
    value_note: global 0.7590 within std
    paper_rank: 117
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.759
    sort_std: 0.032
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.752
    std: 0.039
    paper_value: 0.752
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Sun et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 56
    true_value: 0.752
    true_std: 0.039
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.752
    sort_std: 0.039
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7509
    std: 0.0059
    paper_value: 0.7509
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 66
    true_value: 0.7509
    true_std: 0.0059
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7509
    sort_std: 0.0059
    is_best: false
  - model: PATCHY-SAN
    model_key: patchy-san
    model_plain: PATCHY-SAN
    value: 0.75
    std: 0.0251
    paper_value: 0.75
    paper_std: 0.0251
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Niepert et al. 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 73
    true_value: 0.75
    true_std: 0.0251
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.0251
    is_best: false
  - model: ASAP
    model_key: asap
    model_plain: ASAP
    value: 0.7392
    std: 0.0063
    paper_value: 0.7392
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ranjan et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 99
    true_value: 0.7392
    true_std: 0.0063
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7392
    sort_std: 0.0063
    is_best: false
  - model: SAGPool
    model_key: sagpool
    model_plain: SAGPool
    value: 0.7156
    std: 0.0149
    paper_value: 0.7156
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lee et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 155
    true_value: 0.7156
    true_std: 0.0149
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7156
    sort_std: 0.0149
    is_best: false
  - model: PathNet
    model_key: pathnet
    model_plain: PathNet
    value: 0.705
    std: 0.039
    paper_value: 0.705
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Michel et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 172
    true_value: 0.705
    true_std: 0.039
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.705
    sort_std: 0.039
    is_best: false
  - model: TopKPool
    model_key: topkpool
    model_plain: TopKPool
    value: 0.7048
    std: 0.0101
    paper_value: 0.7048
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gao et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 174
    true_value: 0.7048
    true_std: 0.0101
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7048
    sort_std: 0.0101
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Squirrel
  rows:
  - model: MRS-Dir-GCN_DA
    model_key: mrs-dir-gcn_da
    model_plain: MRS-Dir-GCN_DA
    value: 0.7601
    std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7601
    sort_std: 0.019
    is_best: true
  - model: Dir-GNN
    model_key: dir-gnn
    model_plain: Dir-GNN
    value: 0.7531
    std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    date_display: Sep 2024
    date_iso: 2024-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7531
    sort_std: 0.0192
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.6893
    std: null
    paper_value: 0.6893
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Maurya et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 3
    true_value: 0.741
    true_std: 0.0189
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05169999999999997
    value_note: ''
    paper_rank: 8
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7298
    std: 0.0178
    paper_value: 0.7298
    paper_std: 0.0178
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 4
    true_value: 0.7298
    true_std: 0.0178
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7298
    sort_std: 0.0178
    is_best: true
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.7295
    std: 0.0023
    paper_value: 0.7295
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 5
    true_value: 0.7295
    true_std: 0.0023
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7295
    sort_std: 0.0023
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7205
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.7205
    sort_std: 0.014
    is_best: false
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.518
    std: 0.015
    paper_value: 0.518
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 8
    true_value: 0.6998
    true_std: 0.0153
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18179999999999996
    value_note: ''
    paper_rank: 37
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.6998
    sort_std: 0.0153
    is_best: false
  - model: ResNet+adj
    model_key: resnet+adj
    model_plain: ResNet+adj
    value: 0.6546
    std: null
    paper_value: 0.6546
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 13
    true_value: 0.6546
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6546
    sort_std: null
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.6181
    std: 0.018
    paper_value: 0.6181
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 20
    true_value: 0.6181
    true_std: 0.018
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6181
    sort_std: 0.018
    is_best: false
  - model: AERO-GNN
    model_key: aero-gnn
    model_plain: AERO-GNN
    value: 0.6176
    std: 0.024
    paper_value: 0.6176
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 21
    true_value: 0.6176
    true_std: 0.024
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6176
    sort_std: 0.024
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.6121
    std: null
    paper_value: 0.6121
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Li et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 23
    true_value: 0.6121
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6121
    sort_std: null
    is_best: false
  - model: JacobiConv
    model_key: jacobiconv
    model_plain: JacobiConv
    value: 0.4617
    std: null
    paper_value: 0.4617
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wang et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 26
    true_value: 0.5738
    true_std: 0.0125
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11209999999999998
    value_note: ''
    paper_rank: 47
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.5738
    sort_std: 0.0125
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.5517
    std: 0.0158
    paper_value: 0.5517
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 28
    true_value: 0.5517
    true_std: 0.0158
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5517
    sort_std: 0.0158
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3689
    std: 0.0134
    paper_value: 0.3689
    paper_std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1654
    value_note: ''
    paper_rank: 95
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3339
    std: null
    paper_value: 0.3339
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Chien et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 41
    true_value: 0.5015
    true_std: 0.0192
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16759999999999997
    value_note: ''
    paper_rank: 106
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.5015
    sort_std: 0.0192
    is_best: false
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.4631
    std: 0.0246
    paper_value: 0.4631
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 46
    true_value: 0.4631
    true_std: 0.0246
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4631
    sort_std: 0.0246
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3221
    std: null
    paper_value: 0.3221
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12280000000000002
    value_note: ''
    paper_rank: 107
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.4386
    std: 0.0164
    paper_value: 0.4386
    paper_std: 0.0164
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 53
    true_value: 0.4386
    true_std: 0.0164
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4386
    sort_std: 0.0164
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.438
    std: 0.0148
    paper_value: 0.438
    paper_std: 0.0148
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 54
    true_value: 0.438
    true_std: 0.0148
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.438
    sort_std: 0.0148
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.3083
    std: 0.0069
    paper_value: 0.3083
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 67
    true_value: 0.4224
    true_std: 0.012
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11409999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.4224
    sort_std: 0.012
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3673
    std: 0.0121
    paper_value: 0.3673
    paper_std: 0.0121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 69
    true_value: 0.41609999999999997
    true_std: 0.0074
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.048799999999999955
    value_note: ''
    paper_rank: 95
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.41609999999999997
    sort_std: 0.0074
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.2945
    std: null
    paper_value: 0.2945
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Zhu et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 78
    true_value: 0.3953
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1008
    value_note: ''
    paper_rank: 109
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.3953
    sort_std: 0.0088
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.3847
    std: 0.0158
    paper_value: 0.3847
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 83
    true_value: 0.3847
    true_std: 0.0158
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3847
    sort_std: 0.0158
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.3815
    std: 0.0092
    paper_value: 0.3815
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 85
    true_value: 0.3815
    true_std: 0.0092
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3815
    sort_std: 0.0092
    is_best: false
  - model: GBK-GNN
    model_key: gbk-gnn
    model_plain: GBK-GNN
    value: 0.3706
    std: null
    paper_value: 0.3706
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Du et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 95
    true_value: 0.3706
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3706
    sort_std: null
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.292
    std: 0.0145
    paper_value: 0.292
    paper_std: 0.0145
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 101
    true_value: 0.353
    true_std: 0.019
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.061
    value_note: ''
    paper_rank: 109
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.353
    sort_std: 0.019
    is_best: false
  - model: ResNet+SGC
    model_key: resnet+sgc
    model_plain: ResNet+SGC
    value: 0.3436
    std: null
    paper_value: 0.3436
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Wu et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 105
    true_value: 0.3436
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3436
    sort_std: null
    is_best: false
  - model: ResNet
    model_key: resnet
    model_plain: ResNet
    value: 0.3388
    std: null
    paper_value: 0.3388
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 106
    true_value: 0.3388
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3388
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.8676
    std: 0.0475
    paper_value: 0.8676
    paper_std: 0.0475
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 4
    true_value: 0.9475
    true_std: 0.0291
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07989999999999997
    value_note: ''
    paper_rank: 29
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.9475
    sort_std: 0.0291
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
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.551
    std: 0.0623
    paper_value: 0.551
    paper_std: 0.0623
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 19
    true_value: 0.9118
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3608
    value_note: ''
    paper_rank: 155
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
    sort_value: 0.9118
    sort_std: 0.007
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7649
    std: 0.0287
    paper_value: 0.7649
    paper_std: 0.0287
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 24
    true_value: 0.8885
    true_std: 0.0439
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12359999999999993
    value_note: ''
    paper_rank: 82
    rank_delta: 58
    rank_delta_abs: 58
    rank_delta_direction: worse
    sort_value: 0.8885
    sort_std: 0.0439
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8039
    std: 0.0383
    paper_value: 0.8039
    paper_std: 0.0383
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 26
    true_value: 0.8852
    true_std: 0.0302
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08130000000000004
    value_note: ''
    paper_rank: 60
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.8852
    sort_std: 0.0302
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.773
    std: 0.0407
    paper_value: 0.773
    paper_std: 0.0407
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 30
    true_value: 0.8622
    true_std: 0.0245
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08919999999999995
    value_note: ''
    paper_rank: 73
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.8622
    sort_std: 0.0245
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8521
    std: 0.0049
    paper_value: 0.8521
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 33
    true_value: 0.8521
    true_std: 0.0049
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8521
    sort_std: 0.0049
    is_best: false
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.849
    std: 0.0105
    paper_value: 0.849
    paper_std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 34
    true_value: 0.849
    true_std: 0.0105
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.849
    sort_std: 0.0105
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8486
    std: 0.0455
    paper_value: 0.8486
    paper_std: 0.0455
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 35
    true_value: 0.8486
    true_std: 0.0455
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8486
    sort_std: 0.0455
    is_best: false
  - model: AERO-GNN
    model_key: aero-gnn
    model_plain: AERO-GNN
    value: 0.8435
    std: 0.052
    paper_value: 0.8435
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 38
    true_value: 0.8435
    true_std: 0.052
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8435
    sort_std: 0.052
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5946
    std: 0.0525
    paper_value: 0.5946
    paper_std: 0.0525
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 44
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23649999999999993
    value_note: ''
    paper_rank: 145
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8203
    std: 0.0277
    paper_value: 0.8203
    paper_std: 0.0277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 49
    true_value: 0.8243
    true_std: 0.061399999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0040000000000000036
    value_note: global 0.8243 within std
    paper_rank: 51
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.8243
    sort_std: 0.061399999999999996
    is_best: false
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.8135
    std: 0.0532
    paper_value: 0.8135
    paper_std: 0.0532
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 54
    true_value: 0.8135
    true_std: 0.0532
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8135
    sort_std: 0.0532
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7784
    std: 0.0773
    paper_value: 0.7784
    paper_std: 0.0773
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 67
    true_value: 0.7784
    true_std: 0.07730000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7784
    sort_std: 0.07730000000000001
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.746
    std: 0.0837
    paper_value: 0.746
    paper_std: 0.0837
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 91
    true_value: 0.746
    true_std: 0.0837
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.746
    sort_std: 0.0837
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6676
    std: 0.0272
    paper_value: 0.6676
    paper_std: 0.0272
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 116
    true_value: 0.676
    true_std: null
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008400000000000074
    value_note: global 0.6760 within std
    paper_rank: 119
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.676
    sort_std: null
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
    value: 0.5459
    std: 0.0613
    paper_value: 0.5459
    paper_std: 0.0613
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 3
    true_value: 0.901
    true_std: 0.035
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.35509999999999997
    value_note: ''
    paper_rank: 128
    rank_delta: 125
    rank_delta_abs: 125
    rank_delta_direction: worse
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.028300000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.00647'
    title: Cooperative Sheaf Neural Networks
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9
    sort_std: 0.028300000000000002
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.8745
    std: 0.0374
    paper_value: 0.8745
    paper_std: 0.0374
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 15
    true_value: 0.8745
    true_std: 0.0374
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8745
    sort_std: 0.0374
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8692
    std: 0.0141
    paper_value: 0.8692
    paper_std: 0.0141
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 17
    true_value: 0.8692
    true_std: 0.0141
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8692
    sort_std: 0.0141
    is_best: false
  - model: CoCN vanilla
    model_key: cocn vanilla
    model_plain: CoCN vanilla
    value: 0.8688
    std: 0.0045
    paper_value: 0.8688
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 18
    true_value: 0.8688
    true_std: 0.0045
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8688
    sort_std: 0.0045
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8686
    std: 0.0329
    paper_value: 0.8686
    paper_std: 0.0329
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 19
    true_value: 0.8686
    true_std: 0.0329
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8686
    sort_std: 0.0329
    is_best: true
  - model: AERO-GNN
    model_key: aero-gnn
    model_plain: AERO-GNN
    value: 0.848
    std: 0.033
    paper_value: 0.848
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 23
    true_value: 0.848
    true_std: 0.033
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.848
    sort_std: 0.033
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7961
    std: 0.0158
    paper_value: 0.7961
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 27
    true_value: 0.8294
    true_std: 0.0795
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.033299999999999996
    value_note: global 0.8294 within std
    paper_rank: 47
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.8294
    sort_std: 0.0795
    is_best: true
  - model: GPRGCN
    model_key: gprgcn
    model_plain: GPRGCN
    value: 0.8255
    std: 0.0623
    paper_value: 0.8255
    paper_std: 0.0623
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 29
    true_value: 0.8255
    true_std: 0.0623
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8255
    sort_std: 0.0623
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8136
    std: 0.0391
    paper_value: 0.8136
    paper_std: 0.0391
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 36
    true_value: 0.8136
    true_std: 0.0391
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8136
    sort_std: 0.0391
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.7757
    std: 0.034
    paper_value: 0.7757
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 39
    true_value: 0.8039000000000001
    true_std: 0.034
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.028200000000000114
    value_note: global 0.8039 within std
    paper_rank: 65
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.8039000000000001
    sort_std: 0.034
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.7941
    std: 0.0446
    paper_value: 0.7941
    paper_std: 0.0446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 44
    true_value: 0.8
    true_std: 0.0432
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005900000000000016
    value_note: global 0.8000 within std
    paper_rank: 48
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8
    sort_std: 0.0432
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.598
    std: 0.07
    paper_value: 0.598
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18830000000000002
    value_note: ''
    paper_rank: 115
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7588
    std: 0.049
    paper_value: 0.7588
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 66
    true_value: 0.7745
    true_std: 0.031
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.015699999999999936
    value_note: global 0.7745 within std
    paper_rank: 76
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7745
    sort_std: 0.031
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.7549
    std: 0.0572
    paper_value: 0.7549
    paper_std: 0.0572
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 79
    true_value: 0.7549
    true_std: 0.0572
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7549
    sort_std: 0.0572
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6451
    std: 0.0366
    paper_value: 0.6451
    paper_std: 0.0366
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 111
    true_value: 0.6451
    true_std: 0.0366
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6451
    sort_std: 0.0366
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
- benchmark: LRGB
  datasets:
  - *id008
- benchmark: TU Dortmund
  datasets:
  - *id009
  - *id010
  - *id011
  - *id012
  - *id013
  - *id014
  - *id015
main_figure: /figures/2407.18480/main_figure.png
---

