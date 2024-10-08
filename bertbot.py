import os
import nltk
import ssl
import streamlit as st
import random
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Set up SSL and download NLTK data
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Define the intents
intents = [
    {"tag": "greeting", "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"], "responses": ["Hi there", "Hello", "Hey", "I'm fine, thank you", "Nothing much"]},
    {"tag": "goodbye", "patterns": ["Bye", "See you later", "Goodbye", "Take care"], "responses": ["Goodbye", "See you later", "Take care"]},
    {"tag": "thanks", "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"], "responses": ["You're welcome", "No problem", "Glad I could help"]},
    {"tag": "about", "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"], "responses": ["I am a chatbot", "My purpose is to assist you", "I can answer questions and provide assistance"]},
    {"tag": "help", "patterns": ["Help", "I need help", "Can you help me", "What should I do"], "responses": ["Sure, what do you need help with?", "I'm here to help. What's the problem?", "How can I assist you?"]},
    {"tag": "age", "patterns": ["How old are you", "What's your age"], "responses": ["I don't have an age. I'm a chatbot.", "I was just born in the digital world.", "Age is just a number for me."]},
    {"tag": "weather", "patterns": ["What's the weather like", "How's the weather today"], "responses": ["I'm sorry, I cannot provide real-time weather information.", "You can check the weather on a weather app or website."]},
    {"tag": "budget", "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"], "responses": ["To make a budget, start by tracking your income and expenses..."]},
    {"tag": "credit_score", "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"], "responses": ["A credit score is a number that represents your creditworthiness..."]}
]

# Load pre-trained BERT tokenizer and model for intent classification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(intents))

# Prepare the data (Assuming you have a more structured training setup for BERT)
tags = [intent['tag'] for intent in intents]

def predict_intent(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    pred_tag = tags[torch.argmax(outputs.logits, dim=1).item()]
    return pred_tag

# Use BERT intent prediction in the chatbot
def chatbot(input_text):
    tag = predict_intent(input_text)
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

# Deploy the chatbot with Streamlit
def main():
    st.title("Chatbot")
    st.write("Welcome! Please type a message below.")

    user_input = st.text_input("You:")
    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100)

if __name__ == '__main__':
    main()
