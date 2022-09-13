import requests
from functools import lru_cache

@lru_cache(maxsize=None)

def clima (lat, lon):
   url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=df3f287580fda7c0dab43d1051a30497'
    data = requests.get(url).json()
    return data['main']
