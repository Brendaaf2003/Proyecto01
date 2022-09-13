import pandas as pd

def Base_de_datos():
    df = pd.read_csv('/Users/Brenda_Sem3/Proyecto01/data/dataset2.csv')
    return df.drop_duplicates()

def estado_origen():
    df = Base_de_datos()
    return df['origin'].unique()

def estado_destino():
    df = Base_de_datos()
    return df['destination'].unique()

def coordenadas(edo, orig = True):
    df = Base_de_datos()
    if orig:
        return df[df['origin'] == edo][['origin_latitude', 'origin_longitude']].values[0]
    else:   
        return df[df['destination'] == edo][['destination_latitude', 'destination_longitude']].values[0]