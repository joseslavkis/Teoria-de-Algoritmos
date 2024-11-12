from grafo import Grafo

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

grafo = Grafo(dirigido=False)

grafo.agregar_vertice("H")
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')
grafo.agregar_arista("H", "C", 0)
grafo.agregar_arista('H', 'A', 0)
grafo.agregar_arista('A', 'B', 0)
grafo.agregar_arista('B', 'C', 0)
grafo.agregar_arista('C', 'D', 0)
grafo.agregar_arista('D', 'E', 0)
grafo.agregar_arista('E', 'F', 0)
grafo.agregar_arista('F', 'B', 0)

print(independent_set(grafo))