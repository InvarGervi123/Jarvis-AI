import json
from pathlib import Path


class Config:
    """Manage user configuration settings."""

    def __init__(self, path: str = "config.json"):
        self.path = Path(path)
        self.data = {
            "user_name": "Invar",
            "ask_permission": True,
            "language": "auto",  # could be "he" "ru" "en" or "auto"
        }
        self.load()

    def load(self) -> None:
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.data.update(json.load(f))
            except json.JSONDecodeError:
                pass

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def __getitem__(self, item):
        return self.data.get(item)

    def __setitem__(self, key, value) -> None:
        self.data[key] = value
        self.save()
