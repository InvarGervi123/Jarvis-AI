"""Entry point for the AI assistant."""

from config import Config
from voice import VoiceAssistant
from memory import MemoryManager
from commands import CommandHandler


def main():
    config = Config()
    voice = VoiceAssistant()
    memory = MemoryManager()
    commands = CommandHandler(config, voice, memory)

    voice.say(f"Hello {config['user_name']}. How can I help you?")

    while True:
        text = voice.listen()
        if not text:
            continue
        response = commands.handle(text)
        if not response:
            response = "Sorry, I didn't understand that."
        voice.say(response)
        memory.log(text, response)


if __name__ == "__main__":
    main()
