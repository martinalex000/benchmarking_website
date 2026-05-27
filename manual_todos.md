I want a simple script that processes those papers one-by-one during off-peak hours (23PM until 7:30AM). 

vllm serve einrichten und dann dagegen verbinden. 

todo papers queue sinnvoll updaten sobald ein neues paper eingefügt wurde

dark mode

shadcn/ui

MLP baseline für fehlende Datensätze selbst berechnen

also extract and store in the database whether a suggested model is a transformer or message-passing whenever that is clearly stated.

3rd party data with pretraining and finetuning (use of external data) could be interesting too

Used hardware for the experiments and potentially runtime (even though thats usually not the big tiebreaker)




## Script cleanup backlog

- consolidate `scripts/find_todo_papers.py` and `scripts/process_todo_list.py` if both remain in use; right now the first is a manual queue manager while the second is the priority-queue batch runner
- decide whether `scripts/test_model_ping.py` should stay as a committed diagnostic utility or move into docs-only troubleshooting notes once the endpoint/model situation stabilizes
- review whether `scripts/run_pipeline.sh` should absorb the off-peak-hours scheduling logic directly, or whether that belongs in external cron/systemd config instead of the repo

at some point in the future: add generation benchmarks/metrics etc. But this feels more like a paper than a normal benchmarking overview since everything is extremely scattered.

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

