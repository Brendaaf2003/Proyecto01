import requests
from dotenv import load_dotenv
from functools import lru_cache
import os

#Leer el archivo .env (Key api)
def lee_dotenv():
    
    load_dotenv()

#Crea el cache
@lru_cache(maxsize=None)

#Funcion que hace la peticion a la api con la latitud y longitud
def peticion_lat_lon(lat, lon):
   
   api_key = open('Api_key.txt', 'r').read()

   url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
   data = requests.get(url).json()
   return data['main']
