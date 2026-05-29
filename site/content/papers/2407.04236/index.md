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
  tools from Graph Theory. In this work, we introduce a graph pooling operator (ORC-Pool),
  which utilizes a characterization of the graph's geometry via Ollivier's discrete
  Ricci curvature and an associated geometric flow. Previous Ricci flow based clustering
  approaches have shown great promise across several domains, but are by construction
  unable to account for similarity structure encoded in the node attributes. However,
  in many ML applications, such information is vital for downstream tasks. ORC-Pool
  extends such clustering approaches to attributed graphs, allowing for the integration
  of geometric coarsening into Graph Neural Networks as a pooling layer.
codebase_url: ''
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- ORC (us)
- ORC-Pool
- ORC
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- Classic
- TU Dortmund
- OGB
- LRGB
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id007
  dataset: COLLAB
  rows:
  - model: novel dynamic message-passing mechanism
    model_key: novel dynamic message-passing mechanism
    model_plain: novel dynamic message-passing mechanism
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 1
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
    codebase_url: https://github.com/sunjss/N2
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8615
    sort_std: 0.001
    is_best: true
  - model: PXGL-GNN
    model_key: pxgl-gnn
    model_plain: PXGL-GNN
    value: 0.8396
    std: 0.0159
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2512.04530'
    title: Explainable Graph Representation Learning via Graph Pattern Analysis
    date: Dec 2025
    date_display: Dec 2025
    date_iso: 2025-12
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8396
    sort_std: 0.0159
    is_best: true
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 158
    true_value: 0.71
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 158
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 160
    true_value: 0.7
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 161
    true_value: 0.7
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.02
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 164
    true_value: 0.68
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 164
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.02
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 172
    true_value: 0.67
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 172
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.67
    sort_std: 0.02
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: CiteSeer
  rows:
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.952
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.952
    sort_std: 0.002
    is_best: true
  - model: Policy-GNN
    model_key: policy-gnn
    model_plain: Policy-GNN
    value: 0.897
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2006.15097'
    title: 'Policy-GNN: Aggregation Optimization for Graph Neural Networks'
    date: Jun 2020
    date_display: Jun 2020
    date_iso: 2020-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.897
    sort_std: 0.021
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.88
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1805.07984'
    title: Adversarial Attacks on Neural Networks for Graph Data
    date: May 2018
    date_display: May 2018
    date_iso: 2018-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.88
    sort_std: null
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.35
    sort_std: 0.04
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.3
    sort_std: 0.05
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 781
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
    variant_inference_reason: 'dataset: exact match'
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
  - model: Self-Explainable GNN
    model_key: self-explainable gnn
    model_plain: Self-Explainable GNN
    value: 0.977
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.977
    sort_std: 0.016
    is_best: true
  - model: GCN-K
    model_key: gcn-k
    model_plain: GCN-K
    value: 0.948
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.007
    is_best: false
  - model: KP-GIN
    model_key: kp-gin
    model_plain: KP-GIN
    value: 0.946
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2108.12055'
    title: Towards Self-Explainable Graph Neural Network
    date: Aug 2021
    date_display: Aug 2021
    date_iso: 2021-08
    codebase_url: https://github.com/EnyanDai/SEGNN
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.946
    sort_std: 0.007
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.47
    sort_std: 0.04
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.43
    sort_std: 0.03
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.37
    sort_std: 0.05
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
    variant_inference_reason: 'dataset: exact match'
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.2
    sort_std: 0.04
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: ENZYMES
  rows:
  - model: C-M
    model_key: c-m
    model_plain: C-M
    value: 0.802
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.802
    sort_std: 0.009
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.794
    std: 0.008
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
    global_rank: 2
    sort_value: 0.794
    sort_std: 0.008
    is_best: true
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.785
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2301.10857'
    title: arXiv:2301.10857
    date: Jan 2023
    date_display: Jan 2023
    date_iso: 2023-01
    codebase_url: https://github.com/Genentech/bandwidth-graph-generation
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.785
    sort_std: 0.01
    is_best: true
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 107
    true_value: 0.4
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 107
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 109
    true_value: 0.38
    true_std: 0.06
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 109
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.38
    sort_std: 0.06
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 113
    true_value: 0.37
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 114
    true_value: 0.37
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 114
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 119
    true_value: 0.31
    true_std: 0.03
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 119
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
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.834
    std: 0.049
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2205.12245'
    title: Asynchronous Neural Networks for Learning in Graphs
    date: May 2022
    date_display: May 2022
    date_iso: 2022-05
    codebase_url: https://github.com/beabevi/ESAN
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.834
    sort_std: 0.049
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.83
    std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.83
    sort_std: 0.032
    is_best: true
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
    codebase_url: https://github.com/Zehong-Wang/GPM
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8267
    sort_std: 0.0047
    is_best: true
  - model: ORC
    model_key: orc
    model_plain: ORC
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 197
    true_value: 0.71
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 197
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.71
    sort_std: 0.04
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 233
    true_value: 0.65
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 233
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.05
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 234
    true_value: 0.65
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 234
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.04
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 237
    true_value: 0.64
    true_std: 0.06
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 237
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 254
    true_value: 0.54
    true_std: 0.03
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 254
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
  - model: RC-Explainer
    model_key: rc-explainer
    model_plain: RC-Explainer
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2204.11028'
    title: Reinforced Causal Explainer for Graph Neural Networks
    date: Apr 2022
    date_display: Apr 2022
    date_iso: 2022-04
    codebase_url: https://github.com/xiangwang1223/reinforced_causal_explainer
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: SVMs
    model_key: svms
    model_plain: SVMs
    value: 0.983
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2203.07691'
    title: Supervised Contrastive Learning with Structure Inference for Graph Classification
    date: Mar 2022
    date_display: Mar 2022
    date_iso: 2022-03
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.983
    sort_std: 0.025
    is_best: true
  - model: Base (GCN)
    model_key: base (gcn)
    model_plain: Base (GCN)
    value: 0.9805
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2202.08816'
    title: Learning and Evaluating Graph Neural Network Explanations based on Counterfactual
      and Factual Reasoning
    date: Feb 2022
    date_display: Feb 2022
    date_iso: 2022-02
    codebase_url: https://github.com/chrisjtan/gnn_cff
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9805
    sort_std: null
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 47
    true_value: 0.9
    true_std: 0.06
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9
    sort_std: 0.06
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 169
    true_value: 0.84
    true_std: 0.08
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.84
    sort_std: 0.08
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 194
    true_value: 0.83
    true_std: 0.09
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 194
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.09
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 195
    true_value: 0.83
    true_std: 0.07
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.07
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 196
    true_value: 0.83
    true_std: 0.08
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 196
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
  - model: HGP-SL
    model_key: hgp-sl
    model_plain: HGP-SL
    value: 0.8491
    std: 0.0162
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8491
    sort_std: 0.0162
    is_best: true
  - model: rLap
    model_key: rlap
    model_plain: rLap
    value: 0.8434
    std: 0.0403
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.04004'
    title: Randomized Schur Complement Views for Graph Contrastive Learning
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: https://github.com/kvignesh1420/rlap
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8434
    sort_std: 0.0403
    is_best: true
  - model: HGP-SL_DEN
    model_key: hgp-sl_den
    model_plain: HGP-SL_DEN
    value: 0.8312
    std: 0.0084
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '1911.05954'
    title: Hierarchical Graph Pooling with Structure Learning
    date: Nov 2019
    date_display: Nov 2019
    date_iso: 2019-11
    codebase_url: https://github.com/cszhangzhen/HGP-SL
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8312
    sort_std: 0.0084
    is_best: true
  - model: ORC
    model_key: orc
    model_plain: ORC
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 46
    true_value: 0.78
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.78
    sort_std: 0.04
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 116
    true_value: 0.76
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 116
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.05
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 117
    true_value: 0.76
    true_std: 0.05
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 117
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.05
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 165
    true_value: 0.75
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 165
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 166
    true_value: 0.75
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 166
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.04
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id012
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
  - model: gLSTM
    model_key: glstm
    model_plain: gLSTM
    value: 0.725
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.08450'
    title: ': Mitigating by Increasing Storage Capacity'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/HughBlayney/gLSTM
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.725
    sort_std: 0.0023
    is_best: true
  - model: ORC
    model_key: orc
    model_plain: ORC
    value: 0.69
    std: 0.01
    paper_value: 0.69
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.69
    sort_std: 0.01
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.67
    sort_std: 0.02
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.67
    sort_std: 0.02
    is_best: false
  - model: TV
    model_key: tv
    model_plain: TV
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.67
    sort_std: 0.02
    is_best: false
  - model: Diff
    model_key: diff
    model_plain: Diff
    value: 0.66
    std: 0.02
    paper_value: 0.66
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.66
    sort_std: 0.02
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: AIO
    model_key: aio
    model_plain: AIO
    value: 0.986
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2510.22555'
    title: Cross-Paradigm Graph Backdoor Attacks with Promptable Subgraph Triggers
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    codebase_url: https://github.com/novdream/CP-GBA
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.986
    sort_std: null
    is_best: true
  - model: S-VAE/VGAE
    model_key: s-vae/vgae
    model_plain: S-VAE/VGAE
    value: 0.96
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2407.09468'
    title: 'Beyond Euclid: An Illustrated Guide to Modern Machine Learning with Geometric,
      Topological, and Algebraic Structures'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.96
    sort_std: 0.001
    is_best: false
  - model: SAGN
    model_key: sagn
    model_plain: SAGN
    value: 0.9517
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.08170'
    title: arXiv:2402.08170
    date: Feb 2024
    date_display: Feb 2024
    date_iso: 2024-02
    codebase_url: https://github.com/VITA-Group/LLaGA
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9517
    sort_std: null
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.24
    sort_std: 0.04
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.23
    sort_std: 0.04
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: null
    sort_value: 0.21
    sort_std: 0.03
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 746
    sort_value: 0.18
    sort_std: 0.04
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
    variant_inference_reason: 'dataset: exact match'
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
  - model: PEs
    model_key: pes
    model_plain: PEs
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
    codebase_url: https://github.com/ehejin/Pearl-PE
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.945
    sort_std: 0.004
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.936
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.936
    sort_std: null
    is_best: false
  - model: Base
    model_key: base
    model_plain: Base
    value: 0.936
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2209.03473'
    title: Higher-order Clustering and Pooling for Graph Neural Networks
    date: Sep 2022
    date_display: Sep 2022
    date_iso: 2022-09
    codebase_url: https://github.com/AlexDuvalinho/HoscPool
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.936
    sort_std: null
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 37
    true_value: 0.88
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 37
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 47
    true_value: 0.86
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 47
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.86
    sort_std: 0.02
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 49
    true_value: 0.85
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.02
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 50
    true_value: 0.85
    true_std: 0.02
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 51
    true_value: 0.85
    true_std: 0.03
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.85
    sort_std: 0.03
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
  dataset: ogbg-molhiv
  rows:
  - model: ML
    model_key: ml
    model_plain: ML
    value: 0.997
    std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.08443'
    title: 'CLEAR: Generative Counterfactual Explanations on Graphs'
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.997
    sort_std: 0.002
    is_best: true
  - model: ILLS
    model_key: ills
    model_plain: ILLS
    value: 0.862
    std: 0.002
    metric: ROC-AUC
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
    global_rank: 2
    sort_value: 0.862
    sort_std: 0.002
    is_best: false
  - model: GraphGPS
    model_key: graphgps
    model_plain: GraphGPS
    value: 0.858
    std: 0.002
    metric: ROC-AUC
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
    sort_std: 0.002
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 161
    true_value: 0.73
    true_std: 0.037
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 161
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.037
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 162
    true_value: 0.73
    true_std: 0.048
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 162
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.73
    sort_std: 0.048
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 168
    true_value: 0.7
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 168
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.04
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 169
    true_value: 0.69
    true_std: 0.034
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 169
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 171
    true_value: 0.68
    true_std: 0.052
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.68
    sort_std: 0.052
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id010
  dataset: ogbn-arxiv
  rows:
  - model: KCoT
    model_key: kcot
    model_plain: KCoT
    value: 0.7925
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2605.24867'
    title: 'Clustering as Reasoning: A $k$-Means Interpretation of Chain-of-Thought
      Graph Learning'
    date: May 24, 2026
    date_display: May 2026
    date_iso: '2026-05-24'
    codebase_url: https://github.com/Uncnbb/KCoT
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.7925
    sort_std: null
    is_best: true
  - model: TAPE + SimTeG
    model_key: tape + simteg
    model_plain: TAPE + SimTeG
    value: 0.7803
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.02565'
    title: 'SimTeG: A Frustratingly ple Approach Improves xtual raph Learning'
    date: Aug 2023
    date_display: Aug 2023
    date_iso: 2023-08
    codebase_url: https://github.com/vermouthdky/SimTeG
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.7803
    sort_std: 0.0007
    is_best: false
  - model: OFA
    model_key: ofa
    model_plain: OFA
    value: 0.7751
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2412.19211'
    title: 'Large Language Models Meet Graph Neural Networks: A Perspective of Graph
      Mining'
    date: Dec 2024
    date_display: Dec 2024
    date_iso: 2024-12
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.7751
    sort_std: 0.0017
    is_best: false
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 215
    true_value: 0.72
    true_std: 0.036
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 215
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.72
    sort_std: 0.036
    is_best: false
  - model: Mincut
    model_key: mincut
    model_plain: Mincut
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 298
    true_value: 0.7
    true_std: 0.027
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 298
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7
    sort_std: 0.027
    is_best: false
  - model: DMoN
    model_key: dmon
    model_plain: DMoN
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 324
    true_value: 0.68
    true_std: 0.028
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 324
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 325
    true_value: 0.68
    true_std: 0.04
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 325
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    global_rank: 348
    true_value: 0.65
    true_std: 0.031
    value_gap_source_arxiv: '2407.04236'
    value_gap_source_title: Graph Pooling via Ricci Flow
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 348
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
- benchmark: LRGB
  datasets:
  - *id012
main_figure: /figures/2407.04236/main_figure.png
---

