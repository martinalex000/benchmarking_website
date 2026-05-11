---
title: 'Node Identifiers: Compact, Discrete Representations for Efficient Graph Learning'
arxiv_id: '2405.16435'
authors: []
published_date: May 2024
abstract: We present a novel end-to-end framework that generates highly compact (typically
  6-15 dimensions), discrete (int4 type), and interpretable node representations,
  termed node identifiers (node IDs), to tackle inference challenges on large-scale
  graphs. By employing vector quantization, we compress continuous node embeddings
  from multiple layers of a Graph Neural Network (GNN) into discrete codes, applicable
  under both self-supervised and supervised learning paradigms. These node IDs capture
  high-level abstractions of graph data and offer interpretability that traditional
  GNN embeddings lack. Extensive experiments on 34 datasets, encompassing node classification,
  graph classification, link prediction, and attributed graph clustering tasks, demonstrate
  that the generated node IDs significantly enhance speed and memory efficiency while
  achieving competitive performance compared to current state-of-the-art methods.
codebase_url: https://github.com/LUOyk1999/NodeID
extraction_model: glm-4.7
results:
- dataset: Cora
  is_multi_metric: true
  rows:
  - model: NID_GCN (End-to-End Learning)
    metric_values:
    - 87.88
    - null
    - null
    metric_stds:
    - 0.69
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: true
  - model: NID_GCN (Post-hoc RVQ)
    metric_values:
    - 86.17
    - null
    - null
    metric_stds:
    - 0.33
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: NID_GCN
    metric_values:
    - 85.63
    - 6.15
    - 84.7
    metric_stds:
    - 0.31
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: CCA-SSG
    metric_values:
    - 84.0
    - null
    - null
    metric_stds:
    - 0.4
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: MVGRL
    metric_values:
    - 83.5
    - null
    - null
    metric_stds:
    - 0.4
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: InfoGCL
    metric_values:
    - 83.5
    - null
    - null
    metric_stds:
    - 0.3
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: DGI
    metric_values:
    - 82.3
    - null
    - null
    metric_stds:
    - 0.6
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: GCN
    metric_values:
    - 81.83
    - null
    - null
    metric_stds:
    - 0.26
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    is_best: false
  - model: NID_SAGE
    metric_values:
    - 76.78
    - null
    - null
    metric_stds:
    - 0.59
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: VQGraph without reconstruction loss
    metric_values:
    - 76.17
    - null
    - null
    metric_stds:
    - 0.47
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: VQGraph
    metric_values:
    - 76.08
    - 6.85
    - 1.3
    metric_stds:
    - 0.55
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: GAE
    metric_values:
    - 71.5
    - null
    - null
    metric_stds:
    - 0.4
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: SAGE
    metric_values:
    - 70.52
    - null
    - null
    metric_stds:
    - 0.14
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: DGCluster
    metric_values:
    - 69.8
    - null
    - null
    metric_stds:
    - null
    - null
    - null
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: VQGraph tokens
    metric_values:
    - 63.39
    - null
    - null
    metric_stds:
    - 1.15
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: MLP
    metric_values:
    - 57.8
    - null
    - null
    metric_stds:
    - 0.5
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: NID_GCN(M=1)
    metric_values:
    - null
    - null
    - 83.3
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  - model: Random
    metric_values:
    - null
    - 7.21
    - null
    metric_stds:
    - null
    - null
    - null
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    is_best: false
  metrics:
  - Accuracy
  - GED
  - Usage rate
  primary_metric: Accuracy
  higher_is_better: true
- dataset: Peptides-func
  rows:
  - model: GRIT
    value: 0.6988
    std: 0.0082
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: true
  - model: Graph ViT
    value: 0.697
    std: 0.008
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: true
  - model: GCN
    value: 0.6762
    std: 0.0053
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: NID_GCN
    value: 0.6608
    std: 0.0058
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: GraphGPS
    value: 0.6535
    std: 0.0041
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
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
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: GT
    value: 0.6326
    std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
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
    table_ref: Table 3
    source_ref: this paper
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
    table_ref: Table 3
    source_ref: this paper
    is_best: true
  - model: Exphormer
    value: 0.2481
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: GraphGPS
    value: 0.25
    std: 0.0012
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: GCN
    value: 0.2512
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: GT
    value: 0.2529
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  - model: NID_GCN
    value: 0.2589
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 3
    source_ref: this paper
    is_best: false
  metric: MAE
  higher_is_better: false
- dataset: ogbg-molhiv
  rows:
  - model: ContextPred
    value: 68.9
    std: 0.4
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: true
  - model: JOAO
    value: 68.1
    std: 0.9
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: true
  - model: SimGRACE
    value: 66.3
    std: 1.5
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: false
  - model: EdgePred
    value: 64.9
    std: 2.0
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: false
  - model: NID_CL
    value: 64.3
    std: 0.8
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: false
  - model: GraphCL
    value: 63.7
    std: 2.3
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: false
  - model: AttrMask
    value: 60.9
    std: 1.3
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 13
    source_ref: this paper
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
main_figure: /figures/2405.16435/main_figure.png
---

