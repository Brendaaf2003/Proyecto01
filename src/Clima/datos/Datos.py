from requests import *
import pandas as pd
import os

rutaAbsoluta1 = open('Ruta_Absoluta.txt', 'r').read()

'''Variable que contiene la ruta absoluta del archivo .env'''


def leer_base_de_datos(rutaAbsoluta = rutaAbsoluta1):
    '''Esta función lee la base de datos y la convierte en un dataframe'''

    df = pd.read_csv(rutaAbsoluta)
    return df.drop_duplicates()

def obtener_vuelos_unicos(rutaAbsoluta = rutaAbsoluta1):
    '''Esta función filtra los vuelos unicos'''


#Esta función lee la base de datos y la convierte en un dataframe
def leer_base_de_datos(rutaAbsoluta = rutaAbsoluta1):
    df = pd.read_csv(rutaAbsoluta)
    return df.drop_duplicates()

#Esta función filtra los vuelos unicos
def obtener_vuelos_unicos(rutaAbsoluta = rutaAbsoluta1):

    df = leer_base_de_datos(rutaAbsoluta)
    df = df[['origin', 'destination']].drop_duplicates()
    df['ID_Vuelo'] = [i for i in range(1, len(df) + 1)]
    return df


def extraer_coordenadas(edo, orig = True, rutaAbsoluta = rutaAbsoluta1):
    '''Esta función extrae las coordenadas de los estados de origen y destino'''

#Esta función extrae las coordenadas de los estados de origen y destino
def extraer_coordenadas(edo, orig = True, rutaAbsoluta = rutaAbsoluta1):

    df = leer_base_de_datos(rutaAbsoluta)
    if orig:
        return df[df['origin'] == edo][['origin_latitude', 'origin_longitude']].values[0]
    else:   
        return df[df['destination'] == edo][['destination_latitude', 'destination_longitude']].values[0]