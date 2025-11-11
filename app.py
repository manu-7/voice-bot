import streamlit as st
from audio_recorder_streamlit import audio_recorder
from utils import transcribe_wav_bytes, generate_answer, tts_bytes

st.set_page_config(page_title="Talk to Manu Singh", page_icon="🎙️")
st.title("🎙️ Talk to Manu Singh – Your Personal Voice Q&A")

audio_bytes = audio_recorder(
    text="Click to record",
    recording_color="#cc3333",
    neutral_color="#6aa36f",
)

if audio_bytes:
    with st.spinner("🌀 Transcribing..."):
        transcript = transcribe_wav_bytes(audio_bytes)

    if transcript and not transcript.lower().startswith("error"):
        st.success(f"📝 You said: {transcript}")
        answer = generate_answer(transcript)
        st.info(f"💬 Answer: {answer}")

        st.text("🔊 Speaking...")
        st.audio(tts_bytes(answer), format="audio/mp3")
    else:
        st.error("❌ Could not understand. Try again.")
