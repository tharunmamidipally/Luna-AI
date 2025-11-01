import threading
import time
import pyttsx3

from listener import Listener
from conversation import get_response
from tasks import perform_task
from gui import LunaGUI
from config import AUTO_SLEEP_TIMEOUT

# Initialize
listener = Listener()
gui = LunaGUI()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def assistant_loop():
    active = False
    last_active_time = None

    while True:
        if not active:
            # Listen for wake word
            if listener.listen_wake_word():
                active = True
                listener.active = True
                gui.start_ripple()
                speak("Hello! I am Luna. How can I help you?")
                last_active_time = time.time()
        else:
            # Continuous listening
            command = listener.listen_command()
            if command:
                print("You:", command)
                last_active_time = time.time()

                # Run response + task in parallel
                threading.Thread(target=lambda: speak(get_response(command))).start()
                threading.Thread(target=lambda: perform_task(command)).start()

            # Auto-sleep after inactivity
            if last_active_time and time.time() - last_active_time > AUTO_SLEEP_TIMEOUT:
                active = False
                listener.active = False
                gui.stop_ripple()
                print("Going to sleep...")
                speak("Going to sleep. Call me when you need me!")

# Run GUI in parallel
threading.Thread(target=gui.run).start()
assistant_loop()
