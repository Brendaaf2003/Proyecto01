from Request import *
from Datos import *
from Clima import *
import pandas as pd 
from prettytable import PrettyTable
import cowsay
from functools import lru_cache

cowsay.daemon("Bienvenido a Clima")

tabla_orig = PrettyTable()
tabla_dest = PrettyTable()
tabla_vuelos = PrettyTable()
respuesta = "si"
aux=1

@lru_cache(maxsize=None)

def tablita(num):
    lista=[Ciudad,f'{round(Temp,2)}°C',
                                    f'{round(Temperatura_Maxima,2)}°C',
                                    f'{round(Temperatura_Minima,2)}°C',
                                    Humedad,
                                    f'{round(Difenecia_de_Temperatura,2)}°C']
    return lista

def dic_vuelos_unicos():
    dic={}
    vuelos=zip(vuelos_unicos()['origin'],vuelos_unicos()['destination'])
    for i,j in zip(vuelos_unicos()['ID_Vuelo'],vuelos):
        dic[i]=list(j)
    return dic


tabla_vuelos.field_names=['ID','Origen','Destino']

unicos=zip(vuelos_unicos()['ID_Vuelo'],vuelos_unicos()['origin'],vuelos_unicos()['destination'])

for i,j,k in unicos:
    tabla_vuelos.add_row([i,j,k])



while respuesta == "si":


    print("**********Estas son los vuelos disponibles:**********")
    print(tabla_vuelos)
    print("Ingrese el numero  de tu vuelo")
    orig = input()

    clima_orig, clima_dest = Peticion(dic_vuelos_unicos()[int(orig)][0], 
                                            dic_vuelos_unicos()[int(orig)][1])




    tabla_resultados_de_clima=PrettyTable()
    tabla_resultados_de_clima.field_names = ["Ciudad","Temperatura","Temperatura Maxima","Temperatura Minima","Humedad","Difenecia de Temperatura"]
    Ciudad= dic_vuelos_unicos()[int(orig)][1]
    Temp=clima_dest["temp"]-273.15
    Temperatura_Maxima=(clima_dest["temp_max"]- 273.15)#*5/9
    Temperatura_Minima=(clima_dest["temp_min"]- 273.15)#*5/9
    Humedad=clima_dest['humidity']
    Difenecia_de_Temperatura=(clima_orig["temp"]-273.15)-Temp

    for i in range(aux):
        tabla_resultados_de_clima.add_row(tablita(i+1))

    print(f'**********Estos son los resultados de la ciudad de {dic_vuelos_unicos()[int(orig)][1]} la cual es tu ciudad Destino **********')

    print(tabla_resultados_de_clima)
    aux+=1
    print("Desea realizar otra consulta? si/no")
    respuesta = input()