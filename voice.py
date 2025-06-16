import pyttsx3
import speech_recognition as sr
import tkinter as tk



def init_tts():
    engine = pyttsx3.init()
    # Set Jarvis-like voice if available
    for voice in engine.getProperty('voices'):
        if 'David' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)
    return engine


def speak(text, engine=None):
    if engine is None:
        engine = init_tts()
    print(text)
    engine.say(text)
    engine.runAndWait()


def list_microphone_names():
    return sr.Microphone.list_microphone_names()


def choose_microphone_gui(names):
    root = tk.Tk()
    root.title("Select Microphone")
    var = tk.StringVar(value=names)
    listbox = tk.Listbox(root, listvariable=var, height=len(names))
    listbox.pack()

    result = {'name': None}

    def on_select():
        selection = listbox.curselection()
        if selection:
            result['name'] = names[selection[0]]
            root.destroy()

    btn = tk.Button(root, text="OK", command=on_select)
    btn.pack()
    root.mainloop()
    return result['name']


def print_available_microphones():
    names = list_microphone_names()
    for idx, name in enumerate(names):
        print(f"{idx}: {name}")

class Listener:
    def __init__(self, language='auto', microphone_name=None):
        self.recognizer = sr.Recognizer()
        self.language = language

        mic_names = list_microphone_names()
        device_index = None
        if microphone_name and microphone_name in mic_names:
            device_index = mic_names.index(microphone_name)

        self.microphone = sr.Microphone(device_index=device_index)

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            if self.language == 'auto':
                return self.recognizer.recognize_google(audio)
            else:
                return self.recognizer.recognize_google(audio, language=self.language)
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None


