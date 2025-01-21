import time
from datetime import datetime
import pyautogui

DURATION = 60  # Duration in seconds
while True:

    # Get the current mouse position
    current_position = pyautogui.position()

    # Move the mouse slightly to simulate activity
    pyautogui.moveTo(current_position.x + 10, current_position.y + 10, duration=0.5)
    pyautogui.moveTo(current_position, duration=0.5)  # Move back to the original position

    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")  # Format: Hour:Minute:Second
    print("Mouse moved!: ", formatted_time)
    time.sleep(DURATION)  # Wait for the specified duration before moving the mouse again
