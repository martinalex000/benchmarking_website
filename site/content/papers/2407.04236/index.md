---
title: Graph Pooling via Ricci Flow
arxiv_id: '2407.04236'
source_url: ''
authors: []
published_date: Jul 2024
published_date_iso: 2024-07
abstract: Graph Machine Learning often involves the clustering of nodes based on similarity
  structure encoded in the graph's topology and the nodes' attributes. On homophilous
  graphs, the integration of pooling layers has been shown to enhance the performance
  of Graph Neural Networks by accounting for inherent multi-scale structure. Here,
  similar nodes are grouped together to coarsen the graph and reduce the input size
  in subsequent layers in deeper architectures. In both settings, the underlying clustering
  approach can be implemented via graph pooling operators, which often rely on classical
  tools from Graph Theory. In this work, we introduce a graph pooling operator, which
  utilizes a characterization of the graph's geometry via Ollivier's discrete Ricci
  curvature and an associated geometric flow. Previous Ricci flow based clustering
  approaches have shown great promise across several domains, but are by construction
  unable to account for similarity structure encoded in the node attributes. However,
  in many ML applications, such information is vital for downstream tasks. extends
  such clustering approaches to attributed graphs, allowing for the integration of
  geometric coarsening into Graph Neural Networks as a pooling layer.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- ORC (us)
- ORC (us) [2 iters]
- ORC (us) (4 iterations)
- ORC (us) with GAT
- ORC (us) with GIN
- ORC-Pool
- ORC
mrr: 0.0475
adjusted_mrr: 0.0317
mrr_dataset_count: 2
benchmark_categories:
- Classic
- TU Dortmund
- OGB
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
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
  - model: ORC
    model_key: orc
    model_plain: ORC
    value: 0.71
    std: 0.02
    paper_value: 0.71
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 77
    true_value: 0.71
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.02
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.67
    std: 0.02
    paper_value: 0.67
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 79
    true_value: 0.7
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.029999999999999916
    value_note: ''
    paper_rank: 92
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.7
    sort_std: 0.02
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.7
    std: 0.02
    paper_value: 0.7
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 80
    true_value: 0.7
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.02
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.7
    std: 0.02
    paper_value: 0.7
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 81
    true_value: 0.7
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.02
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.68
    std: 0.02
    paper_value: 0.68
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 87
    true_value: 0.68
    true_std: 0.02
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: ORC (us)
    model_key: orc (us)
    model_plain: ORC (us)
    value: 0.35
    std: 0.04
    paper_value: 0.35
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: 0.04
    is_best: false
  - model: EMD
    model_key: emd
    model_plain: EMD
    value: 0.35
    std: 0.04
    paper_value: 0.35
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: 0.04
    is_best: false
  - model: Sinkhorn
    model_key: sinkhorn
    model_plain: Sinkhorn
    value: 0.35
    std: 0.03
    paper_value: 0.35
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: 0.03
    is_best: false
  - model: ORC-approx
    model_key: orc-approx
    model_plain: ORC-approx
    value: 0.35
    std: 0.03
    paper_value: 0.35
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: 0.03
    is_best: false
  - model: ORC (us) with GIN
    model_key: orc (us) with gin
    model_plain: ORC (us) with GIN
    value: 0.35
    std: 0.04
    paper_value: 0.35
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: 0.04
    is_best: false
  - model: ORC (us) with GAT
    model_key: orc (us) with gat
    model_plain: ORC (us) with GAT
    value: 0.34
    std: 0.04
    paper_value: 0.34
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.34
    sort_std: 0.04
    is_best: false
  - model: ORC (us) (4 iterations)
    model_key: orc (us) (4 iterations)
    model_plain: ORC (us) (4 iterations)
    value: 0.33
    std: 0.02
    paper_value: 0.33
    paper_std: 0.02
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.33
    sort_std: 0.02
    is_best: false
  - model: Curv
    model_key: curv
    model_plain: Curv
    value: 0.32
    std: null
    paper_value: 0.32
    paper_std: null
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.32
    sort_std: null
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.31
    std: 0.04
    paper_value: 0.31
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 211
    sort_value: 0.31
    sort_std: 0.04
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.3
    std: 0.05
    paper_value: 0.3
    paper_std: 0.05
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.3
    sort_std: 0.05
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.29
    std: 0.03
    paper_value: 0.29
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 212
    sort_value: 0.29
    sort_std: 0.03
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.24
    std: 0.12
    paper_value: 0.24
    paper_std: 0.12
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.24
    sort_std: 0.12
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
  - model: ORC (us)
    model_key: orc (us)
    model_plain: ORC (us)
    value: 0.47
    std: 0.04
    paper_value: 0.47
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.47
    sort_std: 0.04
    is_best: false
  - model: EMD
    model_key: emd
    model_plain: EMD
    value: 0.47
    std: 0.04
    paper_value: 0.47
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.47
    sort_std: 0.04
    is_best: false
  - model: Sinkhorn
    model_key: sinkhorn
    model_plain: Sinkhorn
    value: 0.45
    std: 0.03
    paper_value: 0.45
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.45
    sort_std: 0.03
    is_best: false
  - model: ORC-approx
    model_key: orc-approx
    model_plain: ORC-approx
    value: 0.45
    std: 0.03
    paper_value: 0.45
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.45
    sort_std: 0.03
    is_best: false
  - model: ORC (us) [2 iters]
    model_key: orc (us) [2 iters]
    model_plain: ORC (us) [2 iters]
    value: 0.44
    std: 0.05
    paper_value: 0.44
    paper_std: 0.05
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.44
    sort_std: 0.05
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.43
    std: 0.03
    paper_value: 0.43
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 293
    sort_value: 0.43
    sort_std: 0.03
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.37
    std: 0.05
    paper_value: 0.37
    paper_std: 0.05
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 288
    sort_value: 0.37
    sort_std: 0.05
    is_best: false
  - model: CurvPool
    model_key: curvpool
    model_plain: CurvPool
    value: 0.35
    std: null
    paper_value: 0.35
    paper_std: null
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 5
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: null
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.33
    std: 0.05
    paper_value: 0.33
    paper_std: 0.05
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.33
    sort_std: 0.05
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.2
    std: 0.04
    paper_value: 0.2
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.2
    sort_std: 0.04
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
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
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.4
    std: 0.04
    paper_value: 0.4
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 48
    true_value: 0.4
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4
    sort_std: 0.04
    is_best: false
  - model: ORC
    model_key: orc
    model_plain: ORC
    value: 0.38
    std: 0.06
    paper_value: 0.38
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 55
    true_value: 0.38
    true_std: 0.06
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.38
    sort_std: 0.06
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.37
    std: 0.05
    paper_value: 0.37
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 59
    true_value: 0.37
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37
    sort_std: 0.05
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.37
    std: 0.05
    paper_value: 0.37
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 60
    true_value: 0.37
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.37
    sort_std: 0.05
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.31
    std: 0.03
    paper_value: 0.31
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 86
    true_value: 0.31
    true_std: 0.03
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.31
    sort_std: 0.03
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id006
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
  - model: ORC-Pool
    model_key: orc-pool
    model_plain: ORC-Pool
    value: 0.71
    std: 0.04
    paper_value: 0.71
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 86
    true_value: 0.71
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.04
    is_best: false
  - model: HighCurvPool
    model_key: highcurvpool
    model_plain: HighCurvPool
    value: 0.71
    std: 0.051
    paper_value: 0.71
    paper_std: 0.051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: Sanders et al.
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 87
    true_value: 0.71
    true_std: 0.051
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.051
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.65
    std: 0.04
    paper_value: 0.65
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 124
    true_value: 0.65
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 124
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.04
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.65
    std: 0.05
    paper_value: 0.65
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 123
    true_value: 0.65
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.05
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.64
    std: 0.06
    paper_value: 0.64
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 129
    true_value: 0.64
    true_std: 0.06
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 129
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.64
    sort_std: 0.06
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.54
    std: 0.03
    paper_value: 0.54
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 146
    true_value: 0.54
    true_std: 0.03
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 146
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.54
    sort_std: 0.03
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
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
  - model: ORC
    model_key: orc
    model_plain: ORC
    value: 0.9
    std: 0.06
    paper_value: 0.9
    paper_std: 0.06
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 23
    true_value: 0.9
    true_std: 0.06
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: 0.06
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.84
    std: 0.08
    paper_value: 0.84
    paper_std: 0.08
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 69
    true_value: 0.84
    true_std: 0.08
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.08
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.83
    std: 0.07
    paper_value: 0.83
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 78
    true_value: 0.83
    true_std: 0.07
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.07
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.83
    std: 0.09
    paper_value: 0.83
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 79
    true_value: 0.83
    true_std: 0.09
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.09
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.83
    std: 0.08
    paper_value: 0.83
    paper_std: 0.08
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 80
    true_value: 0.83
    true_std: 0.08
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.08
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
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
  - model: ORC-Pool
    model_key: orc-pool
    model_plain: ORC-Pool
    value: 0.78
    std: 0.04
    paper_value: 0.78
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 12
    true_value: 0.78
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.04
    is_best: true
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.76
    std: 0.05
    paper_value: 0.76
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 16
    true_value: 0.77
    true_std: 0.05
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.010000000000000009
    value_note: global 0.7700 within std
    paper_rank: 36
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.77
    sort_std: 0.05
    is_best: true
  - model: HighCurvPool
    model_key: highcurvpool
    model_plain: HighCurvPool
    value: 0.77
    std: 0.061
    paper_value: 0.77
    paper_std: 0.061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 4
    source_ref: Sanders et al.
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 17
    true_value: 0.77
    true_std: 0.061
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.061
    is_best: true
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.76
    std: 0.05
    paper_value: 0.76
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 39
    true_value: 0.76
    true_std: 0.04
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.04
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.75
    std: 0.04
    paper_value: 0.75
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 74
    true_value: 0.75
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.04
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.75
    std: 0.04
    paper_value: 0.75
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 75
    true_value: 0.75
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.04
    is_best: false
  metric: Accuracy
  higher_is_better: true
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
  - model: EMD
    model_key: emd
    model_plain: EMD
    value: 0.24
    std: 0.04
    paper_value: 0.24
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.24
    sort_std: 0.04
    is_best: false
  - model: ORC-Pool
    model_key: orc-pool
    model_plain: ORC-Pool
    value: 0.24
    std: 0.04
    paper_value: 0.24
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.24
    sort_std: 0.04
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.23
    std: 0.04
    paper_value: 0.23
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 169
    sort_value: 0.23
    sort_std: 0.04
    is_best: false
  - model: Sinkhorn
    model_key: sinkhorn
    model_plain: Sinkhorn
    value: 0.22
    std: 0.05
    paper_value: 0.22
    paper_std: 0.05
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.22
    sort_std: 0.05
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.21
    std: 0.03
    paper_value: 0.21
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.21
    sort_std: 0.03
    is_best: false
  - model: ORC-approx
    model_key: orc-approx
    model_plain: ORC-approx
    value: 0.21
    std: 0.03
    paper_value: 0.21
    paper_std: 0.03
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.21
    sort_std: 0.03
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.18
    std: 0.04
    paper_value: 0.18
    paper_std: 0.04
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 170
    sort_value: 0.18
    sort_std: 0.04
    is_best: false
  - model: CurvPool
    model_key: curvpool
    model_plain: CurvPool
    value: 0.15
    std: null
    paper_value: 0.15
    paper_std: null
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.15
    sort_std: null
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.03
    std: 0.02
    paper_value: 0.03
    paper_std: 0.02
    metric: NMI
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.03
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: REDDIT-BINARY
  rows:
  - model: R-method
    model_key: r-method
    model_plain: R-method
    value: 0.945
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.01122'
    title: Learning Efficient Positional Encodings with Graph Neural Networks
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.9199
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 19.22
    arxiv_id: '2309.16014'
    title: Graph-level Representation Learning with Joint-Embedding Predictive Architectures
    date: Sep 2023
    date_display: Sep 2023
    date_iso: 2023-09
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9199
    sort_std: 0.0159
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.918
    std: 0.01
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.918
    sort_std: 0.01
    is_best: false
  - model: ORC
    model_key: orc
    model_plain: ORC
    value: 0.88
    std: 0.02
    paper_value: 0.88
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 9
    true_value: 0.88
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.88
    sort_std: 0.02
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.86
    std: 0.02
    paper_value: 0.86
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 13
    true_value: 0.86
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.02
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.85
    std: 0.02
    paper_value: 0.85
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 17
    true_value: 0.85
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.02
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.85
    std: 0.02
    paper_value: 0.85
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 16
    true_value: 0.85
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.02
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.85
    std: 0.03
    paper_value: 0.85
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 18
    true_value: 0.85
    true_std: 0.03
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.03
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
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
    value: 0.9681
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
    global_rank: 3
    sort_value: 0.9681
    sort_std: 0.0003
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.73
    std: 0.037
    paper_value: 0.73
    paper_std: 0.037
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 141
    true_value: 0.77
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.040000000000000036
    value_note: ''
    paper_rank: 203
    rank_delta: 62
    rank_delta_abs: 62
    rank_delta_direction: worse
    sort_value: 0.77
    sort_std: 0.01
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.7
    std: 0.04
    paper_value: 0.7
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 163
    true_value: 0.76
    true_std: 0.01
    value_gap_source_arxiv: '2501.09821'
    value_gap_source_title: 'bnpool: Bayesian Nonparametric Pooling for Graphs'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.06000000000000005
    value_note: ''
    paper_rank: 210
    rank_delta: 47
    rank_delta_abs: 47
    rank_delta_direction: worse
    sort_value: 0.76
    sort_std: 0.01
    is_best: false
  - model: ORC (us)
    model_key: orc (us)
    model_plain: ORC (us)
    value: 0.73
    std: 0.048
    paper_value: 0.73
    paper_std: 0.048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 205
    true_value: 0.73
    true_std: 0.048
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 205
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.048
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.69
    std: 0.034
    paper_value: 0.69
    paper_std: 0.034
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 212
    true_value: 0.69
    true_std: 0.034
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 212
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.034
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.68
    std: 0.052
    paper_value: 0.68
    paper_std: 0.052
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 214
    true_value: 0.68
    true_std: 0.052
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 214
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.052
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id011
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
  - model: ORC (us)
    model_key: orc (us)
    model_plain: ORC (us)
    value: 0.72
    std: 0.036
    paper_value: 0.72
    paper_std: 0.036
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 53
    true_value: 0.72
    true_std: 0.036
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.036
    is_best: false
  - model: MinCut
    model_key: mincut
    model_plain: MinCut
    value: 0.7
    std: 0.027
    paper_value: 0.7
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 79
    true_value: 0.7
    true_std: 0.027
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.027
    is_best: false
  - model: DMON
    model_key: dmon
    model_plain: DMON
    value: 0.68
    std: 0.028
    paper_value: 0.68
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 85
    true_value: 0.68
    true_std: 0.028
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.028
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
    value: 0.68
    std: 0.04
    paper_value: 0.68
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 86
    true_value: 0.68
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.04
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.65
    std: 0.031
    paper_value: 0.65
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 95
    true_value: 0.65
    true_std: 0.031
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.031
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: TU Dortmund
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: OGB
  datasets:
  - *id010
  - *id011
main_figure: /figures/2407.04236/main_figure.png
---

