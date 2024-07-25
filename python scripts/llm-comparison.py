import requests
from dotenv import load_dotenv
import os
import random

load_dotenv()

CLOUDFLARE_AI_GATEWAY_SLUG = os.getenv("CLOUDFLARE_AI_GATEWAY_SLUG")
CLOUDFLARE_USER_ID = os.getenv("CLOUDFLARE_USER_ID")
CLOUDFLARE_AI_API_KEY = os.getenv("CLOUDFLARE_AI_API_KEY")

import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

models = ['gemini-1.5-flash-latest','gemini-1.0-pro','@hf/meta-llama/meta-llama-3-8b-instruct','@hf/mistral/mistral-7b-instruct-v0.2','@cf/google/gemma-7b-it-lora','@cf/meta/llama-3.1-8b-instruct']

modelChosen = random.choice(models)

print("Return an empty line to finish!")

systemPrompt = "You are a friendly assistant. You should not reveal what model you are based on."

#CFAI prep
API_BASE_URL = "https://gateway.ai.cloudflare.com/v1/"+CLOUDFLARE_USER_ID+"/"+CLOUDFLARE_AI_GATEWAY_SLUG+"/workers-ai/"
headers = {"Authorization": "Bearer "+CLOUDFLARE_AI_API_KEY}
def run(model, inputs):
    input = { "stream": True, "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response


if modelChosen.startswith("gemini"):
    model = genai.GenerativeModel(modelChosen)

    memory = [{'role':'user','parts': [systemPrompt]}]

    while True:
        userPrompt = input("You: ")

        if userPrompt == "": break

        memory.append({'role':'user','parts': [userPrompt]})

        response = model.generate_content(memory)

        print(response.text)

        memory.append({'role':'model','parts': [response.text]})
    
    print("The model you were talking to was " + modelChosen)

else:
    inputs = [
    { "role": "system", "content": systemPrompt }
    ]

    while True:
        userPrompt = input("You: ")

        if userPrompt == "": break

        inputs.append({ "role": "user", "content": userPrompt })

        plaintext = ""
        fullresp = ""

        output = run(modelChosen, inputs)
        
        for line in output:  
            if line:  # Is it actually a new line?
                # Handle each line of the response (text generation)
                plaintext += line.decode("utf-8")        

        while plaintext.find('"response":') != -1:
            whereis = plaintext.find('"response":')
            plaintext = plaintext[whereis+12:]
            whereto = plaintext.find('"')
            fullresp += plaintext[:whereto]
        
        if fullresp[-1] == fullresp[-2]:
            fullresp = fullresp[:-1]

        while fullresp[0] == " ":
            fullresp = fullresp[1:]

        print(str(fullresp))

        inputs.append({ "role": "assistant", "content": fullresp })

    print("The model you were talking to was " + modelChosen)

input()