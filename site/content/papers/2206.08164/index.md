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
    value: 0.0841
    std: 0.001
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
  - model: GCNII
    value: 0.1404
    std: 0.0011
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 3
    source_ref: this paper
  - model: GatedGCN
    value: 0.2641
    std: 0.0045
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 3
    source_ref: this paper
  - model: GatedGCN+LapPE
    value: 0.2574
    std: 0.0034
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 3
    source_ref: this paper
  metric: F1
  higher_is_better: true
- dataset: PCQM-Contact
  is_multi_metric: true
  rows:
  - model: SAN+LapPE
    metric_values:
    - 0.335
    - 0.1355
    - 0.8478
    - 0.4004
    metric_stds:
    - 0.0003
    - 0.0017
    - 0.0044
    - 0.0021
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
  - model: SAN+RWSE
    metric_values:
    - 0.3341
    - 0.1312
    - 0.855
    - 0.403
    metric_stds:
    - 0.0006
    - 0.0016
    - 0.0024
    - 0.0008
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.468
  - model: GatedGCN+RWSE
    metric_values:
    - 0.3242
    - 0.1288
    - 0.8517
    - 0.3808
    metric_stds:
    - 0.0008
    - 0.0013
    - 0.0005
    - 0.0006
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
  - model: GCN
    metric_values:
    - 0.3234
    - 0.1321
    - 0.8256
    - 0.3791
    metric_stds:
    - 0.0006
    - 0.0007
    - 0.0006
    - 0.0004
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
  - model: GatedGCN
    metric_values:
    - 0.3218
    - 0.1279
    - 0.8433
    - 0.3783
    metric_stds:
    - 0.0011
    - 0.0018
    - 0.0011
    - 0.0004
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
  - model: GINE
    metric_values:
    - 0.318
    - 0.1337
    - 0.8147
    - 0.3642
    metric_stds:
    - 0.0027
    - 0.0013
    - 0.0062
    - 0.0043
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
  - model: Transformer+LapPE
    metric_values:
    - 0.3174
    - 0.1221
    - 0.8517
    - 0.3679
    metric_stds:
    - 0.002
    - 0.0011
    - 0.0039
    - 0.0033
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
  - model: GCNII
    metric_values:
    - 0.3161
    - 0.1325
    - 0.8116
    - 0.3607
    metric_stds:
    - 0.0004
    - 0.0009
    - 0.0009
    - 0.0003
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
  metrics:
  - MRR
  - Hits@1
  - Hits@10
  - Hits@3
  primary_metric: MRR
  higher_is_better: true
- dataset: PascalVOC-SP
  rows:
  - model: GCN
    value: 0.1268
    std: 0.006
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
  - model: GCNII
    value: 0.1698
    std: 0.008
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 3
    source_ref: this paper
  - model: GatedGCN
    value: 0.2873
    std: 0.0219
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 3
    source_ref: this paper
  - model: GatedGCN+LapPE
    value: 0.286
    std: 0.0085
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 3
    source_ref: this paper
  metric: F1
  higher_is_better: true
- dataset: Peptides-func
  rows:
  - model: GCN
    value: 0.593
    std: 0.0023
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
  - model: GCNII
    value: 0.5543
    std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 4
    source_ref: this paper
  - model: GatedGCN
    value: 0.5864
    std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 4
    source_ref: this paper
  - model: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 4
    source_ref: this paper
  metric: AP
  higher_is_better: true
- dataset: Peptides-struct
  rows:
  - model: GCN
    value: 0.3496
    std: 0.0013
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
  - model: GCNII
    value: 0.3471
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 4
    source_ref: this paper
  - model: GatedGCN
    value: 0.342
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 4
    source_ref: this paper
  - model: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 4
    source_ref: this paper
  metric: MAE
  higher_is_better: false
---

