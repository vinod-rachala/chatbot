from langdetect import detect
from googletrans import Translator

# Function to detect the language of the input text
def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "unknown"

# Function to translate text to a target language (e.g., English)
def translate_to_target_language(text, target_language="en"):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

# Multilingual chatbot
def chatbot(input_text, target_language="en"):
    detected_language = detect_language(input_text)
    
    if detected_language == target_language:
        # If the detected language is the same as the target language, no translation is needed.
        response = "You are speaking in " + target_language + ": " + input_text
    else:
        # Translate the input text to the target language
        translated_text = translate_to_target_language(input_text, target_language)
        response = "Detected language: " + detected_language + "\nTranslation: " + translated_text

    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot(user_input)
        print("Bot: " + response)
