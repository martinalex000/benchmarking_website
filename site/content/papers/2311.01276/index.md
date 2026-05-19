---
title: 'Neural Atoms: Propagating Long-range - Interaction in Molecular Graphs through
  - Efficient Communication Channel'
arxiv_id: '2311.01276'
authors: []
published_date: Nov 2023
abstract: Graph Neural Networks (GNNs) have been widely adopted for drug discovery
  with molecular graphs. Nevertheless, current GNNs mainly excel in leveraging short-range
  interactions (SRI) but struggle to capture long-range interactions (LRI), both of
  which are crucial for determining molecular properties. To tackle this issue, we
  propose a method to abstract the collective information of atomic groups into a
  few Neural Atoms by implicitly projecting the atoms of a molecular. Specifically,
  we explicitly exchange the information among neural atoms and project them back
  to the atoms’ representations as an enhancement. With this mechanism, neural atoms
  establish the communication channels among distant nodes, effectively reducing the
  interaction scope of arbitrary node pairs into a single hop. To provide an inspection
  of our method from a physical perspective, we reveal its connection to the traditional
  LRI calculation method, Ewald Summation. The Neural Atom can enhance GNNs to capture
  LRI by approximating the potential LRI of the molecular. We conduct extensive experiments
  on four long-range graph benchmarks, covering graph-level and link-level tasks on
  molecular graphs. We achieve up to a 27.32\ Empirically, our method can be equipped
  with an arbitrary GNN to help capture LRI. Code and datasets are publicly available
  in https://github.com/tmlr-group/NeuralAtom.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- GCN + Neural Atoms
- GatedGCN + Neural Atoms
mrr: 0.0095
results:
- &id003
  dataset: PCQM-Contact
  rows:
  - model: FloydNet
    value: 0.6143
    std: null
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2601.19094'
    title: 'FloydNet: A Learning Paradigm for Global Relational Reasoning'
    date: Jan 2026
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: NeuralWalker
    value: 0.4707
    std: 0.0007
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: GPS
    value: 0.4703
    std: 0.0014
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2406.03386'
    title: Learning Long Range Dependencies on Graphs - via Random Walks
    date: Jun 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: SAN+LapPE
    value: 0.335
    std: 0.0003
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 41
    is_best: false
  - model: GraphGPS
    value: 0.3337
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 44
    is_best: false
  - model: GatedGCN + Neural Atoms
    value: 0.3262
    std: 0.001
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 49
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.3242
    std: 0.0008
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 1
    source_ref: this paper
    global_rank: 51
    is_best: false
  - model: GatedGCN
    value: 0.3218
    std: 0.0011
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 4
    is_best: false
  - model: GINE
    value: 0.318
    std: 0.0027
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 16
    is_best: false
  - model: Transformer+LapPE
    value: 0.3174
    std: 0.002
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 1
    source_ref: this paper
    global_rank: 52
    is_best: false
  - model: GCNII
    value: 0.3161
    std: 0.0004
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 54
    is_best: false
  - model: GCN + Neural Atoms
    value: 0.3049
    std: 0.0006
    metric: MRR
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 56
    is_best: false
  - model: GCN
    value: 0.2329
    std: 0.0009
    metric: MRR
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 6
    is_best: false
  metric: MRR
  higher_is_better: true
- &id001
  dataset: Peptides-func
  rows:
  - model: LightGBM (ECFP)
    value: 0.746
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Random Forest (ECFP)
    value: 0.7355
    std: 0.001
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: LightGBM (TT)
    value: 0.7318
    std: null
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2501.17901'
    title: Molecular Fingerprints Are Strong Models for Peptide Function Prediction
    date: '2025-01-29'
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: GatedGCN + Neural Atoms
    value: 0.6591
    std: 0.005
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 149
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
    table_ref: Table 1
    source_ref: this paper
    global_rank: 153
    is_best: false
  - model: SAN+LapPE
    value: 0.6384
    std: 0.0121
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 190
    is_best: false
  - model: Transformer+LapPE
    value: 0.6326
    std: 0.0126
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 1
    source_ref: this paper
    global_rank: 195
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.6069
    std: 0.0035
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 1
    source_ref: this paper
    global_rank: 128
    is_best: false
  - model: GCN + Neural Atoms
    value: 0.5996
    std: 0.0033
    metric: AP
    higher_is_better: true
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 220
    is_best: false
  - model: GCN
    value: 0.593
    std: 0.0023
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 9
    is_best: false
  - model: GatedGCN
    value: 0.5864
    std: 0.0077
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 46
    is_best: false
  - model: GCNII
    value: 0.5543
    std: 0.0078
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 246
    is_best: false
  - model: GINE
    value: 0.5498
    std: 0.0079
    metric: AP
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 135
    is_best: false
  metric: AP
  higher_is_better: true
- &id002
  dataset: Peptides-struct
  rows:
  - model: GRPE-FFGT
    value: 0.2416
    std: 0.0026
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2311.04653'
    title: Hybrid Focal and Full-Range Attention Based Graph Transformers -
    date: Nov 2023
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: Tango_GPS
    value: 0.2422
    std: 0.0014
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2508.05070'
    title: 'Tango: Graph Neural Dynamics via Learned Energy and Tangential Flows'
    date: Aug 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: true
  - model: IPR-MPNN
    value: 0.2422
    std: 0.0007
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2312.16560'
    title: Algorithmic Graph Tasks
    date: Dec 2023
    codebase_url: https://github.com/nec-research/Adaptive-Message-Passing
    uses_external_data: false
    is_global_top: true
    global_rank: 4
    is_best: true
  - model: GraphGPS
    value: 0.25
    std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 117
    is_best: false
  - model: Transformer+LapPE
    value: 0.2529
    std: 0.0016
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.501
    table_ref: Table 1
    source_ref: this paper
    global_rank: 142
    is_best: false
  - model: GCN + Neural Atoms
    value: 0.2563
    std: 0.002
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 167
    is_best: false
  - model: GatedGCN + Neural Atoms
    value: 0.2568
    std: 0.0005
    metric: MAE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: 170
    is_best: false
  - model: SAN+LapPE
    value: 0.2683
    std: 0.0043
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.531
    table_ref: Table 1
    source_ref: this paper
    global_rank: 200
    is_best: false
  - model: GatedGCN+RWSE
    value: 0.3357
    std: 0.0006
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.506
    table_ref: Table 1
    source_ref: this paper
    global_rank: 141
    is_best: false
  - model: GatedGCN
    value: 0.342
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.502
    table_ref: Table 1
    source_ref: this paper
    global_rank: 10
    is_best: false
  - model: GCNII
    value: 0.3471
    std: 0.001
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.492
    table_ref: Table 1
    source_ref: this paper
    global_rank: 232
    is_best: false
  - model: GCN
    value: 0.3496
    std: 0.0013
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    table_ref: Table 1
    source_ref: this paper
    global_rank: 2
    is_best: false
  - model: GINE
    value: 0.3547
    std: 0.0045
    metric: MAE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.505
    table_ref: Table 1
    source_ref: this paper
    global_rank: 69
    is_best: false
  metric: MAE
  higher_is_better: false
results_grouped:
- benchmark: LRGB
  datasets:
  - *id001
  - *id002
  - *id003
main_figure: /figures/2311.01276/main_figure.png
---

