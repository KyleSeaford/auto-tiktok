##############################################################################
#    ensure the meme folder, genvid.py and emailKYLE_tt.py are in the same   #
#    directory as this file and that the meme folder has been eddited with   #
#    "ResizeMeme.py" and that the folder "new_memes" has been created.       #
#    ensusre all the directories are correct in all scripts                  #
##############################################################################

import logging
import os
import datetime
import pyautogui as pg
import time
import webbrowser
import random

from genvid  import meme
from emailKYLE_tt import sendlogTOkyle

wait = 8
mouse_deration = 1

# Set logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./ZZ_logs/gen.log', filemode='w')

def openTT():
    webbrowser.open('https://www.tiktok.com/creator-center/upload?from=upload')
    time.sleep(wait)
    logging.info("TikTok opened")

def SelectedMeme():
    pg.moveTo(1081, 640, duration=mouse_deration) 
    pg.click()
    #pg.typewrite('I:\\CODE\\auto-tiktok2\\auto-tiktok')
    #pg.press('enter')
    logging.info("Meme folder opened")
    time.sleep(wait)
    pg.moveTo(581, 973, duration=mouse_deration)
    pg.click()
    pg.typewrite('video.mp4')
    pg.press('enter')
    time.sleep(wait)
    logging.info("Meme selected")

def selectSound():
    pg.moveTo(973, 250, duration=mouse_deration) 
    pg.click()
    time.sleep(wait)
    pg.moveTo(832, 345, duration=mouse_deration)
    pg.click()
    pg.moveTo(839, 401, duration=mouse_deration)
    pg.click()
    time.sleep(wait)
    pg.moveTo(1365, 231, duration=mouse_deration)
    pg.click()
    logging.info("Sound selected")

def writeCaption():
    captions = [
        "Bug squashed, another arises", 
        "Risking it all with an update", 
        "Break? Just switch code types", 
        "Not a bug, a feature!", 
        "how did this ever work?",
        "To err is human, to debug divine",
        "Code like a butterfly, test like a bee",
        "In the kingdom of code, the debugger is king",
        "The only thing we have to fear is uncaught exceptions",
        "Coding is thinking, not typing",
        "The code is dark and full of errors",
        "Keep calm and trust the debugger",
        "Code it, break it, fix it, repeat",
        "Coding: Where every character counts",
        "May the source be with you: The coder's blessing",
        "In the quest for perfection, we debug endlessly",
        "Code: It's not a bug, it's an undocumented feature",
        "Embracing the beauty of data chaos",
        "Plot twist: Data speaks for itself",
        "Visualizing the invisible: Data magic",
        "In data we trust, in visualizations we marvel",
        "Unveiling patterns, one data point at a time",
        "When numbers become art: The power of visualization",
        "Data whispers, visualizations shout",
        "Lost in the scatter: Finding meaning in the chaos",
        "A symphony of data points: Visualizing harmony",
        "Where data and design dance together",
        "The art of storytelling through data visualizations",
        "Decoding the data: A visual journey",
        "From raw data to visual poetry",
        "When dots connect: The power of visual narratives",
        "Data alchemy: Turning numbers into gold",
        "The language of data: Spoken in visuals",
        "Unveiling the hidden: The art of data revelation",
        "When data takes center stage: The visual spotlight",
        "In the realm of visual insights: Where data comes to life"
    ]
    
    random_caption = random.choice(captions)
    logging.info(f"Caption selected: {random_caption}")

    pg.moveTo(1233, 482, duration=mouse_deration)
    pg.click()
    time.sleep(0.2)
    pg.click()          # clear caption
    time.sleep(0.2)
    pg.click()
    logging.info("Caption cleared")
    pg.typewrite(random_caption)
    time.sleep(wait)
    pg.press('enter')
    pg.press('enter')
    logging.info("Caption written")

def writeHashtags():

    hashtags = [
    "#CodeHumor", "#GeekHumor", "#TechJokes", "#DevLife", 
    "#ProgrammerLife", "#ProgrammingHumor", "#ProgrammingJokes", 
    "#ProgrammerHumor", "#SoftwareDeveloper", "#SoftwareEngineer", 
    "#SoftwareDevelopment", "#SoftwareEngineerLife", "#SoftwareEngineerProblems", 
    "#SoftwareEngineerHumor", "#SoftwareEng" ,"#SoftwareEngineering", 
    "#programming", "#joke", "#funny", "#coding", "#programmer", "#developer",         
    "#codinglife", "#webdeveloper", "#webdevelopment", 
    "#webdev", "#webdesign", "#webdesigner", "#webdesigning", 
    "#webdesignlife", "#webdesignerlife", "#webdesigners", 
    "#webdesignerslife", "#webdesignersofinstagram", "#webdesignersofinsta", 
    "#webdesignersoftheworld", "#webdesignersoftheworld", "#webdesignersoftheworldunite",
    "#computer", "#computers", "#computerscience", "#computersciencestudent",
    "#python", "#pythonprogramming", "#pythonprogramminglanguage", "#pythonprogrammer",
    "#code", "#coder", "#codingisfun", "#codingpics", "#c", "#csharp", "#csharpdeveloper",
    "#meme", "#memes", "#memesdaily", "#memes4days", "#memes4life", "#memes4ever", "#memes4u",
    ]

    random_hashtags = random.sample(hashtags, 4)  # Select 6 unique hashtags from the list
    random_hashtag1, random_hashtag2, random_hashtag3, random_hashtag4 = random_hashtags
     
    logging.info(f"Hashtags selected: {random_hashtags}")

    time.sleep(wait)
    pg.typewrite(random_hashtag1)
    time.sleep(wait)
    pg.moveTo(1141, 558, duration=mouse_deration)
    pg.click()
    time.sleep(wait)
    logging.info(f"Hashtag 1: {random_hashtag1} written")
    pg.typewrite(random_hashtag2)
    time.sleep(wait)
    pg.moveTo(1141, 558, duration=mouse_deration)
    pg.click()
    time.sleep(wait)
    logging.info(f"Hashtag 2: {random_hashtag2} written")
    pg.typewrite(random_hashtag3)
    time.sleep(wait)
    pg.moveTo(1141, 558, duration=mouse_deration)
    pg.click()
    time.sleep(wait)
    logging.info(f"Hashtag 3: {random_hashtag3} written")
    pg.typewrite(random_hashtag4)
    time.sleep(wait)
    pg.moveTo(1141, 558, duration=mouse_deration)
    pg.click()
    time.sleep(wait)
    logging.info(f"Hashtag 4: {random_hashtag4} written")



def post():
    time.sleep(wait)
    pg.scroll(-400)
    logging.info("Scrolling down")
    time.sleep(wait)
    pg.moveTo(1146, 809, duration=mouse_deration)
    pg.click()
    time.sleep(wait)
    logging.info("Post button clicked")

    

def main():
    meme()              # Generate the video
    openTT()            # Open TikTok
    SelectedMeme()      # Select meme
    selectSound()       # Select sound
    writeCaption()      # Write caption
    writeHashtags()     # Write hashtags
    post()              # Post video
    sendlogTOkyle()     # Send log to Kyle



logging.critical("Script running at " + str(datetime.datetime.now()))
logging.warning(f"The screen size is: {pg.size()}")
main()
logging.critical("Script ended at:  " + str(datetime.datetime.now()))
