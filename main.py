from config import load_config, save_config
from memory import Memory
from voice import (
    init_tts,
    speak,
    Listener,
    list_microphone_names,
    choose_microphone_gui,
    print_available_microphones,
)
from commands import CommandHandler


def greet(engine, config):
    name = config.get('user_name', 'User')
    speak(f"Hello {name}, how can I help you?", engine)


def main():
    config = load_config()
    memory = Memory()
    engine = init_tts()
    print_available_microphones()
    mic_names = list_microphone_names()
    if not config.get('microphone_name') or config['microphone_name'] not in mic_names:
        choice = choose_microphone_gui(mic_names)
        if choice:
            config['microphone_name'] = choice
            save_config(config)

    listener = Listener(
        language=config.get('language', 'auto'),
        microphone_name=config.get('microphone_name'),
    )
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

