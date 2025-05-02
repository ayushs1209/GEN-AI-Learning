system_prompt_text = """
    you are a maths ai assistant and will only solve maths problems which are given to you.
    **Very Important instruction** you cannot solve any other query you are only supposed to solve mathematical problems and nothing else

    Example 1:
    input : "Hi"
    output : "hell0 how are you"

    input: "Can you tell me what is 2 + 2"
    output : "The Answer of 2 + 2 is 4 as it is a basic addition problem" 

    input: "Can you tell me what is 3*3"
    output : "The Answer of 3*3 = 9 and here's a fun fact if you want to multiply any numvber by 5 half the number and multiply it by 10 to get the answer" 

    Example 2:
    input: "why is nextjs used worldwide more"
    output : " I am a Maths Ai Assistant and I am not able to help you with your query" 

    Example 1:
    input: "can you make a python code for generating a sum of two numbers"
    output : "I am a Maths Ai Assistant and I am not able to help you with your query"

"""

'''
model='gemini-2.5-flash-preview-04-17', contents ='what is your knowledge cutoff' ,
    model='gemini-2.5-flash-preview-04-17', contents =' can you generate a basic html and css file which has a slider game that used a random number between 0 to 10 and then the user has to guess the number using the slider and the user has 3 tries to guess the number and if he guesses correct he should win the game but if he guesses lesser then a prompt should appear that the number you guessed is lesser and the same likewise for higher number which would happen only for 3 tries from the starting try after then the game should reset if he could not guess the number in addition to this also add a restart button which resets the game when pressed' ,
'''
"""You are intelligent enought to make files, make directories, add content to a file, remove content from a file, delete a file, read data from a file, write or overwrite data to a file upon the instruction of the user. The instruction aren't language specific so if I tell you to make a file in any language you have the brains to make the file and now by the help of the run_a_command tool you can help the user generate the content in specific file"""

"""
make a directory in the exisiting directory by the name of my-portfolio and as the name suggests it should contain files for my personalised portfolio I want you to make and add each required files to the portfolio directory and now I will give you the instructions for the portfolio app. The app should be made as a full stack website using react and the corresponding necessary components which must include every file related to it. The website should be responsive and very neatly made. Now I shall give you the instructions about the portfolio owner. My name is Ayush Sus and I am software developer. I expertise in Java Python and C++. I also have a good hold over full stack web development using the mern stack and also next js. I also make gen ai based applications too. the theme of the portfolio by default should be in dark mode and there should be a dedicated small button to change it to light mode. The website should follow aesthetical colors which should MOSTLY include gradient based colors only. The portfolio web app should be filled with animations and hover effects. The animations should be smooth throughout in the website and the hover effect should also be throughout the app and also add onscroll animations and effects which should work always on scroll. all of this is a must to have features and you also can add some more aesthetic features as well if you want. You should make all the files and should follow every instruction given to you about the portfolio app. and also make a readme file in which there are instructions to run the portfolio


"""



"""

make a directory named my-portfolio in which as the name suggests generate the code files for the portfolio website. tech stack of the website should be html css and javascript. information about the portfolio owner, name ayush sus, i am a softwarte developer specializing in java, python c++. i also have full command over full stack web develpmet using the mern stack, and i also love making RAG applications using Generative Ai. general instructions. the website should follow a aesthetical theme. the default themefor the website should be a dark theme with a dedicated small button to chang ethe theme to light mode and back to dark mode. gradient colors should be strictly used instead of simple plain solid colors. the website should be responsive over different devices and should be full of animations, animations should be smooth and the website should also have hover effects for almost everything and also should have scroll effects too for each type of scroll. all of this should be achieved html css and javascript while following the instructions strictly 



"""