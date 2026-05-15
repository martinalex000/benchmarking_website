---
title: HSG-12M
arxiv_id: '2506.08618'
authors: []
published_date: Jun 2025
abstract: 'AI is transforming scientific research by revealing new ways to understand
  complex physical systems, but its impact remains constrained by the lack of large,
  high-quality domain-specific datasets. A rich, largely untapped resource lies in
  non-Hermitian quantum physics, where the energy spectra of crystals form intricate
  geometries on the complex plane---termed as Hamiltonian spectral graphs. Despite
  their significance as fingerprints for electronic behavior, their systematic study
  has been intractable due to the reliance on manual extraction. To unlock this potential,
  we introduce Poly2Graph pkg:p2ghttps://github.com/sarinstein-yan/Poly2Graph: a high-performance,
  open-source pipeline that automates the mapping of 1-D crystal Hamiltonians to spectral
  graphs. Using this tool, we present HSG-12M pkg:hsghttps://github.com/sarinstein-yan/HSG-12M:
  a dataset containing 11.6 million static and 5.1 million dynamic Hamiltonian spectral
  graphs across 1401 characteristic-polynomial classes, distilled from 177 TB of spectral
  potential data. Crucially, HSG-12M is the first large-scale dataset of spatial multigraphs---graphs
  embedded in a metric space where multiple geometrically distinct trajectories between
  two nodes are retained as separate edges. This simultaneously addresses a critical
  gap, as existing graph benchmarks overwhelmingly assume simple, non-spatial edges,
  discarding vital geometric information. Benchmarks with popular GNNs expose new
  challenges in learning spatial multi-edges at scale. Beyond its practical utility,
  we show that spectral graphs serve as universal topological fingerprints of polynomials,
  vectors, and matrices, forging a new algebra-to-graph link. HSG-12M lays the groundwork
  for data-driven scientific discovery in condensed matter physics, new opportunities
  in geometry-aware graph learning and beyond.'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GraphSAGE
mrr: 0.0161
results:
- &id001
  dataset: D&D
  rows:
  - model: MPNN
    value: 0.989
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HAC (BFS)
    value: 0.981
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: k-hop
    value: 0.976
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GraphSAGE
    value: 0.523
    std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 62
    is_best: false
  - model: CGCNN
    value: 0.478
    std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 66
    is_best: false
  - model: GINE
    value: 0.379
    std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 68
    is_best: false
  - model: GAT
    value: 0.344
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 34
    is_best: false
  - model: GCN
    value: 0.337
    std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 36
    is_best: false
  - model: GATv2
    value: 0.282
    std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 72
    is_best: false
  - model: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 73
    is_best: false
  - model: GIN
    value: 0.05
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 35
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: HSG-12M
  rows:
  - model: GraphSAGE
    value: 0.546
    std: 0.004
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
  - model: CGCNN
    value: 0.531
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie & Grossman 2018
    global_rank: 2
    is_best: false
  - model: GINE
    value: 0.46
    std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: Hu et al. 2019
    global_rank: 3
    is_best: false
  - model: GCN
    value: 0.365
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    global_rank: 4
    is_best: false
  - model: GAT
    value: 0.365
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Velickovic et al. 2018
    global_rank: 5
    is_best: false
  - model: GATv2
    value: 0.351
    std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2022
    global_rank: 6
    is_best: false
  - model: MF
    value: 0.295
    std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Duvenaud et al. 2015
    global_rank: 7
    is_best: false
  - model: GIN
    value: 0.063
    std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    global_rank: 8
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: HSG-topology
  rows:
  - model: GraphSAGE
    value: 0.62
    std: 0.003
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
  - model: CGCNN
    value: 0.566
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GINE
    value: 0.533
    std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: GAT
    value: 0.434
    std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GATv2
    value: 0.401
    std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: GCN
    value: 0.397
    std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: MF
    value: 0.348
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 7
    is_best: false
  - model: GIN
    value: 0.095
    std: 0.059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
- benchmark: HSG-12M
  datasets:
  - *id002
  - *id003
single_proposed_model: GraphSAGE
main_figure: /figures/2506.08618/main_figure.png
---

