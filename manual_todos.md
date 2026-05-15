- benchmarks for the heterogenous graphs, plus a comment on which of them are considered actually heterogenous (there is a v1 and v2 of such datasets)
- the prompt for the decision which papers to look at does not really work. it should be a two-stage thing which is first fed the abstract and title and checks whether it is on graph learning at all (there could also be some extremely simple pattern matching as a very first stage). And then in the second step it should actually read the paper and extract the information, the info which datasets are used is typically not included in the abstract and often not even in the introduction. 
- decide what to do with custom datasets, the information should be stored somewhere
- there should also be a table that effectively tracks which papers are NOT about graph learning such that there is no need to evaluate that every single time again...


extract datasets from OGB and pyg (find the papers and put them into a list of papers to be processed). Then I want a simple script that processes those papers one-by-one during off-peak hours (23PM until 7:30AM). 

Use TU Dresden models and compare their effectiveness (especially the minimax model) use 2406.08993 2210.07606 for that as teh qwen model struggled there.

In some cases the result reported as a baseline in the paper and the best result for the model do not match. On the paper view indicate such places (I believe currently they are only evident by numbers being non-ascending - at least that is the only explanation i have for that behavior).

╭────────────────────────────────────┬────────────┬─────────┬─────────┬───────┬─────────────────────────────────────────────────────────────────────┬────────╮
│ Model                              │ Paper      │    Time │    TTFT │ tok/s │ Datasets found                                                      │ Status │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ openai-gpt-oss-120b                │ 2206.08164 │    6.8s │   4.64s │   315 │ PascalVOC-SP, COCO-SP, Peptides-func, Peptides-struct, PCQM-Contact │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ meta-llama-3.1-8b-instruct         │ 2206.08164 │    1.4s │   0.20s │   190 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3-omni-30b-a3b-instruct        │ 2206.08164 │    1.8s │   0.25s │   174 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ internvl3.5-30b-a3b                │ 2206.08164 │    2.0s │   0.18s │   146 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-35b-a3b                    │ 2206.08164 │    7.9s │       — │   130 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-397b-a17b                  │ 2206.08164 │    9.0s │       — │   114 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-122b-a10b                  │ 2206.08164 │    9.0s │       — │   113 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.6-35b-a3b                    │ 2206.08164 │   12.2s │       — │    84 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ glm-4.7                            │ 2206.08164 │  246.9s │ 241.98s │    63 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3-30b-a3b-instruct-2507        │ 2206.08164 │   16.3s │  11.10s │    58 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3-coder-30b-a3b-instruct       │ 2206.08164 │    7.1s │   1.20s │    50 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ qwen3.5-27b                        │ 2206.08164 │   21.5s │       — │    48 │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ gemma-3-27b-it                     │ 2206.08164 │    7.8s │   0.72s │    39 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ medgemma-27b-it                    │ 2206.08164 │   16.2s │   1.10s │    24 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ devstral-2-123b-instruct-2512      │ 2206.08164 │  541.5s │ 155.90s │    16 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ mistral-large-3-675b-instruct-2512 │ 2206.08164 │   40.2s │   3.38s │     8 │ PascalVOC-SP, COCO-SP, PCQM-Contact, Peptides-func, Peptides-struct │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ gemma-4-31b-it                     │ 2206.08164 │ 1095.1s │       — │     — │ none                                                                │ ✓      │
├────────────────────────────────────┼────────────┼─────────┼─────────┼───────┼─────────────────────────────────────────────────────────────────────┼────────┤
│ teuken-7b-instruct-research        │ 2206.08164 │   10.5s │       — │     — │ none                                                                │ ✓      │
╰────────────────────────────────────┴────────────┴─────────┴─────────┴───────┴─────────────────────────────────────────────────────────────────────┴────────╯

 Model Extraction Quality vs GLM 4.7 Baseline                                            
╭───────────────────────────────────┬────────┬──────────┬──────┬────────┬────────┬──────────┬────────┬───────────┬─────────┬───────╮
│                                   │        │ Baseline │      │    Val │        │ Halluci- │        │           │ Halluc. │   Avg │
│ Model                             │ Papers │  Entries │ Hits │ Errors │ Misses │  nations │ Recall │ Precision │    Rate │  Time │
├───────────────────────────────────┼────────┼──────────┼──────┼────────┼────────┼──────────┼────────┼───────────┼─────────┼───────┤
│ MiniMaxAI/MiniMax-M2.5            │      1 │      327 │  314 │      0 │     13 │       37 │    96% │       89% │     11% │ 2636s │
├───────────────────────────────────┼────────┼──────────┼──────┼────────┼────────┼──────────┼────────┼───────────┼─────────┼───────┤
│ moonshotai/Kimi-K2.6              │      1 │      327 │  314 │      0 │     13 │       37 │    96% │       89% │     11% │ 2442s │
├───────────────────────────────────┼────────┼──────────┼──────┼────────┼────────┼──────────┼────────┼───────────┼─────────┼───────┤
│ Qwen/Qwen3-Coder-30B-A3B-Instruct │      1 │      327 │  151 │     14 │    162 │       47 │    46% │       71% │     22% │  307s │
╰───────────────────────────────────┴────────┴──────────┴──────┴────────┴────────┴──────────┴────────┴───────────┴─────────┴───────╯
│ google/gemma-4-31B-it             │      1 │      327 │  314 │      0 │     13 │       35 │    96% │       90% │     10% │ 4459s │
│ alias-huge-no-thinking            │      1 │      327 │  289 │      0 │     38 │      124 │    88% │       70% │     30% │ 2369s │
│ alias-huge-no-thinking            │      1 │      327 │   70 │      0 │    257 │       10 │    21% │       88% │     12% │ 7521s │ - wtf...

