# Project: Ash - An assistance tool
# File: main.py

import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import pyjokes
import datetime
import os
import requests
from dotenv import load_dotenv

# load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

load_dotenv()

YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

def play_song_on_youtube(song_name: str):
    if not YOUTUBE_API_KEY:
        speak("YouTube API key is not set.")
        return

    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": song_name + " song",
        "type": "video",
        "maxResults": 1,
        "key": YOUTUBE_API_KEY,
    }

    response = requests.get(search_url, params=params)
    data = response.json()

    try:
        video_id = data["items"][0]["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        speak(f"Playing {song_name} on YouTube.")
        webbrowser.open(video_url)
    except (KeyError, IndexError):
        speak("Sorry, I could not find that song on YouTube.")

def processQuery(command: str):
    print(f"[COMMAND]: {command}")
    # Here you will add: open youtube, google, jokes, etc.
    # For now we just speak it back:
    speak(f"You said: {command}")

    if "open youtube" in command.lower():
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open wikipedia" in command.lower():
        speak("Opening Wikipedia.")
        webbrowser.open("https://www.wikipedia.org")
    elif "open facebook" in command.lower():
        speak("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command.lower():
        speak("Opening Twitter.")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in command.lower():
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")    
    elif "open google" in command.lower():
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "play" in command.lower():
        song_name = command.lower().replace("play", "").strip()
        if song_name:
            play_song_on_youtube(song_name)
        else:
            speak("Please specify a song name to play.")
    elif "tell me a joke" in command.lower():
        joke = pyjokes.get_joke()
        speak(joke)
    elif "what time is it" in command.lower():
        current_time = time.strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "open github" in command.lower():
        speak("Opening GitHub.")
        webbrowser.open("https://www.github.com")
    elif "open stack overflow" in command.lower():
        speak("Opening Stack Overflow.")
        webbrowser.open("https://stackoverflow.com")
    elif "open gmail" in command.lower():
        speak("Opening Gmail.")
        webbrowser.open("https://mail.google.com")
    elif "what is your name" in command.lower():
        speak("I am Ayush, your personal assistant.")
    elif "exit" in command.lower() or "quit" in command.lower():
        speak("Goodbye!")
        exit()
    elif "what day is it" in command.lower():
        day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {day}.")

def speak(text: str):
    print(f"[AYUSH]: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello, I am Ayush. Say Ayush to wake me up.")

    while True:
        # 1️⃣ Listen for wake word
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("\nListening for wake word 'Ayush'...")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                print("Recognizing wake word...")
                wake_text = recognizer.recognize_google(audio, language="en-IN")
                print(f"[USER]: {wake_text}")

                if wake_text.lower().strip() in ("aayush", "aayushh"):
                    speak("Yes, Mr. Tyagi. How can I help you?")

                    # 2️⃣ Now listen for actual command
                    with sr.Microphone() as source2:
                        recognizer.adjust_for_ambient_noise(source2, duration=1)
                        print("Listening for your command...")
                        cmd_audio = recognizer.listen(source2, timeout=8, phrase_time_limit=5)
                        print("Recognizing command...")
                        command = recognizer.recognize_google(cmd_audio, language="en-IN")
                        print(f"[USER COMMAND]: {command}")
                        processQuery(command)

                else:
                    speak("Please say aayush to get my attention.")

            except sr.WaitTimeoutError:
                print("[ERROR]: Timeout – no speech detected.")
            except sr.UnknownValueError:
                print("[ERROR]: Could not understand audio.")
                # speak("Sorry, I did not catch that. Could you please repeat?")
            except sr.RequestError as e:
                print(f"[ERROR]: Could not request results; {e}")
                # speak("There is a problem reaching the speech service.")
