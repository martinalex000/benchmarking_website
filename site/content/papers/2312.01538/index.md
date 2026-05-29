---
title: Recurrent Distance Filtering for Graph Representation Learning
arxiv_id: '2312.01538'
source_url: ''
authors: []
published_date: Dec 3, 2023
published_date_iso: '2023-12-03'
abstract: 'Graph neural networks based on iterative one-hop message passing have been
  shown to struggle in harnessing the information from distant nodes effectively.
  Conversely, graph transformers allow each node to attend to all other nodes directly,
  but lack graph inductive bias and have to rely on ad-hoc positional encoding. In
  this paper, we propose a new architecture to reconcile these challenges. Our approach
  stems from the recent breakthroughs in long-range modeling provided by deep state-space
  models: for a given target node, our model aggregates other nodes by their shortest
  distances to the target and uses a linear RNN to encode the sequence of hop representations.
  The linear RNN is parameterized in a particular diagonal form for stable long-range
  signal propagation and is theoretically expressive enough to encode the neighborhood
  hierarchy. With no need for positional encoding, we empirically show that the performance
  of our model is comparable to or better than that of state-of-the-art graph transformers
  on various benchmarks, with a significantly reduced computational cost. Our code
  is open-source at https://github.com/skeletondyh/GRED.'
codebase_url: https://github.com/skeletondyh/GRED
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- GRED
- GRED+LapPE
- GRED (K=10)
mrr: 0.0485
adjusted_mrr: 0.0323
mrr_dataset_count: 2
benchmark_categories:
- Classic
- TU Dortmund
- LRGB
- GNNBenchmark
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id007
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.64223
    std: 0.00455
    paper_value: 0.64223
    paper_std: 0.00455
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 4
    true_value: 0.9
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.25777000000000005
    value_note: ''
    paper_rank: 38
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.9
    sort_std: 0.01
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5571
    std: 0.00381
    paper_value: 0.5571
    paper_std: 0.00381
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 5
    true_value: 0.89
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3329
    value_note: ''
    paper_rank: 39
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.89
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.55255
    std: 0.01527
    paper_value: 0.55255
    paper_std: 0.01527
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 6
    true_value: 0.89
    true_std: 0.01
    value_gap_source_arxiv: '1312.6203'
    value_gap_source_title: Spectral Networks and Locally Connected Networks on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.33745
    value_note: ''
    paper_rank: 39
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.89
    sort_std: 0.01
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 10
    true_value: 0.76853
    true_std: 0.00185
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76853
    sort_std: 0.00185
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 11
    true_value: 0.76468
    true_std: 0.00881
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76468
    sort_std: 0.00881
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 14
    true_value: 0.7396
    true_std: 0.0033
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7396
    sort_std: 0.0033
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 18
    true_value: 0.723
    true_std: 0.0036
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.7230 within std
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.0036
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 32
    true_value: 0.68702
    true_std: 0.00409
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68702
    sort_std: 0.00409
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.67312
    std: 0.00311
    paper_value: 0.67312
    paper_std: 0.00311
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 35
    true_value: 0.67312
    true_std: 0.00311
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67312
    sort_std: 0.00311
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: NCI1
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.874
    std: 0.003
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
    sort_value: 0.874
    sort_std: 0.003
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.862
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
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.004
    is_best: false
  - model: Graphtransformer
    model_key: graphtransformer
    model_plain: Graphtransformer
    value: 0.858
    std: 0.005
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
    sort_value: 0.858
    sort_std: 0.005
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
    table_ref: Table 2 (tab:tud)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 4
    true_value: 0.851
    true_std: 0.003
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.050999999999999934
    value_note: ''
    paper_rank: 26
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.003
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
    table_ref: Table 2 (tab:tud)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 6
    true_value: 0.838
    true_std: 0.006
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07799999999999996
    value_note: ''
    paper_rank: 46
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.006
    is_best: false
  - model: GRED (K=10)
    model_key: gred (k=10)
    model_plain: GRED (K=10)
    value: 0.826
    std: 0.014
    paper_value: 0.826
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 2 (tab:tud)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 13
    true_value: 0.826
    true_std: 0.014
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.826
    sort_std: 0.014
    is_best: false
  - model: SPN (K=10)
    model_key: spn (k=10)
    model_plain: SPN (K=10)
    value: 0.782
    std: 0.012
    paper_value: 0.782
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:tud)
    source_ref: Abboud et al.
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 35
    true_value: 0.782
    true_std: 0.012
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.012
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.769
    std: 0.019
    paper_value: 0.769
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:tud)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 39
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.764
    std: 0.017
    paper_value: 0.764
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:tud)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 42
    true_value: 0.764
    true_std: 0.017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.017
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.762
    std: 0.014
    paper_value: 0.762
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (tab:tud)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 45
    true_value: 0.762
    true_std: 0.014
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.014
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: PATTERN
  rows:
  - model: DGN
    model_key: dgn
    model_plain: DGN
    value: 0.96
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.96
    sort_std: 0.002
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.93
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.93
    sort_std: 0.002
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.85568
    std: 0.00088
    paper_value: 0.85568
    paper_std: 0.00088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 3
    true_value: 0.92
    true_std: 0.003
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06432000000000004
    value_note: ''
    paper_rank: 36
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.92
    sort_std: 0.003
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8559
    std: 0.00011
    paper_value: 0.8559
    paper_std: 0.00011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 4
    true_value: 0.91
    true_std: 0.003
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05410000000000004
    value_note: ''
    paper_rank: 35
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.91
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.78271
    std: 0.00186
    paper_value: 0.78271
    paper_std: 0.00186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2017
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 5
    true_value: 0.9
    true_std: 0.004
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11729
    value_note: ''
    paper_rank: 43
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.9
    sort_std: 0.004
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.89
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2010.02863'
    title: Directional Graph Networks
    date: Oct 2020
    date_display: Oct 2020
    date_iso: 2020-10
    codebase_url: https://github.com/Saro00/DGN
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.89
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.85614
    std: 0.00032
    paper_value: 0.85614
    paper_std: 0.00032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 7
    true_value: 0.88
    true_std: 0.005
    value_gap_source_arxiv: '2010.02863'
    value_gap_source_title: Directional Graph Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.023859999999999992
    value_note: ''
    paper_rank: 35
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.88
    sort_std: 0.005
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
    table_ref: Table 1
    source_ref: Ma 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 10
    true_value: 0.87196
    true_std: 0.00076
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.87196
    sort_std: 0.00076
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
    table_ref: Table 1
    source_ref: Chen 2022
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 15
    true_value: 0.86848
    true_std: 0.00037
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86848
    sort_std: 0.00037
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
    table_ref: Table 1
    source_ref: Hussain 2022
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 16
    true_value: 0.86821
    true_std: 0.0002
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 17
    true_value: 0.86759
    true_std: 0.0002
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86759
    sort_std: 0.0002
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: Table 1
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 24
    true_value: 0.86685
    true_std: 0.00059
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86685
    sort_std: 0.00059
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
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 29
    true_value: 0.86581
    true_std: 0.00037
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86581
    sort_std: 0.00037
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: PROTEINS
  rows:
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.802
    std: 0.009
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
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.795
    std: 0.01
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
    sort_value: 0.795
    sort_std: 0.01
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.791
    std: 0.011
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
    sort_value: 0.791
    sort_std: 0.011
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.733
    std: 0.04
    paper_value: 0.733
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 5
    true_value: 0.785
    true_std: 0.012
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.052000000000000046
    value_note: ''
    paper_rank: 64
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.785
    sort_std: 0.012
    is_best: true
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.737
    std: 0.035
    paper_value: 0.737
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 6
    true_value: 0.781
    true_std: null
    value_gap_source_arxiv: '2305.06102'
    value_gap_source_title: Towards Better Graph Representation Learning with Parameterized
      Decomposition & Filtering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04400000000000004
    value_note: ''
    paper_rank: 62
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.781
    sort_std: null
    is_best: true
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
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 18
    true_value: 0.768
    true_std: 0.018
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.038000000000000034
    value_note: global 0.7680 within std
    paper_rank: 65
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.768
    sort_std: 0.018
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.729
    std: 0.035
    paper_value: 0.729
    paper_std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 26
    true_value: 0.7626
    true_std: null
    value_gap_source_arxiv: '1905.05178'
    value_gap_source_title: Graph U-Nets
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03359999999999996
    value_note: global 0.7626 within std
    paper_rank: 66
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.7626
    sort_std: null
    is_best: true
  - model: GRED (K=10)
    model_key: gred (k=10)
    model_plain: GRED (K=10)
    value: 0.75
    std: 0.029
    paper_value: 0.75
    paper_std: 0.029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 50
    true_value: 0.75
    true_std: 0.029
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.029
    is_best: false
  - model: SPN (K=10)
    model_key: spn (k=10)
    model_plain: SPN (K=10)
    value: 0.745
    std: 0.032
    paper_value: 0.745
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: Abboud et al.
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 57
    true_value: 0.745
    true_std: 0.032
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.745
    sort_std: 0.032
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.723
    std: 0.034
    paper_value: 0.723
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (labeled tab:tud in text)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 67
    true_value: 0.7265
    true_std: null
    value_gap_source_arxiv: '1806.08804'
    value_gap_source_title: Hierarchical Graph Representation Learning with Differentiable
      Pooling
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0035000000000000586
    value_note: global 0.7265 within std
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7265
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.6996
    std: 0.0076
    paper_value: 0.6996
    paper_std: 0.0076
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 4
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01539999999999997
    value_note: ''
    paper_rank: 16
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: DRew+LapPE
    model_key: drew+lappe
    model_plain: DRew+LapPE
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 5
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.7085
    std: 0.0027
    paper_value: 0.7085
    paper_std: 0.0027
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 7
    true_value: 0.7133
    true_std: 0.0011
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0048000000000000265
    value_note: ''
    paper_rank: 10
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7133
    sort_std: 0.0011
    is_best: false
  - model: GRED+LapPE
    model_key: gred+lappe
    model_plain: GRED+LapPE
    value: 0.7133
    std: 0.0011
    paper_value: 0.7133
    paper_std: 0.0011
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 8
    true_value: 0.7133
    true_std: 0.0011
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7133
    sort_std: 0.0011
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 19
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
    is_best: false
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 22
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.686
    std: 0.005
    paper_value: 0.686
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 28
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.686
    sort_std: 0.005
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.6816
    std: 0.0026
    paper_value: 0.6816
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 34
    true_value: 0.6816
    true_std: 0.0026
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6816
    sort_std: 0.0026
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6765
    std: 0.0047
    paper_value: 0.6765
    paper_std: 0.0047
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 35
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6765
    sort_std: 0.0047
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.6621
    std: 0.0067
    paper_value: 0.6621
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 45
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6621
    sort_std: 0.0067
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 50
    true_value: 0.6565
    true_std: 0.0038
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0030000000000000027
    value_note: global 0.6565 within std
    paper_rank: 52
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.6565
    sort_std: 0.0038
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.6384
    std: 0.0121
    paper_value: 0.6384
    paper_std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 67
    true_value: 0.6384
    true_std: 0.0121
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384
    sort_std: 0.0121
    is_best: false
  metric: AP
  higher_is_better: true
- &id004
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
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.2503
    std: 0.0019
    paper_value: 0.2503
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 10
    true_value: 0.2455
    true_std: 0.0013
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0048000000000000265
    value_note: ''
    paper_rank: 48
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.2455
    sort_std: 0.0013
    is_best: false
  - model: GRED+LapPE
    model_key: gred+lappe
    model_plain: GRED+LapPE
    value: 0.2455
    std: 0.0013
    paper_value: 0.2455
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 11
    true_value: 0.2455
    true_std: 0.0013
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2455
    sort_std: 0.0013
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.246
    std: 0.0007
    paper_value: 0.246
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 14
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0007
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 15
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.2473
    std: 0.0017
    paper_value: 0.2473
    paper_std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 22
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: Graph-MLPMixer
    model_key: graph-mlpmixer
    model_plain: Graph-MLPMixer
    value: 0.2475
    std: 0.0015
    paper_value: 0.2475
    paper_std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 26
    true_value: 0.2475
    true_std: 0.0015
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0015
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2477
    std: 0.0009
    paper_value: 0.2477
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Tonshoff 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 31
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 44
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
    value: 0.2781
    std: 0.0028
    paper_value: 0.2781
    paper_std: 0.0028
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 57
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.024500000000000022
    value_note: ''
    paper_rank: 85
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: DRew+LapPE
    model_key: drew+lappe
    model_plain: DRew+LapPE
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 58
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.254
    std: 0.0046
    paper_value: 0.254
    paper_std: 0.0046
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 62
    true_value: 0.254
    true_std: 0.0046
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.254
    sort_std: 0.0046
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
    value: 0.2683
    std: 0.0043
    paper_value: 0.2683
    paper_std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 78
    true_value: 0.268
    true_std: 0.004
    value_gap_source_arxiv: '2502.01122'
    value_gap_source_title: Learning Efficient Positional Encodings with Graph Neural
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.2680 within std
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.282
    std: 0.015
    paper_value: 0.282
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 1
    true_value: 0.004
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27799999999999997
    value_note: ''
    paper_rank: 107
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
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
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.387
    std: 0.015
    paper_value: 0.387
    paper_std: 0.015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.373
    value_note: ''
    paper_rank: 113
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: true
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
    is_best: true
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.021
    std: 0.002
    metric: MAE
    higher_is_better: false
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
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.021
    sort_std: 0.002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.278
    std: 0.003
    paper_value: 0.278
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 9
    true_value: 0.024
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.254
    value_note: ''
    paper_rank: 106
    rank_delta: 97
    rank_delta_abs: 97
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: null
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
    source_ref: Ying 2021
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 11
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
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
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
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
    table_ref: Table 1
    source_ref: Ma 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 24
    true_value: 0.059
    true_std: 0.002
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.059
    sort_std: 0.002
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Corso 2020
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 31
    true_value: 0.067
    true_std: 0.009
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.121
    value_note: ''
    paper_rank: 97
    rank_delta: 66
    rank_delta_abs: 66
    rank_delta_direction: worse
    sort_value: 0.067
    sort_std: 0.009
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
    table_ref: Table 1
    source_ref: He 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 39
    true_value: 0.073
    true_std: 0.001
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.001
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 43
    true_value: 0.077
    true_std: 0.002
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.077
    sort_std: 0.002
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.09
    std: 0.004
    paper_value: 0.09
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Michel 2023
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 52
    true_value: 0.09
    true_std: 0.004
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.09
    sort_std: 0.004
    is_best: false
  - model: KP-GIN
    model_key: kp-gin
    model_plain: KP-GIN
    value: 0.093
    std: 0.007
    paper_value: 0.093
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Feng 2022
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 55
    true_value: 0.093
    true_std: 0.007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.093
    sort_std: 0.007
    is_best: false
  - model: K-Subgraph SAT
    model_key: k-subgraph sat
    model_plain: K-Subgraph SAT
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
    source_ref: Chen 2022
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 57
    true_value: 0.094
    true_std: 0.008
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.008
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.384
    std: 0.007
    paper_value: 0.384
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Veličković 2017
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
    global_rank: 67
    true_value: 0.111
    true_std: 0.002
    value_gap_source_arxiv: '2301.09505'
    value_gap_source_title: Rethinking the Expressive Power of GNNs via Graph Biconnectivity
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.273
    value_note: ''
    paper_rank: 113
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.111
    sort_std: 0.002
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
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Dec 3, 2023
    date_display: Dec 2023
    date_iso: '2023-12-03'
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
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: TU Dortmund
  datasets:
  - *id002
  - *id003
- benchmark: LRGB
  datasets:
  - *id004
  - *id005
- benchmark: GNNBenchmark
  datasets:
  - *id006
  - *id007
main_figure: /figures/2312.01538/main_figure.png
---

