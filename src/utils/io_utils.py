import json
from pathlib import Path
def load_config(path='config/config.yaml'):
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)

def write_json(path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)
