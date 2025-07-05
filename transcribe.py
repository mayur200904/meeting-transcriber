# -*- coding: utf-8 -*-
#pip install streamlit openai torch torchvision torchaudio git+https://github.com/openai/whisper.git

import whisper
import os

model = whisper.load_model("base")  # or "small", "medium", "large" for higher accuracy

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
