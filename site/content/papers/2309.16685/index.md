---
title: Target-aware Variational Auto-encoders for Ligand Generation with Multimodal
  Protein Representation Learning
arxiv_id: '2309.16685'
source_url: ''
authors: []
published_date: Aug 2, 2023
published_date_iso: '2023-08-02'
published_venue: ''
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
  is publicly available at.
codebase_url: https://github.com/HySonLab/Ligand_Generation
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
has_results: true
paper_type: method
proposed_models:
- PMN
mrr: 0.0
adjusted_mrr: 0.0
mrr_dataset_count: 0
benchmark_categories:
- TU Dortmund
task_categories:
- graph_classification
experiment_scopes:
- graph-level
results:
- &id001
  dataset: D&D
  rows:
  - model: DGI
    model_key: dgi
    model_plain: DGI
    value: 0.0222
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_display: Feb 2025
    date_iso: '2025-02-17'
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_global_top: true
    global_rank: 1
    sort_value: 0.0222
    sort_std: null
    is_best: true
  - model: OFA
    model_key: ofa
    model_plain: OFA
    value: 0.0305
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2502.11836'
    title: 'Model Generalization on Text Attribute Graphs: Principles with Large Language
      Models'
    date: Feb 17, 2025
    date_display: Feb 2025
    date_iso: '2025-02-17'
    codebase_url: https://github.com/Graph-COM/LLM_BP
    uses_external_data: false
    is_global_top: true
    global_rank: 2
    sort_value: 0.0305
    sort_std: null
    is_best: false
  - model: Dino
    model_key: dino
    model_plain: Dino
    value: 0.047
    std: null
    metric: Accuracy
    higher_is_better: true
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    arxiv_id: '2408.13661'
    title: Hierarchical Network Fusion for Multi-Modal Electron Micrograph Representation
      Learning with Foundational Large Language Models
    date: Aug 2024
    date_display: Aug 2024
    date_iso: 2024-08
    codebase_url: ''
    uses_external_data: false
    is_global_top: true
    global_rank: 3
    sort_value: 0.047
    sort_std: null
    is_best: false
  - model: PMN
    model_key: pmn
    model_plain: PMN
    value: 0.202
    std: 0.007
    paper_value: 0.202
    paper_std: 0.007
    metric: MSE
    higher_is_better: false
    is_baseline: false
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: this paper
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.202
    sort_std: 0.007
    is_best: false
  - model: AttentionDTA
    model_key: attentiondta
    model_plain: AttentionDTA
    value: 0.216
    std: null
    paper_value: 0.216
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: zhao2019attentiondta
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.216
    sort_std: null
    is_best: false
  - model: FusionDTA
    model_key: fusiondta
    model_plain: FusionDTA
    value: 0.22
    std: null
    paper_value: 0.22
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1093/bib/bbab506
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.22
    sort_std: null
    is_best: false
  - model: MATT-DTI
    model_key: matt-dti
    model_plain: MATT-DTI
    value: 0.227
    std: null
    paper_value: 0.227
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1093/bib/bbab117
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.227
    sort_std: null
    is_best: false
  - model: BiCompDTA
    model_key: bicompdta
    model_plain: BiCompDTA
    value: 0.237
    std: null
    paper_value: 0.237
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1371/journal.pcbi.1011036
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.237
    sort_std: null
    is_best: false
  - model: GraphDTA
    model_key: graphdta
    model_plain: GraphDTA
    value: 0.258
    std: null
    paper_value: 0.258
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: D3RA00281K
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.258
    sort_std: null
    is_best: false
  - model: DeepDTA
    model_key: deepdta
    model_plain: DeepDTA
    value: 0.261
    std: null
    paper_value: 0.261
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: 10.1093/bioinformatics/bty593
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.261
    sort_std: null
    is_best: false
  - model: SimBoost
    model_key: simboost
    model_plain: SimBoost
    value: 0.282
    std: null
    paper_value: 0.282
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: He2017
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.282
    sort_std: null
    is_best: false
  - model: SimCNN-DTA
    model_key: simcnn-dta
    model_plain: SimCNN-DTA
    value: 0.319
    std: null
    paper_value: 0.319
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: shim2021prediction
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.319
    sort_std: null
    is_best: false
  - model: KronRLS
    model_key: kronrls
    model_plain: KronRLS
    value: 0.379
    std: null
    paper_value: 0.379
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: nascimento2016multiple
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.379
    sort_std: null
    is_best: false
  - model: WideDTA
    model_key: widedta
    model_plain: WideDTA
    value: 0.886
    std: null
    paper_value: 0.886
    paper_std: null
    metric: MSE
    higher_is_better: false
    is_baseline: true
    is_overridden: false
    override_reason: ''
    params_millions: null
    table_ref: Table 1
    source_ref: ozturk2019widedta
    variant_inference_reason: 'dataset: fuzzy match to d&d (score=86)'
    date: Aug 2, 2023
    date_display: Aug 2023
    date_iso: '2023-08-02'
    published_venue: null
    global_rank: null
    sort_value: 0.886
    sort_std: null
    is_best: false
  metric: Accuracy
  higher_is_better: false
results_grouped:
- benchmark: TU Dortmund
  datasets:
  - *id001
single_proposed_model: PMN
---

