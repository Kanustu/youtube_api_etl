import requests
import os
import csv
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY") 


# if API_KEY:
    #print("key loaded successfully")
#else:
    #print("key did not load successfully")

base_url = 'https://www.googleapis.com/youtube/v3/videos'
params = {
    'part': 'snippet, statistics',
    'chart': 'mostPopular',
    'maxResults': 5,
    'regionCode': 'US',
    'key': API_KEY
    }

response = requests.get(base_url, params = params)
print(response.json())
