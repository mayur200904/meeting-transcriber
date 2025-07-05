# -*- coding: utf-8 -*-
#pip install streamlit-audiorec

import streamlit as st
from transcribe import transcribe_audio
from summarize import summarize_text
import tempfile
from streamlit-audiorec import st_audiorec

st.title("🎙️ Live Meeting Recorder & Summarizer")

st.markdown("### 🎤 Record your voice")
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        tmpfile.write(wav_audio_data)
        audio_path = tmpfile.name

    st.success("✅ Audio recorded!")
    st.info("Transcribing...")

    transcript = transcribe_audio(audio_path)
    st.text_area("📝 Transcript", transcript, height=300)

    if st.button("🔍 Summarize"):
        summary = summarize_text(transcript)
        st.markdown("### 📌 Summary")
        st.markdown(summary)
from database import save_to_db

title = st.text_input("Give a title for this meeting:", value="Untitled Meeting")

if st.button("💾 Save to Database"):
    save_to_db(title, transcript, summary)
    st.success("Saved to database!")
