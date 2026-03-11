"""
python-dotenv is a Python library that simplifies the process of managing environment variables by loading key-value pairs from a .env file into the application's environment. 
This practice helps developers keep sensitive information, such as API keys and database credentials, out of the source code.
"""
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()

"""
A Python dotenv file is a plain text file that contains configuration data in the form of key-value pairs, where both the key and the value are treated as strings."""

#Test a basic API request(official documentation of OpenAI Python library)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

response = client.responses.create(
    model="gpt-5-nano", #llm integrated.
    input="what is the capital of pakistan?",
    instructions="you are a helpful assistant that provides concise answers to questions"
)
print(response.output_text)
