import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Check if the API key is loaded
if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in environment variables.")
    print("Please create a .env file with GOOGLE_API_KEY='YOUR_API_KEY'")
else:
    # Configure the Gemini API
    genai.configure(api_key=GOOGLE_API_KEY)

    # Create the model
    # Refer to the Gemini API quickstart docs for more information on GenerativeModel
    model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

    # Start a chat session
    chat = model.start_chat(history=[])
    print("Gemini Chat App - Type 'quit' to exit")
    print("-------------------------------------")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        try:
            # Send the message and get the response
            response = chat.send_message(user_input)

            # Print the response
            # Ensure response content is available before accessing .parts[0].text
            if response and response.parts:
                 print("Gemini:", response.parts[0].text)
            else:
                 print("Gemini: Could not get a response.")

        except Exception as e:
            print(f"An error occurred: {e}")

    print("Chat ended.")
