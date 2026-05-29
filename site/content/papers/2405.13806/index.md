---
title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
arxiv_id: '2405.13806'
source_url: ''
authors: []
published_date: May 22, 2024
published_date_iso: '2024-05-22'
abstract: 'Spectral graph convolution, an important tool of data filtering on graphs,
  relies on two essential decisions: selecting spectral bases for signal transformation
  and parameterizing the kernel for frequency analysis. While recent techniques mainly
  focus on standard Fourier transform and vector-valued spectral functions, they fall
  short in flexibility to model signal distributions over large spatial ranges, and
  capacity of spectral function. In this paper, we present a novel wavelet-based graph
  convolution network, namely WaveGC, which integrates multi-resolution spectral bases
  and a matrix-valued filter kernel. Theoretically, we establish that WaveGC can effectively
  capture and decouple short-range and long-range information, providing superior
  filtering flexibility, surpassing existing graph wavelet neural networks. To instantiate
  WaveGC, we introduce a novel technique for learning general graph wavelets by separately
  combining odd and even terms of Chebyshev polynomials. This approach strictly satisfies
  wavelet admissibility criteria. Our numerical experiments showcase the consistent
  improvements in both short-range and long-range tasks. This underscores the effectiveness
  of the proposed model in handling different scenarios. Our code is available at
  https://github.com/liun-online/WaveGC.'
codebase_url: https://github.com/liun-online/WaveGC
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- SGT
mrr: 0.4369
adjusted_mrr: 0.4369
mrr_dataset_count: 10
benchmark_categories:
- Classic
- LRGB
- OGB
task_categories:
- graph_classification
- graph_regression
- link_prediction
- node_classification
experiment_scopes:
- edge-level
- graph-level
- node-level
results:
- &id001
  dataset: Amazon-Computers
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9228
    std: 0.0039
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
    sort_value: 0.9228
    sort_std: 0.0039
    is_best: true
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9226
    std: 0.0018
    paper_value: 0.9226
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 2
    true_value: 0.9226
    true_std: 0.0018
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9226
    sort_std: 0.0018
    is_best: true
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.9206
    std: 0.0033
    paper_value: 0.9206
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 3
    true_value: 0.9206
    true_std: 0.0033
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9206
    sort_std: 0.0033
    is_best: true
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.9203
    std: 0.0013
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9203
    sort_std: 0.0013
    is_best: true
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.9163
    std: 0.0052
    paper_value: 0.9163
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 6
    true_value: 0.9163
    true_std: 0.0052
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9163
    sort_std: 0.0052
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9163
    std: 0.0018
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9163
    sort_std: 0.0018
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9078
    std: 0.0013
    paper_value: 0.9078
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
    true_value: 0.9078
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9078
    sort_std: 0.0013
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.9075
    std: 0.0059
    paper_value: 0.9075
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 13
    true_value: 0.9075
    true_std: 0.0059
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9075
    sort_std: 0.0059
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.9018
    std: 0.0017
    paper_value: 0.9018
    paper_std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 15
    true_value: 0.9018
    true_std: 0.0017
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9018
    sort_std: 0.0017
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.8988
    std: 0.0064
    paper_value: 0.8988
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 16
    true_value: 0.8988
    true_std: 0.0064
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8988
    sort_std: 0.0064
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8965
    std: 0.0052
    paper_value: 0.8965
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 18
    true_value: 0.8965
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8965
    sort_std: 0.0052
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.8929
    std: 0.0046
    paper_value: 0.8929
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 20
    true_value: 0.8929
    true_std: 0.0046
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8929
    sort_std: 0.0046
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.8883
    std: 0.0044
    paper_value: 0.8883
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
    true_value: 0.8883
    true_std: 0.0044
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8883
    sort_std: 0.0044
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.882
    std: 0.0065
    paper_value: 0.882
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 24
    true_value: 0.882
    true_std: 0.0065
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.882
    sort_std: 0.0065
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.8568
    std: 0.0071
    paper_value: 0.8568
    paper_std: 0.0071
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 33
    true_value: 0.8568
    true_std: 0.0071
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8568
    sort_std: 0.0071
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.8519
    std: 0.0059
    paper_value: 0.8519
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 35
    true_value: 0.8519
    true_std: 0.0059
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8519
    sort_std: 0.0059
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Amazon-Photo
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9537
    std: 0.0044
    paper_value: 0.9537
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 1
    true_value: 0.9537
    true_std: 0.0044
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9537
    sort_std: 0.0044
    is_best: true
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.9445
    std: 0.0045
    paper_value: 0.9445
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: De Bortoli et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 2
    true_value: 0.9445
    true_std: 0.0045
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9445
    sort_std: 0.0045
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.9435
    std: 0.0044
    paper_value: 0.9435
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 3
    true_value: 0.9435
    true_std: 0.0044
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9435
    sort_std: 0.0044
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.9435
    std: 0.005
    paper_value: 0.9435
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 4
    true_value: 0.9435
    true_std: 0.005
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9435
    sort_std: 0.005
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.9434
    std: 0.0034
    paper_value: 0.9434
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 5
    true_value: 0.9434
    true_std: 0.0034
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9434
    sort_std: 0.0034
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.9432
    std: 0.0014
    paper_value: 0.9432
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 6
    true_value: 0.9432
    true_std: 0.0014
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9432
    sort_std: 0.0014
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.9409
    std: 0.0063
    paper_value: 0.9409
    paper_std: 0.0063
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 7
    true_value: 0.9409
    true_std: 0.0063
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9409
    sort_std: 0.0063
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9387
    std: 0.0011
    paper_value: 0.9387
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 8
    true_value: 0.9387
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9387
    sort_std: 0.0011
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.9354
    std: 0.009
    paper_value: 0.9354
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 9
    true_value: 0.9354
    true_std: 0.009
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9354
    sort_std: 0.009
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.9307
    std: 0.0042
    paper_value: 0.9307
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bruna et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 10
    true_value: 0.9307
    true_std: 0.0042
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9307
    sort_std: 0.0042
    is_best: false
  - model: UnionSNN
    model_key: unionsnn
    model_plain: UnionSNN
    value: 0.9292
    std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 11
    sort_value: 0.9292
    sort_std: 0.0038
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.927
    std: 0.002
    paper_value: 0.927
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
    true_value: 0.927
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.927
    sort_std: 0.002
    is_best: false
  - model: CurvGN
    model_key: curvgn
    model_plain: CurvGN
    value: 0.925
    std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 13
    sort_value: 0.925
    sort_std: 0.005
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.9245
    std: 0.0062
    paper_value: 0.9245
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: De Bortoli et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
    true_value: 0.9245
    true_std: 0.0062
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9245
    sort_std: 0.0062
    is_best: false
  - model: UnionGCN
    model_key: uniongcn
    model_plain: UnionGCN
    value: 0.9228
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2305.15747'
    title: Union Subgraph Neural Networks
    date: May 2023
    date_display: May 2023
    date_iso: 2023-05
    codebase_url: https://github.com/AngusMonroe/UnionSNN
    uses_external_data: false
    is_global_top: true
    global_rank: 15
    sort_value: 0.9228
    sort_std: 0.0019
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.921
    std: 0.0061
    paper_value: 0.921
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bruna et al. 2013
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 17
    true_value: 0.921
    true_std: 0.0061
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.921
    sort_std: 0.0061
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: COCO-SP
  rows:
  - model: LPE
    model_key: lpe
    model_plain: LPE
    value: 0.4483
    std: 0.0071
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.4483
    sort_std: 0.0071
    is_best: true
  - model: SPE
    model_key: spe
    model_plain: SPE
    value: 0.4387
    std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.4387
    sort_std: 0.0054
    is_best: true
  - model: RWSE
    model_key: rwse
    model_plain: RWSE
    value: 0.4382
    std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.08028'
    title: Generalizable Insights for Graph Transformers in Theory and Practice
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.4382
    sort_std: 0.0101
    is_best: true
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.3596
    std: 0.0022
    paper_value: 0.3596
    paper_std: 0.0022
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 6
    true_value: 0.3596
    true_std: 0.0022
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3596
    sort_std: 0.0022
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.3297
    std: 0.0053
    paper_value: 0.3297
    paper_std: 0.0053
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 10
    true_value: 0.3297
    true_std: 0.0053
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3297
    sort_std: 0.0053
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.3027
    std: 0.006
    paper_value: 0.3027
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 11
    true_value: 0.3027
    true_std: 0.006
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3027
    sort_std: 0.006
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.3014
    std: 0.0049
    paper_value: 0.3014
    paper_std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
    true_value: 0.3014
    true_std: 0.0049
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3014
    sort_std: 0.0049
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2641
    std: 0.0045
    paper_value: 0.2641
    paper_std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 13
    true_value: 0.2641
    true_std: 0.0045
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2641
    sort_std: 0.0045
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.2602
    std: 0.0048
    paper_value: 0.2602
    paper_std: 0.0048
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 15
    true_value: 0.2602
    true_std: 0.0048
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2602
    sort_std: 0.0048
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.2433
    std: 0.0023
    paper_value: 0.2433
    paper_std: 0.0023
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 20
    true_value: 0.2433
    true_std: 0.0023
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2433
    sort_std: 0.0023
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.2306
    std: 0.0018
    paper_value: 0.2306
    paper_std: 0.0018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
    true_value: 0.2306
    true_std: 0.0018
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2306
    sort_std: 0.0018
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.1644
    std: 0.0079
    paper_value: 0.1644
    paper_std: 0.0079
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
    true_value: 0.1644
    true_std: 0.0079
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1644
    sort_std: 0.0079
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.1339
    std: 0.0044
    paper_value: 0.1339
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 24
    true_value: 0.1339
    true_std: 0.0044
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1339
    sort_std: 0.0044
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.1339
    std: 0.0044
    paper_value: 0.1339
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 25
    true_value: 0.1339
    true_std: 0.0044
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1339
    sort_std: 0.0044
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.1112
    std: 0.0046
    paper_value: 0.1112
    paper_std: 0.0046
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 31
    true_value: 0.1112
    true_std: 0.0046
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1112
    sort_std: 0.0046
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.0841
    std: 0.001
    paper_value: 0.0841
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 37
    true_value: 0.0841
    true_std: 0.001
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0841
    sort_std: 0.001
    is_best: false
  metric: F1
  higher_is_better: true
- &id003
  dataset: Coauthor-CS
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9589
    std: 0.0034
    paper_value: 0.9589
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 1
    true_value: 0.9589
    true_std: 0.0034
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9577
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9577
    sort_std: 0.0015
    is_best: true
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9575
    std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9575
    sort_std: 0.0009
    is_best: true
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.9546
    std: 0.0033
    paper_value: 0.9546
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 4
    true_value: 0.9546
    true_std: 0.0033
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9546
    sort_std: 0.0033
    is_best: true
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.9518
    std: 0.003
    paper_value: 0.9518
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 5
    true_value: 0.9518
    true_std: 0.003
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9518
    sort_std: 0.003
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.9511
    std: 0.0037
    paper_value: 0.9511
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 6
    true_value: 0.9511
    true_std: 0.0037
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9511
    sort_std: 0.0037
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.9504
    std: 0.0032
    paper_value: 0.9504
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 7
    true_value: 0.9504
    true_std: 0.0032
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9504
    sort_std: 0.0032
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.9491
    std: 0.0029
    paper_value: 0.9491
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 8
    true_value: 0.9491
    true_std: 0.0029
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9491
    sort_std: 0.0029
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.949
    std: 0.003
    paper_value: 0.949
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 9
    true_value: 0.949
    true_std: 0.003
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.949
    sort_std: 0.003
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.9481
    std: 0.0023
    paper_value: 0.9481
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 10
    true_value: 0.9481
    true_std: 0.0023
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9481
    sort_std: 0.0023
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.9477
    std: 0.0033
    paper_value: 0.9477
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 11
    true_value: 0.9477
    true_std: 0.0033
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9477
    sort_std: 0.0033
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.9451
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 12
    sort_value: 0.9451
    sort_std: 0.0015
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.9449
    std: 0.0007
    paper_value: 0.9449
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 13
    true_value: 0.9449
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9449
    sort_std: 0.0007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9361
    std: 0.0014
    paper_value: 0.9361
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 15
    true_value: 0.9361
    true_std: 0.0014
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9361
    sort_std: 0.0014
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9292
    std: 0.0012
    paper_value: 0.9292
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 16
    true_value: 0.9292
    true_std: 0.0012
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9292
    sort_std: 0.0012
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.9075
    std: 0.0059
    paper_value: 0.9075
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 25
    true_value: 0.9075
    true_std: 0.0059
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9075
    sort_std: 0.0059
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: PCQM-Contact
  rows:
  - model: ViT-PS
    model_key: vit-ps
    model_plain: ViT-PS
    value: 0.5341
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.02866'
    title: Learning Probabilistic Symmetrization for Architecture Agnostic Equivariance
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: https://github.com/jw9730/lps
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.5341
    sort_std: null
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3637
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2303.06147'
    title: 'Exphormer: Sparse Transformers for Graphs'
    date: Mar 10, 2023
    date_display: Mar 2023
    date_iso: '2023-03-10'
    codebase_url: https://github.com/hamed1375/Exphormer
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.345
    std: 0.0002
    paper_value: 0.345
    paper_std: 0.0002
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 3
    true_value: 0.345
    true_std: 0.0002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.345
    sort_std: 0.0002
    is_best: false
  - model: GPS+Transformer
    model_key: gps+transformer
    model_plain: GPS+Transformer
    value: 0.3442
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.286725
    arxiv_id: '2402.00789'
    title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective
      State Spaces'
    date: Feb 1, 2024
    date_display: Feb 2024
    date_iso: '2024-02-01'
    codebase_url: https://github.com/bowang-lab/Graph-Mamba
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.3442
    sort_std: 0.0009
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.3425
    std: 0.0006
    paper_value: 0.3425
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 6
    true_value: 0.3425
    true_std: 0.0006
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3425
    sort_std: 0.0006
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.3408
    std: 0.002
    paper_value: 0.3408
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 7
    true_value: 0.3408
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3408
    sort_std: 0.002
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.3404
    std: 0.0005
    paper_value: 0.3404
    paper_std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 8
    true_value: 0.3404
    true_std: 0.0005
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3404
    sort_std: 0.0005
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.339
    std: 0.0027
    paper_value: 0.339
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 11
    true_value: 0.339
    true_std: 0.0027
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.339
    sort_std: 0.0027
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.3373
    std: 0.0045
    paper_value: 0.3373
    paper_std: 0.0045
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
    true_value: 0.3373
    true_std: 0.0045
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3373
    sort_std: 0.0045
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.3319
    std: 0.002
    paper_value: 0.3319
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 17
    true_value: 0.3319
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3319
    sort_std: 0.002
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.3272
    std: 0.0008
    paper_value: 0.3272
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 18
    true_value: 0.3272
    true_std: 0.0008
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3272
    sort_std: 0.0008
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.3256
    std: 0.0011
    paper_value: 0.3256
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 19
    true_value: 0.3256
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3256
    sort_std: 0.0011
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
    true_value: 0.3234
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3234
    sort_std: 0.0006
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
    true_value: 0.3218
    true_std: 0.0011
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3218
    sort_std: 0.0011
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 23
    true_value: 0.318
    true_std: 0.0027
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.318
    sort_std: 0.0027
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.2989
    std: 0.0026
    paper_value: 0.2989
    paper_std: 0.0026
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 27
    true_value: 0.2989
    true_std: 0.0026
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2989
    sort_std: 0.0026
    is_best: false
  metric: MRR
  higher_is_better: true
- &id007
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
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.4163
    std: 0.0019
    paper_value: 0.4163
    paper_std: 0.0019
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 4
    true_value: 0.4163
    true_std: 0.0019
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4163
    sort_std: 0.0019
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.3598
    std: 0.002
    paper_value: 0.3598
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 10
    true_value: 0.3598
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3598
    sort_std: 0.002
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.3197
    std: 0.0055
    paper_value: 0.3197
    paper_std: 0.0055
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
    true_value: 0.3197
    true_std: 0.0055
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3197
    sort_std: 0.0055
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.3122
    std: 0.0056
    paper_value: 0.3122
    paper_std: 0.0056
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 15
    true_value: 0.3122
    true_std: 0.0056
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3122
    sort_std: 0.0056
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.3108
    std: 0.0033
    paper_value: 0.3108
    paper_std: 0.0033
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 16
    true_value: 0.3108
    true_std: 0.0033
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3108
    sort_std: 0.0033
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.3045
    std: 0.0036
    paper_value: 0.3045
    paper_std: 0.0036
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 17
    true_value: 0.3045
    true_std: 0.0036
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3045
    sort_std: 0.0036
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2873
    std: 0.0219
    paper_value: 0.2873
    paper_std: 0.0219
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 19
    true_value: 0.2873
    true_std: 0.0219
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2873
    sort_std: 0.0219
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.286
    std: 0.0015
    paper_value: 0.286
    paper_std: 0.0015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
    true_value: 0.286
    true_std: 0.0015
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.286
    sort_std: 0.0015
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.256
    std: 0.0056
    paper_value: 0.256
    paper_std: 0.0056
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 25
    true_value: 0.256
    true_std: 0.0056
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.256
    sort_std: 0.0056
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.188
    std: 0.0085
    paper_value: 0.188
    paper_std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 26
    true_value: 0.188
    true_std: 0.0085
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.188
    sort_std: 0.0085
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.1658
    std: 0.0049
    paper_value: 0.1658
    paper_std: 0.0049
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 28
    true_value: 0.1658
    true_std: 0.0049
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1658
    sort_std: 0.0049
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1268
    std: 0.006
    paper_value: 0.1268
    paper_std: 0.006
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 36
    true_value: 0.1268
    true_std: 0.006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1268
    sort_std: 0.006
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.1265
    std: 0.0076
    paper_value: 0.1265
    paper_std: 0.0076
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 37
    true_value: 0.1265
    true_std: 0.0076
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1265
    sort_std: 0.0076
    is_best: false
  metric: F1
  higher_is_better: true
- &id006
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
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.7182
    std: 0.0024
    metric: AP
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
    global_rank: 3
    sort_value: 0.7182
    sort_std: 0.0024
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.6973
    std: 0.0043
    paper_value: 0.6973
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
    true_value: 0.6973
    true_std: 0.0043
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6973
    sort_std: 0.0043
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.6875
    std: 0.002
    paper_value: 0.6875
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 26
    true_value: 0.6875
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6875
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.593
    std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 28
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09300000000000008
    value_note: ''
    paper_rank: 78
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5864
    std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 35
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09009999999999996
    value_note: ''
    paper_rank: 78
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.6765
    sort_std: 0.0047
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.6695
    std: 0.0063
    paper_value: 0.6695
    paper_std: 0.0063
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 42
    true_value: 0.6695
    true_std: 0.0063
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6695
    sort_std: 0.0063
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.5498
    std: 0.0079
    paper_value: 0.5498
    paper_std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 45
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 83
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.6547
    std: 0.0048
    paper_value: 0.6547
    paper_std: 0.0048
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 52
    true_value: 0.6547
    true_std: 0.0048
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6547
    sort_std: 0.0048
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.6529
    std: 0.0082
    paper_value: 0.6529
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 57
    true_value: 0.6529
    true_std: 0.0082
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6529
    sort_std: 0.0082
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.6463
    std: 0.0027
    paper_value: 0.6463
    paper_std: 0.0027
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 62
    true_value: 0.6463
    true_std: 0.0027
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6463
    sort_std: 0.0027
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.6287
    std: 0.0064
    paper_value: 0.6287
    paper_std: 0.0064
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 72
    true_value: 0.6287
    true_std: 0.0064
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6287
    sort_std: 0.0064
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.6112
    std: 0.0053
    paper_value: 0.6112
    paper_std: 0.0053
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 74
    true_value: 0.6112
    true_std: 0.0053
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6112
    sort_std: 0.0053
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.6023
    std: 0.0027
    paper_value: 0.6023
    paper_std: 0.0027
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 76
    true_value: 0.6023
    true_std: 0.0027
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6023
    sort_std: 0.0027
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.568
    std: 0.0038
    paper_value: 0.568
    paper_std: 0.0038
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 82
    true_value: 0.568
    true_std: 0.0038
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.568
    sort_std: 0.0038
    is_best: false
  metric: AP
  higher_is_better: true
- &id005
  dataset: Peptides-struct
  rows:
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: true
  - model: B-PEARL+SRF
    model_key: b-pearl+srf
    model_plain: B-PEARL+SRF
    value: 0.243
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.243
    sort_std: null
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.2436
    std: 0.0022
    metric: MAE
    higher_is_better: false
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.2436
    sort_std: 0.0022
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3496
    std: 0.0013
    paper_value: 0.3496
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10360000000000003
    value_note: ''
    paper_rank: 94
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: 0.0045000000000000005
    paper_value: 0.3547
    paper_std: 0.0045000000000000005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 94
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.342
    std: 0.0013
    paper_value: 0.342
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 31
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09430000000000002
    value_note: ''
    paper_rank: 93
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.2483
    std: 0.0011
    paper_value: 0.2483
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 38
    true_value: 0.2483
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2483
    sort_std: 0.0011
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.2506
    std: 0.0013
    paper_value: 0.2506
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 51
    true_value: 0.2506
    true_std: 0.0013
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.0013
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.2539
    std: 0.0021
    paper_value: 0.2539
    paper_std: 0.0021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 60
    true_value: 0.2539
    true_std: 0.0021
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2539
    sort_std: 0.0021
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.2564
    std: 0.0031
    paper_value: 0.2564
    paper_std: 0.0031
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 68
    true_value: 0.2564
    true_std: 0.0031
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2564
    sort_std: 0.0031
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.2588
    std: 0.0001
    paper_value: 0.2588
    paper_std: 0.0001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 70
    true_value: 0.2588
    true_std: 0.0001
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2588
    sort_std: 0.0001
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.2643
    std: 0.002
    paper_value: 0.2643
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 76
    true_value: 0.2643
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2643
    sort_std: 0.002
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.2677
    std: 0.0011
    paper_value: 0.2677
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 77
    true_value: 0.2677
    true_std: 0.0011
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2677
    sort_std: 0.0011
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.2734
    std: 0.0004
    paper_value: 0.2734
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 81
    true_value: 0.2734
    true_std: 0.0004
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2734
    sort_std: 0.0004
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.27449999999999997
    std: 0.0006
    paper_value: 0.27449999999999997
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 83
    true_value: 0.27449999999999997
    true_std: 0.0006
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.27449999999999997
    sort_std: 0.0006
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.275
    std: 0.0021
    paper_value: 0.275
    paper_std: 0.0021
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 84
    true_value: 0.275
    true_std: 0.0021
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.275
    sort_std: 0.0021
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: WikiCS
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9589
    std: 0.0034
    paper_value: 0.9589
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 1
    true_value: 0.9589
    true_std: 0.0034
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8019
    std: 0.0041
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
    global_rank: 2
    sort_value: 0.8019
    sort_std: 0.0041
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.7901
    std: 0.0068
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7901
    sort_std: 0.0068
    is_best: false
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.789
    std: 0.01
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
    global_rank: 4
    sort_value: 0.789
    sort_std: 0.01
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: ogbn-arxiv
  rows:
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.7573
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: Llama-7b
    model_key: llama-7b
    model_plain: Llama-7b
    value: 0.757
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.07134'
    title: Language is All a Graph Needs
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/agiresearch/InstructGLM
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.757
    sort_std: 0.0012
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.752
    std: 0.002
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
    global_rank: 3
    sort_value: 0.752
    sort_std: 0.002
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.719
    std: 0.0025
    paper_value: 0.719
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 7
    true_value: 0.742
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02300000000000002
    value_note: ''
    paper_rank: 40
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7182
    std: 0.0023
    paper_value: 0.7182
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
    true_value: 0.7391
    true_std: 0.0012
    value_gap_source_arxiv: '2106.07476'
    value_gap_source_title: Training Graph Neural Networks with 1000 Layers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02090000000000003
    value_note: ''
    paper_rank: 40
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.7391
    sort_std: 0.0012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7174
    std: 0.0029
    paper_value: 0.7174
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
    true_value: 0.731
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013599999999999945
    value_note: ''
    paper_rank: 40
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.731
    sort_std: 0.003
    is_best: false
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.7301
    std: 0.0018
    paper_value: 0.7301
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
    true_value: 0.7301
    true_std: 0.0018
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7301
    sort_std: 0.0018
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.7264
    std: 0.0021
    paper_value: 0.7264
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 29
    true_value: 0.7264
    true_std: 0.0021
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7264
    sort_std: 0.0021
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.7201
    std: 0.002
    paper_value: 0.7201
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 38
    true_value: 0.7201
    true_std: 0.002
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7201
    sort_std: 0.002
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.7197
    std: 0.0012
    paper_value: 0.7197
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 39
    true_value: 0.7197
    true_std: 0.0012
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7197
    sort_std: 0.0012
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.7137
    std: 0.0014
    paper_value: 0.7137
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 43
    true_value: 0.7137
    true_std: 0.0014
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7137
    sort_std: 0.0014
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.7118
    std: 0.0076
    paper_value: 0.7118
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 44
    true_value: 0.7118
    true_std: 0.0076
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7118
    sort_std: 0.0076
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.7113
    std: 0.0047
    paper_value: 0.7113
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 45
    true_value: 0.7113
    true_std: 0.0047
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7113
    sort_std: 0.0047
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.6908
    std: 0.003
    paper_value: 0.6908
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
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 52
    true_value: 0.6908
    true_std: 0.003
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6908
    sort_std: 0.003
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.6623
    std: 0.0019
    paper_value: 0.6623
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 55
    true_value: 0.6623
    true_std: 0.0019
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6623
    sort_std: 0.0019
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
- benchmark: LRGB
  datasets:
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: OGB
  datasets:
  - *id010
single_proposed_model: SGT
main_figure: /figures/2405.13806/main_figure.png
---

