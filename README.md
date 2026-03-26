
# Práctica 6
Algoritmo de Dijkstra

## Integrantes

- Domíminguez León José Miguel
- Lazcano Flores Valeria
- Sánchez García Rafael


## Uso e instalación

(Si no eliminas esta línea lloro) Aquí escribe qué necesitas que instale para ejecutar tu código, por ejemplo:

- `matplotlib`

(Si no eliminas esta línea lloro) Y dime cómo debería ejecutar tu código y en qué orden. Recuerda que antes de ejecutar tu código leeré tu `README.md`. Por ejemplo la manera en la que propongo que organizes tu código es

- `main.py`: Contiene el código para graficar cada uno de los tres ejercicios
- `data.py`: Tal vez aquí puedes leer el csv para a partir crear una matriz de adyacencia


## Introducción 
El problema de encontrar rutas óptimas en redes es fundamental en diversas áreas como transporte, telecomunicaciones y ciencias de la computación. En particular, los grafos ponderados permiten modelar situaciones donde las conexiones entre nodos tienen un costo asociado, como distancia, tiempo o peso.

Un grafo dirigido ponderado se define como una estructura ( G = (V, E) ), donde ( V ) es el conjunto de vértices y ( E ) el conjunto de aristas dirigidas, cada una con un peso asociado. Este peso representa el costo de trasladarse de un nodo a otro.

El algoritmo de Dijkstra es una herramienta fundamental para resolver el problema del camino más corto desde un nodo origen hacia todos los demás nodos en un grafo con pesos no negativos. Su eficiencia y simplicidad lo convierten en uno de los algoritmos más utilizados en optimización de rutas.
- ¿Cómo funciona el algoritmo?
El algoritmo de Dijkstra es un método iterativo que construye progresivamente las distancias mínimas desde un nodo origen hacia todos los demás nodos del grafo.

Sea una matriz de adyacencia $( M )$, donde:
$$
M[u][v] =
\begin{cases}
w & \text{si existe una arista de } u \rightarrow v \\
\infty & \text{en otro caso}
\end{cases}
$$

Se define un arreglo de distancias $( D )$ tal que:

$$
D[v] = \text{distancia mínima conocida desde el origen hasta } v
$$

Inicialmente:

$$
D[v] =
\begin{cases}
0 & \text{si } v = \text{origen} \\
\infty & \text{en otro caso}
\end{cases}
$$

---

El algoritmo sigue los siguientes pasos:

1. **Inicialización:**  
   Se asigna distancia infinita a todos los nodos excepto al origen.

2. **Selección del nodo permanente:**  
   Se elige el nodo no visitado con menor distancia.

3. **Relajación (reetiquetado):**  
   Para cada vecino \( v \) del nodo seleccionado \( u \), se actualiza:

   $$
   D[v] = \min(D[v],\; D[u] + M[u][v])
   $$

4. **Actualización de predecesores:**  
   Si la distancia mejora, se registra el nodo previo:

   $$
   P[v] = u
   $$

5. **Repetición:**  
   El proceso continúa hasta que todos los nodos han sido visitados o no hay más nodos alcanzables.


   
## Conclusión

¿Te gustó la programación dinámica? ¿Sientes que te será útil? ¿Se te hace una buena estrategia para la resolución de problemas?
