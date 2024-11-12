'''
Implementar un algoritmo greedy que permita obtener el Dominating Set mínimo (es decir, que contenga la menor
cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Inlistaar y
justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.
'''
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo
from collections import deque

def bfs_dominating_set(grafo):
    sol_parcial = set()
    dominado = set()
    raiz = next(iter(grafo))
    cola = deque([raiz])
    visitados = set()

    while cola:
        v = cola.popleft()
        if v not in visitados:
            visitados.add(v)
            dominado.add(v)
            for w in grafo.adyacentes(v):
                if w not in dominado:
                    sol_parcial.add(w)
                    dominado.add(w)
                    for x in grafo.adyacentes(w):
                        dominado.add(x)
                if w not in visitados:
                    cola.append(w)

    if raiz not in dominado:
        sol_parcial.add(raiz)

    return sol_parcial

grafo = Grafo(dirigido=False)
grafo.agregar_vertice("H")
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')
grafo.agregar_vertice('G')
grafo.agregar_vertice('I')
grafo.agregar_arista("H", "C", 0)
grafo.agregar_arista('H', 'A', 0)
grafo.agregar_arista('A', 'B', 0)
grafo.agregar_arista('B', 'G', 0)
grafo.agregar_arista('A', 'I', 0)
grafo.agregar_arista('C', 'D', 0)
grafo.agregar_arista('C', 'E', 0)
grafo.agregar_arista('C', 'F', 0)
print(bfs_dominating_set(grafo))
