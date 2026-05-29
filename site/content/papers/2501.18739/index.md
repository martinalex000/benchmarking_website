---
title: 'Beyond Message Passing: Neural Graph Pattern Machine'
arxiv_id: '2501.18739'
source_url: ''
authors: []
published_date: Jan 30, 2025
published_date_iso: '2025-01-30'
abstract: 'Graph learning tasks often hinge on identifying key substructure patterns
  -- such as triadic closures in social networks or benzene rings in molecular graphs
  -- that underpin downstream performance. However, most existing graph neural networks
  (GNNs) rely on message passing, which aggregates local neighborhood information
  iteratively and struggles to explicitly capture such fundamental motifs, like triangles,
  k-cliques, and rings. This limitation hinders both expressiveness and long-range
  dependency modeling. In this paper, we introduce the Neural Graph Pattern Machine
  (GPM), a novel framework that bypasses message passing by learning directly from
  graph substructures. GPM efficiently extracts, encodes, and prioritizes task-relevant
  graph patterns, offering greater expressivity and improved ability to capture long-range
  dependencies. Empirical evaluations across four standard tasks -- node classification,
  link prediction, graph classification, and graph regression -- demonstrate that
  GPM outperforms state-of-the-art baselines. Further analysis reveals that GPM exhibits
  strong out-of-distribution generalization, desirable scalability, and enhanced interpretability.
  Code and datasets are available at: https://github.com/Zehong-Wang/GPM.'
codebase_url: https://github.com/Zehong-Wang/GPM
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- GPM
mrr: 0.4554
adjusted_mrr: 0.4554
mrr_dataset_count: 9
benchmark_categories:
- Classic
- TU Dortmund
- OGB
- GNNBenchmark
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
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9228
    std: 0.0039
    paper_value: 0.9228
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
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.9228
    true_std: 0.0039
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9228
    sort_std: 0.0039
    is_best: true
  - model: SGT
    model_key: sgt
    model_plain: SGT
    value: 0.9226
    std: 0.0018
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
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9226
    sort_std: 0.0018
    is_best: true
  - model: WaveNet
    model_key: wavenet
    model_plain: WaveNet
    value: 0.9206
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9206
    sort_std: 0.0033
    is_best: true
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.9203
    std: 0.0013
    paper_value: 0.9203
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Song 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.9203
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9203
    sort_std: 0.0013
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9163
    std: 0.0018
    paper_value: 0.9163
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.9163
    true_std: 0.0018
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9163
    sort_std: 0.0018
    is_best: false
  - model: DEFT
    model_key: deft
    model_plain: DEFT
    value: 0.9163
    std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.13806'
    title: A General Graph Spectral Wavelet Convolution via Chebyshev Order Decomposition
    date: May 22, 2024
    date_display: May 2024
    date_iso: '2024-05-22'
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.9163
    sort_std: 0.0052
    is_best: true
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.9122
    std: 0.0014
    paper_value: 0.9122
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.9122
    true_std: 0.0014
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9122
    sort_std: 0.0014
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9119
    std: 0.0054
    paper_value: 0.9119
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.9119
    true_std: 0.0054
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9119
    sort_std: 0.0054
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.9104
    std: 0.0012
    paper_value: 0.9104
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Fu 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.9104
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9104
    sort_std: 0.0012
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.9098
    std: 0.0073
    paper_value: 0.9098
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Jin 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.9098
    true_std: 0.0073
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9098
    sort_std: 0.0073
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9096
    std: 0.009
    paper_value: 0.9096
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.9096
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9096
    sort_std: 0.009
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
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.9078
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
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
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.9062
    std: 0.0024
    paper_value: 0.9062
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.9062
    true_std: 0.0024
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9062
    sort_std: 0.0024
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
    source_ref: Gasteiger 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 15
    true_value: 0.9018
    true_std: 0.0017
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
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
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.8983
    std: 0.0016
    paper_value: 0.8983
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 17
    true_value: 0.8983
    true_std: 0.0016
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8983
    sort_std: 0.0016
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
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.8965
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
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
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8932
    std: 0.0029
    paper_value: 0.8932
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.8932
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8932
    sort_std: 0.0029
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8698
    std: 0.0062
    paper_value: 0.8698
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.8698
    true_std: 0.0062
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8698
    sort_std: 0.0062
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: COLLAB
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8672
    sort_std: 0.0162
    is_best: true
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8615
    sort_std: 0.001
    is_best: true
  - model: SE2P-C3
    model_key: se2p-c3
    model_plain: SE2P-C3
    value: 0.835
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.11714'
    title: Scalable Expressiveness through Preprocessed Graph Perturbations
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: https://github.com/Danial-sb/SE2P
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.835
    sort_std: 0.017
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
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
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.822
    true_std: 0.021
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.016100000000000003
    value_note: global 0.8220 within std
    paper_rank: 14
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.822
    sort_std: 0.021
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.7894
    std: 0.0044
    paper_value: 0.7894
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.8074
    true_std: 0.0054
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018000000000000016
    value_note: ''
    paper_rank: 15
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.8074
    sort_std: 0.0054
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.807
    std: 0.0074
    paper_value: 0.807
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.807
    true_std: 0.0074
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.807
    sort_std: 0.0074
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7882
    std: 0.0121
    paper_value: 0.7882
    paper_std: 0.0121
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 17
    true_value: 0.7882
    true_std: 0.0121
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7882
    sort_std: 0.0121
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.7879
    std: 0.0074
    paper_value: 0.7879
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.7879
    true_std: 0.0074
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7879
    sort_std: 0.0074
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.7835
    std: 0.0085
    paper_value: 0.7835
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.7835
    true_std: 0.0085
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7835
    sort_std: 0.0085
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7741
    std: 0.0056
    paper_value: 0.7741
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 26
    true_value: 0.7741
    true_std: 0.0056
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7741
    sort_std: 0.0056
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.7735
    std: 0.0093
    paper_value: 0.7735
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 27
    true_value: 0.7735
    true_std: 0.0093
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7735
    sort_std: 0.0093
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.773
    std: 0.0198
    paper_value: 0.773
    paper_std: 0.0198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 28
    true_value: 0.773
    true_std: 0.0198
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.0198
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7717
    std: 0.0078
    paper_value: 0.7717
    paper_std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.7717
    true_std: 0.0078
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7717
    sort_std: 0.0078
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.755
    std: 0.0058
    paper_value: 0.755
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 35
    true_value: 0.755
    true_std: 0.0058
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.0058
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7473
    std: 0.0109
    paper_value: 0.7473
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.7473
    true_std: 0.0109
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7473
    sort_std: 0.0109
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7445
    std: 0.0246
    paper_value: 0.7445
    paper_std: 0.0246
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 39
    true_value: 0.7445
    true_std: 0.0246
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7445
    sort_std: 0.0246
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.7393
    std: 0.0194
    paper_value: 0.7393
    paper_std: 0.0194
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 41
    true_value: 0.7393
    true_std: 0.0194
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7393
    sort_std: 0.0194
    is_best: false
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.7309
    std: 0.0025
    paper_value: 0.7309
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yanardag and Vishwanathan 2015
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 45
    true_value: 0.7309
    true_std: 0.0025
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7309
    sort_std: 0.0025
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: CSL
  rows:
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
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
    sort_std: null
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
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
    sort_std: null
    is_best: true
  - model: ESC-GNN
    model_key: esc-gnn
    model_plain: ESC-GNN
    value: 1.0
    std: null
    paper_value: 1.0
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yan 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 1.0
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
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
    sort_std: null
    is_best: true
  - model: B-PEs
    model_key: b-pes
    model_plain: B-PEs
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: R-PEs
    model_key: r-pes
    model_plain: R-PEs
    value: 1.0
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 1.0
    sort_std: null
    is_best: true
  - model: 3-GNN
    model_key: 3-gnn
    model_plain: 3-GNN
    value: 0.957
    std: null
    paper_value: 0.957
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Morris 2019
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.957
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.957
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.1
    std: null
    paper_value: 0.1
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.1
    true_std: null
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Cora
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.9285
    std: 0.0054
    paper_value: 0.9285
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.9285
    true_std: 0.0054
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: Flan-T5-base
    model_key: flan-t5-base
    model_plain: Flan-T5-base
    value: 0.9077
    std: 0.0052
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
    global_rank: 4
    sort_value: 0.9077
    sort_std: 0.0052
    is_best: false
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
    paper_value: 0.8995
    paper_std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Guo 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.8995
    true_std: 0.0201
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.8874
    std: 0.006
    paper_value: 0.8874
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.8874
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8874
    sort_std: 0.006
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8414
    std: 0.0119
    paper_value: 0.8414
    paper_std: 0.0119
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 29
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2308.07134'
    value_gap_source_title: Language is All a Graph Needs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03639999999999999
    value_note: ''
    paper_rank: 59
    rank_delta: 30
    rank_delta_abs: 30
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8078
    std: 0.0144
    paper_value: 0.8078
    paper_std: 0.0144
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 37
    true_value: 0.8744
    true_std: 0.0137
    value_gap_source_arxiv: '2602.07256'
    value_gap_source_title: 'Graph homophily booster: Reimagining the role of discrete
      features in heterophilic graph learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06659999999999999
    value_note: ''
    paper_rank: 80
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.8744
    sort_std: 0.0137
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.8687
    std: 0.0158
    paper_value: 0.8687
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 42
    true_value: 0.8687
    true_std: 0.0158
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8687
    sort_std: 0.0158
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: IMDB-BINARY
  rows:
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8267
    std: 0.0047
    paper_value: 0.8267
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 1
    true_value: 0.8267
    true_std: 0.0047
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.811
    std: 0.045
    paper_value: 0.811
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.811
    true_std: 0.045
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.811
    sort_std: 0.045
    is_best: true
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7995
    sort_std: 0.0246
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.006
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
    sort_value: 0.785
    sort_std: 0.006
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.7829
    std: 0.0126
    paper_value: 0.7829
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.7829
    true_std: 0.0126
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7829
    sort_std: 0.0126
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.7805
    std: 0.01
    paper_value: 0.7805
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.7805
    true_std: 0.01
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7805
    sort_std: 0.01
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7776
    std: 0.0098
    paper_value: 0.7776
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.7776
    true_std: 0.0098
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7776
    sort_std: 0.0098
    is_best: false
  - model: CoCN
    model_key: cocn
    model_plain: CoCN
    value: 0.7726
    std: 0.0027
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.7726
    sort_std: 0.0027
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.7674
    std: 0.0086
    paper_value: 0.7674
    paper_std: 0.0086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.771
    true_std: 0.007
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0036000000000000476
    value_note: global 0.7710 within std
    paper_rank: 10
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.771
    sort_std: 0.007
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.76
    std: 0.019
    paper_value: 0.76
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.76
    true_std: 0.019
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.019
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.7588
    std: 0.036
    paper_value: 0.7588
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 16
    true_value: 0.7588
    true_std: 0.036
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7588
    sort_std: 0.036
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7231
    std: 0.0367
    paper_value: 0.7231
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 17
    true_value: 0.758
    true_std: 0.009
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03490000000000004
    value_note: global 0.7580 within std
    paper_rank: 46
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.758
    sort_std: 0.009
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
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
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 21
    true_value: 0.755
    true_std: 0.04
    value_gap_source_arxiv: '2406.11714'
    value_gap_source_title: Scalable Expressiveness through Preprocessed Graph Perturbations
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.022399999999999975
    value_note: global 0.7550 within std
    paper_rank: 44
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.04
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.75
    std: 0.042
    paper_value: 0.75
    paper_std: 0.042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 26
    true_value: 0.75
    true_std: 0.042
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.042
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.7445
    std: 0.0583
    paper_value: 0.7445
    paper_std: 0.0583
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 30
    true_value: 0.7445
    true_std: 0.0583
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7445
    sort_std: 0.0583
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.7369
    std: 0.0205
    paper_value: 0.7369
    paper_std: 0.0205
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 40
    true_value: 0.7369
    true_std: 0.0205
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7369
    sort_std: 0.0205
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
    source_ref: Baek et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 43
    true_value: 0.7348
    true_std: 0.0076
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
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
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.6696
    std: 0.0056
    paper_value: 0.6696
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yanardag and Vishwanathan 2015
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 61
    true_value: 0.6696
    true_std: 0.0056
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6696
    sort_std: 0.0056
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: REDDIT-MULTI-5K
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.871
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
    global_rank: 1
    sort_value: 0.871
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.862
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
    sort_value: 0.862
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.3857
    std: 0.0186
    paper_value: 0.3857
    paper_std: 0.0186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.856
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4703
    value_note: ''
    paper_rank: 43
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.856
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3937
    std: 0.014
    paper_value: 0.3937
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4573
    value_note: ''
    paper_rank: 41
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.848
    std: 0.004
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
    global_rank: 5
    sort_value: 0.848
    sort_std: 0.004
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.4307
    std: 0.0029
    paper_value: 0.4307
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 28
    true_value: 0.4307
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4307
    sort_std: 0.0029
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.4215
    std: 0.0013
    paper_value: 0.4215
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 29
    true_value: 0.4215
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4215
    sort_std: 0.0013
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.4214
    std: 0.0007
    paper_value: 0.4214
    paper_std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 30
    true_value: 0.4214
    true_std: 0.0007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4214
    sort_std: 0.0007
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.4166
    std: 0.0015
    paper_value: 0.4166
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2024
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 33
    true_value: 0.4166
    true_std: 0.0015
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4166
    sort_std: 0.0015
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.4155
    std: 0.0016
    paper_value: 0.4155
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 34
    true_value: 0.4155
    true_std: 0.0016
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4155
    sort_std: 0.0016
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.4142
    std: 0.0042
    paper_value: 0.4142
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 35
    true_value: 0.4142
    true_std: 0.0042
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4142
    sort_std: 0.0042
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.4072
    std: 0.0065
    paper_value: 0.4072
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 37
    true_value: 0.4072
    true_std: 0.0065
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4072
    sort_std: 0.0065
    is_best: false
  - model: GMT
    model_key: gmt
    model_plain: GMT
    value: 0.4063
    std: 0.0094
    paper_value: 0.4063
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Baek et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.4063
    true_std: 0.0094
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4063
    sort_std: 0.0094
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.406
    std: 0.0099
    paper_value: 0.406
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 39
    true_value: 0.406
    true_std: 0.0099
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.406
    sort_std: 0.0099
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.4017
    std: 0.0052
    paper_value: 0.4017
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 40
    true_value: 0.4017
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4017
    sort_std: 0.0052
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.3992
    std: 0.0102
    paper_value: 0.3992
    paper_std: 0.0102
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 41
    true_value: 0.3992
    true_std: 0.0102
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3992
    sort_std: 0.0102
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.392
    std: 0.0209
    paper_value: 0.392
    paper_std: 0.0209
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 42
    true_value: 0.392
    true_std: 0.0209
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.392
    sort_std: 0.0209
    is_best: false
  - model: DGK
    model_key: dgk
    model_plain: DGK
    value: 0.3222
    std: 0.001
    paper_value: 0.3222
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Yanardag and Vishwanathan 2015
    variant_inference_reason: 'dataset: fuzzy match to reddit-multi-5k (score=90)'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 45
    true_value: 0.3222
    true_std: 0.001
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3222
    sort_std: 0.001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: WikiCS
  rows:
  - model: SGT
    model_key: sgt
    model_plain: SGT
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
    codebase_url: https://github.com/liun-online/WaveGC
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9589
    sort_std: 0.0034
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8019
    std: 0.0041
    paper_value: 0.8019
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 2
    true_value: 0.8019
    true_std: 0.0041
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8019
    sort_std: 0.0041
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.7901
    std: 0.0068
    paper_value: 0.7901
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Song 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.7901
    true_std: 0.0068
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7887
    std: 0.0011
    paper_value: 0.7887
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.7887
    true_std: 0.0011
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7887
    sort_std: 0.0011
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7866
    std: 0.0049
    paper_value: 0.7866
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 6
    true_value: 0.7866
    true_std: 0.0049
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7866
    sort_std: 0.0049
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7846
    std: 0.0099
    paper_value: 0.7846
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.7846
    true_std: 0.0099
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7846
    sort_std: 0.0099
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.782
    std: 0.0029
    paper_value: 0.782
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.782
    true_std: 0.0029
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.0029
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7812
    std: 0.005
    paper_value: 0.7812
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.7812
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7812
    sort_std: 0.005
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7812
    std: 0.0023
    paper_value: 0.7812
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.7812
    true_std: 0.0023
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7812
    sort_std: 0.0023
    is_best: false
  - model: RAW-GNN
    model_key: raw-gnn
    model_plain: RAW-GNN
    value: 0.7801
    std: 0.0058
    paper_value: 0.7801
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Jin 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.7801
    true_std: 0.0058
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7801
    sort_std: 0.0058
    is_best: false
  - model: VCR-Graphormer
    model_key: vcr-graphormer
    model_plain: VCR-Graphormer
    value: 0.7769
    std: 0.0033
    paper_value: 0.7769
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Fu 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.7769
    true_std: 0.0033
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7769
    sort_std: 0.0033
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7747
    std: 0.0085
    paper_value: 0.7747
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 13
    true_value: 0.7747
    true_std: 0.0085
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7747
    sort_std: 0.0085
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.7716
    std: 0.0072
    paper_value: 0.7716
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.7716
    true_std: 0.0072
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7716
    sort_std: 0.0072
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.77
    std: 0.0077
    paper_value: 0.77
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 15
    true_value: 0.77
    true_std: 0.0077
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.0077
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7691
    std: 0.0082
    paper_value: 0.7691
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 16
    true_value: 0.7691
    true_std: 0.0082
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7691
    sort_std: 0.0082
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.763
    std: 0.013
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
    global_rank: 17
    sort_value: 0.763
    sort_std: 0.013
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7473
    std: 0.0094
    paper_value: 0.7473
    paper_std: 0.0094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.7473
    true_std: 0.0094
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7473
    sort_std: 0.0094
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
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
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.006
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
    global_rank: 2
    sort_value: 0.006
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.526
    std: 0.051
    paper_value: 0.526
    paper_std: 0.051
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.512
    value_note: ''
    paper_rank: 118
    rank_delta: 115
    rank_delta_abs: 115
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.088
    std: 0.002
    paper_value: 0.088
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.074
    value_note: ''
    paper_rank: 49
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.014
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
    value: 0.064
    std: 0.004
    paper_value: 0.064
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.021
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043
    value_note: ''
    paper_rank: 27
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.021
    sort_std: 0.002
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.021
    std: 0.002
    paper_value: 0.021
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.021
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.021
    sort_std: 0.002
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 72
    rank_delta: 61
    rank_delta_abs: 61
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.025
    std: 0.004
    paper_value: 0.025
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.07
    std: 0.004
    paper_value: 0.07
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.0262
    true_std: 0.0025
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043800000000000006
    value_note: ''
    paper_rank: 36
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.0262
    sort_std: 0.0025
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046
    value_note: ''
    paper_rank: 45
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.034
    std: 0.007
    paper_value: 0.034
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 18
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.073
    std: 0.001
    paper_value: 0.073
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03799999999999999
    value_note: ''
    paper_rank: 38
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: Graph-ViT
    model_key: graph-vit
    model_plain: Graph-ViT
    value: 0.035
    std: 0.005
    paper_value: 0.035
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.085
    std: 0.004
    paper_value: 0.085
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.036
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04900000000000001
    value_note: ''
    paper_rank: 46
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.005
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.036
    std: 0.005
    paper_value: 0.036
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.036
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.036
    sort_std: 0.005
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.094
    std: 0.008
    paper_value: 0.094
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 21
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.058
    value_note: ''
    paper_rank: 56
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.036
    std: 0.002
    paper_value: 0.036
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 21
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.144
    std: 0.016
    paper_value: 0.144
    paper_std: 0.016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 22
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10399999999999998
    value_note: ''
    paper_rank: 82
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  - model: AgentNet
    model_key: agentnet
    model_plain: AgentNet
    value: 0.04
    std: 0.006
    paper_value: 0.04
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Martinkus et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 22
    true_value: 0.04
    true_std: 0.006
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.04
    sort_std: 0.006
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.094
    std: 0.005
    paper_value: 0.094
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.059
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.035
    value_note: ''
    paper_rank: 56
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.059
    sort_std: 0.005
    is_best: false
  - model: AWE
    model_key: awe
    model_plain: AWE
    value: 0.059
    std: 0.005
    paper_value: 0.059
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ivanov et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 25
    true_value: 0.059
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.059
    sort_std: 0.005
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.142
    std: 0.01
    paper_value: 0.142
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.067
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07499999999999998
    value_note: ''
    paper_rank: 80
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.067
    sort_std: 0.009
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.067
    std: 0.009
    paper_value: 0.067
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 31
    true_value: 0.067
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.067
    sort_std: 0.009
    is_best: false
  - model: DeepGraph
    model_key: deepgraph
    model_plain: DeepGraph
    value: 0.072
    std: 0.004
    paper_value: 0.072
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al. 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 38
    true_value: 0.072
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.072
    sort_std: 0.004
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 79
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 80
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: GEANet
    model_key: geanet
    model_plain: GEANet
    value: 0.193
    std: 0.001
    paper_value: 0.193
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Liang et al. 2024
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 100
    true_value: 0.193
    true_std: 0.001
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.193
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id010
  dataset: ogbl-collab
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.785
    std: 0.002
    metric: Hits@50
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
    global_rank: 1
    sort_value: 0.785
    sort_std: 0.002
    is_best: true
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.768
    std: 0.003
    metric: Hits@50
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
    sort_value: 0.768
    sort_std: 0.003
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.762
    std: 0.002
    metric: Hits@50
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
    sort_value: 0.762
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4475
    std: 0.0107
    paper_value: 0.4475
    paper_std: 0.0107
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.736
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2885
    value_note: ''
    paper_rank: 12
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.736
    sort_std: 0.002
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.497
    std: 0.0059
    paper_value: 0.497
    paper_std: 0.0059
    metric: Hits@50
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 8
    true_value: 0.497
    true_std: 0.0059
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.497
    sort_std: 0.0059
    is_best: false
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.491
    std: 0.0057
    paper_value: 0.491
    paper_std: 0.0057
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Guo 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.491
    true_std: 0.0057
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.491
    sort_std: 0.0057
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.4819
    std: 0.0094
    paper_value: 0.4819
    paper_std: 0.0094
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 10
    true_value: 0.4819
    true_std: 0.0094
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4819
    sort_std: 0.0094
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.4756
    std: 0.0052
    paper_value: 0.4756
    paper_std: 0.0052
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.4756
    true_std: 0.0052
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4756
    sort_std: 0.0052
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4656
    std: 0.0062
    paper_value: 0.4656
    paper_std: 0.0062
    metric: Hits@50
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 12
    true_value: 0.4656
    true_std: 0.0062
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4656
    sort_std: 0.0062
    is_best: false
  metric: Hits@50
  higher_is_better: true
- &id008
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
    value: 0.694
    std: 0.005
    paper_value: 0.694
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 7
    true_value: 0.742
    true_std: 0.002
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04800000000000004
    value_note: ''
    paper_rank: 51
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.742
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
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
    source_ref: Veličković et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.7391
    true_std: 0.0012
    value_gap_source_arxiv: '2106.07476'
    value_gap_source_title: Training Graph Neural Networks with 1000 Layers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019000000000000017
    value_note: ''
    paper_rank: 37
    rank_delta: 23
    rank_delta_abs: 23
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
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
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
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.7289
    std: 0.0068
    paper_value: 0.7289
    paper_std: 0.0068
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 24
    true_value: 0.7289
    true_std: 0.0068
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7289
    sort_std: 0.0068
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.7248
    std: 0.0
    paper_value: 0.7248
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Behrouz et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 32
    true_value: 0.7248
    true_std: 0.0
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7248
    sort_std: 0.0
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7241
    std: 0.004
    paper_value: 0.7241
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 35
    true_value: 0.7241
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7241
    sort_std: 0.004
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.711
    std: 0.0012
    paper_value: 0.711
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 46
    true_value: 0.711
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.711
    sort_std: 0.0012
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.7054
    std: 0.003
    paper_value: 0.7054
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 48
    true_value: 0.7054
    true_std: 0.003
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7054
    sort_std: 0.003
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.7013
    std: 0.0055
    paper_value: 0.7013
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 49
    true_value: 0.7013
    true_std: 0.0055
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7013
    sort_std: 0.0055
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6719
    std: 0.0083
    paper_value: 0.6719
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 54
    true_value: 0.6719
    true_std: 0.0083
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6719
    sort_std: 0.0083
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: ogbn-products
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.835
    std: 0.001
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
    global_rank: 1
    sort_value: 0.835
    sort_std: 0.001
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.83
    std: 0.001
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
    sort_value: 0.83
    sort_std: 0.001
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.7758
    std: 0.0047
    paper_value: 0.7758
    paper_std: 0.0047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gasteiger 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 3
    true_value: 0.827
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05119999999999991
    value_note: ''
    paper_rank: 19
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.001
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.8262
    std: 0.0039
    paper_value: 0.8262
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
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 4
    true_value: 0.8262
    true_std: 0.0039
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8262
    sort_std: 0.0039
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7945
    std: 0.0059
    paper_value: 0.7945
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 5
    true_value: 0.826
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03149999999999997
    value_note: ''
    paper_rank: 14
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.826
    sort_std: 0.001
    is_best: false
  - model: UniMP
    model_key: unimp
    model_plain: UniMP
    value: 0.8256
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.475605
    arxiv_id: '2009.03509'
    title: 'Masked Label Prediction: Unified Message Passing Model for Semi-Supervised
      Classification'
    date: Sep 2020
    date_display: Sep 2020
    date_iso: 2020-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.8256
    sort_std: 0.0031
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7564
    std: 0.0021
    paper_value: 0.7564
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2017
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 9
    true_value: 0.823
    true_std: 0.001
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06659999999999999
    value_note: ''
    paper_rank: 19
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.823
    sort_std: 0.001
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.82
    std: 0.0043
    paper_value: 0.82
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 11
    true_value: 0.82
    true_std: 0.0043
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.0043
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7976
    std: 0.0059
    paper_value: 0.7976
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chien 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 14
    true_value: 0.7976
    true_std: 0.0059
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7976
    sort_std: 0.0059
    is_best: false
  - model: RUM
    model_key: rum
    model_plain: RUM
    value: 0.7868
    std: 0.014
    paper_value: 0.7868
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 19
    true_value: 0.7868
    true_std: 0.014
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7868
    sort_std: 0.014
    is_best: false
  - model: NAGphormer
    model_key: nagphormer
    model_plain: NAGphormer
    value: 0.7355
    std: 0.0021
    paper_value: 0.7355
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 20
    true_value: 0.7355
    true_std: 0.0021
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7355
    sort_std: 0.0021
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7293
    std: 0.0013
    paper_value: 0.7293
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    global_rank: 22
    true_value: 0.7293
    true_std: 0.0013
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7293
    sort_std: 0.0013
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
- benchmark: TU Dortmund
  datasets:
  - *id005
  - *id006
  - *id007
- benchmark: OGB
  datasets:
  - *id008
  - *id009
  - *id010
- benchmark: GNNBenchmark
  datasets:
  - *id011
single_proposed_model: GPM
main_figure: /figures/2501.18739/main_figure.png
---

