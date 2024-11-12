from grafo import Grafo

def vertex_cover_min(grafo):
    if not grafo.obtener_vertices():
        return []
    vertices = grafo.obtener_vertices()
    vertex_cover = [vertices[:]]
    vertex_cover_rec(grafo, vertices, 0, [], vertex_cover)
    return vertex_cover[0]

def vertex_cover_rec(grafo, vertices, v, conjunto, min_conjunto):
    if v == len(vertices):
        if es_compatible(grafo, conjunto) and len(conjunto) < len(min_conjunto[0]):
            min_conjunto[0] = conjunto[:]
        return

    conjunto.append(vertices[v])
    vertex_cover_rec(grafo, vertices, v+1, conjunto, min_conjunto)

    conjunto.pop()
    vertex_cover_rec(grafo, vertices, v+1, conjunto, min_conjunto)

def es_compatible(grafo, conjunto):
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v not in conjunto and w not in conjunto:
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

print(vertex_cover_min(grafo))