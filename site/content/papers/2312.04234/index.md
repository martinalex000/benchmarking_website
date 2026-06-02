---
title: Graph Convolutions Enrich the Self-Attention in Transformers!
arxiv_id: '2312.04234'
source_url: ''
authors: []
published_date: Dec 7, 2023
published_date_iso: '2023-12-07'
published_venue: ''
abstract: Transformers, renowned for their self-attention mechanism, have achieved
  state-of-the-art performance across various tasks in natural language processing,
  computer vision, time-series modeling, etc. However, one of the challenges with
  deep Transformer models is the oversmoothing problem, where representations across
  layers converge to indistinguishable values, leading to significant performance
  degradation. We interpret the original self-attention as a simple graph filter and
  redesign it from a graph signal processing (GSP) perspective. We propose a graph-filter-based
  self-attention (GFSA). to learn a general yet effective one, whose complexity, however,
  is slightly larger than that of the original self-attention mechanism. We demonstrate
  that GFSA improves the performance of Transformers in various fields, including
  computer vision, natural language processing, graph-level tasks, speech recognition,
  and code classification.
codebase_url: https://github.com/jeongwhanchoi/GFSA
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- GPS + GFSA
- Graph-ViT + GFSA
mrr: 0.0406
adjusted_mrr: 0.0271
mrr_dataset_count: 2
benchmark_categories:
- GNNBenchmark
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id002
  dataset: CIFAR10
  rows:
  - model: CNNs
    model_key: cnns
    model_plain: CNNs
    value: 0.93
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_display: Dec 2013
    date_iso: '2013-12-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.93
    sort_std: 0.005
    is_best: true
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.92
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_display: Dec 2013
    date_iso: '2013-12-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.92
    sort_std: 0.007
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.91
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1312.6203'
    title: Spectral Networks and Locally Connected Networks on Graphs
    date: Dec 21, 2013
    date_display: Dec 2013
    date_iso: '2013-12-21'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.91
    sort_std: 0.008
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.6967
    std: 0.004
    paper_value: 0.6967
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
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 16
    true_value: 0.73961
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.042910000000000004
    value_note: ''
    paper_rank: 35
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.73961
    sort_std: 0.0033
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.7244
    std: 0.0048
    paper_value: 0.7244
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 22
    true_value: 0.7244
    true_std: 0.0048
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7244
    sort_std: 0.0048
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.723
    std: 0.0036
    paper_value: 0.723
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 23
    true_value: 0.723
    true_std: 0.0036
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.0036
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.6987
    std: 0.0028
    paper_value: 0.6987
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 35
    true_value: 0.6987
    true_std: 0.0028
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6987
    sort_std: 0.0028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: MNIST
  rows:
  - model: Classical CNN
    model_key: classical cnn
    model_plain: Classical CNN
    value: 0.9933
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1606.09375'
    title: Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering
    date: Jun 30, 2016
    date_display: Jun 2016
    date_iso: '2016-06-30'
    codebase_url: https://github.com/mdeff/cnn_graph
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9933
    sort_std: null
    is_best: true
  - model: LeNet5
    model_key: lenet5
    model_plain: LeNet5
    value: 0.9933
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 22, 2017
    date_display: May 2017
    date_iso: '2017-05-22'
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9933
    sort_std: null
    is_best: true
  - model: CayleyNets
    model_key: cayleynets
    model_plain: CayleyNets
    value: 0.9918
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1705.07664'
    title: 'CayleyNets: Graph Convolutional Neural Networks with Complex Rational
      Spectral Filters'
    date: May 22, 2017
    date_display: May 2017
    date_iso: '2017-05-22'
    codebase_url: https://github.com/fmonti/mgcnn
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9918
    sort_std: null
    is_best: false
  - model: Graph-ViT + GFSA
    model_key: graph-vit + gfsa
    model_plain: Graph-ViT + GFSA
    value: 0.9826
    std: 0.0004
    paper_value: 0.9826
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 17
    true_value: 0.9826
    true_std: 0.0004
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9826
    sort_std: 0.0004
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.982
    std: 0.0005
    paper_value: 0.982
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 20
    true_value: 0.982
    true_std: 0.0005
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.982
    sort_std: 0.0005
    is_best: false
  - model: GPS + GFSA
    model_key: gps + gfsa
    model_plain: GPS + GFSA
    value: 0.9814
    std: 0.0014
    paper_value: 0.9814
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 28
    true_value: 0.9814
    true_std: 0.0014
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9814
    sort_std: 0.0014
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.9805
    std: 0.0013
    paper_value: 0.9805
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 7, 2023
    date_display: Dec 2023
    date_iso: '2023-12-07'
    published_venue: null
    global_rank: 35
    true_value: 0.98082
    true_std: 0.00114
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00031999999999998696
    value_note: global 0.9808 within std
    paper_rank: 36
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.98082
    sort_std: 0.00114
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
  - *id002
---

