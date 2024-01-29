from gtts import gTTS
import os
import time 

def convert_text_to_speech(file_path, output_directory="textToSpeech", language='en'):
    with open(file_path, 'r') as file:
        text = file.read()

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    os.makedirs(output_directory, exist_ok=True)

    output_file_path = os.path.join(output_directory, f"{file_name}_output.mp3")

    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file_path)

    print(f"Text-to-speech generated for {file_name}.")


def convert_all_txt_to_speech(directory_path="stories", output_directory="textToSpeech", language='en'):
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(directory_path, file_name)
            convert_text_to_speech(file_path, output_directory, language)

convert_all_txt_to_speech()
