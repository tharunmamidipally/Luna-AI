import speech_recognition as sr
from config import WAKE_WORD

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.active = False

    def listen_wake_word(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source, phrase_time_limit=3)
        try:
            text = self.recognizer.recognize_google(audio).lower()
            if WAKE_WORD in text:
                self.active = True
                return True
        except:
            return False
        return False

    def listen_command(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source, phrase_time_limit=5)
        try:
            return self.recognizer.recognize_google(audio)
        except:
            return ""
