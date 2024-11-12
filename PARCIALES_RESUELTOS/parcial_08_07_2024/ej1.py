# Definimos a un grafo ordenado como un grafo dirigido con vértices v1, · · · , vn en el que todos los vértices, salvo vn
# tienen al menos una arista que sale del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es
# decir, las aristas tienen la forma (vi, vj) con i < j). Implementar un algoritmo de programación dinámica que dado
# un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) determine cuál es la longitud del camino más
# largo. Dar la ecuación de recurrencia correspondiente. Dar también el algoritmo de recontrucción de la solución. Indicar
# y justificar la complejidad del algoritmo implementado. Se pone a continuación un ejemplo de un grafo ordenado.
#
#                                       { 1 si gr_ent(v) = 0   
#ecuación de recurrencia -> opt(v_n) =  {
#                                       { max(opt[v_i-1] + 1, opt[v_i]) si gr_ent(v) > 0, siendo v_i-1 predecesor de v_i 
#                                       {   



import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def camino_mas_largo(grafo):
    if not grafo:
        return 0, []

    opt = {v: 1 for v in grafo}  # uso un dic porque no puedo usar una lista para representar vértices...
    predecesor = {v: None for v in grafo}  #Para reconstrucción

    for v in grafo:
        for w in grafo.adyacentes(v):
            if opt[v] + 1 > opt[w]:
                opt[w] = opt[v] + 1
                predecesor[w] = v
    largo = max(opt.values())
    last = max(opt, key=opt.get)
    return largo, reconstruccion(predecesor, last)

def reconstruccion(predecesor, last_vertex):
    camino = []
    while last_vertex:
        camino.append(last_vertex)
        last_vertex = predecesor[last_vertex]
    return camino[::-1]


grafo = Grafo(dirigido=True)
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")
grafo.agregar_vertice("E")

grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("A", "D", 1)
grafo.agregar_arista("B", "D", 1)
grafo.agregar_arista("B", "E", 1)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("D", "E", 1)

longitud, camino = camino_mas_largo(grafo)
print(f"Longitud del camino más largo: {longitud}")
print(f"Camino más largo: {camino}")