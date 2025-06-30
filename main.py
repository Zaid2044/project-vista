from core.vision import verify_user
from core.speech import listen, speak

if __name__ == "__main__":
    if verify_user():
        speak("Welcome Zaid, how can I help you today?")
        user_input = listen()
        if user_input:
            speak(f"You said: {user_input}")
        else:
            speak("Sorry, I didn't catch that.")
    else:
        print("❌ Access Denied.")
