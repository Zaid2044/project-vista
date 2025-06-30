import spacy
import google.generativeai as genai
import os

nlp = spacy.load("en_core_web_sm")

def get_intent(text):
    doc = nlp(text.lower())

    if "time" in text:
        return "get_time"
    elif "date" in text:
        return "get_date"
    elif any(token.lemma_ in ["your", "name"] for token in doc):
        return "get_name"
    elif "open" in text and "browser" in text:
        return "open_browser"
    else:
        return "fallback"

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def fallback_response(text):
    try:
        response = model.generate_content(text)
        return response.text.strip()
    except Exception as e:
        return "I had trouble generating a response."
