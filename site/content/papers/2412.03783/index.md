---
title: 'Expressivity of Representation Learning on Continuous-Time Dynamic Graphs:
  An Information-Flow Centric Review'
arxiv_id: '2412.03783'
authors: []
published_date: Dec 2024
abstract: Graphs are ubiquitous in real-world applications, ranging from social networks
  to biological systems, and have inspired the development of Graph Neural Networks
  (GNNs) for learning expressive representations. While most research has centered
  on static graphs, many real-world scenarios involve dynamic, temporally evolving
  graphs, motivating the need for Continuous-Time Dynamic Graph (CTDG) models. This
  paper provides a comprehensive review of Graph Representation Learning (GRL) on
  CTDGs with a focus on Self-Supervised Representation Learning (SSRL). We introduce
  a novel theoretical framework that analyzes the expressivity of CTDG models through
  an Information-Flow (IF) lens, quantifying their ability to propagate and encode
  temporal and structural information. Leveraging this framework, we categorize existing
  CTDG methods based on their suitability for different graph types and application
  scenarios. Within the same scope, we examine the design of SSRL methods tailored
  to CTDGs, such as predictive and contrastive approaches, highlighting their potential
  to mitigate the reliance on labeled data. Empirical evaluations on synthetic and
  real-world datasets validate our theoretical insights, demonstrating the strengths
  and limitations of various methods across long-range, bi-partite and community-based
  graphs. This work offers both a theoretical foundation and practical guidance for
  selecting and developing CTDG models, advancing the understanding of GRL in dynamic
  settings.
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: true
proposed_models:
- CTAN
mrr: 0.1667
results:
- &id001
  dataset: ogbl-wikikg2
  rows:
  - model: DyGFormer
    value: 0.7983
    std: 0.0042
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: TCL
    value: 0.7811
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.9
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: CAWN
    value: 0.7304
    std: 0.006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 4.0
    arxiv_id: '2406.02740'
    title: Long Range Propagation on Continuous-Time Dynamic Graphs
    date: '2024-06-04'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: CTAN
    value: 0.611
    std: 0.011
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: TGN
    value: 0.577
    std: 0.015
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 5
    is_best: false
  - model: TGAT
    value: 0.282
    std: 0.022
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 18
    is_best: false
  - model: DyRep
    value: 0.263
    std: 0.005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 21
    is_best: false
  - model: JODIE
    value: 0.261
    std: 0.123
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 13
    is_best: false
  metric: MRR
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
single_proposed_model: CTAN
main_figure: /figures/2412.03783/main_figure.png
---

