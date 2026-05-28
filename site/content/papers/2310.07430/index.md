---
title: Non-backtracking Graph Neural Networks
arxiv_id: '2310.07430'
source_url: ''
authors: []
published_date: Oct 2023
published_date_iso: 2023-10
abstract: The celebrated message-passing updates for graph neural networks allow representing
  large-scale graphs with local and computationally tractable updates. However, the
  updates suffer from backtracking, i.e., a message flowing through the same edge
  twice and revisiting the previously visited node. Since the number of message flows
  increases exponentially with the number of updates, the redundancy in local updates
  prevents the graph neural network from accurately recognizing a particular message
  flow relevant for downstream tasks. In this work, we propose to resolve such a redundancy
  issue via the non-backtracking graph neural network (NBA-GNN) that updates a message
  without incorporating the message from the previously visited node. We theoretically
  investigate how NBA-GNN alleviates the over-squashing of GNNs, and establish a connection
  between NBA-GNN and the impressive performance of non-backtracking updates for stochastic
  block model recovery. Furthermore, we empirically verify the effectiveness of our
  NBA-GNN on the long-range graph benchmark and transductive node classification problems.
  $^ $ Equal Contribution, $^ $ Co-corresponding author.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- NBA-GCN
- NBA-GCN+LapPE
- NBA-GIN
- NBA-GatedGCN
- GraphSAGE + NBA
- GAT + NBA
- GAT + NBA+LapPE
- ChebNet + NBA
- ChebNet + NBA+LapPE
mrr: 0.0101
adjusted_mrr: 0.0101
mrr_dataset_count: 5
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
task_categories:
- graph_classification
- graph_regression
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id002
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7532
    std: 0.0134
    paper_value: 0.7532
    paper_std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 12
    true_value: 0.8139
    true_std: 0.0123
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.060699999999999976
    value_note: ''
    paper_rank: 80
    rank_delta: 68
    rank_delta_abs: 68
    rank_delta_direction: worse
    sort_value: 0.8139
    sort_std: 0.0123
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7463
    std: 0.0159
    paper_value: 0.7463
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 19
    true_value: 0.8052
    true_std: 0.0071
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05890000000000006
    value_note: ''
    paper_rank: 92
    rank_delta: 73
    rank_delta_abs: 73
    rank_delta_direction: worse
    sort_value: 0.8052
    sort_std: 0.0071
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7559
    std: 0.0161
    paper_value: 0.7559
    paper_std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 34
    true_value: 0.7923
    true_std: 0.0053
    value_gap_source_arxiv: '2405.03481'
    value_gap_source_title: 'AnchorGT: Efficient and Flexible Attention Architecture
      for Scalable Graph Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03639999999999999
    value_note: ''
    paper_rank: 76
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.7923
    sort_std: 0.0053
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.7399
    std: 0.016
    paper_value: 0.7399
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 35
    true_value: 0.7911
    true_std: 0.0075
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05120000000000002
    value_note: ''
    paper_rank: 100
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.7911
    sort_std: 0.0075
    is_best: false
  - model: GraphSAGE + LapPE
    model_key: graphsage + lappe
    model_plain: GraphSAGE + LapPE
    value: 0.7621
    std: 0.0172
    paper_value: 0.7621
    paper_std: 0.0172
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 65
    true_value: 0.7621
    true_std: 0.0172
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7621
    sort_std: 0.0172
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.7609
    std: 0.0186
    paper_value: 0.7609
    paper_std: 0.0186
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 67
    true_value: 0.7609
    true_std: 0.0186
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7609
    sort_std: 0.0186
    is_best: false
  - model: GraphSAGE + NBA
    model_key: graphsage + nba
    model_plain: GraphSAGE + NBA
    value: 0.7586
    std: 0.0213
    paper_value: 0.7586
    paper_std: 0.0213
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 70
    true_value: 0.7586
    true_std: 0.0213
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7586
    sort_std: 0.0213
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.7585
    std: 0.0175
    paper_value: 0.7585
    paper_std: 0.0175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 71
    true_value: 0.7585
    true_std: 0.0175
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7585
    sort_std: 0.0175
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.7572
    std: 0.0132
    paper_value: 0.7572
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 74
    true_value: 0.7572
    true_std: 0.0132
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7572
    sort_std: 0.0132
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.7567
    std: 0.0221
    paper_value: 0.7567
    paper_std: 0.0221
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 75
    true_value: 0.7567
    true_std: 0.0221
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7567
    sort_std: 0.0221
    is_best: false
  - model: GAT + NBA+LapPE
    model_key: gat + nba+lappe
    model_plain: GAT + NBA+LapPE
    value: 0.7561
    std: 0.0175
    paper_value: 0.7561
    paper_std: 0.0175
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 76
    true_value: 0.7561
    true_std: 0.0175
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7561
    sort_std: 0.0175
    is_best: false
  - model: GAT + NBA
    model_key: gat + nba
    model_plain: GAT + NBA
    value: 0.7549
    std: 0.0171
    paper_value: 0.7549
    paper_std: 0.0171
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 78
    true_value: 0.7549
    true_std: 0.0171
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7549
    sort_std: 0.0171
    is_best: false
  - model: CensNet
    model_key: censnet
    model_plain: CensNet
    value: 0.7516
    std: 0.0162
    paper_value: 0.7516
    paper_std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 84
    true_value: 0.7516
    true_std: 0.0162
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7516
    sort_std: 0.0162
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.7512
    std: 0.0154
    paper_value: 0.7512
    paper_std: 0.0154
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 85
    true_value: 0.7512
    true_std: 0.0154
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7512
    sort_std: 0.0154
    is_best: false
  - model: ChebNet + NBA+LapPE
    model_key: chebnet + nba+lappe
    model_plain: ChebNet + NBA+LapPE
    value: 0.7421
    std: 0.0137
    paper_value: 0.7421
    paper_std: 0.0137
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 100
    true_value: 0.7421
    true_std: 0.0137
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 100
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7421
    sort_std: 0.0137
    is_best: false
  - model: ChebNet + LapPE
    model_key: chebnet + lappe
    model_plain: ChebNet + LapPE
    value: 0.7396
    std: 0.0241
    paper_value: 0.7396
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 101
    true_value: 0.7396
    true_std: 0.0241
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7396
    sort_std: 0.0241
    is_best: false
  - model: ChebNet + NBA
    model_key: chebnet + nba
    model_plain: ChebNet + NBA
    value: 0.7379
    std: 0.0099
    paper_value: 0.7379
    paper_std: 0.0099
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 103
    true_value: 0.7379
    true_std: 0.0099
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7379
    sort_std: 0.0099
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.7325
    std: 0.0192
    paper_value: 0.7325
    paper_std: 0.0192
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 109
    true_value: 0.7325
    true_std: 0.0192
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7325
    sort_std: 0.0192
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
    value: 0.8694
    std: 0.0119
    paper_value: 0.8694
    paper_std: 0.0119
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 31
    true_value: 0.8825
    true_std: 0.0053
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0131
    value_note: ''
    paper_rank: 68
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.8825
    sort_std: 0.0053
    is_best: false
  - model: ChebNet + NBA
    model_key: chebnet + nba
    model_plain: ChebNet + NBA
    value: 0.8823
    std: 0.0159
    paper_value: 0.8823
    paper_std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.8823
    true_std: 0.0159
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8823
    sort_std: 0.0159
    is_best: false
  - model: ChebNet + NBA+LapPE
    model_key: chebnet + nba+lappe
    model_plain: ChebNet + NBA+LapPE
    value: 0.8795
    std: 0.0217
    paper_value: 0.8795
    paper_std: 0.0217
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 42
    true_value: 0.8795
    true_std: 0.0217
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 42
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8795
    sort_std: 0.0217
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8658
    std: 0.006
    paper_value: 0.8658
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 48
    true_value: 0.8778
    true_std: 0.0096
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01200000000000001
    value_note: ''
    paper_rank: 82
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.8778
    sort_std: 0.0096
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.8769
    std: 0.0125
    paper_value: 0.8769
    paper_std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 51
    true_value: 0.8769
    true_std: 0.0125
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8769
    sort_std: 0.0125
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.8722
    std: 0.0095
    paper_value: 0.8722
    paper_std: 0.0095
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.8722
    true_std: 0.0095
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8722
    sort_std: 0.0095
    is_best: false
  - model: GAT + NBA
    model_key: gat + nba
    model_plain: GAT + NBA
    value: 0.8722
    std: 0.012
    paper_value: 0.8722
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 62
    true_value: 0.8722
    true_std: 0.012
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8722
    sort_std: 0.012
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.872
    std: 0.0129
    paper_value: 0.872
    paper_std: 0.0129
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.872
    true_std: 0.0129
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.872
    sort_std: 0.0129
    is_best: false
  - model: GraphSAGE + NBA
    model_key: graphsage + nba
    model_plain: GraphSAGE + NBA
    value: 0.8702
    std: 0.0083
    paper_value: 0.8702
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 66
    true_value: 0.8702
    true_std: 0.0083
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8702
    sort_std: 0.0083
    is_best: false
  - model: GAT + NBA+LapPE
    model_key: gat + nba+lappe
    model_plain: GAT + NBA+LapPE
    value: 0.8692
    std: 0.0098
    paper_value: 0.8692
    paper_std: 0.0098
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 70
    true_value: 0.8692
    true_std: 0.0098
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8692
    sort_std: 0.0098
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8632
    std: 0.0158
    paper_value: 0.8632
    paper_std: 0.0158
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 71
    true_value: 0.8690000000000001
    true_std: 0.0104
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005800000000000138
    value_note: global 0.8690 within std
    paper_rank: 86
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.8690000000000001
    sort_std: 0.0104
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.8686
    std: 0.0152
    paper_value: 0.8686
    paper_std: 0.0152
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 73
    true_value: 0.8686
    true_std: 0.0152
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8686
    sort_std: 0.0152
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8523
    std: 0.011
    paper_value: 0.8523
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 77
    true_value: 0.8667
    true_std: 0.0082
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.01440000000000008
    value_note: ''
    paper_rank: 100
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.8667
    sort_std: 0.0082
    is_best: false
  - model: GraphSAGE + LapPE
    model_key: graphsage + lappe
    model_plain: GraphSAGE + LapPE
    value: 0.865
    std: 0.012
    paper_value: 0.865
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 84
    true_value: 0.865
    true_std: 0.012
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.865
    sort_std: 0.012
    is_best: false
  - model: CensNet
    model_key: censnet
    model_plain: CensNet
    value: 0.8648
    std: 0.0138
    paper_value: 0.8648
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 85
    true_value: 0.8648
    true_std: 0.0138
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8648
    sort_std: 0.0138
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.8592
    std: 0.0083
    paper_value: 0.8592
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 90
    true_value: 0.8592
    true_std: 0.0083
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8592
    sort_std: 0.0083
    is_best: false
  - model: ChebNet + LapPE
    model_key: chebnet + lappe
    model_plain: ChebNet + LapPE
    value: 0.8531
    std: 0.0139
    paper_value: 0.8531
    paper_std: 0.0139
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 98
    true_value: 0.8531
    true_std: 0.0139
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8531
    sort_std: 0.0139
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8477
    std: 0.0156
    paper_value: 0.8477
    paper_std: 0.0156
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 106
    true_value: 0.8477
    true_std: 0.0156
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8477
    sort_std: 0.0156
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Cornell
  rows:
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9525
    std: 0.0155
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
    sort_value: 0.9525
    sort_std: 0.0155
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9393
    std: 0.0105
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
    global_rank: 2
    sort_value: 0.9393
    sort_std: 0.0105
    is_best: true
  - model: ACM-SGC-1
    model_key: acm-sgc-1
    model_plain: ACM-SGC-1
    value: 0.9377
    std: 0.0217
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
    global_rank: 3
    sort_value: 0.9377
    sort_std: 0.0217
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5946
    std: 0.0662
    paper_value: 0.5946
    paper_std: 0.0662
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.22999999999999998
    value_note: ''
    paper_rank: 101
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.6027
    std: 0.0625
    paper_value: 0.6027
    paper_std: 0.0625
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 30
    true_value: 0.8008
    true_std: 0.0296
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19809999999999994
    value_note: ''
    paper_rank: 99
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.8008
    sort_std: 0.0296
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4757
    std: 0.0614
    paper_value: 0.4757
    paper_std: 0.0614
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 37
    true_value: 0.76
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2843
    value_note: ''
    paper_rank: 131
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.0101
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.6473
    std: 0.052
    paper_value: 0.6473
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 43
    true_value: 0.743
    true_std: 0.0746
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09570000000000001
    value_note: ''
    paper_rank: 91
    rank_delta: 48
    rank_delta_abs: 48
    rank_delta_direction: worse
    sort_value: 0.743
    sort_std: 0.0746
    is_best: false
  - model: ChebNet + NBA
    model_key: chebnet + nba
    model_plain: ChebNet + NBA
    value: 0.6973
    std: 0.0483
    paper_value: 0.6973
    paper_std: 0.0483
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 68
    true_value: 0.6973
    true_std: 0.0483
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6973
    sort_std: 0.0483
    is_best: false
  - model: ChebNet + NBA+LapPE
    model_key: chebnet + nba+lappe
    model_plain: ChebNet + NBA+LapPE
    value: 0.6757
    std: 0.0634
    paper_value: 0.6757
    paper_std: 0.0634
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 77
    true_value: 0.6757
    true_std: 0.0634
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6757
    sort_std: 0.0634
    is_best: false
  - model: ChebNet + LapPE
    model_key: chebnet + lappe
    model_plain: ChebNet + LapPE
    value: 0.6527
    std: 0.0506
    paper_value: 0.6527
    paper_std: 0.0506
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 88
    true_value: 0.6527
    true_std: 0.0506
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0506
    is_best: false
  - model: GraphSAGE + NBA
    model_key: graphsage + nba
    model_plain: GraphSAGE + NBA
    value: 0.6459
    std: 0.0691
    paper_value: 0.6459
    paper_std: 0.0691
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 92
    true_value: 0.6459
    true_std: 0.0691
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6459
    sort_std: 0.0691
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.6378
    std: 0.0317
    paper_value: 0.6378
    paper_std: 0.0317
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 95
    true_value: 0.6378
    true_std: 0.0317
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6378
    sort_std: 0.0317
    is_best: false
  - model: GraphSAGE + LapPE
    model_key: graphsage + lappe
    model_plain: GraphSAGE + LapPE
    value: 0.6378
    std: 0.0544
    paper_value: 0.6378
    paper_std: 0.0544
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 96
    true_value: 0.6378
    true_std: 0.0544
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6378
    sort_std: 0.0544
    is_best: false
  - model: CensNet
    model_key: censnet
    model_plain: CensNet
    value: 0.6162
    std: 0.0707
    paper_value: 0.6162
    paper_std: 0.0707
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 97
    true_value: 0.6162
    true_std: 0.0707
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6162
    sort_std: 0.0707
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.6108
    std: 0.0614
    paper_value: 0.6108
    paper_std: 0.0614
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 98
    true_value: 0.6108
    true_std: 0.0614
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6108
    sort_std: 0.0614
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.5946
    std: 0.0573
    paper_value: 0.5946
    paper_std: 0.0573
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 102
    true_value: 0.5946
    true_std: 0.0573
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5946
    sort_std: 0.0573
    is_best: false
  - model: GAT + NBA
    model_key: gat + nba
    model_plain: GAT + NBA
    value: 0.5838
    std: 0.0558
    paper_value: 0.5838
    paper_std: 0.0558
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 104
    true_value: 0.5838
    true_std: 0.0558
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5838
    sort_std: 0.0558
    is_best: false
  - model: GAT + NBA+LapPE
    model_key: gat + nba+lappe
    model_plain: GAT + NBA+LapPE
    value: 0.5784
    std: 0.064
    paper_value: 0.5784
    paper_std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 106
    true_value: 0.5784
    true_std: 0.064
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5784
    sort_std: 0.064
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.5703
    std: 0.0547
    paper_value: 0.5703
    paper_std: 0.0547
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 111
    true_value: 0.5703
    true_std: 0.0547
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5703
    sort_std: 0.0547
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5216
    std: 0.0987
    paper_value: 0.5216
    paper_std: 0.0987
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 122
    true_value: 0.5216
    true_std: 0.0987
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5216
    sort_std: 0.0987
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.5108
    std: 0.0769
    paper_value: 0.5108
    paper_std: 0.0769
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 125
    true_value: 0.5108
    true_std: 0.0769
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5108
    sort_std: 0.0769
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 25
    true_value: 0.4191
    true_std: 0.0126
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: Exphormer
    model_key: exphormer
    model_plain: Exphormer
    value: 0.3966
    std: 0.0027
    paper_value: 0.3966
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 35
    true_value: 0.3975
    true_std: 0.0037
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.3975 within std
    paper_rank: 37
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.3975
    sort_std: 0.0037
    is_best: false
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
    value: 0.3969
    std: 0.0027
    paper_value: 0.3969
    paper_std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 36
    true_value: 0.3969
    true_std: 0.0027
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3969
    sort_std: 0.0027
    is_best: false
  - model: NBA-GatedGCN
    model_key: nba-gatedgcn
    model_plain: NBA-GatedGCN
    value: 0.391
    std: 0.001
    paper_value: 0.391
    paper_std: 0.001
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 40
    true_value: 0.391
    true_std: 0.001
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.391
    sort_std: 0.001
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 47
    true_value: 0.3748
    true_std: 0.0109
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3748
    sort_std: 0.0109
    is_best: false
  - model: DRew-GatedGCN+LapPE
    model_key: drew-gatedgcn+lappe
    model_plain: DRew-GatedGCN+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 60
    true_value: 0.3314
    true_std: 0.0024
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3314
    sort_std: 0.0024
    is_best: false
  - model: SAN+LapPE
    model_key: san+lappe
    model_plain: SAN+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.323
    true_std: 0.0039
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.323
    sort_std: 0.0039
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.3223
    std: 0.0063
    paper_value: 0.3223
    paper_std: 0.0063
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.3223
    true_std: 0.0063
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3223
    sort_std: 0.0063
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 67
    true_value: 0.3189
    true_std: 0.0105
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.19240000000000002
    value_note: ''
    paper_rank: 109
    rank_delta: 42
    rank_delta_abs: 42
    rank_delta_direction: worse
    sort_value: 0.3189
    sort_std: 0.0105
    is_best: false
  - model: NBA-GIN
    model_key: nba-gin
    model_plain: NBA-GIN
    value: 0.304
    std: 0.0119
    paper_value: 0.304
    paper_std: 0.0119
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 72
    true_value: 0.304
    true_std: 0.0119
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.304
    sort_std: 0.0119
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.2921
    std: 0.0038
    paper_value: 0.2921
    paper_std: 0.0038
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 74
    true_value: 0.2921
    true_std: 0.0038
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2921
    sort_std: 0.0038
    is_best: false
  - model: DIGL+MPNN
    model_key: digl+mpnn
    model_plain: DIGL+MPNN
    value: 0.2824
    std: 0.0039
    paper_value: 0.2824
    paper_std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 77
    true_value: 0.2824
    true_std: 0.0039
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2824
    sort_std: 0.0039
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 81
    true_value: 0.2694
    true_std: 0.0098
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2694
    sort_std: 0.0098
    is_best: false
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.2692
    std: 0.0059
    paper_value: 0.2692
    paper_std: 0.0059
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 84
    true_value: 0.2692
    true_std: 0.0059
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2692
    sort_std: 0.0059
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.2537
    std: 0.0054
    paper_value: 0.2537
    paper_std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 88
    true_value: 0.2537
    true_std: 0.0054
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2537
    sort_std: 0.0054
    is_best: false
  - model: MixHop-GCN
    model_key: mixhop-gcn
    model_plain: MixHop-GCN
    value: 0.2506
    std: 0.0133
    paper_value: 0.2506
    paper_std: 0.0133
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 89
    true_value: 0.2506
    true_std: 0.0133
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2506
    sort_std: 0.0133
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.2218
    std: 0.0174
    paper_value: 0.2218
    paper_std: 0.0174
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 92
    true_value: 0.2218
    true_std: 0.0174
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2218
    sort_std: 0.0174
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.137
    std: 0.0077
    paper_value: 0.137
    paper_std: 0.0077
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 108
    true_value: 0.137
    true_std: 0.0077
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.137
    sort_std: 0.0077
    is_best: false
  - model: GINE + LapPE
    model_key: gine + lappe
    model_plain: GINE + LapPE
    value: 0.1302
    std: 0.0105
    paper_value: 0.1302
    paper_std: 0.0105
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 109
    true_value: 0.1302
    true_std: 0.0105
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.1302
    sort_std: 0.0105
    is_best: false
  metric: F1
  higher_is_better: true
- &id007
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.7126
    std: 0.0045
    paper_value: 0.7126
    paper_std: 0.0045
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 23
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0023999999999999577
    value_note: global 0.7150 within std
    paper_rank: 32
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.7071
    std: 0.0067
    paper_value: 0.7071
    paper_std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 39
    true_value: 0.7071
    true_std: 0.0067
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7071
    sort_std: 0.0067
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 41
    true_value: 0.7059
    true_std: 0.0089
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.15610000000000002
    value_note: ''
    paper_rank: 288
    rank_delta: 247
    rank_delta_abs: 247
    rank_delta_direction: worse
    sort_value: 0.7059
    sort_std: 0.0089
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
    value: 0.6982
    std: 0.0014
    paper_value: 0.6982
    paper_std: 0.0014
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 56
    true_value: 0.6982
    true_std: 0.0014
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6982
    sort_std: 0.0014
    is_best: false
  - model: DRew-GatedGCN+LapPE
    model_key: drew-gatedgcn+lappe
    model_plain: DRew-GatedGCN+LapPE
    value: 0.6977
    std: 0.0026
    paper_value: 0.6977
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 57
    true_value: 0.6977
    true_std: 0.0026
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6977
    sort_std: 0.0026
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: NBA-GIN
    model_key: nba-gin
    model_plain: NBA-GIN
    value: 0.6961
    std: 0.0045
    paper_value: 0.6961
    paper_std: 0.0045
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 67
    true_value: 0.6961
    true_std: 0.0045
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6961
    sort_std: 0.0045
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.6951
    std: 0.0024
    paper_value: 0.6951
    paper_std: 0.0024
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 71
    true_value: 0.6951
    true_std: 0.0024
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6951
    sort_std: 0.0024
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.6843
    std: 0.0049
    paper_value: 0.6843
    paper_std: 0.0049
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 93
    true_value: 0.6843
    true_std: 0.0049
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6843
    sort_std: 0.0049
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.683
    std: 0.0026
    paper_value: 0.683
    paper_std: 0.0026
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 96
    true_value: 0.683
    true_std: 0.0026
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
    sort_value: 0.683
    sort_std: 0.0026
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 105
    true_value: 0.6816
    true_std: 0.0026
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6816
    sort_std: 0.0026
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: MixHop-GCN
    model_key: mixhop-gcn
    model_plain: MixHop-GCN
    value: 0.6592
    std: 0.0036
    paper_value: 0.6592
    paper_std: 0.0036
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 156
    true_value: 0.6592
    true_std: 0.0036
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 156
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6592
    sort_std: 0.0036
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.6569
    std: 0.0117
    paper_value: 0.6569
    paper_std: 0.0117
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 165
    true_value: 0.6569
    true_std: 0.0117
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6569
    sort_std: 0.0117
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 169
    true_value: 0.6535
    true_std: 0.0040999999999999995
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6535
    sort_std: 0.0040999999999999995
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: DIGL+MPNN
    model_key: digl+mpnn
    model_plain: DIGL+MPNN
    value: 0.6469
    std: 0.0019
    paper_value: 0.6469
    paper_std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 189
    true_value: 0.6469
    true_std: 0.0019
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 189
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6469
    sort_std: 0.0019
    is_best: false
  - model: NBA-GatedGCN
    model_key: nba-gatedgcn
    model_plain: NBA-GatedGCN
    value: 0.6429
    std: 0.0062
    paper_value: 0.6429
    paper_std: 0.0062
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 205
    true_value: 0.6429
    true_std: 0.0062
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 205
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6429
    sort_std: 0.0062
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 212
    true_value: 0.6384000000000001
    true_std: 0.0121
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384000000000001
    sort_std: 0.0121
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 217
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.6213
    std: 0.006
    paper_value: 0.6213
    paper_std: 0.006
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 233
    true_value: 0.6218
    true_std: 0.0055
    value_gap_source_arxiv: '2307.07107'
    value_gap_source_title: Graph Positional and Structural Encoder
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000500000000000056
    value_note: global 0.6218 within std
    paper_rank: 234
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.6218
    sort_std: 0.0055
    is_best: false
  - model: GINE + LapPE
    model_key: gine + lappe
    model_plain: GINE + LapPE
    value: 0.5877
    std: 0.0044
    paper_value: 0.5877
    paper_std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 270
    true_value: 0.5877
    true_std: 0.0044
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 270
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5877
    sort_std: 0.0044
    is_best: false
  metric: AP
  higher_is_better: true
- &id008
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
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.2424
    std: 0.001
    paper_value: 0.2424
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 7
    true_value: 0.2424
    true_std: 0.001
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2424
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.3547
    std: 0.0045
    paper_value: 0.3547
    paper_std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 9
    true_value: 0.2429
    true_std: 0.0019
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11180000000000001
    value_note: ''
    paper_rank: 311
    rank_delta: 302
    rank_delta_abs: 302
    rank_delta_direction: worse
    sort_value: 0.2429
    sort_std: 0.0019
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
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
  - model: GatedGCN+LapPE
    model_key: gatedgcn+lappe
    model_plain: GatedGCN+LapPE
    value: 0.2466
    std: 0.0012
    paper_value: 0.2466
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 68
    true_value: 0.2466
    true_std: 0.0012
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2466
    sort_std: 0.0012
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
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
    value: 0.2481
    std: 0.0007
    paper_value: 0.2481
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 102
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GraphGPS+LapPE
    model_key: graphgps+lappe
    model_plain: GraphGPS+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 138
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.2523
    std: 0.0013
    paper_value: 0.2523
    paper_std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 163
    true_value: 0.2523
    true_std: 0.0013
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2523
    sort_std: 0.0013
    is_best: false
  - model: Transformer+LapPE
    model_key: transformer+lappe
    model_plain: Transformer+LapPE
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 168
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: LRGB
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: DRew-GCN+LapPE
    model_key: drew-gcn+lappe
    model_plain: DRew-GCN+LapPE
    value: 0.2606
    std: 0.0014
    paper_value: 0.2606
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 175
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007000000000000006
    value_note: ''
    paper_rank: 214
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  - model: DRew-GatedGCN+LapPE
    model_key: drew-gatedgcn+lappe
    model_plain: DRew-GatedGCN+LapPE
    value: 0.2539
    std: 0.0007
    paper_value: 0.2539
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 179
    true_value: 0.2539
    true_std: 0.0007
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 179
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2539
    sort_std: 0.0007
    is_best: false
  - model: NBA-GatedGCN
    model_key: nba-gatedgcn
    model_plain: NBA-GatedGCN
    value: 0.2539
    std: 0.0011
    paper_value: 0.2539
    paper_std: 0.0011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 180
    true_value: 0.2539
    true_std: 0.0011
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 180
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2539
    sort_std: 0.0011
    is_best: false
  - model: PathNN
    model_key: pathnn
    model_plain: PathNN
    value: 0.2545
    std: 0.0032
    paper_value: 0.2545
    paper_std: 0.0032
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 181
    true_value: 0.254
    true_std: 0.0046
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0005000000000000004
    value_note: global 0.2540 within std
    paper_rank: 187
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.254
    sort_std: 0.0046
    is_best: false
  - model: MixHop-GCN+LapPE
    model_key: mixhop-gcn+lappe
    model_plain: MixHop-GCN+LapPE
    value: 0.2614
    std: 0.0023
    paper_value: 0.2614
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 217
    true_value: 0.2614
    true_std: 0.0023
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 217
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2614
    sort_std: 0.0023
    is_best: false
  - model: DIGL+MPNN+LapPE
    model_key: digl+mpnn+lappe
    model_plain: DIGL+MPNN+LapPE
    value: 0.2616
    std: 0.0018
    paper_value: 0.2616
    paper_std: 0.0018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 218
    true_value: 0.2616
    true_std: 0.0018
    value_gap_source_arxiv: '2510.02565'
    value_gap_source_title: On The Expressive Power of GNN Derivatives
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 218
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2616
    sort_std: 0.0018
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.2656
    std: 0.0009
    paper_value: 0.2656
    paper_std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 236
    true_value: 0.2656
    true_std: 0.0009
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 236
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2656
    sort_std: 0.0009
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 242
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
    paper_rank: 242
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: NBA-GIN
    model_key: nba-gin
    model_plain: NBA-GIN
    value: 0.2775
    std: 0.0057
    paper_value: 0.2775
    paper_std: 0.0057
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 255
    true_value: 0.2775
    true_std: 0.0057
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 255
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2775
    sort_std: 0.0057
    is_best: false
  - model: MixHop-GCN
    model_key: mixhop-gcn
    model_plain: MixHop-GCN
    value: 0.2921
    std: 0.0023
    paper_value: 0.2921
    paper_std: 0.0023
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 264
    true_value: 0.2921
    true_std: 0.0023
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 264
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2921
    sort_std: 0.0023
    is_best: false
  - model: DIGL+MPNN
    model_key: digl+mpnn
    model_plain: DIGL+MPNN
    value: 0.3173
    std: 0.0007
    paper_value: 0.3173
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 284
    true_value: 0.3173
    true_std: 0.0007
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 284
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3173
    sort_std: 0.0007
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.325
    std: 0.018
    paper_value: 0.325
    paper_std: 0.018
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 287
    true_value: 0.3195
    true_std: 0.0014
    value_gap_source_arxiv: '2512.15549'
    value_gap_source_title: Photonics-Enhanced Graph Convolutional Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005500000000000005
    value_note: global 0.3195 within std
    paper_rank: 287
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3195
    sort_std: 0.0014
    is_best: false
  - model: GINE + LapPE
    model_key: gine + lappe
    model_plain: GINE + LapPE
    value: 0.3369
    std: 0.0026
    paper_value: 0.3369
    paper_std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 290
    true_value: 0.3369
    true_std: 0.0026
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 290
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3369
    sort_std: 0.0026
    is_best: false
  metric: MAE
  higher_is_better: false
- &id003
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
    value: 0.8825
    std: 0.0042
    paper_value: 0.8825
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 5
    true_value: 0.9224
    true_std: 0.0123
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03990000000000005
    value_note: ''
    paper_rank: 65
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.9224
    sort_std: 0.0123
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8787
    std: 0.0046
    paper_value: 0.8787
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 6
    true_value: 0.9201
    true_std: 0.0024
    value_gap_source_arxiv: '2511.16767'
    value_gap_source_title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed
      Graphs as Effectively as We Expected'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04139999999999999
    value_note: ''
    paper_rank: 73
    rank_delta: 67
    rank_delta_abs: 67
    rank_delta_direction: worse
    sort_value: 0.9201
    sort_std: 0.0024
    is_best: false
  - model: GraphSAGE + NBA
    model_key: graphsage + nba
    model_plain: GraphSAGE + NBA
    value: 0.8871
    std: 0.0044
    paper_value: 0.8871
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 52
    true_value: 0.8871
    true_std: 0.0044
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8871
    sort_std: 0.0044
    is_best: false
  - model: GraphSAGE + LapPE
    model_key: graphsage + lappe
    model_plain: GraphSAGE + LapPE
    value: 0.887
    std: 0.0037
    paper_value: 0.887
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 53
    true_value: 0.887
    true_std: 0.0037
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.887
    sort_std: 0.0037
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8864
    std: 0.003
    paper_value: 0.8864
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 54
    true_value: 0.8864
    true_std: 0.003
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8864
    sort_std: 0.003
    is_best: false
  - model: ChebNet + NBA
    model_key: chebnet + nba
    model_plain: ChebNet + NBA
    value: 0.8832
    std: 0.0062
    paper_value: 0.8832
    paper_std: 0.0062
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 60
    true_value: 0.8832
    true_std: 0.0062
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8832
    sort_std: 0.0062
    is_best: false
  - model: GAT + NBA
    model_key: gat + nba
    model_plain: GAT + NBA
    value: 0.8829
    std: 0.0043
    paper_value: 0.8829
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 62
    true_value: 0.8829
    true_std: 0.0043
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8829
    sort_std: 0.0043
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.8827
    std: 0.0048
    paper_value: 0.8827
    paper_std: 0.0048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.8827
    true_std: 0.0048
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8827
    sort_std: 0.0048
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.8826
    std: 0.0044
    paper_value: 0.8826
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 65
    true_value: 0.8826
    true_std: 0.0044
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8826
    sort_std: 0.0044
    is_best: false
  - model: GAT + NBA+LapPE
    model_key: gat + nba+lappe
    model_plain: GAT + NBA+LapPE
    value: 0.8822
    std: 0.0047
    paper_value: 0.8822
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 66
    true_value: 0.8822
    true_std: 0.0047
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 66
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8822
    sort_std: 0.0047
    is_best: false
  - model: ChebNet + NBA+LapPE
    model_key: chebnet + nba+lappe
    model_plain: ChebNet + NBA+LapPE
    value: 0.8821
    std: 0.0076
    paper_value: 0.8821
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 68
    true_value: 0.8821
    true_std: 0.0076
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8821
    sort_std: 0.0076
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.8817
    std: 0.004
    paper_value: 0.8817
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 71
    true_value: 0.8817
    true_std: 0.004
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8817
    sort_std: 0.004
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8718
    std: 0.0029
    paper_value: 0.8718
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 72
    true_value: 0.8795
    true_std: 0.0028
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007699999999999929
    value_note: ''
    paper_rank: 88
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.8795
    sort_std: 0.0028
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.8775
    std: 0.0045
    paper_value: 0.8775
    paper_std: 0.0045
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 75
    true_value: 0.8775
    true_std: 0.0045
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8775
    sort_std: 0.0045
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.8769
    std: 0.0028
    paper_value: 0.8769
    paper_std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 76
    true_value: 0.8769
    true_std: 0.0028
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8769
    sort_std: 0.0028
    is_best: false
  - model: CensNet
    model_key: censnet
    model_plain: CensNet
    value: 0.8753
    std: 0.0076
    paper_value: 0.8753
    paper_std: 0.0076
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 81
    true_value: 0.8753
    true_std: 0.0076
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8753
    sort_std: 0.0076
    is_best: false
  - model: ChebNet + LapPE
    model_key: chebnet + lappe
    model_plain: ChebNet + LapPE
    value: 0.8701
    std: 0.0047
    paper_value: 0.8701
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
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 91
    true_value: 0.8701
    true_std: 0.0047
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8701
    sort_std: 0.0047
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.8671
    std: 0.006
    paper_value: 0.8671
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 93
    true_value: 0.8671
    true_std: 0.006
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8671
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.9656
    std: 0.02
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
    sort_value: 0.9656
    sort_std: 0.02
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.9574
    std: 0.0222
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
    global_rank: 2
    sort_value: 0.9574
    sort_std: 0.0222
    is_best: true
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9475
    std: 0.0309
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
    global_rank: 3
    sort_value: 0.9475
    sort_std: 0.0309
    is_best: true
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.6811
    std: 0.0554
    paper_value: 0.6811
    paper_std: 0.0554
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 32
    true_value: 0.8622
    true_std: 0.0245
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18109999999999993
    value_note: ''
    paper_rank: 117
    rank_delta: 85
    rank_delta_abs: 85
    rank_delta_direction: worse
    sort_value: 0.8622
    sort_std: 0.0245
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6162
    std: 0.0634
    paper_value: 0.6162
    paper_std: 0.0634
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21489999999999998
    value_note: ''
    paper_rank: 140
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7108
    std: 0.0556
    paper_value: 0.7108
    paper_std: 0.0556
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 51
    true_value: 0.8243
    true_std: 0.061399999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11350000000000005
    value_note: ''
    paper_rank: 111
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.8243
    sort_std: 0.061399999999999996
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6054
    std: 0.0386
    paper_value: 0.6054
    paper_std: 0.0386
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20279999999999998
    value_note: ''
    paper_rank: 145
    rank_delta: 84
    rank_delta_abs: 84
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: ChebNet + NBA
    model_key: chebnet + nba
    model_plain: ChebNet + NBA
    value: 0.7568
    std: 0.0468
    paper_value: 0.7568
    paper_std: 0.0468
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 88
    true_value: 0.7568
    true_std: 0.0468
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7568
    sort_std: 0.0468
    is_best: false
  - model: GraphSAGE + LapPE
    model_key: graphsage + lappe
    model_plain: GraphSAGE + LapPE
    value: 0.7486
    std: 0.0612
    paper_value: 0.7486
    paper_std: 0.0612
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 92
    true_value: 0.7486
    true_std: 0.0612
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7486
    sort_std: 0.0612
    is_best: false
  - model: GraphSAGE + NBA
    model_key: graphsage + nba
    model_plain: GraphSAGE + NBA
    value: 0.727
    std: 0.0905
    paper_value: 0.727
    paper_std: 0.0905
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 106
    true_value: 0.727
    true_std: 0.0905
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.0905
    is_best: false
  - model: ChebNet + NBA+LapPE
    model_key: chebnet + nba+lappe
    model_plain: ChebNet + NBA+LapPE
    value: 0.7243
    std: 0.052
    paper_value: 0.7243
    paper_std: 0.052
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 108
    true_value: 0.7243
    true_std: 0.052
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7243
    sort_std: 0.052
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.7108
    std: 0.0796
    paper_value: 0.7108
    paper_std: 0.0796
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 112
    true_value: 0.7108
    true_std: 0.0796
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7108
    sort_std: 0.0796
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.6811
    std: 0.0595
    paper_value: 0.6811
    paper_std: 0.0595
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 118
    true_value: 0.6811
    true_std: 0.0595
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 118
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6811
    sort_std: 0.0595
    is_best: false
  - model: GAT + NBA+LapPE
    model_key: gat + nba+lappe
    model_plain: GAT + NBA+LapPE
    value: 0.673
    std: 0.0348
    paper_value: 0.673
    paper_std: 0.0348
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 122
    true_value: 0.673
    true_std: 0.0348
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 122
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.673
    sort_std: 0.0348
    is_best: false
  - model: GAT + NBA
    model_key: gat + nba
    model_plain: GAT + NBA
    value: 0.6622
    std: 0.0514
    paper_value: 0.6622
    paper_std: 0.0514
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 125
    true_value: 0.6622
    true_std: 0.0514
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6622
    sort_std: 0.0514
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.6216
    std: 0.0584
    paper_value: 0.6216
    paper_std: 0.0584
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 126
    true_value: 0.6595
    true_std: 0.0367
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.037899999999999934
    value_note: global 0.6595 within std
    paper_rank: 138
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.6595
    sort_std: 0.0367
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.6595
    std: 0.0527
    paper_value: 0.6595
    paper_std: 0.0527
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 127
    true_value: 0.6595
    true_std: 0.0527
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6595
    sort_std: 0.0527
    is_best: false
  - model: CensNet
    model_key: censnet
    model_plain: CensNet
    value: 0.6405
    std: 0.051
    paper_value: 0.6405
    paper_std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 132
    true_value: 0.6405
    true_std: 0.051
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 132
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6405
    sort_std: 0.051
    is_best: false
  - model: ChebNet + LapPE
    model_key: chebnet + lappe
    model_plain: ChebNet + LapPE
    value: 0.6324
    std: 0.0308
    paper_value: 0.6324
    paper_std: 0.0308
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 135
    true_value: 0.6324
    true_std: 0.0308
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6324
    sort_std: 0.0308
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.6135
    std: 0.0404
    paper_value: 0.6135
    paper_std: 0.0404
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 142
    true_value: 0.6135
    true_std: 0.0404
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6135
    sort_std: 0.0404
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.6108
    std: 0.0652
    paper_value: 0.6108
    paper_std: 0.0652
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 144
    true_value: 0.6108
    true_std: 0.0652
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 144
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6108
    sort_std: 0.0652
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Wisconsin
  rows:
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.919
    std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.918
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.901
    std: 0.035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05593'
    title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.901
    sort_std: 0.035
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7706
    std: 0.0403
    paper_value: 0.7706
    paper_std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 36
    true_value: 0.8136
    true_std: 0.0391
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04300000000000004
    value_note: ''
    paper_rank: 68
    rank_delta: 32
    rank_delta_abs: 32
    rank_delta_direction: worse
    sort_value: 0.8136
    sort_std: 0.0391
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.7098
    std: 0.0322
    paper_value: 0.7098
    paper_std: 0.0322
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 44
    true_value: 0.8
    true_std: 0.0432
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09020000000000006
    value_note: ''
    paper_rank: 94
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.8
    sort_std: 0.0432
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6059
    std: 0.0438
    paper_value: 0.6059
    paper_std: 0.0438
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1804
    value_note: ''
    paper_rank: 115
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6
    std: 0.0491
    paper_value: 0.6
    paper_std: 0.0491
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 61
    true_value: 0.7817
    true_std: 0.057
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.18169999999999997
    value_note: ''
    paper_rank: 115
    rank_delta: 54
    rank_delta_abs: 54
    rank_delta_direction: worse
    sort_value: 0.7817
    sort_std: 0.057
    is_best: false
  - model: GraphSAGE + NBA
    model_key: graphsage + nba
    model_plain: GraphSAGE + NBA
    value: 0.7765
    std: 0.0508
    paper_value: 0.7765
    paper_std: 0.0508
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 64
    true_value: 0.7765
    true_std: 0.0508
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7765
    sort_std: 0.0508
    is_best: false
  - model: GraphSAGE + LapPE
    model_key: graphsage + lappe
    model_plain: GraphSAGE + LapPE
    value: 0.7647
    std: 0.0531
    paper_value: 0.7647
    paper_std: 0.0531
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 74
    true_value: 0.7647
    true_std: 0.0531
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7647
    sort_std: 0.0531
    is_best: false
  - model: ChebNet + NBA
    model_key: chebnet + nba
    model_plain: ChebNet + NBA
    value: 0.749
    std: 0.0671
    paper_value: 0.749
    paper_std: 0.0671
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 82
    true_value: 0.749
    true_std: 0.0671
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.749
    sort_std: 0.0671
    is_best: false
  - model: NBA-GCN
    model_key: nba-gcn
    model_plain: NBA-GCN
    value: 0.7471
    std: 0.0386
    paper_value: 0.7471
    paper_std: 0.0386
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 83
    true_value: 0.7471
    true_std: 0.0386
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7471
    sort_std: 0.0386
    is_best: false
  - model: NBA-GCN+LapPE
    model_key: nba-gcn+lappe
    model_plain: NBA-GCN+LapPE
    value: 0.7471
    std: 0.0466
    paper_value: 0.7471
    paper_std: 0.0466
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 84
    true_value: 0.7471
    true_std: 0.0466
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 84
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7471
    sort_std: 0.0466
    is_best: false
  - model: ChebNet + NBA+LapPE
    model_key: chebnet + nba+lappe
    model_plain: ChebNet + NBA+LapPE
    value: 0.7451
    std: 0.0808
    paper_value: 0.7451
    paper_std: 0.0808
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 88
    true_value: 0.7451
    true_std: 0.0808
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7451
    sort_std: 0.0808
    is_best: false
  - model: GAT + NBA+LapPE
    model_key: gat + nba+lappe
    model_plain: GAT + NBA+LapPE
    value: 0.7314
    std: 0.0531
    paper_value: 0.7314
    paper_std: 0.0531
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 92
    true_value: 0.7314
    true_std: 0.0531
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7314
    sort_std: 0.0531
    is_best: false
  - model: GAT + NBA
    model_key: gat + nba
    model_plain: GAT + NBA
    value: 0.7059
    std: 0.0562
    paper_value: 0.7059
    paper_std: 0.0562
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 97
    true_value: 0.7059
    true_std: 0.0562
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7059
    sort_std: 0.0562
    is_best: false
  - model: ChebNet + LapPE
    model_key: chebnet + lappe
    model_plain: ChebNet + LapPE
    value: 0.6941
    std: 0.0905
    paper_value: 0.6941
    paper_std: 0.0905
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 101
    true_value: 0.6941
    true_std: 0.0905
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6941
    sort_std: 0.0905
    is_best: false
  - model: EGNN
    model_key: egnn
    model_plain: EGNN
    value: 0.6784
    std: 0.0407
    paper_value: 0.6784
    paper_std: 0.0407
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 105
    true_value: 0.6784
    true_std: 0.0407
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6784
    sort_std: 0.0407
    is_best: false
  - model: GCN+LapPE
    model_key: gcn+lappe
    model_plain: GCN+LapPE
    value: 0.6
    std: 0.06
    paper_value: 0.6
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 107
    true_value: 0.6647
    true_std: 0.0137
    value_gap_source_arxiv: '2404.03380'
    value_gap_source_title: On the Theoretical Expressive Power and the Design Space
      of Higher-Order Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06469999999999998
    value_note: ''
    paper_rank: 115
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.6647
    sort_std: 0.0137
    is_best: false
  - model: CensNet
    model_key: censnet
    model_plain: CensNet
    value: 0.6608
    std: 0.0463
    paper_value: 0.6608
    paper_std: 0.0463
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 108
    true_value: 0.6608
    true_std: 0.0463
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 108
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6608
    sort_std: 0.0463
    is_best: false
  - model: GAT (LapPE)
    model_key: gat (lappe)
    model_plain: GAT (LapPE)
    value: 0.6294
    std: 0.0448
    paper_value: 0.6294
    paper_std: 0.0448
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 112
    true_value: 0.6294
    true_std: 0.0448
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6294
    sort_std: 0.0448
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.5824
    std: 0.0641
    paper_value: 0.5824
    paper_std: 0.0641
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    global_rank: 119
    true_value: 0.5824
    true_std: 0.0641
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5824
    sort_std: 0.0641
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Heterophilic Graphs
  datasets:
  - *id004
  - *id005
  - *id006
- benchmark: LRGB
  datasets:
  - *id007
  - *id008
  - *id009
main_figure: /figures/2310.07430/main_figure.png
---

