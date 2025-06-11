import streamlit as st
import pandas as pd
import speech_recognition as sr
import difflib
import pyttsx3
import threading
from streamlit_chat import message

# Load mood-song data
df = pd.read_csv("mood_songs_with_youtube_links.csv")

# TTS setup (non-blocking)
tts_engine = pyttsx3.init()
def speak_async(text):
    threading.Thread(target=lambda: (tts_engine.say(text), tts_engine.runAndWait())).start()

# Page setup
st.set_page_config(page_title="VoiceMood DJ", layout="centered")
st.title("🎧 VoiceMood DJ - AI Mood-Based Playlist Generator")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "mood_songs" not in st.session_state:
    st.session_state.mood_songs = []
if "last_mood" not in st.session_state:
    st.session_state.last_mood = ""

# First message
if not any(msg["role"] == "assistant" for msg in st.session_state.messages):
    intro = "👋 Hi! I'm your Mood DJ. Tell me your mood — type it or speak it!"
    st.session_state.messages.append({"role": "assistant", "content": intro})
    speak_async("Hi! I'm your Mood DJ. Tell me your mood.")

# Display chat messages
for i, msg in enumerate(st.session_state.messages):
    message(msg["content"], is_user=(msg["role"] == "user"), key=f"msg_{i}")

# Input columns
col1, col2 = st.columns([1, 1])
with col1:
    typed_input = st.text_input("Type your mood:", key="typed_mood")
    typed_submit = st.button("📩 Submit Mood", key="typed_submit")

with col2:
    voice_submit = st.button("🎙️ Speak Your Mood", key="voice_submit")

# Handle voice input
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("🎤 Listening... Speak your mood now.")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            st.session_state.voice_mood = text
            st.toast(f"🗣️ You said: {text}")
        except sr.UnknownValueError:
            st.toast("😕 Couldn't understand your speech.")
        except sr.RequestError:
            st.toast("⚠️ Speech service unavailable.")
        except sr.WaitTimeoutError:
            st.toast("⌛ Timeout: No speech detected.")

# Start voice input thread
if voice_submit:
    st.session_state.voice_mood = ""
    threading.Thread(target=get_voice_input).start()

# Get final mood input
final_mood = ""
if typed_submit and typed_input.strip():
    final_mood = typed_input.strip().lower()
    st.session_state.messages.append({"role": "user", "content": typed_input.strip()})
elif "voice_mood" in st.session_state and st.session_state.voice_mood:
    final_mood = st.session_state.voice_mood.strip().lower()
    st.session_state.messages.append({"role": "user", "content": final_mood})
    st.session_state.voice_mood = ""  # Reset for next input

# If new mood provided, process and update
if final_mood and final_mood != st.session_state.last_mood:
    valid_moods = df["Mood"].dropna().str.lower().unique()
    closest = difflib.get_close_matches(final_mood, valid_moods, n=1, cutoff=0.3)

    if closest:
        mood = closest[0]
        st.session_state.last_mood = mood
        songs = df[df["Mood"].str.lower() == mood]
        st.session_state.mood_songs = songs.to_dict(orient="records")

        reply = f"🎵 Found {len(songs)} songs for mood: **{mood.capitalize()}**"
        st.session_state.messages.append({"role": "assistant", "content": reply})
        speak_async(reply)

        for song in st.session_state.mood_songs:
            content = f"🎶 {song['Song']}  \n*Artist:* {song['Artist']}  \n*Language:* {song['Language']}  \n[▶️ Play on YouTube]({song['YouTubeLink']})"
            st.session_state.messages.append({"role": "assistant", "content": content})

    else:
        reply = "😢 I couldn't understand your mood. Try typing or saying: happy, sad, romantic, energetic, etc."
        st.session_state.messages.append({"role": "assistant", "content": reply})
        speak_async("Sorry, I couldn't understand your mood.")

