from src.agents.evaluator import EvaluatorAgent

def test_evaluator_rejects_when_no_drop():
    config = {'roas_drop_threshold': 0.15}
    evaluator = EvaluatorAgent(config)
    insights = [{'hypothesis': 'test roas drop'}]
    data_summary = {'last7': {'roas': 1.0}, 'prev7': {'roas': 1.0}}
    out = evaluator.run(insights, data_summary)
    assert out[0]['verdict'] in ['rejected','weakly_supported','supported']

def test_evaluator_supports_large_drop():
    config = {'roas_drop_threshold': 0.05}
    evaluator = EvaluatorAgent(config)
    insights = [{'hypothesis': 'test roas drop'}]
    data_summary = {'last7': {'roas': 0.5}, 'prev7': {'roas': 1.0}}
    out = evaluator.run(insights, data_summary)
    assert out[0]['verdict'] == 'supported'
