# ResilienceAI_Prac

A reproducible Google Colab-compatible notebook using **only synthetic data**.

## Run in Google Colab
1. Open https://colab.research.google.com/ and choose File → Upload notebook.
2. Upload `ResilienceAI.ipynb` from this package.
3. Select a Python 3 CPU runtime, then Runtime → Run all.
4. Inspect tables, plots and test results. Download generated CSV/PNG/JSON files from the `resilienceai_outputs` folder in Colab's Files panel. Colab storage is temporary.

The first cell installs missing core libraries. No keys, GPU, Google Drive mount or external datasets are needed. Internet is needed only if a package is missing.

## Run locally
```bash
python -m pip install -r requirements.txt
python execute_notebook.py
```
This writes an executed notebook and regenerates all output files. The delivered notebook already includes execution results. The included execution script uses IPython to run every cell in a fresh Python process (without kernel sockets) and fails on cell errors.

## Contents
- `ResilienceAI.ipynb`: generation, ML evaluation, provenance-aware duplicates, structured contradiction rules, source reliability, claim/evidence/status/confidence/escalation ledger, resilience assertions, explanations and plots.
- `resilienceai_outputs/`: all 250 reports, independent fictional source history, pair relations, 50 claim records, test results, run summary and PNG charts.
- `requirements.txt`, `environment_tested.txt`: broad compatible dependencies and exact versions used for the delivered run.

## Methods and limits
TF-IDF + logistic regression classify incident type using text alone. Training and test event IDs are disjoint, with separate wording families. Held-out synthetic metrics do not establish real-world performance. Current claim truth is evaluation-only; it never drives reliability or the evidence ledger.

Structured event, time, location, observation and provenance fields are supplied by the generator. Contradiction detection compares opposing observations in the same 30-minute event/location window; it is not general natural-language inference. Exact/near duplicate components cap evidence contribution. Unknown sources default to a 0.5 heuristic reliability weight. Historical reliability uses Laplace smoothing on fictional past reviewer decisions. Source history is not automatically rewritten from model output.

All classification, source reliability and claim confidence scores are **uncalibrated heuristics**, not probabilities of correctness. Disputed claims always escalate; high-severity claims also require human review. The main dataset deliberately injects opposing evidence for every event. No dispatch or external communication occurs.

Resilience tests cover report count, leakage, abstention, conflict detection, replay amplification, ordering, location/time isolation, missing sources and observations, agreement and confidence bounds. These do not certify operational safety. Use only synthetic data; this educational prototype is unsuitable for real emergency decisions.

## Delivered validation
All 7 code cells executed successfully and all 17 resilience tests passed. Held-out wording-shift classification macro F1: **0.3514** (100 reports, 20 events). This is a weak baseline under vocabulary shift; no classifier-quality threshold is asserted. Google-hosted Colab execution was not available; local execution validated the standard Python notebook cells.
