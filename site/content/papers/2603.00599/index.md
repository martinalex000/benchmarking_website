---
title: Heterophily-Agnostic Hypergraph Neural Networks with Riemannian Local Exchanger
arxiv_id: '2603.00599'
authors: []
published_date: Mar 2026
abstract: 'Abstract. Hypergraphs are the natural description of higher-order interactions among objects,
  widely applied in social network analysis, cross-modal retrieval, etc. Hypergraph Neural Networks (HGNNs)
  have become the dominant solution for learning on hypergraphs. Traditional HGNNs are extended from message
  passing graph neural networks, following the homophily assumption, and thus struggle with the prevalent
  heterophilic hypergraphs that call for long-range dependence modeling. Existing solutions enlarge the
  message flow through the hypergraph bottleneck, mitigating the oversquashing issue and capturing long-range
  dependence. However, they often accelerate the loss of representation distinguishability in the repeated
  aggregations, leading to oversmoothing. This dilemma motivates an interesting question: Can we develop
  a unified mechanism that is agnostic to both homophilic and heterophilic hypergraphs? In this paper,
  we achieve the best of both worlds through the lens of Riemannian geometry, which provides the potential
  to adjust the message passing behavior in different regions. The key insight lies in the connection
  between oversquashing and hypergraph bottleneck within the framework of Riemannian manifold heat flow.
  Building on this, we propose the novel idea of locally adapting the bottlenecks of different subhypergraphs.
  The core innovation of the proposed mechanism is the design of an adaptive local (heat) exchanger. Specifically,
  it captures the rich long-range dependencies via the Robin condition, and preserves the representation
  distinguishability via source terms, thereby enabling heterophily-agnostic message passing with theoretical
  guarantees. Based on this theoretical foundation, we present a novel H eat- E xchanger with A daptive
  L ocality for Hypergraph Neural Network (HealHGNN), designed as a node-hyperedge bidirectional systems
  with linear complexity in the number of nodes and hyperedges. Extensive experiments on both homophilic
  and heterophilic cases show that HealHGNN achieves the state-of-the-art performance.'
codebase_url: https://github.com/Mingzhang21/HealHGNN
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- HealHGNN
mrr: 0.0125
results:
- &id002
  dataset: CiteSeer
  rows:
  - model: FAGCN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: ANS-GT-AnchorGT
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GrokFormer
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
    date: '2024-11-26'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: HealHGNN
    value: 0.7456
    std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 93
    is_best: false
  - model: HGNN
    value: 0.6245
    std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    global_rank: 178
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id005
  dataset: Congress
  rows:
  - model: HealHGNN
    value: 0.9345
    std: 0.0079
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
  - model: ED-HNN
    value: 0.9328
    std: 0.0059
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 2
    is_best: true
  - model: HGNN
    value: 0.9255
    std: 0.0103
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    global_rank: 3
    is_best: true
  - model: Deep-HGNN
    value: 0.9247
    std: 0.0106
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    global_rank: 4
    is_best: true
  - model: UniGCNII
    value: 0.9243000000000001
    std: 0.0070999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    global_rank: 5
    is_best: true
  - model: AllSetTransformer
    value: 0.9216
    std: 0.0105
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 6
    is_best: true
  - model: SheafHyperGNN
    value: 0.9181
    std: 0.016
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    global_rank: 7
    is_best: true
  - model: AllDeepSets
    value: 0.9179999999999999
    std: 0.015300000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 8
    is_best: true
  - model: HNHN
    value: 0.9089
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    global_rank: 9
    is_best: false
  - model: HCHA
    value: 0.9043000000000001
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PR 2021
    global_rank: 10
    is_best: false
  - model: PhenomNN
    value: 0.8824
    std: 0.0147
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    global_rank: 11
    is_best: false
  - model: HyperGCN
    value: 0.8743000000000001
    std: 0.0146
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    global_rank: 12
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id001
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
  - model: HealHGNN
    value: 0.7506
    std: 0.0116
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 197
    is_best: false
  - model: HGNN
    value: 0.748
    std: 0.011000000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    global_rank: 163
    is_best: false
  - model: FrameHGNN
    value: 0.7472
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2025
    global_rank: 199
    is_best: false
  - model: SheafHyperGNN
    value: 0.7471
    std: 0.0123
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    global_rank: 200
    is_best: false
  - model: PhenomNN
    value: 0.7445
    std: 0.0096
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    global_rank: 202
    is_best: false
  - model: Deep-HGNN
    value: 0.7406999999999999
    std: 0.016399999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    global_rank: 203
    is_best: false
  - model: ED-HNN
    value: 0.737
    std: 0.0138
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 206
    is_best: false
  - model: AllSetTransformer
    value: 0.7308
    std: 0.012
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 211
    is_best: false
  - model: UniGCNII
    value: 0.7304999999999999
    std: 0.022099999999999998
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    global_rank: 212
    is_best: false
  - model: HyperGCN
    value: 0.7276
    std: 0.011200000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    global_rank: 214
    is_best: false
  - model: HNHN
    value: 0.7264
    std: 0.015700000000000002
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    global_rank: 218
    is_best: false
  - model: HCHA
    value: 0.7242000000000001
    std: 0.014199999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PR 2021
    global_rank: 223
    is_best: false
  - model: AllDeepSets
    value: 0.7082999999999999
    std: 0.0163
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 235
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id004
  dataset: Cora-CA
  rows:
  - model: HealHGNN
    value: 0.8478
    std: 0.015700000000000002
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
  - model: HGNN
    value: 0.7864
    std: 0.0165
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    global_rank: 2
    is_best: false
  - model: UniGCNII (Hodge H-20-LAPE depth 2)
    value: 0.7635
    std: 0.0108
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: UniGCNII (no encodings depth 2)
    value: 0.7634
    std: 0.0112
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: UniGCNII (H-19-RWPEE EE depth 2)
    value: 0.7631
    std: 0.0115
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.09570'
    title: Enhancing the Utility of Higher-Order Information Relational Learning
    date: Feb 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 5
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id010
  dataset: DBLP
  rows:
  - model: HGSL
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HealHGNN
    value: 0.9198000000000001
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: true
  - model: ED-HNN
    value: 0.919
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: null
    is_best: false
  - model: PhenomNN
    value: 0.9186
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    global_rank: null
    is_best: false
  - model: SUBLIME
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: Deep-HGNN
    value: 0.9176000000000001
    std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    global_rank: null
    is_best: false
  - model: UniGCNII
    value: 0.9168999999999999
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    global_rank: null
    is_best: false
  - model: SheafHyperGNN
    value: 0.9159
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    global_rank: null
    is_best: false
  - model: AllSetTransformer
    value: 0.9153
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: null
    is_best: false
  - model: GTN
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
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: AllDeepSets
    value: 0.9127
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: null
    is_best: false
  - model: HGNN
    value: 0.9120999999999999
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    global_rank: null
    is_best: false
  - model: HCHA
    value: 0.9092
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pattern Recognition 2021
    global_rank: null
    is_best: false
  - model: HyperGCN
    value: 0.8998
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    global_rank: null
    is_best: false
  - model: HNHN
    value: 0.8678
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    global_rank: null
    is_best: false
  metric: Micro-F1
  higher_is_better: true
- &id006
  dataset: DBLP-CA
  rows:
  - model: HealHGNN
    value: 0.9198000000000001
    std: 0.0031
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
  - model: ED-HNN
    value: 0.919
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 2
    is_best: true
  - model: PhenomNN
    value: 0.9186
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    global_rank: 3
    is_best: true
  - model: Deep-HGNN
    value: 0.9176000000000001
    std: 0.0028000000000000004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    global_rank: 4
    is_best: true
  - model: UniGCNII
    value: 0.9168999999999999
    std: 0.0019
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    global_rank: 5
    is_best: true
  - model: SheafHyperGNN
    value: 0.9159
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    global_rank: 6
    is_best: true
  - model: AllSetTransformer
    value: 0.9153
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 7
    is_best: true
  - model: AllDeepSets
    value: 0.9127
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 8
    is_best: false
  - model: HGNN
    value: 0.9120999999999999
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    global_rank: 9
    is_best: false
  - model: HCHA
    value: 0.9092
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pattern Recognition 2021
    global_rank: 10
    is_best: false
  - model: HyperGCN
    value: 0.8998
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    global_rank: 11
    is_best: false
  - model: HNHN
    value: 0.8678
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    global_rank: 12
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id008
  dataset: House
  rows:
  - model: HealHGNN
    value: 0.7718
    std: 0.0235
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
  - model: HGNN
    value: 0.6139
    std: 0.0296
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    global_rank: 2
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id003
  dataset: PubMed
  rows:
  - model: CO
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: HN-1
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: MLP
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
    codebase_url: ''
    uses_external_data: null
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: HealHGNN
    value: 0.888
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: FrameHGNN
    value: 0.8873000000000001
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2025
    global_rank: 50
    is_best: false
  - model: HGNN
    value: 0.8847
    std: 0.004699999999999999
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI 2019
    global_rank: 57
    is_best: false
  - model: SheafHyperGNN
    value: 0.8768
    std: 0.006
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2023
    global_rank: 77
    is_best: false
  - model: AllSetTransformer
    value: 0.8765999999999999
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 78
    is_best: false
  - model: ED-HNN
    value: 0.8758
    std: 0.006500000000000001
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 80
    is_best: false
  - model: Deep-HGNN
    value: 0.8742
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2022
    global_rank: 82
    is_best: false
  - model: UniGCNII
    value: 0.8731
    std: 0.0045000000000000005
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2021
    global_rank: 86
    is_best: false
  - model: AllDeepSets
    value: 0.8704000000000001
    std: 0.0052
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR 2022
    global_rank: 89
    is_best: false
  - model: HCHA
    value: 0.8456
    std: 0.0031
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Pattern Recognition 2021
    global_rank: 102
    is_best: false
  - model: HNHN
    value: 0.8421
    std: 0.0064
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arXiv 2020
    global_rank: 103
    is_best: false
  - model: HyperGCN
    value: 0.8284
    std: 0.0067
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: NeurIPS 2019
    global_rank: 105
    is_best: false
  - model: PhenomNN
    value: 0.7812
    std: 0.0024
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML 2024
    global_rank: 125
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id009
  dataset: Senate
  rows:
  - model: HealHGNN
    value: 0.7606
    std: 0.041299999999999996
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
  - model: HGNN
    value: 0.48590000000000005
    std: 0.0452
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    global_rank: 2
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id007
  dataset: Walmart
  rows:
  - model: HealHGNN
    value: 0.6822
    std: 0.005600000000000001
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
  - model: ED-HNN
    value: 0.6679
    std: 0.0040999999999999995
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICLR22-edhnn
    global_rank: 2
    is_best: false
  - model: AllSetTransformer
    value: 0.6546
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: iclr22-alldeepsets-allsettrans
    global_rank: 3
    is_best: false
  - model: HGNN
    value: 0.6517000000000001
    std: 0.0079
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: AAAI19-hgnn
    global_rank: 4
    is_best: false
  - model: AllDeepSets
    value: 0.6455
    std: 0.0033
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: iclr22-alldeepsets-allsettrans
    global_rank: 5
    is_best: false
  - model: PhenomNN
    value: 0.6343
    std: 0.0043
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ICML24-PhenomNN
    global_rank: 6
    is_best: false
  - model: HCHA
    value: 0.6235
    std: 0.0026
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: PR21-hcha
    global_rank: 7
    is_best: false
  - model: Deep-HGNN
    value: 0.5864
    std: 0.0074
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arxiv22-deephgnn
    global_rank: 8
    is_best: false
  - model: UniGCNII
    value: 0.5445
    std: 0.0037
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arxiv21-hgnn-uniGCNII
    global_rank: 9
    is_best: false
  - model: HNHN
    value: 0.5118
    std: 0.0034999999999999996
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: arxiv20-hnhn
    global_rank: 10
    is_best: false
  - model: HyperGCN
    value: 0.4874
    std: 0.0281
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nips19-hypergcn
    global_rank: 11
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

