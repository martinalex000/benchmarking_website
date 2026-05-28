---
title: Bridging Input Feature Spaces Towards Graph Foundation Models
arxiv_id: '2605.04834'
source_url: ''
authors: []
published_date: ''
published_date_iso: ''
abstract: Abstract Unlike vision and language domains, graph learning lacks a shared
  input space, as input features differ across graph datasets not only in semantics,
  but also in value ranges and dimensionality. This misalignment prevents graph models
  from generalizing across datasets, limiting their use as foundation models. In this
  work, we propose All-In, a simple and theoretically grounded method that enables
  transferability across datasets with different input features. Our approach projects
  node features into a shared random space and constructs representations via covariance-based
  statistics, thus eliminating dependence on the original feature space. We show that
  the computed node-covariance operators and the resulting node representations are
  invariant in distribution to permutations of the input features. We further demonstrate
  that the expected operator exhibits invariance to general orthogonal transformations
  of the input features. Empirically, All-In achieves strong performance across diverse
  node- and graph-level tasks on unseen datasets with new input features, without
  requiring architecture changes or retraining. These results point to a promising
  direction for input-agnostic, transferable graph models.
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
paper_type: dataset
proposed_models: []
mrr: null
adjusted_mrr: null
mrr_dataset_count: 0
benchmark_categories: []
task_categories: []
experiment_scopes: []
results: []
results_grouped: []
---

