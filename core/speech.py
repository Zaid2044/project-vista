import speech_recognition as sr
import whisper
import pyttsx3
from pydub import AudioSegment

model = whisper.load_model("base")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)

    try:
        raw_data = audio.get_wav_data()
        with open("temp_raw.wav", "wb") as f:
            f.write(raw_data)

        sound = AudioSegment.from_file("temp_raw.wav", format="wav")
        sound.export("temp.wav", format="wav")

        result = model.transcribe("temp.wav")
        text = result["text"].strip()
        print(f"🗣️ You said: {text}")
        return text

    except Exception as e:
        print("⚠️ Error:", e)
        return None


engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print(f"🧠 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
