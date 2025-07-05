import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, ClientSettings
import av
import whisper
import openai
import tempfile
import os
import numpy as np

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Whisper model
@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

st.title("🎙️ Meeting Transcriber with Whisper + GPT")

st.markdown("Record your voice, transcribe using Whisper, and summarize with OpenAI GPT.")

# Audio processor
class AudioProcessor:
    def __init__(self):
        self.audio = b""

    def recv(self, frame: av.AudioFrame):
        pcm = frame.to_ndarray().tobytes()
        self.audio += pcm
        return frame

ctx = webrtc_streamer(
    key="mic",
    mode=WebRtcMode.SENDONLY,
    in_audio=True,
    client_settings=ClientSettings(
        media_stream_constraints={"audio": True, "video": False},
        rtc_configuration={}
    ),
    audio_receiver_size=1024,
)

if ctx and ctx.state.playing:
    st.warning("🔴 Recording... Speak now.")
    ctx.audio_receiver = AudioProcessor()

elif ctx and not ctx.state.playing and hasattr(ctx, "audio_receiver") and ctx.audio_receiver.audio:
    st.success("✅ Recording stopped. Processing...")

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(ctx.audio_receiver.audio)
        temp_audio_path = f.name

    # Transcribe with Whisper
    with st.spinner("Transcribing..."):
        result = model.transcribe(temp_audio_path)
        transcription = result["text"]
    st.subheader("📝 Transcription")
    st.write(transcription)

    # Summarize with GPT
    with st.spinner("Summarizing..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a meeting assistant."},
                {"role": "user", "content": f"Summarize this meeting: {transcription}"}
            ],
            temperature=0.7,
            max_tokens=300
        )
        summary = response.choices[0].message["content"]

    st.subheader("📋 Summary")
    st.write(summary)
