def es_compatible(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w:
                continue
            if grafo.estan_unidos(v,w):
                return False
    return True

def no_adyacentes_rec(grafo, vertices, vertice_actual, puestos, n):
    if len(puestos) == n:
        return es_compatible(grafo, puestos)
    if vertice_actual == len(grafo):
        return False

    if not es_compatible(grafo, puestos):
        return False

    puestos.append(vertices[vertice_actual])
    if no_adyacentes_rec(grafo, vertices, vertice_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[vertice_actual])
    return no_adyacentes_rec(grafo, vertices, vertice_actual + 1, puestos, n)

def no_adyacentes(grafo, n):
    puestos = []
    vertices = grafo.obtener_vertices()
    resultado = no_adyacentes_rec(grafo, vertices, 0, puestos, n)
    if resultado:
        return puestos
    else:
        return None