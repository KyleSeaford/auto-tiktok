import time
import pyautogui
import logging

logging.basicConfig(level=logging.DEBUG,  
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./ZZ_logs/mouse.log', filemode='w')


def findMouse():
    # find screen size
    logging.info(pyautogui.size())
    time.sleep(4)

    # find mouse position
    logging.info(pyautogui.position())


logging.info("Script started")
findMouse()

