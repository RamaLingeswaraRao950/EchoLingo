# 🌐 EchoLingo 💬  

🎙️ **EchoLingo** is a **speech translation and synthesis app**. It allows you to **speak in one language**, automatically **detects it**, **translates it** into another language of your choice, and even **speaks it aloud** using **text-to-speech**. Perfect for multilingual communication and learning! 🌎✨  

---

## 🚀 Features :-- 

- 🎧 **Real-time Speech Recognition** – Speak naturally, and EchoLingo captures your voice instantly.  
- 🌍 **Auto Language Detection** – Detects the language you’re speaking in automatically.  
- 🔄 **Instant Translation** – Translates your spoken text into the target language in seconds.  
- 🔊 **Text-to-Speech (TTS)** – Hear your translated output with realistic speech playback.  
- 🗂️ **Translation History** – Stores all your translations with timestamps for later reference.  
- 🧹 **Clear Log Functionality** – Quickly clear the on-screen logs for a clean workspace.  
- 🌈 **Animated UI** – Enjoy a modern and dynamic interface with smooth background transitions.  
- 🪶 **Lightweight & Fast** – Simple, efficient, and fully offline-capable (except translation & speech services).  

---

## 🧠 How It Works :-- 

1. 🎙️ Click **“Start Listening”**.  
2. 🗣️ Speak in any language (EchoLingo will detect it automatically).  
3. 🌍 The app will translate it into your selected target language.  
4. 🔊 The translated text is spoken aloud instantly.  
5. 📜 Your translation is saved to the `history/speech_translations.txt` file for future use.  

---

## 🧩 Tech Stack :-- 

| Component | Technology |
|------------|-------------|
| 🎨 UI Framework | Tkinter |
| 🗣️ Speech Recognition | `speech_recognition` |
| 🧏 Translation | `mtranslate` |
| 🔊 Text-to-Speech | `gTTS` (Google Text-to-Speech) |
| 🌐 Language Detection | `langdetect` |
| 🧵 Multithreading | `threading` |
| 🕒 Data Storage | Local `.txt` file with timestamps |

---

## ⚙️ Installation :-- 

### 🪄 Prerequisites : 
Make sure you have **Python 3.8+** installed on your system.

### 🧰 Setup Steps : 
```bash
1️⃣ Clone the repository :--  git clone

2️⃣ Navigate to the project folder :--  cd EchoLingo

3️⃣ Install dependencies :--  pip install speechrecognition gtts mtranslate langdetect tkinter
```

---

## ▶️ Usage :-- 

Run the app with :
```bash
python echolingo.py
```

Once launched :
- 🎙️ Click **Start Listening** to begin recording.  
- 🗣️ Speak into your microphone.  
- 🌍 View translated text in the console area.  
- 🔊 Listen to the translated speech.  
- 📜 View or clear your translation history.  

---

## 🖼️ UI Preview :-- 

🪄 A sleek, animated interface with:  
- Dynamic background transitions 🌈  
- Vibrant buttons with hover effects ✨  
- A glowing console log for real-time updates ⚡  

---

🌟 “EchoLingo helps you break language barriers — one word at a time.” 🌟  
