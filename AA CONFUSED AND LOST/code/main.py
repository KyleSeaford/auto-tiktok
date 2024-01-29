from gtts import gTTS
from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, TextClip, AudioFileClip
import os

def text_to_speech_from_file(input_file, output_file, language='en'):
    with open(input_file, 'r') as file:
        text = file.read()

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

    print(f"Text-to-speech generated and saved to: {output_file}")

def trim_video_audio(video_path, audio_path, duration, output_video_path, output_audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    
    # Trim video and audio to match the specified duration
    trimmed_video = video_clip.subclip(0, duration)
    trimmed_audio = audio_clip.subclip(0, duration)
    
    # Write the trimmed video and audio
    trimmed_video.write_videofile(output_video_path, codec='libx264', audio_codec='aac')
    trimmed_audio.write_audiofile(output_audio_path, codec='aac')

def generate_captions(text, video_clip):
    # Create a function to overlay captions on video frames
    def create_caption_frame(txt, fontsize, color='white', bg_color='black', size=None):
        txt_clip = TextClip(txt, fontsize=fontsize, color=color, bg_color=bg_color, size=size)
        return txt_clip.set_pos(('center', 'bottom')).set_duration(video_clip.duration)

    # Generate a list of caption frames
    caption_frames = [create_caption_frame(text, fontsize=24, size=(video_clip.size[0], None))]

    # Create a CompositeVideoClip with the caption frames
    captions_clip = CompositeVideoClip(caption_frames)

    return captions_clip

def combine_video_audio_text(video_path, audio_path, text_path, output_path="output.mp4"):
    # Load video and audio clips
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # Read text from file
    with open(text_path, 'r') as file:
        text = file.read()

    # Generate text clip with captions
    text_clip = generate_captions(text, video_clip)

    # Combine video, audio, and text clips
    final_clip = concatenate_videoclips([video_clip.set_audio(audio_clip), text_clip])
    final_clip = final_clip.set_duration(audio_clip.duration)

    # Write the final video
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage
input_text_file = "stories/story1.txt"
output_audio_file = "output.mp3"
output_video_file = "trimmed_video.mp4"
output_audio_trimmed_file = "trimmed_audio.aac"
final_output_file = "vids/final_output.mp4"

try:
    # Generate text-to-speech audio
    text_to_speech_from_file(input_text_file, output_audio_file)

    # Get the duration of the generated audio
    audio_info = AudioFileClip(output_audio_file)
    audio_duration = audio_info.duration

    # Trim the background video and music
    trim_video_audio("background video/Minecraft Parkour.mp4", "background music/snowfall.mp3", audio_duration, output_video_file, output_audio_trimmed_file)

    # Combine trimmed video, audio, and captions
    combine_video_audio_text(output_video_file, output_audio_trimmed_file, input_text_file, final_output_file)

    print("Video successfully created.")
except Exception as e:
    print(f"An error occurred: {e}")

# Cleanup (optional)
# os.remove(output_video_file)
# os.remove(output_audio_trimmed_file)
