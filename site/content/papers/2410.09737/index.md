---
title: Towards Stable, Globally Expressive Graph Representations with Laplacian Eigenvectors
arxiv_id: '2410.09737'
source_url: ''
authors: []
published_date: Oct 2024
published_date_iso: 2024-10
abstract: Graph neural networks (GNNs) have achieved remarkable success in a variety
  of machine learning tasks over graph data. Existing GNNs usually rely on message
  passing, i.e., computing node representations by gathering information from the
  neighborhood, to build their underlying computational graphs. Such an approach has
  been shown fairly limited in expressive power, and often fails to capture global
  characteristics of graphs. To overcome the issue, a popular solution is to use Laplacian
  eigenvectors as additional node features, as they are known to contain global positional
  information of nodes, and can serve as extra node identifiers aiding GNNs to separate
  structurally similar nodes. Since eigenvectors naturally come with symmetries---namely,
  $O(p)$-group symmetry for every $p$ eigenvectors with equal eigenvalue, properly
  handling such symmetries is crucial for the stability and generalizability of Laplacian
  eigenvector augmented GNNs. However, using a naive $O(p)$-group invariant encoder
  for each $p$-dimensional eigenspace may not keep the full expressivity in the Laplacian
  eigenvectors. Moreover, computing such invariants inevitably entails a hard split
  of Laplacian eigenvalues according to their numerical identity, which suffers from
  great instability when the graph structure has small perturbations. In this paper,
  we propose a novel method exploiting Laplacian eigenvectors to generate stable and
  globally expressive graph representations. The main difference from previous works
  is that (i) our method utilizes learnable $O(p)$-invariant representations for each
  Laplacian eigenspace of dimension $p$, which are built upon powerful orthogonal
  group equivariant neural network layers already well studied in the literature,
  and that (ii) our method deals with numerically close eigenvalues in a smooth fashion,
  ensuring its better robustness against perturbations. Experiments on various graph
  learning benchmarks witness the competitive performance of our method, especially
  its great potential to learn global properties of graphs.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- GINE, with OGE-Aug
- GPS, with OGE-Aug
- GPS & OGE-Aug
mrr: 0.013
adjusted_mrr: 0.0043
mrr_dataset_count: 1
benchmark_categories:
- Classic
- LRGB
- PyG Imported Datasets
task_categories:
- graph_regression
- link_prediction
experiment_scopes:
- edge-level
- graph-level
results:
- &id003
  dataset: Alchemy
  rows:
  - model: GINE + OGE-Aug
    model_key: gine + oge-aug
    model_plain: GINE + OGE-Aug
    value: 0.087
    std: 0.001
    paper_value: 0.087
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 1
    true_value: 0.087
    true_std: 0.001
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.087
    sort_std: 0.001
    is_best: true
  - model: GIN + SPE (All)
    model_key: gin + spe (all)
    model_plain: GIN + SPE (All)
    value: 0.108
    std: 0.001
    paper_value: 0.108
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Huang et al. (2023)
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 2
    true_value: 0.108
    true_std: 0.001
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.108
    sort_std: 0.001
    is_best: false
  - model: GIN + BasisNet (All)
    model_key: gin + basisnet (all)
    model_plain: GIN + BasisNet (All)
    value: 0.11
    std: 0.001
    paper_value: 0.11
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lim et al. (2022)
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 3
    true_value: 0.11
    true_std: 0.001
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.11
    sort_std: 0.001
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.112
    std: 0.001
    paper_value: 0.112
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 4
    true_value: 0.112
    true_std: 0.001
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.112
    sort_std: 0.001
    is_best: false
  - model: GIN + SignNet (All)
    model_key: gin + signnet (all)
    model_plain: GIN + SignNet (All)
    value: 0.113
    std: 0.002
    paper_value: 0.113
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Lim et al. (2022)
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.113
    true_std: 0.002
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.113
    sort_std: 0.002
    is_best: false
  - model: GIN + PEG (8)
    model_key: gin + peg (8)
    model_plain: GIN + PEG (8)
    value: 0.114
    std: 0.001
    paper_value: 0.114
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wang et al. (2022)
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 6
    true_value: 0.114
    true_std: 0.001
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.114
    sort_std: 0.001
    is_best: false
  metric: MAE
  higher_is_better: false
- &id002
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
    value: 0.3337
    std: 0.0006
    paper_value: 0.3337
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 4
    true_value: 0.4703
    true_std: 0.0014
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.1366
    value_note: ''
    paper_rank: 47
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.4703
    sort_std: 0.0014
    is_best: false
  - model: GatedGCN
    model_key: gatedgcn
    model_plain: GatedGCN
    value: 0.3218
    std: 0.0011
    paper_value: 0.3218
    paper_std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 5
    true_value: 0.467
    true_std: 0.0004
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.14520000000000005
    value_note: ''
    paper_rank: 60
    rank_delta: 55
    rank_delta_abs: 55
    rank_delta_direction: worse
    sort_value: 0.467
    sort_std: 0.0004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.3234
    std: 0.0006
    paper_value: 0.3234
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.4526
    true_std: 0.0006
    value_gap_source_arxiv: '2406.03386'
    value_gap_source_title: Learning Long Range Dependencies on Graphs via Random
      Walks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.12919999999999998
    value_note: ''
    paper_rank: 59
    rank_delta: 52
    rank_delta_abs: 52
    rank_delta_direction: worse
    sort_value: 0.4526
    sort_std: 0.0006
    is_best: false
  - model: GPS & OGE-Aug
    model_key: gps & oge-aug
    model_plain: GPS & OGE-Aug
    value: 0.3543
    std: 0.0004
    paper_value: 0.3543
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 11
    true_value: 0.3543
    true_std: 0.0004
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3543
    sort_std: 0.0004
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.318
    std: 0.0027
    paper_value: 0.318
    paper_std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 17
    true_value: 0.3509
    true_std: 0.0006
    value_gap_source_arxiv: '2309.00367'
    value_gap_source_title: Where Did the Gap Go? Reassessing the Long-Range Graph
      Benchmark
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.032899999999999985
    value_note: ''
    paper_rank: 60
    rank_delta: 43
    rank_delta_abs: 43
    rank_delta_direction: worse
    sort_value: 0.3509
    sort_std: 0.0006
    is_best: false
  - model: GPS+EdgeRWSE
    model_key: gps+edgerwse
    model_plain: GPS+EdgeRWSE
    value: 0.3408
    std: 0.0003
    paper_value: 0.3408
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 34
    true_value: 0.3408
    true_std: 0.0003
    value_gap_source_arxiv: '2310.19285'
    value_gap_source_title: Facilitating Graph Neural Networks with Random Walk on
      Simplicial Complexes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 34
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3408
    sort_std: 0.0003
    is_best: false
  - model: GPS+Hodge1Lap
    model_key: gps+hodge1lap
    model_plain: GPS+Hodge1Lap
    value: 0.3407
    std: 0.0004
    paper_value: 0.3407
    paper_std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 35
    true_value: 0.3407
    true_std: 0.0004
    value_gap_source_arxiv: '2310.19285'
    value_gap_source_title: Facilitating Graph Neural Networks with Random Walk on
      Simplicial Complexes
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3407
    sort_std: 0.0004
    is_best: false
  - model: SAN+RWSE
    model_key: san+rwse
    model_plain: SAN+RWSE
    value: 0.3341
    std: 0.0006
    paper_value: 0.3341
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 45
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2310.19285'
    value_gap_source_title: Facilitating Graph Neural Networks with Random Walk on
      Simplicial Complexes
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.0009000000000000119
    value_note: ''
    paper_rank: 47
    rank_delta: 2
    rank_delta_abs: 2
    rank_delta_direction: worse
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: SAN
    model_key: san
    model_plain: SAN
    value: 0.335
    std: 0.0003
    paper_value: 0.335
    paper_std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 46
    true_value: 0.335
    true_std: 0.0003
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.335
    sort_std: 0.0003
    is_best: false
  - model: GPS+LapPE
    model_key: gps+lappe
    model_plain: GPS+LapPE
    value: 0.3337
    std: 0.0006
    paper_value: 0.3337
    paper_std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 49
    true_value: 0.3337
    true_std: 0.0006
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 49
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3337
    sort_std: 0.0006
    is_best: false
  - model: Transformer
    model_key: transformer
    model_plain: Transformer
    value: 0.3174
    std: 0.002
    paper_value: 0.3174
    paper_std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 62
    true_value: 0.3174
    true_std: 0.002
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 62
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.3174
    sort_std: 0.002
    is_best: false
  metric: MRR
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
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 137
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
    is_best: false
  - model: CIN
    model_key: cin
    model_plain: CIN
    value: 0.079
    std: 0.006
    paper_value: 0.079
    paper_std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 7
    true_value: 0.022
    true_std: 0.002
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.057
    value_note: ''
    paper_rank: 137
    rank_delta: 130
    rank_delta_abs: 130
    rank_delta_direction: worse
    sort_value: 0.022
    sort_std: 0.002
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
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
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 198
    rank_delta: 180
    rank_delta_abs: 180
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
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
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 18
    true_value: 0.025
    true_std: 0.004
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.097
    value_note: ''
    paper_rank: 198
    rank_delta: 180
    rank_delta_abs: 180
    rank_delta_direction: worse
    sort_value: 0.025
    sort_std: 0.004
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.08
    std: 0.001
    paper_value: 0.08
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
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046
    value_note: ''
    paper_rank: 139
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
    value: 0.08
    std: 0.001
    paper_value: 0.08
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.046
    value_note: ''
    paper_rank: 139
    rank_delta: 106
    rank_delta_abs: 106
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13072978921109524
    value_note: ''
    paper_rank: 238
    rank_delta: 190
    rank_delta_abs: 190
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: PNA
    model_key: pna
    model_plain: PNA
    value: 0.188
    std: 0.004
    paper_value: 0.188
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 48
    true_value: 0.05727021078890476
    true_std: 0.006639614126119909
    value_gap_source_arxiv: '2402.10793'
    value_gap_source_title: An end-to-end attention-based approach for learning on
      graphs
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.13072978921109524
    value_note: ''
    paper_rank: 238
    rank_delta: 190
    rank_delta_abs: 190
    rank_delta_direction: worse
    sort_value: 0.05727021078890476
    sort_std: 0.006639614126119909
    is_best: false
  - model: GPS, with OGE-Aug
    model_key: gps, with oge-aug
    model_plain: GPS, with OGE-Aug
    value: 0.064
    std: 0.003
    paper_value: 0.064
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 69
    true_value: 0.064
    true_std: 0.003
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.064
    sort_std: 0.003
    is_best: false
  - model: GPS, with OGE-Aug
    model_key: gps, with oge-aug
    model_plain: GPS, with OGE-Aug
    value: 0.064
    std: 0.003
    paper_value: 0.064
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 69
    true_value: 0.064
    true_std: 0.003
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 69
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.064
    sort_std: 0.003
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.098
    value_note: ''
    paper_rank: 233
    rank_delta: 160
    rank_delta_abs: 160
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
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
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 73
    true_value: 0.065
    true_std: 0.004
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.098
    value_note: ''
    paper_rank: 233
    rank_delta: 160
    rank_delta_abs: 160
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.066
    std: 0.003
    paper_value: 0.066
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 76
    true_value: 0.066
    true_std: 0.003
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.066
    sort_std: 0.003
    is_best: false
  - model: SpecFormer
    model_key: specformer
    model_plain: SpecFormer
    value: 0.066
    std: 0.003
    paper_value: 0.066
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 76
    true_value: 0.066
    true_std: 0.003
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.066
    sort_std: 0.003
    is_best: false
  - model: GINE, with OGE-Aug
    model_key: gine, with oge-aug
    model_plain: GINE, with OGE-Aug
    value: 0.066
    std: 0.002
    paper_value: 0.066
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 77
    true_value: 0.066
    true_std: 0.002
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.066
    sort_std: 0.002
    is_best: false
  - model: GINE, with OGE-Aug
    model_key: gine, with oge-aug
    model_plain: GINE, with OGE-Aug
    value: 0.066
    std: 0.002
    paper_value: 0.066
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 77
    true_value: 0.066
    true_std: 0.002
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.066
    sort_std: 0.002
    is_best: false
  - model: GIN, with PEG
    model_key: gin, with peg
    model_plain: GIN, with PEG
    value: 0.069
    std: 0.004
    paper_value: 0.069
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 98
    true_value: 0.069
    true_std: 0.004
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.004
    is_best: false
  - model: GIN, with PEG
    model_key: gin, with peg
    model_plain: GIN, with PEG
    value: 0.069
    std: 0.004
    paper_value: 0.069
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 98
    true_value: 0.069
    true_std: 0.004
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 98
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.069
    sort_std: 0.004
    is_best: false
  - model: GIN, with SignNet
    model_key: gin, with signnet
    model_plain: GIN, with SignNet
    value: 0.085
    std: 0.003
    paper_value: 0.085
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 155
    true_value: 0.085
    true_std: 0.003
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.003
    is_best: false
  - model: GIN, with SignNet
    model_key: gin, with signnet
    model_plain: GIN, with SignNet
    value: 0.085
    std: 0.003
    paper_value: 0.085
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 155
    true_value: 0.085
    true_std: 0.003
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 155
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.085
    sort_std: 0.003
    is_best: false
  - model: KP-GIN+
    model_key: kp-gin+
    model_plain: KP-GIN+
    value: 0.119
    std: 0.002
    paper_value: 0.119
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 170
    true_value: 0.093
    true_std: 0.007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025999999999999995
    value_note: ''
    paper_rank: 193
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.093
    sort_std: 0.007
    is_best: false
  - model: KP-GIN+
    model_key: kp-gin+
    model_plain: KP-GIN+
    value: 0.119
    std: 0.002
    paper_value: 0.119
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 170
    true_value: 0.093
    true_std: 0.007
    value_gap_source_arxiv: '2312.01538'
    value_gap_source_title: Recurrent Distance Filtering for Graph Representation
      Learning
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.025999999999999995
    value_note: ''
    paper_rank: 193
    rank_delta: 23
    rank_delta_abs: 23
    rank_delta_direction: worse
    sort_value: 0.093
    sort_std: 0.007
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.115
    std: 0.012
    paper_value: 0.115
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 176
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013999999999999999
    value_note: ''
    paper_rank: 187
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.101
    sort_std: 0.01
    is_best: false
  - model: GSN
    model_key: gsn
    model_plain: GSN
    value: 0.115
    std: 0.012
    paper_value: 0.115
    paper_std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 176
    true_value: 0.101
    true_std: 0.01
    value_gap_source_arxiv: '2501.03113'
    value_gap_source_title: 'Balancing Efficiency and Expressiveness: Subgraph GNNs
      with Walk-Based Centrality'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.013999999999999999
    value_note: ''
    paper_rank: 187
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
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
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 211
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
    paper_rank: 212
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
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
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 211
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
    paper_rank: 212
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.1341
    sort_std: 0.0063
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.187
    std: 0.004
    paper_value: 0.187
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 223
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.033
    value_note: ''
    paper_rank: 238
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.187
    std: 0.004
    paper_value: 0.187
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 223
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.033
    value_note: ''
    paper_rank: 238
    rank_delta: 15
    rank_delta_abs: 15
    rank_delta_direction: worse
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  - model: GIN, with BasisNet
    model_key: gin, with basisnet
    model_plain: GIN, with BasisNet
    value: 0.155
    std: 0.007
    paper_value: 0.155
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 224
    true_value: 0.155
    true_std: 0.007
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 224
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.155
    sort_std: 0.007
    is_best: false
  - model: GIN, with BasisNet
    model_key: gin, with basisnet
    model_plain: GIN, with BasisNet
    value: 0.155
    std: 0.007
    paper_value: 0.155
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    variant_inference_reason: ''
    date: Oct 2024
    date_display: Oct 2024
    date_iso: 2024-10
    global_rank: 224
    true_value: 0.155
    true_std: 0.007
    value_gap_source_arxiv: '2410.09737'
    value_gap_source_title: Towards Stable, Globally Expressive Graph Representations
      with Laplacian Eigenvectors
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 224
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.155
    sort_std: 0.007
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
- benchmark: PyG Imported Datasets
  datasets:
  - *id003
main_figure: /figures/2410.09737/main_figure.png
---

