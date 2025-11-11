import streamlit as st
from utils import listen_and_transcribe, generate_answer, speak

st.title("🎙️ Talk to Manu Singh – Your Personal Voice Q&A")

if st.button("Ask Question"):
    st.text("🎧 Listening...")
    transcript = listen_and_transcribe()
    if transcript:
        st.text(f"📝 You said: {transcript}")
        answer = generate_answer(transcript)
        st.text(f"💬 Answer: {answer}")
        speak(answer)
    else:
        st.text("❌ Could not understand. Try again.")
