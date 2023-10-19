// script.js
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const languageSelector = document.getElementById('language-selector');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', sendMessage);

function sendMessage() {
    const userMessage = userInput.value;
    if (userMessage.trim() === '') return;

    const targetLanguages = [...languageSelector.selectedOptions].map(option => option.value);
    if (targetLanguages.length === 0) return;

    appendMessage(`You: ${userMessage}`);
    userInput.value = '';

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: userMessage, target_languages: targetLanguages }),
    })
    .then(response => response.json())
    .then(data => {
        for (const [language, translation] of Object.entries(data)) {
            appendMessage(`${language} Translation: ${translation}`);
        }
    });
}

function appendMessage(message) {
    chatBox.innerHTML += `<p>${message}</p>`;
}
