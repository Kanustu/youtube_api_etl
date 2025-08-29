import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY") 

if api_key:
    print("api_key loaded successfully")
else:
    print("api key did not load successfully")