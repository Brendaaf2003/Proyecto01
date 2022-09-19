import requests
from dotenv import load_dotenv
from functools import lru_cache
import os

def config():
    load_dotenv()

@lru_cache(maxsize=None)

def clima (lat, lon):
   config()
   url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv("api")}'
   data = requests.get(url).json()
   return data['main']
