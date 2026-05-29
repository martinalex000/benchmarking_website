---
title: ': Mitigating by Increasing Storage Capacity'
arxiv_id: '2510.08450'
source_url: ''
authors: []
published_date: Oct 2025
published_date_iso: 2025-10
abstract: Graph Neural Networks (GNNs) leverage the graph structure to transmit information
  between nodes, typically through the message-passing mechanism. While these models
  have found a wide variety of applications, they are known to suffer from, where
  information from a large receptive field of node representations is collapsed into
  a single fixed sized vector, resulting in an information bottleneck. In this paper,
  we re-examine the phenomenon through the lens of model storage and retrieval capacity,
  which we define as the amount of information that can be stored in a node's representation
  for later use. We study some of the limitations of existing tasks used to measure
  and introduce a new synthetic task to demonstrate that an information bottleneck
  can saturate this capacity. Furthermore, we adapt ideas from the sequence modeling
  literature on associative memories, fast weight programmers, and the xLSTM model
  to develop a novel GNN architecture with improved capacity. We demonstrate strong
  performance of this architecture both on our capacity synthetic task, as well as
  a range of real-world graph benchmarks.
codebase_url: https://github.com/HughBlayney/gLSTM
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- gLSTM
mrr: 0.3333
adjusted_mrr: 0.1111
mrr_dataset_count: 1
benchmark_categories:
- TU Dortmund
- LRGB
- Algorithmic Graph Tasks
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: gLSTM
    model_key: glstm
    model_plain: gLSTM
    value: 0.00019
    std: 9.0e-05
    paper_value: 0.00019
    paper_std: 9.0e-05
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: null
    sort_value: 0.00019
    sort_std: 9.0e-05
    is_best: true
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 0.00028
    std: 7.0e-05
    paper_value: 0.00028
    paper_std: 7.0e-05
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gravina 2022
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: null
    sort_value: 0.00028
    sort_std: 7.0e-05
    is_best: true
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.0015
    std: 0.00011
    paper_value: 0.0015
    paper_std: 0.00011
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 94
    sort_value: 0.0015
    sort_std: 0.00011
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.0043
    std: 0.0025
    paper_value: 0.0043
    paper_std: 0.0025
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 91
    sort_value: 0.0043
    sort_std: 0.0025
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.0055
    std: 0.0005
    paper_value: 0.0055
    paper_std: 0.0005
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 25
    sort_value: 0.0055
    sort_std: 0.0005
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.0067
    std: 0.0012
    paper_value: 0.0067
    paper_std: 0.0012
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 130
    sort_value: 0.0067
    sort_std: 0.0012
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.0067
    std: 0.0011
    paper_value: 0.0067
    paper_std: 0.0011
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: null
    sort_value: 0.0067
    sort_std: 0.0011
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.0097
    std: 0.0016
    paper_value: 0.0097
    paper_std: 0.0016
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 119
    sort_value: 0.0097
    sort_std: 0.0016
    is_best: false
  - model: DGC
    model_key: dgc
    model_plain: DGC
    value: 0.0099
    std: 0.0
    paper_value: 0.0099
    paper_std: 0.0
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: null
    sort_value: 0.0099
    sort_std: 0.0
    is_best: false
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.0222
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_display: Feb 2025
    date_iso: '2025-02-17'
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0222
    sort_std: null
    is_best: false
  - model: OFA
    model_key: ofa
    model_plain: OFA
    value: 0.0305
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_display: Feb 2025
    date_iso: '2025-02-17'
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0305
    sort_std: null
    is_best: false
  - model: Dino
    model_key: dino
    model_plain: Dino
    value: 0.047
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.13661'
    title: Hierarchical Network Fusion for Multi-Modal Electron Micrograph Representation
      Learning with Foundational Large Language Models
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.047
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
- &id003
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
    paper_value: 0.725
    paper_std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 3
    true_value: 0.725
    true_std: 0.0023
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.725
    sort_std: 0.0023
    is_best: true
  - model: LRDs
    model_key: lrds
    model_plain: LRDs
    value: 0.7182
    std: 0.0024
    metric: AP
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
    global_rank: 4
    sort_value: 0.7182
    sort_std: 0.0024
    is_best: false
  - model: DRew-GCN
    model_key: drew-gcn
    model_plain: DRew-GCN
    value: 0.6804
    std: 0.0144
    paper_value: 0.6804
    paper_std: 0.0144
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Arroyo2025OnVG
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 19
    true_value: 0.6996
    true_std: 0.0076
    value_gap_source_arxiv: '2506.07624'
    value_gap_source_title: 'Return of ChebNet: Understanding and Improving an Overlooked
      GNN on Long-Range Tasks'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.019199999999999995
    value_note: ''
    paper_rank: 39
    rank_delta: 20
    rank_delta_abs: 20
    rank_delta_direction: worse
    sort_value: 0.6996
    sort_std: 0.0076
    is_best: false
  - model: kGCN-SSM
    model_key: kgcn-ssm
    model_plain: kGCN-SSM
    value: 0.6902
    std: 0.0022
    paper_value: 0.6902
    paper_std: 0.0022
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Arroyo2025OnVG
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 29
    true_value: 0.6902
    true_std: 0.0022
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6902
    sort_std: 0.0022
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
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 33
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 33
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.686
    sort_std: 0.005
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
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 41
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 41
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6765
    sort_std: 0.0047
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 53
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 53
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6621
    sort_std: 0.0067
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
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 57
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.006700000000000039
    value_note: global 0.6601 within std
    paper_rank: 65
    rank_delta: 8
    rank_delta_abs: 8
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
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
    global_rank: 1
    sort_value: 0.2422
    sort_std: 0.0014
    is_best: true
  - model: B-PEARL+SRF
    model_key: b-pearl+srf
    model_plain: B-PEARL+SRF
    value: 0.243
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.03824'
    title: Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph
      Neural Networks
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: https://github.com/ryienh/sketched-random-features
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.243
    sort_std: null
    is_best: true
  - model: GRAMA
    model_key: grama
    model_plain: GRAMA
    value: 0.2436
    std: 0.0022
    metric: MAE
    higher_is_better: false
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
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.2436
    sort_std: 0.0022
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
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 16
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.246
    sort_std: 0.0007
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 26
    true_value: 0.2473
    true_std: 0.0017
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2473
    sort_std: 0.0017
    is_best: false
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.2527
    std: 0.0015
    paper_value: 0.2527
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
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 32
    true_value: 0.2475
    true_std: 0.0007
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.005199999999999982
    value_note: ''
    paper_rank: 63
    rank_delta: 31
    rank_delta_abs: 31
    rank_delta_direction: worse
    sort_value: 0.2475
    sort_std: 0.0007
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
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 35
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2477
    sort_std: 0.0009
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 50
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0009000000000000119
    value_note: global 0.2500 within std
    paper_rank: 59
    rank_delta: 9
    rank_delta_abs: 9
    rank_delta_direction: worse
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: kGCN-SSM
    model_key: kgcn-ssm
    model_plain: kGCN-SSM
    value: 0.2581
    std: 0.0003
    paper_value: 0.2581
    paper_std: 0.0003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Arroyo 2025
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 79
    true_value: 0.2581
    true_std: 0.0003
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2581
    sort_std: 0.0003
    is_best: false
  - model: DRew-GCN
    model_key: drew-gcn
    model_plain: DRew-GCN
    value: 0.2766
    std: 0.0019
    paper_value: 0.2766
    paper_std: 0.0019
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Arroyo 2025
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 95
    true_value: 0.2766
    true_std: 0.0019
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2766
    sort_std: 0.0019
    is_best: false
  metric: MAE
  higher_is_better: false
- &id004
  dataset: SSSP
  rows:
  - model: A-DGN
    model_key: a-dgn
    model_plain: A-DGN
    value: 4.0e-07
    std: 3.0e-07
    paper_value: 4.0e-07
    paper_std: 3.0e-07
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Gravina 2022
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 1
    true_value: 4.0e-07
    true_std: 3.0e-07
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 4.0e-07
    sort_std: 3.0e-07
    is_best: true
  - model: gLSTM
    model_key: glstm
    model_plain: gLSTM
    value: 1.5e-06
    std: 9.0e-06
    paper_value: 1.5e-06
    paper_std: 9.0e-06
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 2
    true_value: 1.5e-06
    true_std: 9.0e-06
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 1.5e-06
    sort_std: 9.0e-06
    is_best: true
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 7.4e-06
    std: 1.0e-07
    paper_value: 7.4e-06
    paper_std: 1.0e-07
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 3
    true_value: 7.4e-06
    true_std: 1.0e-07
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 7.4e-06
    sort_std: 1.0e-07
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.00029
    std: 0.0026
    paper_value: 0.00029
    paper_std: 0.0026
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 4
    true_value: 0.00029
    true_std: 0.0026
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.00029
    sort_std: 0.0026
    is_best: true
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.002
    std: 0.0071
    paper_value: 0.002
    paper_std: 0.0071
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 5
    true_value: 0.002
    true_std: 0.0071
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.002
    sort_std: 0.0071
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.0062
    std: 0.00015
    paper_value: 0.0062
    paper_std: 0.00015
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 6
    true_value: 0.0062
    true_std: 0.00015
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0062
    sort_std: 0.00015
    is_best: false
  - model: DGC
    model_key: dgc
    model_plain: DGC
    value: 0.0071
    std: 5.0e-05
    paper_value: 0.0071
    paper_std: 5.0e-05
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 7
    true_value: 0.0071
    true_std: 5.0e-05
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0071
    sort_std: 5.0e-05
    is_best: false
  - model: GRAND
    model_key: grand
    model_plain: GRAND
    value: 0.008
    std: 0.0046
    paper_value: 0.008
    paper_std: 0.0046
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 8
    true_value: 0.008
    true_std: 0.0046
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.008
    sort_std: 0.0046
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.0089
    std: 0.0
    paper_value: 0.0089
    paper_std: 0.0
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to sssp (score=90)'
    date: Oct 2025
    date_display: Oct 2025
    date_iso: 2025-10
    global_rank: 9
    true_value: 0.0089
    true_std: 0.0
    value_gap_source_arxiv: '2510.08450'
    value_gap_source_title: ': Mitigating by Increasing Storage Capacity'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.0089
    sort_std: 0.0
    is_best: false
  metric: MSE
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
  - *id003
- benchmark: Algorithmic Graph Tasks
  datasets:
  - *id004
single_proposed_model: gLSTM
main_figure: /figures/2510.08450/main_figure.png
---

