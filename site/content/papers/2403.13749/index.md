---
title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy - for Graph Representational
  Learning'
arxiv_id: '2403.13749'
authors: []
published_date: Mar 2024
abstract: We introduce $r$-loopy Weisfeiler-Leman ($r$-), a novel hierarchy of graph
  isomorphism tests and a corresponding GNN framework, $r$-, that can count cycles
  up to length $r+2$. Most notably, we show that $r$- can count homomorphisms of cactus
  graphs. This extends 1-WL, which can only count homomorphisms of trees and, in fact,
  we prove that $r$- is incomparable to $k$-WL for any fixed $k$. We empirically validate
  the expressive and counting power of $r$- on several synthetic datasets and demonstrate
  the scalability and strong performance on various real-world datasets, particularly
  on sparse graphs. Our code is available on GitHub.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- 1-lGIN
- 2-lGIN
- 3-lGIN
- 4-lGIN
- 5-lGIN
- 6-lGIN
- 7-ℓGIN
mrr: 0.0083
results:
- &id002
  dataset: Peptides-func
  is_multi_metric: true
  rows:
  - model: LightGBM (ECFP)
    metric_values:
    - 0.746
    - null
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
    metric_values:
    - 0.7355
    - null
    metric_stds:
    - 0.001
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
    metric_values:
    - 0.7318
    - null
    metric_stds:
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    date_iso: ''
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: 7-ℓGIN
    metric_values:
    - 0.657
    - 0.2513
    metric_stds:
    - 0.006
    - 0.0021
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 160
  - model: Kipf et al.
    metric_values:
    - 0.593
    - 0.3496
    metric_stds:
    - 0.0023
    - 0.0013
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 255
  - model: Hu et al.
    metric_values:
    - 0.593
    - 0.3496
    metric_stds:
    - 0.0023
    - 0.0013
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 256
  - model: Bresson et al.
    metric_values:
    - 0.5864
    - 0.342
    metric_stds:
    - 0.0077
    - 0.0013
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
    global_rank: 262
  metrics:
  - AP
  - MAE
  primary_metric: AP
  higher_is_better: true
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
  - model: 5-lGIN
    value: 0.072
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 105
    is_best: false
  - model: 4-lGIN
    value: 0.077
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 120
    is_best: false
  - model: 6-lGIN
    value: 0.077
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 121
    is_best: false
  - model: 3-lGIN
    value: 0.184
    std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 222
    is_best: false
  - model: 2-lGIN
    value: 0.198
    std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 230
    is_best: false
  - model: 1-lGIN
    value: 0.201
    std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 231
    is_best: false
  - model: 0-lGIN
    value: 0.209
    std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 233
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: Classic
  datasets:
  - *id001
- benchmark: LRGB
  datasets:
  - *id002
main_figure: /figures/2403.13749/main_figure.png
---

