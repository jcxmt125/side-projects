import requests, multiprocessing
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

#CFAI prep
API_BASE_URL = "https://gateway.ai.cloudflare.com/v1/"+CLOUDFLARE_USER_ID+"/"+CLOUDFLARE_AI_GATEWAY_SLUG+"/workers-ai/"
headers = {"Authorization": "Bearer "+CLOUDFLARE_AI_API_KEY}
def run(model, inputs):
    input = { "stream": True, "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response


def gemini(modelChosen, inputs):
    model = genai.GenerativeModel(modelChosen)

    response = model.generate_content(inputs)

    print("Request completed to " + modelChosen + "\n> " + response.text)

    inputs.append({ "role": "model", "content": [response.text] })

    return inputs

def cfllm(modelChosen, inputs):

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

    print("Request completed to " + modelChosen + "\n> " + str(fullresp))


if __name__ == "__main__":
    models = ['gemini-1.5-flash-latest','gemini-1.0-pro','@hf/meta-llama/meta-llama-3-8b-instruct','@hf/mistral/mistral-7b-instruct-v0.2','@cf/google/gemma-7b-it-lora','@cf/meta/llama-3.1-8b-instruct']

    systemPrompt = input("What should the system prompt be? \n> ")

    if systemPrompt == "":
        systemPrompt = "You are a friendly assistant."

    modelmemories = dict()

    for i in models:

        if i.startswith("gemini"):
            modelmemories[i] = [{"role":"user", "parts":[systemPrompt]}]

        else:
            modelmemories[i] = [{"role": "system", "content": systemPrompt}]

    while True:

        messageSend = input("You: ")
        
        if messageSend == "": break
        
        processes = []

        for i in models:
            modelChosen = i

            if modelChosen.startswith("gemini"):
                modelmemories[modelChosen].append({"role": "user", "parts": [messageSend]})
                processes.append(multiprocessing.Process(target=gemini, args=(modelChosen, modelmemories[modelChosen])))

            else:

                modelmemories[modelChosen].append({"role": "user", "content": messageSend})
                processes.append(multiprocessing.Process(target=cfllm, args=(modelChosen, modelmemories[modelChosen])))

        for i in processes:
            #It's **start** not **run**
            i.start()

        for i in processes:
            i.join()

