# MurmurOpenUI
A lightweight, open-source macOS python script to run OpenAI’s Whisper models with a simple graphical interface.

## Features
- Speech-to-Text: Transcribe audio files using OpenAI Whisper (locally)
- Select any Whisper models: from tiny to large-v3-turbo
- Supports multiple languages (auto-detect, English, French, Spanish, Korean, and more)
- Simple & easy to use graphical interface (built with tkinter)
- Outputs in txt, srt, vtt, and json formats
- Default output folder is ~/Downloads
- macOS-optimised with automatic ffmpeg path support
- Easily customise the Python script to your preferences

---

## 🔧 REQUIREMENTS BEFORE RUNNING THIS PROGRAM (on macOS)

1. **Install Homebrew** (if not already):  
[brew.sh](https://brew.sh) (Right-click and "Open link in new tab")


3. **Install ffmpeg** (required for audio/video processing):
   ```bash
   brew install ffmpeg
   ```

4. Install Python 3 (if not installed):
   ```bash
   brew install python
   ```

5.	Install required Python packages
  Try this first:
    ```bash
    pip install openai-whisper torch
    ```
    
    If that fails, you might need to use pip3.

6. Pre-download the Whisper model you want to use:
   ```bash
   python3 -c "import whisper; whisper.load_model('large-v3-turbo')"
   ```
   Replace 'large-v3-turbo' with 'base', 'tiny', 'small', 'medium', 'large', or else as needed.

---

## 🚀 How to Run
In your terminal, navigate to the folder containing the script.
Then run:
```bash
python3 MurmurOpenUI_public.py
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

Look at the 'Requirements' section for more details.

---

## 📝 License

This project is licensed under the MIT License — see the LICENSE file for full details.

---

## 🙏 Credits & Acknowledgements
- Built on top of OpenAI Whisper
- Created because I didn't want to pay 3rd-party apps to run the best Whisper models
- Sharing to make local transcription easier for everyone

🎓 Made for the AI in Society class.

Built by N. in May 2025

---

## 🔎 SEO Keywords
macOS Whisper GUI, Python Whisper transcription, OpenAI Whisper macOS, Whisper speech-to-text app, Whisper Python GUI, macOS audio transcription tool, run Whisper locally macOS, open-source Whisper GUI, transcribe audio macOS, Whisper model selector, multilingual Whisper transcription, tkinter Whisper interface, ffmpeg Whisper setup, Whisper transcription script, local speech recognition macOS, Whisper v3 turbo macOS, Python speech-to-text app, convert audio to text macOS, subtitle generator macOS, SRT VTT transcription tool.
