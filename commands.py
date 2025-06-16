import subprocess
import webbrowser
import datetime
from typing import Optional


class CommandHandler:
    """Parse and execute user commands."""

    def __init__(self, config, voice, memory):
        self.config = config
        self.voice = voice
        self.memory = memory

    def confirm(self, prompt: str) -> bool:
        if not self.config["ask_permission"]:
            return True
        self.voice.say(prompt)
        resp = self.voice.listen().lower()
        return resp in {"yes", "sure", "ok", "okay"}

    def handle(self, text: str) -> Optional[str]:
        text_lower = text.lower()
        if "time" in text_lower:
            now = datetime.datetime.now().strftime("%H:%M")
            return f"It is {now}"
        if "weather" in text_lower:
            return "I cannot check the weather right now."
        if "notepad" in text_lower:
            if self.confirm("Open Notepad?"):
                subprocess.Popen(["notepad.exe"])
                return "Opening Notepad"
            else:
                return "Cancelled"
        if "calculator" in text_lower:
            if self.confirm("Open Calculator?"):
                subprocess.Popen(["calc.exe"])
                return "Opening Calculator"
            else:
                return "Cancelled"
        if "open" in text_lower and "youtube" in text_lower:
            if self.confirm("Open YouTube in browser?"):
                webbrowser.open("https://www.youtube.com")
                return "Opening YouTube"
            else:
                return "Cancelled"
        return None
