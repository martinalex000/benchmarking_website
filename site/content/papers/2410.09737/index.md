---
title: Towards Stable, Globally Expressive Graph Representations with Laplacian Eigenvectors
arxiv_id: '2410.09737'
authors: []
published_date: Oct 2024
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
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- GINE, with OGE-Aug
- GPS, with OGE-Aug
- GPS & OGE-Aug
mrr: 0.0141
results:
- &id002
  dataset: PCQM-Contact
  rows:
  - model: FloydNet
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ViT-PS
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: NeuralWalker
    value: 0.4707
    std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GPS & OGE-Aug
    value: 0.3543
    std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: SAN
    value: 0.335
    std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GPS
    value: 0.3337
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GCN
    value: 0.3234
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GatedGCN
    value: 0.3218
    std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GINE
    value: 0.318
    std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 17
    is_best: false
  - model: Transformer
    value: 0.3174
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table LRGB
    source_ref: this paper
    global_rank: 61
    is_best: false
  metric: MRR
  higher_is_better: true
- &id001
  dataset: ZINC
  rows:
  - model: ESA
    value: 0.010894100678479495
    std: 0.00022839903839981288
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2402.10793'
    title: An end-to-end attention-based approach for learning on graphs
    date: Feb 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ESA (PE)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: PST
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GPS, with OGE-Aug
    value: 0.064
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 63
    is_best: false
  - model: SpecFormer
    value: 0.066
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 70
    is_best: false
  - model: GINE, with OGE-Aug
    value: 0.066
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 71
    is_best: false
  - model: GIN, with PEG
    value: 0.069
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 91
    is_best: false
  - model: GPS
    value: 0.07
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: CIN
    value: 0.079
    std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GNN (a)
    value: 0.08
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: GIN, with SignNet
    value: 0.085
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 142
    is_best: false
  - model: GSN
    value: 0.115
    std: 0.012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 161
    is_best: false
  - model: KP-GIN+
    value: 0.119
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 155
    is_best: false
  - model: Graphormer
    value: 0.122
    std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: SAN
    value: 0.139
    std: 0.006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 196
    is_best: false
  - model: GIN, with BasisNet
    value: 0.155
    std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 211
    is_best: false
  - model: GIN
    value: 0.163
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: OSAN
    value: 0.187
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 210
    is_best: false
  - model: PNA
    value: 0.188
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table_zinc
    source_ref: this paper
    global_rank: 40
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
main_figure: /figures/2410.09737/main_figure.png
---

