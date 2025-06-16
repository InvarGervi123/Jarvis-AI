import pyttsx3
import speech_recognition as sr


class VoiceAssistant:
    """Handle speech input and output."""

    def __init__(self, language: str = "en-US"):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.language = language
        # slower rate for clarity
        self.engine.setProperty('rate', 150)

    def listen(self) -> str:
        """Listen from the default microphone and return recognized text."""
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio, language=self.language)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            # Fallback to console when network is unavailable
            return input("(no internet) Type command: ")

    def say(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()
