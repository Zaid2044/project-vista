import speech_recognition as sr
import whisper
import pyttsx3

model = whisper.load_model("base")
engine = pyttsx3.init()
engine.setProperty("rate", 180)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)

    try:
        with open("temp.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe("temp.wav")
        text = result["text"].strip()
        print(f"🗣️ You said: {text}")
        return text

    except Exception as e:
        print("⚠️ Error:", e)
        return None

def speak(text):
    print(f"🧠 Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
