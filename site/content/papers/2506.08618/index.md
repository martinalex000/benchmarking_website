---
title: HSG-12M
arxiv_id: '2506.08618'
source_url: ''
authors: []
published_date: Jun 2025
published_date_iso: 2025-06
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
paper_type: method
proposed_models:
- GraphSAGE
mrr: 0.0152
adjusted_mrr: 0.0051
mrr_dataset_count: 1
benchmark_categories:
- TU Dortmund
- HSG-12M
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: MPNN
    model_key: mpnn
    model_plain: MPNN
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
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.989
    sort_std: null
    is_best: true
  - model: HAC (BFS)
    model_key: hac (bfs)
    model_plain: HAC (BFS)
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
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.981
    sort_std: null
    is_best: false
  - model: k-hop
    model_key: k-hop
    model_plain: k-hop
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
    date_display: Nov 2024
    date_iso: 2024-11
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.976
    sort_std: null
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.344
    std: 0.012
    paper_value: 0.344
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 35
    true_value: 0.762
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.41800000000000004
    value_note: ''
    paper_rank: 72
    rank_delta: 37
    rank_delta_abs: 37
    rank_delta_direction: worse
    sort_value: 0.762
    sort_std: null
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.05
    std: 0.021
    paper_value: 0.05
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 38
    true_value: 0.7556
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.7056
    value_note: ''
    paper_rank: 77
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.7556
    sort_std: null
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.337
    std: 0.014
    paper_value: 0.337
    paper_std: 0.014
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 39
    true_value: 0.7546
    true_std: null
    value_gap_source_arxiv: '2407.18480'
    value_gap_source_title: Scalable Graph Compressed Convolutions
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.4176
    value_note: ''
    paper_rank: 72
    rank_delta: 33
    rank_delta_abs: 33
    rank_delta_direction: worse
    sort_value: 0.7546
    sort_std: null
    is_best: false
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.523
    std: 0.02
    paper_value: 0.523
    paper_std: 0.02
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 66
    true_value: 0.554
    true_std: 0.002
    value_gap_source_arxiv: '2503.09008'
    value_gap_source_title: City-Networks
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.031000000000000028
    value_note: ''
    paper_rank: 67
    rank_delta: 1
    rank_delta_abs: 1
    rank_delta_direction: worse
    sort_value: 0.554
    sort_std: 0.002
    is_best: false
  - model: CGCNN
    model_key: cgcnn
    model_plain: CGCNN
    value: 0.478
    std: 0.011
    paper_value: 0.478
    paper_std: 0.011
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 70
    true_value: 0.478
    true_std: 0.011
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 70
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.478
    sort_std: 0.011
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.379
    std: 0.013
    paper_value: 0.379
    paper_std: 0.013
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 72
    true_value: 0.379
    true_std: 0.013
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 72
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.379
    sort_std: 0.013
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.282
    std: 0.03
    paper_value: 0.282
    paper_std: 0.03
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 76
    true_value: 0.282
    true_std: 0.03
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 76
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.282
    sort_std: 0.03
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.271
    std: 0.004
    paper_value: 0.271
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 77
    true_value: 0.271
    true_std: 0.004
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.271
    sort_std: 0.004
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: HSG-12M
  rows:
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.546
    std: 0.004
    paper_value: 0.546
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.546
    true_std: 0.004
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.546
    sort_std: 0.004
    is_best: true
  - model: CGCNN
    model_key: cgcnn
    model_plain: CGCNN
    value: 0.531
    std: 0.004
    paper_value: 0.531
    paper_std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xie & Grossman 2018
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.531
    true_std: 0.004
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.531
    sort_std: 0.004
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.46
    std: 0.025
    paper_value: 0.46
    paper_std: 0.025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Hu et al. 2019
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.46
    true_std: 0.025
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.46
    sort_std: 0.025
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.365
    std: 0.021
    paper_value: 0.365
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kipf & Welling 2017
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.365
    true_std: 0.021
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.365
    sort_std: 0.021
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.365
    std: 0.01
    paper_value: 0.365
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Velickovic et al. 2018
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.365
    true_std: 0.01
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.365
    sort_std: 0.01
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.351
    std: 0.002
    paper_value: 0.351
    paper_std: 0.002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Brody et al. 2022
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.351
    true_std: 0.002
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.351
    sort_std: 0.002
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.295
    std: 0.01
    paper_value: 0.295
    paper_std: 0.01
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Duvenaud et al. 2015
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.295
    true_std: 0.01
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.295
    sort_std: 0.01
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.063
    std: 0.031
    paper_value: 0.063
    paper_std: 0.031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Xu et al. 2019
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 8
    true_value: 0.063
    true_std: 0.031
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.063
    sort_std: 0.031
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: HSG-topology
  rows:
  - model: GraphSAGE
    model_key: graphsage
    model_plain: GraphSAGE
    value: 0.62
    std: 0.003
    paper_value: 0.62
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 1
    true_value: 0.62
    true_std: 0.003
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.62
    sort_std: 0.003
    is_best: true
  - model: CGCNN
    model_key: cgcnn
    model_plain: CGCNN
    value: 0.566
    std: 0.016
    paper_value: 0.566
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 2
    true_value: 0.566
    true_std: 0.016
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.566
    sort_std: 0.016
    is_best: false
  - model: GINE
    model_key: gine
    model_plain: GINE
    value: 0.533
    std: 0.017
    paper_value: 0.533
    paper_std: 0.017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 3
    true_value: 0.533
    true_std: 0.017
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.533
    sort_std: 0.017
    is_best: false
  - model: GAT
    model_key: gat
    model_plain: GAT
    value: 0.434
    std: 0.015
    paper_value: 0.434
    paper_std: 0.015
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 4
    true_value: 0.434
    true_std: 0.015
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.434
    sort_std: 0.015
    is_best: false
  - model: GATv2
    model_key: gatv2
    model_plain: GATv2
    value: 0.401
    std: 0.003
    paper_value: 0.401
    paper_std: 0.003
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 5
    true_value: 0.401
    true_std: 0.003
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.401
    sort_std: 0.003
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.397
    std: 0.009
    paper_value: 0.397
    paper_std: 0.009
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 6
    true_value: 0.397
    true_std: 0.009
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.397
    sort_std: 0.009
    is_best: false
  - model: MF
    model_key: mf
    model_plain: MF
    value: 0.348
    std: 0.012
    paper_value: 0.348
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 7
    true_value: 0.348
    true_std: 0.012
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.348
    sort_std: 0.012
    is_best: false
  - model: GIN
    model_key: gin
    model_plain: GIN
    value: 0.095
    std: 0.059
    paper_value: 0.095
    paper_std: 0.059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Jun 2025
    date_display: Jun 2025
    date_iso: 2025-06
    global_rank: 8
    true_value: 0.095
    true_std: 0.059
    value_gap_source_arxiv: '2506.08618'
    value_gap_source_title: HSG-12M
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.095
    sort_std: 0.059
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

