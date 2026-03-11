import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

#page_configuration
st.set_page_config(page_title="AI Chatbot", layout="centered")

# Streamlit page title
st.title("🤖Simple AI Chatbot")
st.write("Ask anything!")

# User input
user_input = st.chat_input("Enter your question:")

# When user clicks button
if st.button("Ask AI"):

    if user_input:
        response = client.responses.create(
            model="gpt-5-nano",
            input=user_input,
            instructions="you are a helpful assistant that provides concise answers to questions"
        )

        # Display result
        st.subheader("AI Response:")
        st.write(response.output_text)

    else:
        st.warning("Please enter a question.")
