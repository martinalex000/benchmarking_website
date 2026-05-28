---
title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
arxiv_id: '2603.00599'
source_url: ''
authors: []
published_date: Mar 2026
published_date_iso: 2026-03
abstract: 'Abstract. Hypergraphs are the natural description of higher-order interactions
  among objects, widely applied in social network analysis, cross-modal retrieval,
  etc. Hypergraph Neural Networks (HGNNs) have become the dominant solution for learning
  on hypergraphs. Traditional HGNNs are extended from message passing graph neural
  networks, following the homophily assumption, and thus struggle with the prevalent
  heterophilic hypergraphs that call for long-range dependence modeling. Existing
  solutions enlarge the message flow through the hypergraph bottleneck, mitigating
  the oversquashing issue and capturing long-range dependence. However, they often
  accelerate the loss of representation distinguishability in the repeated aggregations,
  leading to oversmoothing. This dilemma motivates an interesting question: Can we
  develop a unified mechanism that is agnostic to both homophilic and heterophilic
  hypergraphs? In this paper, we achieve the best of both worlds through the lens
  of Riemannian geometry, which provides the potential to adjust the message passing
  behavior in different regions. The key insight lies in the connection between oversquashing
  and hypergraph bottleneck within the framework of Riemannian manifold heat flow.
  Building on this, we propose the novel idea of locally adapting the bottlenecks
  of different subhypergraphs. The core innovation of the proposed mechanism is the
  design of an adaptive local (heat) exchanger. Specifically, it captures the rich
  long-range dependencies via the Robin condition, and preserves the representation
  distinguishability via source terms, thereby enabling heterophily-agnostic message
  passing with theoretical guarantees. Based on this theoretical foundation, we present
  a novel H eat- E xchanger with A daptive L ocality for Hypergraph Neural Network
  (HealHGNN), designed as a node-hyperedge bidirectional systems with linear complexity
  in the number of nodes and hyperedges. Extensive experiments on both homophilic
  and heterophilic cases show that HealHGNN achieves the state-of-the-art performance.'
codebase_url: https://github.com/Mingzhang21/HealHGNN
extraction_model: qwen3.6-35b-a3b
has_results: true
paper_type: method
proposed_models:
- HealHGNN
mrr: 0.0125
adjusted_mrr: 0.0125
mrr_dataset_count: 3
benchmark_categories:
- Classic
- Hypergraph Benchmarks
- Heterogeneous Graph Benchmarks
task_categories:
- node_classification
experiment_scopes:
- node-level
results:
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
    model_key: fagcn
    model_plain: FAGCN
    value: 0.8237
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2210.07606'
    title: Revisiting Heterophily For Graph Neural Networks
    date: Oct 2022
    date_display: Oct 2022
    date_iso: 2022-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.8237
    sort_std: 0.0146
    is_best: true
  - model: ANS-GT-AnchorGT
    model_key: ans-gt-anchorgt
    model_plain: ANS-GT-AnchorGT
    value: 0.8201
    std: 0.0021
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2405.03481'
    title: 'AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph
      Transformers'
    date: May 2024
    date_display: May 2024
    date_iso: 2024-05
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.8201
    sort_std: 0.0021
    is_best: true
  - model: GrokFormer
    model_key: grokformer
    model_plain: GrokFormer
    value: 0.8192
    std: 0.0125
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2411.17296'
    title: 'GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers'
    date: Nov 26, 2024
    date_display: Nov 2024
    date_iso: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.8192
    sort_std: 0.0125
    is_best: true
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.7456
    std: 0.0116
    paper_value: 0.7456
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 93
    true_value: 0.7456
    true_std: 0.0116
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 93
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7456
    sort_std: 0.0116
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.6245
    std: 0.0116
    paper_value: 0.6245
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 181
    true_value: 0.6245
    true_std: 0.0116
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 181
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6245
    sort_std: 0.0116
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Congress
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.9345
    std: 0.0079
    paper_value: 0.9345
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 1
    true_value: 0.9345
    true_std: 0.0079
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9345
    sort_std: 0.0079
    is_best: true
  - model: ED-HNN
    model_key: ed-hnn
    model_plain: ED-HNN
    value: 0.9328
    std: 0.0059
    paper_value: 0.9328
    paper_std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.9328
    true_std: 0.0059
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9328
    sort_std: 0.0059
    is_best: true
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.9255
    std: 0.0103
    paper_value: 0.9255
    paper_std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 3
    true_value: 0.9255
    true_std: 0.0103
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9255
    sort_std: 0.0103
    is_best: true
  - model: Deep-HGNN
    model_key: deep-hgnn
    model_plain: Deep-HGNN
    value: 0.9247
    std: 0.0106
    paper_value: 0.9247
    paper_std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 4
    true_value: 0.9247
    true_std: 0.0106
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9247
    sort_std: 0.0106
    is_best: true
  - model: UniGCNII
    model_key: unigcnii
    model_plain: UniGCNII
    value: 0.9243000000000001
    std: 0.0070999999999999995
    paper_value: 0.9243000000000001
    paper_std: 0.0070999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 5
    true_value: 0.9243000000000001
    true_std: 0.0070999999999999995
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9243000000000001
    sort_std: 0.0070999999999999995
    is_best: true
  - model: AllSetTransformer
    model_key: allsettransformer
    model_plain: AllSetTransformer
    value: 0.9216
    std: 0.0105
    paper_value: 0.9216
    paper_std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 6
    true_value: 0.9216
    true_std: 0.0105
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9216
    sort_std: 0.0105
    is_best: true
  - model: SheafHyperGNN
    model_key: sheafhypergnn
    model_plain: SheafHyperGNN
    value: 0.9181
    std: 0.016
    paper_value: 0.9181
    paper_std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 7
    true_value: 0.9181
    true_std: 0.016
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9181
    sort_std: 0.016
    is_best: true
  - model: AllDeepSets
    model_key: alldeepsets
    model_plain: AllDeepSets
    value: 0.9179999999999999
    std: 0.015300000000000001
    paper_value: 0.9179999999999999
    paper_std: 0.015300000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 8
    true_value: 0.9179999999999999
    true_std: 0.015300000000000001
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9179999999999999
    sort_std: 0.015300000000000001
    is_best: true
  - model: HNHN
    model_key: hnhn
    model_plain: HNHN
    value: 0.9089
    std: 0.0031
    paper_value: 0.9089
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 9
    true_value: 0.9089
    true_std: 0.0031
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9089
    sort_std: 0.0031
    is_best: false
  - model: HCHA
    model_key: hcha
    model_plain: HCHA
    value: 0.9043000000000001
    std: 0.012
    paper_value: 0.9043000000000001
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PR 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 10
    true_value: 0.9043000000000001
    true_std: 0.012
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9043000000000001
    sort_std: 0.012
    is_best: false
  - model: PhenomNN
    model_key: phenomnn
    model_plain: PhenomNN
    value: 0.8824
    std: 0.0147
    paper_value: 0.8824
    paper_std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 11
    true_value: 0.8824
    true_std: 0.0147
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8824
    sort_std: 0.0147
    is_best: false
  - model: HyperGCN
    model_key: hypergcn
    model_plain: HyperGCN
    value: 0.8743000000000001
    std: 0.0146
    paper_value: 0.8743000000000001
    paper_std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 12
    true_value: 0.8743000000000001
    true_std: 0.0146
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8743000000000001
    sort_std: 0.0146
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
  dataset: Cora
  rows:
  - model: TRIGON
    model_key: trigon
    model_plain: TRIGON
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9170999999999999
    sort_std: 0.0029
    is_best: true
  - model: DR
    model_key: dr
    model_plain: DR
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
    date_display: Aug 2025
    date_iso: 2025-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9139
    sort_std: 0.0024
    is_best: true
  - model: LLP
    model_key: llp
    model_plain: LLP
    value: 0.8995
    std: 0.0201
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.18739'
    title: 'Beyond Message Passing: Neural Graph Pattern Machine'
    date: Jan 30, 2025
    date_display: Jan 2025
    date_iso: '2025-01-30'
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.8995
    sort_std: 0.0201
    is_best: true
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.748
    std: 0.011000000000000001
    paper_value: 0.748
    paper_std: 0.011000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 161
    true_value: 0.793
    true_std: 0.0051
    value_gap_source_arxiv: '2309.04082'
    value_gap_source_title: 'Curve Your Attention: Mixed-Curvature Transformers for
      Graph Representation Learning'
    value_gap_source_is_current_paper: false
    has_value_gap: true
    has_value_note: false
    value_gap: 0.04500000000000004
    value_note: ''
    paper_rank: 200
    rank_delta: 39
    rank_delta_abs: 39
    rank_delta_direction: worse
    sort_value: 0.793
    sort_std: 0.0051
    is_best: false
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.7506
    std: 0.0116
    paper_value: 0.7506
    paper_std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 199
    true_value: 0.7506
    true_std: 0.0116
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 199
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7506
    sort_std: 0.0116
    is_best: false
  - model: FrameHGNN
    model_key: framehgnn
    model_plain: FrameHGNN
    value: 0.7472
    std: 0.021
    paper_value: 0.7472
    paper_std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2025
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 201
    true_value: 0.7472
    true_std: 0.021
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 201
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7472
    sort_std: 0.021
    is_best: false
  - model: SheafHyperGNN
    model_key: sheafhypergnn
    model_plain: SheafHyperGNN
    value: 0.7471
    std: 0.0123
    paper_value: 0.7471
    paper_std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 202
    true_value: 0.7471
    true_std: 0.0123
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 202
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7471
    sort_std: 0.0123
    is_best: false
  - model: PhenomNN
    model_key: phenomnn
    model_plain: PhenomNN
    value: 0.7445
    std: 0.0096
    paper_value: 0.7445
    paper_std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 204
    true_value: 0.7445
    true_std: 0.0096
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 204
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7445
    sort_std: 0.0096
    is_best: false
  - model: Deep-HGNN
    model_key: deep-hgnn
    model_plain: Deep-HGNN
    value: 0.7406999999999999
    std: 0.016399999999999998
    paper_value: 0.7406999999999999
    paper_std: 0.016399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 205
    true_value: 0.7406999999999999
    true_std: 0.016399999999999998
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 205
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7406999999999999
    sort_std: 0.016399999999999998
    is_best: false
  - model: ED-HNN
    model_key: ed-hnn
    model_plain: ED-HNN
    value: 0.737
    std: 0.0138
    paper_value: 0.737
    paper_std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 208
    true_value: 0.737
    true_std: 0.0138
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 208
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.737
    sort_std: 0.0138
    is_best: false
  - model: AllSetTransformer
    model_key: allsettransformer
    model_plain: AllSetTransformer
    value: 0.7308
    std: 0.012
    paper_value: 0.7308
    paper_std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 213
    true_value: 0.7308
    true_std: 0.012
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 213
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7308
    sort_std: 0.012
    is_best: false
  - model: UniGCNII
    model_key: unigcnii
    model_plain: UniGCNII
    value: 0.7304999999999999
    std: 0.022099999999999998
    paper_value: 0.7304999999999999
    paper_std: 0.022099999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 214
    true_value: 0.7304999999999999
    true_std: 0.022099999999999998
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 214
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7304999999999999
    sort_std: 0.022099999999999998
    is_best: false
  - model: HyperGCN
    model_key: hypergcn
    model_plain: HyperGCN
    value: 0.7276
    std: 0.011200000000000002
    paper_value: 0.7276
    paper_std: 0.011200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 216
    true_value: 0.7276
    true_std: 0.011200000000000002
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 216
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7276
    sort_std: 0.011200000000000002
    is_best: false
  - model: HNHN
    model_key: hnhn
    model_plain: HNHN
    value: 0.7264
    std: 0.015700000000000002
    paper_value: 0.7264
    paper_std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 220
    true_value: 0.7264
    true_std: 0.015700000000000002
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 220
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7264
    sort_std: 0.015700000000000002
    is_best: false
  - model: HCHA
    model_key: hcha
    model_plain: HCHA
    value: 0.7242000000000001
    std: 0.014199999999999999
    paper_value: 0.7242000000000001
    paper_std: 0.014199999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PR 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 225
    true_value: 0.7242000000000001
    true_std: 0.014199999999999999
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 225
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7242000000000001
    sort_std: 0.014199999999999999
    is_best: false
  - model: AllDeepSets
    model_key: alldeepsets
    model_plain: AllDeepSets
    value: 0.7082999999999999
    std: 0.0163
    paper_value: 0.7082999999999999
    paper_std: 0.0163
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 239
    true_value: 0.7082999999999999
    true_std: 0.0163
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 239
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7082999999999999
    sort_std: 0.0163
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Cora-CA
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.8478
    std: 0.015700000000000002
    paper_value: 0.8478
    paper_std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 1
    true_value: 0.8478
    true_std: 0.015700000000000002
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8478
    sort_std: 0.015700000000000002
    is_best: true
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.7864
    std: 0.0165
    paper_value: 0.7864
    paper_std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.7864
    true_std: 0.0165
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7864
    sort_std: 0.0165
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    model_key: unigcnii (hodge h-20-lape depth 2)
    model_plain: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7635
    std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.7635
    sort_std: 0.0108
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    model_key: unigcnii (no encodings depth 2)
    model_plain: UniGCNII (no encodings depth 2)
    value: 0.7634
    std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    sort_value: 0.7634
    sort_std: 0.0112
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    model_key: unigcnii (h-19-rwpee ee depth 2)
    model_plain: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7631
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information in Relational Learning
    date: Feb 2025
    date_display: Feb 2025
    date_iso: 2025-02
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    sort_value: 0.7631
    sort_std: 0.0115
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: DBLP
  rows:
  - model: HGSL
    model_key: hgsl
    model_plain: HGSL
    value: 0.9249
    std: 0.0035
    metric: Micro-F1
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.9249
    sort_std: 0.0035
    is_best: true
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.9198000000000001
    std: 0.0031
    paper_value: 0.9198000000000001
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9198000000000001
    sort_std: 0.0031
    is_best: true
  - model: ED-HNN
    model_key: ed-hnn
    model_plain: ED-HNN
    value: 0.919
    std: 0.0019
    paper_value: 0.919
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.919
    sort_std: 0.0019
    is_best: false
  - model: PhenomNN
    model_key: phenomnn
    model_plain: PhenomNN
    value: 0.9186
    std: 0.0022
    paper_value: 0.9186
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9186
    sort_std: 0.0022
    is_best: false
  - model: SUBLIME
    model_key: sublime
    model_plain: SUBLIME
    value: 0.9182
    std: 0.0027
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.9182
    sort_std: 0.0027
    is_best: false
  - model: Deep-HGNN
    model_key: deep-hgnn
    model_plain: Deep-HGNN
    value: 0.9176000000000001
    std: 0.0028000000000000004
    paper_value: 0.9176000000000001
    paper_std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9176000000000001
    sort_std: 0.0028000000000000004
    is_best: false
  - model: UniGCNII
    model_key: unigcnii
    model_plain: UniGCNII
    value: 0.9168999999999999
    std: 0.0019
    paper_value: 0.9168999999999999
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9168999999999999
    sort_std: 0.0019
    is_best: false
  - model: SheafHyperGNN
    model_key: sheafhypergnn
    model_plain: SheafHyperGNN
    value: 0.9159
    std: 0.0024
    paper_value: 0.9159
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9159
    sort_std: 0.0024
    is_best: false
  - model: AllSetTransformer
    model_key: allsettransformer
    model_plain: AllSetTransformer
    value: 0.9153
    std: 0.0023
    paper_value: 0.9153
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9153
    sort_std: 0.0023
    is_best: false
  - model: GTN
    model_key: gtn
    model_plain: GTN
    value: 0.9148
    std: 0.0039
    metric: Micro-F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2310.05174'
    title: 'GSLB: The Graph Structure Learning Benchmark'
    date: Oct 2023
    date_display: Oct 2023
    date_iso: 2023-10
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.9148
    sort_std: 0.0039
    is_best: false
  - model: AllDeepSets
    model_key: alldeepsets
    model_plain: AllDeepSets
    value: 0.9127
    std: 0.0027
    paper_value: 0.9127
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9127
    sort_std: 0.0027
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.9120999999999999
    std: 0.0037
    paper_value: 0.9120999999999999
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9120999999999999
    sort_std: 0.0037
    is_best: false
  - model: HCHA
    model_key: hcha
    model_plain: HCHA
    value: 0.9092
    std: 0.0022
    paper_value: 0.9092
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pattern Recognition 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.9092
    sort_std: 0.0022
    is_best: false
  - model: HyperGCN
    model_key: hypergcn
    model_plain: HyperGCN
    value: 0.8998
    std: 0.0043
    paper_value: 0.8998
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.8998
    sort_std: 0.0043
    is_best: false
  - model: HNHN
    model_key: hnhn
    model_plain: HNHN
    value: 0.8678
    std: 0.0029
    paper_value: 0.8678
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: null
    sort_value: 0.8678
    sort_std: 0.0029
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id006
  dataset: DBLP-CA
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.9198000000000001
    std: 0.0031
    paper_value: 0.9198000000000001
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 1
    true_value: 0.9198000000000001
    true_std: 0.0031
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9198000000000001
    sort_std: 0.0031
    is_best: true
  - model: ED-HNN
    model_key: ed-hnn
    model_plain: ED-HNN
    value: 0.919
    std: 0.0019
    paper_value: 0.919
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.919
    true_std: 0.0019
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.919
    sort_std: 0.0019
    is_best: true
  - model: PhenomNN
    model_key: phenomnn
    model_plain: PhenomNN
    value: 0.9186
    std: 0.0022
    paper_value: 0.9186
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 3
    true_value: 0.9186
    true_std: 0.0022
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9186
    sort_std: 0.0022
    is_best: true
  - model: Deep-HGNN
    model_key: deep-hgnn
    model_plain: Deep-HGNN
    value: 0.9176000000000001
    std: 0.0028000000000000004
    paper_value: 0.9176000000000001
    paper_std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 4
    true_value: 0.9176000000000001
    true_std: 0.0028000000000000004
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9176000000000001
    sort_std: 0.0028000000000000004
    is_best: true
  - model: UniGCNII
    model_key: unigcnii
    model_plain: UniGCNII
    value: 0.9168999999999999
    std: 0.0019
    paper_value: 0.9168999999999999
    paper_std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 5
    true_value: 0.9168999999999999
    true_std: 0.0019
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9168999999999999
    sort_std: 0.0019
    is_best: true
  - model: SheafHyperGNN
    model_key: sheafhypergnn
    model_plain: SheafHyperGNN
    value: 0.9159
    std: 0.0024
    paper_value: 0.9159
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 6
    true_value: 0.9159
    true_std: 0.0024
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9159
    sort_std: 0.0024
    is_best: true
  - model: AllSetTransformer
    model_key: allsettransformer
    model_plain: AllSetTransformer
    value: 0.9153
    std: 0.0023
    paper_value: 0.9153
    paper_std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 7
    true_value: 0.9153
    true_std: 0.0023
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9153
    sort_std: 0.0023
    is_best: true
  - model: AllDeepSets
    model_key: alldeepsets
    model_plain: AllDeepSets
    value: 0.9127
    std: 0.0027
    paper_value: 0.9127
    paper_std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 8
    true_value: 0.9127
    true_std: 0.0027
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9127
    sort_std: 0.0027
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.9120999999999999
    std: 0.0037
    paper_value: 0.9120999999999999
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 9
    true_value: 0.9120999999999999
    true_std: 0.0037
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9120999999999999
    sort_std: 0.0037
    is_best: false
  - model: HCHA
    model_key: hcha
    model_plain: HCHA
    value: 0.9092
    std: 0.0022
    paper_value: 0.9092
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pattern Recognition 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 10
    true_value: 0.9092
    true_std: 0.0022
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.9092
    sort_std: 0.0022
    is_best: false
  - model: HyperGCN
    model_key: hypergcn
    model_plain: HyperGCN
    value: 0.8998
    std: 0.0043
    paper_value: 0.8998
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 11
    true_value: 0.8998
    true_std: 0.0043
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8998
    sort_std: 0.0043
    is_best: false
  - model: HNHN
    model_key: hnhn
    model_plain: HNHN
    value: 0.8678
    std: 0.0029
    paper_value: 0.8678
    paper_std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 12
    true_value: 0.8678
    true_std: 0.0029
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 12
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8678
    sort_std: 0.0029
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: House
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.7718
    std: 0.0235
    paper_value: 0.7718
    paper_std: 0.0235
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 1
    true_value: 0.7718
    true_std: 0.0235
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7718
    sort_std: 0.0235
    is_best: true
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.6139
    std: 0.0296
    paper_value: 0.6139
    paper_std: 0.0296
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.6139
    true_std: 0.0296
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6139
    sort_std: 0.0296
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: CO
    model_key: co
    model_plain: CO
    value: 0.9484
    std: 0.0004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    sort_value: 0.9484
    sort_std: 0.0004
    is_best: true
  - model: HN-1
    model_key: hn-1
    model_plain: HN-1
    value: 0.948
    std: 0.0017
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    sort_value: 0.948
    sort_std: 0.0017
    is_best: true
  - model: MLP
    model_key: mlp
    model_plain: MLP
    value: 0.9476
    std: 0.001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2511.16767'
    title: 'When Structure Doesn’t Help: LLMs Do Not Read Text-Attributed Graphs as
      Effectively as We Expected'
    date: Nov 2025
    date_display: Nov 2025
    date_iso: 2025-11
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    sort_value: 0.9476
    sort_std: 0.001
    is_best: true
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.888
    std: 0.0031
    paper_value: 0.888
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 46
    true_value: 0.888
    true_std: 0.0031
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 46
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.888
    sort_std: 0.0031
    is_best: false
  - model: FrameHGNN
    model_key: framehgnn
    model_plain: FrameHGNN
    value: 0.8873000000000001
    std: 0.0042
    paper_value: 0.8873000000000001
    paper_std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2025
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 50
    true_value: 0.8873000000000001
    true_std: 0.0042
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 50
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8873000000000001
    sort_std: 0.0042
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.8847
    std: 0.004699999999999999
    paper_value: 0.8847
    paper_std: 0.004699999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 57
    true_value: 0.8847
    true_std: 0.004699999999999999
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 57
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8847
    sort_std: 0.004699999999999999
    is_best: false
  - model: SheafHyperGNN
    model_key: sheafhypergnn
    model_plain: SheafHyperGNN
    value: 0.8768
    std: 0.006
    paper_value: 0.8768
    paper_std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 77
    true_value: 0.8768
    true_std: 0.006
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 77
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8768
    sort_std: 0.006
    is_best: false
  - model: AllSetTransformer
    model_key: allsettransformer
    model_plain: AllSetTransformer
    value: 0.8765999999999999
    std: 0.0043
    paper_value: 0.8765999999999999
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 78
    true_value: 0.8765999999999999
    true_std: 0.0043
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 78
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8765999999999999
    sort_std: 0.0043
    is_best: false
  - model: ED-HNN
    model_key: ed-hnn
    model_plain: ED-HNN
    value: 0.8758
    std: 0.006500000000000001
    paper_value: 0.8758
    paper_std: 0.006500000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 80
    true_value: 0.8758
    true_std: 0.006500000000000001
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 80
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8758
    sort_std: 0.006500000000000001
    is_best: false
  - model: Deep-HGNN
    model_key: deep-hgnn
    model_plain: Deep-HGNN
    value: 0.8742
    std: 0.0022
    paper_value: 0.8742
    paper_std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 82
    true_value: 0.8742
    true_std: 0.0022
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 82
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8742
    sort_std: 0.0022
    is_best: false
  - model: UniGCNII
    model_key: unigcnii
    model_plain: UniGCNII
    value: 0.8731
    std: 0.0045000000000000005
    paper_value: 0.8731
    paper_std: 0.0045000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 86
    true_value: 0.8731
    true_std: 0.0045000000000000005
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 86
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8731
    sort_std: 0.0045000000000000005
    is_best: false
  - model: AllDeepSets
    model_key: alldeepsets
    model_plain: AllDeepSets
    value: 0.8704000000000001
    std: 0.0052
    paper_value: 0.8704000000000001
    paper_std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 89
    true_value: 0.8704000000000001
    true_std: 0.0052
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 89
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8704000000000001
    sort_std: 0.0052
    is_best: false
  - model: HCHA
    model_key: hcha
    model_plain: HCHA
    value: 0.8456
    std: 0.0031
    paper_value: 0.8456
    paper_std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pattern Recognition 2021
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 102
    true_value: 0.8456
    true_std: 0.0031
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 102
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8456
    sort_std: 0.0031
    is_best: false
  - model: HNHN
    model_key: hnhn
    model_plain: HNHN
    value: 0.8421
    std: 0.0064
    paper_value: 0.8421
    paper_std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 103
    true_value: 0.8421
    true_std: 0.0064
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 103
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8421
    sort_std: 0.0064
    is_best: false
  - model: HyperGCN
    model_key: hypergcn
    model_plain: HyperGCN
    value: 0.8284
    std: 0.0067
    paper_value: 0.8284
    paper_std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 105
    true_value: 0.8284
    true_std: 0.0067
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 105
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.8284
    sort_std: 0.0067
    is_best: false
  - model: PhenomNN
    model_key: phenomnn
    model_plain: PhenomNN
    value: 0.7812
    std: 0.0024
    paper_value: 0.7812
    paper_std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 125
    true_value: 0.7812
    true_std: 0.0024
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 125
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7812
    sort_std: 0.0024
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: Senate
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.7606
    std: 0.041299999999999996
    paper_value: 0.7606
    paper_std: 0.041299999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 1
    true_value: 0.7606
    true_std: 0.041299999999999996
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.7606
    sort_std: 0.041299999999999996
    is_best: true
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.48590000000000005
    std: 0.0452
    paper_value: 0.48590000000000005
    paper_std: 0.0452
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.48590000000000005
    true_std: 0.0452
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.48590000000000005
    sort_std: 0.0452
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Walmart
  rows:
  - model: HealHGNN
    model_key: healhgnn
    model_plain: HealHGNN
    value: 0.6822
    std: 0.005600000000000001
    paper_value: 0.6822
    paper_std: 0.005600000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 1
    true_value: 0.6822
    true_std: 0.005600000000000001
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 1
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6822
    sort_std: 0.005600000000000001
    is_best: true
  - model: ED-HNN
    model_key: ed-hnn
    model_plain: ED-HNN
    value: 0.6679
    std: 0.0040999999999999995
    paper_value: 0.6679
    paper_std: 0.0040999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR22-edhnn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 2
    true_value: 0.6679
    true_std: 0.0040999999999999995
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 2
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6679
    sort_std: 0.0040999999999999995
    is_best: false
  - model: AllSetTransformer
    model_key: allsettransformer
    model_plain: AllSetTransformer
    value: 0.6546
    std: 0.0025
    paper_value: 0.6546
    paper_std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: iclr22-alldeepsets-allsettrans
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 3
    true_value: 0.6546
    true_std: 0.0025
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 3
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6546
    sort_std: 0.0025
    is_best: false
  - model: HGNN
    model_key: hgnn
    model_plain: HGNN
    value: 0.6517000000000001
    std: 0.0079
    paper_value: 0.6517000000000001
    paper_std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI19-hgnn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 4
    true_value: 0.6517000000000001
    true_std: 0.0079
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 4
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6517000000000001
    sort_std: 0.0079
    is_best: false
  - model: AllDeepSets
    model_key: alldeepsets
    model_plain: AllDeepSets
    value: 0.6455
    std: 0.0033
    paper_value: 0.6455
    paper_std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: iclr22-alldeepsets-allsettrans
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 5
    true_value: 0.6455
    true_std: 0.0033
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 5
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6455
    sort_std: 0.0033
    is_best: false
  - model: PhenomNN
    model_key: phenomnn
    model_plain: PhenomNN
    value: 0.6343
    std: 0.0043
    paper_value: 0.6343
    paper_std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML24-PhenomNN
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 6
    true_value: 0.6343
    true_std: 0.0043
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 6
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6343
    sort_std: 0.0043
    is_best: false
  - model: HCHA
    model_key: hcha
    model_plain: HCHA
    value: 0.6235
    std: 0.0026
    paper_value: 0.6235
    paper_std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PR21-hcha
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 7
    true_value: 0.6235
    true_std: 0.0026
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 7
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.6235
    sort_std: 0.0026
    is_best: false
  - model: Deep-HGNN
    model_key: deep-hgnn
    model_plain: Deep-HGNN
    value: 0.5864
    std: 0.0074
    paper_value: 0.5864
    paper_std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arxiv22-deephgnn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 8
    true_value: 0.5864
    true_std: 0.0074
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 8
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5864
    sort_std: 0.0074
    is_best: false
  - model: UniGCNII
    model_key: unigcnii
    model_plain: UniGCNII
    value: 0.5445
    std: 0.0037
    paper_value: 0.5445
    paper_std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arxiv21-hgnn-uniGCNII
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 9
    true_value: 0.5445
    true_std: 0.0037
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 9
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5445
    sort_std: 0.0037
    is_best: false
  - model: HNHN
    model_key: hnhn
    model_plain: HNHN
    value: 0.5118
    std: 0.0034999999999999996
    paper_value: 0.5118
    paper_std: 0.0034999999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arxiv20-hnhn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 10
    true_value: 0.5118
    true_std: 0.0034999999999999996
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 10
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.5118
    sort_std: 0.0034999999999999996
    is_best: false
  - model: HyperGCN
    model_key: hypergcn
    model_plain: HyperGCN
    value: 0.4874
    std: 0.0281
    paper_value: 0.4874
    paper_std: 0.0281
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    variant_inference_reason: ''
    date: Mar 2026
    date_display: Mar 2026
    date_iso: 2026-03
    global_rank: 11
    true_value: 0.4874
    true_std: 0.0281
    value_gap_source_arxiv: '2603.00599'
    value_gap_source_title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian
      Local Exchanger
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 11
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.4874
    sort_std: 0.0281
    is_best: false
  metric: Accuracy
  higher_is_better: true
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
  - *id002
  - *id003
- benchmark: Hypergraph Benchmarks
  datasets:
  - *id004
  - *id005
  - *id006
  - *id007
  - *id008
  - *id009
- benchmark: Heterogeneous Graph Benchmarks
  datasets:
  - *id010
single_proposed_model: HealHGNN
---

