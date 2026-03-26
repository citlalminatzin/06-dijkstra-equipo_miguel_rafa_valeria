#!/usr/bin/env python

from math import inf
import networkx as nx
import matplotlib.pyplot as plt

def create_adjacency_matrix(tabla) -> list[list[float]]:
    """
    Crea una matriz de adyacencia
    """
    max_node = max(tabla["origen"].max(), tabla["destino"].max())
    n = int(max_node)

    adj = [[inf] * n for _ in range(n)]
    # Distancia de un nodo a sí mismo es 0
    for i in range(n):
        adj[i][i] = 0

    for _, row in tabla.iterrows():
        u = int(row["origen"]) - 1
        v = int(row["destino"]) - 1
        w = float(row["peso"])
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
    D = [inf] * n  # distancias
    P = [-1] * n  # predecesores
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


def minimal_distance(M: list[list[float]], origin: int, destination: int) -> float:
    """
    Devuelve la distancia mínima entre origin y destination
    usando el algoritmo de Dijkstra.
    """

    # Ejecutar Dijkstra desde el nodo origen
    D, _ = dijkstra(M, origin)

    # Regresar la distancia al destino
    return D[destination]



def reconstruir_camino(
    P: list[float], origin: float, destination: float
) -> list[float]:
    """
    Reconstruye el camino mínimo desde origin hasta destination
    usando la lista de predecesores P.
    """

    camino = []
    actual = destination

    # recorrer hacia atrás
    while actual != -1:
        camino.append(actual)
        actual = P[actual]

    # invertir para que vaya de origen → destino
    camino.reverse()

    # verificar que el camino inicia en el origen
    if camino[0] == origin:
        return camino
    else:
        return []  # no hay camino
    

def graf(matriz: list[list[float]], name: str, dir=True, bfs=False):
    n = len(matriz)
    if dir:
        g = nx.DiGraph()
    else:
        g = nx.Graph()

    for i in range(n):
        for j in range(n):
            if matriz[i][j] != 0 and matriz[i][j] != inf:
                g.add_edge(i, j, weight=matriz[i][j])

    large = [(u, v) for (u, v, d) in g.edges(data=True)]

    if bfs:
        pos = nx.bfs_layout(g, 0)
    else:
        pos = nx.spring_layout(g, seed=1270)

    nx.draw_networkx_nodes(g, pos, node_size=200)
    nx.draw_networkx_edges(g, pos, edgelist=large, width=3)

    nx.draw_networkx_labels(g, pos, font_size=8)
    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels)

    ax = plt.gca()
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("media/" + name + ".png")
    ax.clear()

    return None   


def main():
    ... # Puedes eliminar esta línea

if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()

