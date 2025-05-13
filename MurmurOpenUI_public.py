"""
MurmurOpenUI
A lightweight, open-source macOS Python GUI for running OpenAI’s Whisper models.

Created: May 2025
Author: thegitmate
GitHub: https://github.com/thegitmate/MurmurOpenUI
Version: Beta 2

This script provides a simple tkinter-based interface for transcribing audio using Whisper.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import whisper
import threading
import warnings
import time

# Ignore non-important warning for a clean terminal
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Ensure ffmpeg is available on macOS
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

# Default output folder = Downloads
default_output_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Available models
# Add models to the following list if you downloaded them but they are not listed
available_models = ["tiny", "base", "small", "medium", "large", "large-v3-turbo"]

# Output formats
output_formats = ["txt", "srt", "vtt", "json"]

# Languages (mapped to Whisper codes)
# Add languages if needed
language_options = {
    "automatic": None,
    "english": "en",
    "french": "fr",
    "spanish": "es",
    "korean": "ko"
}

# Helper: format timestamps for SRT/VTT
def format_timestamp(seconds, vtt=False):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    millis = int((seconds - int(seconds)) * 1000)
    if vtt:
        return f"{hours:02}:{minutes:02}:{int(seconds):02}.{millis:03}"
    else:
        return f"{hours:02}:{minutes:02}:{int(seconds):02},{millis:03}"

# Timer thread to update elapsed time label
def start_timer():
    start = time.time()
    def update():
        elapsed = int(time.time() - start)
        mins, secs = divmod(elapsed, 60)
        time_label.config(text=f"Time elapsed: {mins:02}:{secs:02}")
        if transcription_running[0]:
            root.after(1000, update)
    update()

# Transcription logic
def transcribe_file(model_name, file_path, output_folder, output_format, language_code):
    try:
        model = whisper.load_model(model_name)
        result = model.transcribe(file_path, language=language_code)
        filename = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_folder, filename + f".{output_format}")

        if output_format == "txt":
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["text"])
        elif output_format == "srt":
            with open(output_path, "w", encoding="utf-8") as f:
                for segment in result["segments"]:
                    start = format_timestamp(segment["start"])
                    end = format_timestamp(segment["end"])
                    f.write(f"{segment['id'] + 1}\n{start} --> {end}\n{segment['text'].strip()}\n\n")
        elif output_format == "vtt":
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("WEBVTT\n\n")
                for segment in result["segments"]:
                    start = format_timestamp(segment["start"], vtt=True)
                    end = format_timestamp(segment["end"], vtt=True)
                    f.write(f"{start} --> {end}\n{segment['text'].strip()}\n\n")
        elif output_format == "json":
            import json
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

        messagebox.showinfo("Success", f"Saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        transcription_running[0] = False
        time_label.config(text="")

# Start transcription thread + timer
def start_transcription():
    model_name = model_var.get()
    file_path = file_var.get()
    output_folder = output_var.get()
    output_format = format_var.get()
    language_label = language_var.get()
    language_code = language_options[language_label]

    if not file_path:
        messagebox.showwarning("Warning", "Please select a file.")
        return

    transcription_running[0] = True
    threading.Thread(target=transcribe_file, args=(model_name, file_path, output_folder, output_format, language_code)).start()
    start_timer()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Media files", "*.mp3 *.mp4 *.wav *.m4a *.mkv")])
    if file_path:
        file_var.set(file_path)

def browse_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_var.set(folder)

# GUI Setup
root = tk.Tk()
root.title("Whisper Transcriber")

# Shared state for timer
transcription_running = [False]

# Model selection
tk.Label(root, text="Select Model:").pack(pady=(10, 2))
model_var = tk.StringVar(value="large-v3-turbo") # DEFAULT MODEL
tk.OptionMenu(root, model_var, *available_models).pack()

# File selection
tk.Label(root, text="Select File:").pack(pady=(10, 2))
file_frame = tk.Frame(root)
file_frame.pack()
file_var = tk.StringVar()
tk.Entry(file_frame, textvariable=file_var, width=40).pack(side=tk.LEFT, padx=(0, 5))
tk.Button(file_frame, text="Browse", command=browse_file).pack(side=tk.LEFT)

# Output folder selection
tk.Label(root, text="Output Folder:").pack(pady=(10, 2))
output_frame = tk.Frame(root)
output_frame.pack()
output_var = tk.StringVar(value=default_output_folder)
tk.Entry(output_frame, textvariable=output_var, width=40).pack(side=tk.LEFT, padx=(0, 5))
tk.Button(output_frame, text="Change", command=browse_output_folder).pack(side=tk.LEFT)

# Output format selection
tk.Label(root, text="Output Format:").pack(pady=(10, 2))
format_var = tk.StringVar(value="txt")
tk.OptionMenu(root, format_var, *output_formats).pack()

# Language selection
tk.Label(root, text="Language:").pack(pady=(10, 2))
language_var = tk.StringVar(value="automatic")
tk.OptionMenu(root, language_var, *language_options.keys()).pack()

# Transcribe button
tk.Button(root, text="Transcribe", command=start_transcription, padx=10, pady=5).pack(pady=10)

# Time label
time_label = tk.Label(root, text="", font=("Courier", 11))
time_label.pack(pady=(0, 10))

root.mainloop()
