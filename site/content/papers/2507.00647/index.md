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
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CSNN
mrr: 0.1961
adjusted_mrr: 0.1961
mrr_dataset_count: 10
benchmark_categories:
- Heterophilic Graphs
- LINKX Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id005
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
    value: 0.49090000000000006
    std: 0.0063
    paper_value: 0.49090000000000006
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.5554
    true_std: 0.0051
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06449999999999995
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
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.542
    std: 0.0034000000000000002
    paper_value: 0.542
    paper_std: 0.0034000000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.542
    true_std: 0.0034000000000000002
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
    sort_value: 0.542
    sort_std: 0.0034000000000000002
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.48700000000000004
    std: 0.0063
    paper_value: 0.48700000000000004
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.538
    true_std: 0.0
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05099999999999999
    value_note: ''
    paper_rank: 58
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.538
    sort_std: 0.0
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 18
    true_value: 0.5374
    true_std: 0.0051
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
    sort_value: 0.5374
    sort_std: 0.0051
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.5363
    std: 0.0039000000000000003
    paper_value: 0.5363
    paper_std: 0.0039000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 37
    true_value: 0.5207
    true_std: 0.01
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 85
    true_value: 0.4276
    true_std: 0.0054
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4276
    sort_std: 0.0054
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
    value: 0.8514
    std: 0.060700000000000004
    paper_value: 0.8514
    paper_std: 0.060700000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.9393
    true_std: 0.0105
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08789999999999998
    value_note: ''
    paper_rank: 21
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
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
  - model: ACMII-Snowball-3
    model_key: acmii-snowball-3
    model_plain: ACMII-Snowball-3
    value: 0.9361
    std: 0.0279
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
    global_rank: 4
    sort_value: 0.9361
    sort_std: 0.0279
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.8027
    std: 0.08109999999999999
    paper_value: 0.8027
    paper_std: 0.08109999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.9136
    true_std: 0.007
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1109
    value_note: ''
    paper_rank: 29
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9136
    sort_std: 0.007
    is_best: false
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.913
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09410000000000007
    value_note: ''
    paper_rank: 27
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.913
    sort_std: 0.007
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.9049
    true_std: 0.0445
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12630000000000008
    value_note: ''
    paper_rank: 32
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9049
    sort_std: 0.0445
    is_best: true
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.7918999999999999
    std: 0.09789999999999999
    paper_value: 0.7918999999999999
    paper_std: 0.09789999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 15
    true_value: 0.8803
    true_std: 0.056
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.08840000000000003
    value_note: global 0.8803 within std
    paper_rank: 31
    rank_delta: 16
    rank_delta_abs: 16
    rank_delta_direction: worse
    sort_value: 0.8803
    sort_std: 0.056
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.873
    true_std: 0.0453
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.8649
    true_std: 0.0735
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
    sort_value: 0.8649
    sort_std: 0.0735
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8270000000000001
    std: 0.0528
    paper_value: 0.8270000000000001
    paper_std: 0.0528
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 18
    true_value: 0.8623
    true_std: 0.0471
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.03529999999999989
    value_note: global 0.8623 within std
    paper_rank: 26
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.8623
    sort_std: 0.0471
    is_best: false
  - model: GGCN
    model_key: ggcn
    model_plain: GGCN
    value: 0.8568000000000001
    std: 0.0663
    paper_value: 0.8568000000000001
    paper_std: 0.0663
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 20
    true_value: 0.8568000000000001
    true_std: 0.0663
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
    sort_value: 0.8568000000000001
    sort_std: 0.0663
    is_best: false
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8568000000000001
    std: 0.06509999999999999
    paper_value: 0.8568000000000001
    paper_std: 0.06509999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 21
    true_value: 0.8568000000000001
    true_std: 0.06509999999999999
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
    sort_value: 0.8568000000000001
    sort_std: 0.06509999999999999
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 22
    true_value: 0.8486
    true_std: 0.0471
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
    sort_value: 0.8486
    sort_std: 0.0471
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.8351000000000001
    std: 0.0426
    paper_value: 0.8351000000000001
    paper_std: 0.0426
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.8351000000000001
    true_std: 0.0426
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
    sort_value: 0.8351000000000001
    sort_std: 0.0426
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.6053999999999999
    std: 0.053
    paper_value: 0.6053999999999999
    paper_std: 0.053
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 27
    true_value: 0.8246
    true_std: 0.0311
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.21920000000000006
    value_note: ''
    paper_rank: 99
    rank_delta: 72
    rank_delta_abs: 72
    rank_delta_direction: worse
    sort_value: 0.8246
    sort_std: 0.0311
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 28
    true_value: 0.8162
    true_std: 0.0432
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
    sort_value: 0.8162
    sort_std: 0.0432
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.7595000000000001
    std: 0.0501
    paper_value: 0.7595000000000001
    paper_std: 0.0501
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 30
    true_value: 0.8008
    true_std: 0.0296
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.04129999999999989
    value_note: global 0.8008 within std
    paper_rank: 37
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.8008
    sort_std: 0.0296
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.6189
    std: 0.050499999999999996
    paper_value: 0.6189
    paper_std: 0.050499999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 37
    true_value: 0.76
    true_std: 0.0101
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1411
    value_note: ''
    paper_rank: 96
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.0101
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7351000000000001
    std: 0.0634
    paper_value: 0.7351000000000001
    paper_std: 0.0634
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 45
    true_value: 0.7351000000000001
    true_std: 0.0634
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
    sort_value: 0.7351000000000001
    sort_std: 0.0634
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 47
    true_value: 0.727
    true_std: 0.0547
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.727
    sort_std: 0.0547
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6053999999999999
    std: 0.036699999999999997
    paper_value: 0.6053999999999999
    paper_std: 0.036699999999999997
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 99
    true_value: 0.6081
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027000000000000357
    value_note: global 0.6081 within std
    paper_rank: 99
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6081
    sort_std: null
    is_best: false
  - model: + PairNorm
    model_key: + pairnorm
    model_plain: + PairNorm
    value: 0.5892000000000001
    std: 0.0315
    paper_value: 0.5892000000000001
    paper_std: 0.0315
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 103
    true_value: 0.5892000000000001
    true_std: 0.0315
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5892000000000001
    sort_std: 0.0315
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: Film
  rows:
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.4186
    true_std: 0.0148
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.055800000000000016
    value_note: ''
    paper_rank: 27
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.4186
    sort_std: 0.0148
    is_best: true
  - model: BernNet
    model_key: bernnet
    model_plain: BernNet
    value: 0.4179
    std: 0.0101
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
    sort_value: 0.4179
    sort_std: 0.0101
    is_best: true
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.4166
    std: 0.0142
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
    sort_value: 0.4166
    sort_std: 0.0142
    is_best: true
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.4154
    true_std: 0.0099
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.041000000000000036
    value_note: ''
    paper_rank: 18
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.4154
    sort_std: 0.0099
    is_best: true
  - model: ACM-Snowball-2
    model_key: acm-snowball-2
    model_plain: ACM-Snowball-2
    value: 0.414
    std: 0.0123
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
    global_rank: 5
    sort_value: 0.414
    sort_std: 0.0123
    is_best: true
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.393
    true_std: 0.0027
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046699999999999964
    value_note: ''
    paper_rank: 35
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.393
    sort_std: 0.0027
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.3885
    true_std: 0.0117
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.03149999999999997
    value_note: ''
    paper_rank: 30
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.3885
    sort_std: 0.0117
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.3803
    std: 0.011200000000000002
    paper_value: 0.3803
    paper_std: 0.011200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.3803
    true_std: 0.011200000000000002
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 15
    true_value: 0.37810000000000005
    true_std: 0.0115
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.37799999999999995
    true_std: 0.012199999999999999
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.3779
    true_std: 0.0101
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
    sort_value: 0.3779
    sort_std: 0.0101
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 18
    true_value: 0.3754
    true_std: 0.015600000000000001
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
    sort_value: 0.3754
    sort_std: 0.015600000000000001
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 19
    true_value: 0.3735
    true_std: 0.013000000000000001
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.3653
    true_std: 0.006999999999999999
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
    sort_value: 0.3653
    sort_std: 0.006999999999999999
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 27
    true_value: 0.3637
    true_std: 0.0021
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02140000000000003
    value_note: ''
    paper_rank: 36
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.3637
    sort_std: 0.0021
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 28
    true_value: 0.3626
    true_std: 0.0374
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
    sort_value: 0.3626
    sort_std: 0.0374
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 30
    true_value: 0.3598
    true_std: 0.0023
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08539999999999998
    value_note: ''
    paper_rank: 43
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.3598
    sort_std: 0.0023
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 31
    true_value: 0.35619999999999996
    true_std: 0.0087
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35619999999999996
    sort_std: 0.0087
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 32
    true_value: 0.3551
    true_std: 0.0099
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08190000000000003
    value_note: ''
    paper_rank: 44
    rank_delta: 12
    rank_delta_abs: 12
    rank_delta_direction: worse
    sort_value: 0.3551
    sort_std: 0.0099
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 35
    true_value: 0.34869999999999995
    true_std: 0.0125
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
    sort_value: 0.34869999999999995
    sort_std: 0.0125
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 38
    true_value: 0.3313
    true_std: 0.024
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.009099999999999997
    value_note: global 0.3313 within std
    paper_rank: 39
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.3313
    sort_std: 0.024
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 41
    true_value: 0.3163
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00040000000000001146
    value_note: global 0.3163 within std
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3163
    sort_std: null
    is_best: false
  - model: + PairNorm
    model_key: + pairnorm
    model_plain: + PairNorm
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 44
    true_value: 0.27399999999999997
    true_std: 0.0124
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
    sort_value: 0.27399999999999997
    sort_std: 0.0124
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
  dataset: Minesweeper
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9906999999999999
    std: 0.0025
    paper_value: 0.9906999999999999
    paper_std: 0.0025
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.9906999999999999
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
    sort_value: 0.9906999999999999
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
    variant_inference_reason: ''
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
  - model: Tango<sub>GatedGCN</sub>
    model_key: tango\textsubscript{gatedgcn}
    model_plain: TangoGatedGCN
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
  - model: NeuralWalker
    model_key: neuralwalker
    model_plain: NeuralWalker
    value: 0.9782
    std: 0.004
    metric: ROC-AUC
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
    global_rank: 6
    sort_value: 0.9782
    sort_std: 0.004
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.9201
    std: 0.0068000000000000005
    paper_value: 0.9201
    paper_std: 0.0068000000000000005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.9734999999999999
    std: 0.0063
    paper_value: 0.9734999999999999
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.9734999999999999
    true_std: 0.0063
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
    sort_value: 0.9734999999999999
    sort_std: 0.0063
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.9229
    std: 0.004699999999999999
    paper_value: 0.9229
    paper_std: 0.004699999999999999
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    std: 0.005699999999999999
    paper_value: 0.9351
    paper_std: 0.005699999999999999
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.9215000000000001
    std: 0.0084
    paper_value: 0.9215000000000001
    paper_std: 0.0084
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 49
    true_value: 0.9215000000000001
    true_std: 0.0084
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
    sort_value: 0.9215000000000001
    sort_std: 0.0084
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
- &id011
  dataset: Penn94
  rows:
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.86
    std: 0.0039000000000000003
    paper_value: 0.86
    paper_std: 0.0039000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.86
    true_std: 0.0039000000000000003
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
    sort_std: 0.0039000000000000003
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
    value: 0.8556999999999999
    std: 0.0034999999999999996
    paper_value: 0.8556999999999999
    paper_std: 0.0034999999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.8556999999999999
    true_std: 0.0034999999999999996
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
    sort_value: 0.8556999999999999
    sort_std: 0.0034999999999999996
    is_best: true
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.8471
    true_std: 0.0052
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
    sort_value: 0.8471
    sort_std: 0.0052
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.8347
    std: 0.0070999999999999995
    paper_value: 0.8347
    paper_std: 0.0070999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.8347
    true_std: 0.0070999999999999995
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
    sort_value: 0.8347
    sort_std: 0.0070999999999999995
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.8292
    true_std: 0.0059
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
    sort_value: 0.8292
    sort_std: 0.0059
    is_best: false
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8251999999999999
    std: 0.0096
    paper_value: 0.8251999999999999
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.8251999999999999
    true_std: 0.0096
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
    sort_value: 0.8251999999999999
    sort_std: 0.0096
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 7
    true_value: 0.8247
    true_std: 0.0027
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
    sort_value: 0.8247
    sort_std: 0.0027
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8153
    std: 0.0055000000000000005
    paper_value: 0.8153
    paper_std: 0.0055000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.8153
    true_std: 0.0055000000000000005
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
    sort_value: 0.8153
    sort_std: 0.0055000000000000005
    is_best: false
  - model: Supervised
    model_key: supervised
    model_plain: Supervised
    value: 0.8153
    std: 0.0055
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
    global_rank: 9
    sort_value: 0.8153
    sort_std: 0.0055
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.8138
    true_std: 0.0016
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
    sort_value: 0.8138
    sort_std: 0.0016
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.8131
    true_std: 0.006
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.7432
    true_std: 0.0053
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.7361
    true_std: 0.004
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
    sort_value: 0.7361
    sort_std: 0.004
    is_best: false
  - model: GraphMAE
    model_key: graphmae
    model_plain: GraphMAE
    value: 0.7179
    std: 0.0037
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
    global_rank: 14
    sort_value: 0.7179
    sort_std: 0.0037
    is_best: false
  - model: S2GAE
    model_key: s2gae
    model_plain: S2GAE
    value: 0.7024
    std: 0.0009
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
    global_rank: 15
    sort_value: 0.7024
    sort_std: 0.0009
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.7931
    std: 0.012199999999999999
    paper_value: 0.7931
    paper_std: 0.012199999999999999
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 9
    true_value: 0.7931
    true_std: 0.012199999999999999
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
    sort_value: 0.7931
    sort_std: 0.012199999999999999
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.7875
    true_std: 0.0109
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
    sort_value: 0.7875
    sort_std: 0.0109
    is_best: true
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.7805
    std: 0.009300000000000001
    paper_value: 0.7805
    paper_std: 0.009300000000000001
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    value: 0.7795000000000001
    std: 0.0068000000000000005
    paper_value: 0.7795000000000001
    paper_std: 0.0068000000000000005
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 23
    true_value: 0.7795000000000001
    true_std: 0.0068000000000000005
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
    sort_value: 0.7795000000000001
    sort_std: 0.0068000000000000005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.7743000000000001
    std: 0.012
    paper_value: 0.7743000000000001
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 24
    true_value: 0.7795
    true_std: 0.0051
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.005199999999999871
    value_note: global 0.7795 within std
    paper_rank: 31
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7795
    sort_std: 0.0051
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 47
    true_value: 0.7597
    true_std: 0.0089
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
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
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 57
    true_value: 0.6969
    true_std: 0.0146
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6969
    sort_std: 0.0146
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
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
    paper_value: 0.9262999999999999
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.9262999999999999
    true_std: 0.005
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
    sort_value: 0.9262999999999999
    sort_std: 0.005
    is_best: true
  - model: GENs
    model_key: gens
    model_plain: GENs
    value: 0.9252
    std: 0.005
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
    global_rank: 4
    sort_value: 0.9252
    sort_std: 0.005
    is_best: true
  - model: BuNN
    model_key: bunn
    model_plain: BuNN
    value: 0.9175
    std: 0.0039000000000000003
    paper_value: 0.9175
    paper_std: 0.0039000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.9175
    true_std: 0.0039000000000000003
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
    sort_value: 0.9175
    sort_std: 0.0039000000000000003
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    value: 0.8087000000000001
    std: 0.003
    paper_value: 0.8087000000000001
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 26
    true_value: 0.9063
    true_std: 0.0014
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09759999999999991
    value_note: ''
    paper_rank: 67
    rank_delta: 41
    rank_delta_abs: 41
    rank_delta_direction: worse
    sort_value: 0.9063
    sort_std: 0.0014
    is_best: false
  - model: CO-GNN
    model_key: co-gnn
    model_plain: CO-GNN
    value: 0.8944
    std: 0.005
    paper_value: 0.8944
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 30
    true_value: 0.8944
    true_std: 0.005
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8944
    sort_std: 0.005
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8732
    std: 0.0039000000000000003
    paper_value: 0.8732
    paper_std: 0.0039000000000000003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
    value: 0.8651000000000001
    std: 0.0073
    paper_value: 0.8651000000000001
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 44
    true_value: 0.8651000000000001
    true_std: 0.0073
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
    sort_value: 0.8651000000000001
    sort_std: 0.0073
    is_best: false
  - model: SAGE
    model_key: sage
    model_plain: SAGE
    value: 0.8573999999999999
    std: 0.0067
    paper_value: 0.8573999999999999
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
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
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8040999999999999
    std: 0.0072
    paper_value: 0.8040999999999999
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
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 69
    true_value: 0.8040999999999999
    true_std: 0.0072
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8040999999999999
    sort_std: 0.0072
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 3
    true_value: 0.741
    true_std: 0.0189
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.38480000000000003
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.6856
    true_std: 0.0133
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.3228
    value_note: ''
    paper_rank: 97
    rank_delta: 87
    rank_delta_abs: 87
    rank_delta_direction: worse
    sort_value: 0.6856
    sort_std: 0.0133
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 23
    true_value: 0.6121
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.23859999999999998
    value_note: ''
    paper_rank: 94
    rank_delta: 71
    rank_delta_abs: 71
    rank_delta_direction: worse
    sort_value: 0.6121
    sort_std: null
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 28
    true_value: 0.5517
    true_std: 0.0158
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17629999999999996
    value_note: ''
    paper_rank: 92
    rank_delta: 64
    rank_delta_abs: 64
    rank_delta_direction: worse
    sort_value: 0.5517
    sort_std: 0.0158
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 31
    true_value: 0.5343
    true_std: 0.0201
    value_gap_source_arxiv: '2409.11504'
    value_gap_source_title: Preventing Representational Rank Collapse in MPNNs by
      Splitting the Computational Graph
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2611
    value_note: ''
    paper_rank: 111
    rank_delta: 80
    rank_delta_abs: 80
    rank_delta_direction: worse
    sort_value: 0.5343
    sort_std: 0.0201
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 41
    true_value: 0.5015
    true_std: 0.0192
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1551999999999999
    value_note: ''
    paper_rank: 103
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.5015
    sort_std: 0.0192
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 51
    true_value: 0.4449
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.17049999999999998
    value_note: ''
    paper_rank: 110
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.4449
    sort_std: 0.0088
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 54
    true_value: 0.438
    true_std: 0.0148
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11580000000000001
    value_note: ''
    paper_rank: 107
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.438
    sort_std: 0.0148
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 67
    true_value: 0.4224
    true_std: 0.012
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07370000000000004
    value_note: ''
    paper_rank: 103
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.4224
    sort_std: 0.012
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 69
    true_value: 0.41609999999999997
    true_std: 0.0074
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.07379999999999998
    value_note: ''
    paper_rank: 105
    rank_delta: 36
    rank_delta_abs: 36
    rank_delta_direction: worse
    sort_value: 0.41609999999999997
    sort_std: 0.0074
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 78
    true_value: 0.3953
    true_std: 0.0088
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.038299999999999945
    value_note: ''
    paper_rank: 99
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.3953
    sort_std: 0.0088
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 83
    true_value: 0.3847
    true_std: 0.0158
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010300000000000031
    value_note: global 0.3847 within std
    paper_rank: 93
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.3847
    sort_std: 0.0158
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 85
    true_value: 0.3815
    true_std: 0.0092
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06559999999999999
    value_note: ''
    paper_rank: 108
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.3815
    sort_std: 0.0092
    is_best: false
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.3803
    std: 0.011200000000000002
    paper_value: 0.3803
    paper_std: 0.011200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 86
    true_value: 0.3803
    true_std: 0.011200000000000002
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 89
    true_value: 0.37810000000000005
    true_std: 0.0115
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 90
    true_value: 0.37799999999999995
    true_std: 0.012199999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 91
    true_value: 0.3779
    true_std: 0.0101
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 91
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3779
    sort_std: 0.0101
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 96
    true_value: 0.366
    true_std: 0.018000000000000002
    value_gap_source_arxiv: '2512.14619'
    value_gap_source_title: 'ParaFormer: A Generalized PageRank Graph Transformer
      for Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006999999999999784
    value_note: global 0.3660 within std
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.366
    sort_std: 0.018000000000000002
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 98
    true_value: 0.3626
    true_std: 0.0374
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3626
    sort_std: 0.0374
    is_best: false
  - model: + PairNorm
    model_key: + pairnorm
    model_plain: + PairNorm
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 111
    true_value: 0.27399999999999997
    true_std: 0.0124
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.27399999999999997
    sort_std: 0.0124
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Texas
  rows:
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8784000000000001
    std: 0.044000000000000004
    paper_value: 0.8784000000000001
    paper_std: 0.044000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 1
    true_value: 0.9656
    true_std: 0.02
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.08719999999999994
    value_note: ''
    paper_rank: 29
    rank_delta: 28
    rank_delta_abs: 28
    rank_delta_direction: worse
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
  - model: ACMII-GCN
    model_key: acmii-gcn
    model_plain: ACMII-GCN
    value: 0.9475
    std: 0.0291
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
    global_rank: 4
    sort_value: 0.9475
    sort_std: 0.0291
    is_best: true
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.7837999999999999
    std: 0.0436
    paper_value: 0.7837999999999999
    paper_std: 0.0436
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 11
    true_value: 0.9295
    true_std: 0.0131
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14570000000000005
    value_note: ''
    paper_rank: 68
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.9295
    sort_std: 0.0131
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.923
    true_std: 0.007
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1149
    value_note: ''
    paper_rank: 61
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.923
    sort_std: 0.007
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 17
    true_value: 0.9189
    true_std: 0.0393
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.07030000000000003
    value_note: global 0.9189 within std
    paper_rank: 36
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.9189
    sort_std: 0.0393
    is_best: true
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 25
    true_value: 0.8885
    true_std: 0.0439
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.06419999999999992
    value_note: global 0.8885 within std
    paper_rank: 50
    rank_delta: 25
    rank_delta_abs: 25
    rank_delta_direction: worse
    sort_value: 0.8885
    sort_std: 0.0439
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 28
    true_value: 0.8852
    true_std: 0.0302
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10950000000000004
    value_note: ''
    paper_rank: 72
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.8852
    sort_std: 0.0302
    is_best: false
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8756999999999999
    std: 0.048600000000000004
    paper_value: 0.8756999999999999
    paper_std: 0.048600000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 30
    true_value: 0.8756999999999999
    true_std: 0.048600000000000004
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8756999999999999
    sort_std: 0.048600000000000004
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 31
    true_value: 0.873
    true_std: 0.0593
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
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
    std: 0.055099999999999996
    paper_value: 0.8595
    paper_std: 0.055099999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 33
    true_value: 0.8595
    true_std: 0.055099999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8595
    sort_std: 0.055099999999999996
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 34
    true_value: 0.8567
    true_std: 0.0695
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 37
    true_value: 0.8486
    true_std: 0.0455
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8486
    sort_std: 0.0455
    is_best: false
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 41
    true_value: 0.8432
    true_std: 0.0415
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8432
    sort_std: 0.0415
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 46
    true_value: 0.8311
    true_std: 0.032
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.27969999999999995
    value_note: ''
    paper_rank: 160
    rank_delta: 114
    rank_delta_abs: 114
    rank_delta_direction: worse
    sort_value: 0.8311
    sort_std: 0.032
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 48
    true_value: 0.8297
    true_std: 0.0513
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
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
    std: 0.061399999999999996
    paper_value: 0.8243
    paper_std: 0.061399999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 51
    true_value: 0.8243
    true_std: 0.061399999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8243
    sort_std: 0.061399999999999996
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 61
    true_value: 0.8082
    true_std: 0.0213
    value_gap_source_arxiv: '2411.17296'
    value_gap_source_title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.2866000000000001
    value_note: ''
    paper_rank: 162
    rank_delta: 101
    rank_delta_abs: 101
    rank_delta_direction: worse
    sort_value: 0.8082
    sort_std: 0.0213
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7784
    std: 0.07730000000000001
    paper_value: 0.7784
    paper_std: 0.07730000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 70
    true_value: 0.7784
    true_std: 0.07730000000000001
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7784
    sort_std: 0.07730000000000001
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 73
    true_value: 0.7757
    true_std: 0.0541
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7757
    sort_std: 0.0541
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.6676000000000001
    std: 0.027200000000000002
    paper_value: 0.6676000000000001
    paper_std: 0.027200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 119
    true_value: 0.676
    true_std: null
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.008399999999999963
    value_note: global 0.6760 within std
    paper_rank: 122
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.676
    sort_std: null
    is_best: false
  - model: + PairNorm
    model_key: + pairnorm
    model_plain: + PairNorm
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 147
    true_value: 0.6027
    true_std: 0.0434
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6027
    sort_std: 0.0434
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
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
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.8545
    std: 0.0053
    paper_value: 0.8545
    paper_std: 0.0053
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.8545
    true_std: 0.0053
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 25
    true_value: 0.8484
    true_std: 0.0096
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 29
    true_value: 0.8478
    true_std: 0.008
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 44
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
    paper_rank: 49
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.838
    sort_std: 0.0034
    is_best: false
  - model: GAT-sep
    model_key: gat-sep
    model_plain: GAT-sep
    value: 0.8251999999999999
    std: 0.0092
    paper_value: 0.8251999999999999
    paper_std: 0.0092
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 45
    true_value: 0.8378
    true_std: 0.0043
    value_gap_source_arxiv: '2505.23185'
    value_gap_source_title: Improving the Effective Receptive Field of Message-Passing
      Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012600000000000056
    value_note: ''
    paper_rank: 58
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.8378
    sort_std: 0.0043
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.8370000000000001
    std: 0.004699999999999999
    paper_value: 0.8370000000000001
    paper_std: 0.004699999999999999
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 48
    true_value: 0.8370000000000001
    true_std: 0.004699999999999999
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8370000000000001
    sort_std: 0.004699999999999999
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 55
    true_value: 0.8323
    true_std: 0.0064
    value_gap_source_arxiv: '2508.05070'
    value_gap_source_title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential
      Flows'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8323
    sort_std: 0.0064
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 61
    true_value: 0.8243
    true_std: 0.0044
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 67
    true_value: 0.7883
    true_std: 0.0076
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
    sort_value: 0.7883
    sort_std: 0.0076
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id003
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
    value: 0.8529000000000001
    std: 0.0331
    paper_value: 0.8529000000000001
    paper_std: 0.0331
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 2
    true_value: 0.918
    true_std: 0.031
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06509999999999994
    value_note: ''
    paper_rank: 21
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
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
  - model: CSNN
    model_key: csnn
    model_plain: CSNN
    value: 0.9
    std: 0.028300000000000002
    paper_value: 0.9
    paper_std: 0.028300000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 4
    true_value: 0.9
    true_std: 0.028300000000000002
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
    sort_value: 0.9
    sort_std: 0.028300000000000002
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 5
    true_value: 0.899
    true_std: 0.03
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0696
    value_note: ''
    paper_rank: 26
    rank_delta: 21
    rank_delta_abs: 21
    rank_delta_direction: worse
    sort_value: 0.899
    sort_std: 0.03
    is_best: true
  - model: O(d)-NSD
    model_key: o(d)-nsd
    model_plain: O(d)-NSD
    value: 0.8941
    std: 0.047400000000000005
    paper_value: 0.8941
    paper_std: 0.047400000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 6
    true_value: 0.8941
    true_std: 0.047400000000000005
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
    sort_value: 0.8941
    sort_std: 0.047400000000000005
    is_best: true
  - model: DMD-ACMP
    model_key: dmd-acmp
    model_plain: DMD-ACMP
    value: 0.894
    std: 0.022
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
    global_rank: 7
    sort_value: 0.894
    sort_std: 0.022
    is_best: true
  - model: Gen-NSD
    model_key: gen-nsd
    model_plain: Gen-NSD
    value: 0.8920999999999999
    std: 0.0384
    paper_value: 0.8920999999999999
    paper_std: 0.0384
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 8
    true_value: 0.8920999999999999
    true_std: 0.0384
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
    sort_value: 0.8920999999999999
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 10
    true_value: 0.8863
    true_std: 0.0275
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
    sort_value: 0.8863
    sort_std: 0.0275
    is_best: true
  - model: ACMGCN
    model_key: acmgcn
    model_plain: ACMGCN
    value: 0.8843000000000001
    std: 0.0322
    paper_value: 0.8843000000000001
    paper_std: 0.0322
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 12
    true_value: 0.8843000000000001
    true_std: 0.0322
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
    sort_value: 0.8843000000000001
    sort_std: 0.0322
    is_best: true
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.8765000000000001
    std: 0.049800000000000004
    paper_value: 0.8765000000000001
    paper_std: 0.049800000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 13
    true_value: 0.879
    true_std: 0.042
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0024999999999999467
    value_note: global 0.8790 within std
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.879
    sort_std: 0.042
    is_best: true
  - model: FSGNN
    model_key: fsgnn
    model_plain: FSGNN
    value: 0.8765000000000001
    std: 0.0351
    paper_value: 0.8765000000000001
    paper_std: 0.0351
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 14
    true_value: 0.8765000000000001
    true_std: 0.0351
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
    sort_value: 0.8765000000000001
    sort_std: 0.0351
    is_best: true
  - model: GLoGNN
    model_key: glognn
    model_plain: GLoGNN
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 16
    true_value: 0.8706
    true_std: 0.0353
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
    sort_value: 0.8706
    sort_std: 0.0353
    is_best: true
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 19
    true_value: 0.8686
    true_std: 0.0329
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
    sort_value: 0.8686
    sort_std: 0.0329
    is_best: true
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 25
    true_value: 0.8373
    true_std: 0.0403
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 27
    true_value: 0.8294
    true_std: 0.0795
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
    sort_value: 0.8294
    sort_std: 0.0795
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.8118000000000001
    std: 0.0556
    paper_value: 0.8118000000000001
    paper_std: 0.0556
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 36
    true_value: 0.8136
    true_std: 0.0391
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0017999999999999128
    value_note: global 0.8136 within std
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8136
    sort_std: 0.0391
    is_best: false
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.8039000000000001
    std: 0.034
    paper_value: 0.8039000000000001
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 39
    true_value: 0.8039000000000001
    true_std: 0.034
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039000000000001
    sort_std: 0.034
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.5176
    std: 0.030600000000000002
    paper_value: 0.5176
    paper_std: 0.030600000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 53
    true_value: 0.7863
    true_std: 0.0543
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.26870000000000005
    value_note: ''
    paper_rank: 134
    rank_delta: 81
    rank_delta_abs: 81
    rank_delta_direction: worse
    sort_value: 0.7863
    sort_std: 0.0543
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 61
    true_value: 0.7817
    true_std: 0.057
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.28759999999999997
    value_note: ''
    paper_rank: 136
    rank_delta: 75
    rank_delta_abs: 75
    rank_delta_direction: worse
    sort_value: 0.7817
    sort_std: 0.057
    is_best: false
  - model: MixHop
    model_key: mixhop
    model_plain: MixHop
    value: 0.7587999999999999
    std: 0.049
    paper_value: 0.7587999999999999
    paper_std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 66
    true_value: 0.7745
    true_std: 0.031
    value_gap_source_arxiv: '2410.05697'
    value_gap_source_title: 'Diffusing to the Top: Boost Graph Neural Networks with
      Minimal Hyperparameter Tuning'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.015700000000000047
    value_note: global 0.7745 within std
    paper_rank: 76
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.7745
    sort_std: 0.031
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
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 111
    true_value: 0.6451
    true_std: 0.0366
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6451
    sort_std: 0.0366
    is_best: false
  - model: + PairNorm
    model_key: + pairnorm
    model_plain: + PairNorm
    value: 0.4843
    std: 0.061399999999999996
    paper_value: 0.4843
    paper_std: 0.061399999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2025
    date_display: Jul 2025
    date_iso: 2025-07
    global_rank: 137
    true_value: 0.4843
    true_std: 0.061399999999999996
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4843
    sort_std: 0.061399999999999996
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
- benchmark: LINKX Benchmarks
  datasets:
  - *id011
single_proposed_model: CSNN
main_figure: /figures/2507.00647/main_figure.png
---

