# Leaderboard mistakes audit

## Scope and method

This report audits the five largest standard leaderboards in the current database:

1. QM9
2. CiteSeer
3. PubMed
4. ogbn-arxiv
5. PROTEINS

For each dataset, the top five rows were reduced to five distinct papers by arXiv ID.
The database row was compared with the paper's extracted LaTeX, extraction notes, and
stored protocol metadata. A paper is marked **accidental inclusion** when the reported
row is not comparable with the dataset's canonical task and split, or when the extracted
value is not supported by the cited table.

## QM9

| Rank | Paper | Row | Finding |
| --- | --- | --- | --- |
| 1 | [2106.07971](papers/2106.07971/) | SchNet, gap MAE `0.0000` | **Accidental inclusion.** The source reports the gap in meV (SchNet `63`), while the database contains zero-valued rows. This is a failed unit conversion/truncated-result salvage. |
| 2 | [2409.15800](papers/2409.15800/) | Equiformer, gap MAE `0.0011` | **Accidental inclusion.** Extraction notes say the table was truncated and representative values were synthesized; the source reports approximately `30` meV, not the stored value. |
| 3 | [2410.09737](papers/2410.09737/) | OGE-Aug, gap MAE `0.00198` | Retained. The source reports the value directly for the stated `0.8/0.1/0.1` split. |
| 4 | [2309.04941](papers/2309.04941/) | 2-DRFWL(2), gap MAE `0.00226` | Retained. Direct test MAE on the stated `0.8/0.1/0.1` split. |
| 5 | [2205.13328](papers/2205.13328/) | KP-GIN, gap MAE `0.00333` | Retained. Direct per-target QM9 result. |

### QM9 pattern

Truncated or uncertain extraction output was salvaged into the database, and electronic
properties reported in meV were not reliably converted to the database's native units.
Missing protocol metadata was also accepted.

## CiteSeer

| Rank | Paper | Row | Finding |
| --- | --- | --- | --- |
| 1 | [2407.11025](papers/2407.11025/) | GCN and baselines, Accuracy `1.0` | **Accidental inclusion.** The source metric is attack success rate (ASR), not node-classification accuracy; CTA/backdoor rows are also non-comparable. |
| 2 | [2412.04064](papers/2412.04064/) | CNA, Accuracy `0.9575` | Retained. Canonical CiteSeer dimensions and node-classification accuracy match; split evidence is weak and should be strengthened on future extraction. |
| 3 | [2406.02997](papers/2406.02997/) | GAT powerembed, Accuracy `0.955` | **Accidental inclusion.** The paper uses 5-fold cross-validation rather than the fixed Planetoid split. |
| 4 | [2505.22362](papers/2505.22362/) | DHGNN, Accuracy `0.946` | **Accidental inclusion.** The source evaluates CiteSeer-Full, which was fuzzy-mapped to canonical CiteSeer. |
| 5 | [2209.00793](papers/2209.00793/) | SPGRL, Accuracy `0.94` | **Accidental inclusion.** Results use variable label budgets of 20/40/60 labels per class rather than the canonical fixed setup. |

### CiteSeer pattern

Metric semantics were not checked, dataset qualifiers were lost during fuzzy matching,
and cross-validation or altered label budgets were allowed into the fixed Planetoid
leaderboard despite protocol notes describing the mismatch.

## PubMed

| Rank | Paper | Row | Finding |
| --- | --- | --- | --- |
| 1 | [2602.01771](papers/2602.01771/) | LLaMA3-3B, Accuracy `0.9746` | **Unsupported/accidental inclusion.** The task is node classification, but no canonical split evidence is supplied; the row was nevertheless marked standard. |
| 2 | [2406.13250](papers/2406.13250/) | LangTopo, Accuracy `0.9667` | **Accidental inclusion.** Random 60/20/20 split. |
| 3 | [2410.02296](papers/2410.02296/) | TAPE + RevGAT, Accuracy `0.9618` | **Accidental inclusion.** Random 60/20/20 split and a random-split external leaderboard source. |
| 4 | [2402.05894](papers/2402.05894/) | LinguGraph-Llama3, Accuracy `0.9559` | **Accidental inclusion.** Uses a 6:2:2 split rather than the canonical Planetoid split. |
| 5 | [2310.16421](papers/2310.16421/) | Graph Agent, Accuracy `0.9548` | **Accidental inclusion.** Uses a 60/20/20 partition; its separate PrimeKG link-prediction experiment is not the cause of this row's mismatch. |

### PubMed pattern

The parser accepted absent split metadata and did not reliably propagate explicit random
split descriptions into protocol decisions. Null protocol decisions were exportable.

## ogbn-arxiv

The canonical task is full-dataset transductive node classification on the official OGB
split with Accuracy.

| Rank | Paper | Row | Finding |
| --- | --- | --- | --- |
| 1 | [2502.11394](papers/2502.11394/) | Label-SBP, Accuracy `0.9350` | **Accidental inclusion.** The value came from an unrelated CSBM appendix; the OGB-arxiv table reports approximately 69–71%. |
| 2 | [2409.06998](papers/2409.06998/) | GMoE, Accuracy `0.8888` | **Accidental row.** The OGB-arxiv column is `0.7188`; `0.8888` belongs to the neighboring genius column. Other rows may remain valid and require row-level re-evaluation. |
| 3 | [2205.07308](papers/2205.07308/) | GloGNN, Accuracy `0.8557` | **Accidental inclusion.** The value belongs to Penn94; generic “arXiv” context was mapped to ogbn-arxiv. |
| 4 | [2507.19526](papers/2507.19526/) | STAG + Prompt Tuning, Accuracy `0.8357` | **Accidental inclusion.** 5-way/5-shot evaluation over random tasks, not the full official OGB task. |
| 5 | [2202.04936](papers/2202.04936/) | MAGnet-true, Accuracy `0.8088` | **Accidental inclusion.** Attack/attribute-injection conditions use AUROC rather than canonical clean Accuracy. |

### ogbn-arxiv pattern

Wide-table column drift, unrelated appendix tables, generic “arXiv” aliases, few-shot
evaluation, and attack metrics were not independently checked against the official OGB
contract. `2409.06998` is a mixed case and must not be removed wholesale without row review.

## PROTEINS

The canonical variant is TU PROTEINS with the established 10-fold cross-validation
protocol.

| Rank | Paper | Row | Finding |
| --- | --- | --- | --- |
| 1 | [2505.15015](papers/2505.15015/) | MSH-GNN, Accuracy `0.941` | Retained. Explicit standard TU 10-fold protocol. |
| 2 | [2103.00111](papers/2103.00111/) | CSSL, Accuracy `0.858` | Retained. Uses the established Xu et al. split. |
| 3 | [2509.24886](papers/2509.24886/) | A-NLSF, Accuracy `0.8547` | **Accidental inclusion.** Random 80/10/10 splits repeated ten times. |
| 4 | [2009.05923](papers/2009.05923/) | HGP-SL, Accuracy `0.8491` | **Accidental inclusion.** Random 80/10/10 splits, with SSL/pretraining variants mixed into the comparison. |
| 5 | [2406.01249](papers/2406.01249/) | att-Pooling-NLSFs, Accuracy `0.8489` | **Accidental inclusion.** Random 80/10/10 splits and tuning on those splits. |

### PROTEINS pattern

The variant was named `10-fold CV` but had no machine-readable split contract, so random
80/10/10 results were treated as canonical. Row extraction often preserved task type but
not the paper-level split protocol.

## General remediation

The repeated failure is not primarily a paper-specific error. The standard leaderboard
accepted rows with absent or overconfident protocol metadata. The targeted fix is therefore
to make canonical benchmark contracts explicit and conservative:

- require a positive row-local protocol note for a standard variant;
- reject missing or uncertain protocol decisions from standard exports;
- detect random/fold/custom/temporal/few-shot/continual/attack/SSL-probing cues;
- reject conflicting dataset qualifiers instead of fuzzy-mapping them;
- quarantine truncated, partial, synthesized, or representative extraction output;
- validate dataset-specific metric names, units, and impossible values;
- require exact OGB dataset/task/split evidence and source-table context.
