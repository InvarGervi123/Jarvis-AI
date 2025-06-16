import pyttsx3
import speech_recognition as sr


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


class Listener:
    def __init__(self, language='auto'):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language

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

