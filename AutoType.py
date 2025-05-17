import pyautogui
import time

# The code to be typed
code = """
"""

# Give time to switch to text editor
print("Switch to your text editor within 5 seconds...")
time.sleep(5)

# Type the code with proper delays
pyautogui.write(code, interval=0.08)  # 0.08 second delay between characters