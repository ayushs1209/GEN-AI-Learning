import google.generativeai as genai
import os 
from dotenv import load_dotenv
from google.generativeai import types
load_dotenv()

contents = [
    {"role": "model", "parts": "You are 'CodeHelper', an AI assistant whose SOLE function is to help users with coding tasks.You cannot answer any query except coding related query'"},
    {"role": "user", "parts": "what is 2 + 34"},
]
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

response = model.generate_content(contents,
                                  
                                  )
print(response.text)