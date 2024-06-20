import requests, os
from dotenv import load_dotenv

load_dotenv()

print(requests.get(os.getenv("HELLOWORLD_WORKER_URL")).text)