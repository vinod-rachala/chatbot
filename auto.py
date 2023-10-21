from transformers import MarianMTModel, MarianTokenizer, pipeline

# Initialize the translation model and tokenizer
translator = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-multilingual")
translator_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-multilingual")

# Initialize the chatbot model and tokenizer (using GPT-3 for demonstration)
chatbot = pipeline("conversational", model="gpt2")

# Create a function to automatically detect the user's language
def detect_user_language(input_text):
    # You can use language detection libraries like langdetect or deep learning models for better accuracy
    # For simplicity, we assume English as the default language for demonstration
    return "en"

# Create a function to translate user input to English
def translate_to_english(text, src_language):
    if src_language != "en":
        inputs = translator_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = translator.generate(**inputs)
        translated_text = translator_tokenizer.batch_decode(translated, skip_special_tokens=True)
        return translated_text[0]
    return text

# Create a function to handle user input and generate responses
def chat_with_bot():
    while True:
        user_input = input("You: ")
        src_language = detect_user_language(user_input)
        
        # Translate user input to English for processing
        input_text = translate_to_english(user_input, src_language)
        
        # Get the chatbot's response
        response = chatbot(input_text)[0]["generated_text"]
        
        # Translate the response back to the user's language
        response_text = translator.generate(input_text, src_language, return_tensors="pt")
        response_text = translator_tokenizer.batch_decode(response_text, skip_special_tokens=True)

        print(f'Bot: {response_text[0]}')

# Start the chat with the chatbot
if __name__ == '__main__':
    print("Chat with the Multilingual Bot. Type 'exit' to end the conversation.")
    chat_with_bot()
