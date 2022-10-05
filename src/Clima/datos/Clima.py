from Datos import coordenadas
from Request import peticion

#Pide las coordenadas de los estados de origen y destino
def Peticion(orig, destino):
    cor_orig = coordenadas(orig, True)
    cor_dest = coordenadas(destino, False)
    clima_orig = peticion(cor_orig[0], cor_orig[1])
    clima_dest = peticion(cor_dest[0], cor_dest[1])
    return clima_orig, clima_dest

