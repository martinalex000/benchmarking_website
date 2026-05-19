---
title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
  Protein Representation Learning
arxiv_id: '2309.16685'
authors: []
published_date: Sep 2023
abstract: Without knowledge of specific pockets, generating ligands based on the global
  structure of a protein target plays a crucial role in drug discovery as it helps
  reduce the search space for potential drug-like candidates in the pipeline. However,
  contemporary methods require optimizing tailored networks for each protein, which
  is arduous and costly. To address this issue, we introduce TargetVAE, a target-aware
  variational auto-encoder that generates ligands with high binding affinities to
  arbitrary protein targets, guided by a novel multimodal deep neural network built
  based on graph Transformers as the prior for the generative model. This is the first
  effort to unify different representations of proteins (e.g., sequence of amino-acids,
  3D structure) into a single model that we name as Protein Multimodal Network (PMN).
  Our multimodal architecture learns from the entire protein structures and is able
  to capture their sequential, topological and geometrical information. We showcase
  the superiority of our approach by conducting extensive experiments and evaluations,
  including the assessment of generative model quality, ligand generation for unseen
  targets, docking score computation, and binding affinity prediction. Empirical results
  demonstrate the promising performance of our proposed approach. Our software package
  is publicly available at https://github.com/HySonLab/Ligand_Generation.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: true
proposed_models:
- PMN
mrr: 0.0
results:
- &id001
  dataset: D&D
  rows:
  - model: GIN
    value: 0.05
    std: 0.021
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    is_best: true
  - model: GCN
    value: 0.093
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: 0.496
    arxiv_id: '2411.15671'
    title: 'Best of Both Worlds: Advantages of Hybrid Graph Sequence Models'
    date: Nov 2024
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    is_best: false
  - model: PMN
    value: 0.202
    std: 0.007
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    global_rank: null
    is_best: false
  - model: AttentionDTA
    value: 0.216
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2019attentiondta
    global_rank: null
    is_best: false
  - model: FusionDTA
    value: 0.22
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1093/bib/bbab506
    global_rank: null
    is_best: false
  - model: MATT-DTI
    value: 0.227
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1093/bib/bbab117
    global_rank: null
    is_best: false
  - model: BiCompDTA
    value: 0.237
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1371/journal.pcbi.1011036
    global_rank: null
    is_best: false
  - model: GraphDTA
    value: 0.258
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: D3RA00281K
    global_rank: null
    is_best: false
  - model: DeepDTA
    value: 0.261
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1093/bioinformatics/bty593
    global_rank: null
    is_best: false
  - model: MF
    value: 0.271
    std: 0.004
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2506.08618'
    title: HSG-12M
    date: Jun 2025
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    is_best: false
  - model: SimBoost
    value: 0.282
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He2017
    global_rank: null
    is_best: false
  - model: SimCNN-DTA
    value: 0.319
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shim2021prediction
    global_rank: null
    is_best: false
  - model: KronRLS
    value: 0.379
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nascimento2016multiple
    global_rank: null
    is_best: false
  - model: WideDTA
    value: 0.886
    std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ozturk2019widedta
    global_rank: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
single_proposed_model: PMN
main_figure: /figures/2309.16685/main_figure.png
---

