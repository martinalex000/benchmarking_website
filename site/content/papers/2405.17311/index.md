---
title: Probabilistic Graph Rewiring via Virtual Nodes
arxiv_id: '2405.17311'
source_url: ''
authors: []
published_date: May 2024
published_date_iso: 2024-05
abstract: Message-passing graph neural networks (MPNNs) have emerged as a powerful
  paradigm for graph-based machine learning. Despite their effectiveness, MPNNs face
  challenges such as under-reaching and over-squashing, where limited receptive fields
  and structural bottlenecks hinder information flow in the graph. While graph transformers
  hold promise in addressing these issues, their scalability is limited due to quadratic
  complexity regarding the number of nodes, rendering them impractical for larger
  graphs. Here, we propose implicitly rewired message-passing neural networks (IPR-MPNNs),
  a novel approach that integrates implicit probabilistic graph rewiring into MPNNs.
  By introducing a small number of virtual nodes, i.e., adding additional nodes to
  a given graph and connecting them to existing nodes, in a differentiable, end-to-end
  manner, IPR-MPNNs enable long-distance message propagation, circumventing quadratic
  complexity. Theoretically, we demonstrate that IPR-MPNNs surpass the expressiveness
  of traditional MPNNs. Empirically, we validate our approach by showcasing its ability
  to mitigate under-reaching and over-squashing effects, achieving state-of-the-art
  performance across multiple graph datasets. Notably, IPR-MPNNs outperform graph
  transformers while maintaining significantly faster computational efficiency.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- IPR-MPNN
mrr: 0.1815
adjusted_mrr: 0.1815
mrr_dataset_count: 16
benchmark_categories:
- Classic
- Heterophilic Graphs
- LRGB
- TU Dortmund
- OGB
- Quantum Chemistry
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
- &id007
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
    value: 0.5554
    std: 0.0051
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
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
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.488
    std: 0.006
    paper_value: 0.488
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 56
    true_value: 0.488
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.488
    sort_std: 0.006
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.48
    std: 0.007
    paper_value: 0.48
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 64
    true_value: 0.48
    true_std: 0.007
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48
    sort_std: 0.007
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.764
    std: 0.056
    paper_value: 0.764
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 36
    true_value: 0.764
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 36
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.056
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.718
    std: 0.024
    paper_value: 0.718
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 46
    true_value: 0.7297
    true_std: 0.0221
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.011700000000000044
    value_note: global 0.7297 within std
    paper_rank: 52
    rank_delta: 6
    rank_delta_abs: 6
    rank_delta_direction: worse
    sort_value: 0.7297
    sort_std: 0.0221
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.683
    std: 0.017
    paper_value: 0.683
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Biao et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 56
    true_value: 0.7117
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.028699999999999948
    value_note: ''
    paper_rank: 74
    rank_delta: 18
    rank_delta_abs: 18
    rank_delta_direction: worse
    sort_value: 0.7117
    sort_std: 0.0127
    is_best: false
  - model: DiffWire
    model_key: diffwire
    model_plain: DiffWire
    value: 0.69
    std: 0.044
    paper_value: 0.69
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Arnaiz-Gonzalez et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 72
    true_value: 0.69
    true_std: 0.044
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.69
    sort_std: 0.044
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.608
    std: null
    paper_value: 0.608
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 98
    true_value: 0.6081
    true_std: null
    value_gap_source_arxiv: '2210.07606'
    value_gap_source_title: Revisiting Heterophily For Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 9.999999999998899e-05
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6081
    sort_std: null
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.582
    std: 0.005
    paper_value: 0.582
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 104
    true_value: 0.582
    true_std: 0.005
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 104
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.582
    sort_std: 0.005
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.546
    std: 0.004
    paper_value: 0.546
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Topping et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 112
    true_value: 0.546
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 112
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.546
    sort_std: 0.004
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.448
    std: 0.073
    paper_value: 0.448
    paper_std: 0.073
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 138
    true_value: 0.448
    true_std: 0.073
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 138
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.448
    sort_std: 0.073
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id013
  dataset: MUTAG
  rows:
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.984
    std: 0.024
    paper_value: 0.984
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: qian2023probabilistically
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 1
    true_value: 0.984
    true_std: 0.024
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    paper_value: 0.98
    paper_std: 0.034
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 3
    true_value: 0.98
    true_std: 0.034
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.98
    sort_std: 0.034
    is_best: true
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.944
    std: 0.037
    paper_value: 0.944
    paper_std: 0.037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bod+2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 4
    true_value: 0.944
    true_std: 0.037
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.944
    sort_std: 0.037
    is_best: true
  - model: CAN
    model_key: can
    model_plain: CAN
    value: 0.941
    std: 0.048
    paper_value: 0.941
    paper_std: 0.048
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: giusti2022cell
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 5
    true_value: 0.941
    true_std: 0.048
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.941
    sort_std: 0.048
    is_best: true
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.936
    std: 0.058
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
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
    global_rank: 6
    sort_value: 0.936
    sort_std: 0.058
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.922
    std: 0.075
    paper_value: 0.922
    paper_std: 0.075
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: botsas2020improving
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 7
    true_value: 0.922
    true_std: 0.075
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.922
    sort_std: 0.075
    is_best: true
  - model: Graph-JEPA
    model_key: graph-jepa
    model_plain: Graph-JEPA
    value: 0.9125
    std: 0.0575
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
    global_rank: 8
    sort_value: 0.9125
    sort_std: 0.0575
    is_best: true
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.906
    std: 0.087
    paper_value: 0.906
    paper_std: 0.087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 12
    true_value: 0.906
    true_std: 0.087
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.906
    sort_std: 0.087
    is_best: true
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.905
    std: 0.07
    paper_value: 0.905
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: mialon2021graphit
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.905
    true_std: 0.07
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.905
    sort_std: 0.07
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.904
    std: 0.057
    paper_value: 0.904
    paper_std: 0.057
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2011
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 17
    true_value: 0.904
    true_std: 0.057
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.904
    sort_std: 0.057
    is_best: true
  - model: DropGNN
    model_key: dropgnn
    model_plain: DropGNN
    value: 0.904
    std: 0.07
    paper_value: 0.904
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pap+2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 18
    true_value: 0.904
    true_std: 0.07
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.904
    sort_std: 0.07
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.894
    std: 0.056
    paper_value: 0.894
    paper_std: 0.056
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 28
    true_value: 0.894
    true_std: 0.056
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 28
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.056
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.894
    std: 0.016
    paper_value: 0.894
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: de2020natural
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 29
    true_value: 0.894
    true_std: 0.016
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.894
    sort_std: 0.016
    is_best: false
  - model: GAP(R)
    model_key: gap(r)
    model_plain: GAP(R)
    value: 0.869
    std: 0.04
    paper_value: 0.869
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arnaiz2022diffwire
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 50
    true_value: 0.869
    true_std: 0.04
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.869
    sort_std: 0.04
    is_best: false
  - model: GAP(N)
    model_key: gap(n)
    model_plain: GAP(N)
    value: 0.869
    std: 0.04
    paper_value: 0.869
    paper_std: 0.04
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arnaiz2022diffwire
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 51
    true_value: 0.869
    true_std: 0.04
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.869
    sort_std: 0.04
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.862
    std: 0.015
    paper_value: 0.862
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar2022-uz
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 56
    true_value: 0.862
    true_std: 0.015
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 56
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.862
    sort_std: 0.015
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.858
    std: 0.018
    paper_value: 0.858
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zha+2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 58
    true_value: 0.858
    true_std: 0.018
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.858
    sort_std: 0.018
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.839
    std: 0.065
    paper_value: 0.839
    paper_std: 0.065
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi2020-cd
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 71
    true_value: 0.839
    true_std: 0.065
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.065
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.839
    std: 0.13
    paper_value: 0.839
    paper_std: 0.13
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019c
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 70
    true_value: 0.839
    true_std: 0.13
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.13
    is_best: true
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.814
    std: 0.017
    paper_value: 0.814
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2009
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 90
    true_value: 0.814
    true_std: 0.017
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.017
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.76
    std: 0.027
    paper_value: 0.76
    paper_std: 0.027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Neu+2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 131
    true_value: 0.76
    true_std: 0.027
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 131
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.76
    sort_std: 0.027
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
  - model: Tango<sub>\1</sub>
    model_key: tango\textsubscript{gps}
    model_plain: Tango\1
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.887
    std: 0.006
    paper_value: 0.887
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 80
    true_value: 0.887
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.887
    sort_std: 0.006
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.799
    std: 0.002
    paper_value: 0.799
    paper_std: 0.002
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 90
    true_value: 0.799
    true_std: 0.002
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.799
    sort_std: 0.002
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id014
  dataset: NCI1
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.865
    std: 0.014
    paper_value: 0.865
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 1
    true_value: 0.865
    true_std: 0.014
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.865
    sort_std: 0.014
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.86
    std: 0.018
    paper_value: 0.86
    paper_std: 0.018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2011
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 2
    true_value: 0.86
    true_std: 0.018
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.846
    std: 0.012
    paper_value: 0.846
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: qian2023probabilistically
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 5
    true_value: 0.846
    true_std: 0.012
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.846
    sort_std: 0.012
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.846
    std: 0.012
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
    global_rank: 4
    sort_value: 0.846
    sort_std: 0.012
    is_best: true
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.845
    std: 0.024
    paper_value: 0.845
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bod+2021
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 6
    true_value: 0.845
    true_std: 0.024
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.845
    sort_std: 0.024
    is_best: true
  - model: CAN
    model_key: can
    model_plain: CAN
    value: 0.836
    std: 0.012
    paper_value: 0.836
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: giusti2022cell
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 7
    true_value: 0.836
    true_std: 0.012
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.836
    sort_std: 0.012
    is_best: false
  - model: nsqure~
    model_key: nsqure~
    model_plain: nsqure~
    value: 0.8352
    std: 0.0375
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
    global_rank: 8
    sort_value: 0.8352
    sort_std: 0.0375
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.835
    std: 0.023
    paper_value: 0.835
    paper_std: 0.023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: botsas2020improving
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 9
    true_value: 0.835
    true_std: 0.02
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.835
    sort_std: 0.02
    is_best: true
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.83
    std: 0.019
    paper_value: 0.83
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: de2020natural
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 12
    true_value: 0.83
    true_std: 0.019
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.83
    sort_std: 0.019
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.827
    std: 0.017
    paper_value: 0.827
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 18
    true_value: 0.827
    true_std: 0.017
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.017
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.825
    std: 0.005
    paper_value: 0.825
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Neu+2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 20
    true_value: 0.825
    true_std: 0.005
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.825
    sort_std: 0.005
    is_best: false
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.822
    std: 0.014
    paper_value: 0.822
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 24
    true_value: 0.822
    true_std: 0.014
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.822
    sort_std: 0.014
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.814
    std: 0.022
    paper_value: 0.814
    paper_std: 0.022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: mialon2021graphit
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 26
    true_value: 0.814
    true_std: 0.022
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.814
    sort_std: 0.022
    is_best: false
  - model: DropGNN
    model_key: dropgnn
    model_plain: DropGNN
    value: 0.808
    std: 0.026
    paper_value: 0.808
    paper_std: 0.026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pap+2021
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 27
    true_value: 0.808
    true_std: 0.026
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.808
    sort_std: 0.026
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.8
    std: 0.019
    paper_value: 0.8
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi2020-cd
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 33
    true_value: 0.8
    true_std: 0.019
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8
    sort_std: 0.019
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.744
    std: 0.005
    paper_value: 0.744
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zha+2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 57
    true_value: 0.764
    true_std: 0.017
    value_gap_source_arxiv: '2310.01267'
    value_gap_source_title: Cooperative Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.020000000000000018
    value_note: ''
    paper_rank: 65
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.764
    sort_std: 0.017
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.728
    std: 0.015
    paper_value: 0.728
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019c
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 71
    true_value: 0.728
    true_std: 0.015
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.015
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.711
    std: 0.006
    paper_value: 0.711
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar2022-uz
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 74
    true_value: 0.711
    true_std: 0.006
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.711
    sort_std: 0.006
    is_best: false
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.624
    std: 0.003
    paper_value: 0.624
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2009
    variant_inference_reason: 'dataset: fuzzy match to nci1 (score=90)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 83
    true_value: 0.624
    true_std: 0.003
    value_gap_source_arxiv: '2409.19117'
    value_gap_source_title: 'Range-aware Positional Encoding via High-order Pretraining:
      Theory and Practice'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 83
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.624
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id011
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
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    paper_rank: 31
    rank_delta: 24
    rank_delta_abs: 24
    rank_delta_direction: worse
    sort_value: 0.4526
    sort_std: 0.0006
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.367
    std: 0.0082
    paper_value: 0.367
    paper_std: 0.0082
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 9
    true_value: 0.367
    true_std: 0.0082
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 10
    true_value: 0.3637
    true_std: 0.002
    value_gap_source_arxiv: '2401.01233'
    value_gap_source_title: 'GEN: A Practical Alternative to Graph Transformers for
      Long-Range Graph Modeling'
    value_gap_source_is_current_paper: false
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
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.3509
    std: 0.0006
    paper_value: 0.3509
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 17
    true_value: 0.3509
    true_std: 0.0006
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3509
    sort_std: 0.0006
    is_best: false
  metric: MRR
  higher_is_better: true
- &id012
  dataset: PROTEINS
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.854
    std: 0.044
    paper_value: 0.854
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 1
    true_value: 0.854
    true_std: 0.044
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.854
    sort_std: 0.044
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.807
    std: 0.039
    paper_value: 0.807
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: qian2023probabilistically
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 2
    true_value: 0.807
    true_std: 0.039
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.805
    std: 0.039
    paper_value: 0.805
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bod+2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 4
    true_value: 0.805
    true_std: 0.039
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.805
    sort_std: 0.039
    is_best: true
  - model: GIN + HOPE-WavePE
    model_key: gin + hope-wavepe
    model_plain: GIN + HOPE-WavePE
    value: 0.795
    std: 0.0481
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
    global_rank: 5
    sort_value: 0.795
    sort_std: 0.0481
    is_best: true
  - model: CoCN expanded
    model_key: cocn expanded
    model_plain: CoCN expanded
    value: 0.7948
    std: 0.0051
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
    global_rank: 6
    sort_value: 0.7948
    sort_std: 0.0051
    is_best: false
  - model: CAN
    model_key: can
    model_plain: CAN
    value: 0.782
    std: 0.02
    paper_value: 0.782
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: giusti2022cell
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 11
    true_value: 0.782
    true_std: 0.02
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.782
    sort_std: 0.02
    is_best: false
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.772
    std: 0.047
    paper_value: 0.772
    paper_std: 0.047
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 15
    true_value: 0.772
    true_std: 0.047
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.772
    sort_std: 0.047
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.766
    std: 0.05
    paper_value: 0.766
    paper_std: 0.05
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: botsas2020improving
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 23
    true_value: 0.766
    true_std: 0.05
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 23
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.05
    is_best: true
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.766
    std: 0.055
    paper_value: 0.766
    paper_std: 0.055
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019c
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 22
    true_value: 0.766
    true_std: 0.055
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 22
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.766
    sort_std: 0.055
    is_best: true
  - model: DropGNN
    model_key: dropgnn
    model_plain: DropGNN
    value: 0.763
    std: 0.061
    paper_value: 0.763
    paper_std: 0.061
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pap+2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 29
    true_value: 0.763
    true_std: 0.061
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.763
    sort_std: 0.061
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.762
    std: 0.028
    paper_value: 0.762
    paper_std: 0.028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 32
    true_value: 0.762
    true_std: 0.028
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.028
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.762
    std: 0.044
    paper_value: 0.762
    paper_std: 0.044
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: mialon2021graphit
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 33
    true_value: 0.762
    true_std: 0.044
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.044
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.755
    std: 0.009
    paper_value: 0.755
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zha+2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 50
    true_value: 0.755
    true_std: 0.009
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.755
    sort_std: 0.009
    is_best: false
  - model: GAP(N)
    model_key: gap(n)
    model_plain: GAP(N)
    value: 0.753
    std: 0.021
    paper_value: 0.753
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arnaiz2022diffwire
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 53
    true_value: 0.753
    true_std: 0.021
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.021
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.751
    std: 0.008
    paper_value: 0.751
    paper_std: 0.008
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar2022-uz
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 64
    true_value: 0.751
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.751
    sort_std: 0.008
    is_best: false
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.75
    std: 0.031
    paper_value: 0.75
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2011
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 68
    true_value: 0.75
    true_std: 0.031
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 68
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.031
    is_best: false
  - model: GAP(R)
    model_key: gap(r)
    model_plain: GAP(R)
    value: 0.75
    std: 0.03
    paper_value: 0.75
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arnaiz2022diffwire
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 69
    true_value: 0.75
    true_std: 0.03
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.75
    sort_std: 0.03
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.737
    std: 0.007
    paper_value: 0.737
    paper_std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Neu+2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 102
    true_value: 0.737
    true_std: 0.007
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.007
    is_best: false
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.717
    std: 0.01
    paper_value: 0.717
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: de2020natural
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 153
    true_value: 0.717
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 153
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.717
    sort_std: 0.01
    is_best: false
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.714
    std: 0.003
    paper_value: 0.714
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2009
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 160
    true_value: 0.714
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 160
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.714
    sort_std: 0.003
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.701
    std: 0.032
    paper_value: 0.701
    paper_std: 0.032
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi2020-cd
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 178
    true_value: 0.701
    true_std: 0.032
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 178
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.701
    sort_std: 0.032
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id015
  dataset: PTC_MR
  rows:
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.758
    std: 0.053
    paper_value: 0.758
    paper_std: 0.053
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 1
    true_value: 0.758
    true_std: 0.053
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.758
    sort_std: 0.053
    is_best: true
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.743
    std: 0.039
    paper_value: 0.743
    paper_std: 0.039
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: qian2023probabilistically
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 3
    true_value: 0.743
    true_std: 0.039
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.743
    sort_std: 0.039
    is_best: true
  - model: PR-MPNN (10-fold CV)
    model_key: pr-mpnn (10-fold cv)
    model_plain: PR-MPNN (10-fold CV)
    value: 0.743
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
    global_rank: 2
    sort_value: 0.743
    sort_std: 0.039
    is_best: true
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.732
    std: 0.064
    paper_value: 0.732
    paper_std: 0.064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bod+2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 4
    true_value: 0.732
    true_std: 0.064
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.732
    sort_std: 0.064
    is_best: true
  - model: CAN
    model_key: can
    model_plain: CAN
    value: 0.728
    std: 0.083
    paper_value: 0.728
    paper_std: 0.083
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: giusti2022cell
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 5
    true_value: 0.728
    true_std: 0.083
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.728
    sort_std: 0.083
    is_best: true
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.682
    std: 0.072
    paper_value: 0.682
    paper_std: 0.072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: botsas2020improving
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 6
    true_value: 0.682
    true_std: 0.072
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.682
    sort_std: 0.072
    is_best: true
  - model: Natural GN
    model_key: natural gn
    model_plain: Natural GN
    value: 0.668
    std: 0.017
    paper_value: 0.668
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: de2020natural
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 7
    true_value: 0.668
    true_std: 0.017
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.668
    sort_std: 0.017
    is_best: false
  - model: DropGNN
    model_key: dropgnn
    model_plain: DropGNN
    value: 0.663
    std: 0.086
    paper_value: 0.663
    paper_std: 0.086
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pap+2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 8
    true_value: 0.663
    true_std: 0.086
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.663
    sort_std: 0.086
    is_best: true
  - model: PPGNs
    model_key: ppgns
    model_plain: PPGNs
    value: 0.662
    std: 0.066
    paper_value: 0.662
    paper_std: 0.066
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 9
    true_value: 0.662
    true_std: 0.066
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.662
    sort_std: 0.066
    is_best: true
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.646
    std: 0.07
    paper_value: 0.646
    paper_std: 0.07
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 10
    true_value: 0.646
    true_std: 0.07
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.646
    sort_std: 0.07
    is_best: true
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.62
    std: 0.094
    paper_value: 0.62
    paper_std: 0.094
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: mialon2021graphit
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 11
    true_value: 0.62
    true_std: 0.094
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.62
    sort_std: 0.094
    is_best: true
  - model: Kern. WL
    model_key: kern. wl
    model_plain: Kern. WL
    value: 0.599
    std: 0.043
    paper_value: 0.599
    paper_std: 0.043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2011
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 12
    true_value: 0.599
    true_std: 0.043
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.599
    sort_std: 0.043
    is_best: false
  - model: PK
    model_key: pk
    model_plain: PK
    value: 0.595
    std: 0.024
    paper_value: 0.595
    paper_std: 0.024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Neu+2016
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.595
    true_std: 0.024
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.595
    sort_std: 0.024
    is_best: false
  - model: PR-MPNN (train/val/test)
    model_key: pr-mpnn (train/val/test)
    model_plain: PR-MPNN (train/val/test)
    value: 0.589
    std: 0.05
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
    global_rank: 14
    sort_value: 0.589
    sort_std: 0.05
    is_best: false
  - model: DGCNN
    model_key: dgcnn
    model_plain: DGCNN
    value: 0.586
    std: 0.025
    paper_value: 0.586
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zha+2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 15
    true_value: 0.586
    true_std: 0.025
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.586
    sort_std: 0.025
    is_best: false
  - model: FOSR
    model_key: fosr
    model_plain: FOSR
    value: 0.585
    std: 0.017
    paper_value: 0.585
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Karhadkar2022-uz
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 17
    true_value: 0.585
    true_std: 0.017
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 17
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.585
    sort_std: 0.017
    is_best: false
  - model: IGN
    model_key: ign
    model_plain: IGN
    value: 0.585
    std: 0.069
    paper_value: 0.585
    paper_std: 0.069
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Mar+2019c
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 16
    true_value: 0.585
    true_std: 0.069
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.585
    sort_std: 0.069
    is_best: false
  - model: GT
    model_key: gt
    model_plain: GT
    value: 0.584
    std: 0.082
    paper_value: 0.584
    paper_std: 0.082
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi2020-cd
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 18
    true_value: 0.584
    true_std: 0.082
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.584
    sort_std: 0.082
    is_best: false
  - model: GK (k=3)
    model_key: gk (k=3)
    model_plain: GK (k=3)
    value: 0.557
    std: 0.005
    paper_value: 0.557
    paper_std: 0.005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: She+2009
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 19
    true_value: 0.557
    true_std: 0.005
    value_gap_source_arxiv: '2310.02156'
    value_gap_source_title: Probabilistically Rewired Message-Passing Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.557
    sort_std: 0.005
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
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
    date: '2025-01-29'
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
    date: '2025-01-29'
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
    date: '2025-01-29'
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7318
    sort_std: null
    is_best: false
  - model: S2GCN+PE
    model_key: s2gcn+pe
    model_plain: S2GCN+PE
    value: 0.7311
    std: 0.0066
    paper_value: 0.7311
    paper_std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Geisler et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 4
    true_value: 0.7311
    true_std: 0.0066
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7311
    sort_std: 0.0066
    is_best: false
  - model: S2GCN
    model_key: s2gcn
    model_plain: S2GCN
    value: 0.7275
    std: 0.0066
    paper_value: 0.7275
    paper_std: 0.0066
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Geisler et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 8
    true_value: 0.7275
    true_std: 0.0066
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7275
    sort_std: 0.0066
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
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    paper_rank: 86
    rank_delta: 77
    rank_delta_abs: 77
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
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
  - model: 2VN2S
    model_key: 2vn2s
    model_plain: 2VN2S
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
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.721
    true_std: 0.0039
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 13
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.721
    sort_std: 0.0039
    is_best: false
  - model: NBA
    model_key: nba
    model_plain: NBA
    value: 0.7207
    std: 0.0028
    paper_value: 0.7207
    paper_std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Park et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 14
    true_value: 0.7207
    true_std: 0.0028
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7207
    sort_std: 0.0028
    is_best: false
  - model: AMP
    model_key: amp
    model_plain: AMP
    value: 0.7163
    std: 0.0058
    paper_value: 0.7163
    paper_std: 0.0058
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Errica et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 19
    true_value: 0.7163
    true_std: 0.0058
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 19
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7163
    sort_std: 0.0058
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
    source_ref: Gutteridge et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 21
    true_value: 0.715
    true_std: 0.0044
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.715
    sort_std: 0.0044
    is_best: false
  - model: 2VN1S
    model_key: 2vn1s
    model_plain: 2VN1S
    value: 0.7146
    std: 0.0055
    paper_value: 0.7146
    paper_std: 0.0055
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 25
    true_value: 0.7146
    true_std: 0.0055
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7146
    sort_std: 0.0055
    is_best: false
  - model: 2VN4S
    model_key: 2vn4s
    model_plain: 2VN4S
    value: 0.7145
    std: 0.002
    paper_value: 0.7145
    paper_std: 0.002
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 26
    true_value: 0.7145
    true_std: 0.002
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7145
    sort_std: 0.002
    is_best: false
  - model: 1VN - FC
    model_key: 1vn - fc
    model_plain: 1VN - FC
    value: 0.7039
    std: 0.0046
    paper_value: 0.7039
    paper_std: 0.0046
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 43
    true_value: 0.7039
    true_std: 0.0046
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 43
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7039
    sort_std: 0.0046
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
    source_ref: Ma et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 52
    true_value: 0.6988
    true_std: 0.0082
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 52
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6988
    sort_std: 0.0082
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.6942
    std: 0.0075
    paper_value: 0.6942
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 60
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0027999999999999137
    value_note: global 0.6970 within std
    paper_rank: 73
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.697
    sort_std: 0.008
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
    table_ref: Table 1
    source_ref: He et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 62
    true_value: 0.697
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.697
    sort_std: 0.008
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.6825
    std: 0.0086
    paper_value: 0.6825
    paper_std: 0.0086
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 97
    true_value: 0.6825
    true_std: 0.0086
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6825
    sort_std: 0.0086
    is_best: false
  - model: GatedGCN+PE+VN_G
    model_key: gatedgcn+pe+vn_g
    model_plain: GatedGCN+PE+VN_G
    value: 0.6822
    std: 0.0052
    paper_value: 0.6822
    paper_std: 0.0052
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Southern et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 98
    true_value: 0.6822
    true_std: 0.0052
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6822
    sort_std: 0.0052
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
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 141
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 141
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
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 152
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 166
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
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
    source_ref: Shi et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 176
    true_value: 0.6527
    true_std: 0.0043
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 176
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6527
    sort_std: 0.0043
    is_best: false
  metric: AP
  higher_is_better: true
- &id010
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
    source_ref: Kipf & Welling 2017
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
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
    paper_rank: 53
    rank_delta: 50
    rank_delta_abs: 50
    rank_delta_direction: worse
    sort_value: 0.2421
    sort_std: 0.0016
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.2422
    std: 0.0007
    paper_value: 0.2422
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 5
    true_value: 0.2422
    true_std: 0.0007
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2422
    sort_std: 0.0007
    is_best: false
  - model: 2VN2S
    model_key: 2vn2s
    model_plain: 2VN2S
    value: 0.2422
    std: 0.0007
    paper_value: 0.2422
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 6
    true_value: 0.2422
    true_std: 0.0007
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
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
  - model: AMP
    model_key: amp
    model_plain: AMP
    value: 0.2431
    std: 0.0004
    paper_value: 0.2431
    paper_std: 0.0004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Errica et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 15
    true_value: 0.2431
    true_std: 0.0004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 15
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2431
    sort_std: 0.0004
    is_best: false
  - model: 1VN - FC
    model_key: 1vn - fc
    model_plain: 1VN - FC
    value: 0.2435
    std: 0.0007
    paper_value: 0.2435
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 20
    true_value: 0.2435
    true_std: 0.0007
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2435
    sort_std: 0.0007
    is_best: false
  - model: S2GCN+PE
    model_key: s2gcn+pe
    model_plain: S2GCN+PE
    value: 0.2447
    std: 0.0007
    paper_value: 0.2447
    paper_std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Geisler et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 29
    true_value: 0.2447
    true_std: 0.0032
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2447
    sort_std: 0.0032
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
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
    table_ref: Table 1
    source_ref: He et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 30
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
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
    source_ref: He et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 31
    true_value: 0.2449
    true_std: 0.0016
    value_gap_source_arxiv: '2310.07430'
    value_gap_source_title: Non-backtracking Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.002599999999999991
    value_note: ''
    paper_rank: 82
    rank_delta: 51
    rank_delta_abs: 51
    rank_delta_direction: worse
    sort_value: 0.2449
    sort_std: 0.0016
    is_best: false
  - model: GatedGCN+PE+VN_G
    model_key: gatedgcn+pe+vn_g
    model_plain: GatedGCN+PE+VN_G
    value: 0.2458
    std: 0.0006
    paper_value: 0.2458
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Southern et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 48
    true_value: 0.2458
    true_std: 0.0006
    value_gap_source_arxiv: '2405.13526'
    value_gap_source_title: 'Understanding Virtual Nodes: Oversquashing and Node Heterogeneity'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 48
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2458
    sort_std: 0.0006
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
    source_ref: Ma et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 55
    true_value: 0.246
    true_std: 0.0012
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 55
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0012
    is_best: false
  - model: S2GCN
    model_key: s2gcn
    model_plain: S2GCN
    value: 0.2467
    std: 0.0019
    paper_value: 0.2467
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Geisler et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 70
    true_value: 0.2467
    true_std: 0.0019
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2467
    sort_std: 0.0019
    is_best: false
  - model: NBA
    model_key: nba
    model_plain: NBA
    value: 0.2472
    std: 0.0008
    paper_value: 0.2472
    paper_std: 0.0008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Park et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 75
    true_value: 0.2472
    true_std: 0.0008
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2472
    sort_std: 0.0008
    is_best: false
  - model: 2VN1S
    model_key: 2vn1s
    model_plain: 2VN1S
    value: 0.2472
    std: 0.0014
    paper_value: 0.2472
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 77
    true_value: 0.2472
    true_std: 0.0014
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
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
    sort_std: 0.0014
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
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 78
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2604.03815'
    value_gap_source_title: k-Maximum Inner Product Attention for Graph Transformers
      and the Expressive Power of GraphGPS
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.2477
    std: 0.0005
    paper_value: 0.2477
    paper_std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 90
    true_value: 0.2477
    true_std: 0.0005
    value_gap_source_arxiv: '2312.16560'
    value_gap_source_title: Algorithmic Graph Tasks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 90
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0005
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
    table_ref: Table 1
    source_ref: Shi et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 101
    true_value: 0.2481
    true_std: 0.0007
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 101
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2481
    sort_std: 0.0007
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.2509
    std: 0.0014
    paper_value: 0.2509
    paper_std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 132
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 145
    rank_delta: 13
    rank_delta_abs: 13
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
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
    source_ref: Gutteridge et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 171
    true_value: 0.2536
    true_std: 0.0015
    value_gap_source_arxiv: '2605.06462'
    value_gap_source_title: Invariant-Based Diagnostics for Graph Benchmarks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 171
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2536
    sort_std: 0.0015
    is_best: false
  metric: MAE
  higher_is_better: false
- &id017
  dataset: QM9
  rows:
  - model: Mace
    model_key: mace
    model_plain: Mace
    value: 0.02
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.02
    sort_std: null
    is_best: true
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.023
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    arxiv_id: '2405.02795'
    title: Graph as Point Set
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.02578744427174226
    std: 0.000867405321348238
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
    global_rank: 3
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 2.64
    std: 0.01
    paper_value: 2.64
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 18
    true_value: 0.0969
    true_std: 0.0017
    value_gap_source_arxiv: '2406.18380'
    value_gap_source_title: 'KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 2.5431
    value_note: ''
    paper_rank: 61
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.0969
    sort_std: 0.0017
    is_best: false
  - model: Drew-GIN
    model_key: drew-gin
    model_plain: Drew-GIN
    value: 1.93
    std: 0.06
    paper_value: 1.93
    paper_std: 0.06
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gutteridge et al. 2023
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 57
    true_value: 1.93
    true_std: 0.06
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.93
    sort_std: 0.06
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 1.99
    std: 0.02
    paper_value: 1.99
    paper_std: 0.02
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al. 2023
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 58
    true_value: 1.99
    true_std: 0.02
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.99
    sort_std: 0.02
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 2.01
    std: 0.01
    paper_value: 2.01
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 59
    true_value: 2.01
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.01
    sort_std: 0.01
    is_best: false
  - model: SPN
    model_key: spn
    model_plain: SPN
    value: 2.32
    std: 0.28
    paper_value: 2.32
    paper_std: 0.28
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Abboud et al. 2022
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 60
    true_value: 2.32
    true_std: 0.28
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 60
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.32
    sort_std: 0.28
    is_best: false
  - model: R-GIN+FA
    model_key: r-gin+fa
    model_plain: R-GIN+FA
    value: 2.54
    std: 0.09
    paper_value: 2.54
    paper_std: 0.09
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Schlichtkrull et al. 2019
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 61
    true_value: 2.54
    true_std: 0.09
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 61
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 2.54
    sort_std: 0.09
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.839
    std: 0.006
    paper_value: 0.839
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 59
    true_value: 0.839
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.839
    sort_std: 0.006
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.476
    std: 0.006
    paper_value: 0.476
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 97
    true_value: 0.476
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: 0.006
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.808
    std: 0.052
    paper_value: 0.808
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 59
    true_value: 0.808
    true_std: 0.052
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 59
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.808
    sort_std: 0.052
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.767
    std: 0.017
    paper_value: 0.767
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: graphormer
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 73
    true_value: 0.7748
    true_std: 0.0127
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.007800000000000029
    value_note: global 0.7748 within std
    paper_rank: 80
    rank_delta: 7
    rank_delta_abs: 7
    rank_delta_direction: worse
    sort_value: 0.7748
    sort_std: 0.0127
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.773
    std: 0.013
    paper_value: 0.773
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek2022-uc
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 74
    true_value: 0.773
    true_std: 0.013
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.773
    sort_std: 0.013
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.676
    std: null
    paper_value: 0.676
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: webkb
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 115
    true_value: 0.676
    true_std: null
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.676
    sort_std: null
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.65
    std: 0.068
    paper_value: 0.65
    paper_std: 0.068
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: xu2018how
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 126
    true_value: 0.65
    true_std: 0.068
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 126
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.65
    sort_std: 0.068
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.644
    std: 0.004
    paper_value: 0.644
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Topping2021-iy
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 127
    true_value: 0.644
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 127
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.644
    sort_std: 0.004
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.62
    std: 0.003
    paper_value: 0.62
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kli+2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 136
    true_value: 0.62
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.62
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: Tolokers
  rows:
  - model: GRAMA<sub>\1</sub>
    model_key: grama$_{gcn}$
    model_plain: GRAMA\1
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.82
    std: 0.008
    paper_value: 0.82
    paper_std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 62
    true_value: 0.82
    true_std: 0.008
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.82
    sort_std: 0.008
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.807
    std: 0.006
    paper_value: 0.807
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 64
    true_value: 0.807
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 64
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.807
    sort_std: 0.006
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
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
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.804
    std: 0.052
    paper_value: 0.804
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
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 38
    true_value: 0.804
    true_std: 0.052
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.804
    sort_std: 0.052
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.798
    std: 0.09
    paper_value: 0.798
    paper_std: 0.09
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 45
    true_value: 0.798
    true_std: 0.09
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 45
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.798
    sort_std: 0.09
    is_best: false
  - model: DiffWire
    model_key: diffwire
    model_plain: DiffWire
    value: 0.791
    std: 0.021
    paper_value: 0.791
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Arnaiz-Gonzalez et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 51
    true_value: 0.791
    true_std: 0.021
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 51
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.791
    sort_std: 0.021
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.77
    std: 0.019
    paper_value: 0.77
    paper_std: 0.019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Biao et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 69
    true_value: 0.77
    true_std: 0.019
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.77
    sort_std: 0.019
    is_best: false
  - model: Geom-GCN
    model_key: geom-gcn
    model_plain: Geom-GCN
    value: 0.641
    std: null
    paper_value: 0.641
    paper_std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pei et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 110
    true_value: 0.6451
    true_std: 0.0366
    value_gap_source_arxiv: '2507.00647'
    value_gap_source_title: Cooperative Sheaf Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0040999999999999925
    value_note: global 0.6451 within std
    paper_rank: 110
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6451
    sort_std: 0.0366
    is_best: false
  - model: SDRF
    model_key: sdrf
    model_plain: SDRF
    value: 0.555
    std: 0.003
    paper_value: 0.555
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Topping et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 125
    true_value: 0.555
    true_std: 0.003
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.555
    sort_std: 0.003
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.517
    std: 0.054
    paper_value: 0.517
    paper_std: 0.054
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 135
    true_value: 0.517
    true_std: 0.054
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 135
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.517
    sort_std: 0.054
    is_best: false
  - model: + DIGL
    model_key: + digl
    model_plain: + DIGL
    value: 0.495
    std: 0.003
    paper_value: 0.495
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Klicpera et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 134
    true_value: 0.517
    true_std: 0.013
    value_gap_source_arxiv: '2406.03671'
    value_gap_source_title: 'PANDA: Expanded Width-Aware Message Passing Beyond Rewiring'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.02200000000000002
    value_note: ''
    paper_rank: 135
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.517
    sort_std: 0.013
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
    date: '2024-05-05'
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
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
    table_ref: Table 1 (in figure caption)
    source_ref: Rampasek et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 104
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
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
    source_ref: Rampasek et al. 2022
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 13
    true_value: 0.023842
    true_std: 0.0069779309254248125
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046158000000000005
    value_note: ''
    paper_rank: 104
    rank_delta: 91
    rank_delta_abs: 91
    rank_delta_direction: worse
    sort_value: 0.023842
    sort_std: 0.0069779309254248125
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.085
    std: 0.005
    paper_value: 0.085
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (in figure caption)
    source_ref: He et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 34
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 150
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.085
    std: 0.005
    paper_value: 0.085
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He et al. 2022
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 34
    true_value: 0.035
    true_std: 0.005
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 150
    rank_delta: 116
    rank_delta_abs: 116
    rank_delta_direction: worse
    sort_value: 0.035
    sort_std: 0.005
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.067
    std: 0.001
    paper_value: 0.067
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (in figure caption)
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 80
    true_value: 0.067
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.067
    sort_std: 0.001
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.067
    std: 0.001
    paper_value: 0.067
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 80
    true_value: 0.067
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.067
    sort_std: 0.001
    is_best: false
  - model: 2VN2S
    model_key: 2vn2s
    model_plain: 2VN2S
    value: 0.067
    std: 0.001
    paper_value: 0.067
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (ablation)
    source_ref: this paper
    variant_inference_reason: 'zinc: default subset fallback'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 85
    true_value: 0.067
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 85
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.067
    sort_std: 0.001
    is_best: false
  - model: 2VN1S
    model_key: 2vn1s
    model_plain: 2VN1S
    value: 0.072
    std: 0.004
    paper_value: 0.072
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (ablation)
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 113
    true_value: 0.072
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 113
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.072
    sort_std: 0.004
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
    table_ref: Table 1 (in figure caption)
    source_ref: He et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 115
    true_value: 0.073
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.001
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
    source_ref: He et al. 2022
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 115
    true_value: 0.073
    true_std: 0.001
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.073
    sort_std: 0.001
    is_best: false
  - model: 1VN - FC
    model_key: 1vn - fc
    model_plain: 1VN - FC
    value: 0.074
    std: 0.002
    paper_value: 0.074
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (ablation)
    source_ref: this paper
    variant_inference_reason: 'zinc: mae fallback >= 0.07'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 123
    true_value: 0.074
    true_std: 0.002
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 123
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.074
    sort_std: 0.002
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.084
    std: 0.002
    paper_value: 0.084
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (in figure caption)
    source_ref: Qian et al. 2023
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 147
    true_value: 0.084
    true_std: 0.002
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.084
    sort_std: 0.002
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.084
    std: 0.002
    paper_value: 0.084
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al. 2023
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 147
    true_value: 0.084
    true_std: 0.002
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 147
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.084
    sort_std: 0.002
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.101
    std: 0.004
    paper_value: 0.101
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (in figure caption)
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 175
    true_value: 0.101
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.004
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.101
    std: 0.004
    paper_value: 0.101
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2018
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 175
    true_value: 0.101
    true_std: 0.004
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 175
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.004
    is_best: false
  - model: K-SG SAT
    model_key: k-sg sat
    model_plain: K-SG SAT
    value: 0.115
    std: 0.005
    paper_value: 0.115
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (in figure caption)
    source_ref: Chen et al. 2022
    variant_inference_reason: 'dataset: fuzzy match to zinc 12k (score=95)'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 188
    true_value: 0.115
    true_std: 0.005
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.115
    sort_std: 0.005
    is_best: false
  - model: K-SG SAT
    model_key: k-sg sat
    model_plain: K-SG SAT
    value: 0.115
    std: 0.005
    paper_value: 0.115
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2022
    variant_inference_reason: ''
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 188
    true_value: 0.115
    true_std: 0.005
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 188
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.115
    sort_std: 0.005
    is_best: false
  metric: MAE
  higher_is_better: false
- &id016
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
  - model: Graph MLP-Mixer
    model_key: graph mlp-mixer
    model_plain: Graph MLP-Mixer
    value: 0.799
    std: 0.01
    paper_value: 0.799
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 33
    true_value: 0.7997
    true_std: 0.0102
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0006999999999999229
    value_note: global 0.7997 within std
    paper_rank: 36
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.7997
    sort_std: 0.0102
    is_best: false
  - model: PR-MPNN
    model_key: pr-mpnn
    model_plain: PR-MPNN
    value: 0.795
    std: 0.009
    paper_value: 0.795
    paper_std: 0.009
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 49
    true_value: 0.795
    true_std: 0.009
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.795
    sort_std: 0.009
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
    value: 0.788
    std: 0.01
    paper_value: 0.788
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 70
    true_value: 0.788
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.01
    is_best: false
  - model: IPR-MPNN
    model_key: ipr-mpnn
    model_plain: IPR-MPNN
    value: 0.788
    std: 0.006
    paper_value: 0.788
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 71
    true_value: 0.788
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 71
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.006
    is_best: false
  - model: 2VN2S
    model_key: 2vn2s
    model_plain: 2VN2S
    value: 0.788
    std: 0.006
    paper_value: 0.788
    paper_std: 0.006
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Ablation)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 75
    true_value: 0.788
    true_std: 0.006
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 75
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.788
    sort_std: 0.006
    is_best: false
  - model: Graph ViT
    model_key: graph vit
    model_plain: Graph ViT
    value: 0.779
    std: 0.015
    paper_value: 0.779
    paper_std: 0.015
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 108
    true_value: 0.7792
    true_std: 0.0149
    value_gap_source_arxiv: '2312.04234'
    value_gap_source_title: Graph Convolutions Enrich the Self-Attention in Transformers!
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.00019999999999997797
    value_note: global 0.7792 within std
    paper_rank: 109
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.7792
    sort_std: 0.0149
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.764
    std: 0.01
    paper_value: 0.764
    paper_std: 0.01
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 142
    true_value: 0.764
    true_std: 0.01
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 142
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.764
    sort_std: 0.01
    is_best: false
  - model: 2VN1S
    model_key: 2vn1s
    model_plain: 2VN1S
    value: 0.762
    std: 0.014
    paper_value: 0.762
    paper_std: 0.014
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Ablation)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 148
    true_value: 0.762
    true_std: 0.014
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 148
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.762
    sort_std: 0.014
    is_best: false
  - model: 1VN - FC
    model_key: 1vn - fc
    model_plain: 1VN - FC
    value: 0.753
    std: 0.011
    paper_value: 0.753
    paper_std: 0.011
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2 (Ablation)
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 163
    true_value: 0.753
    true_std: 0.011
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 163
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.753
    sort_std: 0.011
    is_best: false
  - model: K-SG SAT
    model_key: k-sg sat
    model_plain: K-SG SAT
    value: 0.625
    std: 0.039
    paper_value: 0.625
    paper_std: 0.039
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    global_rank: 204
    true_value: 0.625
    true_std: 0.039
    value_gap_source_arxiv: '2405.17311'
    value_gap_source_title: Probabilistic Graph Rewiring via Virtual Nodes
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 204
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.625
    sort_std: 0.039
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: Heterophilic Graphs
  datasets:
  - *id002
  - *id003
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
- benchmark: LRGB
  datasets:
  - *id009
  - *id010
  - *id011
- benchmark: TU Dortmund
  datasets:
  - *id012
  - *id013
  - *id014
  - *id015
- benchmark: OGB
  datasets:
  - *id016
- benchmark: Quantum Chemistry
  datasets:
  - *id017
single_proposed_model: IPR-MPNN
main_figure: /figures/2405.17311/main_figure.png
---

