def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    solucion_optima = set(vertices)
    solucion_parcial = set()
    return list(dominating_set_rec(grafo, vertices, 0, solucion_parcial, solucion_optima))

def dominating_set_rec(grafo, vertices, index, solucion_parcial, solucion_optima):
    if len(solucion_parcial) >= len(solucion_optima):
        return solucion_optima

    if index == len(vertices):
        if es_dominating_set(grafo, solucion_parcial):
            if len(solucion_parcial) < len(solucion_optima):
                solucion_optima = set(solucion_parcial)
        return solucion_optima

    solucion_optima = dominating_set_rec(grafo, vertices, index + 1, solucion_parcial, solucion_optima)

    v = vertices[index]
    solucion_parcial.add(v)
    solucion_optima = dominating_set_rec(grafo, vertices, index + 1, solucion_parcial, solucion_optima)
    solucion_parcial.remove(v)

    return solucion_optima

def es_dominating_set(grafo, solucion_parcial):
    vertices = grafo.obtener_vertices()
    for v in vertices:
        if v not in solucion_parcial and not any(u in solucion_parcial for u in grafo.adyacentes(v)):
            return False
    return True