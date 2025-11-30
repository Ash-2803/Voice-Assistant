# 🗣️ Ayush Voice Assistant (Python)

A personal voice-controlled assistant built using Python.  
It listens for the wake word **“Ayush”** or **“Ayushh”**, responds intelligently, and performs actions based on your voice commands.

---

## 🚀 Features

Your assistant currently supports:

---

### 🔊 Voice Recognition
- Wake word detection (“Ayush” / “Ayushh”)
- Converts speech → text using Google Speech Recognition
- Speaks responses aloud with `pyttsx3`

---

### 🌐 Web Automation  
Supported commands:
- **Open Google**
- **Open YouTube**
- **Open GitHub**
- **Open Instagram**
- **Open Facebook**
- **Open Twitter**
- **Open Gmail**
- **Open Stack Overflow**

---

### 🎵 Music Search (YouTube API)
- Say **“Play <song name>”**
- Uses **YouTube Data API v3** to fetch the best match
- Opens the song directly in your browser  
- *(API key is stored securely in `.env` and not uploaded)*

---

### 😂 Jokes
- Say **“Tell me a joke”**
- Replies with a random joke using `pyjokes`

---

### 🕒 Time & Date
- “What time is it?”
- “What day is it?”

---

### 👤 Personal Info
- “What is your name?”
- “Who are you?”

---

### 👋 Exit
- “Exit”
- “Quit”

---

## 🛠️ Tech Stack

- **Python 3**
- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `requests`
- `python-dotenv`
- `pyjokes`
- **YouTube Data API v3**

---

## 📂 Project Structure



---

## 🔐 Environment Variables

Your `.env` file should contain:


⚠️ **Never commit your `.env` file to GitHub.**  
This project already ignores it using `.gitignore`.

---

## ▶️ How to Run the Assistant

Clone the repository:

```bash
git clone https://github.com/Ayush-2803/Voice-Assistant.git

cd Voice-Assistant
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```
Create a `.env` file in the root directory with your YouTube API key:

```env
YOUTUBE_API_KEY=your_youtube_api_key_here
```

Run the assistant:

```bAyush
python main.py
``` 
---## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```env
YOUTUBE_API_KEY=your_youtube_api_key_here
```
