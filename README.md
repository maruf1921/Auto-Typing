# Auto Code Typer using PyAutoGUI

This Python script automatically types out a block of code into any active text editor or IDE window using `pyautogui`.

## 🚀 Features
- Simulates human-like typing by writing the code character by character
- Automatically waits for 5 seconds to allow you to switch to your desired text editor
- Adjustable typing speed via the `interval` parameter

## 🔧 Requirements

Install the required package using pip:

pip install pyautogui
# Auto Code Typer using PyAutoGUI

This Python script automatically types out a block of code into any active text editor or IDE window using `pyautogui`.

## 🚀 Features
- Simulates human-like typing by writing the code character by character
- Automatically waits for 5 seconds to allow you to switch to your desired text editor
- Adjustable typing speed via the `interval` parameter

## 🔧 Requirements

Install the required package using pip:


pip install pyautogui


## ⚠️ Important Notes

- **Turn off auto-indentation** in your text editor to avoid unintended formatting issues. This is especially important in editors like:
  - VS Code
  - PyCharm
  - IDLE
- This script simulates keystrokes and does not interact with the editor's API.
- Be careful when using this script, as it will type wherever the active cursor is.
- Always test with a small snippet before running on important files.
