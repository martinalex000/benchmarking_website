---
title: A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products and
  Graph Coarsening
arxiv_id: '2406.09291'
authors: []
published_date: Jun 2024
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
proposed_models:
- CS-GNN
mrr: 0.0058
results:
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
  - model: Subgraphormer
    value: 0.063
    std: 0.001
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
  - model: GNN-SSWL+
    value: 0.07
    std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: SUN
    value: 0.083
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: GNN (a)
    value: 0.091
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 26
    is_best: false
  - model: DSS-GNN
    value: 0.102
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 24
    is_best: false
  - model: Mag-GNN
    value: 0.106
    std: 0.014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 168
    is_best: false
  - model: CS-GNN
    value: 0.109
    std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1
    source_ref: this paper
    global_rank: 171
    is_best: false
  - model: NGNN
    value: 0.111
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: PL
    value: 0.12
    std: 0.003
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 182
    is_best: false
  - model: Random
    value: 0.131
    std: 0.005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 193
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
    table_ref: Table 1
    source_ref: this paper
    global_rank: 67
    is_best: false
  - model: OSAN
    value: 0.177
    std: 0.016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 210
    is_best: false
  - model: GCN
    value: 0.321
    std: 0.009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 115
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

