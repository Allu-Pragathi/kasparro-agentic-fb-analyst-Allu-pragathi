class InsightAgent:
    def __init__(self):
        pass
    def run(self, data_summary):
        insights = []
        last = data_summary.get('last7', {})
        prev = data_summary.get('prev7', {})
        # simple heuristic: if roas dropped more than 10% suggest creative fatigue or audience shift
        roas_last = last.get('roas', 0)
        roas_prev = prev.get('roas', 0)
        if roas_prev > 0:
            drop_pct = (roas_prev - roas_last) / roas_prev
        else:
            drop_pct = 0
        if drop_pct > 0.10:
            insights.append({
                "hypothesis": "ROAS drop >10% may be driven by creative fatigue or audience shift",
                "reasoning": f"ROAS change {drop_pct:.2f}",
                "evidence_needed": ["ctr_trend", "spend_shift"]
            })
        # if low_ctr_campaigns exists, suggest creative refresh
        low = data_summary.get('low_ctr_campaigns', [])
        if low:
            for c in low:
                insights.append({
                    "hypothesis": f"Campaign '{c}' has low CTR and may benefit from creative refresh",
                    "reasoning": "CTR below configured threshold",
                    "evidence_needed": ["ctr_by_campaign", "creative_samples"]
                })
        return insights
