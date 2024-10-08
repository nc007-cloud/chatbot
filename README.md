# BERT-Powered Chatbot

This repository contains a chatbot implementation using BERT for intent recognition and Streamlit for deployment. The bot can recognize various intents such as greetings, farewells, and specific questions, and it provides appropriate responses based on user input.

## Features
- **Intent Recognition**: Uses BERT for high-quality intent recognition.
- **Responses**: Predefined responses for each intent tag.
- **Deployment**: Simple deployment using Streamlit for a web-based interface.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bertbot.git
cd bertbot

**### 2. Create and Activate a Conda Environment**
Create a new Conda environment for package compatibility.
conda create -n bertbot python=3.8
conda activate bertbot

**#### 3. Install Dependencies**
###Install the necessary packages using conda-forge.
conda install -c conda-forge streamlit transformers=4.29.0 tokenizers=0.13.3 huggingface_hub=0.15.1 pytorch


****### 4. Run the Chatbot**
streamlit run bertbot.py

How to Use the Chatbot
Open the URL provided by Streamlit (usually http://localhost:8501) in your browser.
Type your message in the input box, and the chatbot will respond based on the recognized intent.
The bot supports intents like greeting, goodbye, thanks, help, about, and more.
Example Intents
Below are some sample intents the bot can handle:

Greeting: "Hello", "Hey", "Hi there!"
Goodbye: "Bye", "See you", "Take care!"
Help: "I need help", "Can you assist me?"
About: "What are you?", "What's your purpose?"
Troubleshooting
If you encounter any issues with packages, ensure that all dependencies are installed in the active Conda environment. If problems persist, try recreating the environment following the setup steps.

Contributing
Contributions are welcome! Please submit a pull request with suggested changes, and ensure to follow repository guidelines.


