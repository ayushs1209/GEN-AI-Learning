from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
# gemini-2.5-flash-preview-04-17
modal = "gemini-2.5-flash-preview-04-17"
client = genai.Client()

system_prompt = '''
you are a ai chat assistant which is very good at breakind down problems into smaller ones and analyse the problems on smaller level and then make the output
you're supposed to break down the problem into smaller part
your thought process undergoes the following steps, first you get the user input data then you analyse the input data and then you think about the problem and then you solve the problem by generating a result then you validate your answer then finally you generate the final output based on your previous thought process

you are strictly to follow each of the step one at a time

Example 1: 
user : "What is 2 + 2"
you : {{"step" : "analyse", content: "alright the user wants me to solve a maths query" }}
you : {{"step" : "think", content: "the query wants me to add two numbers and i should follow the mathametical rule to evaluate the expression from left to right" }}
you : {{"step" : "result", content: "2 + 2 should be 4 because it comes after adding 2 with 2" }}
you : {{"step" : "validate", content: "yes the answer = 4 is true as the addition generates 4 as output" }}
you : {{"step" : "output", content: "The answer for the expression 2 + 2 is 4 as it is a basic arithimetic operation which means to add the two numbers" }}


'''

user = input("> ")
chat = client.chats.create(model=modal)
while True:
    if user.lower() == 'quit':
        break
    else:
        response = chat.send_message(user)
        print(response.text)
        continue



















# chat = client.chats.create(model=modal)
# while True:
#     user = input("enter query \n")
#     if user.lower() == "q":
#         break
#     else:
#         response = chat.send_message(user)
#         print(response.text)

