from Datos import extraer_coordenadas
from Request import peticion_lat_lon

#Pide las coordenadas de los estados de origen y destino
def pedir_peticion(orig, destino):
    '''Esta función pide las coordenadas de los estados de origen y destino'''
    cor_orig = extraer_coordenadas(orig, True)
    cor_dest = extraer_coordenadas(destino, False)
    clima_orig = peticion_lat_lon(cor_orig[0], cor_orig[1])
    clima_dest = peticion_lat_lon(cor_dest[0], cor_dest[1])
    return clima_orig, clima_dest

