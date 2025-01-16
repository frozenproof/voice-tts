import os
from pydub import AudioSegment
from datetime import datetime

def get_timestamp():
    return datetime.utcnow().strftime('%Y%m%d_%H%M%S')

def concatenate_audio_files(input_folder, output_file):
    # List all files in the directory
    audio_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp3', '.ogg'))]

    # Sort files to maintain order (optional)
    audio_files.sort()

    # Initialize an empty AudioSegment
    combined_audio = AudioSegment.empty()

    # Loop through the audio files
    for file in audio_files:
        file_path = os.path.join(input_folder, file)
        print(f"Processing: {file_path}")
        
        # Load the audio file (MP3 or OGG)
        audio = AudioSegment.from_file(file_path)
        
        # Append the audio to the combined track
        combined_audio += audio

    # Export the final combined audio to the output file
    combined_audio.export(output_file, format="mp3")
    print(f"Audio concatenation completed. Output saved as: {output_file}")

# Define the input folder and output file path
input_folder = 'samplers'  # Replace with your folder path
output_file = f'voices_output/{input_folder}.mp3'  # Replace with your desired output path

concatenate_audio_files(input_folder, output_file)
