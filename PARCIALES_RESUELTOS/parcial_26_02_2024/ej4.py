# Implementar un algoritmo que resuelva el problema de 3-SAT: determinar si, dado un grupo de cláusulas de 3 términos
# (pudiendo ser complementos de variables), existe alguna asignación de valores de las variables tal que la disyunción de
# todas las cláusulas (que son todas conjunciones) evalúan a true.

#Recordar que redujimos este problema a IS...(ver resolución del ejercicio 4 de reducciones)
#Buscaremos un IS de tamaño k, siendo k = cant(vars)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo


def tres_sat(clausulas):
    grafo = Grafo(False)
    vars = set()
    for clausula in clausulas:
        for var in clausula:
            vars.add(var)
            grafo.agregar_vertice(var)
    for clausula in clausulas:
        for i in range(3):
            for j in range(i + 1, 3):
                grafo.agregar_arista(clausula[i], clausula[j])
    for var in vars:
        if not(var) in vars and not grafo.estan_unidos(var, not(var)):
            grafo.agregar_arista(var, not(var))
    IS = independent_set(grafo)
    return [v for v in IS]

def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    max_conjunto = []
    independent_set_rec(grafo, vertices, 0, [], max_conjunto)
    return max_conjunto


def independent_set_rec(grafo, vertices, v, conjunto, max_conjunto):
    if v == len(grafo):
        if es_compatible(grafo, conjunto) and len(conjunto) > len(max_conjunto):
            max_conjunto[:] = conjunto[:]
        return
    
    conjunto.append(vertices[v])
    independent_set_rec(grafo, vertices, v + 1, conjunto, max_conjunto)
    conjunto.pop()
    independent_set_rec(grafo, vertices, v + 1, conjunto, max_conjunto)

def es_compatible(grafo, conjunto):
    for v in conjunto:
        for w in conjunto:
            if v == w:
                continue
            elif grafo.estan_unidos(v,w):
                return False
    return True







