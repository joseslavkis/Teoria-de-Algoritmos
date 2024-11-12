# Implementar un algoritmo Greedy que busque aproximar la solución óptima al problema del mínimo Vertex Cover:
# dado un grafo, obtener el mínimo Vertex Cover del mismo. Indicar la complejidad del algoritmo implementado, dar un
# contraejemplo para el algoritmo implementado y justificar por qué el algoritmo implementado es un algoritmo greedy.



import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo


#cabe aclarar que CUALQUIER SOLUCIÓN QUE HAGAMOS DE VC GREEDY NO SERÁ ÓPTIMA, ya que el problema de VC es NP-Completo. Estaríamos resolviendo
# un problema NP-Completo en forma polinomial, lo cual demostraría que P=NP.

def vertex_cover_greedy(grafo):
    vertex_cover = set()
    aristas = set() # de la forma (v, w)
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            aristas.add((v, w))
            aristas.add((w, v))
    #Ahora la estrategia greedy será ir recorriendo todas las aristas y agregar vértices a los extremos de las aristas si estas no tienen
    # ninguno de sus extremos en el vertex cover. Además entre los 2 elegiremos al que tenga mayor grado
    #Ejemplo, si tenes la arista (A, B) y A tiene grado 1 y B grado 1000. Obviamente elegiremos a B para agregarlo al VC.
    visitados = set()
    for v, w in aristas:
        if (v, w) in visitados or (w, v) in visitados:
            continue
        visitados.add((v, w))
        if v not in vertex_cover and w not in vertex_cover:
            if grafo.grado(v) > grafo.grado(w):
                vertex_cover.add(v)
            else:
                vertex_cover.add(w)
    return vertex_cover

#el contraejemplo te lo dejo a vos pibe, good luck.
