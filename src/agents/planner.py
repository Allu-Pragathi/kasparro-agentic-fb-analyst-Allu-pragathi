import json
from pathlib import Path
class PlannerAgent:
    def __init__(self):
        pass
    def run(self, query):
        # very simple planner: return fixed tasks
        plan = {
            "query": query,
            "tasks": [
                {"id": 1, "action": "load_data"},
                {"id": 2, "action": "summarize_roas_trend"},
                {"id": 3, "action": "identify_low_ctr_segments"},
                {"id": 4, "action": "generate_hypotheses"},
                {"id": 5, "action": "validate_hypotheses"},
                {"id": 6, "action": "propose_creatives"}
            ]
        }
        return plan
