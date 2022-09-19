import requests
from dotenv import load_dotenv
from functools import lru_cache
import os

#Leer el archivo .env (Key api)
def config():
    load_dotenv()

#Crea el cache
@lru_cache(maxsize=None)

#Funcion que hace la peticion a la api con la latitud y longitud
def clima (lat, lon):
   config()
   url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv("api")}'
   data = requests.get(url).json()
   return data['main']
