---
title: Long Range Graph Benchmark
arxiv_id: '2206.08164'
authors: []
published_date: Jun 2022
abstract: 'Graph Neural Networks (GNNs) that are based on the message passing (MP)
  paradigm generally exchange information between 1-hop neighbors to build node representations
  at each layer. In principle, such networks are not able to capture long-range interactions
  (LRI) that may be desired or necessary for learning a given task on graphs. Recently,
  there has been an increasing interest in development of Transformer-based methods
  for graphs that can consider full node connectivity beyond the original sparse structure,
  thus enabling the modeling of LRI. However, MP-GNNs that simply rely on 1-hop message
  passing often fare better in several existing graph benchmarks when combined with
  positional feature representations, among other innovations, hence limiting the
  perceived utility and ranking of Transformer-like architectures. Here, we present
  the Long Range Graph Benchmark (LRGB) with 5 graph learning datasets: PascalVOC-SP,
  COCO-SP, PCQM-Contact, Peptides-func and Peptides-struct that arguably require LRI
  reasoning to achieve strong performance in a given task. We benchmark both baseline
  GNNs and Graph Transformer networks to verify that the models which capture long-range
  dependencies perform significantly better on these tasks. Therefore, these datasets
  are suitable for benchmarking and exploration of MP-GNNs and Graph Transformer architectures
  that are intended to capture LRI.'
codebase_url: https://github.com/vijaydwivedi75/lrgb
extraction_model: glm-4.7
results:
- dataset: COCO-SP
  rows:
  - model: GCN
    value: 0.2574
    std: 0.0034
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
  - model: GINE
    value: 0.1339
    std: 0.0044
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 3
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.2618
    std: 0.0031
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 3
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.2592
    std: 0.0158
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 3
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.2434
    std: 0.0156
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 3
    source_ref: this paper
  metric: F1
  higher_is_better: true
- dataset: PCQM-Contact
  rows:
  - model: GCN
    value: 0.1288
    std: 0.0013
    metric: Hits@1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 5
    source_ref: this paper
  - model: GCN
    value: 0.8517
    std: 0.0005
    metric: Hits@10
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 5
    source_ref: this paper
  - model: GCN
    value: 0.3808
    std: 0.0006
    metric: Hits@3
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 5
    source_ref: this paper
  - model: GCN
    value: 0.3242
    std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 5
    source_ref: this paper
  - model: GINE
    value: 0.1337
    std: 0.0013
    metric: Hits@1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 5
    source_ref: this paper
  - model: GINE
    value: 0.8147
    std: 0.0062
    metric: Hits@10
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 5
    source_ref: this paper
  - model: GINE
    value: 0.3642
    std: 0.0043
    metric: Hits@3
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 5
    source_ref: this paper
  - model: GINE
    value: 0.318
    std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 5
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.1221
    std: 0.0011
    metric: Hits@1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 5
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.8517
    std: 0.0039
    metric: Hits@10
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 5
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.3679
    std: 0.0033
    metric: Hits@3
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 5
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.3174
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.1355
    std: 0.0017
    metric: Hits@1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.8478
    std: 0.0044
    metric: Hits@10
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.4004
    std: 0.0021
    metric: Hits@3
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.335
    std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.1312
    std: 0.0016
    metric: Hits@1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.855
    std: 0.0024
    metric: Hits@10
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.403
    std: 0.0008
    metric: Hits@3
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 5
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.3341
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 5
    source_ref: this paper
  metric: Hits@1
  higher_is_better: true
- dataset: PascalVOC-SP
  rows:
  - model: GCN
    value: 0.286
    std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
  - model: GINE
    value: 0.1265
    std: 0.0076
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 3
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.2694
    std: 0.0098
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 3
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.323
    std: 0.0039
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 3
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.3216
    std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 3
    source_ref: this paper
  metric: F1
  higher_is_better: true
- dataset: Peptides-func
  rows:
  - model: GCN
    value: 0.6069
    std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
  - model: GINE
    value: 0.5498
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 4
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 4
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.6384
    std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 4
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.6439
    std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 4
    source_ref: this paper
  metric: AP
  higher_is_better: true
- dataset: Peptides-struct
  rows:
  - model: GCN
    value: 0.3357
    std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 4
    source_ref: this paper
  - model: GINE
    value: 0.3547
    std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 4
    source_ref: this paper
  - model: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 4
    source_ref: this paper
  - model: SAN+LapPE
    value: 0.2683
    std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 4
    source_ref: this paper
  - model: SAN+RWSE
    value: 0.2545
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
    table_ref: Table 4
    source_ref: this paper
  metric: MAE
  higher_is_better: false
---

