import speech_recognition as sr
import streamlit as st

# Capture speech from microphone and convert to text
def recognize():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙 Speak now...")           # Prompt user
        recog.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recog.listen(source)            # Listen to speech
        return recog.recognize_google(audio)    # Convert speech to text
