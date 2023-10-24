from langdetect import detect
from googletrans import Translator

# Function to detect the language of the input text
def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "unknown"

# Function to translate text to a target language
def translate_to_target_language(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

# Multilingual chatbot
def chatbot(input_text):
    detected_language = detect_language(input_text)
    
    # If the detected language is unknown, respond in English by default
    target_language = detected_language if detected_language != "unknown" else "en"
    
    # Translate the input text to the detected language
    response = translate_to_target_language(input_text, target_language)
    
    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot(user_input)
        print("Bot: " + response)
