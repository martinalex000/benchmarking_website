# Top-method protocol audit

Date: 2026-07-17

## Scope and method

This audit reviewed the leading methods (top three distinct models on each
dataset's configured primary metric and standard variant) after the
three-best-paper re-evaluation cleanup. A row was flagged only when the
paper's local source describes a task, split, or evaluation protocol that is
not comparable with the canonical benchmark variant recorded in the database.

The audit intentionally does not treat a strong score, a non-standard model,
or a missing artifact by itself as evidence of a problem. The findings below
are task/protocol mismatches comparable to the removed `2110.04375` rows.

## Definite whole-paper removals or quarantines

| arXiv | Paper | DB rows | Why the rows are not comparable |
| --- | --- | ---: | --- |
| `2402.14802` | *Link Prediction with Physics-Inspired Graph Neural Networks* | 34 | The paper evaluates transductive **link prediction** on datasets originally designed for node classification, using newly constructed edge splits and random negatives. Its scores currently appear as standard node-classification leaders, including Amazon-ratings (0.9947) and Roman-empire (0.9934). |
| `2304.11116` | *Graph-ToolFormer* | 14 | This is ChatGPT/tool-augmented prompt and API reasoning, with generated prompt instances, rather than the canonical GNN benchmark protocol. It contributes implausible 1.0 scores on several static datasets. |
| `2308.16800` | *Rank Collapse Causes Over-Smoothing and Over-Correlation in GNNs* | 36 | The experiment optimizes cross-entropy over **all nodes** to study function fitting; it has no held-out benchmark split. Its 1.0 scores must not rank against standard Cora/CiteSeer/PubMed/Squirrel evaluation. |
| `2401.13200` | *Topology-aware Embedding Memory for Continual Learning on Expanding Networks* | 33 | The reported values are final average accuracies under a class/task-incremental continual-learning protocol, not ordinary static OGB node-classification test scores. It currently affects the ogbn-arxiv and ogbn-products leaders. |

Source evidence is in the cached LaTeX artifacts:

- `papers/2402.14802/latex/expanded.tex` lines 46–63, 131, 196–197, 438–471, and 495.
- `papers/2304.11116/latex/expanded.tex` lines 91–93, 1871–1908, 2224–2257, and 2302.
- `papers/2308.16800/latex/expanded.tex` lines 427–450.
- `papers/2401.13200/latex/expanded.tex` lines 119–129, 152–166, and 383–396.

## High-confidence candidates needing row-level review

These papers contain link-prediction or continual-learning experiments that
have been mapped to standard static node-classification variants. Remove the
listed incompatible rows, while retaining rows that genuinely belong to an
`ogbl-*` or other canonical link-prediction benchmark.

| arXiv | Paper | DB rows | Review target |
| --- | --- | ---: | --- |
| `2312.14439` | *PUMA* | 58 | Continual graph learning scores (including AP on ogbn-arxiv, ogbn-products, Amazon-Computers, and Reddit) are not static benchmark scores. |
| `2303.08958` | *NESS* | 122 | Link-prediction AP/AUC results are mapped to static node-classification variants such as CiteSeer, Cornell, Texas, and PubMed. |
| `2210.05801` | *Linkless Link Prediction via Relational Distillation* | 51 | Non-OGB link-prediction rows are mapped to standard node-classification variants. Preserve only genuine canonical link-prediction benchmark rows. |
| `2211.14394` | *Link Prediction with Non-Contrastive Learning* | 41 | Same issue: Hits@50 link-prediction results are mapped to Cora, CiteSeer, Coauthor, and Amazon node-classification variants. |

## Remediation completed

1. Removed all rows for the definite protocol-mismatch papers, including PUMA.
2. Removed incompatible non-link-prediction rows for the three mixed-task papers;
   genuine canonical link-prediction rows remain.
3. Added explicit task/protocol extraction, parser validation, source-evidence
   backstops, and curation exclusions. Re-extraction now replaces prior rows,
   including the empty-result case.
4. Re-exported the full Hugo site after cleanup. The cleanup script's final
   dry-run reports zero remaining rows to delete.
