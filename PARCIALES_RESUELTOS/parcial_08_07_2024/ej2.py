# La Cruz Roja cuenta con n ambulancias, de las cuáles conoce la ubicación de cada una. En un momento dado llegan
# p pedidos de ambulancias para socorrer personas. Debido a diferentes reglas que tienen, una ambulancia no debe
# trasladarse más de k kilómetros. Se quiere saber si se puede hacer una asignación de ambulancias a los pedidos,
# asignando cada una a como máximo 1 pedido. Implementar un algoritmo que resuelva este problema, utilizando redes
# de flujo. Indicar y justificar la complejidad del algoritmo implementado para el problema planteado.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo


#doy por hecho que recibo una funcion que me dic la distancia del pedido p y la ambulancia a
#n = cant de ambulancias, p = cant de pedidos, k = distancia maxima
def ambulancias(n, p, k, func):
    grafo = Grafo(dirigido=True)
    grafo.agregar_vertice("s")
    grafo.agregar_vertice("t")
    for i in range(n):
        grafo.agregar_vertice(f"A{i}")
        grafo.agregar_arista("s", f"A{i}", 1)
    for i in range(p):
        grafo.agregar_vertice(f"P{i}")
        grafo.agregar_arista(f"P{i}", "t", 1)
    
    for i in range(n):
        for j in range(p):
            if func(f"A{i}", f"P{j}") <= k:
                grafo.agregar_arista(f"A{i}", f"P{j}", 1)
    flujo_maximo, _, _ = grafo.ford_fulkerson("s", "t")
    return flujo_maximo == p # devolver si se puede hacer la asignacion de pedidos dadas las ambulancias
