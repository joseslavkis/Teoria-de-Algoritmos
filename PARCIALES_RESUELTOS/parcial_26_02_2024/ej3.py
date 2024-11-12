# El K-core de un grafo es el subgrafo del mismo en el cuál todos los vértices tienen grados mayor o igual a K. Implementar
# un algoritmo greedy que dado un grafo y un valor K devuelva el K-core del grafo (es decir, el subgrafo en el cuál todos
# los vértices involucrados tienen grado mayor o igual a K, en dicho subgrafo). Indicar y justificar la complejidad del
# algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo
from collections import deque
#La idea es hacer una copia del grafo e ir eliminando los de menos de k adyacentes

def k_core(grafo, k):
    copia = grafo.copiar_grafo()
    grados = grafo.obtener_grados()
    cola = deque()  
    for v in grafo:
        if grados[v] < k:
            cola.append(v)
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            grados[w] -= 1
            if grados[w] < k:
                cola.append(w)
        copia.elimiar_vertice(v)
    return copia

#La complejidad es O(V + E) ya que recorremos todos los vertices y aristas del grafo
#Es greedy porque vamos siguiendo una regla en cada paso el cual es el optimo local.
#Por cada iteracion eliminamos un vértice de grado menor a k y sus conexiones. Esto nos dará como resultado un
#subgrafo donde todos los vértices tienen grado mayor o igual a k(si es que existe). 
#Ya que este algoritmo asegura que al sacar un elemento de un grafo, el gr[ady] se reduce en uno. 
#Asi no da como resultado un subgrafo en el que no todos los vértices tienen grado mayor o igual a k.







