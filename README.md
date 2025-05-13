# MurmurOpenUI
A lightweight, open-source macOS Python script app to run OpenAI’s Whisper models with a simple graphical interface.

## Features
- Transcribe audio files using OpenAI Whisper (locally)
- Simple & easy to use graphical interface (built with tkinter)
- Supports multiple languages (auto-detect, English, French, Spanish, Korean)
- Outputs in txt, srt, vtt, and json formats
- Selectable models: from tiny to large-v3-turbo
- Default output folder is ~/Downloads
- macOS-optimised with automatic ffmpeg path support
- Customise the Python script to your liking

---

## 🔧 REQUIREMENTS BEFORE RUNNING THIS PROGRAM (on macOS)

1. **Install Homebrew** (if not already):  
   https://brew.sh

2. **Install ffmpeg** (required for audio/video processing):
   ```bash
   brew install ffmpeg
   ```

3. Install Python 3 (if not installed):
   ```bash
   brew install python
   ```

4.	Install required Python packages
  Try this first:
    ```bash
    pip install openai-whisper torch
    ```
    
    If that fails, use:
  	```bash
     pip3 install openai-whisper torch
     ```

---

## 🚀 How to Run
In your terminal, navigate to the folder containing the script.
Then run:
```bash
python3 WhisperApp_beta2.py
```
Alternatively, run it with F5 if you’re using Python’s built-in IDLE, or launch it however your Python interface allows.

---
## 📦 Installation (Dev Setup)

If you’re cloning the repo to develop or modify:
```bash
git clone https://github.com/thegitmate/MurmurOpenUI.git
cd MurmurOpenUI
```

Install dependencies (if not yet installed):
```bash
pip install openai-whisper torch
```

Make sure ffmpeg is working:
```bash
ffmpeg -version
```

---

## 📝 License

This project is licensed under the MIT License — see the LICENSE file for full details.

---

## 🙏 Credits & Acknowledgements
- Built on top of OpenAI Whisper
- Created because I didn't want to pay 3rd-party apps to run the best Whisper models
- Sharing to make local transcription easier for everyone

🎓 Made for the AI in Society class.

May 2025
