import os
# from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

video_dir = r"D:\Diploma\data\MC-EIU"
audio_dir = r"D:\Diploma\data\MC-EIU-audio"

os.makedirs(audio_dir, exist_ok=True)

video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv')

for filename in os.listdir(video_dir):
    if filename.lower().endswith(video_extensions):
        video_path = os.path.join(video_dir, filename)
        audio_path = os.path.join(audio_dir, os.path.splitext(filename)[0] + ".mp3")
        # print(f"Converting: {filename} -> {audio_path}")
        try:
            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path)
            clip.close()
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Conversion complete")
