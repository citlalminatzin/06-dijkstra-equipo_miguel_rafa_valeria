#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros
from math import inf
from data import read_data
from data import df


def create_adjacency_matrix(tabla)->list[list[float]]:
    """
    Crea una matriz de adyacencia
    """
    max_node = max(tabla['origen'].max(), tabla['destino'].max())
    n = int(max_node)
    
    adj = [[inf]*n for _ in range(n)]
    
    for i in range(n):
        adj[i][i] = 0
        
    for _, row in tabla.iterrows():
        u = int(row['origen']) - 1
        v = int(row['destino']) - 1
        w = float(row['peso'])
        adj[u][v] = w
        adj[v][u] = w
        
    return adj


def dijkstra(M: list[list[float]], origin: int) -> list[list[float]]:
    """
    M : Matriz de pesos de una gráfica
    origin: índice del nodo inicial

    returns
    lista con las distancia de las rutas y el origen de la arista
    con la que terminó la ruta
    """
    # ---
    # Paso 1: Inicializa las distancias
    # ---

    # ---
    # Paso 2: Marca el nodo permanente
    # ---

    # ---
    # Paso 3: Identifica los nodos vecinos disponibles
    # ---

    # ---
    # Paso 4: Reetiquetado
    # ---

    # ---
    # Paso 5: Actualizar el nodo permanente
    # ---
    ...

def minimal_distance(M: list[list[float]], origin:int, destination:int)-> float:
    """Devuelve la distancia mínima entre el origin y destination"""
    ...

def ejercicio_1():
    """
    Regresa las distancias mínimas del
    primer vértice a todos los demás
    """
    n = 4
    MD = zeros((n, n))
    MD[0,1] = 9
    MD[3,2] = 2
    MD[0,3] = 6
    MD[1,3] = 1
    MD[2,1] = 3
    
    return dijkstra(MD, 0)

def ejercicio_3a():
    """
    Regresa las distancias mínimas de todos
    los vértices entre sí
    """
    n = 8
    M1 = zeros((n,n))

    M1[0,1] = M1[1,0] = 3
    M1[1,2] = M1[2,1] = 1
    M1[0,3] = M1[3,0] = 2
    M1[3,2] = M1[2,3] = 3
    M1[1,4] = M1[4,1] = 4
    M1[2,5] = M1[5,2] = 2
    M1[2,6] = M1[6,2] = 2
    M1[3,6] = M1[6,3] = 4
    M1[4,7] = M1[7,4] = 6
    M1[5,7] = M1[7,5] = 4
    M1[5,6] = M1[6,5] = 3
    M1[6,7] = M1[7,6] = 5
    
    distancias = [dijkstra(M1, i) for i in range(n)]
    return distancias

def ejercicio_3b():
    n = 4
    M2 = zeros((n,n))

    M2[0,1] = 9
    M2[3,2] = 2
    M2[0,3] = 6
    M2[1,3] = 1
    M2[2,1] = 3

    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias
    
def ejercicio_3c():
    n = 4
    M3 = zeros((n,n))

    M3[0,1] = 4
    M3[0,2] = 8
    M3[0,3] = 16
    M3[1,2] = 5
    M3[1,3] = 11
    M3[2,3] = 6

    distancias = [dijkstra(M3, i) for i in range(n)]
    return distancias

def ejercicio_4():
    ...

def main():
    ...

if __name__ == "__main__":
    o, d, w, df = read_data("data/distances.csv")
    print("\nTabla de datos:\n")
    print(df)
    matriz_adyacente = create_adjacency_matrix(df)
    print(matriz_adyacente)