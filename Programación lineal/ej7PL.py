import pulp

def conjunto_independiente_maximo(grafo):
    problema = pulp.LpProblem("Conjunto_Independiente_Maximo", pulp.LpMaximize)

    vertices = grafo.obtener_vertices()
    x = pulp.LpVariable.dicts("x", vertices, 0, 1, pulp.LpBinary)

    problema += pulp.lpSum(x[v] for v in vertices), "Maximizar cantidad de vértices en el conjunto independiente"

    for v in vertices:
        for w in grafo.adyacentes(v):
            if grafo.estan_unidos(v, w):
                problema += (x[v] + x[w] <= 1), f"Restriccion_{v}_{w}"

    problema.solve()

    if problema.status == pulp.LpStatusOptimal:
        conjunto_independiente = [v for v in vertices if pulp.value(x[v]) == 1]
        return conjunto_independiente
    else:
        return None


from grafo import Grafo

grafo = Grafo()
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')

grafo.agregar_arista('A', 'B')
grafo.agregar_arista('B', 'C')
grafo.agregar_arista('C', 'D')
grafo.agregar_arista('D', 'E')
grafo.agregar_arista('E', 'A')

conjunto_maximo = conjunto_independiente_maximo(grafo)

if conjunto_maximo:
    print("Conjunto Independiente Máximo encontrado:")
    print(conjunto_maximo)
else:
    print("No se encontró solución óptima.")
