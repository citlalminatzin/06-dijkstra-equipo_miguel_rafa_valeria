#!/usr/bin/env python

from numpy import zeros
from math import inf
from data import read_data
from models import create_adjacency_matrix, dijkstra, reconstruir_camino, graf, minimal_distance



def ejercicio_1():
    """
    Regresa las distancias mínimas del
    primer vértice a todos los demás
    """
    n = 4
    MD = zeros((n, n))
    MD[0, 1] = 9
    MD[3, 2] = 2
    MD[0, 3] = 6
    MD[1, 3] = 1
    MD[2, 1] = 3

    # 🔥 Convertir 0 → inf (excepto diagonal)
    for i in range(n):
        for j in range(n):
            if i != j and MD[i][j] == 0:
                MD[i][j] = inf

    # Convertir M a una lista normal
    MD = MD.tolist()
    # Aplicar Dijkstra desde nodo 0
    D, P = dijkstra(MD, 0)

    return D, P


def ejercicio_2(M, origin, destination):
    """
    Devuelve el camino mínimo entre origin y destination
    """

    D, P = dijkstra(M, origin)

    camino = reconstruir_camino(P, origin, destination)

    return camino


def ejercicio_3a():
    """
    Regresa las distancias mínimas de todos
    los vértices entre sí
    """
    n = 8
    M1 = zeros((n, n))

    M1[0, 1] = M1[1, 0] = 3
    M1[1, 2] = M1[2, 1] = 1
    M1[0, 3] = M1[3, 0] = 2
    M1[3, 2] = M1[2, 3] = 3
    M1[1, 4] = M1[4, 1] = 4
    M1[2, 5] = M1[5, 2] = 2
    M1[2, 6] = M1[6, 2] = 2
    M1[3, 6] = M1[6, 3] = 4
    M1[4, 7] = M1[7, 4] = 6
    M1[5, 7] = M1[7, 5] = 4
    M1[5, 6] = M1[6, 5] = 3
    M1[6, 7] = M1[7, 6] = 5

    # convertir 0 → inf
    for i in range(n):
        for j in range(n):
            if i != j and M1[i][j] == 0:
                M1[i][j] = inf

    M1 = M1.tolist()
    distancias = [dijkstra(M1, i) for i in range(n)]

    graf(M1, "ejercicio3a", False)
    return distancias


def ejercicio_3b():
    n = 4
    M2 = zeros((n, n))

    M2[0, 1] = 9
    M2[3, 2] = 2
    M2[0, 3] = 6
    M2[1, 3] = 1
    M2[2, 1] = 3

    # convertir 0 → inf
    for i in range(n):
        for j in range(n):
            if i != j and M2[i][j] == 0:
                M2[i][j] = inf

    M2 = M2.tolist()
    distancias = [dijkstra(M2, i) for i in range(n)]

    graf(M2, "ejercicio3b")

    distancias = [dijkstra(M2, i) for i in range(n)]
    return distancias


def ejercicio_3c():
    n = 4
    M3 = zeros((n, n))

    M3[0, 1] = 4
    M3[0, 2] = 8
    M3[0, 3] = 16
    M3[1, 2] = 5
    M3[1, 3] = 11
    M3[2, 3] = 6

    # convertir 0 → inf
    for i in range(n):
        for j in range(n):
            if i != j and M3[i][j] == 0:
                M3[i][j] = inf

    M3 = M3.tolist()
    distancias = [dijkstra(M3, i) for i in range(n)]

    graf(M3, "ejercicio3c")

    distancias = [dijkstra(M3, i) for i in range(n)]
    return distancias


def ejercicio_4():
    grafica = read_data()
    matriz = create_adjacency_matrix(grafica[3])

    d, p = dijkstra(matriz, 0)
    dist_min = d[11]
    camino = reconstruir_camino(p, 0, 11)

    graf(matriz, "Ejercicio4", True, True)

    return [dist_min, camino]


def main():
    # Probar Ejercicio 1
    D, P = ejercicio_1()

    print("=== Ejercicio 1 ===")
    print("Distancias:", D)
    print("Predecesores:", P)
    print()

    # Probar Ejercicio 2
    camino = reconstruir_camino(P, 0, 2)
    print("=== Ejercicio 2 ===")
    print("Camino de 0 a 2:", camino)
    print()

    # Ejercicio 3a
    print("=== Ejercicio 3a ===")
    res_3a = ejercicio_3a()
    for i, (D, _) in enumerate(res_3a):
        print(f"Desde nodo {i}: {D}")
    print()

    # Ejercicio 3b
    print("=== Ejercicio 3b ===")
    res_3b = ejercicio_3b()
    for i, (D, _) in enumerate(res_3b):
        print(f"Desde nodo {i}: {D}")
    print()

    # Ejercicio 3c
    print("=== Ejercicio 3c ===")
    res_3c = ejercicio_3c()
    for i, (D, _) in enumerate(res_3c):
        print(f"Desde nodo {i}: {D}")
    print()

    # Ejericio 4
    dist_min, camino = ejercicio_4()
    print("=== Ejercicio 4 ===")
    print("Distancia minima de 0 a 11:", dist_min)
    print("Camino de minima distancia:", camino)


if __name__ == "__main__":
    main()
