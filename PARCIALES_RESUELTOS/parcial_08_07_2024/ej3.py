# Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
# cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
# justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
# algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.


from collections import deque

def max_independent_set(raiz):
    incluido, excluido = dfs(raiz)
    return max(incluido, excluido)

def dfs(nodo):
    if not nodo:
        return (0, 0)

    nodo_incluido = 1
    nodo_excluido = 0

    for hijo in nodo.hijos:
        incluido, excluido = dfs(hijo)
        nodo_incluido += excluido #si incluimos este nodo, no incluimos hijos
        nodo_excluido += max(incluido, excluido)  #tomamos el mejor de incluir o no incluir el hijo
    return (nodo_incluido, nodo_excluido)

