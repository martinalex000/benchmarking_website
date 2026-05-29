---
title: Cooperative Sheaf Neural Networks
arxiv_id: '2507.00647'
source_url: ''
authors: []
published_date: Jul 2025
published_date_iso: 2025-07
abstract: Sheaf neural networks (SNNs) leverage cellular sheaves to induce flexible
  diffusion processes on graphs, generalizing the diffusion mechanism of classical
  graph neural networks. While SNNs have been shown to cope well with heterophilic
  tasks and alleviate oversmoothing, we show that there is further room for improving
  sheaf diffusion. More specifically, we argue that SNNs do not allow nodes to independently
  choose how they cooperate with their neighbors, i.e., whether they convey and/or
  gather information to/from their neighbors. To address this issue, we first introduce
  the notion of cellular sheaves over directed graphs and characterize their in- and
  out-degree Laplacians. We then leverage our construction to propose Cooperative
  Sheaf Neural Network (CSNN). Additionally, we formally characterize its receptive
  field and prove that it allows nodes to selectively attend (listen) to arbitrarily
  far nodes while ignoring all others in their path, which is key to alleviating oversquashing.
  Our results on synthetic data empirically substantiate our claims, showing that
  CSNN can handle long-range interactions while avoiding oversquashing. We also show
  that CSNN performs strongly in heterophilic node classification and long-range graph
  classification benchmarks. =-1
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- SNNs
mrr: 0.0278
adjusted_mrr: 0.0093
mrr_dataset_count: 1
benchmark_categories:
- Heterophilic Graphs
- LINKX Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id007
  dataset: Amazon-ratings
  rows:
  - model: here instead
    model_key: here instead
    model_plain: here instead
    value: 0.909
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_display: Jun 2015
    date_iso: 2015-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.909
    sort_std: null
    is_best: true
  - model: CT
    model_key: ct
    model_plain: CT
    value: 0.848
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_display: Jun 2015
    date_iso: 2015-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.848
    sort_std: null
    is_best: false
  - model: WNN
    model_key: wnn
    model_plain: WNN
    value: 0.843
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1506.04757'
    title: Image-based Recommendations on Styles and Substitutes
    date: Jun 2015
    date_display: Jun 2015
    date_iso: 2015-06
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.843
    sort_std: null
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.8326
    true_std: 0.0051
    value_gap_source_arxiv: '2410.10320'
    value_gap_source_title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3456
    value_note: ''
    paper_rank: 46
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.8326
    sort_std: 0.0051
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.8016
    true_std: 0.0232
    value_gap_source_arxiv: '2410.10320'
    value_gap_source_title: 'DiRW: Path-Aware Digraph Learning for Heterophily'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3107
    value_note: ''
    paper_rank: 45
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.8016
    sort_std: 0.0232
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.542
    std: 0.0034
    paper_value: 0.542
    paper_std: 0.0034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 21
    true_value: 0.542
    true_std: 0.0034
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.542
    sort_std: 0.0034
    is_best: false
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.5374
    std: 0.0051
    paper_value: 0.5374
    paper_std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 25
    true_value: 0.5374
    true_std: 0.0051
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5374
    sort_std: 0.0051
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 27
    true_value: 0.5363
    true_std: 0.0039
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5363
    sort_std: 0.0039
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 34
    true_value: 0.5218
    true_std: 0.008
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5218
    sort_std: 0.008
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.5207
    std: 0.01
    paper_value: 0.5207
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 35
    true_value: 0.5207
    true_std: 0.01
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5207
    sort_std: 0.01
    is_best: false
  - model: SNNs
    model_key: snns
    model_plain: SNNs
    value: 0.5207
    std: 0.01
    paper_value: 0.5207
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 36
    true_value: 0.5207
    true_std: 0.01
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5207
    sort_std: 0.01
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 40
    true_value: 0.5117
    true_std: 0.0066
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5117
    sort_std: 0.0066
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.4276
    std: 0.0054
    paper_value: 0.4276
    paper_std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 78
    true_value: 0.4276
    true_std: 0.0054
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4276
    sort_std: 0.0054
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Chameleon
  rows:
  - model: RUNG
    model_key: rung
    model_plain: RUNG
    value: 0.9773
    std: 0.0328
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9773
    sort_std: 0.0328
    is_best: true
  - model: DHGNN
    model_key: dhgnn
    model_plain: DHGNN
    value: 0.8011
    std: 0.0173
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8011
    sort_std: 0.0173
    is_best: false
  - model: NDDGNN
    model_key: nddgnn
    model_plain: NDDGNN
    value: 0.7979
    std: 0.0104
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7979
    sort_std: 0.0104
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.4089
    std: 0.0412
    paper_value: 0.4089
    paper_std: 0.0412
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.723
    true_std: null
    value_gap_source_arxiv: '2101.00797'
    value_gap_source_title: Beyond Low-frequency Information in Graph Convolutional
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3141
    value_note: ''
    paper_rank: 225
    rank_delta: 201
    rank_delta_abs: 201
    rank_delta_direction: worse
    sort_value: 0.723
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3921
    std: 0.0308
    paper_value: 0.3921
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 61
    true_value: 0.673
    true_std: 0.022
    value_gap_source_arxiv: '2205.13700'
    value_gap_source_title: 'ES-GNN: Generalizing Graph Neural Networks Beyond Homophily
      with Edge Splitting'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.28090000000000004
    value_note: ''
    paper_rank: 234
    rank_delta: 173
    rank_delta_abs: 173
    rank_delta_direction: worse
    sort_value: 0.673
    sort_std: 0.022
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.4031
    std: 0.0301
    paper_value: 0.4031
    paper_std: 0.0301
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 167
    true_value: 0.5033
    true_std: 0.0257
    value_gap_source_arxiv: '2302.11640'
    value_gap_source_title: 'A critical look at the evaluation of GNNs under heterophily:
      Are we really making progress?'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10019999999999996
    value_note: ''
    paper_rank: 227
    rank_delta: 60
    rank_delta_abs: 60
    rank_delta_direction: worse
    sort_value: 0.5033
    sort_std: 0.0257
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.3777
    std: 0.0414
    paper_value: 0.3777
    paper_std: 0.0414
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 168
    true_value: 0.5018
    true_std: 0.0178
    value_gap_source_arxiv: '2302.11640'
    value_gap_source_title: 'A critical look at the evaluation of GNNs under heterophily:
      Are we really making progress?'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12410000000000004
    value_note: ''
    paper_rank: 241
    rank_delta: 73
    rank_delta_abs: 73
    rank_delta_direction: worse
    sort_value: 0.5018
    sort_std: 0.0178
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.3887
    std: 0.0366
    paper_value: 0.3887
    paper_std: 0.0366
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 200
    true_value: 0.4493
    true_std: 0.014
    value_gap_source_arxiv: '2302.11640'
    value_gap_source_title: 'A critical look at the evaluation of GNNs under heterophily:
      Are we really making progress?'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06059999999999999
    value_note: ''
    paper_rank: 236
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.4493
    sort_std: 0.014
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.4309
    std: 0.0317
    paper_value: 0.4309
    paper_std: 0.0317
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 208
    true_value: 0.4309
    true_std: 0.0317
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4309
    sort_std: 0.0317
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.4114
    std: 0.054
    paper_value: 0.4114
    paper_std: 0.054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 223
    true_value: 0.4114
    true_std: 0.054
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 223
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4114
    sort_std: 0.054
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.3793
    std: 0.0224
    paper_value: 0.3793
    paper_std: 0.0224
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 240
    true_value: 0.3793
    true_std: 0.0224
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 240
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3793
    sort_std: 0.0224
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Cornell
  rows:
  - model: FMP ode
    model_key: fmp ode
    model_plain: FMP ode
    value: 0.938
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.938
    sort_std: 0.015
    is_best: true
  - model: DMD++
    model_key: dmd++
    model_plain: DMD++
    value: 0.914
    std: 0.017
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
    global_rank: 2
    sort_value: 0.914
    sort_std: 0.017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8189
    std: 0.064
    paper_value: 0.8189
    paper_std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.913
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09410000000000007
    value_note: ''
    paper_rank: 41
    rank_delta: 38
    rank_delta_abs: 38
    rank_delta_direction: worse
    sort_value: 0.913
    sort_std: 0.007
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.898
    std: 0.006
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
    global_rank: 4
    sort_value: 0.898
    sort_std: 0.006
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.873
    std: 0.0453
    paper_value: 0.873
    paper_std: 0.0453
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.873
    true_std: 0.0453
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.873
    sort_std: 0.0453
    is_best: false
  - model: Diag-NSD
    model_key: diag-nsd
    model_plain: Diag-NSD
    value: 0.8649
    std: 0.0735
    paper_value: 0.8649
    paper_std: 0.0735
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.8649
    true_std: 0.0735
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8649
    sort_std: 0.0735
    is_best: true
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.8351
    std: 0.0426
    paper_value: 0.8351
    paper_std: 0.0426
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.8595
    true_std: 0.051
    value_gap_source_arxiv: '2209.15454'
    value_gap_source_title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel
      Geometric Polynomials'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02440000000000009
    value_note: global 0.8595 within std
    paper_rank: 29
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.8595
    sort_std: 0.051
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8568
    std: 0.0663
    paper_value: 0.8568
    paper_std: 0.0663
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 15
    true_value: 0.8568
    true_std: 0.0663
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8568
    sort_std: 0.0663
    is_best: true
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8568
    std: 0.0651
    paper_value: 0.8568
    paper_std: 0.0651
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.8568
    true_std: 0.0651
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8568
    sort_std: 0.0651
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8514
    std: 0.0607
    paper_value: 0.8514
    paper_std: 0.0607
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 18
    true_value: 0.8514
    true_std: 0.0607
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8514
    sort_std: 0.0607
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.827
    std: 0.0528
    paper_value: 0.827
    paper_std: 0.0528
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 21
    true_value: 0.851
    true_std: 0.064
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02400000000000002
    value_note: global 0.8510 within std
    paper_rank: 34
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.064
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8027
    std: 0.0811
    paper_value: 0.8027
    paper_std: 0.0811
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 22
    true_value: 0.85
    true_std: 0.052
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.04730000000000001
    value_note: global 0.8500 within std
    paper_rank: 51
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.85
    sort_std: 0.052
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8486
    std: 0.0471
    paper_value: 0.8486
    paper_std: 0.0471
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.8486
    true_std: 0.0471
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8486
    sort_std: 0.0471
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6189
    std: 0.0505
    paper_value: 0.6189
    paper_std: 0.0505
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 41
    true_value: 0.819
    true_std: 0.054
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20009999999999994
    value_note: ''
    paper_rank: 149
    rank_delta: 108
    rank_delta_abs: 108
    rank_delta_direction: worse
    sort_value: 0.819
    sort_std: 0.054
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.8162
    std: 0.0432
    paper_value: 0.8162
    paper_std: 0.0432
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 43
    true_value: 0.8162
    true_std: 0.0432
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8162
    sort_std: 0.0432
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7919
    std: 0.0979
    paper_value: 0.7919
    paper_std: 0.0979
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 46
    true_value: 0.8135
    true_std: 0.0505
    value_gap_source_arxiv: '2302.12357'
    value_gap_source_title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.021599999999999953
    value_note: global 0.8135 within std
    paper_rank: 58
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.8135
    sort_std: 0.0505
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7595
    std: 0.0501
    paper_value: 0.7595
    paper_std: 0.0501
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 52
    true_value: 0.8008
    true_std: 0.0296
    value_gap_source_arxiv: '2209.08264'
    value_gap_source_title: 'Make Heterophily Graphs Better Fit GNN: A Graph Rewiring
      Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0413
    value_note: global 0.8008 within std
    paper_rank: 76
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.8008
    sort_std: 0.0296
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6054
    std: 0.053
    paper_value: 0.6054
    paper_std: 0.053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 57
    true_value: 0.792
    true_std: 0.063
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1866
    value_note: ''
    paper_rank: 155
    rank_delta: 98
    rank_delta_abs: 98
    rank_delta_direction: worse
    sort_value: 0.792
    sort_std: 0.063
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.7786
    std: 0.0379
    paper_value: 0.7786
    paper_std: 0.0379
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 59
    true_value: 0.7919
    true_std: 0.0612
    value_gap_source_arxiv: '2205.15127'
    value_gap_source_title: 'Universal Deep GNNs: Rethinking Residual Connection in
      GNNs from a Path Decomposition Perspective for Preventing the Over-smoothing'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.01330000000000009
    value_note: global 0.7919 within std
    paper_rank: 64
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.7919
    sort_std: 0.0612
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7351
    std: 0.0634
    paper_value: 0.7351
    paper_std: 0.0634
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 60
    true_value: 0.7868
    true_std: 0.0093
    value_gap_source_arxiv: '2506.08871'
    value_gap_source_title: Adapting to Heterophilic Graph Data with Structure-Guided
      Neighbor Discovery
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.05170000000000008
    value_note: global 0.7868 within std
    paper_rank: 89
    rank_delta: 29
    rank_delta_abs: 29
    rank_delta_direction: worse
    sort_value: 0.7868
    sort_std: 0.0093
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.727
    std: 0.0547
    paper_value: 0.727
    paper_std: 0.0547
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 95
    true_value: 0.727
    true_std: 0.0547
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.0547
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6054
    std: 0.0367
    paper_value: 0.6054
    paper_std: 0.0367
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 155
    true_value: 0.6081
    true_std: null
    value_gap_source_arxiv: '2105.07634'
    value_gap_source_title: Improving Graph Neural Networks with Simple Architecture
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0026999999999999247
    value_note: global 0.6081 within std
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6081
    sort_std: null
    is_best: false
  - model: PairNorm
    model_key: pairnorm
    model_plain: PairNorm
    value: 0.5892
    std: 0.0315
    paper_value: 0.5892
    paper_std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 160
    true_value: 0.5892
    true_std: 0.0315
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5892
    sort_std: 0.0315
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: Film
  rows:
  - model: DoG (ACM-GCN)
    model_key: dog (acm-gcn)
    model_plain: DoG (ACM-GCN)
    value: 0.432
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.432
    sort_std: 0.012
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.3628
    std: 0.0109
    paper_value: 0.3628
    paper_std: 0.0109
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.416
    true_std: 0.011
    value_gap_source_arxiv: '2503.12563'
    value_gap_source_title: 'Diffusion on Graph: Augmentation of Graph Structure for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05319999999999997
    value_note: ''
    paper_rank: 13
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.416
    sort_std: 0.011
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.3803
    std: 0.011200000000000002
    paper_value: 0.3803
    paper_std: 0.011200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.3803
    true_std: 0.011200000000000002
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3803
    sort_std: 0.011200000000000002
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.37810000000000005
    std: 0.0115
    paper_value: 0.37810000000000005
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.37810000000000005
    true_std: 0.0115
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37810000000000005
    sort_std: 0.0115
    is_best: false
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.37799999999999995
    std: 0.012199999999999999
    paper_value: 0.37799999999999995
    paper_std: 0.012199999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.37799999999999995
    true_std: 0.012199999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37799999999999995
    sort_std: 0.012199999999999999
    is_best: false
  - model: Diag-NSD
    model_key: diag-nsd
    model_plain: Diag-NSD
    value: 0.3779
    std: 0.0101
    paper_value: 0.3779
    paper_std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.3779
    true_std: 0.0101
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3779
    sort_std: 0.0101
    is_best: false
  - model: GRED
    model_key: gred
    model_plain: GRED
    value: 0.3759
    std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    sort_value: 0.3759
    sort_std: 0.0106
    is_best: false
  - model: PDE-Log
    model_key: pde-log
    model_plain: PDE-Log
    value: 0.3755
    std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.15326'
    title: Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective
      of Operator Semigroup Theory
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/LOGO-CUHKSZ/SGOS
    uses_external_data: false
    is_global_top: true
    global_rank: 8
    sort_value: 0.3755
    sort_std: 0.008
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.3754
    std: 0.015600000000000001
    paper_value: 0.3754
    paper_std: 0.015600000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.3754
    true_std: 0.015600000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3754
    sort_std: 0.015600000000000001
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.37439999999999996
    std: 0.013000000000000001
    paper_value: 0.37439999999999996
    paper_std: 0.013000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.37439999999999996
    true_std: 0.013000000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37439999999999996
    sort_std: 0.013000000000000001
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.3735
    std: 0.013000000000000001
    paper_value: 0.3735
    paper_std: 0.013000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.3735
    true_std: 0.013000000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3735
    sort_std: 0.013000000000000001
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.3653
    std: 0.006999999999999999
    paper_value: 0.3653
    paper_std: 0.006999999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.3653
    true_std: 0.006999999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3653
    sort_std: 0.006999999999999999
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.3626
    std: 0.0374
    paper_value: 0.3626
    paper_std: 0.0374
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.3626
    true_std: 0.0374
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3626
    sort_std: 0.0374
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.35700000000000004
    std: 0.01
    paper_value: 0.35700000000000004
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.35700000000000004
    true_std: 0.01
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35700000000000004
    sort_std: 0.01
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.35619999999999996
    std: 0.0087
    paper_value: 0.35619999999999996
    paper_std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 18
    true_value: 0.35619999999999996
    true_std: 0.0087
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35619999999999996
    sort_std: 0.0087
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.34869999999999995
    std: 0.0125
    paper_value: 0.34869999999999995
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 20
    true_value: 0.34869999999999995
    true_std: 0.0125
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34869999999999995
    sort_std: 0.0125
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.34630000000000005
    std: 0.012199999999999999
    paper_value: 0.34630000000000005
    paper_std: 0.012199999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 21
    true_value: 0.34630000000000005
    true_std: 0.012199999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.34630000000000005
    sort_std: 0.012199999999999999
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.3423
    std: 0.009899999999999999
    paper_value: 0.3423
    paper_std: 0.009899999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 22
    true_value: 0.3423
    true_std: 0.009899999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3423
    sort_std: 0.009899999999999999
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.3222
    std: 0.023399999999999997
    paper_value: 0.3222
    paper_std: 0.023399999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 23
    true_value: 0.3222
    true_std: 0.023399999999999997
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3222
    sort_std: 0.023399999999999997
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.3159
    std: 0.0115
    paper_value: 0.3159
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.3159
    true_std: 0.0115
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3159
    sort_std: 0.0115
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.27440000000000003
    std: 0.0089
    paper_value: 0.27440000000000003
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 25
    true_value: 0.27440000000000003
    true_std: 0.0089
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.27440000000000003
    sort_std: 0.0089
    is_best: false
  - model: PairNorm
    model_key: pairnorm
    model_plain: PairNorm
    value: 0.27399999999999997
    std: 0.0124
    paper_value: 0.27399999999999997
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 26
    true_value: 0.274
    true_std: 0.0124
    value_gap_source_arxiv: '2402.15326'
    value_gap_source_title: Understanding Oversmoothing in Diffusion-Based GNNs From
      the Perspective of Operator Semigroup Theory
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.274
    sort_std: 0.0124
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.2732
    std: 0.011000000000000001
    paper_value: 0.2732
    paper_std: 0.011000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 27
    true_value: 0.2732
    true_std: 0.011000000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2732
    sort_std: 0.011000000000000001
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9907
    std: 0.0025
    paper_value: 0.9907
    paper_std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.9907
    true_std: 0.0025
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9907
    sort_std: 0.0025
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9899
    std: 0.0016
    paper_value: 0.9899
    paper_std: 0.0016
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.9899
    true_std: 0.0016
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9899
    sort_std: 0.0016
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
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
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.9832
    std: 0.0059
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
    global_rank: 4
    sort_value: 0.9832
    sort_std: 0.0059
    is_best: true
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.9735
    std: 0.0063
    paper_value: 0.9735
    paper_std: 0.0063
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.9735
    true_std: 0.0063
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9735
    sort_std: 0.0063
    is_best: false
  - model: CO-GNN(μ, μ)
    model_key: co-gnn(μ, μ)
    model_plain: CO-GNN(μ, μ)
    value: 0.9731
    std: 0.0041
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
    global_rank: 6
    sort_value: 0.9731
    sort_std: 0.0041
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.9351
    true_std: 0.0057
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9351
    sort_std: 0.0057
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.9229
    true_std: 0.0047
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9229
    sort_std: 0.0047
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.9215
    std: 0.0084
    paper_value: 0.9215
    paper_std: 0.0084
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.9215
    true_std: 0.0084
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9215
    sort_std: 0.0084
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.9201
    true_std: 0.0068
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9201
    sort_std: 0.0068
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.9185
    true_std: 0.0076
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9185
    sort_std: 0.0076
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 21
    true_value: 0.8975
    true_std: 0.0052
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8975
    sort_std: 0.0052
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id012
  dataset: Penn94
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.86
    std: 0.0039
    paper_value: 0.86
    paper_std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.86
    true_std: 0.0039
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.0039
    is_best: true
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.8557
    std: 0.0035
    paper_value: 0.8557
    paper_std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ''
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.8557
    true_std: 0.0035
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8557
    sort_std: 0.0035
    is_best: true
  - model: AdaptKry
    model_key: adaptkry
    model_plain: AdaptKry
    value: 0.8497
    std: 0.0036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8497
    sort_std: 0.0036
    is_best: false
  - model: ChebNet
    model_key: chebnet
    model_plain: ChebNet
    value: 0.8486
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.8486
    sort_std: 0.0033
    is_best: false
  - model: OptBasisGNN
    model_key: optbasisgnn
    model_plain: OptBasisGNN
    value: 0.8485
    std: 0.0039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2403.07954'
    title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace
      Approach'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: https://github.com/kkhuang81/AdaptKry
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.8485
    sort_std: 0.0039
    is_best: false
  - model: LINKX
    model_key: linkx
    model_plain: LINKX
    value: 0.8471
    std: 0.0052
    paper_value: 0.8471
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Li 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.8471
    true_std: 0.0052
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8471
    sort_std: 0.0052
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.8347
    std: 0.0071
    paper_value: 0.8347
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.8409
    true_std: 0.002
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006199999999999983
    value_note: global 0.8409 within std
    paper_rank: 11
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.8409
    sort_std: 0.002
    is_best: false
  - model: GPR-GNN
    model_key: gpr-gnn
    model_plain: GPR-GNN
    value: 0.8138
    std: 0.0016
    paper_value: 0.8138
    paper_std: 0.0016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.8354
    true_std: 0.0032
    value_gap_source_arxiv: '2403.07954'
    value_gap_source_title: 'Optimizing Polynomial Graph Filters: A Novel Adaptive
      Krylov Subspace Approach'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.021600000000000064
    value_note: ''
    paper_rank: 20
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.8354
    sort_std: 0.0032
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8247
    std: 0.0027
    paper_value: 0.8247
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.8323
    true_std: 0.002
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.007600000000000051
    value_note: ''
    paper_rank: 16
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.8323
    sort_std: 0.002
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8292
    std: 0.0059
    paper_value: 0.8292
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 15
    true_value: 0.8292
    true_std: 0.0059
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8292
    sort_std: 0.0059
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8252
    std: 0.0096
    paper_value: 0.8252
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.8252
    true_std: 0.0096
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8252
    sort_std: 0.0096
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8153
    std: 0.0055
    paper_value: 0.8153
    paper_std: 0.0055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 19
    true_value: 0.8153
    true_std: 0.0055
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8153
    sort_std: 0.0055
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8131
    std: 0.006
    paper_value: 0.8131
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 21
    true_value: 0.8131
    true_std: 0.006
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8131
    sort_std: 0.006
    is_best: false
  - model: WRGAT
    model_key: wrgat
    model_plain: WRGAT
    value: 0.7432
    std: 0.0053
    paper_value: 0.7432
    paper_std: 0.0053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 23
    true_value: 0.7432
    true_std: 0.0053
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7432
    sort_std: 0.0053
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.7361
    std: 0.004
    paper_value: 0.7361
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.7418
    true_std: 0.003
    value_gap_source_arxiv: '2310.10064'
    value_gap_source_title: arXiv:2310.10064
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.005700000000000038
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7418
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: Questions
  rows:
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.8039
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
    global_rank: 1
    sort_value: 0.8039
    sort_std: 0.0104
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.8032
    std: 0.0107
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
    sort_value: 0.8032
    sort_std: 0.0107
    is_best: true
  - model: CO-GNN(Σ, Σ)
    model_key: co-gnn(σ, σ)
    model_plain: CO-GNN(Σ, Σ)
    value: 0.8002
    std: 0.0086
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
    sort_value: 0.8002
    sort_std: 0.0086
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.7931
    std: 0.0122
    paper_value: 0.7931
    paper_std: 0.0122
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.7931
    true_std: 0.0122
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7931
    sort_std: 0.0122
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.7875
    std: 0.0109
    paper_value: 0.7875
    paper_std: 0.0109
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.7875
    true_std: 0.0109
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7875
    sort_std: 0.0109
    is_best: true
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.7805
    true_std: 0.0093
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.7795
    true_std: 0.0068
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7795
    sort_std: 0.0068
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.7743
    true_std: 0.012
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7743
    sort_std: 0.012
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 15
    true_value: 0.7644
    true_std: 0.0062
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7644
    sort_std: 0.0062
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.7609
    true_std: 0.0127
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7609
    sort_std: 0.0127
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.7597
    std: 0.0089
    paper_value: 0.7597
    paper_std: 0.0089
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.7597
    true_std: 0.0089
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7597
    sort_std: 0.0089
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.6969
    std: 0.0146
    paper_value: 0.6969
    paper_std: 0.0146
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Platonov et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 32
    true_value: 0.6969
    true_std: 0.0146
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6969
    sort_std: 0.0146
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id006
  dataset: Roman-empire
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9263
    std: 0.005
    paper_value: 0.9263
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.9263
    true_std: 0.005
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9263
    sort_std: 0.005
    is_best: true
  - model: Polynormer
    model_key: polynormer
    model_plain: Polynormer
    value: 0.9255
    std: 0.003
    metric: Accuracy
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
    sort_value: 0.9255
    sort_std: 0.003
    is_best: true
  - model: Stable-ChebNet
    model_key: stable-chebnet
    model_plain: Stable-ChebNet
    value: 0.9203
    std: 0.0085
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
    global_rank: 3
    sort_value: 0.9203
    sort_std: 0.0085
    is_best: true
  - model: Tango_GatedGCN
    model_key: tango_gatedgcn
    model_plain: Tango_GatedGCN
    value: 0.9189
    std: 0.003
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
    global_rank: 4
    sort_value: 0.9189
    sort_std: 0.003
    is_best: true
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Squirrel
  rows:
  - model: RUNG
    model_key: rung
    model_plain: RUNG
    value: 0.9787
    std: 0.0177
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.05534'
    title: 'Adversarial Graph Neural Network Benchmarks: Towards Practical and Fair
      Evaluation'
    date: May 2026
    date_display: May 2026
    date_iso: 2026-05
    codebase_url: https://github.com/FDataLab/GAB
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9787
    sort_std: 0.0177
    is_best: true
  - model: DHGNN
    model_key: dhgnn
    model_plain: DHGNN
    value: 0.7684
    std: 0.0161
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.7684
    sort_std: 0.0161
    is_best: false
  - model: NDDGNN
    model_key: nddgnn
    model_plain: NDDGNN
    value: 0.7538
    std: 0.0195
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.22362'
    title: Directed Homophily-Aware Graph Neural Network
    date: May 2025
    date_display: May 2025
    date_iso: 2025-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7538
    sort_std: 0.0195
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3947
    std: 0.0147
    paper_value: 0.3947
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 32
    true_value: 0.619
    true_std: null
    value_gap_source_arxiv: '2101.00797'
    value_gap_source_title: Beyond Low-frequency Information in Graph Convolutional
      Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2243
    value_note: ''
    paper_rank: 126
    rank_delta: 94
    rank_delta_abs: 94
    rank_delta_direction: worse
    sort_value: 0.619
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.3562
    std: 0.0206
    paper_value: 0.3562
    paper_std: 0.0206
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 55
    true_value: 0.563
    true_std: 0.022
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.20679999999999993
    value_note: ''
    paper_rank: 167
    rank_delta: 112
    rank_delta_abs: 112
    rank_delta_direction: worse
    sort_value: 0.563
    sort_std: 0.022
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.4118
    std: 0.0223
    paper_value: 0.4118
    paper_std: 0.0223
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 115
    true_value: 0.4118
    true_std: 0.0223
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4118
    sort_std: 0.0223
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.3939
    std: 0.0276
    paper_value: 0.3939
    paper_std: 0.0276
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 127
    true_value: 0.3939
    true_std: 0.0276
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3939
    sort_std: 0.0276
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.3666
    std: 0.0163
    paper_value: 0.3666
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 155
    true_value: 0.3666
    true_std: 0.0163
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3666
    sort_std: 0.0163
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.363
    std: 0.0198
    paper_value: 0.363
    paper_std: 0.0198
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 159
    true_value: 0.363
    true_std: 0.0198
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 159
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.363
    sort_std: 0.0198
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.3609
    std: 0.0199
    paper_value: 0.3609
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 160
    true_value: 0.3609
    true_std: 0.0199
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3609
    sort_std: 0.0199
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.3579
    std: 0.0334
    paper_value: 0.3579
    paper_std: 0.0334
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 165
    true_value: 0.3579
    true_std: 0.0334
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3579
    sort_std: 0.0334
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: Texas
  rows:
  - model: DoG (ACM-GCN)
    model_key: dog (acm-gcn)
    model_plain: DoG (ACM-GCN)
    value: 0.966
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2503.12563'
    title: 'Diffusion on Graph: Augmentation of Graph Structure for Node Classification'
    date: Mar 2025
    date_display: Mar 2025
    date_iso: 2025-03
    codebase_url: https://github.com/Statistical-Deep-Learning/DoG
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.966
    sort_std: 0.021
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8784
    std: 0.044
    paper_value: 0.8784
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.951
    true_std: 0.032
    value_gap_source_arxiv: '2503.12563'
    value_gap_source_title: 'Diffusion on Graph: Augmentation of Graph Structure for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0726
    value_note: ''
    paper_rank: 25
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.951
    sort_std: 0.032
    is_best: true
  - model: AD-MixHop
    model_key: ad-mixhop
    model_plain: AD-MixHop
    value: 0.9443
    std: 0.0256
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9443
    sort_std: 0.0256
    is_best: true
  - model: AD-GraphSAGE
    model_key: ad-graphsage
    model_plain: AD-GraphSAGE
    value: 0.9295
    std: 0.0284
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.06608'
    title: 'Beyond Fixed Depth: Adaptive Graph Neural Networks for Node Classification
      Under Varying Homophily'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.9295
    sort_std: 0.0284
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7838
    std: 0.0436
    paper_value: 0.7838
    paper_std: 0.0436
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.9292
    true_std: 0.0061
    value_gap_source_arxiv: '2202.04139'
    value_gap_source_title: Simplified Graph Convolution with Heterophily
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14539999999999997
    value_note: ''
    paper_rank: 109
    rank_delta: 103
    rank_delta_abs: 103
    rank_delta_direction: worse
    sort_value: 0.9292
    sort_std: 0.0061
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8081
    std: 0.0475
    paper_value: 0.8081
    paper_std: 0.0475
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.923
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1149
    value_note: ''
    paper_rank: 93
    rank_delta: 82
    rank_delta_abs: 82
    rank_delta_direction: worse
    sort_value: 0.923
    sort_std: 0.007
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8757
    std: 0.0486
    paper_value: 0.8757
    paper_std: 0.0486
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 28
    true_value: 0.8757
    true_std: 0.0486
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8757
    sort_std: 0.0486
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.873
    std: 0.0593
    paper_value: 0.873
    paper_std: 0.0593
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 29
    true_value: 0.873
    true_std: 0.0593
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.873
    sort_std: 0.0593
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8595
    std: 0.0551
    paper_value: 0.8595
    paper_std: 0.0551
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 40
    true_value: 0.8595
    true_std: 0.0551
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 40
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8595
    sort_std: 0.0551
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8486
    std: 0.0723
    paper_value: 0.8486
    paper_std: 0.0723
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 41
    true_value: 0.859
    true_std: 0.046
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010399999999999965
    value_note: global 0.8590 within std
    paper_rank: 48
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.859
    sort_std: 0.046
    is_best: false
  - model: Diag-NSD
    model_key: diag-nsd
    model_plain: Diag-NSD
    value: 0.8567
    std: 0.0695
    paper_value: 0.8567
    paper_std: 0.0695
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 44
    true_value: 0.8567
    true_std: 0.0695
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 44
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8567
    sort_std: 0.0695
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8486
    std: 0.0455
    paper_value: 0.8486
    paper_std: 0.0455
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 49
    true_value: 0.8486
    true_std: 0.0455
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8486
    sort_std: 0.0455
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8243
    std: 0.0689
    paper_value: 0.8243
    paper_std: 0.0689
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 57
    true_value: 0.8455
    true_std: 0.048
    value_gap_source_arxiv: '2408.14134'
    value_gap_source_title: Exploring the Potential of Large Language Models for Heterophilic
      Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.021199999999999997
    value_note: global 0.8455 within std
    paper_rank: 75
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.8455
    sort_std: 0.048
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.8432
    std: 0.0415
    paper_value: 0.8432
    paper_std: 0.0415
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 58
    true_value: 0.8432
    true_std: 0.0415
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8432
    sort_std: 0.0415
    is_best: false
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8297
    std: 0.0513
    paper_value: 0.8297
    paper_std: 0.0513
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 75
    true_value: 0.8297
    true_std: 0.0513
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8297
    sort_std: 0.0513
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8243
    std: 0.0614
    paper_value: 0.8243
    paper_std: 0.0614
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 76
    true_value: 0.8243
    true_std: 0.0614
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.0614
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7784
    std: 0.0773
    paper_value: 0.7784
    paper_std: 0.0773
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 95
    true_value: 0.8079
    true_std: 0.009
    value_gap_source_arxiv: '2506.08871'
    value_gap_source_title: Adapting to Heterophilic Graph Data with Structure-Guided
      Neighbor Discovery
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.02949999999999997
    value_note: global 0.8079 within std
    paper_rank: 114
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.8079
    sort_std: 0.009
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.5216
    std: 0.0663
    paper_value: 0.5216
    paper_std: 0.0663
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 99
    true_value: 0.798
    true_std: 0.043
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2764000000000001
    value_note: ''
    paper_rank: 250
    rank_delta: 151
    rank_delta_abs: 151
    rank_delta_direction: worse
    sort_value: 0.798
    sort_std: 0.043
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5514
    std: 0.0516
    paper_value: 0.5514
    paper_std: 0.0516
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 108
    true_value: 0.784
    true_std: 0.054
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23260000000000003
    value_note: ''
    paper_rank: 243
    rank_delta: 135
    rank_delta_abs: 135
    rank_delta_direction: worse
    sort_value: 0.784
    sort_std: 0.054
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.7757
    std: 0.0383
    paper_value: 0.7757
    paper_std: 0.0383
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 115
    true_value: 0.7784
    true_std: 0.0564
    value_gap_source_arxiv: '2105.07634'
    value_gap_source_title: Improving Graph Neural Networks with Simple Architecture
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027000000000000357
    value_note: global 0.7784 within std
    paper_rank: 116
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7784
    sort_std: 0.0564
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.7757
    std: 0.0541
    paper_value: 0.7757
    paper_std: 0.0541
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 117
    true_value: 0.7757
    true_std: 0.0541
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7757
    sort_std: 0.0541
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6676
    std: 0.0272
    paper_value: 0.6676
    paper_std: 0.0272
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 168
    true_value: 0.676
    true_std: null
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008400000000000074
    value_note: global 0.6760 within std
    paper_rank: 172
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.676
    sort_std: null
    is_best: false
  - model: PairNorm
    model_key: pairnorm
    model_plain: PairNorm
    value: 0.6027
    std: 0.0434
    paper_value: 0.6027
    paper_std: 0.0434
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 209
    true_value: 0.603
    true_std: 0.043
    value_gap_source_arxiv: '2311.05767'
    value_gap_source_title: Dirichlet Energy Enhancement of Graph Neural Networks
      by Framelet Augmentation
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00029999999999996696
    value_note: global 0.6030 within std
    paper_rank: 210
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.603
    sort_std: 0.043
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Tolokers
  rows:
  - model: GRAMA_GCNGCN
    model_key: grama_gcngcn
    model_plain: GRAMA_GCNGCN
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
    codebase_url: https://github.com/ahariri13/Stable-ChebNet
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    sort_value: 0.8591
    sort_std: 0.0074
    is_best: true
  - model: Tango_GPS
    model_key: tango_gps
    model_plain: Tango_GPS
    value: 0.8566
    std: 0.0101
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
    sort_value: 0.8566
    sort_std: 0.0101
    is_best: true
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.8545
    std: 0.0053
    paper_value: 0.8545
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.8545
    true_std: 0.0053
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8545
    sort_std: 0.0053
    is_best: true
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.8484
    std: 0.0096
    paper_value: 0.8484
    paper_std: 0.0096
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.8484
    true_std: 0.0096
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8484
    sort_std: 0.0096
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.8478
    std: 0.008
    paper_value: 0.8478
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.8478
    true_std: 0.008
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8478
    sort_std: 0.008
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.8364
    std: 0.0067
    paper_value: 0.8364
    paper_std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 19
    true_value: 0.838
    true_std: 0.0034
    value_gap_source_arxiv: '2602.17893'
    value_gap_source_title: 'COMBA: Cross Batch Aggregation for Learning Large Graphs
      with Context Gating State Space Models'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0015999999999999348
    value_note: global 0.8380 within std
    paper_rank: 24
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.837
    std: 0.0047
    paper_value: 0.837
    paper_std: 0.0047
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 23
    true_value: 0.837
    true_std: 0.0047
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.837
    sort_std: 0.0047
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8323
    std: 0.0064
    paper_value: 0.8323
    paper_std: 0.0064
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 32
    true_value: 0.8323
    true_std: 0.0064
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8323
    sort_std: 0.0064
    is_best: false
  - model: GT-sep
    model_key: gt-sep
    model_plain: GT-sep
    value: 0.8252
    std: 0.0092
    paper_value: 0.8252
    paper_std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 36
    true_value: 0.8252
    true_std: 0.0092
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 37
    true_value: 0.8243
    true_std: 0.0044
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.0044
    is_best: false
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.7883
    std: 0.0076
    paper_value: 0.7883
    paper_std: 0.0076
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 45
    true_value: 0.7883
    true_std: 0.0076
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7883
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id005
  dataset: Wisconsin
  rows:
  - model: FMP ode
    model_key: fmp ode
    model_plain: FMP ode
    value: 0.937
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2302.14806'
    title: Framelet Message Passing
    date: Feb 2023
    date_display: Feb 2023
    date_iso: 2023-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.937
    sort_std: 0.012
    is_best: true
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
    global_rank: 2
    sort_value: 0.919
    sort_std: 0.026
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.8529
    std: 0.0331
    paper_value: 0.8529
    paper_std: 0.0331
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.918
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06510000000000005
    value_note: ''
    paper_rank: 50
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.918
    sort_std: 0.031
    is_best: true
  - model: FMLP-O
    model_key: fmlp-o
    model_plain: FMLP-O
    value: 0.906
    std: 0.0012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.06631'
    title: Frameless Graph Knowledge Distillation
    date: Jul 2023
    date_display: Jul 2023
    date_iso: 2023-07
    codebase_url: https://github.com/dshi3553usyd/Frameless_Graph_Distillation.git
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.906
    sort_std: 0.0012
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.0283
    paper_value: 0.9
    paper_std: 0.0283
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.9
    true_std: 0.0283
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: 0.0283
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8294
    std: 0.0421
    paper_value: 0.8294
    paper_std: 0.0421
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.899
    true_std: 0.03
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0696
    value_note: ''
    paper_rank: 73
    rank_delta: 65
    rank_delta_abs: 65
    rank_delta_direction: worse
    sort_value: 0.899
    sort_std: 0.03
    is_best: true
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8941
    std: 0.0474
    paper_value: 0.8941
    paper_std: 0.0474
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.8941
    true_std: 0.0474
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8941
    sort_std: 0.0474
    is_best: true
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8921
    std: 0.0384
    paper_value: 0.8921
    paper_std: 0.0384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.8921
    true_std: 0.0384
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8921
    sort_std: 0.0384
    is_best: true
  - model: Diag-NSD
    model_key: diag-nsd
    model_plain: Diag-NSD
    value: 0.8863
    std: 0.0275
    paper_value: 0.8863
    paper_std: 0.0275
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.8863
    true_std: 0.0275
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8863
    sort_std: 0.0275
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8843
    std: 0.0322
    paper_value: 0.8843
    paper_std: 0.0322
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.8843
    true_std: 0.0322
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8843
    sort_std: 0.0322
    is_best: false
  - model: GloGNN
    model_key: glognn
    model_plain: GloGNN
    value: 0.8706
    std: 0.0353
    paper_value: 0.8706
    paper_std: 0.0353
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 23
    true_value: 0.8804
    true_std: 0.032
    value_gap_source_arxiv: '2209.15454'
    value_gap_source_title: 'GPNet: Simplifying Graph Neural Networks via Multi-channel
      Geometric Polynomials'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00979999999999992
    value_note: global 0.8804 within std
    paper_rank: 33
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.8804
    sort_std: 0.032
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8765
    std: 0.0498
    paper_value: 0.8765
    paper_std: 0.0498
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 25
    true_value: 0.879
    true_std: 0.042
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0025000000000000577
    value_note: global 0.8790 within std
    paper_rank: 27
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.879
    sort_std: 0.042
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8765
    std: 0.0351
    paper_value: 0.8765
    paper_std: 0.0351
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 28
    true_value: 0.8765
    true_std: 0.0351
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8765
    sort_std: 0.0351
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8686
    std: 0.0329
    paper_value: 0.8686
    paper_std: 0.0329
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 35
    true_value: 0.8686
    true_std: 0.0329
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8686
    sort_std: 0.0329
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.4941
    std: 0.0409
    paper_value: 0.4941
    paper_std: 0.0409
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 61
    true_value: 0.843
    true_std: 0.037
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3489
    value_note: ''
    paper_rank: 228
    rank_delta: 167
    rank_delta_abs: 167
    rank_delta_direction: worse
    sort_value: 0.843
    sort_std: 0.037
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.8373
    std: 0.0403
    paper_value: 0.8373
    paper_std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 67
    true_value: 0.8373
    true_std: 0.0403
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 67
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8373
    sort_std: 0.0403
    is_best: false
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8294
    std: 0.0795
    paper_value: 0.8294
    paper_std: 0.0795
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 69
    true_value: 0.8333
    true_std: 0.0201
    value_gap_source_arxiv: '2302.12357'
    value_gap_source_title: 'Auto-HeG: Automated Graph Neural Network on Heterophilic
      Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0039000000000000146
    value_note: global 0.8333 within std
    paper_rank: 73
    rank_delta: 4
    rank_delta_abs: 4
    rank_delta_direction: worse
    sort_value: 0.8333
    sort_std: 0.0201
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5176
    std: 0.0306
    paper_value: 0.5176
    paper_std: 0.0306
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 72
    true_value: 0.831
    true_std: 0.032
    value_gap_source_arxiv: '2206.02386'
    value_gap_source_title: Restructuring Graphs for Higher Homophily via Adaptive
      Spectral Clustering
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3134
    value_note: ''
    paper_rank: 220
    rank_delta: 148
    rank_delta_abs: 148
    rank_delta_direction: worse
    sort_value: 0.831
    sort_std: 0.032
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7588
    std: 0.049
    paper_value: 0.7588
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 74
    true_value: 0.8269
    true_std: 0.0084
    value_gap_source_arxiv: '2506.08871'
    value_gap_source_title: Adapting to Heterophilic Graph Data with Structure-Guided
      Neighbor Discovery
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06809999999999994
    value_note: ''
    paper_rank: 114
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.8269
    sort_std: 0.0084
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8039
    std: 0.034
    paper_value: 0.8039
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 80
    true_value: 0.8157
    true_std: 0.0498
    value_gap_source_arxiv: '2105.07634'
    value_gap_source_title: Improving Graph Neural Networks with Simple Architecture
      Design
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011800000000000033
    value_note: global 0.8157 within std
    paper_rank: 82
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.8157
    sort_std: 0.0498
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8118
    std: 0.0556
    paper_value: 0.8118
    paper_std: 0.0556
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 82
    true_value: 0.812
    true_std: 0.056
    value_gap_source_arxiv: '2302.14806'
    value_gap_source_title: Framelet Message Passing
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.000200000000000089
    value_note: global 0.8120 within std
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.812
    sort_std: 0.056
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6451
    std: 0.0366
    paper_value: 0.6451
    paper_std: 0.0366
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 153
    true_value: 0.6451
    true_std: 0.0366
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6451
    sort_std: 0.0366
    is_best: false
  - model: PairNorm
    model_key: pairnorm
    model_plain: PairNorm
    value: 0.4843
    std: 0.0614
    paper_value: 0.4843
    paper_std: 0.0614
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 234
    true_value: 0.4843
    true_std: 0.0614
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 234
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4843
    sort_std: 0.0614
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
  - *id010
  - *id011
- benchmark: LINKX Benchmarks
  datasets:
  - *id012
single_proposed_model: SNNs
main_figure: /figures/2507.00647/main_figure.png
---

