from dotenv import load_dotenv
import PIL.Image, os

load_dotenv()

import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

image = []

while True:
    
    filePath = input("Drag file here: ")
    
    if filePath == "": break

    image.append(PIL.Image.open(filePath))

construct = [{'role':'user','parts': ["What is in these images?"] + image}]

model = genai.GenerativeModel('gemini-1.5-flash-latest')

response =  model.generate_content(construct)

print(response.text)