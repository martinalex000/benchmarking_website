---
title: 'Latent-Hysteresis Graph ODEs: Modeling Coupled Topology-Feature Evolution
  via Continuous Phase Transitions'
arxiv_id: '2604.24293'
authors: []
published_date: Apr 2026
abstract: 'Abstract Graph neural ordinary differential equations (Graph ODEs) extend
  graph learning from discrete message-passing layers to continuous-time representation
  flows. While it supports adaptive long-range propagation, we show that Graph ODEs
  with strictly positive irreducible mixing operators face an inherent monostability
  trap : in the long-time regime, information leakage is unavoidable and the dynamics
  converge to a single global consensus attractor. We propose the Hysteresis Graph
  ODE (HGODE) , which couples feature evolution with a latent topological potential
  driven by a learned pairwise force. A double-well edge potential and bipolarized
  gate allow edge states to polarize into connected or insulated phases while preserving
  differentiability. We provide asymptotic analysis of the collapse mechanism and
  the proposed hysteretic topology dynamics, and validate HGODE on theory-driven synthetic
  diagnostics and real-world graph benchmarks.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- HGODE
mrr: 0.0282
results:
- &id001
  dataset: Chameleon
  rows:
  - model: GraphMAE
    value: 0.8051
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: MRS-Dir-GCN_DA
    value: 0.8017
    std: 0.0188
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2409.11504'
    title: Preventing Representational Rank Collapse in MPNNs by Splitting the Computational
      Graph
    date: Sep 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: Supervised
    value: 0.8002
    std: 0.0087
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2505.23345'
    title: Graph Positional Autoencoders as Self-supervised Learners
    date: May 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: HGODE
    value: 0.7256
    std: 0.0124
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    table_ref: Table 1
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: SGFormer
    value: 0.4577
    std: 0.0348
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: Polynormer
    value: 0.4169
    std: 0.0322
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 64
    is_best: false
  - model: GraphGPS
    value: 0.4104
    std: 0.0387
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 103
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: Cora
  rows:
  - model: GPM
    value: 0.9285
    std: 0.0054
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: '2025-01-30'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: TRIGON
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: DR
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: HGODE
    value: 0.8626
    std: 0.0078
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    table_ref: Table 1
    source_ref: this paper
    global_rank: 89
    is_best: false
  - model: SGFormer
    value: 0.8459
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 39
    is_best: false
  - model: Polynormer
    value: 0.8324
    std: 0.0072
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 47
    is_best: false
  - model: GraphGPS
    value: 0.8295
    std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 116
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: HGODE
    value: 0.714
    std: 0.022
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    table_ref: Table 2
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: Subgraphormer
    value: 0.661
    std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 147
    is_best: false
  - model: GraphGPS
    value: 0.655
    std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 162
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
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
  - model: GraphGPS
    value: 0.069
    std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 89
    is_best: false
  - model: HGODE
    value: 0.078
    std: 0.025
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    table_ref: Table 1
    source_ref: this paper
    global_rank: 125
    is_best: false
  - model: Subgraphormer
    value: 0.082
    std: 0.04
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  metric: MAE
  higher_is_better: false
- &id005
  dataset: ogbg-molpcba
  rows:
  - model: GatedGCN + VN
    value: 0.3141
    std: 0.0019
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: NeuralWalker
    value: 0.3086
    std: 0.0031
    metric: AP
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
    global_rank: 2
    is_best: false
  - model: GatedGCN
    value: 0.3066
    std: 0.0013
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    arxiv_id: '2405.11951'
    title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
    date: May 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: Subgraphormer
    value: 0.293
    std: 0.004
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  - model: GraphGPS
    value: 0.291
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 20
    is_best: false
  - model: HGODE
    value: 0.278
    std: 0.003
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 1.0
    table_ref: Table 1
    source_ref: this paper
    global_rank: 33
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: Heterophilic Graphs
  datasets:
  - *id001
- benchmark: Classic
  datasets:
  - *id002
  - *id003
- benchmark: LRGB
  datasets:
  - *id004
- benchmark: OGB
  datasets:
  - *id005
single_proposed_model: HGODE
main_figure: /figures/2604.24293/main_figure.png
---

