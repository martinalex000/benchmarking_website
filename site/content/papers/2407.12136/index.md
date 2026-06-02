---
title: Molecular Topological Profile (MOLTOP) - Simple and Strong Baseline for Molecular
  Graph Classification
arxiv_id: '2407.12136'
source_url: ''
authors: []
published_date: Jul 2024
published_date_iso: 2024-07
published_venue: ''
abstract: We revisit the effectiveness of topological descriptors for molecular graph
  classification and design a simple, yet strong baseline. We demonstrate that a simple
  approach to feature engineering - employing histogram aggregation of edge descriptors
  and one-hot encoding for atomic numbers and bond types - when combined with a Random
  Forest classifier, can establish a strong baseline for Graph Neural Networks (GNNs).
  The novel algorithm, Molecular Topological Profile (MOLTOP), integrates Edge Betweenness
  Centrality, Adjusted Rand Index and SCAN Structural Similarity score. This approach
  proves to be remarkably competitive when compared to modern GNNs, while also being
  simple, fast, low-variance and hyperparameter-free. Our approach is rigorously tested
  on MoleculeNet datasets using fair evaluation protocol provided by Open Graph Benchmark.
  We additionally show out-of-domain generation capabilities on peptide classification
  task from Long Range Graph Benchmark. The evaluations across eleven benchmark datasets
  reveal MOLTOP's strong discriminative capabilities, surpassing the $1$-WL test and
  even $3$-WL test for some classes of graphs. Our conclusion is that descriptor-based
  baselines, such as the one we propose, are still crucial for accurately assessing
  advancements in the GNN domain.
codebase_url: https://github.com/j-adamczyk/MOLTOP
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- QSAR
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- OGB
- LRGB
- Hypergraph Benchmarks
task_categories:
- graph_classification
- node_classification
experiment_scopes:
- graph-level
- node-level
results:
- &id003
  dataset: LEN
  rows:
  - model: GEM
    model_key: gem
    model_plain: GEM
    value: 0.781
    std: 0.006
    paper_value: 0.781
    paper_std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.781
    sort_std: 0.006
    is_best: true
  - model: D-MPNN
    model_key: d-mpnn
    model_plain: D-MPNN
    value: 0.746
    std: 0.006
    paper_value: 0.746
    paper_std: 0.006
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.746
    sort_std: 0.006
    is_best: false
  - model: GraphMVP
    model_key: graphmvp
    model_plain: GraphMVP
    value: 0.731
    std: 0.013
    paper_value: 0.731
    paper_std: 0.013
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.731
    sort_std: 0.013
    is_best: false
  - model: AttentiveFP
    model_key: attentivefp
    model_plain: AttentiveFP
    value: 0.725
    std: 0.014
    paper_value: 0.725
    paper_std: 0.014
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.725
    sort_std: 0.014
    is_best: false
  - model: QSAR
    model_key: qsar
    model_plain: QSAR
    value: 0.725
    std: 0.005
    paper_value: 0.725
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.725
    sort_std: 0.005
    is_best: false
  - model: ECFP
    model_key: ecfp
    model_plain: ECFP
    value: 0.71
    std: 0.007
    paper_value: 0.71
    paper_std: 0.007
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.71
    sort_std: 0.007
    is_best: false
  - model: GROVER
    model_key: grover
    model_plain: GROVER
    value: 0.708
    std: 0.011
    paper_value: 0.708
    paper_std: 0.011
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.708
    sort_std: 0.011
    is_best: false
  - model: GraphCL
    model_key: graphcl
    model_plain: GraphCL
    value: 0.706
    std: 0.023
    paper_value: 0.706
    paper_std: 0.023
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.706
    sort_std: 0.023
    is_best: false
  - model: JOAO
    model_key: joao
    model_plain: JOAO
    value: 0.696
    std: 0.014
    paper_value: 0.696
    paper_std: 0.014
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.696
    sort_std: 0.014
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.689
    std: 0.02
    paper_value: 0.689
    paper_std: 0.02
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.689
    sort_std: 0.02
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.684
    std: 0.016
    paper_value: 0.684
    paper_std: 0.016
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.684
    sort_std: 0.016
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.67
    std: 0.027
    paper_value: 0.67
    paper_std: 0.027
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.67
    sort_std: 0.027
    is_best: false
  - model: LTP
    model_key: ltp
    model_plain: LTP
    value: 0.653
    std: 0.005
    paper_value: 0.653
    paper_std: 0.005
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.653
    sort_std: 0.005
    is_best: false
  - model: LDP
    model_key: ldp
    model_plain: LDP
    value: 0.638
    std: 0.003
    paper_value: 0.638
    paper_std: 0.003
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.638
    sort_std: 0.003
    is_best: false
  - model: molecular fingerprint
    model_key: molecular fingerprint
    model_plain: molecular fingerprint
    value: 0.626
    std: 0.003
    paper_value: 0.626
    paper_std: 0.003
    metric: AUROC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to len (score=90)'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: null
    sort_value: 0.626
    sort_std: 0.003
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
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
  - model: GINE
    model_key: gine
    model_plain: GINE
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
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: 53
    true_value: 0.6621
    true_std: 0.0067
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.11230000000000007
    value_note: ''
    paper_rank: 96
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.6621
    sort_std: 0.0067
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
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
  - model: MOLTOP
    model_key: moltop
    model_plain: MOLTOP
    value: 0.6459
    std: 0.0005
    paper_value: 0.6459
    paper_std: 0.0005
    metric: AP
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
    published_venue: null
    global_rank: 74
    true_value: 0.6459
    true_std: 0.0005
    value_gap_source_arxiv: '2407.12136'
    value_gap_source_title: Molecular Topological Profile (MOLTOP) - Simple and Strong
      Baseline for Molecular Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 74
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6459
    sort_std: 0.0005
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
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
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: 81
    true_value: 0.6326
    true_std: 0.0126
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 81
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
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
  - model: GCNII
    model_key: gcnii
    model_plain: GCNII
    value: 0.5543
    std: 0.0078
    paper_value: 0.5543
    paper_std: 0.0078
    metric: AP
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
    published_venue: null
    global_rank: 96
    true_value: 0.5543
    true_std: 0.0078
    value_gap_source_arxiv: '2206.08164'
    value_gap_source_title: Long Range Graph Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 96
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5543
    sort_std: 0.0078
    is_best: false
  metric: AP
  higher_is_better: true
- &id001
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
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.7905
    std: 0.0132
    paper_value: 0.7905
    paper_std: 0.0132
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
    published_venue: null
    global_rank: 7
    true_value: 0.851
    true_std: 0.004
    value_gap_source_arxiv: '2305.17589'
    value_gap_source_title: Graph Inductive Biases in Transformers without Message
      Passing
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0605
    value_note: ''
    paper_rank: 47
    rank_delta: 40
    rank_delta_abs: 40
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.004
    is_best: false
  - model: Graphormer
    model_key: graphormer
    model_plain: Graphormer
    value: 0.8051
    std: 0.0053
    paper_value: 0.8051
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: 8
    true_value: 0.851
    true_std: 0.002
    value_gap_source_arxiv: '2209.05481'
    value_gap_source_title: A Molecular Multimodal Foundation Model Associating Molecule
      Graphs with Natural Language
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04589999999999994
    value_note: ''
    paper_rank: 23
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.851
    sort_std: 0.002
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.8094
    std: 0.0057
    paper_value: 0.8094
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: 16
    true_value: 0.8094
    true_std: 0.0057
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 16
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8094
    sort_std: 0.0057
    is_best: false
  - model: GSAT
    model_key: gsat
    model_plain: GSAT
    value: 0.8067
    std: 0.0095
    paper_value: 0.8067
    paper_std: 0.0095
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
    published_venue: null
    global_rank: 21
    true_value: 0.8067
    true_std: 0.0095
    value_gap_source_arxiv: '2407.12136'
    value_gap_source_title: Molecular Topological Profile (MOLTOP) - Simple and Strong
      Baseline for Molecular Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8067
    sort_std: 0.0095
    is_best: false
  - model: MOLTOP
    model_key: moltop
    model_plain: MOLTOP
    value: 0.8042
    std: 0.0025
    paper_value: 0.8042
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: 25
    true_value: 0.8042
    true_std: 0.0025
    value_gap_source_arxiv: '2407.12136'
    value_gap_source_title: Molecular Topological Profile (MOLTOP) - Simple and Strong
      Baseline for Molecular Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8042
    sort_std: 0.0025
    is_best: false
  - model: GSN (directional)
    model_key: gsn (directional)
    model_plain: GSN (directional)
    value: 0.8039
    std: 0.009
    paper_value: 0.8039
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
    date: Jul 2024
    date_display: Jul 2024
    date_iso: 2024-07
    published_venue: null
    global_rank: 26
    true_value: 0.8039
    true_std: 0.009
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 26
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.009
    is_best: false
  - model: WL sp
    model_key: wl sp
    model_plain: WL sp
    value: 0.8039
    std: 0.004
    paper_value: 0.8039
    paper_std: 0.004
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
    published_venue: null
    global_rank: 27
    true_value: 0.8039
    true_std: 0.004
    value_gap_source_arxiv: '2407.12136'
    value_gap_source_title: Molecular Topological Profile (MOLTOP) - Simple and Strong
      Baseline for Molecular Graph Classification
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 27
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8039
    sort_std: 0.004
    is_best: false
  - model: DeeperGCN
    model_key: deepergcn
    model_plain: DeeperGCN
    value: 0.7858
    std: 0.0117
    paper_value: 0.7858
    paper_std: 0.0117
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
    published_venue: null
    global_rank: 58
    true_value: 0.7858
    true_std: 0.0117
    value_gap_source_arxiv: '2205.12454'
    value_gap_source_title: Recipe for a General, Powerful, Scalable Graph Transformer
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 58
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7858
    sort_std: 0.0117
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id003
single_proposed_model: QSAR
---

