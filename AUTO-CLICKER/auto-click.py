import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Define the key to toggle clicking
TOGGLE_KEY = KeyCode(char="t")

# Initialize clicking status as False
clicking = False
mouse = Controller()

# Function to continuously click the left mouse button when the 'clicking' flag is True
def clicker():
    # Run an infinite loop
    while True:
        # Check if the 'clicking' flag is True
        if clicking:
            # If 'clicking' is True, simulate a left mouse button click (1 click)
            mouse.click(Button.left, 1)
        # Pause for a short duration to control the click rate
        time.sleep(0.01)

# Function to toggle clicking status when the specified key is pressed
def toggle_event(key):
    # Check if the pressed key is the toggle key (in this case, 't')
    if key == TOGGLE_KEY:
        # Access the global variable 'clicking' defined outside this function
        global clicking
        # Toggle the value of 'clicking' (True to False or False to True)
        clicking = not clicking

# Create a thread for the clicker function
click_thread = threading.Thread(target=clicker)
click_thread.start()

# Start listening for key presses to toggle clicking status
with Listener(on_press=toggle_event) as listener:
    listener.join()
