#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import zeros
from math import inf
from data import read_data

def create_adjacency_matrix(tabla)->list[list[float]]:
    """
    Crea una matriz de adyacencia
    """
    max_node = max(tabla['origen'].max(), tabla['destino'].max())
    n = int(max_node)
    
    adj = [[inf]*n for _ in range(n)]
    #Distancia de un nodo a sí mismo es 0
    for i in range(n):
        adj[i][i] = 0
        
    for _, row in tabla.iterrows():
        u = int(row['origen']) - 1
        v = int(row['destino']) - 1
        w = float(row['peso'])
        adj[u][v] = w
        
    return adj

def dijkstra(M: list[list[float]], origin: int) -> list[list[float]]:
    """
    Aplica el algoritmo de Dijkstra.

    Parámetros
    ----------
    M : matriz de adyacencia (lista de listas)
        M[u][v] es el peso de la arista de u a v (inf si no existe)
    origin : int
        nodo inicial (índice base 0)

    Regresa
    -------
    D : lista
        distancias mínimas desde el nodo origen a cada nodo
    P : lista
        predecesor de cada nodo en el camino mínimo
    """

    n = len(M)

    # -----------------------------
    # Paso 1: Inicializar distancias
    # -----------------------------
    D = [inf] * n      # distancias
    P = [-1] * n       # predecesores
    visited = [False] * n  # nodos permanentes

    D[origin] = 0  # distancia del origen a sí mismo es 0

    # -----------------------------
    # Repetir n veces
    # -----------------------------
    for _ in range(n):

        # -----------------------------
        # Paso 2: elegir nodo permanente
        # -----------------------------
        # nodo no visitado con menor distancia
        u = -1
        min_dist = inf

        for i in range(n):
            if not visited[i] and D[i] < min_dist:
                min_dist = D[i]
                u = i

        # Si no encontramos nodo válido, terminamos
        if u == -1:
            break

        visited[u] = True  # marcar como permanente

        # -----------------------------
        # Paso 3: vecinos disponibles
        # -----------------------------
        for v in range(n):

            # solo si hay arista y no está visitado
            if M[u][v] != inf and not visited[v]:

                # -----------------------------
                # Paso 4: Reetiquetado
                # -----------------------------
                if D[u] + M[u][v] < D[v]:
                    D[v] = D[u] + M[u][v]
                    P[v] = u

        # -----------------------------
        # Paso 5: se repite el proceso
        # -----------------------------

    return D, P



def minimal_distance(M: list[list[float]], origin:int, destination:int)-> float:
    """
    Devuelve la distancia mínima entre origin y destination
    usando el algoritmo de Dijkstra.
    """

    # Ejecutar Dijkstra desde el nodo origen
    D, _ = dijkstra(M, origin)

    # Regresar la distancia al destino
    return D[destination]

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

    # 🔥 Convertir 0 → inf (excepto diagonal)
    for i in range(n):
        for j in range(n):
            if i != j and MD[i][j] == 0:
                MD[i][j] = inf

    #Convertir M a una lista normal 
    MD = MD.tolist()
    # Aplicar Dijkstra desde nodo 0
    D, P = dijkstra(MD, 0)

    return D, P
    

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
     # 🔹 Probar Ejercicio 1
    D, P = ejercicio_1()
    
    print("=== Ejercicio 1 ===")
    print("Distancias:", D)
    print("Predecesores:", P)

if __name__ == "__main__":
    main()
   
    