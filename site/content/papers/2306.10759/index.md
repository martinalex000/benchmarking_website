---
title: 'SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations'
arxiv_id: '2306.10759'
authors: []
published_date: Jun 2023
abstract: Learning representations on large-sized graphs is a long-standing challenge
  due to the inter-dependence nature involved in massive data points. Transformers,
  as an emerging class of foundation encoders for graph-structured data, have shown
  promising performance on small graphs due to its global attention capable of capturing
  all-pair influence beyond neighboring nodes. Even so, existing approaches tend to
  inherit the spirit of Transformers in language and vision tasks, and embrace complicated
  models by stacking deep multi-head attentions. In this paper, we critically demonstrate
  that even using a one-layer attention can bring up surprisingly competitive performance
  across node property prediction benchmarks where node numbers range from thousand-level
  to billion-level. This encourages us to rethink the design philosophy for Transformers
  on large graphs, where the quadratic global attention is a computation overhead
  hindering the scalability. We frame the proposed scheme as Simplified Graph Transformers
  (SGFormer), which is empowered by a simple attention model that can efficiently
  propagate information among arbitrary nodes at the minimal cost of one propagation
  layer and linear complexity w.r.t. node numbers. Moreover, SGFormer requires none
  of positional encodings, feature/graph pre-processing or extra loss. Empirically,
  SGFormer successfully scales to the web-scale graph ogbn-papers100M and yields up
  to 141x inference acceleration over SOTA Transformers on medium-sized graphs. Beyond
  current results, we believe the proposed methodology alone enlightens a new technical
  path of independent interest for building Transformers on large graphs. The codes
  are publicly available at https://github.com/qitianwu/SGFormer.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- SGFormer
mrr: 0.1667
results:
- &id001
  dataset: ogbn-arxiv
  rows:
  - model: Polynormer
    value: 0.734
    std: 0.0022
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: true
  - model: GAT
    value: 0.733
    std: 0.0018
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: GraphSAGE
    value: 0.73
    std: 0.0028
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: SGFormer
    value: 0.7263
    std: 0.0013
    metric: Accuracy
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 6
    is_best: false
  - model: GCN
    value: 0.7174
    std: 0.0029
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 2
    source_ref: this paper
    global_rank: 1
    is_best: false
  - model: SIGN
    value: 0.7028
    std: 0.0025
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 23
    is_best: false
  - model: GCN-Nsampler
    value: 0.685
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 25
    is_best: false
  - model: SGC
    value: 0.6779
    std: 0.0027
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 27
    is_best: false
  - model: GAT-NSampler
    value: 0.6763
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 29
    is_best: false
  - model: NodeFormer
    value: 0.599
    std: 0.0042
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 28
    is_best: false
  - model: MLP
    value: 0.555
    std: 0.0023
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 2
    source_ref: this paper
    global_rank: 30
    is_best: false
  metric: Accuracy
  higher_is_better: true
- &id002
  dataset: ogbn-proteins
  rows:
  - model: GAT
    value: 0.8501
    std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GraphSAGE
    value: 0.8221
    std: 0.0032
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: SGFormer
    value: 0.7953
    std: 0.0038
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 3
    is_best: false
  - model: Polynormer
    value: 0.7953
    std: 0.0067
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.08993'
    title: 'Classic GNNs are Strong Baselines: - Reassessing GNNs for Node Classification'
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: false
  - model: NodeFormer
    value: 0.7745
    std: 0.0115
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nodeformer
    global_rank: 6
    is_best: false
  - model: GAT-NSampler
    value: 0.7463
    std: 0.0124
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCN-Nsampler
    value: 0.7351
    std: 0.0131
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 11
    is_best: false
  - model: GCN
    value: 0.7251
    std: 0.0035
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 8
    is_best: false
  - model: MLP
    value: 0.7204
    std: 0.0048
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 13
    is_best: false
  - model: SIGN
    value: 0.7124
    std: 0.0046
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 14
    is_best: false
  - model: SGC
    value: 0.7031
    std: 0.0023
    metric: ROC-AUC
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 15
    is_best: false
  metric: ROC-AUC
  higher_is_better: true
results_grouped:
- benchmark: OGB
  datasets:
  - *id001
  - *id002
single_proposed_model: SGFormer
main_figure: /figures/2306.10759/main_figure.png
---

