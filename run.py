import sys
from pathlib import Path

# repo root is two levels up from this file: <repo>/src/orchestrator/run.py
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import argparse
from src.utils.io_utils import load_config, write_json
from src.utils.logging_utils import log_event
from src.agents.planner import PlannerAgent
from src.agents.data_agent import DataAgent
from src.agents.insight_agent import InsightAgent
from src.agents.evaluator import EvaluatorAgent
from src.agents.creative_generator import CreativeGenerator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str)
    args = parser.parse_args()

    config = load_config('config/config.yaml')
    log_event('planner_start', {'query': args.query})
    planner = PlannerAgent()
    plan = planner.run(args.query)

    log_event('data_agent_start')
    data_agent = DataAgent(config)
    data_summary = data_agent.run()

    log_event('insight_agent_start')
    insight_agent = InsightAgent()
    insights = insight_agent.run(data_summary)

    log_event('evaluator_start')
    evaluator = EvaluatorAgent(config)
    evaluated = evaluator.run(insights, data_summary)
    write_json('reports/insights.json', evaluated)

    log_event('creative_gen_start')
    creative_gen = CreativeGenerator()
    creatives = creative_gen.run(data_summary)
    write_json('reports/creatives.json', creatives)

    # create simple report
    with open('reports/report.md', 'w') as f:
        f.write('# Facebook Ads Performance Report\n\n')
        f.write('## Context\n')
        f.write(f"Data last date: {data_summary.get('max_date')}\n\n")
        f.write('## Validated Insights\n')
        import json
        f.write(json.dumps(evaluated, indent=2))
        f.write('\n\n## Creative Recommendations\n')
        f.write(json.dumps(creatives, indent=2))

    print('Report generated at reports/report.md')

if __name__ == '__main__':
    main()
