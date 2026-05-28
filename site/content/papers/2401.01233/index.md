---
title: 'GEN: A Practical Alternative to Graph Transformers for Long-Range Graph Modeling'
arxiv_id: '2401.01233'
source_url: ''
authors: []
published_date: Jan 2024
published_date_iso: 2024-01
abstract: Message Passing Neural Networks (MPNNs) model local relations effectively
  but struggle to propagate information over long distances. Graph Transformers (GTs)
  mitigate this via global self-attention, yet their quadratic cost in the number
  of nodes limits scalability. We propose Graph Elimination Networks (GENs), an MPNN
  variant that approximates GT–like long-range modeling while maintaining high efficiency.
  GENs combine edge-wise and hop-wise self-attention in parallel; their multiplicative
  composition yields an attention kernel separable across edge and hop factors within
  a bounded $K$-hop receptive field. To enable hop-wise attention, we introduce the
  Graph Elimination Algorithm (GEA), which prevents double counting across hops, ensuring
  that each round injects the $k$-hop incremental contribution exactly once. Taking
  differences between successive rounds recovers the $k$-hop increment and yields
  disentangled multi-hop features as inputs for hop-wise attention. This preserves
  clearer structural distinctions across hop distances and enables more faithful modeling
  of pairwise dependencies between distant nodes within the $K$-hop neighborhood.
  On the Long-Range Graph Benchmark (LRGB), GENs outperform strong MPNN baselines
  by 7.7 and 6.0 percentage points (pp) on PascalVOC-SP and COCO-SP, and achieve performance
  on par with or better than state-of-the-art Graph Transformers. On OGBN-Products,
  GENs support full-batch training/inference, while sparse-attention baselines like
  Exphormer struggle with memory limits under comparable budgets, highlighting GENs
  as a practical alternative for large, sparse graphs. Our code is available at https://github.com/tmp488598/Graph-Elimination-NetworksURL.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GENs
- GENs+RWSE
- GENs+LapPE
- GEN w/o HA
- GEN w/o EA
mrr: 0.1736
adjusted_mrr: 0.1736
mrr_dataset_count: 18
benchmark_categories:
- Classic
- Heterophilic Graphs
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
- &id005
  dataset: Amazon-Photo
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9712
    std: 0.0024
    paper_value: 0.9712
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 1
    true_value: 0.9712
    true_std: 0.0024
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9712
    sort_std: 0.0024
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9678
    std: 0.0023
    paper_value: 0.9678
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 2
    true_value: 0.9678
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9678
    sort_std: 0.0023
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.966
    std: 0.0033
    paper_value: 0.966
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 3
    true_value: 0.966
    true_std: 0.0033
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.966
    sort_std: 0.0033
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9657
    std: 0.0023
    paper_value: 0.9657
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 4
    true_value: 0.9657
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9657
    sort_std: 0.0023
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.9614
    std: 0.0016
    paper_value: 0.9614
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 5
    true_value: 0.9614
    true_std: 0.0016
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9614
    sort_std: 0.0016
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.961
    std: 0.0046
    paper_value: 0.961
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 6
    true_value: 0.961
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.961
    sort_std: 0.0046
    is_best: false
  - model: CARIBOU
    model_key: caribou
    model_plain: CARIBOU
    value: 0.958
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.22727'
    title: Convergent Privacy Framework for Multi-layer GNNs through Contractive Message
      Passing
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.958
    sort_std: null
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.9569
    std: 0.0039
    paper_value: 0.9569
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 8
    true_value: 0.9569
    true_std: 0.0039
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9569
    sort_std: 0.0039
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.9558
    std: 0.0036
    paper_value: 0.9558
    paper_std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 9
    true_value: 0.9558
    true_std: 0.0036
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9558
    sort_std: 0.0036
    is_best: false
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.9552
    std: 0.0052
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
    global_rank: 10
    sort_value: 0.9552
    sort_std: 0.0052
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.9548
    std: 0.0032
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
    global_rank: 11
    sort_value: 0.9548
    sort_std: 0.0032
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.9343
    std: 0.0056
    paper_value: 0.9343
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 16
    true_value: 0.9527
    true_std: 0.0022
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.018399999999999972
    value_note: ''
    paper_rank: 30
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.9527
    sort_std: 0.0022
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.9489
    std: 0.0014
    paper_value: 0.9489
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 18
    true_value: 0.9489
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9489
    sort_std: 0.0014
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.9433
    std: 0.0021
    paper_value: 0.9433
    paper_std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 24
    true_value: 0.9433
    true_std: 0.0021
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9433
    sort_std: 0.0021
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: Amazon-ratings
  rows:
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.5592
    std: 0.0043
    paper_value: 0.5592
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 1
    true_value: 0.5592
    true_std: 0.0043
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5592
    sort_std: 0.0043
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5492
    std: 0.0061
    paper_value: 0.5492
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006199999999999983
    value_note: ''
    paper_rank: 4
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.5554
    sort_std: 0.0051
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.554
    std: 0.0021
    paper_value: 0.554
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 3
    true_value: 0.554
    true_std: 0.0021
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.554
    sort_std: 0.0021
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.5496
    std: 0.0222
    paper_value: 0.5496
    paper_std: 0.0222
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 4
    true_value: 0.5496
    true_std: 0.0222
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: IM-CO-GNN(μ,μ)
    model_key: im-co-gnn(μ,μ)
    model_plain: IM-CO-GNN(μ,μ)
    value: 0.5443
    std: 0.0041
    metric: Accuracy
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
    global_rank: 6
    sort_value: 0.5443
    sort_std: 0.0041
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.542
    std: 0.0034000000000000002
    metric: Accuracy
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
    global_rank: 7
    sort_value: 0.542
    sort_std: 0.0034000000000000002
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.5414
    std: 0.02
    paper_value: 0.5414
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 10
    true_value: 0.5414
    true_std: 0.02
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5414
    sort_std: 0.02
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.538
    std: 0.0
    paper_value: 0.538
    paper_std: 0.0
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 17
    true_value: 0.538
    true_std: 0.0
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.538
    sort_std: 0.0
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.5327
    std: 0.0006
    paper_value: 0.5327
    paper_std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 25
    true_value: 0.5327
    true_std: 0.0006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5327
    sort_std: 0.0006
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.5274
    std: 0.0083
    paper_value: 0.5274
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 33
    true_value: 0.5274
    true_std: 0.0083
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5274
    sort_std: 0.0083
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 77
    true_value: 0.4488
    true_std: 0.0034
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4488
    sort_std: 0.0034
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.4379
    std: 0.0257
    paper_value: 0.4379
    paper_std: 0.0257
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 82
    true_value: 0.4386
    true_std: 0.0035
    value_gap_source_arxiv: '2411.15671'
    value_gap_source_title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence
      Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006999999999999784
    value_note: global 0.4386 within std
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4386
    sort_std: 0.0035
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.3979
    std: 0.0077
    paper_value: 0.3979
    paper_std: 0.0077
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 91
    true_value: 0.3979
    true_std: 0.0077
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3979
    sort_std: 0.0077
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 94
    true_value: 0.3647
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
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
- &id016
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
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.3974
    std: 0.0101
    paper_value: 0.3974
    paper_std: 0.0101
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 10
    true_value: 0.3974
    true_std: 0.0101
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3974
    sort_std: 0.0101
    is_best: false
  - model: Graph Mamba-1
    model_key: graph mamba-1
    model_plain: Graph Mamba-1
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 11
    true_value: 0.396
    true_std: 0.0175
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.396
    sort_std: 0.0175
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 12
    true_value: 0.396
    true_std: 0.0175
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
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
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 14
    true_value: 0.3884
    true_std: 0.0055
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3884
    sort_std: 0.0055
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.2922
    std: 0.0018
    paper_value: 0.2922
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 21
    true_value: 0.3802
    true_std: 0.0015
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08799999999999997
    value_note: ''
    paper_rank: 43
    rank_delta: 22
    rank_delta_abs: 22
    rank_delta_direction: worse
    sort_value: 0.3802
    sort_std: 0.0015
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.3523
    std: 0.0057
    paper_value: 0.3523
    paper_std: 0.0057
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 28
    true_value: 0.3523
    true_std: 0.0057
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3523
    sort_std: 0.0057
    is_best: false
  - model: GENs+LapPE
    model_key: gens+lappe
    model_plain: GENs+LapPE
    value: 0.3523
    std: 0.0057
    paper_value: 0.3523
    paper_std: 0.0057
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 29
    true_value: 0.3523
    true_std: 0.0057
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3523
    sort_std: 0.0057
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 30
    true_value: 0.3458
    true_std: 0.007
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
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
    value: 0.3455
    std: 0.0009
    paper_value: 0.3455
    paper_std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 31
    true_value: 0.3455
    true_std: 0.0009
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3455
    sort_std: 0.0009
    is_best: false
  - model: GENs+RWSE
    model_key: gens+rwse
    model_plain: GENs+RWSE
    value: 0.3404
    std: 0.0042
    paper_value: 0.3404
    paper_std: 0.0042
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 33
    true_value: 0.3404
    true_std: 0.0042
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3404
    sort_std: 0.0042
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 35
    true_value: 0.3314
    true_std: 0.0024
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3314
    sort_std: 0.0024
    is_best: false
  - model: GEN w/o HA
    model_key: gen w/o ha
    model_plain: GEN w/o HA
    value: 0.2987
    std: 0.0033
    paper_value: 0.2987
    paper_std: 0.0033
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 42
    true_value: 0.2987
    true_std: 0.0033
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2987
    sort_std: 0.0033
    is_best: false
  - model: GEN w/o EA
    model_key: gen w/o ea
    model_plain: GEN w/o EA
    value: 0.2969
    std: 0.0048
    paper_value: 0.2969
    paper_std: 0.0048
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 43
    true_value: 0.2969
    true_std: 0.0048
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2969
    sort_std: 0.0048
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.1338
    std: 0.0007
    paper_value: 0.1338
    paper_std: 0.0007
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 45
    true_value: 0.2733
    true_std: 0.0041
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13949999999999999
    value_note: ''
    paper_rank: 68
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.2733
    sort_std: 0.0041
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.2697
    std: 0.0011
    paper_value: 0.2697
    paper_std: 0.0011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 46
    true_value: 0.2697
    true_std: 0.0011
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2697
    sort_std: 0.0011
    is_best: false
  - model: MAGNA
    model_key: magna
    model_plain: MAGNA
    value: 0.2662
    std: 0.0016
    paper_value: 0.2662
    paper_std: 0.0016
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 47
    true_value: 0.2662
    true_std: 0.0016
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2662
    sort_std: 0.0016
    is_best: false
  - model: DAGNN
    model_key: dagnn
    model_plain: DAGNN
    value: 0.2602
    std: 0.0023
    paper_value: 0.2602
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 51
    true_value: 0.2602
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2602
    sort_std: 0.0023
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 55
    true_value: 0.2592
    true_std: 0.0158
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2592
    sort_std: 0.0158
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.2426
    std: 0.0021
    paper_value: 0.2426
    paper_std: 0.0021
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 61
    true_value: 0.2426
    true_std: 0.0021
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2426
    sort_std: 0.0021
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
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
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.4061
    std: 0.0297
    paper_value: 0.4061
    paper_std: 0.0297
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 8
    true_value: 0.7827
    true_std: 0.0128
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.37659999999999993
    value_note: ''
    paper_rank: 124
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.7827
    sort_std: 0.0128
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.259
    std: 0.0358
    paper_value: 0.259
    paper_std: 0.0358
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 23
    true_value: 0.7121
    true_std: 0.0184
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.45309999999999995
    value_note: ''
    paper_rank: 128
    rank_delta: 105
    rank_delta_abs: 105
    rank_delta_direction: worse
    sort_value: 0.7121
    sort_std: 0.0184
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3993
    std: 0.033
    paper_value: 0.3993
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 36
    true_value: 0.6748
    true_std: 0.004
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27549999999999997
    value_note: ''
    paper_rank: 125
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.6748
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4629
    std: 0.034
    paper_value: 0.4629
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 48
    true_value: 0.6482
    true_std: 0.0224
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18530000000000002
    value_note: ''
    paper_rank: 111
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.6482
    sort_std: 0.0224
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4413
    std: 0.0241
    paper_value: 0.4413
    paper_std: 0.0241
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 50
    true_value: 0.639
    true_std: 0.0046
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1977
    value_note: ''
    paper_rank: 117
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.639
    sort_std: 0.0046
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4481
    std: 0.0474
    paper_value: 0.4481
    paper_std: 0.0474
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 60
    true_value: 0.6215
    true_std: 0.0042
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17340000000000005
    value_note: ''
    paper_rank: 117
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.6215
    sort_std: 0.0042
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4521
    std: 0.0372
    paper_value: 0.4521
    paper_std: 0.0372
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 62
    true_value: 0.6144
    true_std: 0.0137
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.16229999999999994
    value_note: ''
    paper_rank: 115
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.6144
    sort_std: 0.0137
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.2675
    std: 0.0364
    paper_value: 0.2675
    paper_std: 0.0364
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 64
    true_value: 0.612
    true_std: 0.0428
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3445
    value_note: ''
    paper_rank: 127
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.612
    sort_std: 0.0428
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.4197
    std: 0.0318
    paper_value: 0.4197
    paper_std: 0.0318
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 70
    true_value: 0.6017
    true_std: 0.0139
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.182
    value_note: ''
    paper_rank: 121
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.6017
    sort_std: 0.0139
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3638
    std: 0.0385
    paper_value: 0.3638
    paper_std: 0.0385
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 84
    true_value: 0.5634
    true_std: 0.0111
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1996
    value_note: ''
    paper_rank: 127
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.5634
    sort_std: 0.0111
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.471
    std: 0.044
    paper_value: 0.471
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 108
    true_value: 0.471
    true_std: 0.044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.471
    sort_std: 0.044
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.4155
    std: 0.0391
    paper_value: 0.4155
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 112
    true_value: 0.4607
    true_std: 0.0151
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04520000000000002
    value_note: ''
    paper_rank: 123
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.4607
    sort_std: 0.0151
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.33
    std: 0.0315
    paper_value: 0.33
    paper_std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 124
    true_value: 0.408
    true_std: 0.02
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07799999999999996
    value_note: ''
    paper_rank: 127
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.408
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
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
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
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
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7219
    std: 0.0083
    paper_value: 0.7219
    paper_std: 0.0083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 6
    true_value: 0.818
    true_std: 0.0076
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09609999999999996
    value_note: ''
    paper_rank: 121
    rank_delta: 115
    rank_delta_abs: 115
    rank_delta_direction: worse
    sort_value: 0.818
    sort_std: 0.0076
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7314
    std: 0.005
    paper_value: 0.7314
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0824999999999999
    value_note: ''
    paper_rank: 110
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7222
    std: 0.0084
    paper_value: 0.7222
    paper_std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08300000000000007
    value_note: ''
    paper_rank: 120
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7059
    std: 0.0089
    paper_value: 0.7059
    paper_std: 0.0089
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 26
    true_value: 0.8012
    true_std: 0.0124
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09530000000000005
    value_note: ''
    paper_rank: 133
    rank_delta: 107
    rank_delta_abs: 107
    rank_delta_direction: worse
    sort_value: 0.8012
    sort_std: 0.0124
    is_best: true
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7272
    std: 0.0115
    paper_value: 0.7272
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 29
    true_value: 0.7962
    true_std: 0.0163
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06900000000000006
    value_note: ''
    paper_rank: 112
    rank_delta: 83
    rank_delta_abs: 83
    rank_delta_direction: worse
    sort_value: 0.7962
    sort_std: 0.0163
    is_best: true
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7237
    std: 0.012
    paper_value: 0.7237
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 30
    true_value: 0.7956
    true_std: 0.011
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07189999999999996
    value_note: ''
    paper_rank: 118
    rank_delta: 88
    rank_delta_abs: 88
    rank_delta_direction: worse
    sort_value: 0.7956
    sort_std: 0.011
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7226
    std: 0.0055
    paper_value: 0.7226
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06969999999999998
    value_note: ''
    paper_rank: 120
    rank_delta: 86
    rank_delta_abs: 86
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7273
    std: 0.0123
    paper_value: 0.7273
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 47
    true_value: 0.7699
    true_std: 0.0112
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04260000000000008
    value_note: ''
    paper_rank: 112
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.7699
    sort_std: 0.0112
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7221
    std: 0.0129
    paper_value: 0.7221
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 50
    true_value: 0.7689
    true_std: 0.0119
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046800000000000064
    value_note: ''
    paper_rank: 120
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7689
    sort_std: 0.0119
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7185
    std: 0.0111
    paper_value: 0.7185
    paper_std: 0.0111
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 52
    true_value: 0.7683
    true_std: 0.0124
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.049799999999999955
    value_note: ''
    paper_rank: 122
    rank_delta: 70
    rank_delta_abs: 70
    rank_delta_direction: worse
    sort_value: 0.7683
    sort_std: 0.0124
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.7356
    std: 0.0046
    paper_value: 0.7356
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 104
    true_value: 0.7356
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7356
    sort_std: 0.0046
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.8273
    std: 0.0075
    paper_value: 0.8273
    paper_std: 0.0075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 20
    true_value: 0.887
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059699999999999975
    value_note: ''
    paper_rank: 131
    rank_delta: 111
    rank_delta_abs: 111
    rank_delta_direction: worse
    sort_value: 0.887
    sort_std: 0.002
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8446
    std: 0.0055
    paper_value: 0.8446
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.037899999999999934
    value_note: ''
    paper_rank: 107
    rank_delta: 76
    rank_delta_abs: 76
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8092
    std: 0.0117
    paper_value: 0.8092
    paper_std: 0.0117
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 33
    true_value: 0.882
    true_std: 0.005
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07279999999999998
    value_note: ''
    paper_rank: 151
    rank_delta: 118
    rank_delta_abs: 118
    rank_delta_direction: worse
    sort_value: 0.882
    sort_std: 0.005
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8482
    std: 0.0085
    paper_value: 0.8482
    paper_std: 0.0085
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 37
    true_value: 0.8809999999999999
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03279999999999994
    value_note: ''
    paper_rank: 105
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.8809999999999999
    sort_std: 0.006999999999999999
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8343
    std: 0.009
    paper_value: 0.8343
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 45
    true_value: 0.879
    true_std: 0.012
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04469999999999996
    value_note: ''
    paper_rank: 120
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.851
    std: 0.0067
    paper_value: 0.851
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026800000000000046
    value_note: ''
    paper_rank: 101
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8388
    std: 0.0065
    paper_value: 0.8388
    paper_std: 0.0065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 71
    true_value: 0.8690000000000001
    true_std: 0.0104
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.030200000000000116
    value_note: ''
    paper_rank: 112
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.8690000000000001
    sort_std: 0.0104
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.8543
    std: 0.0042
    paper_value: 0.8543
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 96
    true_value: 0.8543
    true_std: 0.0042
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8543
    sort_std: 0.0042
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8387
    std: 0.0096
    paper_value: 0.8387
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 114
    true_value: 0.8387
    true_std: 0.0096
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8387
    sort_std: 0.0096
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.8329
    std: 0.0136
    paper_value: 0.8329
    paper_std: 0.0136
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 124
    true_value: 0.8329
    true_std: 0.0136
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8329
    sort_std: 0.0136
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8326
    std: 0.0124
    paper_value: 0.8326
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 125
    true_value: 0.8326
    true_std: 0.0124
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8326
    sort_std: 0.0124
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
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
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.3498
    std: 0.0005
    paper_value: 0.3498
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 4
    true_value: 0.4703
    true_std: 0.0014
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1205
    value_note: ''
    paper_rank: 17
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.4703
    sort_std: 0.0014
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3495
    std: 0.001
    paper_value: 0.3495
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 5
    true_value: 0.467
    true_std: 0.0004
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11750000000000005
    value_note: ''
    paper_rank: 18
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.467
    sort_std: 0.0004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3424
    std: 0.0007
    paper_value: 0.3424
    paper_std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 7
    true_value: 0.4526
    true_std: 0.0006
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11020000000000002
    value_note: ''
    paper_rank: 32
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.4526
    sort_std: 0.0006
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.3516
    std: 0.0102
    paper_value: 0.3516
    paper_std: 0.0102
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 9
    true_value: 0.367
    true_std: 0.0082
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01539999999999997
    value_note: ''
    paper_rank: 16
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.367
    sort_std: 0.0082
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3637
    std: 0.002
    paper_value: 0.3637
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 10
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3637
    sort_std: 0.002
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.352
    std: 0.001
    paper_value: 0.352
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 15
    true_value: 0.352
    true_std: 0.001
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.352
    sort_std: 0.001
    is_best: false
  - model: GENs+LapPE
    model_key: gens+lappe
    model_plain: GENs+LapPE
    value: 0.352
    std: 0.001
    paper_value: 0.352
    paper_std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 16
    true_value: 0.352
    true_std: 0.001
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.352
    sort_std: 0.001
    is_best: false
  - model: GEN w/o EA
    model_key: gen w/o ea
    model_plain: GEN w/o EA
    value: 0.3496
    std: 0.0016
    paper_value: 0.3496
    paper_std: 0.0016
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 18
    true_value: 0.3496
    true_std: 0.0016
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3496
    sort_std: 0.0016
    is_best: false
  - model: GEN w/o HA
    model_key: gen w/o ha
    model_plain: GEN w/o HA
    value: 0.348
    std: 0.0007
    paper_value: 0.348
    paper_std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 20
    true_value: 0.348
    true_std: 0.0007
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.348
    sort_std: 0.0007
    is_best: false
  - model: DRew
    model_key: drew
    model_plain: DRew
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 24
    true_value: 0.3444
    true_std: 0.0017
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3444
    sort_std: 0.0017
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3441
    std: 0.0008
    paper_value: 0.3441
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 28
    true_value: 0.3441
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3441
    sort_std: 0.0008
    is_best: false
  - model: GENs+RWSE
    model_key: gens+rwse
    model_plain: GENs+RWSE
    value: 0.344
    std: 0.0008
    paper_value: 0.344
    paper_std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 29
    true_value: 0.344
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.344
    sort_std: 0.0008
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3414
    std: 0.0006
    paper_value: 0.3414
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 33
    true_value: 0.3414
    true_std: 0.0006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3414
    sort_std: 0.0006
    is_best: false
  - model: Graph Mamba-1
    model_key: graph mamba-1
    model_plain: Graph Mamba-1
    value: 0.3395
    std: 0.0013
    paper_value: 0.3395
    paper_std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 38
    true_value: 0.3395
    true_std: 0.0013
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3395
    sort_std: 0.0013
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.3395
    std: 0.0013
    paper_value: 0.3395
    paper_std: 0.0013
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 39
    true_value: 0.3395
    true_std: 0.0013
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3395
    sort_std: 0.0013
    is_best: false
  - model: MAGNA
    model_key: magna
    model_plain: MAGNA
    value: 0.3364
    std: 0.0008
    paper_value: 0.3364
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 44
    true_value: 0.3364
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3364
    sort_std: 0.0008
    is_best: false
  - model: DAGNN
    model_key: dagnn
    model_plain: DAGNN
    value: 0.3287
    std: 0.002
    paper_value: 0.3287
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 53
    true_value: 0.3287
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3287
    sort_std: 0.002
    is_best: false
  metric: MRR
  higher_is_better: true
- &id014
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
    paper_value: 0.4653
    paper_std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 3
    true_value: 0.4653
    true_std: 0.0097
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: GENs+RWSE
    model_key: gens+rwse
    model_plain: GENs+RWSE
    value: 0.4653
    std: 0.0097
    paper_value: 0.4653
    paper_std: 0.0097
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 4
    true_value: 0.4653
    true_std: 0.0097
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4653
    sort_std: 0.0097
    is_best: false
  - model: PPGT
    model_key: ppgt
    model_plain: PPGT
    value: 0.4641
    std: 0.0033
    metric: F1
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
    sort_value: 0.4641
    sort_std: 0.0033
    is_best: false
  - model: GENs+LapPE
    model_key: gens+lappe
    model_plain: GENs+LapPE
    value: 0.4523
    std: 0.0162
    paper_value: 0.4523
    paper_std: 0.0162
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 8
    true_value: 0.4523
    true_std: 0.0162
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4523
    sort_std: 0.0162
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.444
    std: 0.0065
    paper_value: 0.444
    paper_std: 0.0065
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 9
    true_value: 0.444
    true_std: 0.0065
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.444
    sort_std: 0.0065
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.4393
    std: 0.0112
    paper_value: 0.4393
    paper_std: 0.0112
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 13
    true_value: 0.4393
    true_std: 0.0112
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4393
    sort_std: 0.0112
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.388
    std: 0.004
    paper_value: 0.388
    paper_std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 19
    true_value: 0.4263
    true_std: 0.0057
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0383
    value_note: ''
    paper_rank: 42
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.4263
    sort_std: 0.0057
    is_best: false
  - model: Graph Mamba-1
    model_key: graph mamba-1
    model_plain: Graph Mamba-1
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 25
    true_value: 0.4191
    true_std: 0.0126
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4191
    sort_std: 0.0126
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 26
    true_value: 0.4191
    true_std: 0.0126
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
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
  - model: GEN w/o HA
    model_key: gen w/o ha
    model_plain: GEN w/o HA
    value: 0.4055
    std: 0.0124
    paper_value: 0.4055
    paper_std: 0.0124
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 29
    true_value: 0.4055
    true_std: 0.0124
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4055
    sort_std: 0.0124
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 32
    true_value: 0.4006
    true_std: 0.0061
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
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
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3975
    std: 0.0037
    paper_value: 0.3975
    paper_std: 0.0037
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: GEN w/o EA
    model_key: gen w/o ea
    model_plain: GEN w/o EA
    value: 0.3905
    std: 0.0132
    paper_value: 0.3905
    paper_std: 0.0132
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 42
    true_value: 0.3905
    true_std: 0.0132
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3905
    sort_std: 0.0132
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2078
    std: 0.0031
    paper_value: 0.2078
    paper_std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 46
    true_value: 0.376
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1682
    value_note: ''
    paper_rank: 95
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.376
    sort_std: 0.001
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3335
    std: 0.0045
    paper_value: 0.3335
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 49
    true_value: 0.37
    true_std: 0.001
    value_gap_source_arxiv: '2509.22259'
    value_gap_source_title: Rotary Position Encodings for Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03649999999999998
    value_note: ''
    paper_rank: 58
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.37
    sort_std: 0.001
    is_best: false
  - model: DAGNN
    model_key: dagnn
    model_plain: DAGNN
    value: 0.3613
    std: 0.0084
    paper_value: 0.3613
    paper_std: 0.0084
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 52
    true_value: 0.3613
    true_std: 0.0084
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3613
    sort_std: 0.0084
    is_best: false
  - model: MAGNA
    model_key: magna
    model_plain: MAGNA
    value: 0.3585
    std: 0.0052
    paper_value: 0.3585
    paper_std: 0.0052
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 54
    true_value: 0.3585
    true_std: 0.0052
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3585
    sort_std: 0.0052
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3421
    std: 0.0056
    paper_value: 0.3421
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 58
    true_value: 0.3421
    true_std: 0.0056
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3421
    sort_std: 0.0056
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: SAT
    model_key: sat
    model_plain: SAT
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 63
    true_value: 0.323
    true_std: 0.0039
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.323
    sort_std: 0.0039
    is_best: false
  metric: F1
  higher_is_better: true
- &id012
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 9
    true_value: 0.7261
    true_std: 0.0067
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040099999999999913
    value_note: ''
    paper_rank: 87
    rank_delta: 78
    rank_delta_abs: 78
    rank_delta_direction: worse
    sort_value: 0.7261
    sort_std: 0.0067
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.721
    std: 0.0039
    paper_value: 0.721
    paper_std: 0.0039
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 12
    true_value: 0.721
    true_std: 0.0039
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.0039
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.7142
    std: 0.0071
    paper_value: 0.7142
    paper_std: 0.0071
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 28
    true_value: 0.7142
    true_std: 0.0071
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7142
    sort_std: 0.0071
    is_best: false
  - model: GENs+LapPE
    model_key: gens+lappe
    model_plain: GENs+LapPE
    value: 0.7142
    std: 0.0071
    paper_value: 0.7142
    paper_std: 0.0071
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 29
    true_value: 0.7142
    true_std: 0.0071
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7142
    sort_std: 0.0071
    is_best: false
  - model: GENs+RWSE
    model_key: gens+rwse
    model_plain: GENs+RWSE
    value: 0.7087
    std: 0.0103
    paper_value: 0.7087
    paper_std: 0.0103
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 35
    true_value: 0.7087
    true_std: 0.0103
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7087
    sort_std: 0.0103
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.7071
    std: 0.0083
    paper_value: 0.7071
    paper_std: 0.0083
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 38
    true_value: 0.7071
    true_std: 0.0083
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7071
    sort_std: 0.0083
    is_best: false
  - model: DAGNN
    model_key: dagnn
    model_plain: DAGNN
    value: 0.7021
    std: 0.0075
    paper_value: 0.7021
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 47
    true_value: 0.7021
    true_std: 0.0075
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7021
    sort_std: 0.0075
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 49
    true_value: 0.7006
    true_std: 0.0033
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02410000000000001
    value_note: ''
    paper_rank: 111
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6924
    std: 0.0044
    paper_value: 0.6924
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 78
    true_value: 0.6924
    true_std: 0.0044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6924
    sort_std: 0.0044
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.692
    std: 0.0037
    paper_value: 0.692
    paper_std: 0.0037
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 80
    true_value: 0.692
    true_std: 0.0037
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.692
    sort_std: 0.0037
    is_best: false
  - model: GEN w/o EA
    model_key: gen w/o ea
    model_plain: GEN w/o EA
    value: 0.6889
    std: 0.0092
    paper_value: 0.6889
    paper_std: 0.0092
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 85
    true_value: 0.6889
    true_std: 0.0092
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6889
    sort_std: 0.0092
    is_best: false
  - model: GEN w/o HA
    model_key: gen w/o ha
    model_plain: GEN w/o HA
    value: 0.6847
    std: 0.0089
    paper_value: 0.6847
    paper_std: 0.0089
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 92
    true_value: 0.6847
    true_std: 0.0089
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6847
    sort_std: 0.0089
    is_best: false
  - model: Graph Mamba-1
    model_key: graph mamba-1
    model_plain: Graph Mamba-1
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 117
    true_value: 0.6739
    true_std: 0.0087
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6739
    sort_std: 0.0087
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 118
    true_value: 0.6739
    true_std: 0.0087
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
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
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.6534
    std: 0.0091
    paper_value: 0.6534
    paper_std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 154
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006700000000000039
    value_note: global 0.6601 within std
    paper_rank: 172
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: MAGNA
    model_key: magna
    model_plain: MAGNA
    value: 0.6541
    std: 0.0038
    paper_value: 0.6541
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 168
    true_value: 0.6541
    true_std: 0.0038
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6541
    sort_std: 0.0038
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.6527
    std: 0.0043
    paper_value: 0.6527
    paper_std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 178
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 213
    true_value: 0.6384
    true_std: 0.0121
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384
    sort_std: 0.0121
    is_best: false
  metric: AP
  higher_is_better: true
- &id013
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 3
    true_value: 0.2421
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.003899999999999987
    value_note: ''
    paper_rank: 54
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.2462
    std: 0.0007
    paper_value: 0.2462
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 5
    true_value: 0.2422
    true_std: 0.0007
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0040000000000000036
    value_note: ''
    paper_rank: 58
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.2422
    sort_std: 0.0007
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.243
    std: 0.0013
    paper_value: 0.243
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 10
    true_value: 0.243
    true_std: 0.0013
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.243
    sort_std: 0.0013
    is_best: false
  - model: GENs+LapPE
    model_key: gens+lappe
    model_plain: GENs+LapPE
    value: 0.243
    std: 0.0013
    paper_value: 0.243
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 11
    true_value: 0.243
    true_std: 0.0013
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.243
    sort_std: 0.0013
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 12
    true_value: 0.2431
    true_std: 0.002
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.004599999999999993
    value_note: ''
    paper_rank: 89
    rank_delta: 77
    rank_delta_abs: 77
    rank_delta_direction: worse
    sort_value: 0.2431
    sort_std: 0.002
    is_best: false
  - model: GEN w/o EA
    model_key: gen w/o ea
    model_plain: GEN w/o EA
    value: 0.2432
    std: 0.0013
    paper_value: 0.2432
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 16
    true_value: 0.2432
    true_std: 0.0013
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2432
    sort_std: 0.0013
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: GEN w/o HA
    model_key: gen w/o ha
    model_plain: GEN w/o HA
    value: 0.2472
    std: 0.0009
    paper_value: 0.2472
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 77
    true_value: 0.2472
    true_std: 0.0009
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2472
    sort_std: 0.0009
    is_best: false
  - model: GMN
    model_key: gmn
    model_plain: GMN
    value: 0.2473
    std: 0.0025
    paper_value: 0.2473
    paper_std: 0.0025
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 81
    true_value: 0.2473
    true_std: 0.0025
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
    sort_value: 0.2473
    sort_std: 0.0025
    is_best: false
  - model: Graph Mamba-1
    model_key: graph mamba-1
    model_plain: Graph Mamba-1
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 96
    true_value: 0.2478
    true_std: 0.0016
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2478
    sort_std: 0.0016
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 97
    true_value: 0.2478
    true_std: 0.0016
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
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
    value: 0.2484
    std: 0.0012
    paper_value: 0.2484
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00030000000000002247
    value_note: global 0.2481 within std
    paper_rank: 106
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.253
    std: 0.001
    paper_value: 0.253
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 120
    true_value: 0.2488
    true_std: 0.0018
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.004200000000000009
    value_note: ''
    paper_rank: 172
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.2488
    sort_std: 0.0018
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2509
    std: 0.001
    paper_value: 0.2509
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 135
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 148
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: MAGNA
    model_key: magna
    model_plain: MAGNA
    value: 0.2509
    std: 0.0008
    paper_value: 0.2509
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 151
    true_value: 0.2509
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 151
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2509
    sort_std: 0.0008
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.251
    std: 0.0008
    paper_value: 0.251
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 153
    true_value: 0.251
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.251
    sort_std: 0.0008
    is_best: false
  - model: GENs+RWSE
    model_key: gens+rwse
    model_plain: GENs+RWSE
    value: 0.2521
    std: 0.001
    paper_value: 0.2521
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 162
    true_value: 0.2521
    true_std: 0.001
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2521
    sort_std: 0.001
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: DAGNN
    model_key: dagnn
    model_plain: DAGNN
    value: 0.2645
    std: 0.0023
    paper_value: 0.2645
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 233
    true_value: 0.2645
    true_std: 0.0023
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 233
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2645
    sort_std: 0.0023
    is_best: false
  - model: SAT
    model_key: sat
    model_plain: SAT
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 243
    true_value: 0.2683
    true_std: 0.0043
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 243
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2683
    sort_std: 0.0043
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8112
    std: 0.0022
    paper_value: 0.8112
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11119999999999997
    value_note: ''
    paper_rank: 114
    rank_delta: 109
    rank_delta_abs: 109
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8028
    std: 0.0012
    paper_value: 0.8028
    paper_std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11730000000000007
    value_note: ''
    paper_rank: 116
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7935
    std: 0.0073
    paper_value: 0.7935
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 11
    true_value: 0.9068
    true_std: 0.0031
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11330000000000007
    value_note: ''
    paper_rank: 119
    rank_delta: 108
    rank_delta_abs: 108
    rank_delta_direction: worse
    sort_value: 0.9068
    sort_std: 0.0031
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.8014
    std: 0.0106
    paper_value: 0.8014
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 27
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09560000000000002
    value_note: ''
    paper_rank: 116
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.806
    std: 0.0049
    paper_value: 0.806
    paper_std: 0.0049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 26
    true_value: 0.897
    true_std: 0.002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09099999999999997
    value_note: ''
    paper_rank: 116
    rank_delta: 90
    rank_delta_abs: 90
    rank_delta_direction: worse
    sort_value: 0.897
    sort_std: 0.002
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7967
    std: 0.0073
    paper_value: 0.7967
    paper_std: 0.0073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 32
    true_value: 0.8952
    true_std: 0.0054
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09850000000000003
    value_note: ''
    paper_rank: 117
    rank_delta: 85
    rank_delta_abs: 85
    rank_delta_direction: worse
    sort_value: 0.8952
    sort_std: 0.0054
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7959
    std: 0.0092
    paper_value: 0.7959
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 38
    true_value: 0.8932
    true_std: 0.0025
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09729999999999994
    value_note: ''
    paper_rank: 117
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.8932
    sort_std: 0.0025
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7994
    std: 0.0026
    paper_value: 0.7994
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 45
    true_value: 0.8894
    true_std: 0.0016
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08999999999999997
    value_note: ''
    paper_rank: 116
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.8894
    sort_std: 0.0016
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7972
    std: 0.005
    paper_value: 0.7972
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08919999999999995
    value_note: ''
    paper_rank: 117
    rank_delta: 63
    rank_delta_abs: 63
    rank_delta_direction: worse
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.8006
    std: 0.0067
    paper_value: 0.8006
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 92
    true_value: 0.8687
    true_std: 0.0024
    value_gap_source_arxiv: '2410.13798'
    value_gap_source_title: Learning Graph Quantized Tokenizers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06810000000000005
    value_note: ''
    paper_rank: 116
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.8687
    sort_std: 0.0024
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.8194
    std: 0.0034
    paper_value: 0.8194
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 110
    true_value: 0.8194
    true_std: 0.0034
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8194
    sort_std: 0.0034
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.7922
    std: 0.0074
    paper_value: 0.7922
    paper_std: 0.0074
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 11
    true_value: 0.7922
    true_std: 0.0074
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7922
    sort_std: 0.0074
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7902
    std: 0.006
    paper_value: 0.7902
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 13
    true_value: 0.7902
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7902
    sort_std: 0.006
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.7894
    std: 0.0078
    paper_value: 0.7894
    paper_std: 0.0078
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 14
    true_value: 0.7894
    true_std: 0.0078
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7894
    sort_std: 0.0078
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7886
    std: 0.0292
    paper_value: 0.7886
    paper_std: 0.0292
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 16
    true_value: 0.7886
    true_std: 0.0092
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7886
    sort_std: 0.0092
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7795
    std: 0.0051
    paper_value: 0.7795
    paper_std: 0.0051
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 24
    true_value: 0.7795
    true_std: 0.0051
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795
    sort_std: 0.0051
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7721
    std: 0.0128
    paper_value: 0.7721
    paper_std: 0.0128
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 33
    true_value: 0.7721
    true_std: 0.0128
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7721
    sort_std: 0.0128
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7502
    std: 0.0161
    paper_value: 0.7502
    paper_std: 0.0161
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 49
    true_value: 0.7502
    true_std: 0.0161
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7502
    sort_std: 0.0161
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.7381
    std: 0.0059
    paper_value: 0.7381
    paper_std: 0.0059
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 54
    true_value: 0.7381
    true_std: 0.0059
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7381
    sort_std: 0.0059
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.7256
    std: 0.0133
    paper_value: 0.7256
    paper_std: 0.0133
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 55
    true_value: 0.7256
    true_std: 0.0133
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7256
    sort_std: 0.0133
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.6596
    std: 0.0195
    paper_value: 0.6596
    paper_std: 0.0195
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 60
    true_value: 0.6596
    true_std: 0.0195
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6596
    sort_std: 0.0195
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.6574
    std: 0.0119
    paper_value: 0.6574
    paper_std: 0.0119
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 61
    true_value: 0.6574
    true_std: 0.0119
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6574
    sort_std: 0.0119
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.6359
    std: 0.0146
    paper_value: 0.6359
    paper_std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 62
    true_value: 0.6359
    true_std: 0.0146
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6359
    sort_std: 0.0146
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.5548
    std: 0.0091
    paper_value: 0.5548
    paper_std: 0.0091
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 64
    true_value: 0.5548
    true_std: 0.0091
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5548
    sort_std: 0.0091
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id008
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
    paper_value: 0.9266
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 2
    true_value: 0.9266
    true_std: 0.006
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9252
    std: 0.005
    paper_value: 0.9252
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 4
    true_value: 0.9252
    true_std: 0.005
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9252
    sort_std: 0.005
    is_best: true
  - model: Ours
    model_key: ours
    model_plain: Ours
    value: 0.9212
    std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.18837'
    title: 'L2G-Net: Local to Global Spectral Graph Neural Networks via Cauchy Factorizations'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 5
    sort_value: 0.9212
    sort_std: 0.0112
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.9127
    std: 0.002
    paper_value: 0.9127
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 19
    true_value: 0.9127
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9127
    sort_std: 0.002
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.9106
    std: 0.0027
    paper_value: 0.9106
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 23
    true_value: 0.9106
    true_std: 0.0027
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9106
    sort_std: 0.0027
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9063
    std: 0.0014
    paper_value: 0.9063
    paper_std: 0.0014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.8272
    std: 0.0008
    paper_value: 0.8272
    paper_std: 0.0008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 65
    true_value: 0.8272
    true_std: 0.0008
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8272
    sort_std: 0.0008
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8001
    std: 0.0044
    paper_value: 0.8001
    paper_std: 0.0044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 71
    true_value: 0.8001
    true_std: 0.0044
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8001
    sort_std: 0.0044
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.7992
    std: 0.0056
    paper_value: 0.7992
    paper_std: 0.0056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 74
    true_value: 0.7992
    true_std: 0.0056
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7992
    sort_std: 0.0056
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7483
    std: 0.0081
    paper_value: 0.7483
    paper_std: 0.0081
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 78
    true_value: 0.7483
    true_std: 0.0081
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7483
    sort_std: 0.0081
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.6485
    std: 0.0027
    paper_value: 0.6485
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 80
    true_value: 0.717
    true_std: 0.0031
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0685
    value_note: ''
    paper_rank: 86
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.717
    sort_std: 0.0031
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.6396
    std: 0.0062
    paper_value: 0.6396
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 88
    true_value: 0.6396
    true_std: 0.0062
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6396
    sort_std: 0.0062
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.6011
    std: 0.0052
    paper_value: 0.6011
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 89
    true_value: 0.6363
    true_std: 0.023
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03520000000000001
    value_note: ''
    paper_rank: 90
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6363
    sort_std: 0.023
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.5963
    std: 0.0069
    paper_value: 0.5963
    paper_std: 0.0069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: apd_tab1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 93
    true_value: 0.5963
    true_std: 0.0069
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
    sort_value: 0.5963
    sort_std: 0.0069
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
    value: 0.3592
    std: 0.0132
    paper_value: 0.3592
    paper_std: 0.0132
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 3
    true_value: 0.741
    true_std: 0.0189
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3818
    value_note: ''
    paper_rank: 99
    rank_delta: 96
    rank_delta_abs: 96
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.0189
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7298
    std: 0.0178
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
    global_rank: 4
    sort_value: 0.7298
    sort_std: 0.0178
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.3511
    std: 0.0124
    paper_value: 0.3511
    paper_std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 23
    true_value: 0.6121
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.26099999999999995
    value_note: ''
    paper_rank: 102
    rank_delta: 79
    rank_delta_abs: 79
    rank_delta_direction: worse
    sort_value: 0.6121
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4501
    std: 0.0163
    paper_value: 0.4501
    paper_std: 0.0163
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0842
    value_note: ''
    paper_rank: 49
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.3895
    std: 0.0199
    paper_value: 0.3895
    paper_std: 0.0199
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 41
    true_value: 0.5015
    true_std: 0.0192
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11199999999999993
    value_note: ''
    paper_rank: 81
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.5015
    sort_std: 0.0192
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.4625
    std: 0.0061
    paper_value: 0.4625
    paper_std: 0.0061
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 47
    true_value: 0.4625
    true_std: 0.0061
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4625
    sort_std: 0.0061
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.4265
    std: 0.0241
    paper_value: 0.4265
    paper_std: 0.0241
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 48
    true_value: 0.4582
    true_std: 0.0217
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.031700000000000006
    value_note: ''
    paper_rank: 62
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.4582
    sort_std: 0.0217
    is_best: false
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.4197
    std: 0.0214
    paper_value: 0.4197
    paper_std: 0.0214
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 50
    true_value: 0.4498
    true_std: 0.0303
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03009999999999996
    value_note: global 0.4498 within std
    paper_rank: 68
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.4498
    sort_std: 0.0303
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4173
    std: 0.0207
    paper_value: 0.4173
    paper_std: 0.0207
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.027600000000000013
    value_note: ''
    paper_rank: 68
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.3889
    std: 0.0267
    paper_value: 0.3889
    paper_std: 0.0267
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 56
    true_value: 0.4342
    true_std: 0.0162
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04529999999999995
    value_note: ''
    paper_rank: 82
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.4342
    sort_std: 0.0162
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.4078
    std: 0.0147
    paper_value: 0.4078
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 69
    true_value: 0.41609999999999997
    true_std: 0.0074
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008299999999999974
    value_note: global 0.4161 within std
    paper_rank: 73
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.41609999999999997
    sort_std: 0.0074
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.3981
    std: 0.0228
    paper_value: 0.3981
    paper_std: 0.0228
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 77
    true_value: 0.3981
    true_std: 0.0228
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3981
    sort_std: 0.0228
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.351
    std: 0.0115
    paper_value: 0.351
    paper_std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 78
    true_value: 0.3953
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.044300000000000006
    value_note: ''
    paper_rank: 102
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.3953
    sort_std: 0.0088
    is_best: false
  - model: CPGNN
    model_key: cpgnn
    model_plain: CPGNN
    value: 0.3004
    std: 0.0203
    paper_value: 0.3004
    paper_std: 0.0203
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 82
    true_value: 0.389
    true_std: 0.012
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08860000000000001
    value_note: ''
    paper_rank: 109
    rank_delta: 27
    rank_delta_abs: 27
    rank_delta_direction: worse
    sort_value: 0.389
    sort_std: 0.012
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: WikiCS
  rows:
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8557
    std: 0.0065
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
    sort_value: 0.8557
    sort_std: 0.0065
    is_best: true
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.8515
    std: 0.0063
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
    sort_value: 0.8515
    sort_std: 0.0063
    is_best: true
  - model: HopGNN
    model_key: hopgnn
    model_plain: HopGNN
    value: 0.8473
    std: 0.0059
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
    sort_value: 0.8473
    sort_std: 0.0059
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.8026
    std: 0.0092
    paper_value: 0.8026
    paper_std: 0.0092
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 5
    true_value: 0.8362
    true_std: 0.0017
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.033600000000000074
    value_note: ''
    paper_rank: 25
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.8362
    sort_std: 0.0017
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7792
    std: 0.0093
    paper_value: 0.7792
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 8
    true_value: 0.8341
    true_std: 0.0034
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05489999999999995
    value_note: ''
    paper_rank: 47
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.8341
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8107
    std: 0.0054
    paper_value: 0.8107
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 9
    true_value: 0.8322
    true_std: 0.0078
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021500000000000075
    value_note: ''
    paper_rank: 15
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.8322
    sort_std: 0.0078
    is_best: false
  - model: SGFormer
    model_key: sgformer
    model_plain: SGFormer
    value: 0.8005
    std: 0.0046
    paper_value: 0.8005
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 12
    true_value: 0.8271
    true_std: 0.0056
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026599999999999957
    value_note: ''
    paper_rank: 29
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.8271
    sort_std: 0.0056
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.803
    std: 0.0062
    paper_value: 0.803
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 14
    true_value: 0.8232
    true_std: 0.0069
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020199999999999996
    value_note: ''
    paper_rank: 21
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8232
    sort_std: 0.0069
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.8148
    std: 0.0046
    paper_value: 0.8148
    paper_std: 0.0046
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 15
    true_value: 0.8148
    true_std: 0.0046
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8148
    sort_std: 0.0046
    is_best: false
  - model: NodeFormer
    model_key: nodeformer
    model_plain: NodeFormer
    value: 0.7513
    std: 0.0093
    paper_value: 0.7513
    paper_std: 0.0093
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 16
    true_value: 0.8103
    true_std: 0.0094
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05900000000000005
    value_note: ''
    paper_rank: 51
    rank_delta: 35
    rank_delta_abs: 35
    rank_delta_direction: worse
    sort_value: 0.8103
    sort_std: 0.0094
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8069
    std: 0.0031
    paper_value: 0.8069
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 20
    true_value: 0.8069
    true_std: 0.0031
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8069
    sort_std: 0.0031
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7938
    std: 0.0082
    paper_value: 0.7938
    paper_std: 0.0082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 36
    true_value: 0.7938
    true_std: 0.0082
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7938
    sort_std: 0.0082
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 39
    true_value: 0.7926
    true_std: 0.0057
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.006000000000000005
    value_note: ''
    paper_rank: 43
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.7926
    sort_std: 0.0057
    is_best: false
  - model: GOAT
    model_key: goat
    model_plain: GOAT
    value: 0.7796
    std: 0.0003
    paper_value: 0.7796
    paper_std: 0.0003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 47
    true_value: 0.7796
    true_std: 0.0003
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7796
    sort_std: 0.0003
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.132
    std: 0.005
    paper_value: 0.132
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (Appendix)
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 77
    true_value: 0.066
    true_std: 0.003
    value_gap_source_arxiv: '2604.17324'
    value_gap_source_title: 'SigGate-GT: Taming Over-Smoothing in Graph Transformers
      via Sigmoid-Gated Attention'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.066
    value_note: ''
    paper_rank: 223
    rank_delta: 146
    rank_delta_abs: 146
    rank_delta_direction: worse
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
    table_ref: Table 3 (Appendix)
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.074
    std: 0.012
    paper_value: 0.074
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (Appendix)
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 124
    true_value: 0.074
    true_std: 0.012
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.074
    sort_std: 0.012
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.367
    std: 0.011
    paper_value: 0.367
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3 (Appendix)
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.291
    value_note: ''
    paper_rank: 285
    rank_delta: 154
    rank_delta_abs: 154
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
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
    table_ref: Table 3 (Appendix)
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 142
    true_value: 0.0776354896230479
    true_std: 0.005512609666895327
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3063645103769521
    value_note: ''
    paper_rank: 285
    rank_delta: 143
    rank_delta_abs: 143
    rank_delta_direction: worse
    sort_value: 0.0776354896230479
    sort_std: 0.005512609666895327
    is_best: false
  metric: MAE
  higher_is_better: false
- &id017
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
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
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.7276
    std: 0.0019
    paper_value: 0.7276
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 32
    true_value: 0.7276
    true_std: 0.0019
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7276
    sort_std: 0.0019
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.7178
    std: 0.0026
    paper_value: 0.7178
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 38
    true_value: 0.7248
    true_std: 0.0
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007000000000000006
    value_note: ''
    paper_rank: 62
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.7248
    sort_std: 0.0
    is_best: false
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.7244
    std: 0.0028
    paper_value: 0.7244
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 41
    true_value: 0.7244
    true_std: 0.0028
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7244
    sort_std: 0.0028
    is_best: false
  - model: Graph Mamba-1
    model_key: graph mamba-1
    model_plain: Graph Mamba-1
    value: 0.7178
    std: 0.0026
    paper_value: 0.7178
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 63
    true_value: 0.7178
    true_std: 0.0026
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 63
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7178
    sort_std: 0.0026
    is_best: false
  - model: Nagphormer
    model_key: nagphormer
    model_plain: Nagphormer
    value: 0.7152
    std: 0.0024
    paper_value: 0.7152
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 67
    true_value: 0.7152
    true_std: 0.0024
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7152
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id018
  dataset: ogbn-products
  rows:
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.9334
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9334
    sort_std: 0.0006
    is_best: true
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
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 2
    true_value: 0.9115
    true_std: 0.0004
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15510000000000002
    value_note: ''
    paper_rank: 35
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.9115
    sort_std: 0.0004
    is_best: false
  - model: GLEM-GNN
    model_key: glem-gnn
    model_plain: GLEM-GNN
    value: 0.8736
    std: 0.0007
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
    global_rank: 3
    sort_value: 0.8736
    sort_std: 0.0007
    is_best: false
  - model: GLEM-LM
    model_key: glem-lm
    model_plain: GLEM-LM
    value: 0.8483
    std: 0.0004
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
    global_rank: 4
    sort_value: 0.8483
    sort_std: 0.0004
    is_best: false
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.7944
    std: 0.0032
    paper_value: 0.7944
    paper_std: 0.0032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 21
    true_value: 0.7944
    true_std: 0.0032
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7944
    sort_std: 0.0032
    is_best: false
  - model: Graph-Mamba
    model_key: graph-mamba
    model_plain: Graph-Mamba
    value: 0.7477
    std: 0.0045
    paper_value: 0.7477
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
    date: Jan 2024
    date_display: Jan 2024
    date_iso: 2024-01
    global_rank: 40
    true_value: 0.7477
    true_std: 0.0045
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7477
    sort_std: 0.0045
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
  - *id005
  - *id006
- benchmark: Heterophilic Graphs
  datasets:
  - *id007
  - *id008
  - *id009
  - *id010
  - *id011
- benchmark: LRGB
  datasets:
  - *id012
  - *id013
  - *id014
  - *id015
  - *id016
- benchmark: OGB
  datasets:
  - *id017
  - *id018
main_figure: /figures/2401.01233/main_figure.png
---

