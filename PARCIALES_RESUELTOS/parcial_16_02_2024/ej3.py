# Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
# del grafo, si es que existe.


#Obviamente esto es por backtracking. La complejidad es O(2^(V+E)) donde V es la cantidad de vértices y E la cantidad de aristas.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def ciclo_k(grafo, k):
    for v in grafo:
        resultado = []
        if bt(grafo, k, resultado, set(), v, v):
            return resultado
    return None

def bt(grafo, k, posible_solucion, visitados, v_inicio, v):
    posible_solucion.append(v)
    visitados.add(v)

    if len(posible_solucion) == k:
        if v_inicio in grafo.adyacentes(v):
            posible_solucion.append(v_inicio)
            return True
        else:
            posible_solucion.pop()
            visitados.remove(v)
            return False

    for w in grafo.adyacentes(v):
        if w not in visitados:
            if bt(grafo, k, posible_solucion, visitados, v_inicio, w):
                return True

    posible_solucion.pop()
    visitados.remove(v)
    return False


grafo = Grafo()
grafo.agregar_arista(1, 2, 0)
grafo.agregar_arista(2, 3, 0)
grafo.agregar_arista(3, 4, 0)
grafo.agregar_arista(4, 1, 0)
grafo.agregar_arista(1, 3, 0)

k = 4
ciclo = ciclo_k(grafo, k)
if ciclo:
    print(f"Ciclo de tamaño {k} encontrado:", ciclo)
else:
    print(f"No existe un ciclo de tamaño {k} en el grafo.")






