import json
from pathlib import Path
def log_event(event, details=None, path='logs/trace.json'):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    entry = {'event': event, 'details': details}
    try:
        with open(path, 'a') as f:
            f.write(json.dumps(entry) + '\n')
    except Exception:
        pass
