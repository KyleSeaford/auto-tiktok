import time
import pyautogui
import logging

def findMouse():
    # find screen size
    print(pyautogui.size())
    time.sleep(4)

    # find mouse position
    print(pyautogui.position())


print("Script started")
findMouse()
print("Script ended")

