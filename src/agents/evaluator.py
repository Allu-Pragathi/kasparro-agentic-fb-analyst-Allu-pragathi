class EvaluatorAgent:
    def __init__(self, config):
        self.config = config or {}
    def run(self, insights, data_summary):
        evaluated = []
        for ins in insights:
            hyp = ins.get('hypothesis')
            evidence = {}
            confidence = 0.0
            verdict = "unknown"
            if 'low CTR' in hyp or 'low CTR' in ins.get('reasoning',''):
                # check campaign ctr
                name = None
                # try to parse name
                if "'" in hyp:
                    try:
                        name = hyp.split("'")[1]
                    except:
                        name = None
                if name:
                    ctr = data_summary.get('ctr_by_campaign',{}).get(name, 0)
                    evidence['ctr'] = ctr
                    thresh = self.config.get('ctr_low_threshold', 0.012)
                    if ctr < thresh:
                        confidence = 0.8
                        verdict = 'supported'
                    else:
                        confidence = 0.2
                        verdict = 'rejected'
            else:
                # treat as ROAS drop hypothesis
                last = data_summary.get('last7',{})
                prev = data_summary.get('prev7',{})
                roas_last = last.get('roas',0)
                roas_prev = prev.get('roas',0)
                if roas_prev>0:
                    drop = (roas_prev - roas_last) / roas_prev
                else:
                    drop = 0
                evidence['roas_drop_pct'] = drop
                if drop > self.config.get('roas_drop_threshold',0.15):
                    confidence = 0.85
                    verdict = 'supported'
                elif drop > (self.config.get('roas_drop_threshold',0.15)/2):
                    confidence = 0.6
                    verdict = 'weakly_supported'
                else:
                    confidence = 0.15
                    verdict = 'rejected'
            evaluated.append({
                "hypothesis": hyp,
                "evidence": evidence,
                "confidence": confidence,
                "verdict": verdict
            })
        return evaluated
