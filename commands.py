import os
import subprocess
from datetime import datetime
import webbrowser

import psutil
import pyautogui

from config import load_config, save_config
from memory import Memory
from voice import speak


class CommandHandler:
    def __init__(self, memory, config, tts_engine=None):
        self.memory = memory
        self.config = config
        self.tts_engine = tts_engine

    def confirm(self, action):
        if not self.config.get('ask_permission', True):
            return True
        speak(f"Do you want me to {action}?", self.tts_engine)
        # Simplified confirmation via keyboard input
        resp = input(f"Confirm to {action}? (y/n): ").strip().lower()
        if resp.startswith('y'):
            return True
        return False

    def handle(self, text):
        response = ""
        if not text:
            response = "Sorry, I didn't understand that."
            speak(response, self.tts_engine)
            return response

        lower = text.lower()
        if 'time' in lower:
            now = datetime.now().strftime('%H:%M')
            response = f"It is {now}."
        elif 'weather' in lower:
            # Placeholder for weather logic
            response = "I cannot fetch weather right now."
        elif 'open notepad' in lower:
            if self.confirm('open Notepad'):
                subprocess.Popen('notepad')
                response = 'Opening Notepad.'
            else:
                response = 'Action cancelled.'
        elif 'open calculator' in lower:
            if self.confirm('open Calculator'):
                subprocess.Popen('calc')
                response = 'Opening Calculator.'
            else:
                response = 'Action cancelled.'
        elif 'open chrome' in lower or 'open browser' in lower:
            if self.confirm('open the browser'):
                webbrowser.open('https://www.google.com')
                response = 'Opening browser.'
            else:
                response = 'Action cancelled.'
        elif 'do what you want' in lower or 'no need to ask' in lower:
            self.config['ask_permission'] = False
            save_config(self.config)
            response = 'Okay, I will no longer ask for permission.'
        else:
            response = "This action is not supported."

        speak(response, self.tts_engine)
        self.memory.log(text, response)
        return response

