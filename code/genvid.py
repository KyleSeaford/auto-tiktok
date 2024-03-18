from moviepy.editor import ImageSequenceClip, concatenate_videoclips
import os
import random
import logging
import pyautogui


# Set logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./ZZ_logs/gen.log', filemode='w')

def select_random_meme(folder_path, selected_memes):
    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        logging.error("No meme images found in the folder.")
        return None

    available_memes = list(set(image_files) - set(selected_memes))

    if not available_memes:
        logging.warning("All memes have been used. Resetting selection.")
        selected_memes.clear()
        available_memes = image_files

    random_meme = random.choice(available_memes)
    return random_meme

def create_video(selected_memes):
    meme_folder_path = "new_memes"
    clips = []

    for meme_name in selected_memes:
        meme_path = os.path.join(meme_folder_path, meme_name)
        clips.append(ImageSequenceClip([meme_path], fps=0.5))  # 0.5 frames per second, 2 seconds per frame

    # Create the video with slide transitions
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("video.mp4", codec='libx264', audio_codec='aac', fps=24)  # 24 frames per second

def meme():
    selected_memes = []

    for _ in range(5):
        random_meme_name = select_random_meme("./new_meme", selected_memes)
        if random_meme_name:
            selected_memes.append(random_meme_name)
            logging.info(f"Selected meme: {random_meme_name}")

    create_video(selected_memes)
    logging.info(f"Video created: video.mp4")
