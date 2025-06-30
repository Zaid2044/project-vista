from core.speech import listen, speak
from core.nlp import get_intent, fallback_response
import datetime
import webbrowser
from dotenv import load_dotenv
load_dotenv()

while True:
    user_input = listen()
    if not user_input:
        speak("Sorry, I didn't catch that.")
        continue

    intent = get_intent(user_input)

    if intent == "get_time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    elif intent == "get_date":
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {today}.")

    elif intent == "get_name":
        speak("I'm Project Vista, your AI assistant.")

    elif intent == "open_browser":
        speak("Opening your browser.")
        webbrowser.open("https://www.google.com")

    else:
        response = fallback_response(user_input)
        speak(response)
