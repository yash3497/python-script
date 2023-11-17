import pyautogui
import time
import random

def jiggle_mouse():
    while True:
        # Generate random displacement values for x and y coordinates
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Calculate the new position by adding the displacement values
        new_x = x + dx
        new_y = y + dy
        
        # Move the mouse to the new position
        pyautogui.moveTo(new_x, new_y, duration=0.1)
        
        # Wait for 10 seconds before jiggling the mouse again
        time.sleep(30)

# Start jiggling the mouse
jiggle_mouse()
