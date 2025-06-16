import json
from pathlib import Path
from datetime import datetime


class MemoryManager:
    """Logs interactions and loads history."""

    def __init__(self, path: str = "history.json"):
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def log(self, query: str, response: str) -> None:
        """Append a log entry."""
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = []
        entry = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "response": response,
        }
        data.append(entry)
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def get_history(self):
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
