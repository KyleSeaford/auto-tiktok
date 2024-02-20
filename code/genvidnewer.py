from moviepy.editor import ImageClip, concatenate_videoclips, ColorClip
import os
import random

# Get list of images
image_folder = 'new_memes'
images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith('.jpg')]

# Choose a random image
image_path = os.path.join(image_folder, random.choice(images))

# Create a 7 second video from the image with a 1 second fade-in
image_clip = ImageClip(image_path, duration=5).fadein(3)

# Create a 3 second black screen
black_clip = ColorClip((image_clip.size), col=(0,0,0), duration=0.3)

# Concatenate black screen and image
video = concatenate_videoclips([black_clip, image_clip])

# Write the result to a file with specified fps
video.write_videofile("my_video.mp4", codec='mpeg4', fps=24)