---
title: A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products and
  Graph Coarsening
arxiv_id: '2406.09291'
source_url: ''
authors: []
published_date: Jun 2024
published_date_iso: 2024-06
abstract: Subgraph GNNs enhance message-passing GNNs expressivity by representing
  graphs as sets of subgraphs, demonstrating impressive performance across various
  tasks. However, their scalability is hindered by the need to process large numbers
  of subgraphs. While previous approaches attempted to generate smaller subsets of
  subgraphs through random or learnable sampling, these methods often yielded suboptimal
  selections or were limited to small subset sizes, ultimately compromising their
  effectiveness. This paper introduces a new Subgraph GNN framework to address these
  issues. Our approach diverges from most previous methods by associating subgraphs
  with node clusters rather than with individual nodes. We show that the resulting
  collection of subgraphs can be viewed as the product of coarsened and original graphs,
  unveiling a new connectivity structure on which we perform generalized message passing.
  Crucially, controlling the coarsening function enables meaningful selection of any
  number of subgraphs. In addition, we reveal novel permutation symmetries in the
  resulting node feature tensor, characterize associated linear equivariant layers,
  and integrate them into our Subgraph GNN. We also introduce novel node marking strategies
  and provide a theoretical analysis of their expressive power and other key aspects
  of our approach. Extensive experiments on multiple graph learning benchmarks demonstrate
  that our method is significantly more flexible than previous approaches, as it can
  seamlessly handle any number of subgraphs, while consistently outperforming baseline
  approaches. Our code is available at https://github.com/BarSGuy/Efficient-Subgraph-GNNs.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- CS-GNN
mrr: 0.0051
adjusted_mrr: 0.0017
mrr_dataset_count: 1
benchmark_categories:
- Classic
task_categories:
- graph_regression
experiment_scopes:
- graph-level
results:
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
    date: May 5, 2024
    date_display: May 2024
    date_iso: '2024-05-05'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.018
    sort_std: 0.001
    is_best: false
  - model: GNN-SSWL+
    model_key: gnn-sswl+
    model_plain: GNN-SSWL+
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
    source_ref: Zhang et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 8
    true_value: 0.022
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04800000000000001
    value_note: ''
    paper_rank: 107
    rank_delta: 99
    rank_delta_abs: 99
    rank_delta_direction: worse
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
    source_ref: Bar-Shalom et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 11
    true_value: 0.023
    true_std: 0.001
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04
    value_note: ''
    paper_rank: 64
    rank_delta: 53
    rank_delta_abs: 53
    rank_delta_direction: worse
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
    table_ref: Table 2
    source_ref: Frasca et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 14
    true_value: 0.024
    true_std: 0.003
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.059000000000000004
    value_note: ''
    paper_rank: 150
    rank_delta: 136
    rank_delta_abs: 136
    rank_delta_direction: worse
    sort_value: 0.024
    sort_std: 0.003
    is_best: false
  - model: DSS-GNN
    model_key: dss-gnn
    model_plain: DSS-GNN
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
    table_ref: Table 2
    source_ref: Bevilacqua et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 29
    true_value: 0.029
    true_std: 0.003
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.073
    value_note: ''
    paper_rank: 188
    rank_delta: 159
    rank_delta_abs: 159
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.003
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
    table_ref: Table 2
    source_ref: Zhang et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 28
    true_value: 0.029
    true_std: 0.001
    value_gap_source_arxiv: '2405.02795'
    value_gap_source_title: Graph as Point Set
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.082
    value_note: ''
    paper_rank: 198
    rank_delta: 170
    rank_delta_abs: 170
    rank_delta_direction: worse
    sort_value: 0.029
    sort_std: 0.001
    is_best: false
  - model: GNN (a)
    model_key: gnn (a)
    model_plain: GNN (a)
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
    table_ref: Table 2
    source_ref: Zhao et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 33
    true_value: 0.034
    true_std: 0.007
    value_gap_source_arxiv: '2501.18739'
    value_gap_source_title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.056999999999999995
    value_note: ''
    paper_rank: 178
    rank_delta: 145
    rank_delta_abs: 145
    rank_delta_direction: worse
    sort_value: 0.034
    sort_std: 0.007
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
    source_ref: Xu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 75
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
    paper_rank: 246
    rank_delta: 171
    rank_delta_abs: 171
    rank_delta_direction: worse
    sort_value: 0.065
    sort_std: 0.004
    is_best: false
  - model: GCN
    model_key: gcn
    model_plain: GCN
    value: 0.321
    std: 0.009
    paper_value: 0.321
    paper_std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Kipf & Welling 2016
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 131
    true_value: 0.076
    true_std: 0.009
    value_gap_source_arxiv: '2502.09263'
    value_gap_source_title: Can Classic GNNs Be Strong Baselines for Graph-level Tasks?
      Simple Architectures Meet Excellence
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.245
    value_note: ''
    paper_rank: 276
    rank_delta: 145
    rank_delta_abs: 145
    rank_delta_direction: worse
    sort_value: 0.076
    sort_std: 0.009
    is_best: false
  - model: Mag-GNN
    model_key: mag-gnn
    model_plain: Mag-GNN
    value: 0.106
    std: 0.014
    paper_value: 0.106
    paper_std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 195
    true_value: 0.106
    true_std: 0.014
    value_gap_source_arxiv: '2406.09291'
    value_gap_source_title: A Flexible, Equivariant Framework for Subgraph GNNs via
      Graph Products and Graph Coarsening
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 195
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.106
    sort_std: 0.014
    is_best: false
  - model: CS-GNN
    model_key: cs-gnn
    model_plain: CS-GNN
    value: 0.109
    std: 0.005
    paper_value: 0.109
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 198
    true_value: 0.109
    true_std: 0.005
    value_gap_source_arxiv: '2406.09291'
    value_gap_source_title: A Flexible, Equivariant Framework for Subgraph GNNs via
      Graph Products and Graph Coarsening
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 198
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.109
    sort_std: 0.005
    is_best: false
  - model: PL
    model_key: pl
    model_plain: PL
    value: 0.12
    std: 0.003
    paper_value: 0.12
    paper_std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Bevilacqua et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 208
    true_value: 0.12
    true_std: 0.003
    value_gap_source_arxiv: '2406.09291'
    value_gap_source_title: A Flexible, Equivariant Framework for Subgraph GNNs via
      Graph Products and Graph Coarsening
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.12
    sort_std: 0.003
    is_best: false
  - model: Random
    model_key: random
    model_plain: Random
    value: 0.131
    std: 0.005
    paper_value: 0.131
    paper_std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Kong et al. 2024
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 220
    true_value: 0.131
    true_std: 0.005
    value_gap_source_arxiv: '2406.09291'
    value_gap_source_title: A Flexible, Equivariant Framework for Subgraph GNNs via
      Graph Products and Graph Coarsening
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 220
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.131
    sort_std: 0.005
    is_best: false
  - model: OSAN
    model_key: osan
    model_plain: OSAN
    value: 0.177
    std: 0.016
    paper_value: 0.177
    paper_std: 0.016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Qian et al. 2022
    variant_inference_reason: 'dataset: exact match'
    date: Jun 2024
    date_display: Jun 2024
    date_iso: 2024-06
    global_rank: 236
    true_value: 0.154
    true_std: 0.008
    value_gap_source_arxiv: '2402.08450'
    value_gap_source_title: 'Subgraphormer: Unifying Subgraph GNNs and Graph Transformers
      via Graph Products'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.022999999999999993
    value_note: ''
    paper_rank: 247
    rank_delta: 11
    rank_delta_abs: 11
    rank_delta_direction: worse
    sort_value: 0.154
    sort_std: 0.008
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
single_proposed_model: CS-GNN
main_figure: /figures/2406.09291/main_figure.png
---

