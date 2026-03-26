
# Práctica 6: Algoritmo de Dijkstra

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

   $$D[v] = \min(D[v],\; D[u] + M[u][v])$$

4. **Actualización de predecesores:**  
   Si la distancia mejora, se registra el nodo previo:

   $$P[v] = u$$

5. **Repetición:**  
   El proceso continúa hasta que todos los nodos han sido visitados o no hay más nodos alcanzables.  

El resultado final es un conjunto de distancias mínimas y un arreglo de predecesores que permite reconstruir los caminos óptimos.

## Ejercicio 1

En el Ejercicio 1 se proporciona una matriz de adyacencia de tamaño ($4 \times 4$ ), la cual representa un grafo dirigido ponderado. El objetivo es calcular las distancias mínimas desde el nodo inicial ( 0 ) hacia todos los demás nodos.
Tras aplicar el algoritmo de Dijkstra, se obtiene un arreglo de distancias:

$$
D = [0, 9, 8, 6]
$$

Esto indica que:

- La distancia de $( 0 \rightarrow 1 )$ es 9  
- La distancia de $( 0 \rightarrow 3 )$ es 6  
- La distancia de $( 0 \rightarrow 2 )$ es 8  

Es importante notar que la distancia hacia el nodo 2 no es directa, sino que se obtiene mediante un camino intermedio:

$$
0 \rightarrow 3 \rightarrow 2
$$

con un costo total:

$$
6 + 2 = 8
$$

El arreglo de predecesores obtenido es:

$$
P = [-1, 0, 3, 0]
$$

lo cual confirma la estructura del camino mínimo, indicando que el nodo 2 se alcanza desde el nodo 3, y el nodo 3 desde el nodo 0. Así, se valida el correcto funcionamiento del algoritmo, ya que los resultados coinciden con los cálculos teóricos.

## Ejercicio 2 

El Ejercicio 2 consiste en reconstruir el camino mínimo entre dos nodos utilizando el arreglo de predecesores obtenido mediante el algoritmo de Dijkstra.

El procedimiento consiste en partir del nodo destino y seguir los predecesores hasta llegar al origen:


$$
\text{camino} = \{ \text{destination},\; P[\text{destination}],\; P[P[\text{destination}]],\; \dots,\; \text{origin} \}
$$

Posteriormente, el camino se invierte para obtener la secuencia correcta.

Por ejemplo, para encontrar el camino de $( 0 \rightarrow 2 )$:

- $( P[2] = 3 )$  
- $( P[3] = 0 )$ 

Por lo tanto, el camino es:

$$
0 \rightarrow 3 \rightarrow 2
$$

Este resultado coincide con el obtenido en el Ejercicio 1 y confirma que el algoritmo no solo proporciona la distancia mínima, sino también la estructura del recorrido óptimo.

## Conclusión

¿Te gustó la programación dinámica? ¿Sientes que te será útil? ¿Se te hace una buena estrategia para la resolución de problemas?
