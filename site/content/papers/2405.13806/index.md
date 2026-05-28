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
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- WaveGC
- M
mrr: 0.04
adjusted_mrr: 0.0133
mrr_dataset_count: 1
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
- &id003
  dataset: Amazon-Computers
  rows:
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 1
    true_value: 0.9409
    true_std: 0.0037
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03309999999999991
    value_note: ''
    paper_rank: 20
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9409
    sort_std: 0.0037
    is_best: true
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 2
    true_value: 0.9399
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043399999999999994
    value_note: ''
    paper_rank: 25
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9399
    sort_std: 0.0012
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9378
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9378
    sort_std: 0.001
    is_best: true
  - model: GCN* (-) Dropout
    model_key: gcn* (-) dropout
    model_plain: GCN* (-) Dropout
    value: 0.9378
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9378
    sort_std: 0.0026
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9325
    std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9325
    sort_std: 0.0014
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 11
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
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9226
    sort_std: 0.0018
    is_best: false
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
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
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9206
    sort_std: 0.0033
    is_best: false
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 18
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
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9163
    sort_std: 0.0052
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
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
    paper_rank: 21
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 23
    true_value: 0.9018
    true_std: 0.0017
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 24
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
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8988
    sort_std: 0.0064
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 28
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
    paper_rank: 28
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 29
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
    paper_rank: 29
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 30
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
    paper_rank: 30
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 32
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
    paper_rank: 32
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 33
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
    paper_rank: 33
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9712
    std: 0.0024
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
    sort_value: 0.9712
    sort_std: 0.0024
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9678
    std: 0.0023
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
    global_rank: 2
    sort_value: 0.9678
    sort_std: 0.0023
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 3
    true_value: 0.966
    true_std: 0.0033
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02729999999999999
    value_note: ''
    paper_rank: 26
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9657
    std: 0.0023
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
    sort_value: 0.9657
    sort_std: 0.0023
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 6
    true_value: 0.961
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03399999999999992
    value_note: ''
    paper_rank: 33
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.961
    sort_std: 0.0046
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
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
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9537
    sort_std: 0.0044
    is_best: false
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 20
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
    paper_rank: 20
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
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
    paper_rank: 21
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 22
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
    paper_rank: 22
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 23
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
    paper_rank: 23
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 25
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
    paper_rank: 25
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 26
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
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9409
    sort_std: 0.0063
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 30
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
    paper_rank: 30
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 31
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
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9307
    sort_std: 0.0042
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 36
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
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9245
    sort_std: 0.0062
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 37
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
    paper_rank: 37
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
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.4901
    std: null
    metric: F1
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
    sort_value: 0.4901
    sort_std: null
    is_best: true
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.4752
    std: 0.0032
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
    global_rank: 2
    sort_value: 0.4752
    sort_std: 0.0032
    is_best: false
  - model: GDT (LPE)
    model_key: gdt (lpe)
    model_plain: GDT (LPE)
    value: 0.4483
    std: 0.0070999999999999995
    metric: F1
    higher_is_better: true
    is_baseline: false
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
    sort_value: 0.4483
    sort_std: 0.0070999999999999995
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
    true_value: 0.3802
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11609999999999998
    value_note: ''
    paper_rank: 47
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.3802
    sort_std: 0.0015
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 23
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
    paper_rank: 23
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 36
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
    paper_rank: 36
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 40
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
    paper_rank: 40
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 41
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
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3014
    sort_std: 0.0049
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 45
    true_value: 0.2733
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18919999999999998
    value_note: ''
    paper_rank: 76
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.2733
    sort_std: 0.0041
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 52
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
    paper_rank: 52
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 60
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
    paper_rank: 60
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 62
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
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2306
    sort_std: 0.0018
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 64
    true_value: 0.2125
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0786
    value_note: ''
    paper_rank: 67
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.2125
    sort_std: 0.0009
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 66
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
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1644
    sort_std: 0.0079
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 68
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
    paper_rank: 68
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 69
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
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1112
    sort_std: 0.0046
    is_best: false
  metric: F1
  higher_is_better: true
- &id004
  dataset: Coauthor-CS
  rows:
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9638
    std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9638
    sort_std: 0.0011
    is_best: true
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 2
    true_value: 0.9621
    true_std: 0.0014
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025999999999999912
    value_note: ''
    paper_rank: 20
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.9621
    sort_std: 0.0014
    is_best: true
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 3
    true_value: 0.9617
    true_std: 0.0006
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03249999999999997
    value_note: ''
    paper_rank: 20
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.9617
    sort_std: 0.0006
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9592
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9592
    sort_std: 0.0025
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 5
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
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9585
    std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.9585
    sort_std: 0.0016
    is_best: false
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 9
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
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9546
    sort_std: 0.0033
    is_best: false
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 11
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
    paper_rank: 11
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
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
    paper_rank: 12
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 13
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
    paper_rank: 13
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
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
    paper_rank: 14
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 15
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
    paper_rank: 15
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 16
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
    paper_rank: 16
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 17
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
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9477
    sort_std: 0.0033
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 18
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
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9449
    sort_std: 0.0007
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 21
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
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9075
    sort_std: 0.0059
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6447
    std: 0.0018
    paper_value: 0.6447
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2377999999999999
    value_note: ''
    paper_rank: 274
    rank_delta: 243
    rank_delta_abs: 243
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.6516
    std: 0.0028
    paper_value: 0.6516
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22840000000000005
    value_note: ''
    paper_rank: 273
    rank_delta: 234
    rank_delta_abs: 234
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6176
    std: 0.0014
    paper_value: 0.6176
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2602
    value_note: ''
    paper_rank: 279
    rank_delta: 231
    rank_delta_abs: 231
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: M
    model_key: m
    model_plain: M
    value: 0.6914
    std: 0.0078
    paper_value: 0.6914
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 252
    true_value: 0.6914
    true_std: 0.0078
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 252
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6914
    sort_std: 0.0078
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.6801
    std: 0.0086
    paper_value: 0.6801
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 254
    true_value: 0.6801
    true_std: 0.0086
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 254
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6801
    sort_std: 0.0086
    is_best: false
  - model: SEA-GWNN
    model_key: sea-gwnn
    model_plain: SEA-GWNN
    value: 0.6674
    std: 0.0079
    paper_value: 0.6674
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 268
    true_value: 0.6674
    true_std: 0.0079
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 268
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6674
    sort_std: 0.0079
    is_best: false
  - model: GWNN
    model_key: gwnn
    model_plain: GWNN
    value: 0.6419
    std: 0.0079
    paper_value: 0.6419
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 275
    true_value: 0.6419
    true_std: 0.0079
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 275
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6419
    sort_std: 0.0079
    is_best: false
  - model: UFGConvS
    model_key: ufgconvs
    model_plain: UFGConvS
    value: 0.6243
    std: 0.008
    paper_value: 0.6243
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 279
    true_value: 0.6243
    true_std: 0.008
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 279
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6243
    sort_std: 0.008
    is_best: false
  - model: Scattering GCN
    model_key: scattering gcn
    model_plain: Scattering GCN
    value: 0.6114
    std: 0.0113
    paper_value: 0.6114
    paper_std: 0.0113
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 280
    true_value: 0.6114
    true_std: 0.0113
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 280
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6114
    sort_std: 0.0113
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.5898
    std: 0.0069
    paper_value: 0.5898
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 287
    true_value: 0.5898
    true_std: 0.0069
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 287
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5898
    sort_std: 0.0069
    is_best: false
  - model: Scattering
    model_key: scattering
    model_plain: Scattering
    value: 0.5765
    std: 0.0084
    paper_value: 0.5765
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 290
    true_value: 0.5765
    true_std: 0.0084
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 290
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5765
    sort_std: 0.0084
    is_best: false
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.5765
    std: 0.0105
    paper_value: 0.5765
    paper_std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 291
    true_value: 0.5765
    true_std: 0.0105
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 291
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5765
    sort_std: 0.0105
    is_best: false
  - model: SGWT
    model_key: sgwt
    model_plain: SGWT
    value: 0.5504
    std: 0.0112
    paper_value: 0.5504
    paper_std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 295
    true_value: 0.5504
    true_std: 0.0112
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 295
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5504
    sort_std: 0.0112
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
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
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
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
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 23
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
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.345
    sort_std: 0.0002
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 32
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
    paper_rank: 32
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 34
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
    paper_rank: 34
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 37
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
    paper_rank: 37
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 41
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
    paper_rank: 41
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 43
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
    paper_rank: 43
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 52
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
    paper_rank: 52
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 55
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
    paper_rank: 55
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 58
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
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3256
    sort_std: 0.0011
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 68
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
    paper_rank: 68
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 19
    true_value: 0.4263
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.139
    value_note: ''
    paper_rank: 74
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.4263
    sort_std: 0.0057
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 28
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
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4163
    sort_std: 0.0019
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2492
    value_note: ''
    paper_rank: 109
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 53
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
    paper_rank: 53
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 66
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
    paper_rank: 66
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 68
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
    paper_rank: 68
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 69
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
    paper_rank: 69
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 71
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
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3045
    sort_std: 0.0036
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 76
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
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.286
    sort_std: 0.0015
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 80
    true_value: 0.2718
    true_std: 0.0054
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14529999999999998
    value_note: ''
    paper_rank: 109
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.2718
    sort_std: 0.0054
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 87
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
    paper_rank: 87
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 96
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
    paper_rank: 96
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 103
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
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1658
    sort_std: 0.0049
    is_best: false
  metric: F1
  higher_is_better: true
- &id005
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.746
    sort_std: null
    is_best: true
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7355
    sort_std: 0.001
    is_best: false
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1331
    value_note: ''
    paper_rank: 261
    rank_delta: 252
    rank_delta_abs: 252
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11419999999999997
    value_note: ''
    paper_rank: 273
    rank_delta: 224
    rank_delta_abs: 224
    rank_delta_direction: worse
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: M
    model_key: m
    model_plain: M
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 60
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
    paper_rank: 60
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 86
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
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6875
    sort_std: 0.002
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 128
    true_value: 0.6695
    true_std: 0.0063
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 128
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 142
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 288
    rank_delta: 146
    rank_delta_abs: 146
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 167
    true_value: 0.6547
    true_std: 0.0048
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 167
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 177
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
    paper_rank: 177
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 193
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
    paper_rank: 193
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 225
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
    paper_rank: 225
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 237
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
    paper_rank: 237
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 245
    true_value: 0.6023
    true_std: 0.0027
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 245
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 281
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
    paper_rank: 281
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.568
    sort_std: 0.0038
    is_best: false
  metric: AP
  higher_is_better: true
- &id006
  dataset: Peptides-struct
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.2393
    std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.2393
    sort_std: 0.0004
    is_best: true
  - model: GRPE-FFGT
    model_key: grpe-ffgt
    model_plain: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers
    date: Nov 2023
    date_display: Nov 2023
    date_iso: 2023-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.2416
    sort_std: 0.0026
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10750000000000001
    value_note: ''
    paper_rank: 304
    rank_delta: 301
    rank_delta_abs: 301
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
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
    global_rank: 4
    sort_value: 0.2422
    sort_std: 0.0014
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09890000000000002
    value_note: ''
    paper_rank: 297
    rank_delta: 285
    rank_delta_abs: 285
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 79
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10740000000000002
    value_note: ''
    paper_rank: 311
    rank_delta: 232
    rank_delta_abs: 232
    rank_delta_direction: worse
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: M
    model_key: m
    model_plain: M
    value: 0.2483
    std: 0.0011
    paper_value: 0.2483
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 106
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
    paper_rank: 106
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 147
    true_value: 0.2506
    true_std: 0.0013
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 178
    true_value: 0.2539
    true_std: 0.0021
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 199
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
    paper_rank: 199
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 211
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
    paper_rank: 211
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 232
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
    paper_rank: 232
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 240
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
    paper_rank: 240
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 249
    true_value: 0.2734
    true_std: 0.0004
    value_gap_source_arxiv: '2509.06743'
    value_gap_source_title: Long-Range Graph Wavelet Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 249
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2734
    sort_std: 0.0004
    is_best: false
  - model: WaveShrink-ChebNet
    model_key: waveshrink-chebnet
    model_plain: WaveShrink-ChebNet
    value: 0.2745
    std: 0.0006
    paper_value: 0.2745
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 251
    true_value: 0.2745
    true_std: 0.0006
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 251
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2745
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
    is_overridden: true
    override_reason: Peptides-struct MAE was reported on a x100 scale in extraction;
      corrected to the benchmark scale.
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 252
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
    paper_rank: 252
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.275
    sort_std: 0.0021
    is_best: false
  metric: MAE
  higher_is_better: false
- &id010
  dataset: ogbn-arxiv
  rows:
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.7593
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.7593
    sort_std: 0.0019
    is_best: true
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7573
    sort_std: 0.0051
    is_best: true
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.7571
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) in Learning on
      Graphs
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7571
    sort_std: 0.0024
    is_best: true
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017899999999999916
    value_note: ''
    paper_rank: 64
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014800000000000035
    value_note: ''
    paper_rank: 62
    rank_delta: 45
    rank_delta_abs: 45
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: WaveGC
    model_key: wavegc
    model_plain: WaveGC
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 25
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
    paper_rank: 25
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 35
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
    paper_rank: 35
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 51
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
    paper_rank: 51
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 55
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
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7197
    sort_std: 0.0012
    is_best: false
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 58
    true_value: 0.719
    true_std: 0.0025
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.0025
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 68
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
    paper_rank: 68
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 72
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
    paper_rank: 72
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 74
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
    paper_rank: 74
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 80
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
    paper_rank: 80
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
    variant_inference_reason: ''
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    global_rank: 92
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
    paper_rank: 92
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
main_figure: /figures/2405.13806/main_figure.png
---

