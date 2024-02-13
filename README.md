# TikTok Auto-Posting Bot with Random Captions and Hashtags
This script is an automation tool for generating and posting meme videos on TikTok with random captions and hashtags. It uses the PyAutoGUI library to control the mouse and keyboard to interact with the TikTok website.

## Prerequisites - need to do before running
- The `meme` folder, `genvid.py`, and `emailKYLE_tt.py` should be in the same directory as this file.
- The `meme` folder should be edited with the `ResizeMeme.py` script.
-The `new_memes` folder should be created.
- Ensure all the directories are correct in all scripts.

## Setup
- Install the required libraries 
- This is the libury that manipulates the mouse and keyboard, be sure to check out my [Pyautogui Reposotory](https://github.com/KyleSeaford/Pyautogui-KS) To Learn More:
```bash
pip install pyautogui
```
- Edit the `ResizeMeme.py` script to resize the meme videos to the required dimensions for TikTok, It is ster to 1080 x 1920 as default
- Create a `ZZ_logs` folder (like the one in the reposotiry)  in the same directory as this script to store the log files.

## Usage
Run the script, and it will:

- Generate a meme video using the `genvid.py` script.
- Open the TikTok website in a web browser.
- Open the meme folder and select a meme video.
- Select a sound for the meme video.
- Write a random caption for the meme video.
- Write random hashtags for the meme video.
- Post the meme video on TikTok.
- Send the log file to Kyle using the `emailKYLE_tt.py` script.
- The script logs its actions and errors to a log file named `gen.log` in the `ZZ_logs` folder.

### Note
This script is for educational purposes only and should not be used to spam or violate TikTok's terms of service. The user is responsible for any actions taken using this script.