from dotenv import load_dotenv
import PIL.Image, os

load_dotenv()

import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

image = PIL.Image.open(input("Drag file here: "))

construct = [{'role':'user','parts': ["What is in this image?", image]}]

model = genai.GenerativeModel('gemini-1.5-flash-latest')

response =  model.generate_content(construct)

print(response.text)