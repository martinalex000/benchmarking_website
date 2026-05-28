---
title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph Representational
  Learning'
arxiv_id: '2403.13749'
source_url: ''
authors: []
published_date: Mar 2024
published_date_iso: 2024-03
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
paper_type: method
proposed_models:
- 1-lGIN
- 2-lGIN
- 3-lGIN
- 4-lGIN
- 5-lGIN
- 6-lGIN
- 7-ℓGIN
- 5-\ellGIN
mrr: 0.04
adjusted_mrr: 0.0133
mrr_dataset_count: 1
benchmark_categories:
- Classic
- LRGB
- Quantum Chemistry
task_categories:
- graph_classification
- graph_regression
experiment_scopes:
- graph-level
results:
- &id002
  dataset: Peptides-func
  is_multi_metric: true
  rows:
  - model: LightGBM (ECFP)
    model_key: lightgbm (ecfp)
    model_plain: LightGBM (ECFP)
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
    sort_value: 0.746
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: Random Forest (ECFP)
    model_key: random forest (ecfp)
    model_plain: Random Forest (ECFP)
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
    sort_value: 0.7355
    sort_std: 0.001
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: LightGBM (TT)
    model_key: lightgbm (tt)
    model_plain: LightGBM (TT)
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
    date: Jan 29, 2025
    date_display: Jan 2025
    date_iso: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
    sort_value: 0.7318
    sort_std: null
    has_value_gap: false
    has_value_note: false
    paper_rank: null
    rank_delta: null
    rank_delta_abs: null
    value_note: ''
  - model: 7-ℓGIN
    model_key: 7-ℓgin
    model_plain: 7-ℓGIN
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
    sort_value: 0.657
    sort_std: 0.006
    true_value: 0.657
    true_std: 0.006
    paper_value: 0.657
    paper_std: 0.006
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 163
  - model: 7-\ell{}GIN
    model_key: 7-\ell{}gin
    model_plain: 7-\ell{}GIN
    metric_values:
    - 0.657
    - null
    metric_stds:
    - 0.006
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.657
    sort_std: 0.006
    true_value: 0.657
    true_std: 0.006
    paper_value: 0.657
    paper_std: 0.006
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 164
  - model: Kipf et al.
    model_key: kipf et al.
    model_plain: Kipf et al.
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
    sort_value: 0.593
    sort_std: 0.0023
    true_value: 0.593
    true_std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 264
  - model: Hu et al.
    model_key: hu et al.
    model_plain: Hu et al.
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
    sort_value: 0.593
    sort_std: 0.0023
    true_value: 0.593
    true_std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 265
  - model: Kipf et al. (GCN)
    model_key: kipf et al. (gcn)
    model_plain: Kipf et al. (GCN)
    metric_values:
    - 0.593
    - null
    metric_stds:
    - 0.0023
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.593
    sort_std: 0.0023
    true_value: 0.593
    true_std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 266
  - model: Hu et al. (Graphormer-like/Strategies)
    model_key: hu et al. (graphormer-like/strategies)
    model_plain: Hu et al. (Graphormer-like/Strategies)
    metric_values:
    - 0.593
    - null
    metric_stds:
    - 0.0023
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    sort_value: 0.593
    sort_std: 0.0023
    true_value: 0.593
    true_std: 0.0023
    paper_value: 0.593
    paper_std: 0.0023
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 267
  - model: Bresson et al.
    model_key: bresson et al.
    model_plain: Bresson et al.
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
    sort_value: 0.5864
    sort_std: 0.0077
    true_value: 0.5864
    true_std: 0.0077
    paper_value: 0.5864
    paper_std: 0.0077
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_note: ''
    arxiv_id: ''
    title: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    codebase_url: ''
    uses_external_data: null
    is_best: false
    global_rank: 274
  metrics:
  - AP
  - MAE
  primary_metric: AP
  higher_is_better: true
- &id003
  dataset: QM9
  rows:
  - model: Mace
    model_key: mace
    model_plain: Mace
    value: 0.02
    std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2509.22259'
    title: Rotary Position Encodings for Graphs
    date: Sep 2025
    date_display: Sep 2025
    date_iso: 2025-09
    codebase_url: https://github.com/google-research/scenic
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.02
    sort_std: null
    is_best: true
  - model: PST
    model_key: pst
    model_plain: PST
    value: 0.023
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
    global_rank: 2
    sort_value: 0.023
    sort_std: 0.001
    is_best: false
  - model: DropGIN
    model_key: dropgin
    model_plain: DropGIN
    value: 0.02578744427174226
    std: 0.000867405321348238
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
    global_rank: 3
    sort_value: 0.02578744427174226
    sort_std: 0.000867405321348238
    is_best: false
  - model: Wu et al. 2018
    model_key: wu et al. 2018
    model_plain: Wu et al. 2018
    value: 0.244
    std: null
    paper_value: 0.244
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Wu et al. 2018
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 21
    true_value: 0.244
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 21
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.244
    sort_std: null
    is_best: false
  - model: Zhou et al. 2023
    model_key: zhou et al. 2023
    model_plain: Zhou et al. 2023
    value: 0.346
    std: null
    paper_value: 0.346
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhou et al. 2023
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 24
    true_value: 0.346
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 24
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.346
    sort_std: null
    is_best: false
  - model: 5-\ellGIN
    model_key: 5-\ellgin
    model_plain: 5-\ellGIN
    value: 0.35
    std: 0.011
    paper_value: 0.35
    paper_std: 0.011
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 25
    true_value: 0.35
    true_std: 0.011
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 25
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.35
    sort_std: 0.011
    is_best: false
  - model: Chen et al. 2020
    model_key: chen et al. 2020
    model_plain: Chen et al. 2020
    value: 0.364
    std: null
    paper_value: 0.364
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Chen et al. 2020
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 29
    true_value: 0.364
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 29
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.364
    sort_std: null
    is_best: false
  - model: Maron et al. 2019
    model_key: maron et al. 2019
    model_plain: Maron et al. 2019
    value: 0.382
    std: null
    paper_value: 0.382
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: Maron et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 30
    true_value: 0.382
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 30
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.382
    sort_std: null
    is_best: false
  - model: Zhang et al. 2021
    model_key: zhang et al. 2021
    model_plain: Zhang et al. 2021
    value: 0.428
    std: null
    paper_value: 0.428
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Zhang et al. 2021
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 35
    true_value: 0.428
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 35
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.428
    sort_std: null
    is_best: false
  - model: Morris et al. 2019
    model_key: morris et al. 2019
    model_plain: Morris et al. 2019
    value: 0.476
    std: null
    paper_value: 0.476
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: Morris et al. 2019
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 38
    true_value: 0.476
    true_std: null
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 38
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.476
    sort_std: null
    is_best: false
  - model: 1-GNN
    model_key: 1-gnn
    model_plain: 1-GNN
    value: 0.493
    std: null
    paper_value: 0.493
    paper_std: null
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: exact match'
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 39
    true_value: 0.493
    true_std: null
    value_gap_source_arxiv: '2309.04941'
    value_gap_source_title: Distance-Restricted Folklore Weisfeiler-Leman GNNs with
      Provable Cycle Counting Power
    value_gap_source_is_current_paper: false
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 39
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.493
    sort_std: null
    is_best: false
  metric: MAE
  higher_is_better: false
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
  - model: 5-lGIN
    model_key: 5-lgin
    model_plain: 5-lGIN
    value: 0.072
    std: 0.002
    paper_value: 0.072
    paper_std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 115
    true_value: 0.072
    true_std: 0.002
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 115
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.072
    sort_std: 0.002
    is_best: false
  - model: 4-lGIN
    model_key: 4-lgin
    model_plain: 4-lGIN
    value: 0.077
    std: 0.001
    paper_value: 0.077
    paper_std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 136
    true_value: 0.077
    true_std: 0.001
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 136
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.077
    sort_std: 0.001
    is_best: false
  - model: 6-lGIN
    model_key: 6-lgin
    model_plain: 6-lGIN
    value: 0.077
    std: 0.0
    paper_value: 0.077
    paper_std: 0.0
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 137
    true_value: 0.077
    true_std: 0.0
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 137
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.077
    sort_std: 0.0
    is_best: false
  - model: 3-lGIN
    model_key: 3-lgin
    model_plain: 3-lGIN
    value: 0.184
    std: 0.007
    paper_value: 0.184
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 250
    true_value: 0.184
    true_std: 0.007
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 250
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.184
    sort_std: 0.007
    is_best: false
  - model: 2-lGIN
    model_key: 2-lgin
    model_plain: 2-lGIN
    value: 0.198
    std: 0.008
    paper_value: 0.198
    paper_std: 0.008
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 259
    true_value: 0.198
    true_std: 0.008
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 259
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.198
    sort_std: 0.008
    is_best: false
  - model: 1-lGIN
    model_key: 1-lgin
    model_plain: 1-lGIN
    value: 0.201
    std: 0.004
    paper_value: 0.201
    paper_std: 0.004
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 260
    true_value: 0.201
    true_std: 0.004
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 260
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.201
    sort_std: 0.004
    is_best: false
  - model: 0-lGIN
    model_key: 0-lgin
    model_plain: 0-lGIN
    value: 0.209
    std: 0.007
    paper_value: 0.209
    paper_std: 0.007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: ''
    date: Mar 2024
    date_display: Mar 2024
    date_iso: 2024-03
    global_rank: 262
    true_value: 0.209
    true_std: 0.007
    value_gap_source_arxiv: '2403.13749'
    value_gap_source_title: 'Weisfeiler and Leman Go Loopy: A New Hierarchy for Graph
      Representational Learning'
    value_gap_source_is_current_paper: true
    has_value_gap: false
    has_value_note: false
    value_gap: null
    value_note: ''
    paper_rank: 262
    rank_delta: 0
    rank_delta_abs: 0
    rank_delta_direction: same
    sort_value: 0.209
    sort_std: 0.007
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
- benchmark: Quantum Chemistry
  datasets:
  - *id003
main_figure: /figures/2403.13749/main_figure.png
---

