import os
import random
import time
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Function to create a transparent frame
def create_transparent_frame(size, color=(0, 0, 0, 0)):
    return Image.new('RGBA', size, color)

# Function to create a fade-in effect
def fade_in(image, fade_duration=4):
    alpha_step = 255 / (fade_duration * 2)

    for i in range(int(fade_duration * 2) + 1):
        new_image = create_transparent_frame(image.size)
        alpha = int(255 - (i * alpha_step))
        new_image = Image.alpha_composite(new_image, image.convert('RGBA'))
        yield new_image

# Function to create a fade-out effect
def fade_out(image, fade_duration=4):
    alpha_step = 255 / (fade_duration * 2)

    for i in range(int(fade_duration * 2) + 1):
        new_image = create_transparent_frame(image.size)
        alpha = int((i * alpha_step))
        new_image = Image.alpha_composite(new_image, image.convert('RGBA'))
        yield new_image

# Set the directory containing memes
meme_dir = "new_memes"

# Get a list of meme files
meme_files = [f for f in os.listdir(meme_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Choose a random meme
random_meme = random.choice(meme_files)

# Open the meme
meme_path = os.path.join(meme_dir, random_meme)
meme_image = Image.open(meme_path)

# Calculate the size of the output video
video_size = (meme_image.width, meme_image.height)

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('output.mp4', fourcc, 24, video_size)

# Create the fade-in effect
fade_in_generator = fade_in(meme_image)

# Write frames to the video
total_frames = 8  # Show the meme for 8 seconds with a 24 FPS video
frame_count = 0

# Fade in
while frame_count < 8 * 24 / 2:
    try:
        frame = next(fade_in_generator)
    except StopIteration:
        fade_in_generator = fade_in(meme_image)
        frame = next(fade_in_generator)

    frame_count += 1
    video_writer.write(np.array(frame))

# Show the meme
for _ in range(total_frames):
    video_writer.write(np.array(meme_image))
    frame_count += 1

# Create the fade-out effect
fade_out_generator = fade_out(meme_image)

# Fade out
while frame_count < 8 * 24:
    try:
        frame = next(fade_out_generator)
    except StopIteration:
        fade_out_generator = fade_out(meme_image)
        frame = next(fade_out_generator)

    frame_count += 1
    video_writer.write(np.array(frame))

# Release the VideoWriter object
time.sleep(1)  # Wait for 1 second before releasing the VideoWriter
video_writer.release()