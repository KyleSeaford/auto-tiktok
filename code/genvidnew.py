import random
from moviepy.editor import ImageSequenceClip
import os

# Get list of images
image_folder = 'new_memes'
images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith('.jpg')]

# Sort the images by name
index = random.randint(0, len(images))
print("index=", index)
print("images before=", images)
images = [images[index]]
print("images after=", images)

# Add image folder path to each image name
images = [os.path.join(image_folder, img) for img in images]
print("images after after=", images)

# Make video
clip = ImageSequenceClip(images, fps=24)  # Change fps for speed

# Add transition between images
clip = clip.crossfadein(3)  # 1 second crossfade

# Write the result to a file
clip.write_videofile("video.mp4", codec='mpeg4')