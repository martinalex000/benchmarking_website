---
title: Spatio-Spectral Graph Neural Networks
arxiv_id: '2405.19121'
authors: []
published_date: '2024-05-29'
abstract: Spatial Message Passing Graph Neural Networks (MPGNNs) are widely used for
  learning on graph-structured data. However, key limitations of l-step MPGNNs are
  that their "receptive field" is typically limited to the l-hop neighborhood of a
  node and that information exchange between distant nodes is limited by over-squashing.
  Motivated by these limitations, we propose Spatio-Spectral Graph Neural Networks
  (S$^2$GNNs) -- a new modeling paradigm for Graph Neural Networks (GNNs) that synergistically
  combines spatially and spectrally parametrized graph filters. Parameterizing filters
  partially in the frequency domain enables global yet efficient information propagation.
  We show that S$^2$GNNs vanquish over-squashing and yield strictly tighter approximation-theoretic
  error bounds than MPGNNs. Further, rethinking graph convolutions at a fundamental
  level unlocks new design spaces. For example, S$^2$GNNs allow for free positional
  encodings that make them strictly more expressive than the 1-Weisfeiler-Lehman (WL)
  test. Moreover, to obtain general-purpose S$^2$GNNs, we propose spectrally parametrized
  filters for directed graphs. S$^2$GNNs outperform spatial MPGNNs, graph transformers,
  and graph rewirings, e.g., on the peptide long-range benchmark tasks, and are competitive
  with state-of-the-art sequence modeling. On a 40 GB GPU, S$^2$GNNs scale to millions
  of nodes.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- S$^2$GAT
- S² DirGCN
- S² GCN
- S² GCN (+PE)
- S²GNN s (Trees, direc, PE, Spec)
mrr: 0.1
results:
- &id001
  dataset: CLUSTER
  rows:
  - model: Tango_GPS
    value: 0.80113
    std: 0.0013800000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GRIT
    value: 0.8003
    std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ma_graph_2023
    global_rank: 2
    is_best: true
  - model: PPGT
    value: 0.80027
    std: 0.00114
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2504.12588'
    title: Plain Transformers Can be Powerful Graph Learners
    date: Apr 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GT + HDSE
    value: 0.79965
    std: 0.00203
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2308.11129'
    title: Enhancing Graph Transformers with Hierarchical Distance Structural Encoding
    date: Aug 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: EGT
    value: 0.7923
    std: 0.0035
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: hussain_global_2022
    global_rank: 10
    is_best: false
  - model: GatedGCN
    value: 0.7808
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 12
    is_best: false
  - model: Exphormer
    value: 0.7807
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shirzad_exphormer_2023
    global_rank: 32
    is_best: false
  - model: GPTrans-Nano
    value: 0.7807
    std: 0.0015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: chen_graph_2023
    global_rank: 33
    is_best: false
  - model: TIGT
    value: 0.7803
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: choi_topology-informed_2024
    global_rank: 34
    is_best: false
  - model: GPS
    value: 0.7802
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: rampasek_recipe_2022
    global_rank: 35
    is_best: false
  - model: ARGNP
    value: 0.7735
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: cai_automatic_2022
    global_rank: 46
    is_best: false
  - model: S² GCN
    value: 0.4546
    std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 65
    is_best: false
  - model: S² GCN (+PE)
    value: 0.4546
    std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 66
    is_best: false
  - model: GCN
    value: 0.27
    std: 0.0002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 48
    is_best: false
  - model: GCN (+PE)
    value: 0.2684
    std: 0.0005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 68
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: CS-Trees
  rows:
  - model: DeepSet (M)
    value: 0.12
    std: 0.009
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GNN (M)
    value: 0.16
    std: 0.01
    metric: R2
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: DeepSet (c)
    value: 0.23
    std: 0.012
    metric: R2
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2507.03707'
    title: CosmoBench
    date: Jul 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: S²GNN s (Trees, direc, PE, Spec)
    value: 0.7767
    std: 0.3306
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (app:source_dist)
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DirGCN (Trees, direc, no PE, no Spec)
    value: 0.8166
    std: 0.5012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (app:source_dist)
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: DirGCN (Trees, undir, no PE, no Spec)
    value: 1.2887
    std: 0.1195
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1 (app:source_dist)
    source_ref: this paper
    global_rank: null
    is_best: false
  metric: R2
  higher_is_better: false
- &id003
  dataset: arxiv-year
  rows:
  - model: S² DirGCN
    value: 0.6495
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 1
    is_best: true
  - model: FaberNet
    value: 0.6462
    std: 0.0101
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Koke et al. 2024
    global_rank: 2
    is_best: true
  - model: DirGCN (tuned)
    value: 0.6444
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: true
  - model: DiGCN
    value: 0.6408
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rossi et al. 2023
    global_rank: 4
    is_best: false
  - model: nsqure~
    value: 0.5869
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: LINKX
    value: 0.56
    std: 0.0134
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.23686'
    title: Towards Dynamic Message Passing on Graphs
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    is_best: false
  - model: H2GCN
    value: 0.4909
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 7
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: ogbn-products
  rows:
  - model: SAGE
    value: 0.9334
    std: 0.0006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.9115
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2410.05697'
    title: 'Diffusing to the Top: Boost Graph Neural Networks with Minimal Hyperparameter
      Tuning'
    date: Oct 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GLEM-GNN
    value: 0.8736
    std: 0.0007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.03393'
    title: Exploring the Potential of Large Language Models (LLMs) Learning on Graphs
    date: Jul 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: S$^2$GAT
    value: 0.811
    std: 0.007
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GAT
    value: 0.798
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: GNNBenchmark
  datasets:
  - *id001
- benchmark: OGB
  datasets:
  - *id002
- benchmark: LINKX Benchmarks
  datasets:
  - *id003
- benchmark: CosmoBench
  datasets:
  - *id004
main_figure: /figures/2405.19121/main_figure.png
---

