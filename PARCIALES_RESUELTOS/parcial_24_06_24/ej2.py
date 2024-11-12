# Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
# un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
# del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
# es completo. Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
# y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.



#La estrategia greedy sería, dado un cierto vértice w, revisar todos los adyacentes y tomar la arista de menor peso que tenga un vértice no visitado.
#Como el grafo es completo, da igual en el vértice que estemos, siempre vamos a poder llegar a cualquier otro vértice(si es el final del recorrido
# podremos llegar al vertice inicial de vuelta).
from collections import deque
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def TSP(grafo, vertice):
    v = vertice
    visitados = set(vertice)
    camino = [vertice]
    costo = 0
    while len(camino) < len(grafo): 
        min_peso = float('inf')
        siguiente_vertice = None
        for w in grafo.adyacentes(v):
            if w not in visitados and grafo.peso_arista(v, w) < min_peso:
                siguiente_vertice = w
                min_peso = grafo.peso_arista(v, w)
        if siguiente_vertice:
            visitados.add(siguiente_vertice)
            costo += min_peso
            camino.append(siguiente_vertice)
            v = siguiente_vertice
    camino.append(vertice)
    costo += grafo.peso_arista(v, vertice)
    return costo, camino

#obviamente no es óptimo, primero porque TSP es NP-Completo, no seas boludo. Además imagina que estas recorriendo un grafo
# en el que tenes como adyacente una arista de peso 1(supongamos que sería el minimo entre los adyacentes del v_actual) y depues vas a 
#a ese adyacente y resulta que todas sus aristas son de peso 10000. Te hubiera convenido irte al otro adyacente(ponele que de peso 2)
# y que tenia sus adyacentes de peso -100000000(todo re exagerado pero es para que se entienda)
#Conclusión, no es óptimo. Si fuese óptimo P sería igual NP...