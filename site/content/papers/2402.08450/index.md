---
title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products'
arxiv_id: '2402.08450'
source_url: ''
authors: []
published_date: Feb 13, 2024
published_date_iso: '2024-02-13'
published_venue: ''
abstract: 'In the realm of Graph Neural Networks (GNNs), two exciting research directions
  have recently emerged: Subgraph GNNs and Graph Transformers. In this paper, we propose
  an architecture that integrates both approaches, dubbed Subgraphormer, which combines
  the enhanced expressive power, message-passing mechanisms, and aggregation schemes
  from Subgraph GNNs with attention and positional encodings, arguably the most important
  components in Graph Transformers. Our method is based on an intriguing new connection
  we reveal between Subgraph GNNs and product graphs, suggesting that Subgraph GNNs
  can be formulated as Message Passing Neural Networks (MPNNs) operating on a product
  of the graph with itself. We use this formulation to design our architecture: first,
  we devise an attention mechanism based on the connectivity of the product graph.
  Following this, we propose a novel and efficient positional encoding scheme for
  Subgraph GNNs, which we derive as a positional encoding for the product graph. Our
  experimental results demonstrate significant performance improvements over both
  Subgraph GNNs and Graph Transformers on a wide range of datasets.'
codebase_url: https://github.com/BarSGuy/Subgraphormer
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- MPNN
mrr: 0.0312
adjusted_mrr: 0.0104
mrr_dataset_count: 1
benchmark_categories:
- Classic
- MoleculeNet
- LRGB
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
  dataset: BACE
  rows:
  - model: LLaMA2-7B <SO>G_k</SO>
    model_key: llama2-7b g_k
    model_plain: LLaMA2-7B G_k
    value: 0.984
    std: 0.008
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2602.01771'
    title: '<SO$ _k$>: One LLM Token for Explicit Graph Structural Understanding'
    date: Feb 2026
    date_display: Feb 2026
    date_iso: 2026-02
    codebase_url: https://github.com/Jingyao-Wu/SOG
    uses_external_data: true
    is_global_top: true
    global_rank: 1
    sort_value: 0.984
    sort_std: 0.008
    is_best: true
  - model: Gode
    model_key: gode
    model_plain: Gode
    value: 0.92
    std: 0.022
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 2
    sort_value: 0.92
    sort_std: 0.022
    is_best: false
  - model: KANO_CMPNN
    model_key: kano_cmpnn
    model_plain: KANO_CMPNN
    value: 0.907
    std: 0.031
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.01631'
    title: Bi-level Contrastive Learning for Knowledge-Enhanced Molecule Representations
    date: Jun 2023
    date_display: Jun 2023
    date_iso: 2023-06
    codebase_url: ''
    uses_external_data: true
    is_global_top: true
    global_rank: 3
    sort_value: 0.907
    sort_std: 0.031
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.7297
    std: 0.04
    paper_value: 0.7297
    paper_std: 0.04
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 26
    true_value: 0.861
    true_std: 0.013
    value_gap_source_arxiv: '2006.04804'
    value_gap_source_title: Optimal Transport Graph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13129999999999997
    value_note: ''
    paper_rank: 136
    rank_delta: 110
    rank_delta_abs: 110
    rank_delta_direction: worse
    sort_value: 0.861
    sort_std: 0.013
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.8435
    std: 0.0065
    paper_value: 0.8435
    paper_std: 0.0065
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 38
    true_value: 0.8435
    true_std: 0.0065
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8435
    sort_std: 0.0065
    is_best: false
  - model: GNN-SSWL
    model_key: gnn-sswl
    model_plain: GNN-SSWL
    value: 0.827
    std: 0.018
    paper_value: 0.827
    paper_std: 0.018
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 46
    true_value: 0.827
    true_std: 0.018
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.827
    sort_std: 0.018
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.7915
    std: 0.0144
    paper_value: 0.7915
    paper_std: 0.0144
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 95
    true_value: 0.7915
    true_std: 0.0144
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 95
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7915
    sort_std: 0.0144
    is_best: false
  - model: DS-GNN
    model_key: ds-gnn
    model_plain: DS-GNN
    value: 0.7841
    std: 0.0194
    paper_value: 0.7841
    paper_std: 0.0194
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua 2023
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 105
    true_value: 0.7841
    true_std: 0.0194
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7841
    sort_std: 0.0194
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.723
    std: 0.066
    paper_value: 0.723
    paper_std: 0.066
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian 2022
    variant_inference_reason: 'dataset: fuzzy match to bace (score=90)'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 137
    true_value: 0.723
    true_std: 0.066
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.723
    sort_std: 0.066
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
- &id004
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
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
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
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
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
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 33
    true_value: 0.686
    true_std: 0.005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09300000000000008
    value_note: ''
    paper_rank: 90
    rank_delta: 57
    rank_delta_abs: 57
    rank_delta_direction: worse
    sort_value: 0.686
    sort_std: 0.005
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
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 41
    true_value: 0.6765
    true_std: 0.0047
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09009999999999996
    value_note: ''
    paper_rank: 90
    rank_delta: 49
    rank_delta_abs: 49
    rank_delta_direction: worse
    sort_value: 0.6765
    sort_std: 0.0047
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
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 57
    true_value: 0.6601
    true_std: 0.0061
    value_gap_source_arxiv: '2502.09365'
    value_gap_source_title: Simple Path Structural Encoding for Graph Transformers
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.00660000000000005
    value_note: ''
    paper_rank: 62
    rank_delta: 5
    rank_delta_abs: 5
    rank_delta_direction: worse
    sort_value: 0.6601
    sort_std: 0.0061
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.6439
    std: 0.0075
    paper_value: 0.6439
    paper_std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 61
    true_value: 0.6562
    true_std: 0.0075
    value_gap_source_arxiv: '2302.08647'
    value_gap_source_title: Multiresolution Graph Transformers and Wavelet Positional
      Encoding for Learning Hierarchical Structures
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.012299999999999978
    value_note: ''
    paper_rank: 75
    rank_delta: 14
    rank_delta_abs: 14
    rank_delta_direction: worse
    sort_value: 0.6562
    sort_std: 0.0075
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
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 79
    true_value: 0.6384
    true_std: 0.0121
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 79
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6384
    sort_std: 0.0121
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.6373
    std: 0.011
    paper_value: 0.6373
    paper_std: 0.011
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 80
    true_value: 0.6373
    true_std: 0.011
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6373
    sort_std: 0.011
    is_best: false
  - model: Transf.+LapPE
    model_key: transf.+lappe
    model_plain: Transf.+LapPE
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
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 82
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6326
    sort_std: 0.0126
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    paper_value: 0.6069
    paper_std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 87
    true_value: 0.6069
    true_std: 0.0035
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 87
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6069
    sort_std: 0.0035
    is_best: false
  - model: GNN-SSWL
    model_key: gnn-sswl
    model_plain: GNN-SSWL
    value: 0.5847
    std: 0.005
    paper_value: 0.5847
    paper_std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 92
    true_value: 0.5847
    true_std: 0.005
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 92
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5847
    sort_std: 0.005
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
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 97
    true_value: 0.5498
    true_std: 0.0079
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 97
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5498
    sort_std: 0.0079
    is_best: false
  metric: AP
  higher_is_better: true
- &id003
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
    date: Aug 7, 2025
    date_display: Aug 2025
    date_iso: '2025-08-07'
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
    date: Nov 5, 2025
    date_display: Nov 2025
    date_iso: '2025-11-05'
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
    date: Jun 9, 2025
    date_display: Jun 2025
    date_iso: '2025-06-09'
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
    table_ref: Table 1
    source_ref: Kipf 2016
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 16
    true_value: 0.246
    true_std: 0.0007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.10360000000000003
    value_note: ''
    paper_rank: 105
    rank_delta: 89
    rank_delta_abs: 89
    rank_delta_direction: worse
    sort_value: 0.246
    sort_std: 0.0007
    is_best: false
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
    value: 0.2475
    std: 0.0007
    paper_value: 0.2475
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
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 32
    true_value: 0.2475
    true_std: 0.0007
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 32
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0007
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.2475
    std: 0.0007
    paper_value: 0.2475
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
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 31
    true_value: 0.2475
    true_std: 0.0007
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 31
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2475
    sort_std: 0.0007
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
    table_ref: Table 1
    source_ref: Bresson 2017
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 35
    true_value: 0.2477
    true_std: 0.0009
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.09430000000000002
    value_note: ''
    paper_rank: 104
    rank_delta: 69
    rank_delta_abs: 69
    rank_delta_direction: worse
    sort_value: 0.2477
    sort_std: 0.0009
    is_best: false
  - model: GPS
    model_key: gps
    model_plain: GPS
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
    table_ref: Table 1
    source_ref: Rampásek 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 50
    true_value: 0.25
    true_std: 0.0005
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.25
    sort_std: 0.0005
    is_best: false
  - model: Transf.+LapPE
    model_key: transf.+lappe
    model_plain: Transf.+LapPE
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
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 65
    true_value: 0.2529
    true_std: 0.0016
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 65
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2529
    sort_std: 0.0016
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.2545
    std: 0.0012
    paper_value: 0.2545
    paper_std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 73
    true_value: 0.2545
    true_std: 0.0012
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.2545
    sort_std: 0.0012
    is_best: false
  - model: GNN-SSWL
    model_key: gnn-sswl
    model_plain: GNN-SSWL
    value: 0.257
    std: 0.0006
    paper_value: 0.257
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang 2023
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 78
    true_value: 0.257
    true_std: 0.0006
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.257
    sort_std: 0.0006
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
    table_ref: Table 1
    source_ref: Kreuzer 2021
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 88
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
    paper_rank: 88
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.268
    sort_std: 0.004
    is_best: false
  - model: GatedGCN+RWSE
    model_key: gatedgcn+rwse
    model_plain: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    paper_value: 0.3357
    paper_std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Dwivedi 2022
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 103
    true_value: 0.3357
    true_std: 0.0006
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3357
    sort_std: 0.0006
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
    table_ref: Table 1
    source_ref: Xu 2018
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 106
    true_value: 0.3547
    true_std: 0.0045
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 106
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3547
    sort_std: 0.0045
    is_best: false
  metric: MAE
  higher_is_better: false
- &id001
  dataset: ZINC
  rows:
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.004
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.004
    sort_std: null
    is_best: true
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.006
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2306.03589'
    title: How does over-squashing affect the power of GNNs?
    date: Jun 6, 2023
    date_display: Jun 2023
    date_iso: '2023-06-06'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.006
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.163
    std: 0.004
    paper_value: 0.163
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 3
    true_value: 0.014
    true_std: null
    value_gap_source_arxiv: '2306.03589'
    value_gap_source_title: How does over-squashing affect the power of GNNs?
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.149
    value_note: ''
    paper_rank: 117
    rank_delta: 114
    rank_delta_abs: 114
    rank_delta_direction: worse
    sort_value: 0.014
    sort_std: null
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.071
    std: 0.001
    paper_value: 0.071
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Puny et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 4
    true_value: 0.02
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05099999999999999
    value_note: ''
    paper_rank: 50
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: PPGN++(6)
    model_key: ppgn++(6)
    model_plain: PPGN++(6)
    value: 0.02
    std: 0.001
    paper_value: 0.02
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Puny et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 4
    true_value: 0.02
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.02
    sort_std: 0.001
    is_best: false
  - model: GPM
    model_key: gpm
    model_plain: GPM
    value: 0.021
    std: 0.002
    metric: MAE
    higher_is_better: false
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
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.021
    sort_std: 0.002
    is_best: false
  - model: GNN-SSWL
    model_key: gnn-sswl
    model_plain: GNN-SSWL
    value: 0.07
    std: 0.005
    paper_value: 0.07
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 6
    true_value: 0.022
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04800000000000001
    value_note: ''
    paper_rank: 49
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.001
    is_best: false
  - model: GNN-SSWL
    model_key: gnn-sswl
    model_plain: GNN-SSWL
    value: 0.022
    std: 0.001
    paper_value: 0.022
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 6
    true_value: 0.022
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.022
    sort_std: 0.001
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.063
    std: 0.001
    paper_value: 0.063
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
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 8
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04
    value_note: ''
    paper_rank: 34
    rank_delta: 26
    rank_delta_abs: 26
    rank_delta_direction: worse
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: Subgraphormer
    model_key: subgraphormer
    model_plain: Subgraphormer
    value: 0.023
    std: 0.001
    paper_value: 0.023
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
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 8
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.083
    std: 0.003
    paper_value: 0.083
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Frasca et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 12
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059000000000000004
    value_note: ''
    paper_rank: 58
    rank_delta: 46
    rank_delta_abs: 46
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: SUN
    model_key: sun
    model_plain: SUN
    value: 0.024
    std: 0.003
    paper_value: 0.024
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Frasca et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 12
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.122
    std: 0.006
    paper_value: 0.122
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 13
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 87
    rank_delta: 74
    rank_delta_abs: 74
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.052
    std: 0.005
    paper_value: 0.052
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Ying et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 13
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.026999999999999996
    value_note: ''
    paper_rank: 30
    rank_delta: 17
    rank_delta_abs: 17
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.081
    std: 0.009
    paper_value: 0.081
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 14
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056
    value_note: ''
    paper_rank: 58
    rank_delta: 44
    rank_delta_abs: 44
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: Graphormer-GD
    model_key: graphormer-gd
    model_plain: Graphormer-GD
    value: 0.025
    std: 0.004
    paper_value: 0.025
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 14
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 14
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.025
    sort_std: 0.004
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
    source_ref: Rampásek et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 16
    true_value: 0.0262
    true_std: 0.0025
    value_gap_source_arxiv: '2305.15747'
    value_gap_source_title: Union Subgraph Neural Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.043800000000000006
    value_note: ''
    paper_rank: 49
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.0262
    sort_std: 0.0025
    is_best: false
  - model: URPE
    model_key: urpe
    model_plain: URPE
    value: 0.086
    std: 0.007
    paper_value: 0.086
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luo et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 18
    true_value: 0.028
    true_std: 0.002
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057999999999999996
    value_note: ''
    paper_rank: 61
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.028
    sort_std: 0.002
    is_best: false
  - model: URPE
    model_key: urpe
    model_plain: URPE
    value: 0.028
    std: 0.002
    paper_value: 0.028
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Luo et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 18
    true_value: 0.028
    true_std: 0.002
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 18
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.028
    sort_std: 0.002
    is_best: false
  - model: NGNN
    model_key: ngnn
    model_plain: NGNN
    value: 0.111
    std: 0.003
    paper_value: 0.111
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 20
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.082
    value_note: ''
    paper_rank: 79
    rank_delta: 59
    rank_delta_abs: 59
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: NGNN
    model_key: ngnn
    model_plain: NGNN
    value: 0.029
    std: 0.001
    paper_value: 0.029
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 20
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 20
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: DS-GNN
    model_key: ds-gnn
    model_plain: DS-GNN
    value: 0.102
    std: 0.003
    paper_value: 0.102
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 21
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.073
    value_note: ''
    paper_rank: 74
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.003
    is_best: false
  - model: DS-GNN
    model_key: ds-gnn
    model_plain: DS-GNN
    value: 0.029
    std: 0.003
    paper_value: 0.029
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 21
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.029
    sort_std: 0.003
    is_best: false
  - model: GNN-AK
    model_key: gnn-ak
    model_plain: GNN-AK
    value: 0.091
    std: 0.002
    paper_value: 0.091
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhao et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 23
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056999999999999995
    value_note: ''
    paper_rank: 66
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.094
    std: 0.004
    paper_value: 0.094
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 29
    true_value: 0.044
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: true
    has_value_note: false
    value_gap: 0.05
    value_note: ''
    paper_rank: 68
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.044
    sort_std: 0.003
    is_best: false
  - model: CIN (small)
    model_key: cin (small)
    model_plain: CIN (small)
    value: 0.044
    std: 0.003
    paper_value: 0.044
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bodnar et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 29
    true_value: 0.044
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.044
    sort_std: 0.003
    is_best: false
  - model: K-Subgraph SAT
    model_key: k-subgraph sat
    model_plain: K-Subgraph SAT
    value: 0.094
    std: 0.008
    paper_value: 0.094
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 69
    true_value: 0.094
    true_std: 0.008
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.094
    sort_std: 0.008
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.101
    std: 0.01
    paper_value: 0.101
    paper_std: 0.01
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bouritsas et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 73
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 73
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.139
    std: 0.006
    paper_value: 0.139
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 97
    true_value: 0.1341
    true_std: 0.0063
    value_gap_source_arxiv: '2602.02268'
    value_gap_source_title: 'HopFormer: Sparse Graph Transformers with Explicit Receptive
      Field Control'
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: true
    value_gap: 0.0049000000000000155
    value_note: global 0.1341 within std
    paper_rank: 100
    rank_delta: 3
    rank_delta_abs: 3
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.154
    std: 0.008
    paper_value: 0.154
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al.
    variant_inference_reason: 'dataset: exact match'
    date: Feb 13, 2024
    date_display: Feb 2024
    date_iso: '2024-02-13'
    published_venue: null
    global_rank: 111
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 111
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: MoleculeNet
  datasets:
  - *id002
- benchmark: LRGB
  datasets:
  - *id003
  - *id004
single_proposed_model: MPNN
---

