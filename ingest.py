import requests
import os
import csv
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY") 

if API_KEY:
    print("key loaded successfully")
else:
    print("key did not load successfully")

