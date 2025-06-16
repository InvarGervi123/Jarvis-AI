import json
from pathlib import Path

CONFIG_PATH = Path('config.json')

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'user_name': 'Invar',
        'ask_permission': True,
        'language': 'auto'
    }

def save_config(config):
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

