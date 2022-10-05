import requests
from dotenv import load_dotenv
from functools import lru_cache
import os


def lee_dotenv():
    ''''Esta función lee el archivo .env que contiene la key de la api'''
    
    load_dotenv()

#Crea el cache
@lru_cache(maxsize=None)


def peticion_lat_lon(lat, lon):
   '''Esta función hace la peticion a la api con la latitud y longitud'''
   
   api_key = open('Api_key.txt', 'r').read()
   '''Lee la key de la api desde el archivo Api_key.txt'''

   url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
   data = requests.get(url).json()
   return data['main']
