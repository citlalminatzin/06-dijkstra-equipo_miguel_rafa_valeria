#!/usr/bin/env python
import numpy as np
import pandas as pd

def read_data(path="data/distances.csv"):
    """
    Lee un archivo CSV con aristas de un grafo.

    Parámetro
    ----------
    path : str
        Ruta al archivo csv.

    Regresa
    -------
    origin : numpy.array
        Nodo origen.
    destination : numpy.array
        Nodo destino.
    weight : numpy.array
        Peso de la arista.
    df : pandas.DataFrame
        Tabla con los datos.
    """
    data = np.genfromtxt(path, delimiter=",", skip_header=1)
    o = data[:, 0]
    d = data[:, 1]
    w = data[:, 2]
    df = pd.DataFrame({'origen': o, 'destino': d, 'peso': w})

    return o, d, w, df

#Probabmos que se impriman los datos al ejecutar el script directamente
if __name__ == "__main__":
    o, d, w, df = read_data("data/distances.csv")
    print("\nTabla de datos:\n")
    print(df)