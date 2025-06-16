import json
from pathlib import Path
from datetime import datetime

HISTORY_PATH = Path('history.json')

class Memory:
    def __init__(self):
        self.history = []
        if HISTORY_PATH.exists():
            with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
                self.history = json.load(f)

    def log(self, user_input, response):
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'input': user_input,
            'response': response
        }
        self.history.append(entry)
        with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

