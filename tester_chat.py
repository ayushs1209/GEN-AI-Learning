from google import genai
from google.genai import types
from dotenv import load_dotenv
import requests

load_dotenv()

client = genai.Client()
model = "gemini-2.5-flash-preview-04-17"
system_prompt = """
Your name is Ragnar the III
You are a Helpful and Knowledgeable AI Assistant. Your primary function is to understand user queries and provide accurate, relevant, and helpful information or complete requested tasks to the best of your ability.
You can do mathematical queries you can process your thoughts like a chain. you should analyze the user input, think for a solution then provide a solution after verifying it.
you can make a hybrid system and use the tools given to you and on your own understanding you can generate the output

Example 1 :
user: what is the weather in Jammu
model: the user wants to ask for the weather in jammu
model: I have a tool that lets me calculate the weather in a location
model: i should pass the location to the function and get the result as the weather statitics of the place
model: generate the output
Example 1 :
user: what is the average of the weather of jammu mumbai and patiala
model: user wants me to calculate the average of the weathers of jammu mumbai and patiala
model: i should call the tool to fetch the weather and keep the results
model: now I can average the numerical values of the weather outputs of the different locations
model: now I should return the average weather of the three states and generate the output as the user asked me to



"""
chat = client.chats.create(model=model)

def get_current_weather(location: str) -> str:
    url = f"https://wttr.in/{location}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {location} is {response.text}"
    return "Something Went Wrong"

while True:
    user = input("> ")
    if user == 'q':
        break

    response = chat.send_message(
        user,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[get_current_weather]
            ),
    )
    print(response.text)