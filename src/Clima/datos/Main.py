from Request import *
from Datos import *
from Clima import *
from TablaDatos import *
import pandas as pd 
from prettytable import PrettyTable
import cowsay
from functools import lru_cache

cowsay.daemon("Bienvenid@ a Climapp")
'''Da la bienvenida al usuario'''

#Asegura de que la ruta absoluta sea la correcta
try:
    leer_base_de_datos()
except:
    print(" \n\n ************** \U0001F62A Algo salio mal \U0001F62A **************\n")
    print(" \n La ruta absoluta no es correcta, por favor corrigela en el archivo Ruta_Absoluta.txt \n")
    print(" \U0001F440 Revisa que no tenga espacios en blanco al final \U0001F440 \n")
    os._exit(1)

#Asegura que la key de la api sea la correcta
try:
    peticion_lat_lon(0, 0)
except:
    print(" \n\n ************** \U0001F62A Algo salio mal \U0001F62A **************\n")
    print(" \n La key de la api no es correcta, por favor corrigela en el archivo Api_key.txt \n")
    os._exit(1)

#Genera tablas para mostrar los datos
tabla_orig, tabla_dest, tabla_vuelos, respuesta, aux = crear_tabla()
'''Esta función crea las tablas para mostrar los datos'''

#Genera cache para las peticiones a la api
@lru_cache(maxsize=None)


def dic_vuelos_unicos():
    '''Esta función crea un diccionario con los vuelos unicos y les asigna un ID'''
    dic={}
    vuelos=zip(obtener_vuelos_unicos()['origin'],obtener_vuelos_unicos()['destination'])

    #Ciclo para asignar un ID a cada vuelo
    for i,j in zip(obtener_vuelos_unicos()['ID_Vuelo'],vuelos):
        dic[i]=list(j)
    return dic

tabla_vuelos.field_names=['ID','Origen','Destino']
'''Esta función crea los titulos de la tabla de los vuelos unicos'''


unicos=zip(obtener_vuelos_unicos()['ID_Vuelo'],obtener_vuelos_unicos()['origin'],obtener_vuelos_unicos()['destination'])
'''Esta función crea tuplas con los datos de los vuelos unicos'''

#ciclo que agrega los datos de los vuelos unicos a la tabla
for i,j,k in unicos:
    tabla_vuelos.add_row([i,j,k])


while respuesta == "si":

    #Pide el ID del vuelo
    print("\n ********** Estas son los vuelos disponibles ********** \n")
    print(tabla_vuelos)

    print("Ingrese el ID de vuelo")
    orig = input()

    #Ciclo que verifica que el ID sea valido
    while int(orig) not in dic_vuelos_unicos().keys(): 
        print("El ID ingresado no es valido, ingrese el ID de vuelo")
        orig = input()
    
    clima_orig, clima_dest = pedir_peticion(dic_vuelos_unicos()[int(orig)][0], 
                                            dic_vuelos_unicos()[int(orig)][1])
    '''Esta función pide las coordenadas de los estados de origen y destino'''


    tabla_resultados_de_clima=PrettyTable()
    '''variable que crea la tabla para mostrar los datos del clima'''
    
    tabla_resultados_de_clima.field_names = ["Ciudad","Temperatura","Temperatura Maxima","Temperatura Minima","Humedad","Difenecia de Temperatura"]
    '''variable que contiene los titulos de la tabla'''

    Ciudad= dic_vuelos_unicos()[int(orig)][1]
    '''variable que guarda el nombre de la ciudad de origen'''

    Temp=clima_dest["temp"]-273.15
    '''variable que guarda la temperatura de la ciudad de origen'''

    Temperatura_Maxima=(clima_dest["temp_max"]- 273.15)#*5/9
    '''variable que guarda la temperatura maxima de la ciudad de destino'''

    Temperatura_Minima=(clima_dest["temp_min"]- 273.15)#*5/9
    '''variable que guarda la temperatura minima de la ciudad de destino'''

    Humedad=clima_dest['humidity']
    '''variable que guarda la humedad de la ciudad de destino'''

    Difenecia_de_Temperatura=(clima_orig["temp"]-273.15)-Temp
    '''variable que guarda la diferencia de temperatura entre la ciudad de origen y destino'''


    for i in range(aux):
        tabla_resultados_de_clima.add_row(llenar_tabla(i+1,Ciudad,Temp,Temperatura_Maxima,Temperatura_Minima,Humedad,Difenecia_de_Temperatura))
        '''variable que agrega los datos de la tabla principal de los datos de clima'''

    #Muestra la de destino del usuario
    print(f'********** Estos son los resultados de la ciudad de {dic_vuelos_unicos()[int(orig)][1]} la cual es tu ciudad Destino **********')

    #Regresa una tabla con los datos de clima destino
    print(tabla_resultados_de_clima)

    #Pregunta al usuario si seleccionar otra ciudad
    print("Desea realizar otra consulta? si/no")
    respuesta = input()
    '''variable que guarda la respuesta del usuario'''

    #Ciclo que verifica que la respuesta sea valida
    while respuesta != "si" and respuesta != "no":
        print("Por favor ingrese una respuesta valida")
        print("Desea realizar otra consulta? si/no")
        respuesta = input()
    
    #Condicion que termina el programa si el usuario no desea realizar otra consulta
    if respuesta == "no":
            print("\n************** \U0001F600 Gracias por usar Climapp \U0001F600 **************\n")
            break