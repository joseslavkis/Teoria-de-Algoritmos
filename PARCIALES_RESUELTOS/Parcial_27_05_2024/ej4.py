'''
4. Implementar un algoritmo que (por backtracking) dado un grafo no dirigido en el que sus vértices tienen valores positivos,
permita obtener el Dominating Set de suma mínima. Es decir, aquel dominating set en el cual la suma de todos los
valores de los vértices sea mínima (no es importante que la cantidad de vértices del set sea mínima). Por simplicidad,
considerar que el grafo es conexo.
'''


import sys
import os
import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def dominating_set_min_valores(grafo, valores):
    vertices = grafo.obtener_vertices()
    solucion_parcial = set()
    solucion = set(vertices)
    solucion = backtracking(grafo, 0, vertices, solucion_parcial, solucion, valores)
    return solucion

def backtracking(grafo, idx, vertices, solucion_parcial, solucion, valores):
    if len(vertices) == idx:
        if es_dominating_set(grafo, solucion_parcial):
            if len(solucion_parcial) <= len(solucion):
                suma_parcial = sum(valores[v] for v in solucion_parcial)
                suma_optima = sum(valores[v] for v in solucion)
                if suma_parcial < suma_optima:
                    solucion.clear()
                    solucion.update(solucion_parcial)
        return solucion

    solucion_parcial.add(vertices[idx])
    backtracking(grafo, idx + 1, vertices, solucion_parcial, solucion, valores)
    solucion_parcial.remove(vertices[idx])
    backtracking(grafo, idx + 1, vertices, solucion_parcial, solucion, valores)

    return solucion

def es_dominating_set(grafo, sol):
    for v in grafo.obtener_vertices():
        if v in sol:
            continue
        tiene_ady = False
        for w in grafo.adyacentes(v):
            if w in sol:
                tiene_ady = True
                break
        if not tiene_ady:
            return False
    return True

grafo = Grafo(dirigido=False)
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_vertice("E")
grafo.agregar_vertice("F")
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("A", "C", 1)
grafo.agregar_arista("B", "D", 1)
grafo.agregar_arista("D", "E", 1)
grafo.agregar_arista("D", "F", 1)
valores = {"A": 3, "B": 4, "C": 5, "D": 6, "E": 1, "F": 2}
solucion = dominating_set_min_valores(grafo, valores)
print("Dominating Set de suma mínima:", solucion)
