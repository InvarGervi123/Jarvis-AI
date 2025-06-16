from config import load_config, save_config
from memory import Memory
from voice import init_tts, speak, Listener
from commands import CommandHandler


def greet(engine, config):
    name = config.get('user_name', 'User')
    speak(f"Hello {name}, how can I help you?", engine)


def main():
    config = load_config()
    memory = Memory()
    engine = init_tts()
    listener = Listener(language=config.get('language', 'auto'))
    handler = CommandHandler(memory, config, tts_engine=engine)

    greet(engine, config)

    while True:
        text = listener.listen()
        response = handler.handle(text)
        if response == 'quit':
            break
        save_config(config)


if __name__ == '__main__':
    main()

