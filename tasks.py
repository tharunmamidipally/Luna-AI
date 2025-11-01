import os
from datetime import datetime

def perform_task(command):
    command = command.lower()
    
    if "open notepad" in command:
        os.system("notepad")
    elif "time" in command:
        print("Current time:", datetime.now().strftime("%H:%M"))
    # Add more tasks here
