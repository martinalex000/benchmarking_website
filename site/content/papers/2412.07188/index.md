---
title: 'Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking from
  A Spectral Perspective'
arxiv_id: '2412.07188'
source_url: ''
authors: []
published_date: Dec 2024
published_date_iso: 2024-12
abstract: 'Graph Neural Networks (GNNs) have achieved remarkable success in various
  graph-based learning tasks. While their performance is often attributed to the powerful
  neighborhood aggregation mechanism, recent studies suggest that other components
  such as non-linear layers may also significantly affecting how GNNs process the
  input graph data in the spectral domain. Such evidence challenges the prevalent
  opinion that neighborhood aggregation mechanisms dominate the behavioral characteristics
  of GNNs in the spectral domain. To demystify such a conflict, this paper introduces
  a comprehensive benchmark to measure and evaluate GNNs'' capability in capturing
  and leveraging the information encoded in different frequency components of the
  input graph data. Specifically, we first conduct an exploratory study demonstrating
  that GNNs can flexibly yield outputs with diverse frequency components even when
  certain frequencies are absent or filtered out from the input graph data. We then
  formulate a novel research problem of measuring and benchmarking the performance
  of GNNs from a spectral perspective. To take an initial step towards a comprehensive
  benchmark, we design an evaluation protocol supported by comprehensive theoretical
  analysis. Finally, we introduce a comprehensive benchmark on real-world datasets,
  revealing insights that challenge prevalent opinions from a spectral perspective.
  We believe that our findings will open new avenues for future advancements in this
  area. Our implementations can be found at: https://github.com/yushundong/Spectral-benchmark.'
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- FA
mrr: 0.0068
adjusted_mrr: 0.0023
mrr_dataset_count: 1
benchmark_categories:
- Classic
- Heterogeneous Graph Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
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
    value: 0.5828
    std: 0.0209
    paper_value: 0.5828
    paper_std: 0.0209
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 2
    true_value: 0.9621
    true_std: 0.0014
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.37929999999999997
    value_note: ''
    paper_rank: 39
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.9621
    sort_std: 0.0014
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5982
    std: 0.0404
    paper_value: 0.5982
    paper_std: 0.0404
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 3
    true_value: 0.9617
    true_std: 0.0006
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.36350000000000005
    value_note: ''
    paper_rank: 36
    rank_delta: 33
    rank_delta_abs: 33
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
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.529
    std: 0.0216
    paper_value: 0.529
    paper_std: 0.0216
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 18
    true_value: 0.9449
    true_std: 0.0007
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.41589999999999994
    value_note: ''
    paper_rank: 41
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9449
    sort_std: 0.0007
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6317
    std: 0.0201
    paper_value: 0.6317
    paper_std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 28
    true_value: 0.8842
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25249999999999995
    value_note: ''
    paper_rank: 32
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8842
    sort_std: null
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.6627
    std: 0.0277
    paper_value: 0.6627
    paper_std: 0.0277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 31
    true_value: 0.6627
    true_std: 0.0277
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6627
    sort_std: 0.0277
    is_best: false
  - model: GatedGraph
    model_key: gatedgraph
    model_plain: GatedGraph
    value: 0.6614
    std: 0.0293
    paper_value: 0.6614
    paper_std: 0.0293
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 32
    true_value: 0.6614
    true_std: 0.0293
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6614
    sort_std: 0.0293
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.6291
    std: 0.0275
    paper_value: 0.6291
    paper_std: 0.0275
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 33
    true_value: 0.6291
    true_std: 0.0275
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6291
    sort_std: 0.0275
    is_best: false
  - model: Cheb
    model_key: cheb
    model_plain: Cheb
    value: 0.6088
    std: 0.0193
    paper_value: 0.6088
    paper_std: 0.0193
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 34
    true_value: 0.6088
    true_std: 0.0193
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6088
    sort_std: 0.0193
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.6041
    std: 0.0212
    paper_value: 0.6041
    paper_std: 0.0212
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 35
    true_value: 0.6041
    true_std: 0.0212
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6041
    sort_std: 0.0212
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.5989
    std: 0.0173
    paper_value: 0.5989
    paper_std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 36
    true_value: 0.5989
    true_std: 0.0173
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5989
    sort_std: 0.0173
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.5943
    std: 0.015
    paper_value: 0.5943
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 38
    true_value: 0.5943
    true_std: 0.015
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5943
    sort_std: 0.015
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.5925
    std: 0.0419
    paper_value: 0.5925
    paper_std: 0.0419
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 39
    true_value: 0.5925
    true_std: 0.0419
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5925
    sort_std: 0.0419
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.579
    std: 0.0335
    paper_value: 0.579
    paper_std: 0.0335
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 40
    true_value: 0.579
    true_std: 0.0335
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.579
    sort_std: 0.0335
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.5295
    std: 0.0379
    paper_value: 0.5295
    paper_std: 0.0379
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 41
    true_value: 0.5295
    true_std: 0.0379
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5295
    sort_std: 0.0379
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Coauthor-Physics
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9831
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9831
    sort_std: 0.0018
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9808
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9808
    sort_std: 0.0027
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9796
    std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9796
    sort_std: 0.0081
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6038
    std: 0.021
    paper_value: 0.6038
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 6
    true_value: 0.9782
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.37439999999999996
    value_note: ''
    paper_rank: 26
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.9782
    sort_std: 0.0028
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5949
    std: 0.0361
    paper_value: 0.5949
    paper_std: 0.0361
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 8
    true_value: 0.9774
    true_std: 0.0035
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.38250000000000006
    value_note: ''
    paper_rank: 28
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.9774
    sort_std: 0.0035
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.6655
    std: 0.025
    paper_value: 0.6655
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 20
    true_value: 0.6655
    true_std: 0.025
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6655
    sort_std: 0.025
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.6516
    std: 0.0277
    paper_value: 0.6516
    paper_std: 0.0277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 21
    true_value: 0.6516
    true_std: 0.0277
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6516
    sort_std: 0.0277
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6429
    std: 0.021
    paper_value: 0.6429
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 22
    true_value: 0.6429
    true_std: 0.021
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6429
    sort_std: 0.021
    is_best: false
  - model: Cheb
    model_key: cheb
    model_plain: Cheb
    value: 0.6295
    std: 0.0206
    paper_value: 0.6295
    paper_std: 0.0206
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 23
    true_value: 0.6295
    true_std: 0.0206
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6295
    sort_std: 0.0206
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.629
    std: 0.0152
    paper_value: 0.629
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 24
    true_value: 0.629
    true_std: 0.0152
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.629
    sort_std: 0.0152
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.6258
    std: 0.0212
    paper_value: 0.6258
    paper_std: 0.0212
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 25
    true_value: 0.6258
    true_std: 0.0212
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6258
    sort_std: 0.0212
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.6093
    std: 0.0149
    paper_value: 0.6093
    paper_std: 0.0149
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 26
    true_value: 0.6093
    true_std: 0.0149
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6093
    sort_std: 0.0149
    is_best: false
  - model: GatedGraph
    model_key: gatedgraph
    model_plain: GatedGraph
    value: 0.602
    std: 0.0286
    paper_value: 0.602
    paper_std: 0.0286
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 27
    true_value: 0.602
    true_std: 0.0286
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.602
    sort_std: 0.0286
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5965
    std: 0.0327
    paper_value: 0.5965
    paper_std: 0.0327
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 28
    true_value: 0.5965
    true_std: 0.0327
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5965
    sort_std: 0.0327
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.5887
    std: 0.0338
    paper_value: 0.5887
    paper_std: 0.0338
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 29
    true_value: 0.5887
    true_std: 0.0338
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5887
    sort_std: 0.0338
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.5581
    std: 0.0233
    paper_value: 0.5581
    paper_std: 0.0233
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 30
    true_value: 0.5581
    true_std: 0.0233
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5581
    sort_std: 0.0233
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.536
    std: 0.0138
    paper_value: 0.536
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 31
    true_value: 0.536
    true_std: 0.0138
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.536
    sort_std: 0.0138
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
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.6054
    std: 0.0273
    paper_value: 0.6054
    paper_std: 0.0273
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 16
    true_value: 0.8893
    true_std: 0.0137
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.28389999999999993
    value_note: ''
    paper_rank: 280
    rank_delta: 264
    rank_delta_abs: 264
    rank_delta_direction: worse
    sort_value: 0.8893
    sort_std: 0.0137
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6033
    std: 0.0226
    paper_value: 0.6033
    paper_std: 0.0226
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2792
    value_note: ''
    paper_rank: 282
    rank_delta: 251
    rank_delta_abs: 251
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.5426
    std: 0.018
    paper_value: 0.5426
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 39
    true_value: 0.88
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.33740000000000003
    value_note: ''
    paper_rank: 295
    rank_delta: 256
    rank_delta_abs: 256
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6217
    std: 0.0418
    paper_value: 0.6217
    paper_std: 0.0418
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2561
    value_note: ''
    paper_rank: 279
    rank_delta: 231
    rank_delta_abs: 231
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.6109
    std: 0.0371
    paper_value: 0.6109
    paper_std: 0.0371
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 78
    true_value: 0.866
    true_std: 0.003
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2551
    value_note: ''
    paper_rank: 280
    rank_delta: 202
    rank_delta_abs: 202
    rank_delta_direction: worse
    sort_value: 0.866
    sort_std: 0.003
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6397
    std: 0.018
    paper_value: 0.6397
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 117
    true_value: 0.836
    true_std: null
    value_gap_source_arxiv: '2603.27529'
    value_gap_source_title: Cross-attentive Cohesive Subgraph Embedding to Mitigate
      Oversquashing in GNNs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19629999999999992
    value_note: ''
    paper_rank: 275
    rank_delta: 158
    rank_delta_abs: 158
    rank_delta_direction: worse
    sort_value: 0.836
    sort_std: null
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.6305
    std: 0.0221
    paper_value: 0.6305
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 119
    true_value: 0.835
    true_std: 0.005
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20450000000000002
    value_note: ''
    paper_rank: 277
    rank_delta: 158
    rank_delta_abs: 158
    rank_delta_direction: worse
    sort_value: 0.835
    sort_std: 0.005
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.6098
    std: 0.0294
    paper_value: 0.6098
    paper_std: 0.0294
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 128
    true_value: 0.8303
    true_std: 0.0541
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22050000000000003
    value_note: ''
    paper_rank: 280
    rank_delta: 152
    rank_delta_abs: 152
    rank_delta_direction: worse
    sort_value: 0.8303
    sort_std: 0.0541
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.5488
    std: 0.0282
    paper_value: 0.5488
    paper_std: 0.0282
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 147
    true_value: 0.8165
    true_std: null
    value_gap_source_arxiv: '2502.07364'
    value_gap_source_title: Effects of Dropout on Performance in Long-range Graph
      Learning Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.26770000000000005
    value_note: ''
    paper_rank: 295
    rank_delta: 148
    rank_delta_abs: 148
    rank_delta_direction: worse
    sort_value: 0.8165
    sort_std: null
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.6289
    std: 0.0175
    paper_value: 0.6289
    paper_std: 0.0175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 231
    true_value: 0.7183
    true_std: 0.0168
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08940000000000003
    value_note: ''
    paper_rank: 278
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.7183
    sort_std: 0.0168
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.5823
    std: 0.0099
    paper_value: 0.5823
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 234
    true_value: 0.715
    true_std: 0.0051
    value_gap_source_arxiv: '2506.04765'
    value_gap_source_title: 'OpenGT: A Comprehensive Benchmark For Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13269999999999993
    value_note: ''
    paper_rank: 287
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.715
    sort_std: 0.0051
    is_best: false
  - model: GatedGraph
    model_key: gatedgraph
    model_plain: GatedGraph
    value: 0.6985
    std: 0.0274
    paper_value: 0.6985
    paper_std: 0.0274
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 244
    true_value: 0.6985
    true_std: 0.0274
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 244
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6985
    sort_std: 0.0274
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.68
    std: 0.0245
    paper_value: 0.68
    paper_std: 0.0245
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 255
    true_value: 0.68
    true_std: 0.0245
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 255
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.0245
    is_best: false
  - model: Cheb
    model_key: cheb
    model_plain: Cheb
    value: 0.6054
    std: 0.014
    paper_value: 0.6054
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 281
    true_value: 0.6054
    true_std: 0.014
    value_gap_source_arxiv: '2412.07188'
    value_gap_source_title: 'Graph Neural Networks Are More Than Filters: Revisiting
      and Benchmarking from A Spectral Perspective'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 281
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6054
    sort_std: 0.014
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: DBLP
  rows:
  - model: HGSL
    model_key: hgsl
    model_plain: HGSL
    value: 0.9249
    std: 0.0035
    metric: Micro-F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9249
    sort_std: 0.0035
    is_best: true
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.9182
    std: 0.0027
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9182
    sort_std: 0.0027
    is_best: false
  - model: GTN
    model_key: gtn
    model_plain: GTN
    value: 0.9148
    std: 0.0039
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9148
    sort_std: 0.0039
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.6416
    std: 0.0196
    paper_value: 0.6416
    paper_std: 0.0196
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.6416
    sort_std: 0.0196
    is_best: false
  - model: GatedGraph
    model_key: gatedgraph
    model_plain: GatedGraph
    value: 0.6384
    std: 0.0256
    paper_value: 0.6384
    paper_std: 0.0256
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.6384
    sort_std: 0.0256
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.6288
    std: 0.0133
    paper_value: 0.6288
    paper_std: 0.0133
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.6288
    sort_std: 0.0133
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.6186
    std: 0.0136
    paper_value: 0.6186
    paper_std: 0.0136
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.6186
    sort_std: 0.0136
    is_best: false
  - model: Cheb
    model_key: cheb
    model_plain: Cheb
    value: 0.6114
    std: 0.0128
    paper_value: 0.6114
    paper_std: 0.0128
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.6114
    sort_std: 0.0128
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.5938
    std: 0.0192
    paper_value: 0.5938
    paper_std: 0.0192
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5938
    sort_std: 0.0192
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5899
    std: 0.0295
    paper_value: 0.5899
    paper_std: 0.0295
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5899
    sort_std: 0.0295
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.5894
    std: 0.0092
    paper_value: 0.5894
    paper_std: 0.0092
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5894
    sort_std: 0.0092
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5841
    std: 0.0167
    paper_value: 0.5841
    paper_std: 0.0167
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 5
    sort_value: 0.5841
    sort_std: 0.0167
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5813
    std: 0.03
    paper_value: 0.5813
    paper_std: 0.03
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5813
    sort_std: 0.03
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5721
    std: 0.0209
    paper_value: 0.5721
    paper_std: 0.0209
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: 6
    sort_value: 0.5721
    sort_std: 0.0209
    is_best: false
  - model: SGC
    model_key: sgc
    model_plain: SGC
    value: 0.5636
    std: 0.0195
    paper_value: 0.5636
    paper_std: 0.0195
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5636
    sort_std: 0.0195
    is_best: false
  - model: FA
    model_key: fa
    model_plain: FA
    value: 0.5276
    std: 0.011
    paper_value: 0.5276
    paper_std: 0.011
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5276
    sort_std: 0.011
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.5169
    std: 0.004
    paper_value: 0.5169
    paper_std: 0.004
    metric: Normalized AUAC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    global_rank: null
    sort_value: 0.5169
    sort_std: 0.004
    is_best: false
  metric: Micro-F1
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id004
single_proposed_model: FA
main_figure: /figures/2412.07188/main_figure.png
---

