'''
Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi−1)). Cada vertice tiene un valor (positivo).
Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima
dentro de un grafo de dichas características. Dar la ecuación de recurrencia correspondiente al problema. Indicar
y justificar la complejidad del algoritmo implementado. Indicar y justificar la complejidad espacial del algoritmo
implementado, y si hay una optimización que permita consumir menos espacio.
'''

# Es "similar" a juan el vago pero no demasiado

'''
ec. de recurrencia -> opt[i] = min(opt[i-1] + valores[i], opt[i-2] + valores[i-1])
Casos base:
1) opt[0] = 0
2) opt[1] = vertices[0][1]
3) opt[2] = min(vertices[0][1], vertices[1][1])
'''

# Asumo que los vertices son de la forma (v, valor)

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def dominating_set_min_valores(grafo, valores):
    vertices = grafo.obtener_vertices()
    n = len(vertices)
    
    if n == 0:
        return 0, []
    if n == 1:
        return valores[vertices[0]], [vertices[0]]
    
    opt = [0] * (n + 1)
    decision = [-1] * (n + 1)

    opt[1] = valores[vertices[0]]
    decision[1] = 1
    if n > 1:
        if valores[vertices[0]] < valores[vertices[1]]:
            opt[2] = valores[vertices[0]]
            decision[2] = 1
        else:
            opt[2] = valores[vertices[1]]
            decision[2] = 2
    
    for i in range(3, n + 1):
        if opt[i - 2] + valores[vertices[i - 1]] < opt[i - 3] + valores[vertices[i - 2]]:
            opt[i] = opt[i - 2] + valores[vertices[i - 1]]
            decision[i] = 2
        else:
            opt[i] = opt[i - 3] + valores[vertices[i - 2]]
            decision[i] = 3
    
    return opt[n], decision

def reconstruir_dominating_set(vertices, decision):
    n = len(vertices)
    dominating_set = []
    i = n

    while i > 0:
        if decision[i] == 1:
            dominating_set.append(vertices[0])
            break
        elif decision[i] == 2:
            dominating_set.append(vertices[i - 1])
            i -= 2
        elif decision[i] == 3:
            dominating_set.append(vertices[i - 2])
            i -= 3
    return dominating_set.reverse()


grafo = Grafo(dirigido=True)
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_vertice("E")
grafo.agregar_vertice("F")

grafo.agregar_arista("A", "B", 0)
grafo.agregar_arista("B", "C", 0)
grafo.agregar_arista("C", "D", 0)
grafo.agregar_arista("D", "E", 0)
grafo.agregar_arista("E", "F", 0)

valores = {
    "A": 1,
    "B": 2,
    "C": 4,
    "D": 1,
    "E": 5,
    "F": 3
}


suma_minima, decision = dominating_set_min_valores(grafo, valores)
vertices = grafo.obtener_vertices()

conjunto_dominante = reconstruir_dominating_set(vertices, decision)

print(f"Suma mínima: {suma_minima}")
print(f"Conjunto dominante: {conjunto_dominante}")
