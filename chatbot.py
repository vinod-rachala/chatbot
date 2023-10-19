# chatbot.py
from transformers import MarianMTModel, MarianTokenizer
from flask import Flask, request, jsonify

app = Flask(__name)

# Initialize the translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-{target_language}"
translator = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

@app.route('/translate', methods=['POST'])
def translate():
    user_input = request.json.get('user_input')
    target_languages = request.json.get('target_languages')

    translations = {}
    for target_language in target_languages:
        target_model_name = model_name.format(target_language=target_language)
        target_translator = MarianMTModel.from_pretrained(target_model_name)
        target_tokenizer = MarianTokenizer.from_pretrained(target_model_name)
        
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        translated_ids = target_translator.generate(input_ids, num_return_sequences=1)
        translation = target_tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        
        translations[target_language] = translation

    return jsonify(translations)

if __name__ == '__main__':
    app.run()
