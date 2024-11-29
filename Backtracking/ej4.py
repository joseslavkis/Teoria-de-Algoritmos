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