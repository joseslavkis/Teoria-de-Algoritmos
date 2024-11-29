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