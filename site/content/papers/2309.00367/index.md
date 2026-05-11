---
title: Where Did the Gap Go? Reassessing the Long-Range Graph Benchmark
arxiv_id: '2309.00367'
authors: []
published_date: Sep 2023
abstract: The recent Long-Range Graph Benchmark (LRGB, Dwivedi et al. 2022) introduced
  a set of graph learning tasks strongly dependent on long-range interaction between
  vertices. Empirical evidence suggests that on these tasks Graph Transformers significantly
  outperform Message Passing GNNs (MPGNNs). In this paper, we carefully reevaluate
  multiple MPGNN baselines as well as the Graph Transformer GPS (Rampášek et al. 2022)
  on LRGB. Through a rigorous empirical analysis, we demonstrate that the reported
  performance gap is overestimated due to suboptimal hyperparameter choices. It is
  noteworthy that across multiple datasets the performance gap completely vanishes
  after basic hyperparameter optimization. In addition, we discuss the impact of lacking
  feature normalization for LRGB's vision datasets and highlight a spurious implementation
  of LRGB's link prediction metric. The principal aim of our paper is to establish
  a higher standard of empirical rigor within the graph machine learning community.
codebase_url: https://github.com/toenshoff/LRGB
extraction_model: glm-4.7
results:
- dataset: COCO-SP
  rows:
  - model: GPS
    value: 0.3884
    std: 0.0055
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 2a
    source_ref: this paper
    is_best: true
  - model: Exphormer
    value: 0.343
    std: 0.0008
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2a
    source_ref: Shirzad et al. 2023
    is_best: false
  - model: GCN
    value: 0.2922
    std: 0.0018
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2a
    source_ref: this paper
    is_best: false
  - model: GINE
    value: 0.2125
    std: 0.0009
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 2a
    source_ref: this paper
    is_best: false
  metric: F1
  higher_is_better: true
- dataset: PCQM-Contact
  rows:
  - model: GPS
    value: 0.4703
    std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Figure 3
    source_ref: this paper
    is_best: true
  - model: GCN
    value: 0.467
    std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Figure 3
    source_ref: this paper
    is_best: false
  - model: GINE
    value: 0.4617
    std: 0.0005
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Figure 3
    source_ref: this paper
    is_best: false
  metric: MRR
  higher_is_better: true
- dataset: PascalVOC-SP
  rows:
  - model: CRAWL
    value: 0.4588
    std: 0.0079
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2a
    source_ref: Tönshoff et al. 2021
    is_best: true
  - model: GPS
    value: 0.444
    std: 0.0065
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 2a
    source_ref: this paper
    is_best: false
  - model: Exphormer
    value: 0.396
    std: 0.0027
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2a
    source_ref: Shirzad et al. 2023
    is_best: false
  - model: GCN
    value: 0.388
    std: 0.004
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2a
    source_ref: this paper
    is_best: false
  - model: DREW
    value: 0.3314
    std: 0.0024
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2a
    source_ref: Gutteridge et al. 2023
    is_best: false
  - model: GINE
    value: 0.2718
    std: 0.0054
    metric: F1
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 2a
    source_ref: this paper
    is_best: false
  metric: F1
  higher_is_better: true
- dataset: Peptides-func
  rows:
  - model: DREW
    value: 0.715
    std: 0.0044
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Gutteridge et al. 2023
    is_best: true
  - model: CRAWL
    value: 0.7074
    std: 0.0032
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Tönshoff et al. 2021
    is_best: true
  - model: GRIT
    value: 0.6988
    std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Ma et al. 2023
    is_best: false
  - model: Graph ViT
    value: 0.6942
    std: 0.0075
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: He et al. 2023
    is_best: false
  - model: G-MLPMixer
    value: 0.6921
    std: 0.0054
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: He et al. 2023
    is_best: false
  - model: GCN
    value: 0.6765
    std: 0.0047
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1a
    source_ref: this paper
    is_best: false
  - model: GINE
    value: 0.6621
    std: 0.0067
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1a
    source_ref: this paper
    is_best: false
  - model: GPS
    value: 0.6534
    std: 0.0091
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1a
    source_ref: this paper
    is_best: false
  - model: Exphormer
    value: 0.6527
    std: 0.0043
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Shirzad et al. 2023
    is_best: false
  metric: AP
  higher_is_better: true
- dataset: Peptides-struct
  rows:
  - model: Graph ViT
    value: 0.2449
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: He et al. 2023
    is_best: true
  - model: GRIT
    value: 0.246
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Ma et al. 2023
    is_best: true
  - model: GINE
    value: 0.2473
    std: 0.0017
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1a
    source_ref: this paper
    is_best: true
  - model: G-MLPMixer
    value: 0.2475
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: He et al. 2023
    is_best: true
  - model: GCN
    value: 0.2477
    std: 0.0009
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1a
    source_ref: this paper
    is_best: false
  - model: Exphormer
    value: 0.2481
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Shirzad et al. 2023
    is_best: false
  - model: CRAWL
    value: 0.2506
    std: 0.0022
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Tönshoff et al. 2021
    is_best: false
  - model: GPS
    value: 0.2509
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.5
    table_ref: Table 1a
    source_ref: this paper
    is_best: false
  - model: DREW
    value: 0.2536
    std: 0.0015
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1a
    source_ref: Gutteridge et al. 2023
    is_best: false
  metric: MAE
  higher_is_better: false
main_figure: /figures/2309.00367/main_figure.png
---

