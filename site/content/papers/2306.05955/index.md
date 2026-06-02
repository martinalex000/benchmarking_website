---
title: 'Path Neural Networks: Expressive and Accurate Graph Neural Networks'
arxiv_id: '2306.05955'
source_url: ''
authors: []
published_date: Jun 9, 2023
published_date_iso: '2023-06-09'
published_venue: ''
abstract: Graph neural networks (GNNs) have recently become the standard approach
  for learning with graph-structured data. Prior work has shed light into their potential,
  but also their limitations. Unfortunately, it was shown that standard GNNs are limited
  in their expressive power. These models are no more powerful than the 1-dimensional
  Weisfeiler-Leman (1-WL) algorithm in terms of distinguishing non-isomorphic graphs.
  In this paper, we propose Path Neural Networks (PathNNs), a model that updates node
  representations by aggregating paths emanating from nodes. We derive three different
  variants of the PathNN model that aggregate single shortest paths, all shortest
  paths and all simple paths of length up to K. We prove that two of these variants
  are strictly more powerful than the 1-WL algorithm, and we experimentally validate
  our theoretical results. We find that PathNNs can distinguish pairs of non-isomorphic
  graphs that are indistinguishable by 1-WL, while our most expressive PathNN variant
  can even distinguish between 3-WL indistinguishable graphs. The different PathNN
  variants are also evaluated on graph classification and graph regression datasets,
  where in most cases, they outperform the baseline methods.
codebase_url: https://github.com/gasmichel/PathNNs_expressive
extraction_model: Qwen/Qwen3.6-35B-A3B-FP8
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

