import tkinter as tk
from tkinter import messagebox
import yt_dlp
from moviepy.editor import AudioFileClip
import os

def download_audio(youtube_url, filename):
    try:
        # Create 'audios' folder if it doesn't exist
        if not os.path.exists('audios'):
            os.makedirs('audios')
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join('audios', f'{filename}.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        # Load the audio file
        audio_clip = AudioFileClip(os.path.join('audios', f"{filename}.webm"))
        # Save the audio in mp3 format
        audio_clip.write_audiofile(os.path.join('audios', f"{filename}.mp3"))
        # Close the audio clip
        audio_clip.close()
        messagebox.showinfo("Success", f"Audio downloaded and saved as audios/{filename}.mp3")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry("400x200")

# URL input field
url_label = tk.Label(root, text="YouTube URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Filename input field
filename_label = tk.Label(root, text="Output Filename:")
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download", command=lambda: download_audio(url_entry.get(), filename_entry.get()))
download_button.pack(pady=20)

# Start the main loop
root.mainloop()
