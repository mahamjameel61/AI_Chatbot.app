# 🤖 Simple AI Chatbot (Streamlit + OpenAI API)
A simple AI chatbot web application built using **Streamlit** and the **OpenAI Python SDK**.  
The chatbot sends user questions to an LLM and returns concise answers in a clean web interface.
This project demonstrates **LLM API integration, environment variable handling, and simple AI web deployment**.

## 📌 Project Overview
This project integrates a **Large Language Model (LLM) "gpt-5-nano"** using **OpenAI API** into a web application.

## Workflow
User Question → Streamlit UI → OpenAI API (API Request) → LLM Processing (gpt-5-nano) → Response → Display in Web App
The application allows users to type questions and receive AI-generated responses in real time.

### Tech stack
Python| Streamlit| OpenAI Python SDK| python-dotenv (Environment variable management)

# 📂 Project Structure
chatbot/
│
├── app.py # Streamlit web app
├── chatbot.py # Basic LLM API test script
├── requirements.txt
├── README.md
└── .env # API key storage (not pushed to GitHub)
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


