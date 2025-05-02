from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv()

model = "gemini-2.5-flash-preview-04-17"

client = genai.Client()

chat = client.chats.create(model=model)


while True:
    response = chat.send_message(
    message= input("> "),
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                code_execution=types.ToolCodeExecution(),
            )
        ]
    )
)

    print(response.text)