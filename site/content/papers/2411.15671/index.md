---
title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
arxiv_id: '2411.15671'
source_url: ''
authors: []
published_date: Nov 2024
published_date_iso: 2024-11
abstract: 'Modern sequence models (e.g., Transformers, linear RNNs, etc.) emerged
  as dominant backbones of recent deep learning frameworks, mainly due to their efficiency,
  representational power, and/or ability to capture long-range dependencies. Adopting
  these sequence models for graph-structured data has recently gained popularity as
  the alternative to Message Passing Neural Networks (MPNNs). There is, however, a
  lack of a common foundation about what constitutes a good graph sequence model,
  and a mathematical description of the benefits and deficiencies in adopting different
  sequence models for learning on graphs. To this end, we first present Graph Sequence
  Model (GSM), a unifying framework for adopting sequence models for graphs, consisting
  of three main steps: (1) Tokenization, which translates the graph into a set of
  sequences; (2) Local Encoding, which encodes local neighborhoods around each node;
  and (3) Global Encoding, which employs a scalable sequence model to capture long-range
  dependencies within the sequences. This framework allows us to understand, evaluate,
  and compare the power of different sequence model backbones in graph tasks. Our
  theoretical evaluations of the representation power of Transformers and modern recurrent
  models through the lens of global and local graph tasks show that there are both
  negative and positive sides for both types of models. Building on this observation,
  we present GSM++, a fast hybrid model that uses the Hierarchical Affinity Clustering
  (HAC) algorithm to tokenize the graph into hierarchical sequences, and then employs
  a hybrid architecture of Transformer to encode these sequences. Our theoretical
  and experimental results support the design of GSM++, showing that GSM++ outperforms
  baselines in most benchmark evaluations.'
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
paper_type: method
proposed_models:
- GSM++ (BFS)
- GSM++ (DFS)
- GSM++ (MoT)
mrr: 0.0817
adjusted_mrr: 0.0817
mrr_dataset_count: 7
benchmark_categories:
- Heterophilic Graphs
- TU Dortmund
- GNNBenchmark
- Other Graph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id002
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
    value: 0.527
    std: 0.0062
    paper_value: 0.527
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02839999999999998
    value_note: ''
    paper_rank: 33
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.5554
    sort_std: 0.0051
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.5363
    std: 0.0039
    paper_value: 0.5363
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 3
    true_value: 0.554
    true_std: 0.0021
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01770000000000005
    value_note: ''
    paper_rank: 19
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
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
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.5458
    std: 0.0036
    metric: Accuracy
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
    global_rank: 5
    sort_value: 0.5458
    sort_std: 0.0036
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.5327
    std: 0.003
    paper_value: 0.5327
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 11
    true_value: 0.5407
    true_std: 0.0031
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008000000000000007
    value_note: ''
    paper_rank: 24
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.5407
    sort_std: 0.0031
    is_best: false
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.539
    std: 0.0104
    paper_value: 0.539
    paper_std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 14
    true_value: 0.539
    true_std: 0.0104
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.539
    sort_std: 0.0104
    is_best: false
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.5381
    std: 0.0035
    paper_value: 0.5381
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 16
    true_value: 0.5381
    true_std: 0.0035
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5381
    sort_std: 0.0035
    is_best: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
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
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.5361
    std: 0.0029
    paper_value: 0.5361
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 21
    true_value: 0.5361
    true_std: 0.0029
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5361
    sort_std: 0.0029
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.5351
    std: 0.0046
    paper_value: 0.5351
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 22
    true_value: 0.5351
    true_std: 0.0046
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5351
    sort_std: 0.0046
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.531
    std: 0.0042
    paper_value: 0.531
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 29
    true_value: 0.531
    true_std: 0.0042
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.531
    sort_std: 0.0042
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.5126
    std: 0.0072
    paper_value: 0.5126
    paper_std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 42
    true_value: 0.5126
    true_std: 0.0072
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5126
    sort_std: 0.0072
    is_best: false
  - model: tGNN
    model_key: tgnn
    model_plain: tGNN
    value: 0.4821
    std: 0.0053
    paper_value: 0.4821
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 61
    true_value: 0.4821
    true_std: 0.0053
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4821
    sort_std: 0.0053
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.43
    std: 0.0032
    paper_value: 0.43
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 64
    true_value: 0.481
    true_std: 0.0071
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05099999999999999
    value_note: ''
    paper_rank: 84
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.481
    sort_std: 0.0071
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.4784
    std: 0.0065
    paper_value: 0.4784
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 67
    true_value: 0.4784
    true_std: 0.0065
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4784
    sort_std: 0.0065
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.4729
    std: 0.0065
    paper_value: 0.4729
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 70
    true_value: 0.4729
    true_std: 0.0065
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4729
    sort_std: 0.0065
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.4461
    std: 0.005
    paper_value: 0.4461
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 79
    true_value: 0.4461
    true_std: 0.005
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4461
    sort_std: 0.005
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4386
    std: 0.0035
    paper_value: 0.4386
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 82
    true_value: 0.4386
    true_std: 0.0035
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4386
    sort_std: 0.0035
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.7781
    std: 0.0028
    paper_value: 0.7781
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 10
    true_value: 0.7781
    true_std: 0.0028
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7781
    sort_std: 0.0028
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6731
    std: 0.0031
    paper_value: 0.6731
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 12
    true_value: 0.77218
    true_std: 0.00381
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09907999999999995
    value_note: ''
    paper_rank: 105
    rank_delta: 93
    rank_delta_abs: 93
    rank_delta_direction: worse
    sort_value: 0.77218
    sort_std: 0.00381
    is_best: false
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.7692
    std: 0.0031
    paper_value: 0.7692
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 14
    true_value: 0.7692
    true_std: 0.0031
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7692
    sort_std: 0.0031
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.7685
    std: 0.0019
    paper_value: 0.7685
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 15
    true_value: 0.76853
    true_std: 0.00185
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 3.0000000000085514e-05
    value_note: global 0.7685 within std
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76853
    sort_std: 0.00185
    is_best: false
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.7659
    std: 0.0024
    paper_value: 0.7659
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 18
    true_value: 0.7659
    true_std: 0.0024
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7659
    sort_std: 0.0024
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.7646
    std: 0.0088
    paper_value: 0.7646
    paper_std: 0.0088
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 20
    true_value: 0.76468
    true_std: 0.00881
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 8.000000000008001e-05
    value_note: global 0.7647 within std
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
    value: 0.7444
    std: 0.0009
    paper_value: 0.7444
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 30
    true_value: 0.7576
    true_std: 0.0042
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0132000000000001
    value_note: ''
    paper_rank: 37
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7576
    sort_std: 0.0042
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7469
    std: 0.0013
    paper_value: 0.7469
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 36
    true_value: 0.74754
    true_std: 0.00194
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006399999999999739
    value_note: global 0.7475 within std
    paper_rank: 37
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.74754
    sort_std: 0.00194
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.7226
    std: 0.0031
    paper_value: 0.7226
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 57
    true_value: 0.72356
    true_std: 0.0032300000000000002
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009599999999999609
    value_note: global 0.7236 within std
    paper_rank: 63
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.72356
    sort_std: 0.0032300000000000002
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.7048
    std: 0.001
    paper_value: 0.7048
    paper_std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 85
    true_value: 0.7048
    true_std: 0.001
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7048
    sort_std: 0.001
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5571
    std: 0.0038
    paper_value: 0.5571
    paper_std: 0.0038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 95
    true_value: 0.69824
    true_std: 0.00413
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14113999999999993
    value_note: ''
    paper_rank: 114
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.69824
    sort_std: 0.00413
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.5526
    std: 0.0152
    paper_value: 0.5526
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 97
    true_value: 0.69592
    true_std: 0.00287
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14332
    value_note: ''
    paper_rank: 115
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.69592
    sort_std: 0.00287
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.6901
    std: 0.0259
    paper_value: 0.6901
    paper_std: 0.0259
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 100
    true_value: 0.69013
    true_std: 0.00259
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.6901 within std
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69013
    sort_std: 0.00259
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.6577
    std: 0.003
    paper_value: 0.6577
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 106
    true_value: 0.6577
    true_std: 0.003
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6577
    sort_std: 0.003
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6422
    std: 0.0046
    paper_value: 0.6422
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 110
    true_value: 0.64223
    true_std: 0.00455
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.6422 within std
    paper_rank: 111
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.64223
    sort_std: 0.00455
    is_best: false
  - model: SPN
    model_key: spn
    model_plain: SPN
    value: 0.3722
    std: 0.0827
    paper_value: 0.3722
    paper_std: 0.0827
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 118
    true_value: 0.3722
    true_std: 0.0827
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3722
    sort_std: 0.0827
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: D&D
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.989
    std: null
    paper_value: 0.989
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 1
    true_value: 0.989
    true_std: null
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.989
    sort_std: null
    is_best: true
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
    value: 0.981
    std: null
    paper_value: 0.981
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 2
    true_value: 0.981
    true_std: null
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
    value: 0.976
    std: null
    paper_value: 0.976
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 3
    true_value: 0.976
    true_std: null
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: S4 + SPT
    model_key: s4 + spt
    model_plain: S4 + SPT
    value: 0.9509
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02980'
    title: 'Never Train from Scratch: Fair Comparison of long-sequence models requires
      data-driven priors'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9509
    sort_std: null
    is_best: false
  - model: S4
    model_key: s4
    model_plain: S4
    value: 0.936
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.02980'
    title: 'Never Train from Scratch: Fair Comparison of long-sequence models requires
      data-driven priors'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.936
    sort_std: null
    is_best: false
  - model: SubdivNet
    model_key: subdivnet
    model_plain: SubdivNet
    value: 0.917
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.04821'
    title: E(3)-Equivariant Mesh Neural Networks
    date: Feb 7, 2024
    date_display: Feb 2024
    date_iso: '2024-02-07'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.917
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.364
    std: null
    paper_value: 0.364
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 38
    true_value: 0.7556
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.39160000000000006
    value_note: ''
    paper_rank: 72
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.7556
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.093
    std: null
    paper_value: 0.093
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 39
    true_value: 0.7546
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.6616000000000001
    value_note: ''
    paper_rank: 77
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.7546
    sort_std: null
    is_best: false
  - model: HAC (DFS)
    model_key: hac (dfs)
    model_plain: HAC (DFS)
    value: 0.31
    std: null
    paper_value: 0.31
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 73
    true_value: 0.31
    true_std: null
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31
    sort_std: null
    is_best: false
  - model: Node
    model_key: node
    model_plain: Node
    value: 0.299
    std: null
    paper_value: 0.299
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 74
    true_value: 0.299
    true_std: null
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.299
    sort_std: null
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.298
    std: null
    paper_value: 0.298
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 75
    true_value: 0.298
    true_std: null
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.298
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
    paper_value: 0.9884
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 2
    true_value: 0.9884
    true_std: 0.0015
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    value: 0.9734
    std: 0.0014
    paper_value: 0.9734
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 4
    true_value: 0.98712
    true_std: 0.00137
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013719999999999954
    value_note: ''
    paper_rank: 80
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.98712
    sort_std: 0.00137
    is_best: false
  - model: PPGT
    model_key: ppgt
    model_plain: PPGT
    value: 0.98614
    std: 0.00096
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
    global_rank: 5
    sort_value: 0.98614
    sort_std: 0.00096
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9855
    std: 0.0003
    paper_value: 0.9855
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 10
    true_value: 0.9855
    true_std: 0.00039
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9855
    sort_std: 0.00039
    is_best: false
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.9848
    std: 0.0012
    paper_value: 0.9848
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 15
    true_value: 0.9848
    true_std: 0.0012
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9848
    sort_std: 0.0012
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.9783
    std: 0.002
    paper_value: 0.9783
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 24
    true_value: 0.98391
    true_std: 0.00182
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.005610000000000004
    value_note: ''
    paper_rank: 75
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.98391
    sort_std: 0.00182
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.9838
    std: 0.0002
    paper_value: 0.9838
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 25
    true_value: 0.98383
    true_std: 0.00012
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.999999999997449e-05
    value_note: global 0.9838 within std
    paper_rank: 26
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.98383
    sort_std: 0.00012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9071
    std: 0.0021
    paper_value: 0.9071
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 26
    true_value: 0.98382
    true_std: 0.00095
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07672000000000001
    value_note: ''
    paper_rank: 100
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.98382
    sort_std: 0.00095
    is_best: false
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.9829
    std: 0.0014
    paper_value: 0.9829
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 31
    true_value: 0.9829
    true_std: 0.0014
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9829
    sort_std: 0.0014
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.9649
    std: 0.0025
    paper_value: 0.9649
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 32
    true_value: 0.98285
    true_std: 0.00103
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01795000000000002
    value_note: ''
    paper_rank: 88
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.98285
    sort_std: 0.00103
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.9817
    std: 0.0001
    paper_value: 0.9817
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 45
    true_value: 0.9817
    true_std: 0.0001
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9817
    sort_std: 0.0001
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.9811
    std: 0.0011
    paper_value: 0.9811
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 54
    true_value: 0.9811
    true_std: 0.0011
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9811
    sort_std: 0.0011
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.981
    std: 0.0011
    paper_value: 0.981
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 57
    true_value: 0.98108
    true_std: 0.00111
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 7.999999999996898e-05
    value_note: global 0.9811 within std
    paper_rank: 59
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.98108
    sort_std: 0.00111
    is_best: false
  - model: CRaWl
    model_key: crawl
    model_plain: CRaWl
    value: 0.9794
    std: 0.05
    paper_value: 0.9794
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 73
    true_value: 0.97944
    true_std: 0.0005
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 3.999999999992898e-05
    value_note: global 0.9794 within std
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.97944
    sort_std: 0.0005
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9731
    std: 0.0009
    paper_value: 0.9731
    paper_std: 0.0009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 82
    true_value: 0.97312
    true_std: 0.00097
    value_gap_source_arxiv: '2407.02758'
    value_gap_source_title: Differential Encoding for Improved Representation Learning
      over Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.9731 within std
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.97312
    sort_std: 0.00097
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9554
    std: 0.0021
    paper_value: 0.9554
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 92
    true_value: 0.9554
    true_std: 0.0021
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9554
    sort_std: 0.0021
    is_best: false
  - model: SPN
    model_key: spn
    model_plain: SPN
    value: 0.8331
    std: 0.0446
    paper_value: 0.8331
    paper_std: 0.0446
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 103
    true_value: 0.8331
    true_std: 0.0446
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8331
    sort_std: 0.0446
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
    value: 0.9223
    std: 0.0065
    paper_value: 0.9223
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 2
    true_value: 0.946
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.023699999999999943
    value_note: ''
    paper_rank: 19
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.946
    sort_std: 0.0057
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9437
    std: 0.0058
    paper_value: 0.9437
    paper_std: 0.0058
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 3
    true_value: 0.9437
    true_std: 0.0058
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9437
    sort_std: 0.0058
    is_best: true
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.9417
    std: 0.002
    paper_value: 0.9417
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 4
    true_value: 0.9417
    true_std: 0.002
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9417
    sort_std: 0.002
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.9352
    std: 0.0036
    paper_value: 0.9352
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 5
    true_value: 0.9415
    true_std: 0.002
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006299999999999972
    value_note: ''
    paper_rank: 12
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.9415
    sort_std: 0.002
    is_best: false
  - model: GSSC
    model_key: gssc
    model_plain: GSSC
    value: 0.9406
    std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09263'
    title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures
      Meet Excellence
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    sort_value: 0.9406
    sort_std: 0.0064
    is_best: true
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9402
    std: 0.002
    paper_value: 0.9402
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 7
    true_value: 0.9402
    true_std: 0.0021
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
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
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.9389
    std: 0.0024
    paper_value: 0.9389
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 8
    true_value: 0.9389
    true_std: 0.0024
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9389
    sort_std: 0.0024
    is_best: false
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.9372
    std: 0.0029
    metric: Accuracy
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
    global_rank: 9
    sort_value: 0.9372
    sort_std: 0.0029
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.81
    std: 0.0
    paper_value: 0.81
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 12
    true_value: 0.9354
    true_std: 0.0045
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12539999999999996
    value_note: ''
    paper_rank: 21
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.9354
    sort_std: 0.0045
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8898
    std: 0.0055
    paper_value: 0.8898
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 16
    true_value: 0.9325
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04269999999999996
    value_note: ''
    paper_rank: 20
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.9325
    sort_std: 0.004
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.9298
    std: 0.0047
    paper_value: 0.9298
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 18
    true_value: 0.9298
    true_std: 0.0047
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9298
    sort_std: 0.0047
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.9234
    std: 0.0034
    paper_value: 0.9234
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 19
    true_value: 0.9234
    true_std: 0.0034
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9234
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8509
    std: 0.0025
    paper_value: 0.8509
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 20
    true_value: 0.921
    true_std: 0.0024
    value_gap_source_arxiv: '2502.00282'
    value_gap_source_title: 'GraphMinNet: Learning Dependencies in Graphs with Light
      Complexity Minimal Architecture'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07010000000000005
    value_note: ''
    paper_rank: 21
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.921
    sort_std: 0.0024
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.873
    std: 0.0002
    paper_value: 0.873
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 21
    true_value: 0.873
    true_std: 0.0002
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.873
    sort_std: 0.0002
    is_best: false
  - model: SPN
    model_key: spn
    model_plain: SPN
    value: 0.6407
    std: 0.0581
    paper_value: 0.6407
    paper_std: 0.0581
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 22
    true_value: 0.6407
    true_std: 0.0581
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6407
    sort_std: 0.0581
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9906999999999999
    std: 0.0025
    metric: ROC-AUC
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
    global_rank: 1
    sort_value: 0.9906999999999999
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    global_rank: 2
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango<sub>GPS</sub>
    model_key: tango\textsubscript{gps}
    model_plain: TangoGPS
    value: 0.9839
    std: 0.0054
    metric: ROC-AUC
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
    global_rank: 3
    sort_value: 0.9839
    sort_std: 0.0054
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8975
    std: 0.0052
    paper_value: 0.8975
    paper_std: 0.0052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 5
    true_value: 0.9786
    true_std: 0.0024
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08110000000000006
    value_note: ''
    paper_rank: 76
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.9786
    sort_std: 0.0024
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9351
    std: 0.0057
    paper_value: 0.9351
    paper_std: 0.0057
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 7
    true_value: 0.9777
    true_std: 0.0062
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04259999999999997
    value_note: ''
    paper_rank: 38
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.9777
    sort_std: 0.0062
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9391
    std: 0.0035
    paper_value: 0.9391
    paper_std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 8
    true_value: 0.9773
    true_std: 0.0073
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0381999999999999
    value_note: ''
    paper_rank: 31
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9773
    sort_std: 0.0073
    is_best: false
  - model: tGNN
    model_key: tgnn
    model_plain: tGNN
    value: 0.9193
    std: 0.0077
    paper_value: 0.9193
    paper_std: 0.0077
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 51
    true_value: 0.9193
    true_std: 0.0077
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9193
    sort_std: 0.0077
    is_best: false
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9149
    std: 0.0111
    paper_value: 0.9149
    paper_std: 0.0111
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 56
    true_value: 0.9149
    true_std: 0.0111
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9149
    sort_std: 0.0111
    is_best: false
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.9145
    std: 0.0036
    paper_value: 0.9145
    paper_std: 0.0036
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 57
    true_value: 0.9145
    true_std: 0.0036
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9145
    sort_std: 0.0036
    is_best: false
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.9109
    std: 0.0098
    paper_value: 0.9109
    paper_std: 0.0098
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 60
    true_value: 0.9109
    true_std: 0.0098
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9109
    sort_std: 0.0098
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.8992
    std: 0.0063
    paper_value: 0.8992
    paper_std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 63
    true_value: 0.9101
    true_std: 0.0023
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01090000000000002
    value_note: ''
    paper_rank: 74
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.9101
    sort_std: 0.0023
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.9089
    std: 0.0058
    paper_value: 0.9089
    paper_std: 0.0058
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 64
    true_value: 0.9089
    true_std: 0.0058
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9089
    sort_std: 0.0058
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9074
    std: 0.0053
    paper_value: 0.9074
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 67
    true_value: 0.9074
    true_std: 0.0053
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9074
    sort_std: 0.0053
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.9063
    std: 0.0067
    paper_value: 0.9063
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 68
    true_value: 0.9063
    true_std: 0.0067
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9063
    sort_std: 0.0067
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8754
    std: 0.0122
    paper_value: 0.8754
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 69
    true_value: 0.905
    true_std: 0.0016
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02960000000000007
    value_note: ''
    paper_rank: 83
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.905
    sort_std: 0.0016
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8419
    std: 0.0066
    paper_value: 0.8419
    paper_std: 0.0066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 70
    true_value: 0.903
    true_std: 0.0006
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06110000000000004
    value_note: ''
    paper_rank: 86
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.903
    sort_std: 0.0006
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8671
    std: 0.0088
    paper_value: 0.8671
    paper_std: 0.0088
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 83
    true_value: 0.8771
    true_std: 0.0069
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.010000000000000009
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8771
    sort_std: 0.0069
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8109
    std: 0.0102
    paper_value: 0.8109
    paper_std: 0.0102
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 88
    true_value: 0.8109
    true_std: 0.0102
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8109
    sort_std: 0.0102
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.8058
    std: 0.0108
    paper_value: 0.8058
    paper_std: 0.0108
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 89
    true_value: 0.8058
    true_std: 0.0108
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8058
    sort_std: 0.0108
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id007
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
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.8793
    std: 0.0015
    paper_value: 0.8793
    paper_std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 6
    true_value: 0.8793
    true_std: 0.0015
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8793
    sort_std: 0.0015
    is_best: false
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.8738
    std: 0.0014
    paper_value: 0.8738
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 12
    true_value: 0.8738
    true_std: 0.0014
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8738
    sort_std: 0.0014
    is_best: false
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.8731
    std: 0.0008
    paper_value: 0.8731
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 14
    true_value: 0.8731
    true_std: 0.0008
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8731
    sort_std: 0.0008
    is_best: false
  - model: GRIT
    model_key: grit
    model_plain: GRIT
    value: 0.8719
    std: 0.0008
    paper_value: 0.8719
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 20
    true_value: 0.87196
    true_std: 0.00076
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 5.999999999994898e-05
    value_note: global 0.8720 within std
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
    value: 0.8649
    std: 0.0019
    paper_value: 0.8649
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 22
    true_value: 0.8714
    true_std: 0.0012
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00649999999999995
    value_note: ''
    paper_rank: 68
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.8714
    sort_std: 0.0012
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8557
    std: 0.0008
    paper_value: 0.8557
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 25
    true_value: 0.87029
    true_std: 0.00037
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014589999999999992
    value_note: ''
    paper_rank: 79
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.87029
    sort_std: 0.00037
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7189
    std: 0.0033
    paper_value: 0.7189
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 26
    true_value: 0.87021
    true_std: 0.00095
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15131000000000006
    value_note: ''
    paper_rank: 89
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.87021
    sort_std: 0.00095
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.8701
    std: 0.0018
    paper_value: 0.8701
    paper_std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 28
    true_value: 0.8701
    true_std: 0.0018
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8701
    sort_std: 0.0018
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.8539
    std: 0.0013
    paper_value: 0.8539
    paper_std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 40
    true_value: 0.86842
    true_std: 0.00048
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.014519999999999977
    value_note: ''
    paper_rank: 80
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.86842
    sort_std: 0.00048
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.8675
    std: 0.0002
    paper_value: 0.8675
    paper_std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 47
    true_value: 0.8676
    true_std: 0.02
    value_gap_source_arxiv: '2402.08678'
    value_gap_source_title: 'Graph Mamba: Towards Learning on Graphs with State Space
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 9.999999999998899e-05
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
    value: 0.867
    std: 0.0003
    paper_value: 0.867
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 48
    true_value: 0.86742
    true_std: 0.00015
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00041999999999997595
    value_note: ''
    paper_rank: 53
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.86742
    sort_std: 0.00015
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.8664
    std: 0.0011
    paper_value: 0.8664
    paper_std: 0.0011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 56
    true_value: 0.86688
    true_std: 0.00073
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00048000000000003595
    value_note: global 0.8669 within std
    paper_rank: 62
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.86688
    sort_std: 0.00073
    is_best: false
  - model: SPN
    model_key: spn
    model_plain: SPN
    value: 0.8657
    std: 0.0014
    paper_value: 0.8657
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 68
    true_value: 0.8657
    true_std: 0.0014
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8657
    sort_std: 0.0014
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8644
    std: 0.0003
    paper_value: 0.8644
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 69
    true_value: 0.8644
    true_std: 0.0003
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8644
    sort_std: 0.0003
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8639
    std: 0.0021
    paper_value: 0.8639
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 70
    true_value: 0.8639
    true_std: 0.0021
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8639
    sort_std: 0.0021
    is_best: false
  - model: GPS + BigBird
    model_key: gps + bigbird
    model_plain: GPS + BigBird
    value: 0.86
    std: 0.0014
    paper_value: 0.86
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 73
    true_value: 0.86
    true_std: 0.0014
    value_gap_source_arxiv: '2402.00789'
    value_gap_source_title: 'Graph-Mamba: Towards Long-Range Graph Sequence Modeling
      with Selective State Spaces'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.0014
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7827
    std: 0.0019
    paper_value: 0.7827
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 88
    true_value: 0.78271
    true_std: 0.00186
    value_gap_source_arxiv: '2605.05689'
    value_gap_source_title: 'GCCM: Enhancing Generative Graph Prediction via Contrastive
      Consistency Model'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 1.0000000000065512e-05
    value_note: global 0.7827 within std
    paper_rank: 89
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.78271
    sort_std: 0.00186
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.5049
    std: 0.0001
    paper_value: 0.5049
    paper_std: 0.0001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 91
    true_value: 0.50492
    true_std: 1.0e-05
    value_gap_source_arxiv: '2404.09774'
    value_gap_source_title: 'RandAlign: A Parameter-Free Method for Regularizing Graph
      Convolutional Networks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 2.0000000000020002e-05
    value_note: global 0.5049 within std
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.50492
    sort_std: 1.0e-05
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Roman-empire
  rows:
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9292
    std: 0.0036
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
    global_rank: 1
    sort_value: 0.9292
    sort_std: 0.0036
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9266
    std: 0.006
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
    sort_value: 0.9266
    sort_std: 0.006
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9262999999999999
    std: 0.005
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
    global_rank: 3
    sort_value: 0.9262999999999999
    sort_std: 0.005
    is_best: true
  - model: GSM++ (MoT)
    model_key: gsm++ (mot)
    model_plain: GSM++ (MoT)
    value: 0.9177
    std: 0.004
    paper_value: 0.9177
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 12
    true_value: 0.9177
    true_std: 0.004
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9177
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7369
    std: 0.0074
    paper_value: 0.7369
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17579999999999996
    value_note: ''
    paper_rank: 79
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: GSM++ (DFS)
    model_key: gsm++ (dfs)
    model_plain: GSM++ (DFS)
    value: 0.9124
    std: 0.0023
    paper_value: 0.9124
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 20
    true_value: 0.9124
    true_std: 0.0023
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9124
    sort_std: 0.0023
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8574
    std: 0.0067
    paper_value: 0.8574
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 23
    true_value: 0.9106
    true_std: 0.0027
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.053199999999999914
    value_note: ''
    paper_rank: 46
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.9106
    sort_std: 0.0027
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7973
    std: 0.0039
    paper_value: 0.7973
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10899999999999999
    value_note: ''
    paper_rank: 74
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: GSM++ (BFS)
    model_key: gsm++ (bfs)
    model_plain: GSM++ (BFS)
    value: 0.9003
    std: 0.0087
    paper_value: 0.9003
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 27
    true_value: 0.9003
    true_std: 0.0087
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9003
    sort_std: 0.0087
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8903
    std: 0.0037
    paper_value: 0.8903
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 31
    true_value: 0.8903
    true_std: 0.0037
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8903
    sort_std: 0.0037
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.8219
    std: 0.0012
    paper_value: 0.8219
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 36
    true_value: 0.8769
    true_std: 0.005
    value_gap_source_arxiv: '2602.18837'
    value_gap_source_title: 'L2G-Net: Local to Global Spectral Graph Neural Networks
      via Cauchy Factorizations'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05500000000000005
    value_note: ''
    paper_rank: 65
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.8769
    sort_std: 0.005
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.82
    std: 0.0061
    paper_value: 0.82
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 38
    true_value: 0.8704000000000001
    true_std: 0.0058
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05040000000000011
    value_note: ''
    paper_rank: 66
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
    sort_value: 0.8704000000000001
    sort_std: 0.0058
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7446
    std: 0.0054
    paper_value: 0.7446
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 63
    true_value: 0.833
    true_std: 0.0079
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08839999999999992
    value_note: ''
    paper_rank: 79
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.833
    sort_std: 0.0079
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7434
    std: 0.0077
    paper_value: 0.7434
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 72
    true_value: 0.8
    true_std: 0.0043
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056600000000000095
    value_note: ''
    paper_rank: 79
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8
    sort_std: 0.0043
    is_best: false
  - model: tGNN
    model_key: tgnn
    model_plain: tGNN
    value: 0.7995
    std: 0.0075
    paper_value: 0.7995
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 73
    true_value: 0.7995
    true_std: 0.0075
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7995
    sort_std: 0.0075
    is_best: false
  - model: DIFFormer
    model_key: difformer
    model_plain: DIFFormer
    value: 0.791
    std: 0.0032
    paper_value: 0.791
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
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 75
    true_value: 0.791
    true_std: 0.0032
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.0032
    is_best: false
  - model: OrderedGNN
    model_key: orderedgnn
    model_plain: OrderedGNN
    value: 0.7768
    std: 0.0039
    paper_value: 0.7768
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 77
    true_value: 0.7768
    true_std: 0.0039
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7768
    sort_std: 0.0039
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.6449
    std: 0.0073
    paper_value: 0.6449
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 78
    true_value: 0.7483
    true_std: 0.0081
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10339999999999994
    value_note: ''
    paper_rank: 87
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.7483
    sort_std: 0.0081
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7159
    std: 0.0125
    paper_value: 0.7159
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Nov 2024
    date_display: Nov 2024
    date_iso: 2024-11
    global_rank: 81
    true_value: 0.7159
    true_std: 0.0125
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
    sort_value: 0.7159
    sort_std: 0.0125
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
- benchmark: GNNBenchmark
  datasets:
  - *id005
  - *id006
  - *id007
- benchmark: Other Graph Benchmarks
  datasets:
  - *id008
main_figure: /figures/2411.15671/main_figure.png
---

