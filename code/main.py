import logging
import os
import datetime
import pyautogui as pg
import time

from genvid  import meme
from emailKYLE_tt import sendlogTOkyle


# Set logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./ZZ_logs/gen.log', filemode='w')


def main():
    meme() # Generate the video


logging.critical("Script running at " + str(datetime.datetime.now()))
logging.warning(f"The screen size is: {pg.size()}")
main()
logging.critical("Script ended at:  " + str(datetime.datetime.now()))

#sendlogTOkyle()
#time.sleep(5)