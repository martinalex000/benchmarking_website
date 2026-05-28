---
title: 'Design Your Own Universe: A Physics-Informed Agnostic Method for Enhancing
  Graph Neural Networks'
arxiv_id: '2401.14580'
source_url: ''
authors: []
published_date: Jan 26, 2024
published_date_iso: '2024-01-26'
abstract: Physics-informed Graph Neural Networks have achieved remarkable performance
  in learning through graph-structured data by mitigating common GNN challenges such
  as over-smoothing, over-squashing, and heterophily adaption. Despite these advancements,
  the development of a simple yet effective paradigm that appropriately integrates
  previous methods for handling all these challenges is still underway. In this paper,
  we draw an analogy between the propagation of GNNs and particle systems in physics,
  proposing a model-agnostic enhancement framework. This framework enriches the graph
  structure by introducing additional nodes and rewiring connections with both positive
  and negative weights, guided by node labeling information. We theoretically verify
  that GNNs enhanced through our approach can effectively circumvent the over-smoothing
  issue and exhibit robustness against over-squashing. Moreover, we conduct a spectral
  analysis on the rewired graph to demonstrate that the corresponding GNNs can fit
  both homophilic and heterophilic graphs. Empirical validations on benchmarks for
  homophilic, heterophilic graphs, and long-term graph datasets show that GNNs enhanced
  by our method significantly outperform their original counterparts.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- UYGCN
- UYGAT
mrr: 0.125
adjusted_mrr: 0.0417
mrr_dataset_count: 1
benchmark_categories:
- OGB
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id001
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
  - model: UYGCN
    model_key: uygcn
    model_plain: UYGCN
    value: 0.744
    std: 0.009
    paper_value: 0.744
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 8
    true_value: 0.744
    true_std: 0.009
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.744
    sort_std: 0.009
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.712
    std: 0.002
    paper_value: 0.712
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 9
    true_value: 0.741
    true_std: 0.023
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029000000000000026
    value_note: ''
    paper_rank: 71
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.741
    sort_std: 0.023
    is_best: true
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.727
    std: 0.003
    paper_value: 0.727
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 14
    true_value: 0.7353
    true_std: 0.0012
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.008299999999999974
    value_note: ''
    paper_rank: 34
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.7353
    sort_std: 0.0012
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.72
    std: 0.005
    paper_value: 0.72
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 17
    true_value: 0.733
    true_std: 0.0018
    value_gap_source_arxiv: '2406.08993'
    value_gap_source_title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for
      Node Classification'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013000000000000012
    value_note: ''
    paper_rank: 51
    rank_delta: 34
    rank_delta_abs: 34
    rank_delta_direction: worse
    sort_value: 0.733
    sort_std: 0.0018
    is_best: false
  - model: LEGCN
    model_key: legcn
    model_plain: LEGCN
    value: 0.733
    std: 0.003
    paper_value: 0.733
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 18
    true_value: 0.733
    true_std: 0.003
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.733
    sort_std: 0.003
    is_best: false
  - model: H2GCN
    model_key: h2gcn
    model_plain: H2GCN
    value: 0.728
    std: 0.024
    paper_value: 0.728
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 29
    true_value: 0.728
    true_std: 0.024
    value_gap_source_arxiv: '2410.05593'
    value_gap_source_title: When Graph Neural Networks Meet Dynamic Mode Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.024
    is_best: false
  - model: UYGAT
    model_key: uygat
    model_plain: UYGAT
    value: 0.723
    std: 0.003
    paper_value: 0.723
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 46
    true_value: 0.723
    true_std: 0.003
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.003
    is_best: false
  - model: SJLR
    model_key: sjlr
    model_plain: SJLR
    value: 0.72
    std: 0.004
    paper_value: 0.72
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 54
    true_value: 0.72
    true_std: 0.004
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 54
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.004
    is_best: false
  - model: APPNP
    model_key: appnp
    model_plain: APPNP
    value: 0.703
    std: 0.025
    paper_value: 0.703
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 58
    true_value: 0.719
    true_std: 0.0025
    value_gap_source_arxiv: '2405.13806'
    value_gap_source_title: A General Graph Spectral Wavelet Convolution via Chebyshev
      Order Decomposition
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.016000000000000014
    value_note: global 0.7190 within std
    paper_rank: 77
    rank_delta: 19
    rank_delta_abs: 19
    rank_delta_direction: worse
    sort_value: 0.719
    sort_std: 0.0025
    is_best: false
  - model: Replusion
    model_key: replusion
    model_plain: Replusion
    value: 0.719
    std: 0.004
    paper_value: 0.719
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 60
    true_value: 0.719
    true_std: 0.004
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.719
    sort_std: 0.004
    is_best: false
  - model: GPRGNN
    model_key: gprgnn
    model_plain: GPRGNN
    value: 0.704
    std: 0.015
    paper_value: 0.704
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 75
    true_value: 0.711
    true_std: 0.0012
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007000000000000006
    value_note: global 0.7110 within std
    paper_rank: 77
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.711
    sort_std: 0.0012
    is_best: false
  - model: ACMP
    model_key: acmp
    model_plain: ACMP
    value: 0.689
    std: 0.003
    paper_value: 0.689
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 81
    true_value: 0.689
    true_std: 0.003
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.689
    sort_std: 0.003
    is_best: false
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.55
    std: 0.003
    paper_value: 0.55
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 91
    true_value: 0.666
    true_std: 0.0025
    value_gap_source_arxiv: '2307.03393'
    value_gap_source_title: Exploring the Potential of Large Language Models (LLMs)
      in Learning on Graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11599999999999999
    value_note: ''
    paper_rank: 101
    rank_delta: 10
    rank_delta_abs: 10
    rank_delta_direction: worse
    sort_value: 0.666
    sort_std: 0.0025
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.645
    std: 0.025
    paper_value: 0.645
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
    date: Jan 26, 2024
    date_display: Jan 2024
    date_iso: '2024-01-26'
    global_rank: 96
    true_value: 0.645
    true_std: 0.025
    value_gap_source_arxiv: '2401.14580'
    value_gap_source_title: 'Design Your Own Universe: A Physics-Informed Agnostic
      Method for Enhancing Graph Neural Networks'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.645
    sort_std: 0.025
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
main_figure: /figures/2401.14580/main_figure.png
---

