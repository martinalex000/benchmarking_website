---
title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
  Meet Excellence
arxiv_id: '2502.09263'
source_url: ''
authors: []
published_date: Feb 2025
published_date_iso: 2025-02
abstract: 'Message-passing Graph Neural Networks (GNNs) are often criticized for their
  limited expressiveness, issues like over-smoothing and over-squashing, and challenges
  in capturing long-range dependencies. Conversely, Graph Transformers (GTs) are regarded
  as superior due to their employment of global attention mechanisms, which potentially
  mitigate these challenges. Literature frequently suggests that GTs outperform GNNs
  in graph-level tasks, especially for graph classification and regression on small
  molecular graphs. In this study, we explore the untapped potential of GNNs through
  an enhanced framework, GNN+, which integrates six widely used techniques: edge feature
  integration, normalization, dropout, residual connections, feed-forward networks,
  and positional encoding, to effectively tackle graph-level tasks. We conduct a systematic
  re-evaluation of three classic GNNs (GCN, GIN, and GatedGCN) enhanced by the GNN+
  framework across 14 well-known graph-level datasets. Our results reveal that, contrary
  to prevailing beliefs, these classic GNNs consistently match or surpass the performance
  of GTs, securing top-three rankings across all datasets and achieving first place
  in eight. Furthermore, they demonstrate greater efficiency, running several times
  faster than GTs on many datasets. This highlights the potential of simple GNN architectures,
  challenging the notion that complex mechanisms in GTs are essential for superior
  graph-level performance. Our source code is available at https://github.com/LUOyk1999/GNNPlus.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GCN
mrr: 0.0941
adjusted_mrr: 0.0941
mrr_dataset_count: 4
benchmark_categories:
- Classic
- LRGB
- TU Dortmund
- GNNBenchmark
- OGB
- Other Graph Benchmarks
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id010
  dataset: CIFAR10
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.8375
    std: 0.00141
    metric: Accuracy
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
    sort_value: 0.8375
    sort_std: 0.00141
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.80027
    std: 0.00185
    metric: Accuracy
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
    sort_value: 0.80027
    sort_std: 0.00185
    is_best: false
  - model: RandAlign (4 layers)
    model_key: randalign (4 layers)
    model_plain: RandAlign (4 layers)
    value: 0.7942
    std: 0.00072
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2404.09774'
    title: 'RandAlign: A Parameter-Free Method for Regularizing Graph Convolutional
      Networks'
    date: Apr 2024
    date_display: Apr 2024
    date_iso: 2024-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7942
    sort_std: 0.00072
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.77218
    std: 0.00381
    paper_value: 0.77218
    paper_std: 0.00381
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.77218
    true_std: 0.00381
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77218
    sort_std: 0.00381
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.76853
    std: 0.00185
    paper_value: 0.76853
    paper_std: 0.00185
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2024recurrent
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.76853
    true_std: 0.00185
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76853
    sort_std: 0.00185
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.76634
    std: 0.00427
    paper_value: 0.76634
    paper_std: 0.00427
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: liang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 17
    true_value: 0.76634
    true_std: 0.00427
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76634
    sort_std: 0.00427
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.76468
    std: 0.00881
    paper_value: 0.76468
    paper_std: 0.00881
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ma2023graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.76468
    true_std: 0.00881
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76468
    sort_std: 0.00881
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.7456
    std: 0.00381
    paper_value: 0.7456
    paper_std: 0.00381
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: behrouz2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 30
    true_value: 0.7576
    true_std: 0.0042
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01200000000000001
    value_note: ''
    paper_rank: 37
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7576
    sort_std: 0.0042
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.737
    std: 0.0034
    paper_value: 0.737
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: wang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 31
    true_value: 0.7576
    true_std: 0.0042
    value_gap_source_arxiv: '2406.05815'
    value_gap_source_title: What Can We Learn from State Space Models for Machine
      Learning on Graphs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020600000000000063
    value_note: ''
    paper_rank: 43
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.7576
    sort_std: 0.0042
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.74754
    std: 0.00194
    paper_value: 0.74754
    paper_std: 0.00194
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 36
    true_value: 0.74754
    true_std: 0.00194
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74754
    sort_std: 0.00194
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.73963
    std: 0.00361
    paper_value: 0.73963
    paper_std: 0.00361
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: choi2024topology
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 38
    true_value: 0.73963
    true_std: 0.00361
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73963
    sort_std: 0.00361
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.7396
    std: 0.0033
    paper_value: 0.7396
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: he2023generalization
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 39
    true_value: 0.73961
    true_std: 0.0033
    value_gap_source_arxiv: '2308.11129'
    value_gap_source_title: Enhancing Graph Transformers with Hierarchical Distance
      Structural Encoding
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.99999999995449e-06
    value_note: global 0.7396 within std
    paper_rank: 40
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.73961
    sort_std: 0.0033
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.72298
    std: 0.00356
    paper_value: 0.72298
    paper_std: 0.00356
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 62
    true_value: 0.72298
    true_std: 0.00356
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72298
    sort_std: 0.00356
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.69824
    std: 0.00413
    paper_value: 0.69824
    paper_std: 0.00413
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 95
    true_value: 0.69824
    true_std: 0.00413
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69824
    sort_std: 0.00413
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.69592
    std: 0.00287
    paper_value: 0.69592
    paper_std: 0.00287
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 97
    true_value: 0.69592
    true_std: 0.00287
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69592
    sort_std: 0.00287
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.68702
    std: 0.00409
    paper_value: 0.68702
    paper_std: 0.00409
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: hussain2022global
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 102
    true_value: 0.68702
    true_std: 0.00409
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68702
    sort_std: 0.00409
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.59753
    std: 0.00293
    paper_value: 0.59753
    paper_std: 0.00293
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: dwivedi2020generalization
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 112
    true_value: 0.59753
    true_std: 0.00293
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.59753
    sort_std: 0.00293
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: CLUSTER
  rows:
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.80113
    std: 0.0013800000000000002
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.80113
    sort_std: 0.0013800000000000002
    is_best: true
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.80026
    std: 0.00277
    paper_value: 0.80026
    paper_std: 0.00277
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 0.8003
    true_std: 0.0028
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 4.0000000000040004e-05
    value_note: global 0.8003 within std
    paper_rank: 3
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8003
    sort_std: 0.0028
    is_best: true
  - model: PPGT
    model_key: ppgt
    model_plain: PPGT
    value: 0.80027
    std: 0.00114
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_display: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.80027
    sort_std: 0.00114
    is_best: true
  - model: GT + HDSE
    model_key: gt + hdse
    model_plain: GT + HDSE
    value: 0.79965
    std: 0.00203
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.79965
    sort_std: 0.00203
    is_best: true
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.79232
    std: 0.00348
    paper_value: 0.79232
    paper_std: 0.00348
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 14
    true_value: 0.79232
    true_std: 0.00348
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79232
    sort_std: 0.00348
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.79128
    std: 0.00235
    paper_value: 0.79128
    paper_std: 0.00235
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 16
    true_value: 0.79128
    true_std: 0.00235
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.79128
    sort_std: 0.00235
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.78495
    std: 0.00103
    paper_value: 0.78495
    paper_std: 0.00103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2024recurrent
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 27
    true_value: 0.78495
    true_std: 0.00103
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78495
    sort_std: 0.00103
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.78025
    std: 0.00223
    paper_value: 0.78025
    paper_std: 0.00223
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: choi2024topology
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 39
    true_value: 0.7803
    true_std: 0.0022
    value_gap_source_arxiv: '2405.19121'
    value_gap_source_title: Spatio-Spectral Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 4.999999999999449e-05
    value_note: global 0.7803 within std
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7803
    sort_std: 0.0022
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.78016
    std: 0.0018
    paper_value: 0.78016
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 41
    true_value: 0.78016
    true_std: 0.0018
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78016
    sort_std: 0.0018
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.77856
    std: 0.00104
    paper_value: 0.77856
    paper_std: 0.00104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: chen2022structure
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 45
    true_value: 0.77856
    true_std: 0.00104
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77856
    sort_std: 0.00104
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.77109
    std: 0.00872
    paper_value: 0.77109
    paper_std: 0.00872
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 53
    true_value: 0.77109
    true_std: 0.00872
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77109
    sort_std: 0.00872
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.768
    std: 0.0036
    paper_value: 0.768
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: wang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 55
    true_value: 0.768
    true_std: 0.0036
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.768
    sort_std: 0.0036
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.76691
    std: 0.0065
    paper_value: 0.76691
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 57
    true_value: 0.76691
    true_std: 0.0065
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76691
    sort_std: 0.0065
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.74794
    std: 0.00213
    paper_value: 0.74794
    paper_std: 0.00213
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 61
    true_value: 0.74794
    true_std: 0.00213
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.74794
    sort_std: 0.00213
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.73169
    std: 0.00622
    paper_value: 0.73169
    paper_std: 0.00622
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: dwivedi2020generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 62
    true_value: 0.73169
    true_std: 0.00622
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73169
    sort_std: 0.00622
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.396
    std: 0.0175
    paper_value: 0.396
    paper_std: 0.0175
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.396
    true_std: 0.0175
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.396
    sort_std: 0.0175
    is_best: false
  - model: GraphGPS (Tonshoff et al. 2023)
    model_key: graphgps (tonshoff et al. 2023)
    model_plain: GraphGPS (Tonshoff et al. 2023)
    value: 0.3884
    std: 0.0055
    paper_value: 0.3884
    paper_std: 0.0055
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Tonshoff et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 18
    true_value: 0.3884
    true_std: 0.0055
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3884
    sort_std: 0.0055
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3802
    std: 0.0015
    paper_value: 0.3802
    paper_std: 0.0015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 21
    true_value: 0.3802
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3802
    sort_std: 0.0015
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.362
    std: 0.0012
    paper_value: 0.362
    paper_std: 0.0012
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023difformer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 22
    true_value: 0.362
    true_std: 0.0012
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.362
    sort_std: 0.0012
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.3458
    std: 0.007
    paper_value: 0.3458
    paper_std: 0.007
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: chen2023nagphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 30
    true_value: 0.3458
    true_std: 0.007
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3458
    sort_std: 0.007
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.343
    std: 0.0108
    paper_value: 0.343
    paper_std: 0.0108
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 31
    true_value: 0.3455
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0024999999999999467
    value_note: global 0.3455 within std
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3455
    sort_std: 0.0009
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3412
    std: 0.0044
    paper_value: 0.3412
    paper_std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 32
    true_value: 0.3412
    true_std: 0.0044
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3412
    sort_std: 0.0044
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.332
    std: 0.0032
    paper_value: 0.332
    paper_std: 0.0032
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: sancak2024scalable
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 34
    true_value: 0.332
    true_std: 0.0032
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.332
    sort_std: 0.0032
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.3219
    std: 0.0052
    paper_value: 0.3219
    paper_std: 0.0052
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: liang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 38
    true_value: 0.3219
    true_std: 0.0052
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3219
    sort_std: 0.0052
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2733
    std: 0.0041
    paper_value: 0.2733
    paper_std: 0.0041
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 45
    true_value: 0.2733
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2733
    sort_std: 0.0041
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.2618
    std: 0.0031
    paper_value: 0.2618
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: dwivedi2020generalization
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 50
    true_value: 0.2618
    true_std: 0.0031
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2618
    sort_std: 0.0031
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2592
    std: 0.0158
    paper_value: 0.2592
    paper_std: 0.0158
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: kreuzer2021rethinking
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 54
    true_value: 0.2592
    true_std: 0.0158
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2592
    sort_std: 0.0158
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2483
    std: 0.0046
    paper_value: 0.2483
    paper_std: 0.0046
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 58
    true_value: 0.2483
    true_std: 0.0046
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2483
    sort_std: 0.0046
    is_best: false
  metric: F1
  higher_is_better: true
- &id008
  dataset: COLLAB
  rows:
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.8722
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.18480'
    title: Scalable Graph Compressed Convolutions
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    value: 0.809
    std: null
    paper_value: 0.809
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 5
    true_value: 0.827
    true_std: 0.009
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.017999999999999905
    value_note: ''
    paper_rank: 9
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.827
    sort_std: 0.009
    is_best: false
  - model: HRN
    model_key: hrn
    model_plain: HRN
    value: 0.818
    std: null
    paper_value: 0.818
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 8
    true_value: 0.818
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.818
    sort_std: null
    is_best: false
  - model: LDP
    model_key: ldp
    model_plain: LDP
    value: 0.781
    std: null
    paper_value: 0.781
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: cai2018simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 21
    true_value: 0.781
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.781
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id016
  dataset: Code
  rows:
  - model: CodeT5-small + GFSA
    model_key: codet5-small + gfsa
    model_plain: CodeT5-small + GFSA
    value: 0.9494
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9494
    sort_std: null
    is_best: true
  - model: CodeT5-base + GFSA
    model_key: codet5-base + gfsa
    model_plain: CodeT5-base + GFSA
    value: 0.9492
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.9492
    sort_std: null
    is_best: false
  - model: CodeT5-small
    model_key: codet5-small
    model_plain: CodeT5-small
    value: 0.9436
    std: null
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.04234'
    title: Graph Convolutions Enrich the Self-Attention in Transformers!
    date: Dec 2023
    date_display: Dec 2023
    date_iso: 2023-12
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9436
    sort_std: null
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.1937
    std: 0.0028
    paper_value: 0.1937
    paper_std: 0.0028
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: chen2022structure
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.1937
    true_std: 0.0028
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1937
    sort_std: 0.0028
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.1915
    std: 0.002
    paper_value: 0.1915
    paper_std: 0.002
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: sancak2024scalable
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 13
    true_value: 0.1915
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1915
    sort_std: 0.002
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.1896
    std: 0.0024
    paper_value: 0.1896
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 14
    true_value: 0.1896
    true_std: 0.0024
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1896
    sort_std: 0.0024
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.1894
    std: 0.0024
    paper_value: 0.1894
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.1894
    true_std: 0.0024
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1894
    sort_std: 0.0024
    is_best: false
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    value: 0.183
    std: 0.0024
    paper_value: 0.183
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: wu2021representing
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 17
    true_value: 0.183
    true_std: 0.0024
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.183
    sort_std: 0.0024
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.1803
    std: 0.0019
    paper_value: 0.1803
    paper_std: 0.0019
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 19
    true_value: 0.1803
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1803
    sort_std: 0.0019
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1787
    std: 0.0026
    paper_value: 0.1787
    paper_std: 0.0026
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.1787
    true_std: 0.0026
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1787
    sort_std: 0.0026
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.167
    std: 0.0015
    paper_value: 0.167
    paper_std: 0.0015
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: dwivedi2020generalization
    variant_inference_reason: 'dataset: fuzzy match to code (score=90)'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 21
    true_value: 0.167
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.167
    sort_std: 0.0015
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
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
    date: Jan 30, 2025
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
    date: Jan 30, 2025
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
  - model: HRN
    model_key: hrn
    model_plain: HRN
    value: 0.775
    std: null
    paper_value: 0.775
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.775
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.775
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.769
    std: null
    paper_value: 0.769
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.769
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: null
    is_best: false
  - model: LDP
    model_key: ldp
    model_plain: LDP
    value: 0.754
    std: null
    paper_value: 0.754
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: cai2018simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 23
    true_value: 0.754
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.754
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
    global_rank: 3
    sort_value: 0.61
    sort_std: 0.02
    is_best: true
  - model: HRN
    model_key: hrn
    model_plain: HRN
    value: 0.528
    std: null
    paper_value: 0.528
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 17
    true_value: 0.528
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.528
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.523
    std: null
    paper_value: 0.523
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 21
    true_value: 0.523
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.523
    sort_std: null
    is_best: false
  - model: LDP
    model_key: ldp
    model_plain: LDP
    value: 0.5
    std: null
    paper_value: 0.5
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: cai2018simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 40
    true_value: 0.5
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: MNIST
  rows:
  - model: GRASS
    model_key: grass
    model_plain: GRASS
    value: 0.98932
    std: 0.00076
    metric: Accuracy
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
    sort_value: 0.98932
    sort_std: 0.00076
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9884
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.9884
    sort_std: 0.0015
    is_best: true
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9876
    std: 0.00079
    metric: Accuracy
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
    global_rank: 3
    sort_value: 0.9876
    sort_std: 0.00079
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.98712
    std: 0.00137
    paper_value: 0.98712
    paper_std: 0.00137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.98712
    true_std: 0.00137
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98712
    sort_std: 0.00137
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.98414
    std: 0.00038
    paper_value: 0.98414
    paper_std: 0.00038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: shirzad2023exphormer
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 10
    true_value: 0.9855
    true_std: 0.00039
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0013600000000000279
    value_note: ''
    paper_rank: 23
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.9855
    sort_std: 0.00039
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.98513
    std: 0.00086
    paper_value: 0.98513
    paper_std: 0.00086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: liang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.98513
    true_std: 0.00086
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98513
    sort_std: 0.00086
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.9846
    std: 0.0009
    paper_value: 0.9846
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 18
    true_value: 0.9846
    true_std: 0.0009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9846
    sort_std: 0.0009
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.9842
    std: 0.0008
    paper_value: 0.9842
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: wang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 23
    true_value: 0.9842
    true_std: 0.0008
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9842
    sort_std: 0.0008
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.98391
    std: 0.00182
    paper_value: 0.98391
    paper_std: 0.00182
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: behrouz2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 24
    true_value: 0.98391
    true_std: 0.00182
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98391
    sort_std: 0.00182
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.98383
    std: 0.00012
    paper_value: 0.98383
    paper_std: 0.00012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2024recurrent
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 25
    true_value: 0.98383
    true_std: 0.00012
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98383
    sort_std: 0.00012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.98382
    std: 0.00095
    paper_value: 0.98382
    paper_std: 0.00095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 26
    true_value: 0.98382
    true_std: 0.00095
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98382
    sort_std: 0.00095
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.98285
    std: 0.00103
    paper_value: 0.98285
    paper_std: 0.00103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 32
    true_value: 0.98285
    true_std: 0.00103
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98285
    sort_std: 0.00103
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.98231
    std: 0.00132
    paper_value: 0.98231
    paper_std: 0.00132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: choi2024topology
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 38
    true_value: 0.98231
    true_std: 0.00132
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98231
    sort_std: 0.00132
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.98173
    std: 0.00087
    paper_value: 0.98173
    paper_std: 0.00087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: hussain2022global
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 44
    true_value: 0.98173
    true_std: 0.00087
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98173
    sort_std: 0.00087
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.98108
    std: 0.00111
    paper_value: 0.98108
    paper_std: 0.00111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 57
    true_value: 0.98108
    true_std: 0.00111
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98108
    sort_std: 0.00111
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.98051
    std: 0.00126
    paper_value: 0.98051
    paper_std: 0.00126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 63
    true_value: 0.98051
    true_std: 0.00126
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98051
    sort_std: 0.00126
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.90831
    std: 0.00161
    paper_value: 0.90831
    paper_std: 0.00161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: dwivedi2020generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 99
    true_value: 0.90831
    true_std: 0.00161
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.90831
    sort_std: 0.00161
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: HRN
    model_key: hrn
    model_plain: HRN
    value: 0.904
    std: null
    paper_value: 0.904
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: wu2022simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 19
    true_value: 0.904
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.904
    sort_std: null
    is_best: false
  - model: LDP
    model_key: ldp
    model_plain: LDP
    value: 0.903
    std: null
    paper_value: 0.903
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: cai2018simple
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.903
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.903
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.901
    std: null
    paper_value: 0.901
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 22
    true_value: 0.901
    true_std: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.901
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id017
  dataset: MalNet-Tiny
  rows:
  - model: ESA
    model_key: esa
    model_plain: ESA
    value: 0.948
    std: 0.00424
    metric: Accuracy
    higher_is_better: true
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
    sort_value: 0.948
    sort_std: 0.00424
    is_best: true
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.946
    std: 0.0057
    paper_value: 0.946
    paper_std: 0.0057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 2
    true_value: 0.946
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.946
    sort_std: 0.0057
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9437
    std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9437
    sort_std: 0.0058
    is_best: true
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.9417
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 4
    sort_value: 0.9417
    sort_std: 0.002
    is_best: false
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.9406
    std: 0.0064
    paper_value: 0.9406
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: huang2024can
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 6
    true_value: 0.9406
    true_std: 0.0064
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9406
    sort_std: 0.0064
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9402
    std: 0.0021
    paper_value: 0.9402
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: shirzad2023exphormer
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.9402
    true_std: 0.0021
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9402
    sort_std: 0.0021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9354
    std: 0.0045
    paper_value: 0.9354
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.9354
    true_std: 0.0045
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9354
    sort_std: 0.0045
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.935
    std: 0.0041
    paper_value: 0.935
    paper_std: 0.0041
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 13
    true_value: 0.935
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.935
    sort_std: 0.0041
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.934
    std: 0.0027
    paper_value: 0.934
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 15
    true_value: 0.934
    true_std: 0.0027
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.934
    sort_std: 0.0027
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9325
    std: 0.004
    paper_value: 0.9325
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 16
    true_value: 0.9325
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9325
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
  dataset: PATTERN
  rows:
  - model: GRIT (our run)
    model_key: grit (our run)
    model_plain: GRIT (our run)
    value: 0.90405
    std: 0.00232
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.90405
    sort_std: 0.00232
    is_best: true
  - model: GRIT 2-QiQRW
    model_key: grit 2-qiqrw
    model_plain: GRIT 2-QiQRW
    value: 0.90165
    std: 0.00446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.20519'
    title: Enhancing Graph Neural Networks with Quantum Computed Encodings
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.90165
    sort_std: 0.00446
    is_best: true
  - model: PPGT
    model_key: ppgt
    model_plain: PPGT
    value: 0.89752
    std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    date_display: Apr 2025
    date_iso: 2025-04
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.89752
    sort_std: 0.0003
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.87196
    std: 0.00076
    paper_value: 0.87196
    paper_std: 0.00076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ma2023graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 20
    true_value: 0.87196
    true_std: 0.00076
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87196
    sort_std: 0.00076
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.8709
    std: 0.0126
    paper_value: 0.8709
    paper_std: 0.0126
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: behrouz2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 22
    true_value: 0.8714
    true_std: 0.0012
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0004999999999999449
    value_note: global 0.8714 within std
    paper_rank: 23
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.8714
    sort_std: 0.0012
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.8671
    std: 0.0005
    paper_value: 0.8671
    paper_std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: wang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 23
    true_value: 0.8714
    true_std: 0.0012
    value_gap_source_arxiv: '2406.05815'
    value_gap_source_title: What Can We Learn from State Space Models for Machine
      Learning on Graphs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0042999999999999705
    value_note: ''
    paper_rank: 52
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.8714
    sort_std: 0.0012
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.87029
    std: 0.00037
    paper_value: 0.87029
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 25
    true_value: 0.87029
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87029
    sort_std: 0.00037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.87021
    std: 0.00095
    paper_value: 0.87021
    paper_std: 0.00095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 26
    true_value: 0.87021
    true_std: 0.00095
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87021
    sort_std: 0.00095
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.8702
    std: 0.00042
    paper_value: 0.8702
    paper_std: 0.00042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: park2022grpe
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 27
    true_value: 0.8702
    true_std: 0.00042
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8702
    sort_std: 0.00042
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.86993
    std: 0.00026
    paper_value: 0.86993
    paper_std: 0.00026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: liang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 30
    true_value: 0.86993
    true_std: 0.00026
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86993
    sort_std: 0.00026
    is_best: false
  - model: LGI-GT
    model_key: lgi-gt
    model_plain: LGI-GT
    value: 0.8693
    std: 0.0004
    paper_value: 0.8693
    paper_std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: yinlgi
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 33
    true_value: 0.8693
    true_std: 0.0004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8693
    sort_std: 0.0004
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
    value: 0.86848
    std: 0.00037
    paper_value: 0.86848
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: chen2022structure
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 39
    true_value: 0.86848
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86848
    sort_std: 0.00037
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.86842
    std: 0.00048
    paper_value: 0.86842
    paper_std: 0.00048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 40
    true_value: 0.86842
    true_std: 0.00048
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86842
    sort_std: 0.00048
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.86821
    std: 0.0002
    paper_value: 0.86821
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: hussain2022global
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 42
    true_value: 0.86821
    true_std: 0.0002
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86821
    sort_std: 0.0002
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.86759
    std: 0.0002
    paper_value: 0.86759
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ding2024recurrent
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 47
    true_value: 0.8676
    true_std: 0.02
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 1.0000000000065512e-05
    value_note: global 0.8676 within std
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8676
    sort_std: 0.02
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.86734
    std: 8.0e-05
    paper_value: 0.86734
    paper_std: 8.0e-05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 48
    true_value: 0.86742
    true_std: 0.00015
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 7.999999999996898e-05
    value_note: global 0.8674 within std
    paper_rank: 51
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.86742
    sort_std: 0.00015
    is_best: false
  - model: GPTrans-Nano
    model_key: gptrans-nano
    model_plain: GPTrans-Nano
    value: 0.86731
    std: 0.00085
    paper_value: 0.86731
    paper_std: 0.00085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: chen2023graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 52
    true_value: 0.86731
    true_std: 0.00085
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86731
    sort_std: 0.00085
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.86685
    std: 0.00059
    paper_value: 0.86685
    paper_std: 0.00059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 57
    true_value: 0.86685
    true_std: 0.00059
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86685
    sort_std: 0.00059
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.86681
    std: 0.00062
    paper_value: 0.86681
    paper_std: 0.00062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: choi2024topology
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 58
    true_value: 0.86681
    true_std: 0.00062
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86681
    sort_std: 0.00062
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.86581
    std: 0.00037
    paper_value: 0.86581
    paper_std: 0.00037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: kreuzer2021rethinking
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 66
    true_value: 0.86581
    true_std: 0.00037
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86581
    sort_std: 0.00037
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.84808
    std: 0.00068
    paper_value: 0.84808
    paper_std: 0.00068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: dwivedi2020generalization
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 83
    true_value: 0.84808
    true_std: 0.00068
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84808
    sort_std: 0.00068
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.4561
    std: 0.0039
    paper_value: 0.4561
    paper_std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: huang2024can
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 7
    true_value: 0.4561
    true_std: 0.0039
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4561
    sort_std: 0.0039
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.4263
    std: 0.0057
    paper_value: 0.4263
    paper_std: 0.0057
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 19
    true_value: 0.4263
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4263
    sort_std: 0.0057
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.421
    std: 0.008
    paper_value: 0.421
    paper_std: 0.008
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: sancak2024scalable
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 22
    true_value: 0.421
    true_std: 0.008
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.421
    sort_std: 0.008
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.4191
    std: 0.0126
    paper_value: 0.4191
    paper_std: 0.0126
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 26
    true_value: 0.4191
    true_std: 0.0126
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4191
    sort_std: 0.0126
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.4006
    std: 0.0061
    paper_value: 0.4006
    paper_std: 0.0061
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: chen2023nagphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 32
    true_value: 0.4006
    true_std: 0.0061
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4006
    sort_std: 0.0061
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.3988
    std: 0.0045
    paper_value: 0.3988
    paper_std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wu2023difformer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 34
    true_value: 0.3988
    true_std: 0.0045
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3988
    sort_std: 0.0045
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3446
    std: 0.0064
    paper_value: 0.3446
    paper_std: 0.0064
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0529
    value_note: ''
    paper_rank: 57
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.3933
    std: 0.0027
    paper_value: 0.3933
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: liang2024graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 38
    true_value: 0.3933
    true_std: 0.0027
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3933
    sort_std: 0.0027
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3357
    std: 0.0087
    paper_value: 0.3357
    paper_std: 0.0087
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0403
    value_note: ''
    paper_rank: 58
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3748
    std: 0.0109
    paper_value: 0.3748
    paper_std: 0.0109
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 48
    true_value: 0.3748
    true_std: 0.0109
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3748
    sort_std: 0.0109
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.3314
    std: 0.0024
    paper_value: 0.3314
    paper_std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: gutteridge2023drew
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 59
    true_value: 0.3314
    true_std: 0.0024
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3314
    sort_std: 0.0024
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.323
    std: 0.0039
    paper_value: 0.323
    paper_std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: kreuzer2021rethinking
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 62
    true_value: 0.323
    true_std: 0.0039
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.323
    sort_std: 0.0039
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3189
    std: 0.0105
    paper_value: 0.3189
    paper_std: 0.0105
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 67
    true_value: 0.3189
    true_std: 0.0105
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3189
    sort_std: 0.0105
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.2694
    std: 0.0098
    paper_value: 0.2694
    paper_std: 0.0098
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: dwivedi2020generalization
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 83
    true_value: 0.2694
    true_std: 0.0098
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2694
    sort_std: 0.0098
    is_best: false
  metric: F1
  higher_is_better: true
- &id002
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
    value: 0.7261
    std: 0.0067
    paper_value: 0.7261
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.715
    std: 0.0044
    paper_value: 0.715
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: gutteridge2023drew
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 22
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.7133
    std: 0.0011
    paper_value: 0.7133
    paper_std: 0.0011
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: ding2024recurrent
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 31
    true_value: 0.7133
    true_std: 0.0011
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7133
    sort_std: 0.0011
    is_best: false
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.7081
    std: 0.0062
    paper_value: 0.7081
    paper_std: 0.0062
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: huang2024can
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 36
    true_value: 0.7081
    true_std: 0.0062
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7081
    sort_std: 0.0062
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7059
    std: 0.0089
    paper_value: 0.7059
    paper_std: 0.0089
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7059
    sort_std: 0.0089
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7006
    std: 0.0033
    paper_value: 0.7006
    paper_std: 0.0033
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7006
    sort_std: 0.0033
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.6988
    std: 0.0082
    paper_value: 0.6988
    paper_std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 53
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.6975
    std: 0.0025
    paper_value: 0.6975
    paper_std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: sancak2024scalable
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 58
    true_value: 0.6975
    true_std: 0.0025
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6975
    sort_std: 0.0025
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.697
    std: 0.008
    paper_value: 0.697
    paper_std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 63
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GPNN
    model_key: gpnn
    model_plain: GPNN
    value: 0.6955
    std: 0.0057
    paper_value: 0.6955
    paper_std: 0.0057
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: lin2024understanding
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 70
    true_value: 0.6955
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6955
    sort_std: 0.0057
    is_best: false
  - model: MGT
    model_key: mgt
    model_plain: MGT
    value: 0.6817
    std: 0.0064
    paper_value: 0.6817
    paper_std: 0.0064
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: ngo2023multiresolution
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 103
    true_value: 0.6817
    true_std: 0.0064
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6817
    sort_std: 0.0064
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.6739
    std: 0.0087
    paper_value: 0.6739
    paper_std: 0.0087
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 118
    true_value: 0.6739
    true_std: 0.0087
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6739
    sort_std: 0.0087
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.6679
    std: 0.0074
    paper_value: 0.6679
    paper_std: 0.0074
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: choi2024topology
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 135
    true_value: 0.6679
    true_std: 0.0074
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6679
    sort_std: 0.0074
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.6415
    std: 0.0052
    paper_value: 0.6415
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: bar2024subgraphormer
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 149
    true_value: 0.661
    true_std: 0.005
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019500000000000073
    value_note: ''
    paper_rank: 208
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.661
    sort_std: 0.005
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.6535
    std: 0.0041
    paper_value: 0.6535
    paper_std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 166
    true_value: 0.655
    true_std: 0.004
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015000000000000568
    value_note: global 0.6550 within std
    paper_rank: 168
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.655
    sort_std: 0.004
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6258
    std: 0.0092
    paper_value: 0.6258
    paper_std: 0.0092
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: shirzad2023exphormer
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026899999999999924
    value_note: ''
    paper_rank: 229
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.6485
    std: 0.0035
    paper_value: 0.6485
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: liang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 186
    true_value: 0.6485
    true_std: 0.0035
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 186
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6485
    sort_std: 0.0035
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 202
    true_value: 0.6439
    true_std: 0.0075
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6439
    sort_std: 0.0075
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.6326
    std: 0.0126
    paper_value: 0.6326
    paper_std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: dwivedi2020generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 219
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 219
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
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
    value: 0.2421
    std: 0.0016
    paper_value: 0.2421
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.2429
    std: 0.0019
    paper_value: 0.2429
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.2429
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2429
    sort_std: 0.0019
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2431
    std: 0.002
    paper_value: 0.2431
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.2449
    std: 0.0016
    paper_value: 0.2449
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: he2023generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 32
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: MGT
    model_key: mgt
    model_plain: MGT
    value: 0.2453
    std: 0.0025
    paper_value: 0.2453
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: ngo2023multiresolution
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 39
    true_value: 0.2453
    true_std: 0.0025
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2453
    sort_std: 0.0025
    is_best: false
  - model: GPNN
    model_key: gpnn
    model_plain: GPNN
    value: 0.2454
    std: 0.0003
    paper_value: 0.2454
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: lin2024understanding
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 42
    true_value: 0.2454
    true_std: 0.0003
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2454
    sort_std: 0.0003
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.2455
    std: 0.0013
    paper_value: 0.2455
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: ding2024recurrent
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 43
    true_value: 0.2455
    true_std: 0.0013
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2455
    sort_std: 0.0013
    is_best: false
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.2459
    std: 0.002
    paper_value: 0.2459
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: huang2024can
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 51
    true_value: 0.2459
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2459
    sort_std: 0.002
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.246
    std: 0.0012
    paper_value: 0.246
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: ma2023graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 56
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.2464
    std: 0.0009
    paper_value: 0.2464
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: sancak2024scalable
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 64
    true_value: 0.2464
    true_std: 0.0009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2464
    sort_std: 0.0009
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.2475
    std: 0.0007
    paper_value: 0.2475
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: bar2024subgraphormer
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 86
    true_value: 0.2475
    true_std: 0.0007
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0007
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.2478
    std: 0.0016
    paper_value: 0.2478
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: wang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 97
    true_value: 0.2478
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2478
    sort_std: 0.0016
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.2512
    std: 0.0025
    paper_value: 0.2512
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: shirzad2023exphormer
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0030999999999999917
    value_note: ''
    paper_rank: 155
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.2485
    std: 0.0015
    paper_value: 0.2485
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: choi2024topology
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 109
    true_value: 0.2485
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2485
    sort_std: 0.0015
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.25
    std: 0.0005
    paper_value: 0.25
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: rampavsek2022recipe
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 136
    true_value: 0.25
    true_std: 0.0012
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0012
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.2529
    std: 0.0016
    paper_value: 0.2529
    paper_std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: dwivedi2020generalization
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 170
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 170
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.2536
    std: 0.0015
    paper_value: 0.2536
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: gutteridge2023drew
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 174
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 174
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.2545
    std: 0.0012
    paper_value: 0.2545
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: kreuzer2021rethinking
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 189
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: GEAET
    model_key: geaet
    model_plain: GEAET
    value: 0.2547
    std: 0.0009
    paper_value: 0.2547
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: liang2024graph
    variant_inference_reason: 'dataset: exact match'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 190
    true_value: 0.2547
    true_std: 0.0009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 190
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2547
    sort_std: 0.0009
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
  dataset: ZINC
  rows:
  - model: FloydNet
    model_key: floydnet
    model_plain: FloydNet
    value: 0.016
    std: null
    metric: MAE
    higher_is_better: false
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
    sort_value: 0.016
    sort_std: null
    is_best: true
  - model: ESA (PE)
    model_key: esa (pe)
    model_plain: ESA (PE)
    value: 0.017331929457918168
    std: 0.0009253668251948539
    metric: MAE
    higher_is_better: false
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.017331929457918168
    sort_std: 0.0009253668251948539
    is_best: false
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.018
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.059
    std: 0.002
    paper_value: 0.059
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: ma2023graph
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 9
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.036
    value_note: ''
    paper_rank: 49
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
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
    table_ref: Table 2
    source_ref: Ying 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 210
    rank_delta: 192
    rank_delta_abs: 192
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.081
    std: 0.009
    paper_value: 0.081
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Zhang 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 19
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056
    value_note: ''
    paper_rank: 150
    rank_delta: 131
    rank_delta_abs: 131
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer-URPE
    model_key: graphormer-urpe
    model_plain: Graphormer-URPE
    value: 0.086
    std: 0.007
    paper_value: 0.086
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Luo 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 25
    true_value: 0.028
    true_std: 0.002
    value_gap_source_arxiv: '2310.20519'
    value_gap_source_title: Enhancing Graph Neural Networks with Quantum Computed
      Encodings
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057999999999999996
    value_note: ''
    paper_rank: 164
    rank_delta: 139
    rank_delta_abs: 139
    rank_delta_direction: worse
    sort_value: 0.028
    sort_std: 0.002
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
    table_ref: Table 2
    source_ref: Chen 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 35
    true_value: 0.036
    true_std: 0.002
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.058
    value_note: ''
    paper_rank: 181
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
    sort_value: 0.036
    sort_std: 0.002
    is_best: false
  - model: TIGT
    model_key: tigt
    model_plain: TIGT
    value: 0.057
    std: 0.002
    paper_value: 0.057
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: choi2024topology
    variant_inference_reason: 'zinc: mae fallback <= 0.06'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 46
    true_value: 0.057
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.057
    sort_std: 0.002
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.065
    std: 0.004
    paper_value: 0.065
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 75
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.066
    std: 0.003
    paper_value: 0.066
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Bo 2023
    variant_inference_reason: 'zinc: default subset fallback'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 78
    true_value: 0.066
    true_std: 0.003
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.066
    sort_std: 0.003
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
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
    table_ref: Table 2
    source_ref: Rampásek 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 98
    true_value: 0.069
    true_std: 0.008
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0010000000000000009
    value_note: global 0.0690 within std
    paper_rank: 107
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.069
    sort_std: 0.008
    is_best: false
  - model: Cluster-GT
    model_key: cluster-gt
    model_plain: Cluster-GT
    value: 0.071
    std: 0.004
    paper_value: 0.071
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Huang 2024
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 112
    true_value: 0.071
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.071
    sort_std: 0.004
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
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
    table_ref: Table 2
    source_ref: He 2023
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 118
    true_value: 0.073
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.076
    std: 0.009
    paper_value: 0.076
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.077
    std: 0.005
    paper_value: 0.077
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 132
    true_value: 0.077
    true_std: 0.005
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.077
    sort_std: 0.005
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.077
    std: 0.002
    paper_value: 0.077
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Ding 2024
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 135
    true_value: 0.077
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.077
    sort_std: 0.002
    is_best: false
  - model: GRPE
    model_key: grpe
    model_plain: GRPE
    value: 0.094
    std: 0.002
    paper_value: 0.094
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Park 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 183
    true_value: 0.094
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 183
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.002
    is_best: false
  - model: EGT
    model_key: egt
    model_plain: EGT
    value: 0.108
    std: 0.009
    paper_value: 0.108
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Hussain 2022
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 197
    true_value: 0.108
    true_std: 0.009
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.009
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
    table_ref: Table 2
    source_ref: Kreuzer 2021
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 224
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
    paper_rank: 225
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.226
    std: 0.014
    paper_value: 0.226
    paper_std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Dwivedi 2020
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 264
    true_value: 0.226
    true_std: 0.014
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 264
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.226
    sort_std: 0.014
    is_best: false
  metric: MAE
  higher_is_better: false
- &id014
  dataset: ogbg-molhiv
  rows:
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9685
    std: 0.0001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9685
    sort_std: 0.0001
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9682
    std: 0.0003
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9682
    sort_std: 0.0003
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8012
    std: 0.0124
    paper_value: 0.8012
    paper_std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 3
    true_value: 0.9681
    true_std: 0.0003
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16689999999999994
    value_note: ''
    paper_rank: 30
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7928
    std: 0.0099
    paper_value: 0.7928
    paper_std: 0.0099
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 4
    true_value: 0.968
    true_std: 0.002
    value_gap_source_arxiv: '2502.02379'
    value_gap_source_title: 'No Metric to Rule Them All: Toward Principled Evaluations
      of Graph-Learning Datasets'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17520000000000002
    value_note: ''
    paper_rank: 56
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.968
    sort_std: 0.002
    is_best: true
  - model: SigGate-GT
    model_key: siggate-gt
    model_plain: SigGate-GT
    value: 0.8247
    std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2604.17324'
    title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers via Sigmoid-Gated
      Attention'
    date: Apr 2026
    date_display: Apr 2026
    date_iso: 2026-04
    codebase_url: https://github.com/bettyguo/SigGate-GT
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8247
    sort_std: 0.0063
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7834
    std: 0.0044
    paper_value: 0.7834
    paper_std: 0.0044
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: shirzad2023exphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 12
    true_value: 0.8075
    true_std: 0.0094
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02410000000000001
    value_note: ''
    paper_rank: 92
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.8075
    sort_std: 0.0094
    is_best: false
  - model: EGT (pre-trained)
    model_key: egt (pre-trained)
    model_plain: EGT (pre-trained)
    value: 0.806
    std: 0.0065
    paper_value: 0.806
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: hussain2022global
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 14
    true_value: 0.806
    true_std: 0.0065
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.806
    sort_std: 0.0065
    is_best: false
  - model: Graphormer (pre-trained)
    model_key: graphormer (pre-trained)
    model_plain: Graphormer (pre-trained)
    value: 0.8051
    std: 0.0053
    paper_value: 0.8051
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: ying2021transformers
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 17
    true_value: 0.8051
    true_std: 0.0053
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8051
    sort_std: 0.0053
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.804
    std: 0.0164
    paper_value: 0.804
    paper_std: 0.0164
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 19
    true_value: 0.804
    true_std: 0.0164
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.804
    sort_std: 0.0164
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.8038
    std: 0.0192
    paper_value: 0.8038
    paper_std: 0.0192
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: bar2024subgraphormer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 23
    true_value: 0.8038
    true_std: 0.0192
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8038
    sort_std: 0.0192
    is_best: false
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.8035
    std: 0.0142
    paper_value: 0.8035
    paper_std: 0.0142
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: huang2024can
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 24
    true_value: 0.8035
    true_std: 0.0142
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8035
    sort_std: 0.0142
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.7997
    std: 0.0102
    paper_value: 0.7997
    paper_std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: he2023generalization
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 34
    true_value: 0.7997
    true_std: 0.0102
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7997
    sort_std: 0.0102
    is_best: false
  - model: GECO
    model_key: geco
    model_plain: GECO
    value: 0.798
    std: 0.02
    paper_value: 0.798
    paper_std: 0.02
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: sancak2024scalable
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 42
    true_value: 0.798
    true_std: 0.02
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.798
    sort_std: 0.02
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.7889
    std: 0.0124
    paper_value: 0.7889
    paper_std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: bo2023specformer
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 72
    true_value: 0.7889
    true_std: 0.0124
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7889
    sort_std: 0.0124
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.788
    std: 0.0101
    paper_value: 0.788
    paper_std: 0.0101
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: rampavsek2022recipe
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 75
    true_value: 0.788
    true_std: 0.0101
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.0101
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.7835
    std: 0.0054
    paper_value: 0.7835
    paper_std: 0.0054
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: ma2023graph
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 92
    true_value: 0.7835
    true_std: 0.0054
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7835
    sort_std: 0.0054
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.7785
    std: 0.247
    paper_value: 0.7785
    paper_std: 0.247
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: kreuzer2021rethinking
    variant_inference_reason: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    global_rank: 122
    true_value: 0.7785
    true_std: 0.247
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7785
    sort_std: 0.247
    is_best: true
  metric: ROC-AUC
  higher_is_better: true
- &id015
  dataset: ogbg-molpcba
  is_multi_metric: true
  rows:
  - model: SAT
    model_key: sat
    model_plain: SAT
    metric_values:
    - null
    - 0.7522
    metric_stds:
    - null
    - 0.0056
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.7522
    sort_std: 0.0056
    true_value: null
    true_std: null
    paper_value: 0.7522
    paper_std: 0.0056
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: true
    global_rank: null
  - model: GT
    model_key: gt
    model_plain: GT
    metric_values:
    - null
    - 0.6454
    metric_stds:
    - null
    - 0.0033
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.6454
    sort_std: 0.0033
    true_value: null
    true_std: null
    paper_value: 0.6454
    paper_std: 0.0033
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: ''
    value_gap_source_title: ''
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: null
  - model: GatedGCN + VN
    model_key: gatedgcn + vn
    model_plain: GatedGCN + VN
    metric_values:
    - 0.3141
    - null
    metric_stds:
    - 0.0019
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: false
    sort_value: 0.3141
    sort_std: 0.0019
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    metric_values:
    - 0.3086
    - null
    metric_stds:
    - 0.0031
    - null
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
    global_rank: 2
    is_best: false
    sort_value: 0.3086
    sort_std: 0.0031
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    metric_values:
    - 0.2981
    - 0.8258
    metric_stds:
    - 0.0024
    - 0.0055
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.3066
    sort_std: 0.0013
    true_value: 0.3066
    true_std: 0.0013
    paper_value: 0.2981
    paper_std: 0.0024
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008500000000000008
    value_gap_source_arxiv: '2405.11951'
    value_gap_source_title: 'Distinguished In Uniform: Self-Attention Vs. Virtual
      Nodes'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 3
  - model: LGI-GT
    model_key: lgi-gt
    model_plain: LGI-GT
    metric_values:
    - 0.304
    - null
    metric_stds:
    - 0.0029
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: Self-Attention Vs. Virtual Nodes'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
    sort_value: 0.304
    sort_std: 0.0029
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    metric_values:
    - 0.2972
    - null
    metric_stds:
    - 0.0023
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2972
    sort_std: 0.0023
    true_value: 0.2972
    true_std: 0.0023
    paper_value: 0.2972
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 8
  - model: GECO
    model_key: geco
    model_plain: GECO
    metric_values:
    - 0.2961
    - 0.7982
    metric_stds:
    - 0.0008
    - 0.0042
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2961
    sort_std: 0.0008
    true_value: 0.2961
    true_std: 0.0008
    paper_value: 0.2961
    paper_std: 0.0008
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 10
  - model: EGT (pre-trained)
    model_key: egt (pre-trained)
    model_plain: EGT (pre-trained)
    metric_values:
    - 0.2961
    - null
    metric_stds:
    - 0.0024
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2961
    sort_std: 0.0024
    true_value: 0.2961
    true_std: 0.0024
    paper_value: 0.2961
    paper_std: 0.0024
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 9
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    metric_values:
    - 0.2849
    - null
    metric_stds:
    - 0.0025
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.292
    sort_std: 0.003
    true_value: 0.292
    true_std: 0.003
    paper_value: 0.2849
    paper_std: 0.0025
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007099999999999995
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 17
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    metric_values:
    - 0.2907
    - 0.8015
    metric_stds:
    - 0.0028
    - 0.0033
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.291
    sort_std: 0.001
    true_value: 0.291
    true_std: 0.001
    paper_value: 0.2907
    paper_std: 0.0028
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_gap_source_arxiv: '2604.24293'
    value_gap_source_title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature
      Evolution via Continuous Phase Transitions'
    value_note: global 0.2910 within std
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 20
  - model: SAN
    model_key: san
    model_plain: SAN
    metric_values:
    - 0.2765
    - null
    metric_stds:
    - 0.0042
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2765
    sort_std: 0.0042
    true_value: 0.2765
    true_std: 0.0042
    paper_value: 0.2765
    paper_std: 0.0042
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 36
  - model: GraphTrans
    model_key: graphtrans
    model_plain: GraphTrans
    metric_values:
    - 0.2761
    - null
    metric_stds:
    - 0.0029
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2761
    sort_std: 0.0029
    true_value: 0.2761
    true_std: 0.0029
    paper_value: 0.2761
    paper_std: 0.0029
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 38
  - model: GCN
    model_key: gcn
    model_plain: GCN
    metric_values:
    - 0.2721
    - 0.8077
    metric_stds:
    - 0.0046
    - 0.0041
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2721
    sort_std: 0.0046
    true_value: 0.2721
    true_std: 0.0046
    paper_value: 0.2721
    paper_std: 0.0046
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 40
  - model: GIN
    model_key: gin
    model_plain: GIN
    metric_values:
    - 0.2703
    - 0.8107
    metric_stds:
    - 0.0024
    - 0.0053
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2703
    sort_std: 0.0024
    true_value: 0.2703
    true_std: 0.0024
    paper_value: 0.2703
    paper_std: 0.0024
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 41
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    metric_values:
    - 0.2362
    - null
    metric_stds:
    - 0.002
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.2362
    sort_std: 0.002
    true_value: 0.2362
    true_std: 0.002
    paper_value: 0.2362
    paper_std: 0.002
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 52
  metrics:
  - AP
  - Accuracy
  primary_metric: AP
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
- benchmark: TU Dortmund
  datasets:
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: GNNBenchmark
  datasets:
  - *id010
  - *id011
  - *id012
  - *id013
- benchmark: OGB
  datasets:
  - *id014
  - *id015
  - *id016
- benchmark: Other Graph Benchmarks
  datasets:
  - *id017
single_proposed_model: GCN
main_figure: /figures/2502.09263/main_figure.png
---

