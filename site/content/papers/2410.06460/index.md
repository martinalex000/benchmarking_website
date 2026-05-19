---
title: A Benchmark on Directed Graph Representation Learning in Hardware Designs
arxiv_id: '2410.06460'
authors: []
published_date: Oct 2024
abstract: 'To keep pace with the rapid advancements in design complexity within modern
  computing systems, directed graph representation learning (DGRL) has become crucial,
  particularly for encoding circuit netlists, computational graphs, and developing
  surrogate models for hardware performance prediction. However, DGRL remains relatively
  unexplored, especially in the hardware domain, mainly due to the lack of comprehensive
  and user-friendly benchmarks. This study presents a novel benchmark comprising five
  hardware design datasets and 13 prediction tasks spanning various levels of circuit
  abstraction. We evaluate 21 DGRL models, employing diverse graph neural networks
  and graph transformers (GTs) as backbones, enhanced by positional encodings (PEs)
  tailored for directed graphs. Our results highlight that bidirected (BI) message
  passing neural networks (MPNNs) and robust PEs significantly enhance model performance.
  Notably, the top-performing models include PE-enhanced GTs interleaved with BI-MPNN
  layers and BI-Graph Isomorphism Network, both surpassing baselines across the 13
  tasks. Additionally, our investigation into out-of-distribution (OOD) performance
  emphasizes the urgent need to improve OOD generalization in DGRL models. This benchmark,
  implemented with a modular codebase, streamlines the evaluation of DGRL models for
  both hardware and ML practitioners. Document for the toolbox is available at: https://benchmark-for-dgrl-in-hardwares.readthedocs.io/en/latest/.'
codebase_url: ''
extraction_model: MiniMaxAI/MiniMax-M2.5
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2410.06460/main_figure.png
---

