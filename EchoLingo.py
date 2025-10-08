import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import speech_recognition as sr
from gtts import gTTS
from mtranslate import translate
import datetime
import os
import langdetect
import itertools

recognizer = sr.Recognizer()
recognizer.energy_threshold = 35000
recognizer.dynamic_energy_threshold = True


def translate_text(text, target_lang="en"):
    try:
        translated = translate(text, target_lang)
        return translated
    except Exception as e:
        log_message(f"⚠️ Translation error: {e}")
        return text


def save_to_file(original, translated, input_lang, output_lang):
    os.makedirs("history", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history/speech_translations.txt", "a", encoding="utf-8") as f:
        f.write(
            f"[{timestamp}]\nInput ({input_lang}): {original}\nOutput ({output_lang}): {translated}\n\n"
        )


def speak_text(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save("output.mp3")
        os.system("start output.mp3" if os.name ==
                  "nt" else "mpg321 output.mp3")
    except Exception as e:
        log_message(f"🔇 Speech synthesis failed: {e}")


def detect_language(text):
    try:
        return langdetect.detect(text)
    except:
        return "unknown"


def log_message(msg):
    text_box.config(state=tk.NORMAL)
    text_box.insert(tk.END, msg + "\n")
    text_box.see(tk.END)
    text_box.config(state=tk.DISABLED)


def listen_and_translate():
    output_lang = lang_output.get().strip() or "en"
    mic = sr.Microphone()

    log_message("🎧 Adjusting for ambient noise...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        log_message("✅ Ready to record. Speak now...")

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            input_lang = detect_language(text)

            log_message(f"🗣️ You said ({input_lang}): {text}")
            translated = translate_text(text, output_lang)
            log_message(f"💬 Translated ({output_lang}): {translated}")

            speak_text(translated, output_lang)
            save_to_file(text, translated, input_lang, output_lang)

        except sr.UnknownValueError:
            log_message("⚠️ Could not understand the speech.")
        except sr.RequestError:
            log_message("❌ Internet issue — please check your connection.")
        except Exception as e:
            log_message(f"🚫 Unexpected error: {e}")


def start_listening():
    threading.Thread(target=listen_and_translate, daemon=True).start()


def show_history():
    try:
        with open("history/speech_translations.txt", "r", encoding="utf-8") as f:
            history_window = tk.Toplevel(root)
            history_window.title("📜 Translation History")
            history_window.geometry("600x400")
            history_text = scrolledtext.ScrolledText(
                history_window, wrap=tk.WORD)
            history_text.insert(tk.END, f.read())
            history_text.config(state=tk.DISABLED)
            history_text.pack(fill=tk.BOTH, expand=True)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No history found yet!")


def clear_log():
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.config(state=tk.DISABLED)


colors = ["#121212", "#1E1E1E", "#2B2B2B", "#00FFB3", "#0078FF", "#FF0078"]
color_cycle = itertools.cycle(colors)


def animate_background():
    next_color = next(color_cycle)
    root.config(bg=next_color)
    lang_frame.config(bg=next_color)
    btn_frame.config(bg=next_color)
    footer_label.config(bg=next_color)
    tagline_label.config(bg=next_color)
    root.after(1500, animate_background)


title_colors = itertools.cycle(
    ["#00FFB3", "#00E0FF", "#FF00C8", "#FFFFFF", "#0078FF"])


def animate_title_and_tagline():
    new_color = next(title_colors)
    title_label.config(fg=new_color)
    tagline_label.config(fg=new_color)
    root.after(500, animate_title_and_tagline)


def on_enter(e):
    e.widget.config(bg="#00FFD1", fg="black")


def on_leave(e):
    if e.widget["text"] == "🎙️ Start Listening":
        e.widget.config(bg="#00FFB3", fg="black")
    elif e.widget["text"] == "📜 Show History":
        e.widget.config(bg="#0078FF", fg="white")
    elif e.widget["text"] == "🧹 Clear Log":
        e.widget.config(bg="#FF0078", fg="white")


root = tk.Tk()
root.title("🌐 EchoLingo ––– Speak Freely.. Understand Instantly.. 🌐")
root.geometry("650x650")
root.config(bg="#121212")

title_label = tk.Label(
    root,
    text="🌐 EchoLingo",
    fg="#00FFB3",
    bg="#121212",
    font=("Poppins", 28, "bold"),
)
title_label.pack(pady=(25, 5))

tagline_label = tk.Label(
    root,
    text="💬 Speak Freely.. Understand Instantly..",
    fg="#CCCCCC",
    bg="#121212",
    font=("Poppins", 14, "italic"),
)
tagline_label.pack(pady=(0, 20))

lang_frame = tk.Frame(root, bg="#121212")
lang_frame.pack(pady=10)
tk.Label(
    lang_frame,
    text="Output Language ( ex : en, hi, fr, es ) : ",
    fg="white",
    bg="#121212",
    font=("Segoe UI", 12),
).pack(side=tk.LEFT)
lang_output = tk.Entry(lang_frame, width=10, font=("Segoe UI", 12))
lang_output.insert(0, "en")
lang_output.pack(side=tk.LEFT, padx=10)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=10)
buttons = [
    ("🎙️ Start Listening", start_listening, "#00FFB3", "black"),
    ("📜 Show History", show_history, "#0078FF", "white"),
    ("🧹 Clear Log", clear_log, "#FF0078", "white"),
]
for text, cmd, bg_color, fg_color in buttons:
    btn = tk.Button(
        btn_frame,
        text=text,
        command=cmd,
        bg=bg_color,
        fg=fg_color,
        font=("Segoe UI", 12, "bold"),
        padx=10,
        pady=5,
    )
    btn.pack(side=tk.LEFT, padx=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

text_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    height=18,
    width=95,
    bg="#1E1E1E",
    fg="#00FFB3",
    font=("Consolas", 12),
)
text_box.pack(padx=15, pady=15)
text_box.config(state=tk.DISABLED)

footer_label = tk.Label(
    root,
    text="👨‍💻 Author : Rama Lingeswara Rao Sivakavi | 🔊 Powered by Python",
    fg="#888888",
    bg="#121212",
    font=("Segoe UI", 10),
)
footer_label.pack(side=tk.BOTTOM, pady=5)

animate_background()
animate_title_and_tagline()

root.mainloop()
