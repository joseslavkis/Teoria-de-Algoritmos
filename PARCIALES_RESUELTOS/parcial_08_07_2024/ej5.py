#Implementar un algoritmo que dado un grafo, obtenga el clique de mayor tamaño del mismo.

#esto es claramente por backtracking

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def max_clique(grafo):
    resultado = []
    vertices = grafo.obtener_vertices()
    bt(grafo, vertices, 0, resultado, [])
    return resultado

def bt(grafo, vertices, idx, resultado, parcial):
    if len(grafo) == idx:
        if len(resultado) < len(parcial) and es_valido(grafo, parcial):
            resultado.clear()
            resultado.extend(parcial)
        return
    v = vertices[idx]
    parcial.add(v)
    bt(grafo, vertices, idx+1, resultado, parcial)
    parcial.pop()
    bt(grafo, vertices, idx+1, resultado, parcial)

def es_valido(grafo, solucion):
    for i in range(len(solucion)):
        for j in range(i + 1, len(solucion)):
            if not grafo.estan_unidos(solucion[i], solucion[j]):
                return False
    return True

