import pandas as pd

#Esta función lee la base de datos y la convierte en un dataframe
def Base_de_datos():
    df = pd.read_csv('/Users/brendaayala/Brenda_Sem3/Proyecto01/data/dataset1.csv')
    return df.drop_duplicates()

#Esta función filtra los vuelos unicos
def vuelos_unicos():
    df = Base_de_datos()
    df = df[['origin', 'destination']].drop_duplicates()
    df['ID_Vuelo'] = [i for i in range(1, len(df) + 1)]
    return df

#Esta función extrae las coordenadas de los estados de origen y destino
def coordenadas(edo, orig = True):
    df = Base_de_datos()
    if orig:
        return df[df['origin'] == edo][['origin_latitude', 'origin_longitude']].values[0]
    else:   
        return df[df['destination'] == edo][['destination_latitude', 'destination_longitude']].values[0]