import streamlit as st
from st_audiorec import st_audiorec
import openai
import tempfile
import whisper
import os

# Set your OpenAI API key securely from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load Whisper model
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")  # you can use 'tiny', 'base', 'small', etc.

model = load_whisper_model()

# UI title
st.title("📝 Otter-like Meeting Transcriber")
st.markdown("Record audio, transcribe it using Whisper, and summarize using GPT.")

# Record audio from mic
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format="audio/wav")
    st.info("✅ Audio recorded. Transcribing...")

    # Save audio to a temp file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        f.write(wav_audio_data)
        audio_path = f.name

    # Transcribe audio using Whisper
    with st.spinner("Transcribing..."):
        result = model.transcribe(audio_path)
        transcription = result["text"]

    st.subheader("🗒️ Transcription")
    st.write(transcription)

    # Summarize using OpenAI
    with st.spinner("Summarizing with GPT..."):
        summary_prompt = f"Summarize the following meeting transcript:\n\n{transcription}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful meeting assistant."},
                {"role": "user", "content": summary_prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        summary = response.choices[0].message["content"]

    st.subheader("📋 Summary")
    st.write(summary)
