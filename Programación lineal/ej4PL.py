"""Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT)."""


import pulp
from grafo import Grafo

def dominating_set(grafo):
    problem = pulp.LpProblem("Dominating_Set_Problem", pulp.LpMinimize)

    vertices = grafo.obtener_vertices()
    x = pulp.LpVariable.dicts("x", vertices, cat="Binary")

    problem += pulp.lpSum(x[i] for i in vertices), "Minimize_Total_Vertices"
    # si el vertice v_j no esta en el dominating set, entonces al menos uno de sus vecinos debe estarlo
    for j in vertices:
        neighbors = grafo.adyacentes(j)
        problem += x[j] + pulp.lpSum(x[i] for i in neighbors) >= 1, f"Dominating_Constraint_{j}"

    problem.solve()

    dominating_vertices = [i for i in vertices if pulp.value(x[i]) == 1]

    return dominating_vertices, pulp.value(problem.objective)

if __name__ == "__main__":
    grafo = Grafo(dirigido=False)
    grafo.agregar_vertice(0)
    grafo.agregar_vertice(1)
    grafo.agregar_vertice(2)
    grafo.agregar_vertice(3)
    grafo.agregar_vertice(4)
    grafo.agregar_arista(0, 1)
    grafo.agregar_arista(0, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(3, 4)

    conjunto_dominante_resultado, tamano_minimo = dominating_set(grafo)

    print("Conjunto dominante mínimo:", conjunto_dominante_resultado)
    print("Tamaño del conjunto dominante:", tamano_minimo)
