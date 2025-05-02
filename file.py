# google_full_content.py
import requests
from bs4 import BeautifulSoup
import os


# API_KEY = os.getenv("SEARCH_API_KEY")
# CX = os.getenv("SEARCH_ENGINE_KEY")

# query = input("Search Google: ")
# url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}'
# response = requests.get(url).json()

# for item in response.get('items', [])[:2]:
#     # print(" item['title'], "\n", item['link'])
#     print("item['title'], \n")
#     try:
#         page = requests.get(item['link'], timeout=5)
#         soup = BeautifulSoup(page.text, 'html.parser')
#         text = soup.get_text(separator=' ', strip=True)
#         print("Query result", text[:1000], "\n")  # show only first 300 chars
#     except:
#         print("⚠️ Could not fetch content.\n")



find = input()
url = f"https://www.google.com/search?q={find}"

req = requests.get(url)
soup = BeautifulSoup(req.text,"html.parser")

mysearch = soup.find("div",class_= "BNeawe").text
print(mysearch)