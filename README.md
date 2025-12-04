# kasparro-agentic-fb-analyst-allu-pragathi

**Assignment:** Kasparro — Agentic Facebook Performance Analyst  
**Author:** Allu Pragathi 
This repo implements a complete multi-agent analytics system that analyzes Facebook Ads performance, diagnoses CTR/ROAS drops, validates hypotheses with strong evidence, and proposes creative recommendations linked to the actual performance drivers.

A full V2-grade pipeline is included: schema governance, insight generation, evaluator with confidence/impact/verdict, driver detection, prioritization, logging, and reproducible reporting.

## Quick start

```bash
python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
## Run the analysis:
```bash
python run.py "why did CTR drop?"
or run without a query:
python run.py
```
Outputs will be generated under reports/ and logs/run_<timestamp>/.

## Repo map
- `config/config.yaml` —  global thresholds, lookbacks and paths.
- `config/schema.json` — required columns, nullable fields, datatype expectations.
- `data/sample_fb_ads.csv` — small sample dataset for quick runs.
- `src/agents/` — implementation of each agent.
   - planner.py
   - dat_agent.py
   - insight_agent.py
   - evaluator.py
   - creative_generator.py 
- `src/utils/` — support utilities:
   - io_utils.py
   - logging_utils.py
   - safe_call.py
- `reports/` — generated
   - insights.json
   - creatives.json
   - report.md
- `logs/` — JSON traces.
- `tests/` — includes test_evaluator.py.

## Reproducibility
- All thresholds, windows, parameters, and random seeds are controlled through config/config.yaml.
- Data loading supports both sample and full datasets.
- Each pipeline run creates a new folder under logs/run_<timestamp>/, containing:
  - input summaries
  - schema validation messages
  - synthesized column warnings
  - coercion warnings
  - raw insights + validated insights
  - creative recommendations
- reports/top_insights.json surfaces the strongest insights for quick reviewer evaluation.

## Evaluation checklist alignment
This V2 submission includes:
- Proper agent separation and modular design
- Strong evaluator:
  - evidence (baseline/current CTR, deltas, impressions)
  - impact classification
  - confidence scoring
  - verdict generation
  - driver detection across multiple dimensions
- Robust schema validation (alias handling, type coercion, default synthesis)
- Full observability:
  - per-run logs
  - warnings for missing or coerced columns
  - safe_call wrappers for all agents
- Generated artifacts:
  - reports/insights.json
  - reports/top_insights.json
  - reports/creatives.json
  - reports/report.md
- Passing tests (pytest -q → 3 passed)
- Instructions to prepare:
  - v1.0 GitHub release
  - PR titled "self-review — Kasparro V2 submission"
