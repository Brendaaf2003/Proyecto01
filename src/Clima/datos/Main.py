from Request import *
from Datos import *
from Clima import *
import pandas as pd 
from prettytable import PrettyTable
import cowsay
from functools import lru_cache

#Dada la bienvenida al usuario
cowsay.daemon("Bienvenido a Clima")

#Genera tablas para mostrar los datos
tabla_orig = PrettyTable()
tabla_dest = PrettyTable()
tabla_vuelos = PrettyTable()
respuesta = "si"
aux=1

#Genera cache para las peticiones
@lru_cache(maxsize=None)

#Genera una tabla con los datos del clima
def tablita(num):
    lista=[Ciudad,f'{round(Temp,2)}°C',
                                f'{round(Temperatura_Maxima,2)}°C',
                                f'{round(Temperatura_Minima,2)}°C',
                                Humedad,
                                f'{round(Difenecia_de_Temperatura,2)}°C']
    return lista

#Coloca un ID de los vuelos unicos
def dic_vuelos_unicos():
    dic={}
    vuelos=zip(vuelos_unicos()['origin'],vuelos_unicos()['destination'])
    for i,j in zip(vuelos_unicos()['ID_Vuelo'],vuelos):
        dic[i]=list(j)
    return dic

#crea los titulos de la tabla de los vuelos unicos
tabla_vuelos.field_names=['ID','Origen','Destino']

#crea tuplas con los datos de los vuelos unicos
unicos=zip(vuelos_unicos()['ID_Vuelo'],vuelos_unicos()['origin'],vuelos_unicos()['destination'])

#agrega los datos de los vuelos unicos a la tabla
for i,j,k in unicos:
    tabla_vuelos.add_row([i,j,k])


#Mientras la respuesta sea si, se ejecuta el programa
while respuesta == "si":

    #Pide el ID del vuelo
    print("**********Estas son los vuelos disponibles:**********")
    print(tabla_vuelos)
    print("Ingrese el numero  de tu vuelo")
    orig = input()

    clima_orig, clima_dest = Peticion(dic_vuelos_unicos()[int(orig)][0], 
                                            dic_vuelos_unicos()[int(orig)][1])



    #Muestra los datos del clima de origen
    tabla_resultados_de_clima=PrettyTable()
    tabla_resultados_de_clima.field_names = ["Ciudad","Temperatura","Temperatura Maxima","Temperatura Minima","Humedad","Difenecia de Temperatura"]
    Ciudad= dic_vuelos_unicos()[int(orig)][1]
    Temp=clima_dest["temp"]-273.15
    Temperatura_Maxima=(clima_dest["temp_max"]- 273.15)#*5/9
    Temperatura_Minima=(clima_dest["temp_min"]- 273.15)#*5/9
    Humedad=clima_dest['humidity']
    Difenecia_de_Temperatura=(clima_orig["temp"]-273.15)-Temp

    #agrerga los datos de la tabla principal de los datos de clima
    for i in range(aux):
        tabla_resultados_de_clima.add_row(tablita(i+1))

    #Muestra los los resultados de los datos de clima
    print(f'**********Estos son los resultados de la ciudad de {dic_vuelos_unicos()[int(orig)][1]} la cual es tu ciudad Destino **********')

    #Regresa una tabla con los datos de clima destino
    print(tabla_resultados_de_clima)
    aux+=1

    #Pregunta al usuario si seleccionar otra ciudad
    print("Desea realizar otra consulta? si/no")
    respuesta = input()