# 🤖 Simple AI Chatbot (Streamlit + OpenAI API)
A simple AI chatbot web application built using **Streamlit** and the **OpenAI Python SDK**.  
The chatbot sends user questions to an LLM and returns concise answers in a clean web interface.
This project demonstrates **LLM API integration, environment variable handling, and simple AI web deployment**.

## 📌 Project Overview
This project integrates a **Large Language Model (LLM) "gpt-5-nano"** using **OpenAI API** into a web application.

## Workflow
User Question → Streamlit UI → OpenAI API (API Request) → LLM Processing (gpt-5-nano) → Response → Display in Web App.
The application allows users to type questions and receive AI-generated responses in real time.

### Workflow Explanation
1. **User Input**  
   The user enters a question through the Streamlit chat interface.
2. **Frontend Handling**  
   Streamlit captures the input and sends it to the backend Python logic.
3. **API Request**  
   The application sends the prompt to the OpenAI API.
4. **LLM Processing**  
   The Large Language Model processes the request and generates a response.
5. **Response Rendering**  
   The generated response is displayed back to the user in the Streamlit interface.

## 📂 Project Structure
```text
chatbot/
│
├── app.py # Streamlit web app
├── chatbot.py # Basic LLM API test script
├── requirements.txt
├── README.md
└── .env # API key storage (not pushed to GitHub)
```
## ⚙️ Requirements & Installation
#### Clone or Download the Project 
git clone https://github.com/mahamjameel61/AI_Chatbot.app 
cd chatbot
#### Install Required Libraries
pip install openai – Connects the application with the LLM API
pip install python-dotenv – Loads API keys securely from the .env file
pip install streamlit – Creates the web interface for the chatbot
#### Add Your API Key in .env file 
Create a .env file in the project folder and add your OpenAI API key (secret key):
OPENAI_API_KEY="your_api_key_here" 
You can create an API key from: https://platform.openai.com/api-keys
#### Run the Application
streamlit run app.py
After running the command, the application will automatically open in your browser:
http://localhost:8501

### Tech stack
Python| Streamlit| OpenAI Python SDK| python-dotenv (Environment variable management)

---
## 📊 Learning Outcomes
Through this project, the following concepts are demonstrated:

- **LLM API Integration**  
  Connecting a Python application to a Large Language Model using the OpenAI API.

- **Prompt-Based Interaction with Language Models**  
  Sending user prompts to the model and receiving generated responses.

- **Streamlit Web Application Development**  
  Building a simple interactive web interface for an AI application.

- **Secure API Key Management**  
  Using environment variables (`.env`) to store and load sensitive credentials securely.

- **Basic AI Application Deployment Workflow** 
  Structuring a project with dependencies (`requirements.txt`) and preparing it for local or cloud deployment.


