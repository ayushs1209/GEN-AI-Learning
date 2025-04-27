from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from PIL import Image

# api = os.getenv("GOOGLE_API_KEY")
load_dotenv()

client = genai.Client()
# system_prompt_text = """
#     you are a coding ai assistant and will only solve coding problems which are given to you.
#     You will return only the code that the user wants you to generate and also generate one example with the code and the coreesponding output for it
#     **Very Important instruction** you cannot solve any other query you are only supposed to solve coding problems and nothing else

#     Example 1:
#     input : "Hi"
#     output : "hell0 how are you"
#     input: "Can you tell me what is 2 + 2"
#     output : " I am a Coding Ai Assistant and I am not able to help you with your query" 
#     Example 2:
#     input: "why is nextjs used worldwide more"
#     output : " I am a Coding Ai Assistant and I am not able to help you with your query" 
#     Example 1:
#     input: "can you make a python code for generating a sum of two numbers"
#     output : "num1 = int(input("Enter first number: "))
#               num2 = int(input("Enter second number: "))
#               print("Sum:", num1 + num2)" 

# """
system_prompt_text = """
    you are very good at breaking down the problem into smaller bits which makes it easier to understand the concept applied
    you will always first take the user input then analyse the problen then think about it several times and then provide a solution to the problem which then further you will validate the solution by logic before giving the final output
    you basically break down the problem in multiple steps before conmpletely solving it
    Rule : You must follow the strict json object response format

    Example 1:
    input : "Hi"
    output : "hell0 how are you"

    input: "Can you tell me what is 2 + 2"
    output :{{ step: "analyse", content :"Alright the user is interested in a mathematical query and he is asking for a basic addition query}}
    output :{{ step: "think", content :"To perform the addition you must evalute the expression from left to right as per the rules of mathematics}}
    output :{{ step: "output", content :"4}}
    output :{{ step: "validate", content :"seems like 4 is the right answer for the given expression as when you add 2 to 2 then it becomes 4}}
    output :{{ step: "result", content :"The sum of 2 + 2 is 4 which is calculated by adding the two numbers from left to right according to the rules of mathematics}}
    

"""
# system_prompt_text = """
#     you are a maths ai assistant and will only solve maths problems which are given to you.
#     you are very good at breaking down the problem into smaller bits which makes it easier to understand the concept applied
#     you will always first take the user input then analyse the problen then think about it then again think about it several times and then provide a solution to the problem which then further you will validate the solution by logic before giving the final output
#     you basically break down the problem in multiple steps before conmpletely solving it
#     **Very Important instruction** you cannot solve any other query you are only supposed to solve mathematical problems and nothing else
#     Rule : You must follow the strict json object response format

#     Example 1:
#     input : "Hi"
#     output : "hell0 how are you"

#     input: "Can you tell me what is 2 + 2"
#     output :{{ step: "analyse", content :"Alright the user is interested in a mathematical query and he is asking for a basic addition query}}
#     output :{{ step: "think", content :"To perform the addition you must evalute the expression from left to right as per the rules of mathematics}}
#     output :{{ step: "output", content :"4}}
#     output :{{ step: "validate", content :"seems like 4 is the right answer for the given expression as when you add 2 to 2 then it becomes 4}}
#     output :{{ step: "result", content :"The sum of 2 + 2 is 4 which is calculated by adding the two numbers from left to right according to the rules of mathematics}}
    

# """
# gemini-2.0-flash
# gemini-2.5-flash-preview-04-17
# response = client.models.generate_content(
#     model='gemini-2.5-flash-preview-04-17', contents ='what is greater 9.8 or 9.11' ,
#     config=types.GenerateContentConfig(

#         system_instruction=system_prompt_text,
#         temperature=0.5,
#     )
# )
# print(response.text)
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash-preview-04-17',
    contents=[
        'if i run a model through ollama does it cost me ',
    ]
)
print(response.text)




# for chunk in client.models.generate_content_stream(
#     model='gemini-2.5-flash-preview-04-17', contents='Tell me a story about a bird in 300 words.'
# ):
#     print(chunk.text, end='')