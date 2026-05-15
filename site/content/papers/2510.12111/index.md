---
title: 'Chimera: State Space Models Beyond Sequences'
arxiv_id: '2510.12111'
authors: []
published_date: ''
abstract: 'Transformer-based deep learning methods have emerged as the standard approach
  to model diverse data such as sequences, images, and graphs. These methods rely
  on self-attention, which treats data as an unordered set of elements. This ignores
  the neighborhood structure or graph topology of the data and requires the use of
  inductive biases, such as position embeddings in sequences and images, and random
  walks in graphs, to incorporate topology. However, developing bespoke inductive
  biases for each task requires significant effort and can also introduce side-effects
  hindering generalization. In this work, we introduce , a unified model that directly
  incorporates the data topology in a principled way, obviating the need for domain-specific
  biases. Central to is the observation that state-space models---which naturally
  do not require position embeddings---can be generalized to capture any general graph
  topology. Our experiments demonstrate the versatility of our approach--- achieves
  strong performance across the domains of language, vision, and graphs, outperforming
  BERT on GLUE by 0.7 points, ViT on ImageNet-1k by 2.6\ Our results validate ''s
  principled methodological contributions and affirm the long-held belief that data
  topology is a powerful inductive bias across modalities.~We further propose algorithmic
  optimizations to improve ''s efficiency while maintaining performance: 1) For the
  subclass of Directed Acyclic Graphs we show that can be implemented as a linear
  time recurrence. 2) For general graphs, we relax the method with a simple mathematical
  approximation, achieving Transformer''s quadratic complexity without relying on
  domain-specific biases. =-1 : https://github.com/goombalab/chimeragithub.com/goombalab/chimerafootnote-1'
codebase_url: ''
extraction_model: qwen3.6-35b-a3b
has_results: false
proposed_models: []
mrr: null
results: []
results_grouped: []
main_figure: /figures/2510.12111/main_figure.png
---

