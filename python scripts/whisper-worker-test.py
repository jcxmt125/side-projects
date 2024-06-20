import requests
from dotenv import load_dotenv

load_dotenv()

import os

def cfwhisperworker():
  # API URL: your workers URL!
  API_URL = os.getenv("WHISPER_WORKER_URL")

  # Open the audio file in binary mode

  # Set headers with authorization token
  headers = {"fileUrl": input("Drop file URL: "),
             "authKey": os.getenv("WHISPER_WORKER_KEY")}

  # Send POST request with audio data
  response = requests.get(API_URL, headers=headers)


  # Check for successful response
  if response.status_code == 200:
    return (response.json())
  else:
    return response.json()
  
if __name__ == "__main__":
  print(cfwhisperworker())