# **🎧 VoiceMood DJ – AI Mood-Based Playlist Generator**

## **🧠 Problem Statement**
- We all listen to music based on how we feel — when we’re happy, we want energetic beats; when we’re sad, we crave soulful melodies. But finding music that matches your current mood isn’t always straightforward. Most music apps rely on predefined playlists or require you to search manually using exact keywords.

- That’s a problem when your mood doesn’t match typical categories, or you don’t know what exactly you want to hear. Moreover, many people just want a more human-like experience — like talking to a DJ and saying, “I feel nostalgic”, and instantly getting a list of songs to match that mood.

- But existing apps don’t let users simply talk to the system and receive intelligent, mood-based song suggestions in return. There’s a gap in intuitive, voice-friendly music discovery — and that’s what this project aims to solve.

## **💡 Proposed System / Solution**

To address the problem of finding music that aligns with a person’s mood quickly and intuitively, we propose VoiceMood DJ — an intelligent, voice-enabled, mood-based music recommendation system.

The core idea is to create a chatbot-style interface where users can simply speak or type their current mood, and the system responds with a personalized playlist curated from a dataset of songs labeled by mood. This eliminates the need to manually search through apps or playlists, offering a hands-free, conversational, and emotionally aware experience.

*How it works:*
* Accepts both typed or spoken mood input using text fields or microphone.
* SpeechRecognition transcribes voice to text.
* Uses fuzzy matching (via `difflib`) to recognize moods even with typos or unclear pronunciation.
* Filters songs from a curated dataset (`mood_songs_with_youtube_links.csv`) based on the interpreted mood.
* Displays song details: 🎵 Title, 🎤 Artist, 🌐 Language, and 🔗 clickable YouTube link.
* Responds using text-to-speech via `pyttsx3` to create a friendly voice assistant experience.
* Designed to be lightweight, intuitive, and accessible for all — especially helpful for visually impaired or older users.

*Not:* Runs fully offline (except for YouTube playback) with instant feedback.

## **🛠️ System Development Approach (Technologies Used)**

Component	Tool / Library: 
| Component               | Tool / Library                    |
| ----------------------- | --------------------------------- |
| 💻 Programming Language | Python                            |
| 🌐 Interface            | [Streamlit](https://streamlit.io) |
| 🗣️ Voice Recognition   | `speech_recognition`              |
| 🧠 Text-to-Speech       | `pyttsx3`                         |
| 📊 Data Handling        | `pandas`                          |
| 💬 Chat UI              | `streamlit-chat`                  |
| 🎵 Music Data           | CSV file of songs tagged by mood  |
| 🔗 Music Playback       | YouTube links                     |

*Note:* All tools used are free, open-source, and pip-installable — making the project easy to replicate and run.

## **🧩 Algorithm & Deployment**

🔁 Step-by-step Flow:

1. Input Collection
* User types a mood or speaks it using the mic.
* Voice input is transcribed via Google Speech Recognition.

2. Mood Matching
* List of valid moods stored (e.g., happy, sad, romantic, energetic, nostalgic).
* Fuzzy matching (difflib.get_close_matches) ensures input doesn't need to be perfect.

3. Playlist Generation
* Mood is matched with a filtered subset of the CSV.
* Songs are sorted and displayed.

4. Chatbot Feedback
* System speaks a response and shows the playlist using message cards. 

5. Deployment
* Run locally using streamlit run app.py.
* No internet required for voice input, response, or matching (except for YouTube playback).

## **📸 Result**

When you run the app, here’s what happens:
* You see a welcome message from your mood-based DJ 🎧
* Two input options:
   - 📩 Type your mood
   - 🎙️ Speak your mood
* When you provide a mood like "happy":
  - You hear a voice say: “Found 5 songs for mood: Happy”
  - You get a list of tracks like:

    🎵 Song: Happy  
    🎤 Artist: Pharrell Williams  
    🌐 Language: English  
    🔗 [▶️ Play on YouTube](https://youtube.com/link)

*Note:* 
  * Typed and voice inputs work separately
  * Works repeatedly without errors or thread issues

## **🧾 Conclusion**
VoiceMood DJ proves that even with simple tools, you can build intelligent and delightful experiences. With basic speech/text processing, fuzzy logic, and curated data, it becomes a human-like DJ assistant that listens, understands, and responds with meaningful music.

It’s engaging, practical, and adds a personal touch to music discovery — perfect for students, music lovers, or those exploring conversational UIs.

## **🚀 Future Scope**
Here’s what’s next for VoiceMood DJ:

* 😃 Emotion detection via webcam (facial recognition).
* 🎧 Spotify or YouTube API integration for live trending songs.
* 🌍 Support for regional languages like Hindi, Tamil, Bengali.
* ⭐ Add memory/favorites for personal recommendations.
*📱 Build a mobile app or voice assistant skill (Alexa, Google).
* 🕓 Smart filters like “Morning Chill” or “Night Drive”.

## **📚 References**

* Streamlit Documentation
* SpeechRecognition Package
* pyttsx3 Text-to-Speech
* Difflib – Fuzzy Matching
* CSV Dataset (Handcrafted)
* YouTube (for music demo)
