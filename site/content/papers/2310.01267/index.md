---
title: Cooperative Graph Neural Networks
arxiv_id: '2310.01267'
source_url: ''
authors: []
published_date: Oct 2, 2023
published_date_iso: '2023-10-02'
abstract: 'Graph neural networks are popular architectures for graph machine learning,
  based on iterative computation of node representations of an input graph through
  a series of invariant transformations. A large class of graph neural networks follow
  a standard message-passing paradigm: at every layer, each node state is updated
  based on an aggregate of messages from its neighborhood. In this work, we propose
  a novel framework for training graph neural networks, where every node is viewed
  as a player that can choose to either ''listen'', ''broadcast'', ''listen and broadcast'',
  or to ''isolate''. The standard message propagation scheme can then be viewed as
  a special case of this framework where every node ''listens and broadcasts'' to
  all neighbors. Our approach offers a more flexible and dynamic message-passing paradigm,
  where each node can determine its own strategy based on their state, effectively
  exploring the graph topology while learning. We provide a theoretical analysis of
  the new message-passing scheme which is further supported by an extensive empirical
  analysis on a synthetic dataset and on real-world datasets.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CO-GNN($\Sigma$, $\Sigma$)
- CO-GNN($\mu$, $\mu$)
- CO-GNN(Σ, Σ)
- CO-GNN(μ, μ)
mrr: 0.0317
adjusted_mrr: 0.0317
mrr_dataset_count: 6
benchmark_categories:
- Heterophilic Graphs
- TU Dortmund
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.5417
    std: 0.0037
    paper_value: 0.5417
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 8
    true_value: 0.5417
    true_std: 0.0037
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5417
    sort_std: 0.0037
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
  - model: SAGE
    model_key: sage
    model_plain: SAGE
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 20
    true_value: 0.5363
    true_std: 0.0039
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5363
    sort_std: 0.0039
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.5218
    std: 0.008
    paper_value: 0.5218
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 34
    true_value: 0.527
    true_std: 0.0062
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999982
    value_note: global 0.5270 within std
    paper_rank: 36
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.527
    sort_std: 0.0062
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.5128
    std: 0.0056
    paper_value: 0.5128
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 40
    true_value: 0.5128
    true_std: 0.0056
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5128
    sort_std: 0.0056
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.5117
    std: 0.0066
    paper_value: 0.5117
    paper_std: 0.0066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 43
    true_value: 0.5117
    true_std: 0.0066
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5117
    sort_std: 0.0066
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: ENZYMES
  rows:
  - model: PathNN-P (K=1)
    model_key: pathnn-p (k=1)
    model_plain: PathNN-P (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    model_key: pathnn-\mathcal{p\phantom{s}}\phantom{^+} \, (k=1)
    model_plain: PathNN-\mathcal{P\phantom{S}}\phantom{^+} \, (K=1)
    value: 0.73
    std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.73
    sort_std: 0.052
    is_best: true
  - model: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    model_key: pathnn-\mathcal{sp}\phantom{^+} \, (k=2)
    model_plain: PathNN-\mathcal{SP}\phantom{^+} \, (K=2)
    value: 0.718
    std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.05955'
    title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
    date: Jun 9, 2023
    date_display: Jun 2023
    date_iso: '2023-06-09'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.718
    sort_std: 0.048
    is_best: true
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.694
    std: 0.062
    paper_value: 0.694
    paper_std: 0.062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 6
    true_value: 0.694
    true_std: 0.062
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.694
    sort_std: 0.062
    is_best: true
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.683
    std: 0.057
    paper_value: 0.683
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 10
    true_value: 0.683
    true_std: 0.057
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.683
    sort_std: 0.057
    is_best: true
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.657
    std: 0.049
    paper_value: 0.657
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 12
    true_value: 0.657
    true_std: 0.049
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.657
    sort_std: 0.049
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.596
    std: 0.045
    paper_value: 0.596
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 13
    true_value: 0.606
    true_std: 0.034
    value_gap_source_arxiv: '2601.07419'
    value_gap_source_title: 'Position: Don''t be Afraid of Over-Smoothing And Over-Squashing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010000000000000009
    value_note: global 0.6060 within std
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.606
    sort_std: 0.034
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.595
    std: 0.056
    paper_value: 0.595
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 14
    true_value: 0.595
    true_std: 0.056
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: 0.056
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.582
    std: 0.06
    paper_value: 0.582
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 16
    true_value: 0.582
    true_std: 0.06
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.582
    sort_std: 0.06
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.389
    std: 0.057
    paper_value: 0.389
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 52
    true_value: 0.389
    true_std: 0.057
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.389
    sort_std: 0.057
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.295
    std: 0.082
    paper_value: 0.295
    paper_std: 0.082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 98
    true_value: 0.295
    true_std: 0.082
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.295
    sort_std: 0.082
    is_best: false
  metric: Accuracy
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
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.712
    std: 0.039
    paper_value: 0.712
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 25
    true_value: 0.751
    true_std: 0.051
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.039000000000000035
    value_note: global 0.7510 within std
    paper_rank: 81
    rank_delta: 56
    rank_delta_abs: 56
    rank_delta_direction: worse
    sort_value: 0.751
    sort_std: 0.051
    is_best: false
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.684
    std: 0.033
    paper_value: 0.684
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 46
    true_value: 0.7314
    true_std: 0.007
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0474
    value_note: ''
    paper_rank: 108
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.7314
    sort_std: 0.007
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.722
    std: 0.041
    paper_value: 0.722
    paper_std: 0.041
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 62
    true_value: 0.722
    true_std: 0.041
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.722
    sort_std: 0.041
    is_best: false
  - model: ICGMM_f
    model_key: icgmm_f
    model_plain: ICGMM_f
    value: 0.718
    std: 0.044
    paper_value: 0.718
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 69
    true_value: 0.718
    true_std: 0.044
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.718
    sort_std: 0.044
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.708
    std: 0.033
    paper_value: 0.708
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 90
    true_value: 0.708
    true_std: 0.033
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.708
    sort_std: 0.033
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.692
    std: 0.03
    paper_value: 0.692
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 100
    true_value: 0.7
    true_std: 0.009
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008000000000000007
    value_note: global 0.7000 within std
    paper_rank: 107
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7
    sort_std: 0.009
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 108
    true_value: 0.688
    true_std: 0.045
    value_gap_source_arxiv: '2410.23686'
    value_gap_source_title: Towards Dynamic Message Passing on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.688
    sort_std: 0.045
    is_best: false
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.677
    std: 0.028
    paper_value: 0.677
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 115
    true_value: 0.677
    true_std: 0.028
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.677
    sort_std: 0.028
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
  - model: DiffPool
    model_key: diffpool
    model_plain: DiffPool
    value: 0.456
    std: 0.034
    paper_value: 0.456
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 10
    true_value: 0.56
    true_std: 0.03
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10400000000000004
    value_note: ''
    paper_rank: 68
    rank_delta: 58
    rank_delta_abs: 58
    rank_delta_direction: worse
    sort_value: 0.56
    sort_std: 0.03
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.485
    std: 0.033
    paper_value: 0.485
    paper_std: 0.033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 22
    true_value: 0.523
    true_std: 0.028
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.038000000000000034
    value_note: ''
    paper_rank: 60
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.523
    sort_std: 0.028
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.499
    std: 0.045
    paper_value: 0.499
    paper_std: 0.045
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 42
    true_value: 0.499
    true_std: 0.045
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.499
    sort_std: 0.045
    is_best: false
  - model: ICGMM_f
    model_key: icgmm_f
    model_plain: ICGMM_f
    value: 0.49
    std: 0.038
    paper_value: 0.49
    paper_std: 0.038
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 53
    true_value: 0.49
    true_std: 0.038
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.49
    sort_std: 0.038
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.485
    std: 0.04
    paper_value: 0.485
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 61
    true_value: 0.485
    true_std: 0.04
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.485
    sort_std: 0.04
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.456
    std: 0.034
    paper_value: 0.456
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 66
    true_value: 0.478
    true_std: 0.009
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.021999999999999964
    value_note: global 0.4780 within std
    paper_rank: 68
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.478
    sort_std: 0.009
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
  - model: ECC
    model_key: ecc
    model_plain: ECC
    value: 0.435
    std: 0.031
    paper_value: 0.435
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 73
    true_value: 0.435
    true_std: 0.031
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.435
    sort_std: 0.031
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9201
    std: 0.0068
    paper_value: 0.9201
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 8
    true_value: 0.9773
    true_std: 0.0073
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05719999999999992
    value_note: ''
    paper_rank: 50
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.9773
    sort_std: 0.0073
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.9731
    std: 0.0041
    paper_value: 0.9731
    paper_std: 0.0041
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 14
    true_value: 0.9731
    true_std: 0.0041
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9731
    sort_std: 0.0041
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.9509
    std: 0.0118
    paper_value: 0.9509
    paper_std: 0.0118
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 26
    true_value: 0.9509
    true_std: 0.0118
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9509
    sort_std: 0.0118
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.9229
    std: 0.0047
    paper_value: 0.9229
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 32
    true_value: 0.9391
    true_std: 0.0035
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.016199999999999992
    value_note: ''
    paper_rank: 48
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.9391
    sort_std: 0.0035
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 39
    true_value: 0.9351
    true_std: 0.0057
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9351
    sort_std: 0.0057
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.9185
    std: 0.0076
    paper_value: 0.9185
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 52
    true_value: 0.9185
    true_std: 0.0076
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9185
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id009
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
    global_rank: 3
    sort_value: 0.8583
    sort_std: 0.0086
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.806
    std: 0.011
    paper_value: 0.806
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 31
    true_value: 0.806
    true_std: 0.011
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.806
    sort_std: 0.011
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.794
    std: 0.007
    paper_value: 0.794
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 37
    true_value: 0.794
    true_std: 0.007
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.794
    sort_std: 0.007
    is_best: false
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.786
    std: 0.017
    paper_value: 0.786
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 42
    true_value: 0.786
    true_std: 0.017
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.786
    sort_std: 0.017
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 55
    true_value: 0.769
    true_std: 0.019
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.769
    sort_std: 0.019
    is_best: false
  - model: GSPN
    model_key: gspn
    model_plain: GSPN
    value: 0.766
    std: 0.019
    paper_value: 0.766
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 59
    true_value: 0.766
    true_std: 0.019
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 61
    true_value: 0.764
    true_std: 0.017
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.017
    is_best: false
  - model: ICGMM_f
    model_key: icgmm_f
    model_plain: ICGMM_f
    value: 0.764
    std: 0.014
    paper_value: 0.764
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 62
    true_value: 0.764
    true_std: 0.014
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.014
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 64
    true_value: 0.762
    true_std: 0.014
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.014
    is_best: false
  - model: CGMM
    model_key: cgmm
    model_plain: CGMM
    value: 0.762
    std: 0.02
    paper_value: 0.762
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 65
    true_value: 0.762
    true_std: 0.02
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 31
    true_value: 0.7625
    true_std: 0.01
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.025499999999999967
    value_note: global 0.7625 within std
    paper_rank: 101
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7625
    sort_std: 0.01
    is_best: false
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.029000000000000026
    value_note: global 0.7620 within std
    paper_rank: 110
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: 0.028
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 50
    true_value: 0.755
    true_std: 0.009
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.026000000000000023
    value_note: global 0.7550 within std
    paper_rank: 125
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.755
    sort_std: 0.009
    is_best: false
  - model: SPN(k=5)
    model_key: spn(k=5)
    model_plain: SPN(k=5)
    value: 0.742
    std: 0.027
    paper_value: 0.742
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 85
    true_value: 0.742
    true_std: 0.027
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.742
    sort_std: 0.027
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.731
    std: 0.023
    paper_value: 0.731
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 114
    true_value: 0.731
    true_std: 0.023
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.731
    sort_std: 0.023
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 142
    true_value: 0.723
    true_std: 0.034
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.034
    is_best: false
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.713
    std: 0.02
    paper_value: 0.713
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 161
    true_value: 0.713
    true_std: 0.02
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.713
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Questions
  rows:
  - model: IM-CO-GNN(Σ,Σ)
    model_key: im-co-gnn(σ,σ)
    model_plain: IM-CO-GNN(Σ,Σ)
    value: 0.8049
    std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23185'
    title: Improving the Effective Receptive Field of Message-Passing Neural Networks
    date: May 29, 2025
    date_display: May 2025
    date_iso: '2025-05-29'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.8049
    sort_std: 0.0092
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.8039000000000001
    std: 0.0104
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
    global_rank: 2
    sort_value: 0.8039000000000001
    sort_std: 0.0104
    is_best: true
  - model: Tango<sub>GatedGCN</sub>
    model_key: tango\textsubscript{gatedgcn}
    model_plain: TangoGatedGCN
    value: 0.8039
    std: 0.0104
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.8039
    sort_std: 0.0104
    is_best: true
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.8002
    std: 0.0086
    paper_value: 0.8002
    paper_std: 0.0086
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 6
    true_value: 0.8002
    true_std: 0.0086
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8002
    sort_std: 0.0086
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7609
    std: 0.0127
    paper_value: 0.7609
    paper_std: 0.0127
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 13
    true_value: 0.7902
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029299999999999993
    value_note: ''
    paper_rank: 46
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7902
    sort_std: 0.006
    is_best: true
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.7805
    std: 0.0093
    paper_value: 0.7805
    paper_std: 0.0093
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 21
    true_value: 0.7805
    true_std: 0.0093
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7805
    sort_std: 0.0093
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.7795
    std: 0.0068
    paper_value: 0.7795
    paper_std: 0.0068
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 23
    true_value: 0.7795000000000001
    true_std: 0.0068000000000000005
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795000000000001
    sort_std: 0.0068000000000000005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7743
    std: 0.012
    paper_value: 0.7743
    paper_std: 0.012
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 24
    true_value: 0.7795
    true_std: 0.0051
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999982
    value_note: global 0.7795 within std
    paper_rank: 31
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7795
    sort_std: 0.0051
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.7654
    std: 0.0095
    paper_value: 0.7654
    paper_std: 0.0095
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 42
    true_value: 0.7654000000000001
    true_std: 0.0095
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
    sort_value: 0.7654000000000001
    sort_std: 0.0095
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.7644
    std: 0.0062
    paper_value: 0.7644
    paper_std: 0.0062
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 46
    true_value: 0.7644
    true_std: 0.0062
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7644
    sort_std: 0.0062
    is_best: false
  metric: ROC-AUC
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
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.9157
    std: 0.0032
    paper_value: 0.9157
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 15
    true_value: 0.9157
    true_std: 0.0032
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9157
    sort_std: 0.0032
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.9137
    std: 0.0035
    paper_value: 0.9137
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 17
    true_value: 0.9137
    true_std: 0.0035
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9137
    sort_std: 0.0035
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8087
    std: 0.003
    paper_value: 0.8087
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09760000000000002
    value_note: ''
    paper_rank: 67
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8732
    std: 0.0039
    paper_value: 0.8732
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 32
    true_value: 0.8875
    true_std: 0.0041
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01429999999999998
    value_note: ''
    paper_rank: 36
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8875
    sort_std: 0.0041
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8651
    std: 0.0073
    paper_value: 0.8651
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 44
    true_value: 0.8651000000000001
    true_std: 0.0073
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8651000000000001
    sort_std: 0.0073
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 47
    true_value: 0.8574
    true_std: 0.0067
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8574
    sort_std: 0.0067
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Tolokers
  rows:
  - model: GRAMA<sub>GCN</sub>
    model_key: grama$_{gcn}$
    model_plain: GRAMAGCN
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.8623
    std: 0.011
    metric: ROC-AUC
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8623
    sort_std: 0.011
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8591
    std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
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
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: CO-GNN(\mu, \mu)
    model_key: co-gnn($\mu$, $\mu$)
    model_plain: CO-GNN(\mu, \mu)
    value: 0.8445
    std: 0.0117
    paper_value: 0.8445
    paper_std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 37
    sort_value: 0.8445
    sort_std: 0.0117
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.837
    std: 0.0047
    paper_value: 0.837
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 48
    sort_value: 0.837
    sort_std: 0.0047
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8364
    std: 0.0067
    paper_value: 0.8364
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 44
    sort_value: 0.8364
    sort_std: 0.0067
    is_best: false
  - model: CO-GNN(\Sigma, \Sigma)
    model_key: co-gnn($\sigma$, $\sigma$)
    model_plain: CO-GNN(\Sigma, \Sigma)
    value: 0.8336
    std: 0.0089
    paper_value: 0.8336
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 53
    sort_value: 0.8336
    sort_std: 0.0089
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8323
    std: 0.0064
    paper_value: 0.8323
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 55
    sort_value: 0.8323
    sort_std: 0.0064
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8252
    std: 0.0092
    paper_value: 0.8252
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 45
    sort_value: 0.8252
    sort_std: 0.0092
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8243
    std: 0.0044
    paper_value: 0.8243
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
    date: Oct 2, 2023
    date_display: Oct 2023
    date_iso: '2023-10-02'
    global_rank: 61
    sort_value: 0.8243
    sort_std: 0.0044
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
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
  - *id010
main_figure: /figures/2310.01267/main_figure.png
---

