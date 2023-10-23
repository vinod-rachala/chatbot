# Import necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from googletrans import Translator, LANGUAGES

# Initialize the chatbot
chatbot = ChatBot('MultilingualBot')

# Create a trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English conversations
trainer.train('chatterbot.corpus.english')

# Create a translator object
translator = Translator()

# Function to translate text
def translate(text, target_lang):
    translated = translator.translate(text, src='auto', dest=target_lang)
    return translated.text

# Function to list supported languages
def list_supported_languages():
    return LANGUAGES

# Function for a chat with the multilingual bot
def chat_with_bot():
    print("Multilingual Chatbot")
    print("Supported languages:", list_supported_languages())
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break

        target_lang = 'en'  # Default target language is English
        detected_lang = translator.detect(user_input).lang
        if detected_lang != 'en':
            target_lang = detected_lang

        user_input = translate(user_input, 'en')  # Translate user input to English
        response = chatbot.get_response(user_input)  # Get a response in English
        response = translate(str(response), target_lang)  # Translate the response back

        print(f"Bot ({LANGUAGES[target_lang]}): {response}")

if __name__ == "__main__":
    chat_with_bot()
