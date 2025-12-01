# kasparro-agentic-fb-analyst-pragathi-murali

**Assignment:** Kasparro — Agentic Facebook Performance Analyst  
**Author:** Allu Pragathi 
This repo implements a small multi-agent system that diagnoses ROAS drops, validates hypotheses,
and proposes creative recommendations for low-CTR campaigns.

**Data**: a sample of the provided synthetic dataset is stored at `data/sample_fb_ads.csv`.
The original uploaded CSV used: `/mnt/data/synthetic_fb_ads_undergarments.csv`.

## Quick start

```bash
python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# Run the default analysis:
python src/orchestrator/run.py "Analyze ROAS drop in last 7 days"
```

## Repo map
- `config/config.yaml` — thresholds and paths.
- `data/sample_fb_ads.csv` — small sample dataset for quick runs.
- `prompts/` — structured prompt files for each agent.
- `src/agents/` — implementation of each agent.
- `src/orchestrator/run.py` — main CLI entrypoint.
- `reports/` — generated `insights.json`, `creatives.json`, `report.md`.
- `logs/` — JSON traces.
- `tests/` — minimal tests for evaluator.

## Reproducibility
- Randomness is seeded in `config/config.yaml`.
- Use the config flag `use_sample_data` to switch between sample and full CSV.

## Evaluation checklist alignment
This repo includes:
- separate agent files and prompt files
- `reports/insights.json`, `reports/creatives.json`, `reports/report.md`
- `logs/trace.json`
- `tests/test_evaluator.py`
- instructions to create a `v1.0` release and a PR titled "self-review".

