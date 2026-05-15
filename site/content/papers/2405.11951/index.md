---
title: 'Distinguished In Uniform: - Self-Attention Vs. Virtual Nodes'
arxiv_id: '2405.11951'
authors: []
published_date: May 2024
abstract: 'Graph Transformers (GTs) such as SAN and GPS are graph processing models
  that combine Message-Passing GNNs (MPGNNs) with global Self-Attention. They were
  shown to be universal function approximators, with two reservations: 1. The initial
  node features must be augmented with certain positional encodings. 2. The approximation
  is non-uniform: Graphs of different sizes may require a different approximating
  network. We first clarify that this form of universality is not unique to GTs: Using
  the same positional encodings, also pure MPGNNs and even 2-layer MLPs are non-uniform
  universal approximators. We then consider uniform expressivity: The target function
  is to be approximated by a single network for graphs of all sizes. There, we compare
  GTs to the more efficient MPGNN + Virtual Node architecture. The essential difference
  between the two model definitions is in their global computation method -- Self-Attention
  Vs Virtual Node. We prove that none of the models is a uniform-universal approximator,
  before proving our main result: Neither model’s uniform expressivity subsumes the
  other’s. We demonstrate the theory with experiments on synthetic data. We further
  augment our study with real-world datasets, observing mixed results which indicate
  no clear ranking in practice as well.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GatedGCN + VN
mrr: 1.0
results:
- &id001
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
    table_ref: Table 1
    source_ref: this paper
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
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    global_rank: 3
    is_best: false
  - model: LGI-GT
    value: 0.304
    std: 0.0029
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: LGI-GT
    global_rank: 4
    is_best: false
  - model: CRaWl
    value: 0.2986
    std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.12059'
    title: A Scalable and Effective Alternative to Graph Transformers
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  - model: CRaWI
    value: 0.2986
    std: 0.0025
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2307.07107'
    title: Graph Positional and Structural Encoder
    date: '2023-07-14'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 6
    is_best: false
  - model: GPS
    value: 0.2907
    std: 0.0028
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Rampásek et al. 2022
    global_rank: 21
    is_best: false
  - model: SAN
    value: 0.2765
    std: 0.0042
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kreuzer et al. 2021
    global_rank: 35
    is_best: false
  - model: GINE
    value: 0.2703
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    global_rank: 43
    is_best: false
  - model: GCN
    value: 0.2483
    std: 0.0037
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: Tonshoff et al. 2023
    global_rank: 39
    is_best: false
  metric: AP
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
single_proposed_model: GatedGCN + VN
main_figure: /figures/2405.11951/main_figure.png
---

