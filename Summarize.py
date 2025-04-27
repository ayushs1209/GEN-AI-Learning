from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
# gemini-2.5-flash-preview-04-17
client = genai.Client()

model = "gemini-2.5-flash-preview-04-17"

system_prompt = """

You are a math based chat assistant which can only solve math based queries. You are strictly prohibited to solve any other queries

"""

# responses = client.models.generate_content(
#     contents= "what is and why is the color of sky",
#     model=model
# )
# print(responses.text)


# for response in client.models.generate_content_stream(

#     contents= "why is water blue in color in 500 words",
#     model= model,
#     config=types.GenerateContentConfig(
#         # system_instruction=system_prompt,
#         temperature= 2,
#     )
# ):
    
#     print(response.text)

while True:
    query = input("> ")
    if query == 'q':
        break

    response = client.models.generate_content(
        contents=query,
        model=model,
    )
    print(response.text)
    continue
    
