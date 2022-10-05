from Request import *
from Datos import *
from Clima import *
import pandas as pd 
from prettytable import PrettyTable
from functools import lru_cache


def crear_tabla():
    '''Esta función crea las tablas para mostrar los datos'''

    tabla_orig = PrettyTable()
    tabla_dest = PrettyTable()
    tabla_vuelos = PrettyTable()
    respuesta = "si"
    aux=1
    return tabla_orig, tabla_dest, tabla_vuelos, respuesta, aux

def llenar_tabla(num,Ciudad,Temp,Temperatura_Maxima,Temperatura_Minima,Humedad,Difenecia_de_Temperatura):
    '''Esta función crea las tablas para mostrar los datos'''
    lista=[Ciudad,f'{round(Temp,2)}°C',
                                f'{round(Temperatura_Maxima,2)}°C',
                                f'{round(Temperatura_Minima,2)}°C',
                                Humedad,
                                f'{round(Difenecia_de_Temperatura,2)}°C']
    return lista



